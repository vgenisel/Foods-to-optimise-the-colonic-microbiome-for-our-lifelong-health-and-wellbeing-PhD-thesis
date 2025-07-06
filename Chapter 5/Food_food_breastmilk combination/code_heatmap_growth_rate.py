#Selcted foods
import pandas as pd
data_selected_relative_variation = pd.read_csv('heatmap_growth.csv')

data_selected_relative_variation = pd.pivot_table(data_selected_relative_variation, index = ['Multiple food-breastmilk combination'])

#Plotting heatmap
import seaborn as sns 
import matplotlib.pyplot as plt

plt.figure(figsize=(12,8))
save = sns.heatmap(
    data_selected_relative_variation,
    cmap = 'RdYlGn',
    vmin = -80,
    vmax = 40,
    center = 0,
    annot = True,
    fmt = ".1f",
    yticklabels = True,
    )

save.set_xticklabels(save.get_xticklabels(), fontstyle='italic')

plt.tight_layout()

figure = save.get_figure()
figure.savefig("heatmap_growth.jpg", dpi=400)

#Plotting clustermap
import seaborn as sns 
sns.clustermap(
    data_selected_relative_variation,  # take 50 highest fluxes
    cmap = 'RdYlGn',
    yticklabels = True,  # show all metabolite names
    figsize = (8, 12)    # size of the heatmap
    )

import seaborn as sns 
sns.heatmap(data_selected_relative_variation, cmap = 'RdYlGn',)