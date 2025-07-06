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
  ps_filter(Category %in% c("food_alone"), .keep_all_taxa = TRUE) %>%
  merge_samples(group = "Description")

#Transforming data into relative abundances, collapsing into higher rank, and filtering rare abundant taxa
ps_transformed <- ps_food %>%
  tax_transform(trans = "compositional", rank = "Genus") %>%
  tax_filter(min_prevalence=0.05, min_sample_abundance = 0.0005)

# Subset the phyloseq object to only include the genus 'Lacticaseibacillus'
ps_lacticaseibacillus <- subset_taxa(ps_transformed, Genus == "Lacticaseibacillus")

# Convert to data frame for ggplot2
ps_lacticaseibacillus_df <- psmelt(ps_lacticaseibacillus)

# Plot the relative abundance
ggplot(ps_lacticaseibacillus_df, aes(x = Sample, y = Abundance, fill = Sample)) +
  geom_bar(stat = "identity", position = "dodge") +
  theme_minimal() +
  labs(title = "Relative Abundance of Lacticaseibacillus by Sample",
       x = "Sample",
       y = "Relative Abundance") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

