##Simulating high fibre diet and EU average diet on 4 healthy individuals

# Taxonomy data is obtanied from the following study (https://doi.org/10.1186/s40168-015-0070-0)
# Using taxonomy data from the ISB Course 2020 and AGORA models on genus level
# EU average diet and High-fibre diet were obtanied from the Virtual Metabolic Human database

#Importing data 
from micom.taxonomy import qiime_to_micom
tax = qiime_to_micom("data/table.qza", "data/taxa.qza", collapse_on="genus")

import pandas as pd
metadata = pd.read_table("data/metadata.tsv").rename(columns={"id": "sample_id"})
tax = pd.merge(tax, metadata, on="sample_id") #merging the metadata 
tax = tax.loc[tax["disease_stat"] == 'healthy'] #keeping only the health individuals
tax = tax.replace("ERR1883212", "individual 1")
tax = tax.replace("ERR1883247", "individual 2")
tax = tax.replace("ERR1883260", "individual 3")
tax = tax.replace("ERR1883210", "individual 4")

#Building models
#using AGORA reconstructions
from micom.workflows import build
import pandas as pd
manifest = build(tax, model_db="data/agora103_genus.qza", out_folder="models",
                 solver="osqp", cutoff=0.001, threads=14) #change solver, cutoff and threads

manifest #to check the fraction of the taxa that matches the AGORA database

#Defining the diets
import pandas as pd

medium_hf = pd.read_csv('data/high_fibre.csv') #high fibre diet
medium_eu = pd.read_csv('data/EU_average.csv') #european average diet

#Growing the models
from micom.workflows import grow, save_results

#high fibre diet
res_hf = grow(manifest, model_folder="models", medium=medium_hf, tradeoff=0.5, threads=14) 
save_results(res_hf, "results/high_fibre.zip") #saving results

#EU average diet
res_eu = grow(manifest, model_folder="models", medium=medium_eu, tradeoff=0.5, threads=14) 
save_results(res_eu, "results/EU_average.zip") #saving results

from micom.workflows import load_results
res_hf = load_results("results/high_fibre.zip")
res_eu = load_results("results/EU_average.zip")

#Visualisations
from micom.viz import plot_growth
#Growth rates
plot_growth(res_hf, filename="results/growth_rates_high_fibre.html") 
plot_growth(res_eu, filename="results/growth_rates_EU_average.html") 

#Production rate
from micom.measures import production_rates

hf_prod = production_rates(res_hf) #calculates the production rates
hf_prod.to_csv("results/high_fibre_prod_rate.csv") #saving as excel table

eu_prod = production_rates(res_eu) 
eu_prod.to_csv("results/EU_average_prod_rate.csv")

hf_prod['diet'] = 'high_fibre' #create new colum
eu_prod['diet'] = 'EU_average' #create new colum

exchanges = pd.concat([hf_prod, eu_prod])  # merging the production rates
exchanges = pd.pivot_table(exchanges, index = ['diet','sample_id'], columns = 'name', values = 'flux') #converting into matrix
exchanges = exchanges[["acetate", "propionate", "butyrate",
                       "Isobutyrate, 2-Methylpropanoate", "Isovalerate, 3-Methylbutanoate",
                       "Hydrogen","carbon dioxide"]] #selecting the metabolites of interest

exchanges.to_csv("results/exchanges_metabolites.csv") #saving the results

#Making additional plots
import pandas as pd
import seaborn as sns

sns.set_style("white")
sns.set_context("notebook", font_scale=1.2, rc={"lines.linewidth": 2.5})

#plot of production rates
hf_prod = pd.pivot_table(hf_prod, index = ['diet',"sample_id"], columns = "name", values = "flux") #pivoting the table
hf_prod = hf_prod[["acetate", "propionate", "butyrate",
                       "Isobutyrate, 2-Methylpropanoate", "Isovalerate, 3-Methylbutanoate",
                       "Hydrogen","carbon dioxide"]] #selecting the metabolites of interest

eu_prod = pd.pivot_table(eu_prod, index = ['diet',"sample_id"], columns = "name", values = "flux") #pivoting the table
eu_prod = eu_prod[["acetate", "propionate", "butyrate",
                       "Isobutyrate, 2-Methylpropanoate", "Isovalerate, 3-Methylbutanoate",
                       "Hydrogen","carbon dioxide"]] #selecting the metabolites of interest

prod_rates = pd.concat([hf_prod, eu_prod])  # merge the production rates

prod_rates = prod_rates.plot.barh(figsize=(10,12), width=1, align='center')
prod_rates.set_xlabel("mmol/gDW h")
prod_rates.set_ylabel("Diet and individual")
prod_rates.figure.savefig("results/plot_production_rates.png")

#plot growth rates
growth_hf = pd.read_csv("results/growth_rates_high_fibre.csv")  #importing the groth rates
growth_eu = pd.read_csv("results/growth_rates_eu_average.csv")  #importing the groth rates

growth_eu['diet'] = 'EU_average' #create new colum
growth_hf['diet'] = 'high_fibre' #create new colum

growth_eu = pd.pivot_table(growth_eu, index = ["diet","sample_id"], columns = "taxon", values = "growth_rate") #pivoting the table
growth_hf = pd.pivot_table(growth_hf, index = ["diet","sample_id"], columns = "taxon", values = "growth_rate") #pivoting the table

growth_eu = growth_eu[['Bacteroides', 'Faecalibacterium', 'Streptococcus', 'Clostridium', 'Coprococcus','Blautia', 'Roseburia']] #keeping the 7 faster growing 
growth_hf = growth_hf[['Bacteroides', 'Faecalibacterium', 'Streptococcus', 'Clostridium', 'Coprococcus','Blautia', 'Roseburia']] #keeping the 7 faster growing

growth_rates = pd.concat([growth_eu,growth_hf])  # merging the growth rates

sns.set_style("white")
sns.set_context("notebook", font_scale=1.2, rc={"lines.linewidth": 2.5})
plot_growth_rates = growth_rates.plot.barh(figsize=(10,12), width=0.9, align='center')

plot_growth_rates.set_xlabel("growth rate (1/h)")
plot_growth_rates.set_ylabel("Diet, individual")
plot_growth_rates.figure.savefig("results/plot_growth_rates.png")





