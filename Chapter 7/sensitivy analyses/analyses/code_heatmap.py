# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#imporitng and preparing data
data = pd.read_csv('data_z_scores.csv')
data = data[data["Treatment"].isin(["Food_formula"])] #filtering for food_formula samples only
averge_data = data.groupby(['Sample', 'Analyte'], as_index=False)[['Measured', 'Predicted']].mean() # Group by Sample and Analyte, then calculate the mean of Measured and Predicted


averge_data["Difference"] = averge_data["Predicted"] - averge_data["Measured"]
averge_data["Difference"] = averge_data["Difference"].abs()
                          
# Pivot the data for Predicted values
heatmap_predicted = averge_data.pivot(index="Sample", columns="Analyte", values="Predicted")
# Pivot the data for Measured values
heatmap_measured = averge_data.pivot(index="Sample", columns="Analyte", values="Measured")
# Pivot the data for Difference values
heatmap_difference = averge_data.pivot(index="Sample", columns="Analyte", values="Difference")

# Create side-by-side subplots
fig, axes = plt.subplots(1, 3, figsize=(24, 12), gridspec_kw={'width_ratios': [0.8, 1, 1]})

annot_array_predicted = np.round(heatmap_predicted*1, decimals=1)
annot_array_measured = np.round(heatmap_measured*1, decimals=1)
annot_array_difference = np.round(heatmap_difference*1, decimals=1)

# Plot the Predicted heatmap
sns.heatmap(heatmap_predicted, cmap="Spectral", annot=annot_array_predicted, vmin = -3.3, vmax = 3.3, center=0, ax=axes[0], annot_kws={'size': 12}, linewidths=.5,
            cbar=False)  # Remove color legend)
axes[0].set_title("Predicted z-scores (mmol/gDW.h)", fontweight='bold', fontsize=18)
axes[0].set_ylabel('')  # Remove y-axis label
axes[0].set_xlabel('')  # Remove x-axis label
axes[0].tick_params(axis='y', labelsize=16)
axes[0].tick_params(axis='x', labelsize=16)

# Plot the Measured heatmap
sns.heatmap(heatmap_measured, cmap="Spectral", annot=annot_array_measured, vmin = -3.3, vmax = 3.3, center=0, ax=axes[1], annot_kws={'size': 12}, linewidths=.5,
            yticklabels=False, cbar=False) # Remove y-axis labels
axes[1].set_title("Measured z-scores (mmol/gDW.h)", fontweight='bold', fontsize=18)
axes[1].set_ylabel('')  # Remove y-axis label
axes[1].set_xlabel('')  # Remove x-axis label
axes[1].tick_params(axis='x', labelsize=16)

# Plot the Difference heatmap
sns.heatmap(heatmap_difference, cmap="Spectral", annot=annot_array_difference, vmin = -3.3, vmax = 3.3, center=0, ax=axes[2], annot_kws={'size': 12}, linewidths=.5,
            yticklabels=False) # Remove y-axis labels
axes[2].set_title("Distance between z-scores", fontweight='bold', fontsize=18)
axes[2].set_ylabel('')  # Remove y-axis label
axes[2].set_xlabel('')  # Remove x-axis label
axes[2].tick_params(axis='x', labelsize=16)

plt.tight_layout()
fig.savefig('results/heatmap_food_formula.svg', format='svg', dpi=600)
plt.show()
