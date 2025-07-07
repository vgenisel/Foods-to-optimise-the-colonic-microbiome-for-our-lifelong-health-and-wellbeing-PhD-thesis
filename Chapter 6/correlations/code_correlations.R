library(ggplot2)
library(reshape2)
library(corrplot)
library(dplyr)
library(RColorBrewer)  # For color palettes

# Importing data
merged_data <- read.csv("data_correlation.csv")
merged_data[merged_data < 0] <- 0

# List of SCFAs and Food Components in your dataset
scfa_list <- c("Formate", "Acetate", "Propionate", "Butyrate", "total_SCFA", "Isovalerate", "Lactate", "Succinate")
food_component_list <- c("ash", "crude_protein", "fat", "saturated_fat",
                         "carbohydrate", "total_dietary_fibre", "sugar", "beta_glucan",
                         "non_protein_nitrogen", "energy")
microbiota_list <- c("Bacteroides", "Escherichia_Shigella", "Bifidobacterium", "Enterococcus",
                     "Klebsiella", "Streptococcus", "Salmonella",
                     "Enterobacter", "Lacticaseibacillus",
                     "Akkermansia", "Blautia", "Parabacteroides",
                     "Anaeroglobus", "Veillonella", "Eubacterium", "Clostridium_sensu_stricto_1",
                     "Eggerthella")
#microbiota_list <- c("Bacteroides", "Escherichia_Shigella", "Bifidobacterium", "Enterococcus",
                     "Klebsiella", "Streptococcus", "Salmonella", "Hafnia_Obesumbacterium",
                     "Collinsella", "Enterobacter", "Hungatella", "Lacticaseibacillus",
                     "Akkermansia", "Blautia", "Parabacteroides",
                     "Anaeroglobus", "Veillonella", "Eubacterium", "Clostridium_sensu_stricto_1",
                     "Pluralibacter", "Eggerthella", "Citrobacter")

## Spearman correlation for SCFA and food composition
cor_results <- data.frame(SCFA = character(), Food_Component = character(), 
                          Correlation = numeric(), P_Value = numeric(), 
                          stringsAsFactors = FALSE)

for (scfa in scfa_list) {
  for (food_component in food_component_list) {
    test <- cor.test(merged_data[[scfa]], merged_data[[food_component]], method = "spearman")
    cor_results <- rbind(cor_results, data.frame(SCFA = scfa, 
                                                 Food_Component = food_component, 
                                                 Correlation = test$estimate, 
                                                 P_Value = test$p.value))
  }
}

# Adjust p-values using Benjamini-Hochberg method
cor_results$P_Adjusted <- p.adjust(cor_results$P_Value, method = "BH")
# Round correlation values for cleaner display
cor_results$Correlation_Rounded <- round(cor_results$Correlation, 2)
# Reshape correlation matrix for heatmap plotting
cor_matrix <- acast(cor_results, SCFA ~ Food_Component, value.var = "Correlation")
p_matrix <- acast(cor_results, SCFA ~ Food_Component, value.var = "P_Adjusted")

# Plot heatmap with correlation values inside cells and significant ones highlighted
ggplot(cor_results, aes(x = Food_Component, y = SCFA, fill = Correlation)) +
  geom_tile() +
  scale_fill_gradient2(low = "blue", high = "red", mid = "white", midpoint = 0, limit = c(-1, 1), 
                       name = "Spearman\nCorrelation") +
  geom_text(aes(label = paste0(Correlation_Rounded, 
                               ifelse(P_Adjusted < 0.05, "**", 
                                      ifelse(P_Adjusted < 0.1, "*", "")))), 
            color = "white", size = 3) +  # Display both correlation and significance
  coord_fixed() +  # Move coord_fixed here
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1, vjust = 1, face = "bold"),  # Bold x-axis
        axis.text.y = element_text(face = "bold"))  # Bold y-axis

# Filter for significant correlations (p < 0.1)
cor_results_filtered <- cor_results %>%
  filter(P_Adjusted < 0.1)

# Plot heatmap with filtered results
ggplot(cor_results_filtered, aes(x = Food_Component, y = SCFA, fill = Correlation)) +
  geom_tile() +
  scale_fill_gradient2(low = "blue", high = "red", mid = "white", midpoint = 0, limit = c(-1, 1), 
                       name = "Spearman\nCorrelation") +
  geom_text(aes(label = paste0(Correlation_Rounded, 
                               ifelse(P_Adjusted < 0.05, "**", 
                                      ifelse(P_Adjusted < 0.1, "*", "")))), 
            color = "black", size = 3) +
  coord_fixed() +
  theme_minimal() +
  theme(panel.background = element_rect(fill = "lightgrey", color = NA),
        axis.text.x = element_text(angle = 45, hjust = 1, vjust = 1, face = "bold"), 
        axis.text.y = element_text(face = "bold")) +
  labs(x = "Food components", y = "SCFAs")


## Spearman correlation for food components and microbiota
cor_results_microbiota_food <- data.frame(Microbiota = character(), Food_Component = character(), 
                                          Correlation = numeric(), P_Value = numeric(), 
                                          stringsAsFactors = FALSE)

for (microbiota in microbiota_list) {
  for (food_component in food_component_list) {
    test <- cor.test(merged_data[[microbiota]], merged_data[[food_component]], method = "spearman")
    cor_results_microbiota_food <- rbind(cor_results_microbiota_food, data.frame(Microbiota = microbiota, 
                                                                                 Food_Component = food_component, 
                                                                                 Correlation = test$estimate, 
                                                                                 P_Value = test$p.value))
  }
}

# Adjust p-values using Benjamini-Hochberg method
cor_results_microbiota_food$P_Adjusted <- p.adjust(cor_results_microbiota_food$P_Value, method = "BH")
# Round correlation values
cor_results_microbiota_food$Correlation_Rounded <- round(cor_results_microbiota_food$Correlation, 2)

# Plot heatmap for food components and microbiota with bold axis text
ggplot(cor_results_microbiota_food, aes(x = Food_Component, y = Microbiota, fill = Correlation)) +
  geom_tile() +
  scale_fill_gradient2(low = "blue", high = "red", mid = "white", midpoint = 0, limit = c(-1, 1), 
                       name = "Spearman\nCorrelation") +
  geom_text(aes(label = paste0(Correlation_Rounded, ifelse(P_Adjusted < 0.05, "*", ""))), 
            color = "black", size = 3) +  # Display both correlation and significance
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1, vjust = 1, face = "bold"),  # Bold x-axis
        axis.text.y = element_text(face = "bold")) +  # Bold y-axis
  labs(x = "Food components", y = "Microbiota") +
  coord_fixed()

# Filter for significant correlations (p < 0.1)
cor_results_microbiota_food_filtered <- cor_results_microbiota_food %>%
  filter(P_Adjusted < 0.1)

# Plot heatmap with filtered results
ggplot(cor_results_microbiota_food_filtered, aes(x = Food_Component, y = Microbiota, fill = Correlation)) +
  geom_tile() +
  scale_fill_gradient2(low = "blue", high = "red", mid = "white", midpoint = 0, limit = c(-1, 1), 
                       name = "Spearman\nCorrelation") +
  geom_text(aes(label = paste0(Correlation_Rounded, 
                               ifelse(P_Adjusted < 0.05, "**", 
                                      ifelse(P_Adjusted < 0.1, "*", "")))), 
            color = "black", size = 3) +
  coord_fixed() +
  theme_minimal() +
  theme(panel.background = element_rect(fill = "lightgrey", color = NA),
        axis.text.x = element_text(angle = 45, hjust = 1, vjust = 1, face = "bold"), 
        axis.text.y = element_text(face = "bold")) +
  labs(x = "Food components", y = "Microbiota")


## Spearman correlation for SCFA and microbiota
cor_results_microbiota_scfa <- data.frame(Microbiota = character(), SCFA = character(), 
                                          Correlation = numeric(), P_Value = numeric(), 
                                          stringsAsFactors = FALSE)

for (microbiota in microbiota_list) {
  for (scfa in scfa_list) {
    test <- cor.test(merged_data[[microbiota]], merged_data[[scfa]], method = "spearman")
    cor_results_microbiota_scfa <- rbind(cor_results_microbiota_scfa, data.frame(Microbiota = microbiota, 
                                                                                 SCFA = scfa, 
                                                                                 Correlation = test$estimate, 
                                                                                 P_Value = test$p.value))
  }
}

# Adjust p-values using Benjamini-Hochberg method
cor_results_microbiota_scfa$P_Adjusted <- p.adjust(cor_results_microbiota_scfa$P_Value, method = "BH")
# Round correlation values
cor_results_microbiota_scfa$Correlation_Rounded <- round(cor_results_microbiota_scfa$Correlation, 2)

# Plot heatmap for SCFA and microbiota with bold axis text
ggplot(cor_results_microbiota_scfa, aes(x = SCFA, y = Microbiota, fill = Correlation)) +
  geom_tile() +
  scale_fill_gradient2(low = "blue", high = "red", mid = "white", midpoint = 0, limit = c(-1, 1), 
                       name = "Spearman\nCorrelation") +
  geom_text(aes(label = paste0(Correlation_Rounded, ifelse(P_Adjusted < 0.05, "*", ""))), 
            color = "black", size = 3) +  # Display both correlation and significance
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1, vjust = 1, face = "bold"),  # Bold x-axis
        axis.text.y = element_text(face = "bold")) +  # Bold y-axis
  labs(x = "SCFAs", y = "Microbiota") +
  coord_fixed()

# Filter for significant correlations (p < 0.1)
cor_results_microbiota_scfa_filtered <- cor_results_microbiota_scfa %>%
  filter(P_Adjusted < 0.1)

# Plot heatmap with filtered results
ggplot(cor_results_microbiota_scfa_filtered, aes(x = SCFA, y = Microbiota, fill = Correlation)) +
  geom_tile() +
  scale_fill_gradient2(low = "blue", high = "red", mid = "white", midpoint = 0, limit = c(-1, 1), 
                       name = "Spearman\nCorrelation") +
  geom_text(aes(label = paste0(Correlation_Rounded, 
                               ifelse(P_Adjusted < 0.05, "**", 
                                      ifelse(P_Adjusted < 0.1, "*", "")))), 
            color = "black", size = 3) +
  coord_fixed() +
  theme_minimal() +
  theme(panel.background = element_rect(fill = "lightgrey", color = NA),
        axis.text.x = element_text(angle = 45, hjust = 1, vjust = 1, face = "bold"), 
        axis.text.y = element_text(face = "bold")) +
  labs(x = "SCFAs", y = "Microbiota")

###Analayse per food groups#########
##Food ingredients only
food_data <- merged_data %>% filter(Group == "food")

## Spearman correlation for SCFA and food composition
cor_results_food <- data.frame(SCFA = character(), Food_Component = character(), 
                               Correlation = numeric(), P_Value = numeric(), 
                               stringsAsFactors = FALSE)

for (scfa in scfa_list) {
  for (food_component in food_component_list) {
    test <- cor.test(food_data[[scfa]], food_data[[food_component]], method = "spearman")
    cor_results_food <- rbind(cor_results_food, data.frame(SCFA = scfa,Food_Component = food_component,Correlation = test$estimate, 
                                                           P_Value = test$p.value))
  }}

cor_results_food$P_Adjusted <- p.adjust(cor_results_food$P_Value, method = "BH") # Adjust p-values using Benjamini-Hochberg method
cor_results_food$Correlation_Rounded <- round(cor_results_food$Correlation, 2) # Round correlation values for cleaner display
cor_matrix_food <- acast(cor_results_food, SCFA ~ Food_Component, value.var = "Correlation") # Reshape correlation matrix for heatmap plotting
p_matrix_food <- acast(cor_results_food, SCFA ~ Food_Component, value.var = "P_Adjusted")

# Plot heatmap with correlation values inside cells and significant ones highlighted
ggplot(cor_results_food, aes(x = Food_Component, y = SCFA, fill = Correlation)) +
  geom_tile() +
  scale_fill_gradient2(low = "blue", high = "red", mid = "white", midpoint = 0, limit = c(-1, 1), 
                       name = "Spearman\nCorrelation") +
  geom_text(aes(label = paste0(Correlation_Rounded, 
                               ifelse(P_Adjusted < 0.05, "**", 
                                      ifelse(P_Adjusted < 0.1, "*", "")))), 
            color = "black", size = 3) +  # Display both correlation and significance
  coord_fixed() +  # Move coord_fixed here
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1, vjust = 1, face = "bold"),  # Bold x-axis
        axis.text.y = element_text(face = "bold"))  # Bold y-axis

cor_results_filtered_food <- cor_results_food %>%   filter(P_Adjusted < 0.1)# Filter for significant correlations (p < 0.1)

# Plot heatmap with filtered results
ggplot(cor_results_filtered_food, aes(x = Food_Component, y = SCFA, fill = Correlation)) +
  geom_tile() +
  scale_fill_gradient2(low = "blue", high = "red", mid = "white", midpoint = 0, limit = c(-1, 1), 
                       name = "Spearman\nCorrelation") +
  geom_text(aes(label = paste0(Correlation_Rounded, 
                               ifelse(P_Adjusted < 0.05, "**", 
                                      ifelse(P_Adjusted < 0.1, "*", "")))), 
            color = "black", size = 3) +
  coord_fixed() +
  theme_minimal() +
  theme(panel.background = element_rect(fill = "lightgrey", color = NA),
        axis.text.x = element_text(angle = 45, hjust = 1, vjust = 1, face = "bold"), 
        axis.text.y = element_text(face = "bold")) +
  labs(x = "Food components", y = "SCFAs")


## Spearman correlation for food components and microbiota
cor_results_microbiota_food_food <- data.frame(Microbiota = character(), Food_Component = character(), 
                                               Correlation = numeric(), P_Value = numeric(), 
                                               stringsAsFactors = FALSE)

for (microbiota in microbiota_list) {
  for (food_component in food_component_list) {
    test <- cor.test(food_data[[microbiota]], food_data[[food_component]], method = "spearman")
    cor_results_microbiota_food_food <- rbind(cor_results_microbiota_food_food, data.frame(Microbiota = microbiota, 
                                                                                           Food_Component = food_component, 
                                                                                           Correlation = test$estimate, 
                                                                                           P_Value = test$p.value))
  }
}

# Adjust p-values using Benjamini-Hochberg method
cor_results_microbiota_food_food$P_Adjusted <- p.adjust(cor_results_microbiota_food_food$P_Value, method = "BH")
# Round correlation values
cor_results_microbiota_food_food$Correlation_Rounded <- round(cor_results_microbiota_food_food$Correlation, 2)

# Plot heatmap for food components and microbiota with bold axis text
ggplot(cor_results_microbiota_food_food, aes(x = Food_Component, y = Microbiota, fill = Correlation)) +
  geom_tile() +
  scale_fill_gradient2(low = "blue", high = "red", mid = "white", midpoint = 0, limit = c(-1, 1), 
                       name = "Spearman\nCorrelation") +
  geom_text(aes(label = paste0(Correlation_Rounded, ifelse(P_Adjusted < 0.05, "*", ""))), 
            color = "black", size = 3) +  # Display both correlation and significance
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1, vjust = 1, face = "bold"),  # Bold x-axis
        axis.text.y = element_text(face = "bold")) +  # Bold y-axis
  labs(x = "Food components", y = "Microbiota") +
  coord_fixed()

cor_results_microbiota_food_food_filtered <- cor_results_microbiota_food_food %>%   filter(P_Adjusted < 0.1)# Filter for significant correlations (p < 0.1)

# Plot heatmap with filtered results
ggplot(cor_results_microbiota_food_food_filtered, aes(x = Food_Component, y = SCFA, fill = Correlation)) +
  geom_tile() +
  scale_fill_gradient2(low = "blue", high = "red", mid = "white", midpoint = 0, limit = c(-1, 1), 
                       name = "Spearman\nCorrelation") +
  geom_text(aes(label = paste0(Correlation_Rounded, 
                               ifelse(P_Adjusted < 0.05, "**", 
                                      ifelse(P_Adjusted < 0.1, "*", "")))), 
            color = "black", size = 3) +
  coord_fixed() +
  theme_minimal() +
  theme(panel.background = element_rect(fill = "lightgrey", color = NA),
        axis.text.x = element_text(angle = 45, hjust = 1, vjust = 1, face = "bold"), 
        axis.text.y = element_text(face = "bold")) +
  labs(x = "Food components", y = "SCFAs")

## Spearman correlation for SCFA and microbiota
cor_results_microbiota_scfa_food <- data.frame(Microbiota = character(), SCFA = character(), 
                                               Correlation = numeric(), P_Value = numeric(), 
                                               stringsAsFactors = FALSE)

for (microbiota in microbiota_list) {
  for (scfa in scfa_list) {
    test <- cor.test(food_data[[microbiota]], food_data[[scfa]], method = "spearman")
    cor_results_microbiota_scfa_food <- rbind(cor_results_microbiota_scfa_food, data.frame(Microbiota = microbiota, 
                                                                                           SCFA = scfa, 
                                                                                           Correlation = test$estimate, 
                                                                                           P_Value = test$p.value))
  }
}

# Adjust p-values using Benjamini-Hochberg method
cor_results_microbiota_scfa_food$P_Adjusted <- p.adjust(cor_results_microbiota_scfa_food$P_Value, method = "BH")
# Round correlation values
cor_results_microbiota_scfa_food$Correlation_Rounded <- round(cor_results_microbiota_scfa_food$Correlation, 2)

# Plot heatmap for SCFA and microbiota with bold axis text
ggplot(cor_results_microbiota_scfa_food, aes(x = SCFA, y = Microbiota, fill = Correlation)) +
  geom_tile() +
  scale_fill_gradient2(low = "blue", high = "red", mid = "white", midpoint = 0, limit = c(-1, 1), 
                       name = "Spearman\nCorrelation") +
  geom_text(aes(label = paste0(Correlation_Rounded, ifelse(P_Adjusted < 0.05, "*", ""))), 
            color = "black", size = 3) +  # Display both correlation and significance
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1, vjust = 1, face = "bold"),  # Bold x-axis
        axis.text.y = element_text(face = "bold")) +  # Bold y-axis
  labs(x = "SCFAs", y = "Microbiota") +
  coord_fixed()


##Berry
berry_data <- merged_data %>% filter(category == "berry")

## Spearman correlation for SCFA and food composition
cor_results_berry <- data.frame(SCFA = character(), Food_Component = character(), 
                                Correlation = numeric(), P_Value = numeric(), 
                                stringsAsFactors = FALSE)

for (scfa in scfa_list) {
  for (food_component in food_component_list) {
    test <- cor.test(berry_data[[scfa]], berry_data[[food_component]], method = "spearman")
    cor_results_berry <- rbind(cor_results_berry, data.frame(SCFA = scfa,Food_Component = food_component,Correlation = test$estimate, 
                                                             P_Value = test$p.value))
  }}

cor_results_berry$P_Adjusted <- p.adjust(cor_results_berry$P_Value, method = "BH") # Adjust p-values using Benjamini-Hochberg method
cor_results_berry$Correlation_Rounded <- round(cor_results_berry$Correlation, 2) # Round correlation values for cleaner display
cor_matrix_berry <- acast(cor_results_berry, SCFA ~ Food_Component, value.var = "Correlation") # Reshape correlation matrix for heatmap plotting
p_matrix_berry <- acast(cor_results_berry, SCFA ~ Food_Component, value.var = "P_Adjusted")

# Plot heatmap with correlation values inside cells and significant ones highlighted
ggplot(cor_results_berry, aes(x = Food_Component, y = SCFA, fill = Correlation)) +
  geom_tile() +
  scale_fill_gradient2(low = "blue", high = "red", mid = "white", midpoint = 0, limit = c(-1, 1), 
                       name = "Spearman\nCorrelation") +
  geom_text(aes(label = paste0(Correlation_Rounded, 
                               ifelse(P_Adjusted < 0.05, "**", 
                                      ifelse(P_Adjusted < 0.1, "*", "")))), 
            color = "white", size = 3) +  # Display both correlation and significance
  coord_fixed() +  # Move coord_fixed here
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1, vjust = 1, face = "bold"),  # Bold x-axis
        axis.text.y = element_text(face = "bold"))  # Bold y-axis


## Spearman correlation for food components and microbiota
cor_results_microbiota_food_berry <- data.frame(Microbiota = character(), Food_Component = character(), 
                                                Correlation = numeric(), P_Value = numeric(), 
                                                stringsAsFactors = FALSE)

for (microbiota in microbiota_list) {
  for (food_component in food_component_list) {
    test <- cor.test(berry_data[[microbiota]], berry_data[[food_component]], method = "spearman")
    cor_results_microbiota_food_berry <- rbind(cor_results_microbiota_food_berry, data.frame(Microbiota = microbiota, 
                                                                                             Food_Component = food_component, 
                                                                                             Correlation = test$estimate, 
                                                                                             P_Value = test$p.value))
  }
}

# Adjust p-values using Benjamini-Hochberg method
cor_results_microbiota_food_berry$P_Adjusted <- p.adjust(cor_results_microbiota_food_berry$P_Value, method = "BH")
# Round correlation values
cor_results_microbiota_food_berry$Correlation_Rounded <- round(cor_results_microbiota_food_berry$Correlation, 2)

# Plot heatmap for food components and microbiota with bold axis text
ggplot(cor_results_microbiota_food_berry, aes(x = Food_Component, y = Microbiota, fill = Correlation)) +
  geom_tile() +
  scale_fill_gradient2(low = "blue", high = "red", mid = "white", midpoint = 0, limit = c(-1, 1), 
                       name = "Spearman\nCorrelation") +
  geom_text(aes(label = paste0(Correlation_Rounded, ifelse(P_Adjusted < 0.05, "*", ""))), 
            color = "black", size = 3) +  # Display both correlation and significance
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1, vjust = 1, face = "bold"),  # Bold x-axis
        axis.text.y = element_text(face = "bold")) +  # Bold y-axis
  labs(x = "Food components", y = "Microbiota") +
  coord_fixed()

## Spearman correlation for SCFA and microbiota
cor_results_microbiota_scfa_berry <- data.frame(Microbiota = character(), SCFA = character(), 
                                                Correlation = numeric(), P_Value = numeric(), 
                                                stringsAsFactors = FALSE)

for (microbiota in microbiota_list) {
  for (scfa in scfa_list) {
    test <- cor.test(berry_data[[microbiota]], berry_data[[scfa]], method = "spearman")
    cor_results_microbiota_scfa_berry <- rbind(cor_results_microbiota_scfa_berry, data.frame(Microbiota = microbiota, 
                                                                                             SCFA = scfa, 
                                                                                             Correlation = test$estimate, 
                                                                                             P_Value = test$p.value))
  }
}

# Adjust p-values using Benjamini-Hochberg method
cor_results_microbiota_scfa_berry$P_Adjusted <- p.adjust(cor_results_microbiota_scfa_berry$P_Value, method = "BH")
# Round correlation values
cor_results_microbiota_scfa_berry$Correlation_Rounded <- round(cor_results_microbiota_scfa_berry$Correlation, 2)

# Plot heatmap for SCFA and microbiota with bold axis text
ggplot(cor_results_microbiota_scfa_berry, aes(x = SCFA, y = Microbiota, fill = Correlation)) +
  geom_tile() +
  scale_fill_gradient2(low = "blue", high = "red", mid = "white", midpoint = 0, limit = c(-1, 1), 
                       name = "Spearman\nCorrelation") +
  geom_text(aes(label = paste0(Correlation_Rounded, ifelse(P_Adjusted < 0.05, "*", ""))), 
            color = "black", size = 3) +  # Display both correlation and significance
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1, vjust = 1, face = "bold"),  # Bold x-axis
        axis.text.y = element_text(face = "bold")) +  # Bold y-axis
  labs(x = "SCFAs", y = "Microbiota") +
  coord_fixed()


##All samples
# Importing data
all_data <- read.csv("data_correlation.csv")
all_data[all_data < 0] <- 0

# List of SCFAs and Food Components in your dataset
scfa_list <- c("Formate", "Acetate", "Propionate", "Butyrate", "total_SCFA", "Isovalerate", "Lactate", "Succinate")
food_component_list <- c("ash", "crude_protein", "fat", "saturated_fat",
                         "carbohydrate", "total_dietary_fibre", "sugar", "beta_glucan",
                         "non_protein_nitrogen", "energy")
microbiota_list <- c("Bacteroides", "Escherichia_Shigella", "Bifidobacterium", "Enterococcus",
                     "Klebsiella", "Streptococcus", "Salmonella", "Hafnia_Obesumbacterium",
                     "Collinsella", "Enterobacter", "Hungatella", "Lacticaseibacillus",
                     "Akkermansia", "Blautia", "Parabacteroides",
                     "Anaeroglobus", "Veillonella", "Eubacterium", "Clostridium_sensu_stricto_1",
                     "Pluralibacter", "Eggerthella", "Citrobacter")

## Spearman correlation for SCFA and food composition
cor_results_all <- data.frame(SCFA = character(), Food_Component = character(), 
                          Correlation = numeric(), P_Value = numeric(), 
                          stringsAsFactors = FALSE)

for (scfa in scfa_list) {
  for (food_component in food_component_list) {
    test <- cor.test(all_data[[scfa]], all_data[[food_component]], method = "spearman")
    cor_results_all <- rbind(cor_results_all, data.frame(SCFA = scfa, 
                                                 Food_Component = food_component, 
                                                 Correlation = test$estimate, 
                                                 P_Value = test$p.value))
  }
}

# Adjust p-values using Benjamini-Hochberg method
cor_results_all$P_Adjusted <- p.adjust(cor_results_all$P_Value, method = "BH")
# Round correlation values for cleaner display
cor_results_all$Correlation_Rounded <- round(cor_results_all$Correlation, 2)
# Reshape correlation matrix for heatmap plotting
cor_matrix_all <- acast(cor_results_all, SCFA ~ Food_Component, value.var = "Correlation")
p_matrix_all <- acast(cor_results_all, SCFA ~ Food_Component, value.var = "P_Adjusted")

# Plot heatmap with correlation values inside cells and significant ones highlighted
ggplot(cor_results_all, aes(x = Food_Component, y = SCFA, fill = Correlation)) +
  geom_tile() +
  scale_fill_gradient2(low = "blue", high = "red", mid = "white", midpoint = 0, limit = c(-1, 1), 
                       name = "Spearman\nCorrelation") +
  geom_text(aes(label = paste0(Correlation_Rounded, 
                               ifelse(P_Adjusted < 0.05, "**", 
                                      ifelse(P_Adjusted < 0.1, "*", "")))), 
            color = "white", size = 3) +  # Display both correlation and significance
  coord_fixed() +  # Move coord_fixed here
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1, vjust = 1, face = "bold"),  # Bold x-axis
        axis.text.y = element_text(face = "bold"))  # Bold y-axis

# Filter for significant correlations (p < 0.1)
cor_results_filtered_all <- cor_results_all %>%
  filter(P_Adjusted < 0.1)

# Plot heatmap with filtered results
ggplot(cor_results_filtered_all, aes(x = Food_Component, y = SCFA, fill = Correlation)) +
  geom_tile() +
  scale_fill_gradient2(low = "blue", high = "red", mid = "white", midpoint = 0, limit = c(-1, 1), 
                       name = "Spearman\nCorrelation") +
  geom_text(aes(label = paste0(Correlation_Rounded, 
                               ifelse(P_Adjusted < 0.05, "**", 
                                      ifelse(P_Adjusted < 0.1, "*", "")))), 
            color = "white", size = 3) +
  coord_fixed() +
  theme_minimal() +
  theme(panel.background = element_rect(fill = "lightgrey", color = NA),
        axis.text.x = element_text(angle = 45, hjust = 1, vjust = 1, face = "bold"), 
        axis.text.y = element_text(face = "bold")) +
  labs(x = "Food components", y = "SCFAs")


## Spearman correlation for food components and microbiota
cor_results_microbiota_food_all <- data.frame(Microbiota = character(), Food_Component = character(), 
                                          Correlation = numeric(), P_Value = numeric(), 
                                          stringsAsFactors = FALSE)

for (microbiota in microbiota_list) {
  for (food_component in food_component_list) {
    test <- cor.test(all_data[[microbiota]], all_data[[food_component]], method = "spearman")
    cor_results_microbiota_food_all <- rbind(cor_results_microbiota_food_all, data.frame(Microbiota = microbiota, 
                                                                                 Food_Component = food_component, 
                                                                                 Correlation = test$estimate, 
                                                                                 P_Value = test$p.value))
  }
}

# Adjust p-values using Benjamini-Hochberg method
cor_results_microbiota_food_all$P_Adjusted <- p.adjust(cor_results_microbiota_food_all$P_Value, method = "BH")
# Round correlation values
cor_results_microbiota_food_all$Correlation_Rounded <- round(cor_results_microbiota_food_all$Correlation, 2)

# Plot heatmap for food components and microbiota with bold axis text
ggplot(cor_results_microbiota_food_all, aes(x = Food_Component, y = Microbiota, fill = Correlation)) +
  geom_tile() +
  scale_fill_gradient2(low = "blue", high = "red", mid = "white", midpoint = 0, limit = c(-1, 1), 
                       name = "Spearman\nCorrelation") +
  geom_text(aes(label = paste0(Correlation_Rounded, ifelse(P_Adjusted < 0.05, "*", ""))), 
            color = "black", size = 3) +  # Display both correlation and significance
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1, vjust = 1, face = "bold"),  # Bold x-axis
        axis.text.y = element_text(face = "bold")) +  # Bold y-axis
  labs(x = "Food components", y = "Microbiota") +
  coord_fixed()

# Filter for significant correlations (p < 0.1)
cor_results_microbiota_food_filtered_all <- cor_results_microbiota_food_all %>%
  filter(P_Adjusted < 0.1)

# Plot heatmap with filtered results
ggplot(cor_results_microbiota_food_filtered_all, aes(x = Food_Component, y = Microbiota, fill = Correlation)) +
  geom_tile() +
  scale_fill_gradient2(low = "blue", high = "red", mid = "white", midpoint = 0, limit = c(-1, 1), 
                       name = "Spearman\nCorrelation") +
  geom_text(aes(label = paste0(Correlation_Rounded, 
                               ifelse(P_Adjusted < 0.05, "**", 
                                      ifelse(P_Adjusted < 0.1, "*", "")))), 
            color = "white", size = 3) +
  coord_fixed() +
  theme_minimal() +
  theme(panel.background = element_rect(fill = "lightgrey", color = NA),
        axis.text.x = element_text(angle = 45, hjust = 1, vjust = 1, face = "bold"), 
        axis.text.y = element_text(face = "bold")) +
  labs(x = "Food components", y = "Microbiota")


## Spearman correlation for SCFA and microbiota
cor_results_microbiota_scfa_all <- data.frame(Microbiota = character(), SCFA = character(), 
                                          Correlation = numeric(), P_Value = numeric(), 
                                          stringsAsFactors = FALSE)

for (microbiota in microbiota_list) {
  for (scfa in scfa_list) {
    test <- cor.test(all_data[[microbiota]], all_data[[scfa]], method = "spearman")
    cor_results_microbiota_scfa_all <- rbind(cor_results_microbiota_scfa_all, data.frame(Microbiota = microbiota, 
                                                                                 SCFA = scfa, 
                                                                                 Correlation = test$estimate, 
                                                                                 P_Value = test$p.value))
  }
}

# Adjust p-values using Benjamini-Hochberg method
cor_results_microbiota_scfa_all$P_Adjusted <- p.adjust(cor_results_microbiota_scfa_all$P_Value, method = "BH")
# Round correlation values
cor_results_microbiota_scfa_all$Correlation_Rounded <- round(cor_results_microbiota_scfa_all$Correlation, 2)

# Plot heatmap for SCFA and microbiota with bold axis text
ggplot(cor_results_microbiota_scfa_all, aes(x = SCFA, y = Microbiota, fill = Correlation)) +
  geom_tile() +
  scale_fill_gradient2(low = "blue", high = "red", mid = "white", midpoint = 0, limit = c(-1, 1), 
                       name = "Spearman\nCorrelation") +
  geom_text(aes(label = paste0(Correlation_Rounded, ifelse(P_Adjusted < 0.05, "*", ""))), 
            color = "black", size = 3) +  # Display both correlation and significance
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1, vjust = 1, face = "bold"),  # Bold x-axis
        axis.text.y = element_text(face = "bold")) +  # Bold y-axis
  labs(x = "SCFAs", y = "Microbiota") +
  coord_fixed()

# Filter for significant correlations (p < 0.1)
cor_results_microbiota_scfa_filtered_all <- cor_results_microbiota_scfa_all %>%
  filter(P_Adjusted < 0.1)

# Plot heatmap with filtered results
ggplot(cor_results_microbiota_scfa_filtered_all, aes(x = SCFA, y = Microbiota, fill = Correlation)) +
  geom_tile() +
  scale_fill_gradient2(low = "blue", high = "red", mid = "white", midpoint = 0, limit = c(-1, 1), 
                       name = "Spearman\nCorrelation") +
  geom_text(aes(label = paste0(Correlation_Rounded, 
                               ifelse(P_Adjusted < 0.05, "**", 
                                      ifelse(P_Adjusted < 0.1, "*", "")))), 
            color = "white", size = 3) +
  coord_fixed() +
  theme_minimal() +
  theme(panel.background = element_rect(fill = "lightgrey", color = NA),
        axis.text.x = element_text(angle = 45, hjust = 1, vjust = 1, face = "bold"), 
        axis.text.y = element_text(face = "bold")) +
  labs(x = "SCFAs", y = "Microbiota")