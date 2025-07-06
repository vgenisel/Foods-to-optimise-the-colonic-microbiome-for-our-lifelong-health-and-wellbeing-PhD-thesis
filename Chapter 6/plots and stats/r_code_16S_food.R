library(phyloseq)
library(microViz)
library(microbiome)
library(ANCOMBC)
library(ggplot2)
library(dplyr)
library(data.table)
library(patchwork)
library(vegan)
library(tidyverse)
library(FSA)
library(DT)

#Creating phyloseq object
ASV_table <- read.csv("C:/Users/vgenisel/OneDrive - Massey University/Desktop/16S_sequencing/plots and stats/ASV_table.csv", header=TRUE)
taxa_table <- read.csv("C:/Users/vgenisel/OneDrive - Massey University/Desktop/16S_sequencing/plots and stats/taxatable.csv", header=TRUE)
metadata <- read.csv("C:/Users/vgenisel/OneDrive - Massey University/Desktop/16S_sequencing/plots and stats/metadata.csv", header=TRUE)

# Convert ASV table to matrix
ASV_matrix <- as.matrix(ASV_table[, -1])
rownames(ASV_matrix) <- ASV_table$X
# Convert taxa table to matrix
taxa_matrix <- as.matrix(taxa_table[, -1])
rownames(taxa_matrix) <- taxa_table$X
# Convert metadata to data frame
metadata_df <- as.data.frame(metadata)
rownames(metadata_df) <- metadata$Sample

ps <- phyloseq(otu_table(ASV_matrix, taxa_are_rows=FALSE), 
               sample_data(metadata_df), 
               tax_table(taxa_matrix))

# Veryfing and fixing the data
phyloseq_validate(ps) # no messages or warnings means no detected problems
# here we observe a few NAs in the taxa_table. Also that a lot of ASVs have low counts and are present in just a few samples
ps_fixed <- tax_fix(ps) #replaces NAs with info from a higher taxonomic rank

#Subseting for only food alone and taking time zero as control
ps_food <- ps_fixed %>%
  ps_filter(Category %in% c("food_alone"), .keep_all_taxa = TRUE)

#Alpha-diversity 
alpha_div <- estimate_richness(ps_food, measures = c("Shannon", "Simpson", "Chao1"))

alpha_food <- plot_richness(ps_food, x = "Description", color="Description", measures = c("Shannon", "Simpson", "Chao1")) +
  geom_point(size = 1.5) + theme_bw() +
  theme(legend.position = "none", 
        axis.text.x = element_text(angle = 90, vjust = 0.5, hjust = 1, size = 10),  # Increase size of x-axis text
        axis.text.y = element_text(size = 11),
        axis.title.x = element_text(size = 12, face = "bold"),  # Make x-axis title bold
        axis.title.y = element_text(size = 12, face = "bold")) +
  geom_boxplot()
print(alpha_food)

alpha_div$Sample <- rownames(alpha_div)
alpha_div <- merge(alpha_div, metadata_df, by.x = "Sample", by.y = "row.names")

#Kruskal test to check if there are differences between >2 groups
kruskal.test(Shannon ~ Description, data = alpha_div)#p-value <0.05
kruskal.test(Simpson ~ Description, data = alpha_div) #p-value <0.05
kruskal.test(Chao1 ~ Description, data = alpha_div)

# Dunn's test for pairwise comparisons, corrected by BH method
sample_data(ps_food)$Description <- as.factor(sample_data(ps_food)$Description)
dunn_simpson <- dunnTest(alpha_div$Simpson ~ sample_data(ps_food)$Description, method = "bh")
table_simpson <- dunn_simpson$res %>%
  as.data.frame() %>%
  select(Comparison, P.adj = "P.adj") %>%
  separate(Comparison, into = c("group1", "group2"), sep = " - ") %>%
  na.omit()%>%
  filter(P.adj < 0.10)

dunn_shannon <- dunnTest(alpha_div$Shannon ~ sample_data(ps_food)$Description, method = "bh")
table_shannon <- dunn_shannon$res %>%
  as.data.frame() %>%
  select(Comparison, P.adj = "P.adj") %>%
  separate(Comparison, into = c("group1", "group2"), sep = " - ") %>%
  na.omit()%>%
  filter(P.adj < 0.10)

#Rarefaction or not?
sample_sums(ps_food) #to check number of reads per sample
set.seed(111) # keep result reproductive
ps_rarefied = rarefy_even_depth(ps_food, sample.size = 49433, rngseed = 123) #rarefying to the minimal value of reads

#Beta-diversity
#Bray-curtis ordination
dist = phyloseq::distance(ps_rarefied, method="bray")
ordination = ordinate(ps_rarefied, method="PCoA", distance=dist)
colors_14 <- c("#1f78b4", "#33a02c", "#e31a1c", "#ff7f00", 
               "#6a3d9a", "#b15928", "#a6cee3", "#b2df8a", 
               "#fb9a99", "#fdbf6f", "#cab2d6", "#bc80bd", 
               "#999999", "#333333", "#8c564b")
plot_ordination(ps_rarefied, ordination, color="Description") + 
  geom_point(size=4) +  # Increase point size and add different shapes
  scale_color_manual(values = colors_14) +  # Use the custom palette for colors
  theme_classic() +
  theme(strip.background = element_blank()) +
  labs(title = "PCoA of Bray-Curtis Dissimilarity") 

#adonis - PERMANOVA
metadata_food <- data.frame(sample_data(ps_rarefied))
adonis_food <- adonis2(dist ~ Description, data = metadata_food, permutations = 9999) #p-value <0.05

#Pairwise PERMANOVA
cbn <- combn(x = unique(metadata_food$Description), m = 2)
p_values <- c()
comparisons <- c()

for(i in 1:ncol(cbn)){
  ps.subs <- subset_samples(ps_rarefied, Description %in% cbn[, i])
  metadata_sub <- data.frame(sample_data(ps.subs))
    dist_sub <- phyloseq::distance(ps.subs, method = "bray")
    permanova_pairwise <- adonis2(dist_sub ~ Description, data = metadata_sub, permutations = 9999)
    p_values <- c(p_values, permanova_pairwise$`Pr(>F)`[1])
    comparisons <- c(comparisons, paste(cbn[, i], collapse = " vs "))
}

adjusted_p_values <- p.adjust(p_values, method = "BH")
results_beta_div <- data.frame(Comparison = comparisons,P_Value = p_values,Adjusted_P_Value = adjusted_p_values)

#Transforming data into relative abundances, collapsing into higher rank, and filtering rare abundant taxa
ps_transformed <- ps_food %>%
    tax_transform(trans = "compositional", rank = "Genus") %>%
    tax_filter(min_prevalence=0.05, min_sample_abundance = 0.0005)
   #Filtering to taxa present in at least 10% samples with more than 0.05% relative abundance

#Table of relative abundances
ps_agg <- ps_transformed %>%
  phyloseq::merge_samples(group = "Description") # Aggregating the samples by the grouping variable (e.g., "Description")
ps_agg_normalized <- phyloseq::transform_sample_counts(ps_agg, function(x) x / sum(x))

# Extract the original relative abundance data before merging
otu_table_raw <- ps_transformed %>%
  phyloseq::otu_table() %>%
  as.data.frame()
# Add sample metadata to keep track of sample replicates
sample_data_raw <- ps_transformed %>%
  phyloseq::sample_data() %>%
  as.data.frame()
# Combine OTU data with sample metadata
combined_data_raw <- cbind(sample_data_raw, otu_table_raw)
# Identify the column names for taxa relative abundances
taxa_columns <- names(otu_table_raw)
# Compute mean and standard deviation for each taxon by sample group
agg_stats <- combined_data_raw %>%
  group_by(Description) %>%  # Replace 'Description' with your grouping variable
  summarize(across(all_of(taxa_columns), list(mean = ~mean(.), sd = ~sd(.)), .names = "{col}_{fn}"))

write.csv(agg_stats, "relative_abundance_with_variation_food_genus.csv")

#Plotting the composition
ps_transformed %>%
    phyloseq::merge_samples(group = "Description") %>%
    comp_barplot(tax_level = "Genus", n_taxa = 15, merge_other = TRUE) +
    coord_flip() + labs(x = NULL, y = "Relative abundance") +
  theme(
    axis.ticks.y = element_blank(), 
    strip.text = element_text(face = "bold"), 
    axis.text.y = element_text(size = 12),  # y-axis title
    axis.title.x = element_text(size = 14),  # x-axis title
    axis.text.x = element_text(size = 12),  # x-axis title
    plot.title = element_text(size = 16, face = "bold"),    # plot title
    legend.title = element_text(size = 12),  # legend title
    legend.text = element_text(size = 10)    # legend text
  )

#Differential abundance testing using ANCOM-BC2
tse = mia::makeTreeSummarizedExperimentFromPhyloseq(ps_food)
tse$Description <- factor(tse$Description)
tse$Description = relevel(tse$Description, ref = "Blackcurrant")

set.seed(123)
contrast_matrix <- diag(13)  # Create a 13x13 identity matrix
output = ancombc2(data = tse, assay_name = "counts", tax_level = "Phylum",
                  fix_formula = "Description", rand_formula = NULL,
                  p_adj_method = "holm", pseudo_sens = TRUE,
                  prv_cut = 0.05, lib_cut = 1000, s0_perc = 0.05,
                  group = "Description", struc_zero = TRUE, neg_lb = TRUE,
                  alpha = 0.05, n_cl = 2, verbose = TRUE,
                  global = TRUE, pairwise = TRUE, dunnet = TRUE, trend = TRUE,
                  iter_control = list(tol = 1e-2, max_iter = 20, 
                                      verbose = TRUE),
                  em_control = list(tol = 1e-5, max_iter = 100),
                  lme_control = lme4::lmerControl(),
                  mdfdr_control = list(fwer_ctrl_method = "holm", B = 100),
                  trend_control = list(
                    contrast = list(contrast_matrix),  # Use the 13x13 contrast matrix
                    node = list(rep(1, 13)),  # Adjust nodes accordingly
                    solver = "ECOS",
                    B = 10))

#Primary analyses
res_prim = output$res
#Global test
res_global = output$res_global
write.csv(res_global, file = "ancombc2_global_food_genus.csv", row.names = FALSE)
#multiple pairwise comparisons
res_pair = output$res_pair

#multiple pairwise comparisons against a pre-specified group (Dunnett’s type of test)
res_dunn = output$res_dunn
write.csv(res_dunn, file = "ancombc2_dunn_blakcurrant_genus.csv", row.names = FALSE)

# Filter and transform the data for comparison with Blackcurrant
df_fig_dunn1 = res_dunn %>%
  dplyr::filter(diff_DescriptionBlack_beans == 1 |
                  diff_DescriptionChickpea == 1 |
                  diff_DescriptionCouscous == 1 |
                  diff_DescriptionInfant_formula == 1 |
                  diff_DescriptionKumara_peeled == 1 |
                  diff_DescriptionKumara_with_skin == 1 |
                  diff_DescriptionPork == 1 |
                  diff_DescriptionPrawn == 1 |
                  diff_DescriptionPumpkin == 1 |
                  diff_DescriptionRaspberries == 1 |
                  diff_DescriptionSoybean== 1 |
                  diff_DescriptionStrawberries== 1 |
                  diff_DescriptionYellow_peas == 1 ) %>%
  dplyr::mutate(lfc1 = ifelse(diff_DescriptionBlack_beans == 1, round(lfc_DescriptionBlack_beans, 2), 0),
                lfc2 = ifelse(diff_DescriptionChickpea == 1, round(lfc_DescriptionChickpea, 2), 0),
                lfc3 = ifelse(diff_DescriptionCouscous == 1, round(lfc_DescriptionCouscous, 2), 0),
                lfc4 = ifelse(diff_DescriptionInfant_formula == 1, round(lfc_DescriptionInfant_formula, 2), 0),
                lfc5 = ifelse(diff_DescriptionKumara_peeled == 1, round(lfc_DescriptionKumara_peeled, 2), 0),
                lfc6 = ifelse(diff_DescriptionKumara_with_skin == 1, round(lfc_DescriptionKumara_with_skin, 2), 0),
                lfc7 = ifelse(diff_DescriptionPork == 1, round(lfc_DescriptionPork, 2), 0),
                lfc8 = ifelse(diff_DescriptionPrawn == 1, round(lfc_DescriptionPrawn, 2), 0),
                lfc9 = ifelse(diff_DescriptionPumpkin == 1, round(lfc_DescriptionPumpkin, 2), 0),
                lfc10 = ifelse(diff_DescriptionRaspberries == 1, round(lfc_DescriptionRaspberries, 2), 0),
                lfc11 = ifelse(diff_DescriptionSoybean== 1, round(lfc_DescriptionSoybean, 2), 0),
                lfc12 = ifelse(diff_DescriptionStrawberries== 1, round(lfc_DescriptionStrawberries, 2), 0),
                lfc13 = ifelse(diff_DescriptionYellow_peas == 1, round(lfc_DescriptionYellow_peas, 2), 0)) %>%
  tidyr::pivot_longer(cols = lfc1:lfc13, 
                      names_to = "group", values_to = "value") %>%
  dplyr::arrange(taxon)
df_fig_dunn2 = res_dunn %>%
  dplyr::filter(diff_DescriptionBlack_beans == 1 |  diff_DescriptionChickpea == 1 | 
                  diff_DescriptionCouscous == 1 | diff_DescriptionInfant_formula == 1 | 
                  diff_DescriptionKumara_peeled == 1 | diff_DescriptionKumara_with_skin == 1 |
                  diff_DescriptionPork == 1 | 
                  diff_DescriptionPrawn == 1 | diff_DescriptionPumpkin == 1 | 
                  diff_DescriptionRaspberries == 1 | 
                  diff_DescriptionSoybean== 1 | diff_DescriptionStrawberries == 1 |
                  diff_DescriptionYellow_peas == 1) %>%
  dplyr::mutate(lfc1 = ifelse(passed_ss_DescriptionBlack_beans == 1 & diff_DescriptionBlack_beans == 1, 
                              "aquamarine3", "black"),
                lfc2 = ifelse(passed_ss_DescriptionChickpea == 1 & diff_DescriptionChickpea == 1, 
                              "aquamarine3", "black"),
                lfc3 = ifelse(passed_ss_DescriptionCouscous == 1 & diff_DescriptionCouscous == 1,"aquamarine3", "black"),
                lfc4 = ifelse(passed_ss_DescriptionInfant_formula == 1 & diff_DescriptionInfant_formula == 1,"aquamarine3", "black"),
                lfc5 = ifelse(passed_ss_DescriptionKumara_peeled == 1 & diff_DescriptionKumara_peeled == 1,"aquamarine3", "black"),
                lfc6 = ifelse(passed_ss_DescriptionKumara_with_skin == 1 & diff_DescriptionKumara_with_skin == 1, 
                              "aquamarine3", "black"),
                lfc7 = ifelse(passed_ss_DescriptionPork == 1 & diff_DescriptionPork == 1,"aquamarine3", "black"),
                lfc8 = ifelse(passed_ss_DescriptionPrawn == 1 & diff_DescriptionPrawn == 1,"aquamarine3", "black"),
                lfc9 = ifelse(passed_ss_DescriptionPumpkin == 1 & diff_DescriptionPumpkin == 1,"aquamarine3", "black"),
                lfc10 = ifelse(passed_ss_DescriptionRaspberries == 1 & diff_DescriptionRaspberries == 1,"aquamarine3", "black"),
                lfc11 = ifelse(passed_ss_DescriptionSoybean== 1 & diff_DescriptionSoybean== 1,"aquamarine3", "black"),
                lfc12 = ifelse(passed_ss_DescriptionStrawberries== 1 & diff_DescriptionStrawberries== 1,"aquamarine3", "black"),
                lfc13 = ifelse(passed_ss_DescriptionYellow_peas == 1 & diff_DescriptionYellow_peas == 1, 
                               "aquamarine3", "black")) %>%
  tidyr::pivot_longer(cols = lfc1:lfc13, 
                      names_to = "group", values_to = "color") %>%
  dplyr::arrange(taxon)

df_fig_dunn = df_fig_dunn1 %>%
  dplyr::left_join(df_fig_dunn2, by = c("taxon", "group"))

# Recode the group names to be more descriptive
df_fig_dunn$group = recode(df_fig_dunn$group, 
                           lfc1 = "Blackcurrant vs Black_beans",
                           lfc2 = "Blackcurrant vs Chickpea",
                           lfc3 = "Blackcurrant vs Couscous",
                           lfc4 = "Blackcurrant vs Infant_formula",
                           lfc5 = "Blackcurrant vs Kumara_peeled",
                           lfc6 = "Blackcurrant vs Kumara_with_skin",
                           lfc7 = "Blackcurrant vs Pork",
                           lfc8 = "Blackcurrant vs Prawn",
                           lfc9 = "Blackcurrant vs Pumpkin",
                           lfc10 = "Blackcurrant vs Raspberries",
                           lfc11 = "Blackcurrant vs Soybean",
                           lfc12 = "Blackcurrant vs Strawberries",
                           lfc13 = "Blackcurrant vs Yellow_peas")
df_fig_dunn$group = factor(df_fig_dunn$group, 
                           levels = c("Blackcurrant vs Black_beans",
                                      "Blackcurrant vs Chickpea",
                                      "Blackcurrant vs Couscous",
                                      "Blackcurrant vs Infant_formula",
                                      "Blackcurrant vs Kumara_peeled",
                                      "Blackcurrant vs Kumara_with_skin",
                                      "Blackcurrant vs Pork",
                                      "Blackcurrant vs Prawn",
                                      "Blackcurrant vs Pumpkin",
                                      "Blackcurrant vs Raspberries",
                                      "Blackcurrant vs Soybean",
                                      "Blackcurrant vs Strawberries",
                                      "Blackcurrant vs Yellow_peas"))
df_fig_dunn$group = str_replace(df_fig_dunn$group, "Blackcurrant vs ", "")

# Define the range for the color scale
lo = floor(min(df_fig_dunn$value))
up = ceiling(max(df_fig_dunn$value))
mid = (lo + up)/2

# Create the heatmap plot
fig_dunn = df_fig_dunn %>%
  ggplot(aes(x = group, y = taxon, fill = value)) + 
  geom_tile(color = "black") +
  scale_fill_gradient2(low = "blue", high = "red", mid = "white", 
                       na.value = "aquamarine3", midpoint = 0, limit = c(lo, up),
                       name = NULL) +
  geom_text(aes(group, taxon, label = value, color = color), size = 4, fontface = "bold") +
  scale_color_identity(guide = FALSE) +
  labs(x = NULL, y = NULL, title = "Log fold changes for blackcurrants vs other foods") +
  theme_minimal() +
  theme(plot.title = element_text(hjust = 0.5),
        axis.text.x = element_text(face = "bold", size=11, angle = 45, hjust = 1),  # Bold x-axis text
        axis.text.y = element_text(face = "bold.italic", size=11),   # Bold y-axis text
  )

# Display the plot
fig_dunn

# Modify the data to include labels for all cases and conditional text color with asterisks for significant values
df_fig_dunn <- df_fig_dunn %>%
  dplyr::mutate(
    # Create the label, add '*' to significant LFC values
    label = ifelse(color == "aquamarine3", paste0(round(value, 2), " *"), round(value, 2)),  
    text_color = ifelse(color == "aquamarine3", "white", "black")  # White for significant, black for others
  )

# Create the heatmap plot
fig_dunn = df_fig_dunn %>%
  ggplot(aes(x = group, y = taxon, fill = value)) + 
  geom_tile(color = "black") +
  scale_fill_gradient2(
    low = "blue", high = "red", mid = "white", 
    na.value = "grey50", midpoint = 0, limit = c(lo, up),
    name = NULL
  ) +
  geom_text(aes(label = label, color = text_color), size = 4, fontface = "bold") +  # Conditional text color with labels
  scale_color_identity() +  # Use defined colors without a legend
  labs(
    x = NULL, y = NULL, title = "Log fold changes for blackcurrants vs other foods"
  ) +
  theme_minimal() +
  theme(
    plot.title = element_text(hjust = 0.5),
    axis.text.x = element_text(face = "bold", size = 11, angle = 45, hjust = 1),
    axis.text.y = element_text(face = "bold.italic", size = 11)
  )

# Display the plot
fig_dunn


#Differential abundance testing using ANCOM-BC2
tse = mia::makeTreeSummarizedExperimentFromPhyloseq(ps_food)
tse$Description <- factor(tse$Description)
tse$Description = relevel(tse$Description, ref = "Raspberries")

set.seed(123)
contrast_matrix <- diag(13)  # Create a 13x13 identity matrix
output = ancombc2(data = tse, assay_name = "counts", tax_level = "Phylum",
                  fix_formula = "Description", rand_formula = NULL,
                  p_adj_method = "holm", pseudo_sens = TRUE,
                  prv_cut = 0.05, lib_cut = 1000, s0_perc = 0.05,
                  group = "Description", struc_zero = TRUE, neg_lb = TRUE,
                  alpha = 0.05, n_cl = 2, verbose = TRUE,
                  global = TRUE, pairwise = TRUE, dunnet = TRUE, trend = TRUE,
                  iter_control = list(tol = 1e-2, max_iter = 20, 
                                      verbose = TRUE),
                  em_control = list(tol = 1e-5, max_iter = 100),
                  lme_control = lme4::lmerControl(),
                  mdfdr_control = list(fwer_ctrl_method = "holm", B = 100),
                  trend_control = list(
                    contrast = list(contrast_matrix),  # Use the 13x13 contrast matrix
                    node = list(rep(1, 13)),  # Adjust nodes accordingly
                    solver = "ECOS",
                    B = 10))

#multiple pairwise comparisons against a pre-specified group (Dunnett’s type of test)
res_dunn = output$res_dunn

# Filter and transform the data for comparison with Raspberries
df_fig_dunn1 = res_dunn %>%
  dplyr::filter(diff_DescriptionBlack_beans == 1 |
                  diff_DescriptionBlackcurrant == 1 |
                  diff_DescriptionChickpea == 1 |
                  diff_DescriptionCouscous == 1 |
                  diff_DescriptionInfant_formula == 1 |
                  diff_DescriptionKumara_peeled == 1 |
                  diff_DescriptionKumara_with_skin == 1 |
                  diff_DescriptionPork == 1 |
                  diff_DescriptionPrawn == 1 |
                  diff_DescriptionPumpkin == 1 |
                  diff_DescriptionSoybean== 1 |
                  diff_DescriptionStrawberries== 1 |
                  diff_DescriptionYellow_peas == 1 ) %>%
  dplyr::mutate(lfc1 = ifelse(diff_DescriptionBlack_beans == 1, round(lfc_DescriptionBlack_beans, 2), 0),
                lfc2 = ifelse(diff_DescriptionBlackcurrant == 1, round(lfc_DescriptionBlackcurrant, 2), 0),
                lfc3 = ifelse(diff_DescriptionChickpea == 1, round(lfc_DescriptionChickpea, 2), 0),
                lfc4 = ifelse(diff_DescriptionCouscous == 1, round(lfc_DescriptionCouscous, 2), 0),
                lfc5 = ifelse(diff_DescriptionInfant_formula == 1, round(lfc_DescriptionInfant_formula, 2), 0),
                lfc6 = ifelse(diff_DescriptionKumara_peeled == 1, round(lfc_DescriptionKumara_peeled, 2), 0),
                lfc7 = ifelse(diff_DescriptionKumara_with_skin == 1, round(lfc_DescriptionKumara_with_skin, 2), 0),
                lfc8 = ifelse(diff_DescriptionPork == 1, round(lfc_DescriptionPork, 2), 0),
                lfc9 = ifelse(diff_DescriptionPrawn == 1, round(lfc_DescriptionPrawn, 2), 0),
                lfc10 = ifelse(diff_DescriptionPumpkin == 1, round(lfc_DescriptionPumpkin, 2), 0),
                lfc11 = ifelse(diff_DescriptionSoybean== 1, round(lfc_DescriptionSoybean, 2), 0),
                lfc12 = ifelse(diff_DescriptionStrawberries== 1, round(lfc_DescriptionStrawberries, 2), 0),
                lfc13 = ifelse(diff_DescriptionYellow_peas == 1, round(lfc_DescriptionYellow_peas, 2), 0)) %>%
  tidyr::pivot_longer(cols = lfc1:lfc13, 
                      names_to = "group", values_to = "value") %>%
  dplyr::arrange(taxon)
df_fig_dunn2 = res_dunn %>%
  dplyr::filter(diff_DescriptionBlack_beans == 1 |   diff_DescriptionBlackcurrant == 1 | diff_DescriptionChickpea == 1 | 
                  diff_DescriptionCouscous == 1 | diff_DescriptionInfant_formula == 1 | 
                  diff_DescriptionKumara_peeled == 1 | diff_DescriptionKumara_with_skin == 1 |
                  diff_DescriptionPork == 1 | 
                  diff_DescriptionPrawn == 1 | diff_DescriptionPumpkin == 1 | 
                  diff_DescriptionSoybean== 1 | diff_DescriptionStrawberries == 1 |
                  diff_DescriptionYellow_peas == 1) %>%
  dplyr::mutate(lfc1 = ifelse(passed_ss_DescriptionBlack_beans == 1 & diff_DescriptionBlack_beans == 1, 
                              "aquamarine3", "black"),
                lfc2 = ifelse(passed_ss_DescriptionBlackcurrant == 1 & diff_DescriptionBlackcurrant == 1,"aquamarine3", "black"),
                lfc3 = ifelse(passed_ss_DescriptionChickpea == 1 & diff_DescriptionChickpea == 1, 
                              "aquamarine3", "black"),
                lfc4 = ifelse(passed_ss_DescriptionCouscous == 1 & diff_DescriptionCouscous == 1,"aquamarine3", "black"),
                lfc5 = ifelse(passed_ss_DescriptionInfant_formula == 1 & diff_DescriptionInfant_formula == 1,"aquamarine3", "black"),
                lfc6 = ifelse(passed_ss_DescriptionKumara_peeled == 1 & diff_DescriptionKumara_peeled == 1,"aquamarine3", "black"),
                lfc7 = ifelse(passed_ss_DescriptionKumara_with_skin == 1 & diff_DescriptionKumara_with_skin == 1, 
                              "aquamarine3", "black"),
                lfc8 = ifelse(passed_ss_DescriptionPork == 1 & diff_DescriptionPork == 1,"aquamarine3", "black"),
                lfc9 = ifelse(passed_ss_DescriptionPrawn == 1 & diff_DescriptionPrawn == 1,"aquamarine3", "black"),
                lfc10 = ifelse(passed_ss_DescriptionPumpkin == 1 & diff_DescriptionPumpkin == 1,"aquamarine3", "black"),
                lfc11 = ifelse(passed_ss_DescriptionSoybean== 1 & diff_DescriptionSoybean== 1,"aquamarine3", "black"),
                lfc12 = ifelse(passed_ss_DescriptionStrawberries== 1 & diff_DescriptionStrawberries== 1,"aquamarine3", "black"),
                lfc13 = ifelse(passed_ss_DescriptionYellow_peas == 1 & diff_DescriptionYellow_peas == 1, 
                               "aquamarine3", "black")) %>%
  tidyr::pivot_longer(cols = lfc1:lfc13, 
                      names_to = "group", values_to = "color") %>%
  dplyr::arrange(taxon)

df_fig_dunn = df_fig_dunn1 %>%
  dplyr::left_join(df_fig_dunn2, by = c("taxon", "group"))

# Recode the group names to be more descriptive
df_fig_dunn$group = recode(df_fig_dunn$group, 
                           lfc1 = "Raspberries vs Black_beans",
                           lfc2 = "Raspberries vs Blackcurrant",
                           lfc3 = "Raspberries vs Chickpea",
                           lfc4 = "Raspberries vs Couscous",
                           lfc5 = "Raspberries vs Infant_formula",
                           lfc6 = "Raspberries vs Kumara_peeled",
                           lfc7 = "Raspberries vs Kumara_with_skin",
                           lfc8 = "Raspberries vs Pork",
                           lfc9 = "Raspberries vs Prawn",
                           lfc10 = "Raspberries vs Pumpkin",
                           lfc11 = "Raspberries vs Soybean",
                           lfc12 = "Raspberries vs Strawberries",
                           lfc13 = "Raspberries vs Yellow_peas")
df_fig_dunn$group = factor(df_fig_dunn$group, 
                           levels = c("Raspberries vs Black_beans",
                                      "Raspberries vs Blackcurrant",
                                      "Raspberries vs Chickpea",
                                      "Raspberries vs Couscous",
                                      "Raspberries vs Infant_formula",
                                      "Raspberries vs Kumara_peeled",
                                      "Raspberries vs Kumara_with_skin",
                                      "Raspberries vs Pork",
                                      "Raspberries vs Prawn",
                                      "Raspberries vs Pumpkin",
                                      "Raspberries vs Soybean",
                                      "Raspberries vs Strawberries",
                                      "Raspberries vs Yellow_peas"))
df_fig_dunn$group = str_replace(df_fig_dunn$group, "Raspberries vs ", "")

# Define the range for the color scale
lo = floor(min(df_fig_dunn$value))
up = ceiling(max(df_fig_dunn$value))
mid = (lo + up)/2

# Create the heatmap plot
fig_dunn = df_fig_dunn %>%
  ggplot(aes(x = group, y = taxon, fill = value)) + 
  geom_tile(color = "black") +
  scale_fill_gradient2(low = "blue", high = "red", mid = "white", 
                       na.value = "aquamarine3", midpoint = 0, limit = c(lo, up),
                       name = NULL) +
  geom_text(aes(group, taxon, label = value, color = color), size = 4, fontface = "bold") +
  scale_color_identity(guide = FALSE) +
  labs(x = NULL, y = NULL, title = "Log fold changes for raspberries vs other foods") +
  theme_minimal() +
  theme(plot.title = element_text(hjust = 0.5),
        axis.text.x = element_text(face = "bold", size=11, angle = 45, hjust = 1),  # Bold x-axis text
        axis.text.y = element_text(face = "bold.italic", size=11),   # Bold y-axis text
  )

# Display the plot
fig_dunn

# Modify the data to include labels for all cases and conditional text color with asterisks for significant values
df_fig_dunn <- df_fig_dunn %>%
  dplyr::mutate(
    # Create the label, add '*' to significant LFC values
    label = ifelse(color == "aquamarine3", paste0(round(value, 2), " *"), round(value, 2)),  
    text_color = ifelse(color == "aquamarine3", "white", "black")  # White for significant, black for others
  )

# Create the heatmap plot
fig_dunn = df_fig_dunn %>%
  ggplot(aes(x = group, y = taxon, fill = value)) + 
  geom_tile(color = "black") +
  scale_fill_gradient2(
    low = "blue", high = "red", mid = "white", 
    na.value = "grey50", midpoint = 0, limit = c(lo, up),
    name = NULL
  ) +
  geom_text(aes(label = label, color = text_color), size = 4, fontface = "bold") +  # Conditional text color with labels
  scale_color_identity() +  # Use defined colors without a legend
  labs(
    x = NULL, y = NULL, title = "Log fold changes for raspberries vs other foods"
  ) +
  theme_minimal() +
  theme(
    plot.title = element_text(hjust = 0.5),
    axis.text.x = element_text(face = "bold", size = 11, angle = 45, hjust = 1),
    axis.text.y = element_text(face = "bold.italic", size = 11)
  )

# Display the plot
fig_dunn

#Differential abundance testing using ANCOM-BC2
tse = mia::makeTreeSummarizedExperimentFromPhyloseq(ps_food)
tse$Description <- factor(tse$Description)
tse$Description = relevel(tse$Description, ref = "Kumara_peeled")

set.seed(123)
contrast_matrix <- diag(13)  # Create a 13x13 identity matrix
output = ancombc2(data = tse, assay_name = "counts", tax_level = "Genus",
                  fix_formula = "Description", rand_formula = NULL,
                  p_adj_method = "holm", pseudo_sens = TRUE,
                  prv_cut = 0.05, lib_cut = 1000, s0_perc = 0.05,
                  group = "Description", struc_zero = TRUE, neg_lb = TRUE,
                  alpha = 0.05, n_cl = 2, verbose = TRUE,
                  global = TRUE, pairwise = TRUE, dunnet = TRUE, trend = TRUE,
                  iter_control = list(tol = 1e-2, max_iter = 20, 
                                      verbose = TRUE),
                  em_control = list(tol = 1e-5, max_iter = 100),
                  lme_control = lme4::lmerControl(),
                  mdfdr_control = list(fwer_ctrl_method = "holm", B = 100),
                  trend_control = list(
                    contrast = list(contrast_matrix),  # Use the 13x13 contrast matrix
                    node = list(rep(1, 13)),  # Adjust nodes accordingly
                    solver = "ECOS",
                    B = 10))

#multiple pairwise comparisons against a pre-specified group (Dunnett’s type of test)
res_dunn = output$res_dunn

# Filter and transform the data for comparison with Kumara peeled
df_fig_dunn1 = res_dunn %>%
  dplyr::filter(diff_DescriptionBlack_beans == 1 |
                  diff_DescriptionBlackcurrant == 1 |
                  diff_DescriptionChickpea == 1 |
                  diff_DescriptionCouscous == 1 |
                  diff_DescriptionInfant_formula == 1 |
                  diff_DescriptionKumara_with_skin == 1 |
                  diff_DescriptionPork == 1 |
                  diff_DescriptionPrawn == 1 |
                  diff_DescriptionPumpkin == 1 |
                  diff_DescriptionRaspberries == 1 |
                  diff_DescriptionSoybean== 1 |
                  diff_DescriptionStrawberries== 1 |
                  diff_DescriptionYellow_peas == 1 ) %>%
  dplyr::mutate(lfc1 = ifelse(diff_DescriptionBlack_beans == 1, round(lfc_DescriptionBlack_beans, 2), 0),
                lfc2 = ifelse(diff_DescriptionBlackcurrant == 1, round(lfc_DescriptionBlackcurrant, 2), 0),
                lfc3 = ifelse(diff_DescriptionChickpea == 1, round(lfc_DescriptionChickpea, 2), 0),
                lfc4 = ifelse(diff_DescriptionCouscous == 1, round(lfc_DescriptionCouscous, 2), 0),
                lfc5 = ifelse(diff_DescriptionInfant_formula == 1, round(lfc_DescriptionInfant_formula, 2), 0),
                lfc6 = ifelse(diff_DescriptionKumara_with_skin == 1, round(lfc_DescriptionKumara_with_skin, 2), 0),
                lfc7 = ifelse(diff_DescriptionPork == 1, round(lfc_DescriptionPork, 2), 0),
                lfc8 = ifelse(diff_DescriptionPrawn == 1, round(lfc_DescriptionPrawn, 2), 0),
                lfc9 = ifelse(diff_DescriptionPumpkin == 1, round(lfc_DescriptionPumpkin, 2), 0),
                lfc10 = ifelse(diff_DescriptionRaspberries == 1, round(lfc_DescriptionRaspberries, 2), 0),
                lfc11 = ifelse(diff_DescriptionSoybean== 1, round(lfc_DescriptionSoybean, 2), 0),
                lfc12 = ifelse(diff_DescriptionStrawberries== 1, round(lfc_DescriptionStrawberries, 2), 0),
                lfc13 = ifelse(diff_DescriptionYellow_peas == 1, round(lfc_DescriptionYellow_peas, 2), 0)) %>%
  tidyr::pivot_longer(cols = lfc1:lfc13, 
                      names_to = "group", values_to = "value") %>%
  dplyr::arrange(taxon)
df_fig_dunn2 = res_dunn %>%
  dplyr::filter(diff_DescriptionBlack_beans == 1 |   diff_DescriptionBlackcurrant == 1 | diff_DescriptionChickpea == 1 | 
                  diff_DescriptionCouscous == 1 | diff_DescriptionInfant_formula == 1 | 
                   diff_DescriptionKumara_with_skin == 1 |
                  diff_DescriptionPork == 1 | 
                  diff_DescriptionPrawn == 1 | diff_DescriptionPumpkin == 1 | diff_DescriptionRaspberries == 1 |
                  diff_DescriptionSoybean== 1 | diff_DescriptionStrawberries == 1 |
                  diff_DescriptionYellow_peas == 1) %>%
  dplyr::mutate(lfc1 = ifelse(passed_ss_DescriptionBlack_beans == 1 & diff_DescriptionBlack_beans == 1, 
                              "aquamarine3", "black"),
                lfc2 = ifelse(passed_ss_DescriptionBlackcurrant == 1 & diff_DescriptionBlackcurrant == 1,"aquamarine3", "black"),
                lfc3 = ifelse(passed_ss_DescriptionChickpea == 1 & diff_DescriptionChickpea == 1, 
                              "aquamarine3", "black"),
                lfc4 = ifelse(passed_ss_DescriptionCouscous == 1 & diff_DescriptionCouscous == 1,"aquamarine3", "black"),
                lfc5 = ifelse(passed_ss_DescriptionInfant_formula == 1 & diff_DescriptionInfant_formula == 1,"aquamarine3", "black"),
                lfc6 = ifelse(passed_ss_DescriptionKumara_with_skin == 1 & diff_DescriptionKumara_with_skin == 1, 
                              "aquamarine3", "black"),
                lfc7 = ifelse(passed_ss_DescriptionPork == 1 & diff_DescriptionPork == 1,"aquamarine3", "black"),
                lfc8 = ifelse(passed_ss_DescriptionPrawn == 1 & diff_DescriptionPrawn == 1,"aquamarine3", "black"),
                lfc9 = ifelse(passed_ss_DescriptionPumpkin == 1 & diff_DescriptionPumpkin == 1,"aquamarine3", "black"),
                lfc10 = ifelse(passed_ss_DescriptionRaspberries == 1 & diff_DescriptionRaspberries == 1,"aquamarine3", "black"),
                lfc11 = ifelse(passed_ss_DescriptionSoybean== 1 & diff_DescriptionSoybean== 1,"aquamarine3", "black"),
                lfc12 = ifelse(passed_ss_DescriptionStrawberries== 1 & diff_DescriptionStrawberries== 1,"aquamarine3", "black"),
                lfc13 = ifelse(passed_ss_DescriptionYellow_peas == 1 & diff_DescriptionYellow_peas == 1, 
                               "aquamarine3", "black")) %>%
  tidyr::pivot_longer(cols = lfc1:lfc13, 
                      names_to = "group", values_to = "color") %>%
  dplyr::arrange(taxon)

df_fig_dunn = df_fig_dunn1 %>%
  dplyr::left_join(df_fig_dunn2, by = c("taxon", "group"))

# Recode the group names to be more descriptive
df_fig_dunn$group = recode(df_fig_dunn$group, 
                           lfc1 = "Kumara_peeled vs Black_beans",
                           lfc2 = "Kumara_peeled vs Blackcurrant",
                           lfc3 = "Kumara_peeled vs Chickpea",
                           lfc4 = "Kumara_peeled vs Couscous",
                           lfc5 = "Kumara_peeled vs Infant_formula",
                           lfc6 = "Kumara_peeled vs Kumara_with_skin",
                           lfc7 = "Kumara_peeled vs Pork",
                           lfc8 = "Kumara_peeled vs Prawn",
                           lfc9 = "Kumara_peeled vs Pumpkin",
                           lfc10 = "Kumara_peeled vs Raspberries",
                           lfc11 = "Kumara_peeled vs Soybean",
                           lfc12 = "Kumara_peeled vs Strawberries",
                           lfc13 = "Kumara_peeled vs Yellow_peas")
df_fig_dunn$group = factor(df_fig_dunn$group, 
                           levels = c("Kumara_peeled vs Black_beans",
                                      "Kumara_peeled vs Blackcurrant",
                                      "Kumara_peeled vs Chickpea",
                                      "Kumara_peeled vs Couscous",
                                      "Kumara_peeled vs Infant_formula",
                                      "Kumara_peeled vs Kumara_with_skin",
                                      "Kumara_peeled vs Pork",
                                      "Kumara_peeled vs Prawn",
                                      "Kumara_peeled vs Pumpkin",
                                      "Kumara_peeled vs Raspberries",
                                      "Kumara_peeled vs Soybean",
                                      "Kumara_peeled vs Strawberries",
                                      "Kumara_peeled vs Yellow_peas"))
df_fig_dunn$group = str_replace(df_fig_dunn$group, "Kumara_peeled vs ", "")

# Define the range for the color scale
lo = floor(min(df_fig_dunn$value))
up = ceiling(max(df_fig_dunn$value))
mid = (lo + up)/2

# Create the heatmap plot
fig_dunn = df_fig_dunn %>%
  ggplot(aes(x = group, y = taxon, fill = value)) + 
  geom_tile(color = "black") +
  scale_fill_gradient2(low = "blue", high = "red", mid = "white", 
                       na.value = "aquamarine3", midpoint = 0, limit = c(lo, up),
                       name = NULL) +
  geom_text(aes(group, taxon, label = value, color = color), size = 4, fontface = "bold") +
  scale_color_identity(guide = FALSE) +
  labs(x = NULL, y = NULL, title = "Log fold changes for Kumara peeled vs other foods") +
  theme_minimal() +
  theme(plot.title = element_text(hjust = 0.5),
        axis.text.x = element_text(face = "bold", size=11, angle = 45, hjust = 1),  # Bold x-axis text
        axis.text.y = element_text(face = "bold.italic", size=11),   # Bold y-axis text
  )

# Display the plot
fig_dunn

# Modify the data to include labels for all cases and conditional text color with asterisks for significant values
df_fig_dunn <- df_fig_dunn %>%
  dplyr::mutate(
    # Create the label, add '*' to significant LFC values
    label = ifelse(color == "aquamarine3", paste0(round(value, 2), " *"), round(value, 2)),  
    text_color = ifelse(color == "aquamarine3", "white", "black")  # White for significant, black for others
  )

# Create the heatmap plot
fig_dunn = df_fig_dunn %>%
  ggplot(aes(x = group, y = taxon, fill = value)) + 
  geom_tile(color = "black") +
  scale_fill_gradient2(
    low = "blue", high = "red", mid = "white", 
    na.value = "grey50", midpoint = 0, limit = c(lo, up),
    name = NULL
  ) +
  geom_text(aes(label = label, color = text_color), size = 4, fontface = "bold") +  # Conditional text color with labels
  scale_color_identity() +  # Use defined colors without a legend
  labs(
    x = NULL, y = NULL, title = "Log fold changes for Kumara peeled vs other foods"
  ) +
  theme_minimal() +
  theme(
    plot.title = element_text(hjust = 0.5),
    axis.text.x = element_text(face = "bold", size = 11, angle = 45, hjust = 1),
    axis.text.y = element_text(face = "bold.italic", size = 11)
  )

# Display the plot
fig_dunn

#Differential abundance testing using ANCOM-BC2
tse = mia::makeTreeSummarizedExperimentFromPhyloseq(ps_food)
tse$Description <- factor(tse$Description)
tse$Description = relevel(tse$Description, ref = "Kumara_with_skin")

set.seed(123)
contrast_matrix <- diag(13)  # Create a 13x13 identity matrix
output = ancombc2(data = tse, assay_name = "counts", tax_level = "Genus",
                  fix_formula = "Description", rand_formula = NULL,
                  p_adj_method = "holm", pseudo_sens = TRUE,
                  prv_cut = 0.05, lib_cut = 1000, s0_perc = 0.05,
                  group = "Description", struc_zero = TRUE, neg_lb = TRUE,
                  alpha = 0.05, n_cl = 2, verbose = TRUE,
                  global = TRUE, pairwise = TRUE, dunnet = TRUE, trend = TRUE,
                  iter_control = list(tol = 1e-2, max_iter = 20, 
                                      verbose = TRUE),
                  em_control = list(tol = 1e-5, max_iter = 100),
                  lme_control = lme4::lmerControl(),
                  mdfdr_control = list(fwer_ctrl_method = "holm", B = 100),
                  trend_control = list(
                    contrast = list(contrast_matrix),  # Use the 13x13 contrast matrix
                    node = list(rep(1, 13)),  # Adjust nodes accordingly
                    solver = "ECOS",
                    B = 10))

#multiple pairwise comparisons against a pre-specified group (Dunnett’s type of test)
res_dunn = output$res_dunn

# Filter and transform the data for comparison with Kumara peeled
df_fig_dunn1 = res_dunn %>%
  dplyr::filter(diff_DescriptionBlack_beans == 1 |
                  diff_DescriptionBlackcurrant == 1 |
                  diff_DescriptionChickpea == 1 |
                  diff_DescriptionCouscous == 1 |
                  diff_DescriptionInfant_formula == 1 |
                  diff_DescriptionKumara_peeled == 1 |
                  diff_DescriptionPork == 1 |
                  diff_DescriptionPrawn == 1 |
                  diff_DescriptionPumpkin == 1 |
                  diff_DescriptionRaspberries == 1 |
                  diff_DescriptionSoybean== 1 |
                  diff_DescriptionStrawberries== 1 |
                  diff_DescriptionYellow_peas == 1 ) %>%
  dplyr::mutate(lfc1 = ifelse(diff_DescriptionBlack_beans == 1, round(lfc_DescriptionBlack_beans, 2), 0),
                lfc2 = ifelse(diff_DescriptionBlackcurrant == 1, round(lfc_DescriptionBlackcurrant, 2), 0),
                lfc3 = ifelse(diff_DescriptionChickpea == 1, round(lfc_DescriptionChickpea, 2), 0),
                lfc4 = ifelse(diff_DescriptionCouscous == 1, round(lfc_DescriptionCouscous, 2), 0),
                lfc5 = ifelse(diff_DescriptionInfant_formula == 1, round(lfc_DescriptionInfant_formula, 2), 0),
                lfc6 = ifelse(diff_DescriptionKumara_peeled == 1, round(lfc_DescriptionKumara_peeled, 2), 0),
                lfc7 = ifelse(diff_DescriptionPork == 1, round(lfc_DescriptionPork, 2), 0),
                lfc8 = ifelse(diff_DescriptionPrawn == 1, round(lfc_DescriptionPrawn, 2), 0),
                lfc9 = ifelse(diff_DescriptionPumpkin == 1, round(lfc_DescriptionPumpkin, 2), 0),
                lfc10 = ifelse(diff_DescriptionRaspberries == 1, round(lfc_DescriptionRaspberries, 2), 0),
                lfc11 = ifelse(diff_DescriptionSoybean== 1, round(lfc_DescriptionSoybean, 2), 0),
                lfc12 = ifelse(diff_DescriptionStrawberries== 1, round(lfc_DescriptionStrawberries, 2), 0),
                lfc13 = ifelse(diff_DescriptionYellow_peas == 1, round(lfc_DescriptionYellow_peas, 2), 0)) %>%
  tidyr::pivot_longer(cols = lfc1:lfc13, 
                      names_to = "group", values_to = "value") %>%
  dplyr::arrange(taxon)
df_fig_dunn2 = res_dunn %>%
  dplyr::filter(diff_DescriptionBlack_beans == 1 |   diff_DescriptionBlackcurrant == 1 | diff_DescriptionChickpea == 1 | 
                  diff_DescriptionCouscous == 1 | diff_DescriptionInfant_formula == 1 | 
                  diff_DescriptionKumara_peeled == 1 |
                  diff_DescriptionPork == 1 | 
                  diff_DescriptionPrawn == 1 | diff_DescriptionPumpkin == 1 | diff_DescriptionRaspberries == 1 |
                  diff_DescriptionSoybean== 1 | diff_DescriptionStrawberries == 1 |
                  diff_DescriptionYellow_peas == 1) %>%
  dplyr::mutate(lfc1 = ifelse(passed_ss_DescriptionBlack_beans == 1 & diff_DescriptionBlack_beans == 1, 
                              "aquamarine3", "black"),
                lfc2 = ifelse(passed_ss_DescriptionBlackcurrant == 1 & diff_DescriptionBlackcurrant == 1,"aquamarine3", "black"),
                lfc3 = ifelse(passed_ss_DescriptionChickpea == 1 & diff_DescriptionChickpea == 1, 
                              "aquamarine3", "black"),
                lfc4 = ifelse(passed_ss_DescriptionCouscous == 1 & diff_DescriptionCouscous == 1,"aquamarine3", "black"),
                lfc5 = ifelse(passed_ss_DescriptionInfant_formula == 1 & diff_DescriptionInfant_formula == 1,"aquamarine3", "black"),
                lfc6 = ifelse(passed_ss_DescriptionKumara_peeled == 1 & diff_DescriptionKumara_peeled == 1, 
                              "aquamarine3", "black"),
                lfc7 = ifelse(passed_ss_DescriptionPork == 1 & diff_DescriptionPork == 1,"aquamarine3", "black"),
                lfc8 = ifelse(passed_ss_DescriptionPrawn == 1 & diff_DescriptionPrawn == 1,"aquamarine3", "black"),
                lfc9 = ifelse(passed_ss_DescriptionPumpkin == 1 & diff_DescriptionPumpkin == 1,"aquamarine3", "black"),
                lfc10 = ifelse(passed_ss_DescriptionRaspberries == 1 & diff_DescriptionRaspberries == 1,"aquamarine3", "black"),
                lfc11 = ifelse(passed_ss_DescriptionSoybean== 1 & diff_DescriptionSoybean== 1,"aquamarine3", "black"),
                lfc12 = ifelse(passed_ss_DescriptionStrawberries== 1 & diff_DescriptionStrawberries== 1,"aquamarine3", "black"),
                lfc13 = ifelse(passed_ss_DescriptionYellow_peas == 1 & diff_DescriptionYellow_peas == 1, 
                               "aquamarine3", "black")) %>%
  tidyr::pivot_longer(cols = lfc1:lfc13, 
                      names_to = "group", values_to = "color") %>%
  dplyr::arrange(taxon)

df_fig_dunn = df_fig_dunn1 %>%
  dplyr::left_join(df_fig_dunn2, by = c("taxon", "group"))

# Recode the group names to be more descriptive
df_fig_dunn$group = recode(df_fig_dunn$group, 
                           lfc1 = "Kumara_with_skin vs Black_beans",
                           lfc2 = "Kumara_with_skin vs Blackcurrant",
                           lfc3 = "Kumara_with_skin vs Chickpea",
                           lfc4 = "Kumara_with_skin vs Couscous",
                           lfc5 = "Kumara_with_skin vs Infant_formula",
                           lfc6 = "Kumara_with_skin vs Kumara_peeled",
                           lfc7 = "Kumara_with_skin vs Pork",
                           lfc8 = "Kumara_with_skin vs Prawn",
                           lfc9 = "Kumara_with_skin vs Pumpkin",
                           lfc10 = "Kumara_with_skin vs Raspberries",
                           lfc11 = "Kumara_with_skin vs Soybean",
                           lfc12 = "Kumara_with_skin vs Strawberries",
                           lfc13 = "Kumara_with_skin vs Yellow_peas")
df_fig_dunn$group = factor(df_fig_dunn$group, 
                           levels = c("Kumara_with_skin vs Black_beans",
                                      "Kumara_with_skin vs Blackcurrant",
                                      "Kumara_with_skin vs Chickpea",
                                      "Kumara_with_skin vs Couscous",
                                      "Kumara_with_skin vs Infant_formula",
                                      "Kumara_with_skin vs Kumara_peeled",
                                      "Kumara_with_skin vs Pork",
                                      "Kumara_with_skin vs Prawn",
                                      "Kumara_with_skin vs Pumpkin",
                                      "Kumara_with_skin vs Raspberries",
                                      "Kumara_with_skin vs Soybean",
                                      "Kumara_with_skin vs Strawberries",
                                      "Kumara_with_skin vs Yellow_peas"))
df_fig_dunn$group = str_replace(df_fig_dunn$group, "Kumara_with_skin vs ", "")

# Modify the data to include labels for all cases and conditional text color with asterisks for significant values
df_fig_dunn <- df_fig_dunn %>%
  dplyr::mutate(
    # Create the label, add '*' to significant LFC values
    label = ifelse(color == "aquamarine3", paste0(round(value, 2), " *"), round(value, 2)),  
    text_color = ifelse(color == "aquamarine3", "white", "black")  # White for significant, black for others
  )

# Define the range for the color scale
lo = floor(min(df_fig_dunn$value))
up = ceiling(max(df_fig_dunn$value))
mid = (lo + up)/2

# Create the heatmap plot
fig_dunn = df_fig_dunn %>%
  ggplot(aes(x = group, y = taxon, fill = value)) + 
  geom_tile(color = "black") +
  scale_fill_gradient2(
    low = "blue", high = "red", mid = "white", 
    na.value = "grey50", midpoint = 0, limit = c(lo, up),
    name = NULL
  ) +
  geom_text(aes(label = label, color = text_color), size = 4, fontface = "bold") +  # Conditional text color with labels
  scale_color_identity() +  # Use defined colors without a legend
  labs(
    x = NULL, y = NULL, title = "Log fold changes for kumara with skin vs other foods"
  ) +
  theme_minimal() +
  theme(
    plot.title = element_text(hjust = 0.5),
    axis.text.x = element_text(face = "bold", size = 11, angle = 45, hjust = 1),
    axis.text.y = element_text(face = "bold.italic", size = 11)
  )

# Display the plot
fig_dunn




