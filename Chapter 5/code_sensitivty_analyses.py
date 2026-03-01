##Simulating the influence of foods on the faecal microbiota of 14 infants at weaning age (5 to 12 months)
# data available at https://www.mdpi.com/2076-2607/9/10/2089

#designing diets based on 100 kcal/kg/day for babies untill 1 year. We estime around 608 kcal/day
#https://www.ncbi.nlm.nih.gov/books/NBK560758/

##Comparing the solvers OSQP, GUROBI 10.1, CPLEX 22.1

#1) Grow results using AGORA1 reconstructions (family) and tax information at family level
#2) Load the results
#3) Visualise the growth rates. 
#4) Plot results

#Importing data 
import pandas as pd
tax = pd.read_csv('data/Taxa_genus_parkar_greegenes2.csv') 

##Defining the diets
import pandas as pd
breastmilk = pd.read_csv('data/Breastmilk.csv')

#Building models
#using AGORA reconstructions
from micom.workflows import build
import pandas as pd
manifest_osqp = build(tax, model_db="data/agora201_genus_1.qza", out_folder="models_osqp", solver="osqp", cutoff=0.01, threads=2) 
manifest_gurobi = build(tax, model_db="data/agora201_genus_1.qza", out_folder="models_gurobi", solver="gurobi", cutoff=0.01, threads=2) 
manifest_cplex = build(tax, model_db="data/agora201_genus_1.qza", out_folder="models_cplex", solver="cplex", cutoff=0.01, threads=2) 

manifest_osqp #to check the fraction of the taxa that matches the AGORA2 database
manifest_gurobi #to check the fraction of the taxa that matches the AGORA2 database
manifest_cplex #to check the fraction of the taxa that matches the AGORA2 database

#Choosing the tradeoff
from micom.workflows import tradeoff
from micom.viz import plot_tradeoff

#CPLEX
tradeoff_cplex_breastmilk = tradeoff(manifest_cplex, model_folder="models_cplex", medium=breastmilk, threads=2) 
plot_tradeoff(tradeoff_cplex_breastmilk, filename="results/tradeoff_cplex_breastmilk.html")
#OSQP
tradeoff_osqp_breastmilk = tradeoff(manifest_osqp, model_folder="models_osqp", medium=breastmilk, threads=2) 
plot_tradeoff(tradeoff_osqp_breastmilk, filename="results/tradeoff_osqp_breastmilk.html")
#GUROBI
tradeoff_gurobi_breastmilk = tradeoff(manifest_gurobi, model_folder="models_gurobi", medium=breastmilk, threads=2) 
plot_tradeoff(tradeoff_gurobi_breastmilk, filename="results/tradeoff_gurobi_breastmilk.html")

##Growing the models
from micom.workflows import grow, save_results
#OSQP
res_osqp_breastmilk = grow(manifest_osqp, model_folder="models_osqp", medium=breastmilk, tradeoff=0.7, threads=2)
save_results(res_osqp_breastmilk, "results/osqp_breastmilk.zip") 
#Gurobi
res_gurobi_breastmilk = grow(manifest_gurobi, model_folder="models_gurobi", medium=breastmilk, tradeoff=0.7, threads=2) 
save_results(res_gurobi_breastmilk, "results/gurobi_breastmilk.zip") 
#CPLEX
res_cplex_breastmilk = grow(manifest_cplex, model_folder="models_cplex", medium=breastmilk, tradeoff=0.7, threads=2) 
save_results(res_cplex_breastmilk, "results/cplex_breastmilk.zip") 

#Visualisations
from micom.viz import plot_growth
#Growth rates
#OSQP
plot_growth(res_osqp_breastmilk, filename="results/growth_rates_osqp_breastmilk.html")   
#Gurobi
plot_growth(res_gurobi_breastmilk, filename="results/growth_rates_gurobi_breastmilk.html")   
#CPLEX
plot_growth(res_cplex_breastmilk, filename="results/growth_rates_cplex_breastmilk.html")   

#Plotting growth rates
import pandas as pd
import seaborn as sns

growth_osqp_breastmilk = pd.read_csv('results/growth_rates_osqp_breastmilk.csv')
growth_gurobi_breastmilk = pd.read_csv('results/growth_rates_gurobi_breastmilk.csv')
growth_cplex_breastmilk = pd.read_csv('results/growth_rates_cplex_breastmilk.csv')

growth_osqp_breastmilk['solver'] = 'osqp' 
growth_gurobi_breastmilk['solver'] = 'gurobi' 
growth_cplex_breastmilk['solver'] = 'cplex' 
 
growth_rates_breastmilk = pd.concat([growth_osqp_breastmilk,growth_gurobi_breastmilk,growth_cplex_breastmilk])  # merging the growth rates
growth_rates_breastmilk = pd.pivot_table(growth_rates_breastmilk, index = ["solver"], columns = "taxon", values = "growth_rate") #pivoting the table
growth_rates_breastmilk.to_csv("results/growth_rates_breastmilk.csv")
  
plot_growth_rates_breastmilk = growth_rates_breastmilk.plot.bar(stacked=True, figsize=(10,8)) 
plot_growth_rates_breastmilk.set_ylabel("growth rate [1/h]", fontweight='bold')
plot_growth_rates_breastmilk.set_xlabel("Solver", fontweight='bold')
plot_growth_rates_breastmilk.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plot_growth_rates_breastmilk.figure.savefig("results/plot_growth_rates_breastmilk_stacked.png")

##Comparing growth rates
import numpy as np
import matplotlib.pyplot as plt

# 1. Add a tiny constant to avoid log(0) and transpose for plotting
# 1e-7 is smaller than my smallest observed value
log_growth = np.log10(growth_rates_breastmilk.T + 1e-7)

ax = log_growth.plot(kind='bar', figsize=(12, 6), width=0.8)
ax.set_ylabel("log10 (Growth Rate [1/h])", fontweight='bold')
ax.set_xlabel("Genera", fontweight='bold')
ax.legend(loc='upper center', bbox_to_anchor=(0.1, -0.5), 
          ncol=3, prop={'weight': 'bold'})

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

##Perturbing the uptake bounds in the simulations
#multiplying the lowe bounds (medium) by 0.95, and 1.05
#compare to orginal result

from micom.workflows import grow
import pandas as pd

# Perturbing the diet
breastmilk_reduced = breastmilk.copy()
breastmilk_reduced['flux'] = breastmilk_reduced['flux'] * 0.95

breastmilk_increased = breastmilk.copy()
breastmilk_increased ['flux'] = breastmilk_increased ['flux'] * 1.05

##Growing the models
from micom.workflows import grow, save_results

#Reduced
res_breastmilk_reduced = grow(manifest_cplex, model_folder="models_cplex", medium=breastmilk_reduced, tradeoff=0.7, threads=2) 
save_results(res_breastmilk_reduced, "results/cplex_breastmilk_reduced.zip") 
#Increased
res_breastmilk_increased = grow(manifest_cplex, model_folder="models_cplex", medium=breastmilk_increased, tradeoff=0.7, threads=2) 
save_results(res_breastmilk_increased, "results/cplex_breastmilk_increased.zip") 

#Growth rates
from micom.viz import plot_growth
#Reduced
plot_growth(res_breastmilk_reduced, filename="results/growth_rates_breastmilk_reduced.html")   
#Increased
plot_growth(res_breastmilk_increased, filename="results/growth_rates_breastmilk_increased.html")   

import pandas as pd
import seaborn as sns

growth_breastmilk_reduced = pd.read_csv('results/growth_rates_breastmilk_reduced.csv')
growth_breastmilk_increased = pd.read_csv('results/growth_rates_breastmilk_increased.csv')
growth_cplex_breastmilk = pd.read_csv('results/growth_rates_cplex_breastmilk.csv')

growth_breastmilk_reduced['pertubation'] = 'reduced' 
growth_breastmilk_increased['pertubation'] = 'increased' 
growth_cplex_breastmilk['pertubation'] = 'baseline' 
 
growth_rates_pertubation = pd.concat([growth_breastmilk_reduced,growth_breastmilk_increased,growth_cplex_breastmilk])  # merging the growth rates
growth_rates_pertubation = pd.pivot_table(growth_rates_pertubation, index = ["pertubation"], columns = "taxon", values = "growth_rate") #pivoting the table
growth_rates_pertubation.to_csv("results/growth_rates_pertubation.csv")
  
##Comparing %changes in growth rates
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Calculate Percentage Change relative to Baseline
baseline = growth_rates_pertubation.loc['baseline']
pct_change = ((growth_rates_pertubation.loc[['increased', 'reduced']] - baseline) / baseline) * 100

# Transpose for plotting: Index = Taxa, Columns = Increased/Reduced
df_pct_plot = pct_change.T

# Plotting the Instabilities
ax_3 = df_pct_plot.plot(kind='bar', figsize=(12, 7), color=['#2ca02c', '#d62728'], width=0.8)
# Add 'Stability Reference' lines at +5% and -5%
# Since you perturbed the diet by exactly 5%, biological scaling should be near these lines
ax_3.axhline(5, color='black', linestyle='--', linewidth=1, alpha=0.6, label='Expected +5%')
ax_3.axhline(-5, color='black', linestyle='--', linewidth=1, alpha=0.6, label='Expected -5%')
# Formatting
ax_3.set_ylabel("% Change in Growth Rate", fontweight='bold', fontsize=12)
ax_3.set_xlabel("Genera", fontweight='bold', fontsize=12)
# Bold Tick Labels
for label in (ax_3.get_xticklabels() + ax_3.get_yticklabels()):
    label.set_fontweight('bold')
# Legend at bottom centered
ax_3.legend(loc='upper center', bbox_to_anchor=(0.5, -0.5), 
            ncol=3, prop={'weight': 'bold'})
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()







