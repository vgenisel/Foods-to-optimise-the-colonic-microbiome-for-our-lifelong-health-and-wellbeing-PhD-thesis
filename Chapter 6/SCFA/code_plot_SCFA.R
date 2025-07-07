library(readxl)
library(tidyverse)

# Read Excel file
df <- read_excel("C:/Users/vgenisel/OneDrive - Massey University/Desktop/5-Microbial function in vitro/SCFA_all_samples.xlsx")
df[df < 0] <- 0  # Replacing negative values with 0

# Define the custom order for the Composition variable
composition_order <- c("food", "food and formula", "food and food", "food and food and formula", "control")

# Convert data from wide to long format
df_long <- df %>%
  pivot_longer(cols = Formate:Succinate, names_to = "Metabolite", values_to = "Concentration") %>%
  mutate(Composition = factor(Composition, levels = composition_order))  # Reorder compositions

# Reorder Sample based on Composition and Sample order
df_long <- df_long %>%
  arrange(Composition, Sample) %>%
  mutate(Sample = factor(Sample, levels = unique(Sample)))  # Reorder Sample based on Composition order

# Set inverse order for SCFAs (Metabolites)
scfa_order <- c("Succinate", "Lactate", "Heptanoate", "Isovalerate", "Buytrate", "Propionate", "Acetate", "Formate")
df_long <- df_long %>%
  mutate(Metabolite = factor(Metabolite, levels = scfa_order))  # Reorder SCFA levels in reverse order

# Calculate positions for vertical lines (boundaries between compositions)
composition_boundaries <- df_long %>%
  group_by(Composition) %>%
  summarise(boundary = max(as.numeric(Sample))) %>%
  pull(boundary)

# Create the stacked bar plot with vertical lines between compositions
ggplot(df_long, aes(x = Sample, y = Concentration, fill = Metabolite)) +
  geom_bar(stat = "identity") +
  geom_vline(xintercept = composition_boundaries + 0.5, linetype = "dashed", colour = "black") +  # Add dashed vertical lines
  theme_minimal(base_size = 15) +
  theme(
    text = element_text(family = "Times New Roman"),  # Set font to Times New Roman
    panel.background = element_rect(fill = "#f5f5f5", colour = "#f5f5f5"),  # Lighter grey background
    axis.text.x = element_text(angle = 90, vjust = 0.5, hjust = 1),
    legend.position = "bottom",  # Move the legend to the bottom
    legend.direction = "horizontal",  # Arrange legend items horizontally
    legend.box = "horizontal",  # Align legend items in a single line
    legend.text = element_text(size = 12)  # Reduce legend text size
  ) +
  labs(x = "Sample", 
       y = "Organic acids (mmol/g*DW)",  # Updated y-axis label
       fill = "Organic acid") +  # Updated legend label
  scale_y_continuous(limits = c(0, 10), expand = c(0, 0)) +  # Ensure y-axis starts at 0 and ends at 10
  scale_fill_brewer(palette = "Spectral") +  # Adjust the colour palette if needed
  guides(fill = guide_legend(nrow = 1))  # Make the legend a single row

library(readxl)
library(tidyverse)

# Read Excel file
df <- read_excel("C:/Users/vgenisel/OneDrive - Massey University/Desktop/5-Microbial function in vitro/all_samples.xlsx")
df[df < 0] <- 0  # Replacing negative values with 0

# Define the custom order for the Composition variable
composition_order <- c("food", "food and formula", "food and food", "food and food and formula", "control")

# Convert data from wide to long format
df_long <- df %>%
  pivot_longer(cols = Formate:Succinate, names_to = "Metabolite", values_to = "Concentration") %>%
  mutate(Composition = factor(Composition, levels = composition_order))  # Reorder compositions

# Calculate total organic acids for each Sample
df_totals <- df_long %>%
  group_by(Sample, Composition) %>%
  summarise(Total_Acids = sum(Concentration)) %>%
  ungroup()

# Reorder Sample within each Composition based on the total organic acids
df_long <- df_long %>%
  left_join(df_totals, by = c("Sample", "Composition")) %>%  # Join the total organic acids to the long data frame
  arrange(Composition, desc(Total_Acids)) %>%  # Sort by Composition and total acids (descending)
  mutate(Sample = factor(Sample, levels = unique(Sample)))  # Reorder Sample based on the total acids

# Set inverse order for SCFAs (Metabolites)
scfa_order <- c("Succinate", "Lactate", "Heptanoate", "Isovalerate", "Buytrate", "Propionate", "Acetate", "Formate")
df_long <- df_long %>%
  mutate(Metabolite = factor(Metabolite, levels = scfa_order))  # Reorder SCFA levels in reverse order

# Calculate positions for vertical lines (boundaries between compositions)
composition_boundaries <- df_long %>%
  group_by(Composition) %>%
  summarise(boundary = max(as.numeric(Sample))) %>%
  pull(boundary)

# Create the stacked bar plot with vertical lines between compositions
ggplot(df_long, aes(x = Sample, y = Concentration, fill = Metabolite)) +
  geom_bar(stat = "identity") +
  geom_vline(xintercept = composition_boundaries + 0.5, linetype = "dashed", colour = "black") +  # Add dashed vertical lines
  theme_minimal(base_size = 15) +
  theme(
    text = element_text(family = "Times New Roman"),  # Set font to Times New Roman
    panel.background = element_rect(fill = "#f5f5f5", colour = "#f5f5f5"),  # Lighter grey background
    axis.text.x = element_text(angle = 90, vjust = 0.5, hjust = 1),
    legend.position = "bottom",  # Move the legend to the bottom
    legend.direction = "horizontal",  # Arrange legend items horizontally
    legend.box = "horizontal",  # Align legend items in a single line
    legend.text = element_text(size = 12)  # Reduce legend text size
  ) +
  labs(x = "Sample", 
       y = "Organic acids (mmol/g*DW)",  # Updated y-axis label
       fill = "Organic acid") +  # Updated legend label
  scale_y_continuous(limits = c(0, 10), expand = c(0, 0)) +  # Ensure y-axis starts at 0 and ends at 10
  scale_fill_brewer(palette = "Spectral") +  # Adjust the colour palette if needed
  guides(fill = guide_legend(nrow = 1))  # Make the legend a single row

