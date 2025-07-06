#Imporitng relative fluxes of SCFA and BCFA for breastmilk-food combinations (relative to breastmilk alone)

#Selcted food-combinations

import pandas as pd
data_selected_relative_variation = pd.read_csv('heatmap_selected.csv')

data_selected_relative_variation = pd.pivot_table(data_selected_relative_variation, index = ['Diet'])
data_selected_relative_variation = data_selected_relative_variation[['Acetate', 'Propionate', 'Butyrate', 'SCFAs', 'Isobutyrate', 'Isovalerate', 'BCFAs']]

#Plotting heatmap
import seaborn as sns 
import matplotlib.pyplot as plt

plt.figure(figsize=(11,8))
save = sns.heatmap(
    data_selected_relative_variation,
    cmap = 'RdYlGn',
    center = 0,
    vmin = None,
    vmax = 100,
    robust=True,
    annot = True,
    fmt = ".1f",
    yticklabels = True,
    )

plt.tight_layout()

figure = save.get_figure()
figure.savefig("heatmap_relative_variation.jpg", dpi=400)
