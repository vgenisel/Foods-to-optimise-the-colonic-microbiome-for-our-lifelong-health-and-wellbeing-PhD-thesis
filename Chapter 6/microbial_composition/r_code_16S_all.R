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

#Alpha-diversity 
alpha_div <- estimate_richness(ps_fixed, measures = c("Shannon", "Simpson", "Chao1"))

alpha_food <- plot_richness(ps_fixed, x = "Description", color="Description", measures = c("Shannon", "Simpson", "Chao1")) +
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
kruskal.test(Shannon ~ Time, data = alpha_div)#p-value <0.05
kruskal.test(Simpson ~ Time, data = alpha_div) #p-value <0.05
kruskal.test(Chao1 ~ Time, data = alpha_div)

#Rarefaction or not?
sample_sums(ps_fixed) #to check number of reads per sample
set.seed(111) # keep result reproductive
ps_rarefied = rarefy_even_depth(ps_fixed, sample.size = 49433, rngseed = 123) #rarefying to the minimal value of reads

#Beta-diversity 
#Bray-curtis ordination
dist = phyloseq::distance(ps_rarefied, method="bray")
ordination = ordinate(ps_rarefied, method="PCoA", distance=dist)

# Extract eigenvalues to calculate explained variance
eigenvalues <- ordination$values[, 1]
percent_variance <- round(eigenvalues / sum(eigenvalues) * 100, 1) # Calculate % variance explained

custom_colors <- c("#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "#999999",
                   "#8DD3C7", "#FFFFB3", "#BEBADA", "#FB8072", "#80B1D3", "#FDB462", "#B3DE69", "#FCCDE5", 
                   "#D9D9D9", "#BC80BD", "#CCEBC5", "#FFED6F", "#1F78B4", "#33A02C", "#FB9A99", "#E31A1C", 
                   "#FDBF6F", "#CAB2D6", "#6A3D9A", "#B15928", "#A6CEE3", "#B2DF8A", "#FF7F00", "#6B8E23", 
                   "#FF4500", "#CD5C5C", "#4682B4", "#32CD32", "#FFD700", "#40E0D0", "#EE82EE", "#FF6347", 
                   "#DC143C", "#800000", "#0000CD", "#9400D3", "#20B2AA", "#FF1493", "#7FFFD4", "#B8860B", 
                   "#FFB6C1", "#696969", "#FF00FF", "#6A5ACD", "#F4A460", "#4682B4", "#FF4500")

plot_ordination(ps_rarefied, ordination, color="Description") + 
  geom_point(size=4) +  
  theme_classic() +
  scale_color_manual(values = custom_colors) +  # Apply custom color palette
  theme(strip.background = element_blank(),
        panel.background = element_rect(fill = "#f0f0f0"),  # Set panel background to a lighter grey
        plot.background = element_rect(fill = "#f0f0f0"),   # Set plot background to a lighter grey
        axis.title.x = element_text(size = 12, face = "bold"),  # x-axis title size and bold
        axis.title.y = element_text(size = 12, face = "bold"),  # y-axis title size and bold
        legend.position = "bottom") +  # Move legend to the bottom
  labs(x = paste0("PC1 (", percent_variance[1], "%)"),   # Change x-axis title
       y = paste0("PC2 (", percent_variance[2], "%)"))   # Change y-axis title

#adonis - PERMANOVA
metadata_food <- data.frame(sample_data(ps_rarefied))
adonis_food <- adonis2(dist ~ Time, data = metadata_food, permutations = 9999) #p-value <0.05

#Transforming data into relative abundances, collapsing into higher rank, and filtering rare abundant taxa
ps_transformed <- ps_fixed %>%
    tax_transform(trans = "compositional", rank = "Genus") %>%
    tax_filter(min_prevalence=0.1, min_sample_abundance = 0.0001) #Filtering to taxa present in at least 10% samples with more than 0.01% relative abundance

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

write.csv(agg_stats, "relative_abundance_with_variation_genus.csv")

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

#Subseting to exclude time zero
ps_no_timezero <- ps_fixed %>%
  ps_filter(Category %in% c("food_alone", "food_and_food", "food_and_formula",
                            "food_and_food_and_formula"), .keep_all_taxa = TRUE)

ps_transformed_nozero <- ps_no_timezero %>%
  tax_transform(trans = "compositional", rank = "Genus") %>%
  tax_filter(min_prevalence=0.1, min_sample_abundance = 0.0005) #Filtering to taxa present in at least 10% samples with more than 0.05% relative abundance

ps_transformed_nozero %>%
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
    legend.text = element_text(size = 10))    # legend text

#Differential abundance testing using ANCOM-BC2
tse = mia::makeTreeSummarizedExperimentFromPhyloseq(ps_fixed)
tse$Time <- factor(tse$Time)
#tse$Description = relevel(tse$Time, ref = "0")

set.seed(123)
contrast_matrix <- diag(2)  # Create a 14x14 identity matrix
output = ancombc2(data = tse, assay_name = "counts", tax_level = "Family",
                  fix_formula = "Time", rand_formula = NULL,
                  p_adj_method = "holm", pseudo_sens = TRUE,
                  prv_cut = 0.05, lib_cut = 1000, s0_perc = 0.05,
                  group = "Time", struc_zero = TRUE, neg_lb = TRUE,
                  alpha = 0.05, n_cl = 2, verbose = TRUE,
                  global = TRUE, pairwise = TRUE, dunnet = TRUE, trend = TRUE,
                  iter_control = list(tol = 1e-2, max_iter = 20, 
                                      verbose = TRUE),
                  em_control = list(tol = 1e-5, max_iter = 100),
                  lme_control = lme4::lmerControl(),
                  mdfdr_control = list(fwer_ctrl_method = "holm", B = 100),
                  trend_control = list(
                    contrast = list(contrast_matrix),  # Use the 14x14 contrast matrix
                    node = list(rep(1, 2)),  # Adjust nodes accordingly
                    solver = "ECOS",
                    B = 10))


#Primary analyses
res_prim = output$res
write.csv(res_prim, file = "ancombc2_results_raspberries.csv", row.names = FALSE)
#Global test
res_global = output$res_global
#multiple pairwise comparisons
res_pair = output$res_pair

#multiple pairwise comparisons against a pre-specified group (Dunnett’s type of test)
res_dunn = output$res_dunn
write.csv(res_dunn, file = "ancombc2_dunn_raspberries_genus.csv", row.names = FALSE)

# Filter and transform the data for comparison with Raspberries
df_fig_dunn1 = res_dunn %>%
  dplyr::filter(diff_DescriptionBlack_beans == 1 | diff_DescriptionBlackcurrant == 1 | 
                  diff_DescriptionChickpea == 1 | diff_DescriptionCouscous == 1 | 
                  diff_DescriptionInfant_formula == 1 | diff_DescriptionPork == 1 | 
                  diff_DescriptionPumpkin == 1 | diff_DescriptionShrimp == 1 | 
                  diff_DescriptionSoybean == 1 | diff_DescriptionSplit_peas == 1 | 
                  diff_DescriptionStrawberries == 1 | diff_DescriptionSweet_potato_peeled == 1 | 
                  diff_DescriptionSweet_potato_with_skin == 1) %>%
  dplyr::mutate(lfc1 = ifelse(diff_DescriptionBlack_beans == 1, round(lfc_DescriptionBlack_beans, 2), 0),
                lfc2 = ifelse(diff_DescriptionBlackcurrant == 1, round(lfc_DescriptionBlackcurrant, 2), 0),
                lfc3 = ifelse(diff_DescriptionChickpea == 1, round(lfc_DescriptionChickpea, 2), 0),
                lfc4 = ifelse(diff_DescriptionCouscous == 1, round(lfc_DescriptionCouscous, 2), 0),
                lfc5 = ifelse(diff_DescriptionInfant_formula == 1, round(lfc_DescriptionInfant_formula, 2), 0),
                lfc6 = ifelse(diff_DescriptionPork == 1, round(lfc_DescriptionPork, 2), 0),
                lfc7 = ifelse(diff_DescriptionPumpkin == 1, round(lfc_DescriptionPumpkin, 2), 0),
                lfc8 = ifelse(diff_DescriptionShrimp == 1, round(lfc_DescriptionShrimp, 2), 0),
                lfc9 = ifelse(diff_DescriptionSoybean == 1, round(lfc_DescriptionSoybean, 2), 0),
                lfc10 = ifelse(diff_DescriptionSplit_peas == 1, round(lfc_DescriptionSplit_peas, 2), 0),
                lfc11 = ifelse(diff_DescriptionStrawberries == 1, round(lfc_DescriptionStrawberries, 2), 0),
                lfc12 = ifelse(diff_DescriptionSweet_potato_peeled == 1, round(lfc_DescriptionSweet_potato_peeled, 2), 0),
                lfc13 = ifelse(diff_DescriptionSweet_potato_with_skin == 1, round(lfc_DescriptionSweet_potato_with_skin, 2), 0)) %>%
  tidyr::pivot_longer(cols = lfc1:lfc13, 
                      names_to = "group", values_to = "value") %>%
  dplyr::arrange(taxon)

df_fig_dunn2 = res_dunn %>%
  dplyr::filter(diff_DescriptionBlack_beans == 1 | diff_DescriptionBlackcurrant == 1 | 
                  diff_DescriptionChickpea == 1 | diff_DescriptionCouscous == 1 | 
                  diff_DescriptionInfant_formula == 1 | diff_DescriptionPork == 1 | 
                  diff_DescriptionPumpkin == 1 | diff_DescriptionShrimp == 1 | 
                  diff_DescriptionSoybean == 1 | diff_DescriptionSplit_peas == 1 | 
                  diff_DescriptionStrawberries == 1 | diff_DescriptionSweet_potato_peeled == 1 | 
                  diff_DescriptionSweet_potato_with_skin == 1) %>%
  dplyr::mutate(lfc1 = ifelse(passed_ss_DescriptionBlack_beans == 1 & diff_DescriptionBlack_beans == 1, 
                              "aquamarine3", "black"),
                lfc2 = ifelse(passed_ss_DescriptionBlackcurrant == 1 & diff_DescriptionBlackcurrant == 1, 
                              "aquamarine3", "black"),
                lfc3 = ifelse(passed_ss_DescriptionChickpea == 1 & diff_DescriptionChickpea == 1,"aquamarine3", "black"),
                lfc4 = ifelse(passed_ss_DescriptionCouscous == 1 & diff_DescriptionCouscous == 1,"aquamarine3", "black"),
                lfc5 = ifelse(passed_ss_DescriptionInfant_formula == 1 & diff_DescriptionInfant_formula == 1,"aquamarine3", "black"),
                lfc6 = ifelse(passed_ss_DescriptionPork == 1 & diff_DescriptionPork == 1,"aquamarine3", "black"),
                lfc7 = ifelse(passed_ss_DescriptionPumpkin == 1 & diff_DescriptionPumpkin == 1,"aquamarine3", "black"),
                lfc8 = ifelse(passed_ss_DescriptionShrimp == 1 & diff_DescriptionShrimp == 1,"aquamarine3", "black"),
                lfc9 = ifelse(passed_ss_DescriptionSoybean == 1 & diff_DescriptionSoybean == 1,"aquamarine3", "black"),
                lfc10 = ifelse(passed_ss_DescriptionSplit_peas == 1 & diff_DescriptionSplit_peas == 1,"aquamarine3", "black"),
                lfc11 = ifelse(passed_ss_DescriptionStrawberries == 1 & diff_DescriptionStrawberries == 1,"aquamarine3", "black"),
                lfc12 = ifelse(passed_ss_DescriptionSweet_potato_peeled == 1 & diff_DescriptionSweet_potato_peeled == 1,"aquamarine3", "black"),
                lfc13 = ifelse(passed_ss_DescriptionSweet_potato_with_skin == 1 & diff_DescriptionSweet_potato_with_skin == 1, 
                               "aquamarine3", "black")) %>%
  tidyr::pivot_longer(cols = lfc1:lfc13, 
                      names_to = "group", values_to = "color") %>%
  dplyr::arrange(taxon)

df_fig_dunn = df_fig_dunn1 %>%
  dplyr::left_join(df_fig_dunn2, by = c("taxon", "group"))

# Recode the group names to be more descriptive
df_fig_dunn$group = recode(df_fig_dunn$group, 
                           `lfc1` = "Raspberries vs Black_beans",
                           `lfc2` = "Raspberries vs Blackcurrant",
                           `lfc2` = "Raspberries vs Chickpea",
                           `lfc2` = "Raspberries vs Couscous",
                           `lfc2` = "Raspberries vs Infant_formula",
                           `lfc2` = "Raspberries vs Pork",
                           `lfc2` = "Raspberries vs Pumpkin",
                           `lfc2` = "Raspberries vs Shrimp",
                           `lfc2` = "Raspberries vs Soybean",
                           `lfc2` = "Raspberries vs Split_peas",
                           `lfc2` = "Raspberries vs Strawberries",
                           `lfc2` = "Raspberries vs Sweet_potato_peeled",
                           `lfc13` = "Raspberries vs Sweet_potato_with_skin")
df_fig_dunn$group = factor(df_fig_dunn$group, 
                           levels = c("Raspberries vs Black_beans",
                                      "Raspberries vs Blackcurrant",
                                      "Raspberries vs Chickpea",
                                      "Raspberries vs Couscous",
                                      "Raspberries vs Infant_formula",
                                      "Raspberries vs Pork",
                                      "Raspberries vs Pumpkin",
                                      "Raspberries vs Shrimp",
                                      "Raspberries vs Soybean",
                                      "Raspberries vs Split_peas",
                                      "Raspberries vs Strawberries",
                                      "Raspberries vs Sweet_potato_peeled",
                                      "Raspberries vs Sweet_potato_with_skin"))

# Define the range for the color scale
lo = floor(min(df_fig_dunn$value))
up = ceiling(max(df_fig_dunn$value))
mid = (lo + up)/2

# Create the heatmap plot
fig_dunn = df_fig_dunn %>%
  ggplot(aes(x = group, y = taxon, fill = value)) + 
  geom_tile(color = "black") +
  scale_fill_gradient2(low = "blue", high = "red", mid = "white", 
                       na.value = "white", midpoint = mid, limit = c(lo, up),
                       name = NULL) +
  geom_text(aes(group, taxon, label = value, color = color), size = 4) +
  scale_color_identity(guide = FALSE) +
  labs(x = NULL, y = NULL, title = "Log fold changes for Raspberries vs Other Foods") +
  theme_minimal() +
  theme(plot.title = element_text(hjust = 0.5))

# Display the plot
fig_dunn