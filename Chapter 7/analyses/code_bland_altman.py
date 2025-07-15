#Loaidng libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

df = pd.read_csv('data_z_scores.csv')

analyte = 'total_SCFAs'

df_analyte = df[df["Analyte"] == analyte]
measured = df_analyte["Measured"]
predicted = df_analyte["Predicted"]
diff = measured - predicted

#Testing normallity for all samples
# Plot Histogram
plt.figure(figsize=(8, 6))
sns.histplot(diff, kde=True, color="skyblue", bins=20)
plt.title(f"Histogram of Differences for {analyte}")
plt.xlabel("Difference (Measured - Predicted)")
plt.ylabel("Frequency")
plt.show()

#Perform the Shapiro-Wilk normality test
stat, p_value = stats.shapiro(diff)
# Step 3: Output the result of the Shapiro-Wilk test
print(f'Shapiro-Wilk Test Statistic: {stat:.4f}')
print(f'P-value: {p_value:.4f}')

##Testing normallity for Food and food-food samples
df = pd.read_csv('data_z_scores.csv')
df_filtered = df[df['Treatment'].isin(['Food', 'Food_food'])]
analyte = 'total_SCFAs'

df_analyte = df_filtered[df_filtered["Analyte"] == analyte]
measured = df_analyte["Measured"]
predicted = df_analyte["Predicted"]
diff = measured - predicted

# Plot Histogram
plt.figure(figsize=(8, 6))
sns.histplot(diff, kde=True, color="skyblue", bins=20)
plt.title(f"Histogram of Differences for {analyte}")
plt.xlabel("Difference (Measured - Predicted)")
plt.ylabel("Frequency")
plt.show()

#Perform the Shapiro-Wilk normality test
stat, p_value = stats.shapiro(diff)
# Step 3: Output the result of the Shapiro-Wilk test
print(f'Shapiro-Wilk Test Statistic: {stat:.4f}')
print(f'P-value: {p_value:.4f}')

##Bland-Altman analysis for food and food_food

# Function to create a Bland-Altman plot with Percentage Differences
def bland_altman_plot(ax, df, analyte, treatment=None):
    """
    Creates a Bland-Altman plot for a given analyte and adds it to the given axis.
    
    Parameters:
        ax (matplotlib axis): The axis to plot on.
        df (DataFrame): Pandas DataFrame containing the data.
        analyte (str): The analyte to analyze.
        treatment (str, optional): If provided, filters data by treatment.
    """
    # Filter data for the selected analyte
    df_analyte = df[df["Analyte"] == analyte]
    
    # Filter by treatment if specified
    if treatment:
        df_analyte = df_analyte[df_analyte["Treatment"] == treatment]

    # Extract measured and predicted values
    measured = df_analyte["Measured"]
    predicted = df_analyte["Predicted"]

    # Compute the mean of the measured and predicted values
    mean_values = np.mean([measured, predicted], axis=0)
    
    # Calculate the percentage difference (Measured - Predicted) / Mean * 100
    diff = (measured - predicted)
            
    # Calculate Bland-Altman statistics
    mean_diff = np.mean(diff)  # Mean percentage difference (bias)
    std_diff = np.std(diff, ddof=1)  # Standard deviation of percentage differences
    loa_upper = mean_diff + 1.96 * std_diff  # Upper limit of agreement
    loa_lower = mean_diff - 1.96 * std_diff  # Lower limit of agreement
    
    # Count the number of samples outside the ±1.96 SD range
    outside_loa = np.sum((diff > loa_upper) | (diff < loa_lower))

    # Plot Bland-Altman scatter (Percentage Differences)
    sns.scatterplot(x=mean_values, y=diff, alpha=0.7, ax=ax)
    ax.axhline(mean_diff, color='red', linestyle='--', label="Mean Difference")
    ax.axhline(loa_upper, color='blue', linestyle='--', label="+1.96 SD")
    ax.axhline(loa_lower, color='blue', linestyle='--', label="-1.96 SD")
    
    # Labels and title
    ax.set_title(f"{analyte}", fontsize=20, fontweight='bold')
    ax.set_xlabel("Average of predicted and measured z-scores", fontsize=18)
    ax.set_ylabel("Difference between z-scores", fontsize=18)
    
    # Remove decimals from Y-axis
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}'))  

    # Annotate bias (mean difference)
    ax.text(np.max(mean_values), mean_diff, f"Mean: {mean_diff:.2f}", 
         fontsize=16, verticalalignment='bottom', horizontalalignment='right', color='red')
    # Annotate upper limit of agreement (+1.96 SD)
    ax.text(np.max(mean_values), loa_upper, f"+1.96 SD: {loa_upper:.2f}", 
         fontsize=16, verticalalignment='bottom', horizontalalignment='right', color='blue')
    # Annotate lower limit of agreement (-1.96 SD)
    ax.text(np.max(mean_values), loa_lower, f"-1.96 SD: {loa_lower:.2f}", 
         fontsize=16, verticalalignment='top', horizontalalignment='right', color='blue')
    
    # Annotate the number of samples outside the ±1.96 SD range
    ax.text(np.min(mean_values), np.min(diff), f"Out of ±1.96 SD: {outside_loa}", 
         fontsize=16, verticalalignment='top', horizontalalignment='left', color='black')

# Load data
df = pd.read_csv('data_z_scores.csv')
df_filtered = df[df["Treatment"].isin(["Food", "Food_food"])]
# Define analytes
analytes = ["Acetate", "Propionate", "Butyrate"]

# Create a 1x3 figure layout
fig, axes = plt.subplots(2, 2, figsize=(14, 10))  # 2 rows, 2 columns
axes = axes.flat  # Flatten the array of axes for easy iteration

# Loop through each analyte and assign a subplot
for i, analyte in enumerate(analytes):
    bland_altman_plot(axes[i], df_filtered, analyte)

# Hide the last subplot (4th subplot, index 3)
axes[-1].set_visible(False)
   
# Adjust layout to prevent overlap and add title for the treatment
fig.suptitle(f"Bland-Altman analysis for food and food-food samples", fontsize=22, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.98])  # Make space for the title at the top
plt.subplots_adjust(hspace=0.4)  # Increase vertical space (try adjusting hspace value)
plt.show()
fig.savefig('results/bland_altman.svg', format='svg', dpi=600)
