import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#imporitng and preparing data
data = pd.read_csv('data_z_scores.csv')
data = data[data["Treatment"].isin(["Food", "Food_food"])] #filtering for food and food-food samples only
data = data.groupby(['Sample', 'Analyte'], as_index=False)[['Measured', 'Predicted']].mean()

# Define SCFA categories
categories = ['Acetate', 'Propionate', 'Butyrate', 'total_SCFAs']
num_vars = len(categories)

# Number of rows and columns for the grid layout
nrows = 6  
ncols = 5  

# Calculate the number of required subplots (if samples exceed nrows * ncols, increase the layout)
num_samples = len(data['Sample'].unique())
fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(48, 5 * nrows), subplot_kw=dict(polar=True))

# Flatten axes array for easier iteration (if multiple rows/columns)
axes = axes.flatten()

# Iterate through each sample and plot in a specific subplot
for i, sample in enumerate(data['Sample'].unique()):
    subset = data[data['Sample'] == sample].set_index('Analyte')

    # Ensure analytes are in correct order & handle missing values
    measured_values = subset.reindex(categories)['Measured'].dropna().tolist()
    predicted_values = subset.reindex(categories)['Predicted'].dropna().tolist()

    # Close the circle for radar plot
    measured_values += measured_values[:1]
    predicted_values += predicted_values[:1]

    # Compute angles for radar chart
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]

    # Select the appropriate axis for the current subplot
    ax = axes[i]

    # Plot Measured values
    ax.fill(angles, measured_values, color='blue', alpha=0.25, label='Measured')
    ax.plot(angles, measured_values, color='blue', linewidth=2, linestyle='solid')

    # Plot Predicted values
    ax.fill(angles, predicted_values, color='red', alpha=0.25, label='Predicted')
    ax.plot(angles, predicted_values, color='red', linewidth=2, linestyle='dashed')

    # Labels and Title
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=20)
    ax.set_title(f"{sample}", fontsize=24, y=1.10,fontweight='bold')
    #ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1))
    
# Hide the empty subplots (remaining unused axes)
for i in range(num_samples, len(axes)):
    axes[i].axis('off')
    
# Create a single legend for the entire figure
handles, labels = axes[0].get_legend_handles_labels()  # Get legend elements from the first subplot
fig.legend(handles, labels, loc='lower right', bbox_to_anchor=(0.95, 0.05), fontsize=34, ncol=1)
  
# Adjust layout to prevent overlap
plt.tight_layout()
plt.subplots_adjust(hspace=0.4)  # Increase vertical space (try adjusting hspace value)
fig.savefig('results/spider_plot.svg', format='svg', dpi=600)
plt.show()