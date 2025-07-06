#Imporitng relative fluxes of SCFA and BCFA for breastmilk-food combinations (relative to breastmilk alone)

import pandas as pd
data = pd.read_csv('heatmap.csv')

data = pd.pivot_table(data, index = ['Diet'])
data = data[['Acetate', 'Propionate', 'Butyrate', 'SCFA', 'Isobutyrate', 'Isovalerate', 'BCFA']]

#Plotting heatmap
import seaborn as sns 
sns.clustermap(
    data,  # take 50 highest fluxes
    cmap = 'RdYlGn',
    yticklabels = True,  # show all metabolite names
    figsize = (8, 12)    # size of the heatmap
    )

#Selcted foods
import pandas as pd
data_selected = pd.read_csv('heatmap_selected.csv')

data_selected = pd.pivot_table(data_selected, index = ['Diet'])
data_selected = data_selected[['Acetate', 'Propionate', 'Butyrate', 'SCFA', 'Isobutyrate', 'Isovalerate', 'BCFA']]

#Plotting heatmap
import seaborn as sns 
sns.clustermap(
    data_selected,  # take 50 highest fluxes
    cmap = 'RdYlGn',
    yticklabels = True,  # show all metabolite names
    figsize = (8, 12)    # size of the heatmap
    )

import seaborn as sns 
sns.heatmap(data_selected, cmap = 'RdYlGn',)

