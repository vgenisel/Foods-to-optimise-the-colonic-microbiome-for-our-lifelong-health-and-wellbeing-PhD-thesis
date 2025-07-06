#Selcted foods
import pandas as pd
data_selected_relative_variation = pd.read_csv('heatmap_selected_relative_variation.csv')

data_selected_relative_variation = pd.pivot_table(data_selected_relative_variation, index = ['Diet'])
data_selected_relative_variation = data_selected_relative_variation[['Acetate', 'Propionate', 'Butyrate', 'SCFAs', 'Isobutyrate', 'Isovalerate', 'BCFAs']]

#Plotting heatmap
import seaborn as sns 
import matplotlib.pyplot as plt

plt.figure(figsize=(10,8))
save = sns.heatmap(
    data_selected_relative_variation,
    cmap = 'RdYlGn',
    vmin = None,
    vmax = None,
    center = 0,
    annot = True,
    fmt = ".1f",
    yticklabels = True,
    )

plt.tight_layout()

figure = save.get_figure()
figure.savefig("heatmap_relative_variation.jpg", dpi=400)

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