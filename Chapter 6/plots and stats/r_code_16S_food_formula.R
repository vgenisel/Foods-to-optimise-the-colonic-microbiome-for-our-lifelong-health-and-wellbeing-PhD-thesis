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
ps_food_formula <- ps_fixed %>%
  ps_filter(Category %in% c("food_and_formula"), .keep_all_taxa = TRUE)

#Alpha-diversity 
alpha_div <- estimate_richness(ps_food_formula, measures = c("Shannon", "Simpson", "Chao1"))

alpha_food <- plot_richness(ps_food_formula, x = "Description", color="Description", measures = c("Shannon", "Simpson", "Chao1")) +
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
kruskal.test(Shannon ~ Description, data = alpha_div)
kruskal.test(Simpson ~ Description, data = alpha_div)
kruskal.test(Chao1 ~ Description, data = alpha_div)

#Rarefaction or not?
sample_sums(ps_food_formula) #to check number of reads per sample
set.seed(111) # keep result reproductive
ps_rarefied = rarefy_even_depth(ps_food_formula, sample.size = 76514, rngseed = 123) #rarefying to the minimal value of reads

#Beta-diversity
#Bray-curtis ordination
dist = phyloseq::distance(ps_rarefied, method="bray")
ordination = ordinate(ps_rarefied, method="PCoA", distance=dist)
colors_14 <- c("#1f78b4", "#33a02c", "#e31a1c", "#ff7f00", 
               "#6a3d9a", "#b15928", "#a6cee3", "#b2df8a", 
               "#fb9a99", "#fdbf6f", "#cab2d6", "#bc80bd", 
               "#999999", "#333333")
plot_ordination(ps_rarefied, ordination, color="Description") + 
  geom_point(size=4) +  # Increase point size and add different shapes
  scale_color_manual(values = colors_14) +  # Use the custom palette for colors
  theme_classic() +
  theme(strip.background = element_blank()) +
  labs(title = "PCoA of Bray-Curtis Dissimilarity") 

#adonis - PERMANOVA
metadata_food <- data.frame(sample_data(ps_rarefied))
adonis_food <- adonis2(dist ~ Description, data = metadata_food, permutations = 9999) #p-value >0.05

#Transforming data into relative abundances, collapsing into higher rank, and filtering rare abundant taxa
ps_transformed <- ps_food_formula %>%
    tax_transform(trans = "compositional", rank = "Genus") %>%
    tax_filter(min_prevalence=0.1, min_sample_abundance = 0.0005) #Filtering to taxa present in at least 10% samples with more than 0.05% relative abundance

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

write.csv(agg_stats, "relative_abundance_with_variation_food_formula_genus.csv")

#Plotting the composition
ps_transformed %>%
    phyloseq::merge_samples(group = "Description") %>%
    comp_barplot(tax_level = "Family", n_taxa = 15, merge_other = TRUE) +
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
tse = mia::makeTreeSummarizedExperimentFromPhyloseq(ps_food_formula)
tse$Description <- factor(tse$Description)
tse$Description = relevel(tse$Description, ref = "Black_beans_and_formula")

set.seed(123)
contrast_matrix <- diag(12)  # Create a 12x12 identity matrix
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
                    contrast = list(contrast_matrix),  # Use the 12x12 contrast matrix
                    node = list(rep(1, 12)),  # Adjust nodes accordingly
                    solver = "ECOS",
                    B = 10))

#Global test
res_global = output$res_global
write.csv(res_global, file = "ancombc2_global_food_formula_genus.csv", row.names = FALSE)

#multiple pairwise comparisons against a pre-specified group (Dunnett’s type of test)
res_dunn = output$res_dunn
write.csv(res_dunn, file = "ancombc2_dunn_black_beans_formula_genus.csv", row.names = FALSE)

# Filter and transform the data for comparison with Black beans and formula
df_fig_dunn1 = res_dunn %>%
  dplyr::filter(diff_DescriptionBlackcurrant_and_formula == 1 |
                  diff_DescriptionChickpea_and_formula == 1 |
                  diff_DescriptionCouscous_and_formula == 1 |
                  diff_DescriptionKumara_peeled_and_formula == 1 |
                  diff_DescriptionKumara_with_skin_and_formula == 1 |
                  diff_DescriptionPork_and_formula == 1 |
                  diff_DescriptionPrawn_and_formula == 1 |
                  diff_DescriptionPumpkin_and_formula == 1 |
                  diff_DescriptionRaspberries_and_formula == 1 |
                  diff_DescriptionSoybean_and_formula == 1 |
                  diff_DescriptionStrawberries_and_formula == 1 |
                  diff_DescriptionYellow_peas_and_formula == 1 ) %>%
  dplyr::mutate(lfc1 = ifelse(diff_DescriptionBlackcurrant_and_formula == 1, round(lfc_DescriptionBlackcurrant_and_formula, 2), 0),
                lfc2 = ifelse(diff_DescriptionChickpea_and_formula == 1, round(lfc_DescriptionChickpea_and_formula, 2), 0),
                lfc3 = ifelse(diff_DescriptionCouscous_and_formula == 1, round(lfc_DescriptionCouscous_and_formula, 2), 0),
                lfc4 = ifelse(diff_DescriptionKumara_peeled_and_formula == 1, round(lfc_DescriptionKumara_peeled_and_formula, 2), 0),
                lfc5 = ifelse(diff_DescriptionKumara_with_skin_and_formula == 1, round(lfc_DescriptionKumara_with_skin_and_formula, 2), 0),
                lfc6 = ifelse(diff_DescriptionPork_and_formula == 1, round(lfc_DescriptionPork_and_formula, 2), 0),
                lfc7 = ifelse(diff_DescriptionPrawn_and_formula == 1, round(lfc_DescriptionPrawn_and_formula, 2), 0),
                lfc8 = ifelse(diff_DescriptionPumpkin_and_formula == 1, round(lfc_DescriptionPumpkin_and_formula, 2), 0),
                lfc9 = ifelse(diff_DescriptionRaspberries_and_formula == 1, round(lfc_DescriptionRaspberries_and_formulan, 2), 0),
                lfc10 = ifelse(diff_DescriptionSoybean_and_formula == 1, round(lfc_DescriptionSoybean_and_formula, 2), 0),
                lfc11 = ifelse(diff_DescriptionStrawberries_and_formula == 1, round(lfc_DescriptionStrawberries_and_formula, 2), 0),
                lfc12 = ifelse(diff_DescriptionYellow_peas_and_formula == 1, round(lfc_DescriptionYellow_peas_and_formula, 2), 0)) %>%
  tidyr::pivot_longer(cols = lfc1:lfc12, 
                      names_to = "group", values_to = "value") %>%
  dplyr::arrange(taxon)

df_fig_dunn2 = res_dunn %>%
  dplyr::filter(diff_DescriptionBlackcurrant_and_formula == 1 | diff_DescriptionChickpea_and_formula == 1 | 
                  diff_DescriptionCouscous_and_formula == 1 | diff_DescriptionKumara_peeled_and_formula == 1 | 
                  diff_DescriptionKumara_with_skin_and_formula == 1 | diff_DescriptionPork_and_formula == 1 | 
                  diff_DescriptionPrawn_and_formula == 1 | diff_DescriptionPumpkin_and_formula == 1 | 
                  diff_DescriptionRaspberries_and_formula == 1 | diff_DescriptionSoybean_and_formula == 1 | 
                  diff_DescriptionStrawberries_and_formula == 1 | diff_DescriptionYellow_peas_and_formula == 1) %>%
  dplyr::mutate(lfc1 = ifelse(passed_ss_DescriptionBlackcurrant_and_formula == 1 & diff_DescriptionBlackcurrant_and_formula == 1, 
                              "white", "black"),
                lfc2 = ifelse(passed_ss_DescriptionChickpea_and_formula == 1 & diff_DescriptionChickpea_and_formula == 1, 
                              "white", "black"),
                lfc3 = ifelse(passed_ss_DescriptionCouscous_and_formula == 1 & diff_DescriptionCouscous_and_formula == 1,"white", "black"),
                lfc4 = ifelse(passed_ss_DescriptionKumara_peeled_and_formula == 1 & diff_DescriptionKumara_peeled_and_formula == 1,"white", "black"),
                lfc5 = ifelse(passed_ss_DescriptionKumara_with_skin_and_formula == 1 & diff_DescriptionKumara_with_skin_and_formula == 1,"white", "black"),
                lfc6 = ifelse(passed_ss_DescriptionPork_and_formula == 1 & diff_DescriptionPork_and_formula == 1,"white", "black"),
                lfc7 = ifelse(passed_ss_DescriptionPrawn_and_formula == 1 & diff_DescriptionPrawn_and_formula == 1,"white", "black"),
                lfc8 = ifelse(passed_ss_DescriptionPumpkin_and_formula == 1 & diff_DescriptionPumpkin_and_formula == 1,"white", "black"),
                lfc9 = ifelse(passed_ss_DescriptionRaspberries_and_formula == 1 & diff_DescriptionRaspberries_and_formula == 1,"white", "black"),
                lfc10 = ifelse(passed_ss_DescriptionSoybean_and_formula == 1 & diff_DescriptionSoybean_and_formula == 1,"white", "black"),
                lfc11 = ifelse(passed_ss_DescriptionStrawberries_and_formula == 1 & diff_DescriptionStrawberries_and_formula == 1,"white", "black"),
                lfc12 = ifelse(passed_ss_DescriptionYellow_peas_and_formula == 1 & diff_DescriptionYellow_peas_and_formula == 1, 
                               "white", "black")) %>%
  tidyr::pivot_longer(cols = lfc1:lfc12, 
                      names_to = "group", values_to = "color") %>%
  dplyr::arrange(taxon)

df_fig_dunn = df_fig_dunn1 %>%
  dplyr::left_join(df_fig_dunn2, by = c("taxon", "group"))
                
# Recode the group names to be more descriptive
df_fig_dunn$group = recode(df_fig_dunn$group, 
                          lfc1 = "Black_beans_and_formula vs Blackcurrant_and_formula",
                          lfc2 = "Black_beans_and_formula vs Chickpea_and_formula",
                          lfc3 = "Black_beans_and_formula vs Couscous_and_formula",
                          lfc4 = "Black_beans_and_formula vs Kumara_peeled_and_formula",
                          lfc5 = "Black_beans_and_formula vs Kumara_with_skin_and_formula",
                          lfc6 = "Black_beans_and_formula vs Pork_and_formula",
                          lfc7 = "Black_beans_and_formula vs Prawn_and_formula",
                          lfc8 = "Black_beans_and_formula vs Pumpkin_and_formula",
                          lfc9 = "Black_beans_and_formula vs Raspberries_and_formula",
                          lfc10 = "Black_beans_and_formula vs Soybean_and_formula",
                          lfc11 = "Black_beans_and_formula vs Strawberries_and_formula",
                          lfc12 = "Black_beans_and_formula vs Yellow_peas_and_formula")
df_fig_dunn$group = factor(df_fig_dunn$group, 
                          levels = c("Black_beans_and_formula vs Blackcurrant_and_formula",
                                                      "Black_beans_and_formula vs Chickpea_and_formula",
                                                      "Black_beans_and_formula vs Couscous_and_formula",
                                                      "Black_beans_and_formula vs Kumara_peeled_and_formula",
                                                      "Black_beans_and_formula vs Kumara_with_skin_and_formula",
                                                      "Black_beans_and_formula vs Pork_and_formula",
                                                      "Black_beans_and_formula vs Prawn_and_formula",
                                                      "Black_beans_and_formula vs Pumpkin_and_formula",
                                                      "Black_beans_and_formula vs Raspberries_and_formula",
                                                      "Black_beans_and_formula vs Soybean_and_formula",
                                                      "Black_beans_and_formula vs Strawberries_and_formula",
                                                      "Black_beans_and_formula vs Yellow_peas_and_formula"))
df_fig_dunn$group = str_replace(df_fig_dunn$group, "Black_beans_and_formula vs ", "")
                
# Define the range for the color scale
lo = floor(min(df_fig_dunn$value))
up = ceiling(max(df_fig_dunn$value))
mid = (lo + up)/2
                
# Create the heatmap plot
fig_dunn = df_fig_dunn %>%
  ggplot(aes(x = group, y = taxon, fill = value)) + 
  geom_tile(color = "black") +
  scale_fill_gradient2(low = "blue", high = "red", mid = "white", 
                      na.value = "white", midpoint = 0, limit = c(lo, up),
                      name = NULL) +
  geom_text(aes(group, taxon, label = value, color = color), size = 5, fontface = "bold") +
                scale_color_identity(guide = FALSE) +
                  labs(x = NULL, y = NULL, title = "Log fold changes for black beans-formula vs other food-formula combinations") +
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
    label = ifelse(color == "white", paste0(round(value, 2), " *"), round(value, 2)),  
    text_color = ifelse(color == "white", "white", "black")  # White for significant, black for others
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
    x = NULL, y = NULL, title = "Log fold changes for black beans-formula vs other food-formula combinations"
  ) +
  theme_minimal() +
  theme(
    plot.title = element_text(hjust = 0.5),
    axis.text.x = element_text(face = "bold", size = 11, angle = 45, hjust = 1),
    axis.text.y = element_text(face = "bold.italic", size = 11)
  )

# Display the plot
fig_dunn