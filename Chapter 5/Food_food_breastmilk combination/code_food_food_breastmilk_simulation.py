##Simulating NZ food-breastmilk combinations on the microbiome of weaning infants
#Food1 +  Food2 + Breastmilk (7.5/7.5/85) designed for infants at 6 months (608 kcal/day)
#Daily fluxes, CPLEX 22.1, AGORA2, genus
#66 NZ multiple food combinations + 2 controls (only breastmilk and only infant formula)

import pandas as pd
tax = pd.read_csv('data/Taxa_genus_parkar_greegenes2.csv') 

#Building models using AGORA2 reconstructions
from micom.workflows import build
import pandas as pd
manifest = build(tax, model_db="data/agora201_genus_1.qza", out_folder="models_cplex", solver="cplex", cutoff=0.01, threads=14) #keeping taxa with at least 1% relative abundance
manifest #to check the fraction of the taxa that matches the AGORA2 database

##Defining the diets
import pandas as pd

Blackbeans_Blackcurrant_breastmilk = pd.read_csv('data/Blackbeans_Blackcurrant_breastmilk.csv')
Blackbeans_Chickpea_breastmilk = pd.read_csv('data/Blackbeans_Chickpea_breastmilk.csv')
Blackbeans_Couscous_breastmilk = pd.read_csv('data/Blackbeans_Couscous_breastmilk.csv')
Blackbeans_Pork_breastmilk = pd.read_csv('data/Blackbeans_Pork_breastmilk.csv')
Blackbeans_Pumpkin_breastmilk = pd.read_csv('data/Blackbeans_Pumpkin_breastmilk.csv')
Blackbeans_Raspberries_breastmilk = pd.read_csv('data/Blackbeans_Raspberries_breastmilk.csv')
Blackbeans_Shrimp_breastmilk = pd.read_csv('data/Blackbeans_Shrimp_breastmilk.csv')
Blackbeans_Soybean_breastmilk = pd.read_csv('data/Blackbeans_Soybean_breastmilk.csv')
Blackbeans_Splitpeas_breastmilk = pd.read_csv('data/Blackbeans_Splitpeas_breastmilk.csv')
Blackbeans_Strawberries_breastmilk = pd.read_csv('data/Blackbeans_Strawberries_breastmilk.csv')
Blackbeans_Sweetpotato_breastmilk = pd.read_csv('data/Blackbeans_Sweetpotato_breastmilk.csv')
Blackcurrant_Chickpea_breastmilk = pd.read_csv('data/Blackcurrant_Chickpea_breastmilk.csv')
Blackcurrant_Couscous_breastmilk = pd.read_csv('data/Blackcurrant_Couscous_breastmilk.csv')
Blackcurrant_Pork_breastmilk = pd.read_csv('data/Blackcurrant_Pork_breastmilk.csv')
Blackcurrant_Pumpkin_breastmilk = pd.read_csv('data/Blackcurrant_Pumpkin_breastmilk.csv')
Blackcurrant_Raspberries_breastmilk = pd.read_csv('data/Blackcurrant_Raspberries_breastmilk.csv')
Blackcurrant_Shrimp_breastmilk = pd.read_csv('data/Blackcurrant_Shrimp_breastmilk.csv')
Blackcurrant_Soybean_breastmilk = pd.read_csv('data/Blackcurrant_Soybean_breastmilk.csv')
Blackcurrant_Splitpeas_breastmilk = pd.read_csv('data/Blackcurrant_Splitpeas_breastmilk.csv')
Blackcurrant_Strawberries_breastmilk = pd.read_csv('data/Blackcurrant_Strawberries_breastmilk.csv')
Blackcurrant_Sweetpotato_breastmilk = pd.read_csv('data/Blackcurrant_Sweetpotato_breastmilk.csv')
Chickpea_Couscous_breastmilk = pd.read_csv('data/Chickpea_Couscous_breastmilk.csv')
Chickpea_Pork_breastmilk = pd.read_csv('data/Chickpea_Pork_breastmilk.csv')
Chickpea_Pumpkin_breastmilk = pd.read_csv('data/Chickpea_Pumpkin_breastmilk.csv')
Chickpea_Raspberries_breastmilk = pd.read_csv('data/Chickpea_Raspberries_breastmilk.csv')
Chickpea_Shrimp_breastmilk = pd.read_csv('data/Chickpea_Shrimp_breastmilk.csv')
Chickpea_Soybean_breastmilk = pd.read_csv('data/Chickpea_Soybean_breastmilk.csv')
Chickpea_Splitpeas_breastmilk = pd.read_csv('data/Chickpea_Splitpeas_breastmilk.csv')
Chickpea_Strawberries_breastmilk = pd.read_csv('data/Chickpea_Strawberries_breastmilk.csv')
Chickpea_Sweetpotato_breastmilk = pd.read_csv('data/Chickpea_Sweetpotato_breastmilk.csv')
Couscous_Pork_breastmilk = pd.read_csv('data/Couscous_Pork_breastmilk.csv')
Couscous_Pumpkin_breastmilk = pd.read_csv('data/Couscous_Pumpkin_breastmilk.csv')
Couscous_Raspberries_breastmilk = pd.read_csv('data/Couscous_Raspberries_breastmilk.csv')
Couscous_Shrimp_breastmilk = pd.read_csv('data/Couscous_Shrimp_breastmilk.csv')
Couscous_Soybean_breastmilk = pd.read_csv('data/Couscous_Soybean_breastmilk.csv')
Couscous_Splitpeas_breastmilk = pd.read_csv('data/Couscous_Splitpeas_breastmilk.csv')
Couscous_Strawberries_breastmilk = pd.read_csv('data/Couscous_Strawberries_breastmilk.csv')
Couscous_Sweetpotato_breastmilk = pd.read_csv('data/Couscous_Sweetpotato_breastmilk.csv')
Pork_Pumpkin_breastmilk = pd.read_csv('data/Pork_Pumpkin_breastmilk.csv')
Pork_Raspberries_breastmilk = pd.read_csv('data/Pork_Raspberries_breastmilk.csv')
Pork_Shrimp_breastmilk = pd.read_csv('data/Pork_Shrimp_breastmilk.csv')
Pork_Soybean_breastmilk = pd.read_csv('data/Pork_Soybean_breastmilk.csv')
Pork_Splitpeas_breastmilk = pd.read_csv('data/Pork_Splitpeas_breastmilk.csv')
Pork_Strawberries_breastmilk = pd.read_csv('data/Pork_Strawberries_breastmilk.csv')
Pork_Sweetpotato_breastmilk = pd.read_csv('data/Pork_Sweetpotato_breastmilk.csv')
Pumpkin_Raspberries_breastmilk = pd.read_csv('data/Pumpkin_Raspberries_breastmilk.csv')
Pumpkin_Shrimp_breastmilk = pd.read_csv('data/Pumpkin_Shrimp_breastmilk.csv')
Pumpkin_Soybean_breastmilk = pd.read_csv('data/Pumpkin_Soybean_breastmilk.csv')
Pumpkin_Splitpeas_breastmilk = pd.read_csv('data/Pumpkin_Splitpeas_breastmilk.csv')
Pumpkin_Strawberries_breastmilk = pd.read_csv('data/Pumpkin_Strawberries_breastmilk.csv')
Pumpkin_Sweetpotato_breastmilk = pd.read_csv('data/Pumpkin_Sweetpotato_breastmilk.csv')
Raspberries_Shrimp_breastmilk = pd.read_csv('data/Raspberries_Shrimp_breastmilk.csv')
Raspberries_Soybean_breastmilk = pd.read_csv('data/Raspberries_Soybean_breastmilk.csv')
Raspberries_Splitpeas_breastmilk = pd.read_csv('data/Raspberries_Splitpeas_breastmilk.csv')
Raspberries_Strawberries_breastmilk = pd.read_csv('data/Raspberries_Strawberries_breastmilk.csv')
Raspberries_Sweetpotato_breastmilk = pd.read_csv('data/Raspberries_Sweetpotato_breastmilk.csv')
Shrimp_Soybean_breastmilk = pd.read_csv('data/Shrimp_Soybean_breastmilk.csv')
Shrimp_Splitpeas_breastmilk = pd.read_csv('data/Shrimp_Splitpeas_breastmilk.csv')
Shrimp_Strawberries_breastmilk = pd.read_csv('data/Shrimp_Strawberries_breastmilk.csv')
Shrimp_Sweetpotato_breastmilk = pd.read_csv('data/Shrimp_Sweetpotato_breastmilk.csv')
Soybean_Splitpeas_breastmilk = pd.read_csv('data/Soybean_Splitpeas_breastmilk.csv')
Soybean_Strawberries_breastmilk = pd.read_csv('data/Soybean_Strawberries_breastmilk.csv')
Soybean_Sweetpotato_breastmilk = pd.read_csv('data/Soybean_Sweetpotato_breastmilk.csv')
Splitpeas_Strawberries_breastmilk = pd.read_csv('data/Splitpeas_Strawberries_breastmilk.csv')
Splitpeas_Sweetpotato_breastmilk = pd.read_csv('data/Splitpeas_Sweetpotato_breastmilk.csv')
Strawberries_Sweetpotato_breastmilk = pd.read_csv('data/Strawberries_Sweetpotato_breastmilk.csv')
Control_Breastmilk = pd.read_csv('data/Breastmilk.csv')
Control_Infant_formula = pd.read_csv('data/Infant_formula.csv')

#Choosing the tradeoff
#normally 0.3-0.6 works good
#largest tradeoff that allows the majority of the bacteria to grow 
#compromise between individual and cooperative growth
from micom.workflows import tradeoff
from micom.viz import plot_tradeoff

tradeoff_Blackbeans_Blackcurrant_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Blackbeans_Blackcurrant_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Blackbeans_Blackcurrant_breastmilk, filename="results/tradeoff_Blackbeans_Blackcurrant_breastmilk.html")
tradeoff_Blackbeans_Chickpea_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Blackbeans_Chickpea_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Blackbeans_Chickpea_breastmilk, filename="results/tradeoff_Blackbeans_Chickpea_breastmilk.html")
tradeoff_Blackbeans_Couscous_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Blackbeans_Couscous_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Blackbeans_Couscous_breastmilk, filename="results/tradeoff_Blackbeans_Couscous_breastmilk.html")
tradeoff_Blackbeans_Pork_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Blackbeans_Pork_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Blackbeans_Pork_breastmilk, filename="results/tradeoff_Blackbeans_Pork_breastmilk.html")
tradeoff_Blackbeans_Pumpkin_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Blackbeans_Pumpkin_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Blackbeans_Pumpkin_breastmilk, filename="results/tradeoff_Blackbeans_Pumpkin_breastmilk.html")
tradeoff_Blackbeans_Raspberries_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Blackbeans_Raspberries_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Blackbeans_Raspberries_breastmilk, filename="results/tradeoff_Blackbeans_Raspberries_breastmilk.html")
tradeoff_Blackbeans_Shrimp_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Blackbeans_Shrimp_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Blackbeans_Shrimp_breastmilk, filename="results/tradeoff_Blackbeans_Shrimp_breastmilk.html")
tradeoff_Blackbeans_Soybean_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Blackbeans_Soybean_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Blackbeans_Soybean_breastmilk, filename="results/tradeoff_Blackbeans_Soybean_breastmilk.html")
tradeoff_Blackbeans_Splitpeas_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Blackbeans_Splitpeas_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Blackbeans_Splitpeas_breastmilk, filename="results/tradeoff_Blackbeans_Splitpeas_breastmilk.html")
tradeoff_Blackbeans_Strawberries_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Blackbeans_Strawberries_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Blackbeans_Strawberries_breastmilk, filename="results/tradeoff_Blackbeans_Strawberries_breastmilk.html")
tradeoff_Blackbeans_Sweetpotato_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Blackbeans_Sweetpotato_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Blackbeans_Sweetpotato_breastmilk, filename="results/tradeoff_Blackbeans_Sweetpotato_breastmilk.html")
tradeoff_Blackcurrant_Chickpea_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Blackcurrant_Chickpea_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Blackcurrant_Chickpea_breastmilk, filename="results/tradeoff_Blackcurrant_Chickpea_breastmilk.html")
tradeoff_Blackcurrant_Couscous_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Blackcurrant_Couscous_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Blackcurrant_Couscous_breastmilk, filename="results/tradeoff_Blackcurrant_Couscous_breastmilk.html")
tradeoff_Blackcurrant_Pork_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Blackcurrant_Pork_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Blackcurrant_Pork_breastmilk, filename="results/tradeoff_Blackcurrant_Pork_breastmilk.html")
tradeoff_Blackcurrant_Pumpkin_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Blackcurrant_Pumpkin_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Blackcurrant_Pumpkin_breastmilk, filename="results/tradeoff_Blackcurrant_Pumpkin_breastmilk.html")
tradeoff_Blackcurrant_Raspberries_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Blackcurrant_Raspberries_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Blackcurrant_Raspberries_breastmilk, filename="results/tradeoff_Blackcurrant_Raspberries_breastmilk.html")
tradeoff_Blackcurrant_Shrimp_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Blackcurrant_Shrimp_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Blackcurrant_Shrimp_breastmilk, filename="results/tradeoff_Blackcurrant_Shrimp_breastmilk.html")
tradeoff_Blackcurrant_Soybean_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Blackcurrant_Soybean_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Blackcurrant_Soybean_breastmilk, filename="results/tradeoff_Blackcurrant_Soybean_breastmilk.html")
tradeoff_Blackcurrant_Splitpeas_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Blackcurrant_Splitpeas_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Blackcurrant_Splitpeas_breastmilk, filename="results/tradeoff_Blackcurrant_Splitpeas_breastmilk.html")
tradeoff_Blackcurrant_Strawberries_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Blackcurrant_Strawberries_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Blackcurrant_Strawberries_breastmilk, filename="results/tradeoff_Blackcurrant_Strawberries_breastmilk.html")
tradeoff_Blackcurrant_Sweetpotato_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Blackcurrant_Sweetpotato_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Blackcurrant_Sweetpotato_breastmilk, filename="results/tradeoff_Blackcurrant_Sweetpotato_breastmilk.html")
tradeoff_Chickpea_Couscous_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Chickpea_Couscous_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Chickpea_Couscous_breastmilk, filename="results/tradeoff_Chickpea_Couscous_breastmilk.html")
tradeoff_Chickpea_Pork_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Chickpea_Pork_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Chickpea_Pork_breastmilk, filename="results/tradeoff_Chickpea_Pork_breastmilk.html")
tradeoff_Chickpea_Pumpkin_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Chickpea_Pumpkin_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Chickpea_Pumpkin_breastmilk, filename="results/tradeoff_Chickpea_Pumpkin_breastmilk.html")
tradeoff_Chickpea_Raspberries_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Chickpea_Raspberries_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Chickpea_Raspberries_breastmilk, filename="results/tradeoff_Chickpea_Raspberries_breastmilk.html")
tradeoff_Chickpea_Shrimp_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Chickpea_Shrimp_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Chickpea_Shrimp_breastmilk, filename="results/tradeoff_Chickpea_Shrimp_breastmilk.html")
tradeoff_Chickpea_Soybean_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Chickpea_Soybean_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Chickpea_Soybean_breastmilk, filename="results/tradeoff_Chickpea_Soybean_breastmilk.html")
tradeoff_Chickpea_Splitpeas_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Chickpea_Splitpeas_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Chickpea_Splitpeas_breastmilk, filename="results/tradeoff_Chickpea_Splitpeas_breastmilk.html")
tradeoff_Chickpea_Strawberries_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Chickpea_Strawberries_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Chickpea_Strawberries_breastmilk, filename="results/tradeoff_Chickpea_Strawberries_breastmilk.html")
tradeoff_Chickpea_Sweetpotato_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Chickpea_Sweetpotato_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Chickpea_Sweetpotato_breastmilk, filename="results/tradeoff_Chickpea_Sweetpotato_breastmilk.html")
tradeoff_Couscous_Pork_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Couscous_Pork_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Couscous_Pork_breastmilk, filename="results/tradeoff_Couscous_Pork_breastmilk.html")
tradeoff_Couscous_Pumpkin_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Couscous_Pumpkin_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Couscous_Pumpkin_breastmilk, filename="results/tradeoff_Couscous_Pumpkin_breastmilk.html")
tradeoff_Couscous_Raspberries_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Couscous_Raspberries_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Couscous_Raspberries_breastmilk, filename="results/tradeoff_Couscous_Raspberries_breastmilk.html")
tradeoff_Couscous_Shrimp_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Couscous_Shrimp_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Couscous_Shrimp_breastmilk, filename="results/tradeoff_Couscous_Shrimp_breastmilk.html")
tradeoff_Couscous_Soybean_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Couscous_Soybean_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Couscous_Soybean_breastmilk, filename="results/tradeoff_Couscous_Soybean_breastmilk.html")
tradeoff_Couscous_Splitpeas_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Couscous_Splitpeas_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Couscous_Splitpeas_breastmilk, filename="results/tradeoff_Couscous_Splitpeas_breastmilk.html")
tradeoff_Couscous_Strawberries_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Couscous_Strawberries_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Couscous_Strawberries_breastmilk, filename="results/tradeoff_Couscous_Strawberries_breastmilk.html")
tradeoff_Couscous_Sweetpotato_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Couscous_Sweetpotato_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Couscous_Sweetpotato_breastmilk, filename="results/tradeoff_Couscous_Sweetpotato_breastmilk.html")
tradeoff_Pork_Pumpkin_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Pork_Pumpkin_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Pork_Pumpkin_breastmilk, filename="results/tradeoff_Pork_Pumpkin_breastmilk.html")
tradeoff_Pork_Raspberries_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Pork_Raspberries_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Pork_Raspberries_breastmilk, filename="results/tradeoff_Pork_Raspberries_breastmilk.html")
tradeoff_Pork_Shrimp_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Pork_Shrimp_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Pork_Shrimp_breastmilk, filename="results/tradeoff_Pork_Shrimp_breastmilk.html")
tradeoff_Pork_Soybean_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Pork_Soybean_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Pork_Soybean_breastmilk, filename="results/tradeoff_Pork_Soybean_breastmilk.html")
tradeoff_Pork_Splitpeas_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Pork_Splitpeas_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Pork_Splitpeas_breastmilk, filename="results/tradeoff_Pork_Splitpeas_breastmilk.html")
tradeoff_Pork_Strawberries_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Pork_Strawberries_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Pork_Strawberries_breastmilk, filename="results/tradeoff_Pork_Strawberries_breastmilk.html")
tradeoff_Pork_Sweetpotato_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Pork_Sweetpotato_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Pork_Sweetpotato_breastmilk, filename="results/tradeoff_Pork_Sweetpotato_breastmilk.html")
tradeoff_Pumpkin_Raspberries_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Pumpkin_Raspberries_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Pumpkin_Raspberries_breastmilk, filename="results/tradeoff_Pumpkin_Raspberries_breastmilk.html")
tradeoff_Pumpkin_Shrimp_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Pumpkin_Shrimp_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Pumpkin_Shrimp_breastmilk, filename="results/tradeoff_Pumpkin_Shrimp_breastmilk.html")
tradeoff_Pumpkin_Soybean_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Pumpkin_Soybean_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Pumpkin_Soybean_breastmilk, filename="results/tradeoff_Pumpkin_Soybean_breastmilk.html")
tradeoff_Pumpkin_Splitpeas_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Pumpkin_Splitpeas_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Pumpkin_Splitpeas_breastmilk, filename="results/tradeoff_Pumpkin_Splitpeas_breastmilk.html")
tradeoff_Pumpkin_Strawberries_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Pumpkin_Strawberries_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Pumpkin_Strawberries_breastmilk, filename="results/tradeoff_Pumpkin_Strawberries_breastmilk.html")
tradeoff_Pumpkin_Sweetpotato_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Pumpkin_Sweetpotato_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Pumpkin_Sweetpotato_breastmilk, filename="results/tradeoff_Pumpkin_Sweetpotato_breastmilk.html")
tradeoff_Raspberries_Shrimp_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Raspberries_Shrimp_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Raspberries_Shrimp_breastmilk, filename="results/tradeoff_Raspberries_Shrimp_breastmilk.html")
tradeoff_Raspberries_Soybean_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Raspberries_Soybean_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Raspberries_Soybean_breastmilk, filename="results/tradeoff_Raspberries_Soybean_breastmilk.html")
tradeoff_Raspberries_Splitpeas_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Raspberries_Splitpeas_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Raspberries_Splitpeas_breastmilk, filename="results/tradeoff_Raspberries_Splitpeas_breastmilk.html")
tradeoff_Raspberries_Strawberries_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Raspberries_Strawberries_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Raspberries_Strawberries_breastmilk, filename="results/tradeoff_Raspberries_Strawberries_breastmilk.html")
tradeoff_Raspberries_Sweetpotato_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Raspberries_Sweetpotato_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Raspberries_Sweetpotato_breastmilk, filename="results/tradeoff_Raspberries_Sweetpotato_breastmilk.html")
tradeoff_Shrimp_Soybean_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Shrimp_Soybean_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Shrimp_Soybean_breastmilk, filename="results/tradeoff_Shrimp_Soybean_breastmilk.html")
tradeoff_Shrimp_Splitpeas_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Shrimp_Splitpeas_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Shrimp_Splitpeas_breastmilk, filename="results/tradeoff_Shrimp_Splitpeas_breastmilk.html")
tradeoff_Shrimp_Strawberries_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Shrimp_Strawberries_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Shrimp_Strawberries_breastmilk, filename="results/tradeoff_Shrimp_Strawberries_breastmilk.html")
tradeoff_Shrimp_Sweetpotato_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Shrimp_Sweetpotato_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Shrimp_Sweetpotato_breastmilk, filename="results/tradeoff_Shrimp_Sweetpotato_breastmilk.html")
tradeoff_Soybean_Splitpeas_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Soybean_Splitpeas_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Soybean_Splitpeas_breastmilk, filename="results/tradeoff_Soybean_Splitpeas_breastmilk.html")
tradeoff_Soybean_Strawberries_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Soybean_Strawberries_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Soybean_Strawberries_breastmilk, filename="results/tradeoff_Soybean_Strawberries_breastmilk.html")
tradeoff_Soybean_Sweetpotato_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Soybean_Sweetpotato_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Soybean_Sweetpotato_breastmilk, filename="results/tradeoff_Soybean_Sweetpotato_breastmilk.html")
tradeoff_Splitpeas_Strawberries_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Splitpeas_Strawberries_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Splitpeas_Strawberries_breastmilk, filename="results/tradeoff_Splitpeas_Strawberries_breastmilk.html")
tradeoff_Splitpeas_Sweetpotato_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Splitpeas_Sweetpotato_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Splitpeas_Sweetpotato_breastmilk, filename="results/tradeoff_Splitpeas_Sweetpotato_breastmilk.html")
tradeoff_Strawberries_Sweetpotato_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Strawberries_Sweetpotato_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Strawberries_Sweetpotato_breastmilk, filename="results/tradeoff_Strawberries_Sweetpotato_breastmilk.html")
tradeoff_Control_Breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Control_Breastmilk, threads=14) 
plot_tradeoff(tradeoff_Control_Breastmilk, filename="results/tradeoff_Control_Breastmilk.html")
tradeoff_Control_Infant_formula = tradeoff(manifest, model_folder="models_cplex", medium=Control_Infant_formula, threads=14) 
plot_tradeoff(tradeoff_Control_Infant_formula, filename="results/tradeoff_Control_Infant_formula.html")

##Growing the models
from micom.workflows import grow, save_results

res_Blackbeans_Blackcurrant_breastmilk = grow(manifest, model_folder="models_cplex", medium=Blackbeans_Blackcurrant_breastmilk, tradeoff=0.3, threads=14) 
save_results(res_Blackbeans_Blackcurrant_breastmilk, "results/Blackbeans_Blackcurrant_breastmilk.zip") 
res_Blackbeans_Chickpea_breastmilk = grow(manifest, model_folder="models_cplex", medium=Blackbeans_Chickpea_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Blackbeans_Chickpea_breastmilk, "results/Blackbeans_Chickpea_breastmilk.zip")
res_Blackbeans_Couscous_breastmilk = grow(manifest, model_folder="models_cplex", medium=Blackbeans_Couscous_breastmilk, tradeoff=0.6, threads=14) 
save_results(res_Blackbeans_Couscous_breastmilk, "results/Blackbeans_Couscous_breastmilk.zip") 
res_Blackbeans_Pork_breastmilk = grow(manifest, model_folder="models_cplex", medium=Blackbeans_Pork_breastmilk, tradeoff=0.9, threads=14) 
save_results(res_Blackbeans_Pork_breastmilk, "results/Blackbeans_Pork_breastmilk.zip")  
res_Blackbeans_Pumpkin_breastmilk = grow(manifest, model_folder="models_cplex", medium=Blackbeans_Pumpkin_breastmilk, tradeoff=0.7, threads=14) 
save_results(res_Blackbeans_Pumpkin_breastmilk, "results/Blackbeans_Pumpkin_breastmilk.zip") 
res_Blackbeans_Raspberries_breastmilk = grow(manifest, model_folder="models_cplex", medium=Blackbeans_Raspberries_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Blackbeans_Raspberries_breastmilk, "results/Blackbeans_Raspberries_breastmilk.zip") 
res_Blackbeans_Shrimp_breastmilk = grow(manifest, model_folder="models_cplex", medium=Blackbeans_Shrimp_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Blackbeans_Shrimp_breastmilk, "results/Blackbeans_Shrimp_breastmilk.zip")
res_Blackbeans_Soybean_breastmilk = grow(manifest, model_folder="models_cplex", medium=Blackbeans_Soybean_breastmilk, tradeoff=0.9, threads=14) 
save_results(res_Blackbeans_Soybean_breastmilk, "results/Blackbeans_Soybean_breastmilk.zip") 
res_Blackbeans_Splitpeas_breastmilk = grow(manifest, model_folder="models_cplex", medium=Blackbeans_Splitpeas_breastmilk, tradeoff=0.9, threads=14) 
save_results(res_Blackbeans_Splitpeas_breastmilk, "results/Blackbeans_Splitpeas_breastmilk.zip")  
res_Blackbeans_Strawberries_breastmilk = grow(manifest, model_folder="models_cplex", medium=Blackbeans_Strawberries_breastmilk, tradeoff=0.7, threads=14) 
save_results(res_Blackbeans_Strawberries_breastmilk, "results/Blackbeans_Strawberries_breastmilk.zip") 
res_Blackbeans_Sweetpotato_breastmilk = grow(manifest, model_folder="models_cplex", medium=Blackbeans_Sweetpotato_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Blackbeans_Sweetpotato_breastmilk, "results/Blackbeans_Sweetpotato_breastmilk.zip") 
res_Blackcurrant_Chickpea_breastmilk = grow(manifest, model_folder="models_cplex", medium=Blackcurrant_Chickpea_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Blackcurrant_Chickpea_breastmilk, "results/Blackcurrant_Chickpea_breastmilk.zip")
res_Blackcurrant_Couscous_breastmilk = grow(manifest, model_folder="models_cplex", medium=Blackcurrant_Couscous_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Blackcurrant_Couscous_breastmilk, "results/Blackcurrant_Couscous_breastmilk.zip") 
res_Blackcurrant_Pork_breastmilk = grow(manifest, model_folder="models_cplex", medium=Blackcurrant_Pork_breastmilk, tradeoff=0.9, threads=14) 
save_results(res_Blackcurrant_Pork_breastmilk, "results/Blackcurrant_Pork_breastmilk.zip")  
res_Blackcurrant_Pumpkin_breastmilk = grow(manifest, model_folder="models_cplex", medium=Blackcurrant_Pumpkin_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Blackcurrant_Pumpkin_breastmilk, "results/Blackcurrant_Pumpkin_breastmilk.zip") 
res_Blackcurrant_Raspberries_breastmilk = grow(manifest, model_folder="models_cplex", medium=Blackcurrant_Raspberries_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Blackcurrant_Raspberries_breastmilk, "results/Blackcurrant_Raspberries_breastmilk.zip") 
res_Blackcurrant_Shrimp_breastmilk = grow(manifest, model_folder="models_cplex", medium=Blackcurrant_Shrimp_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Blackcurrant_Shrimp_breastmilk, "results/Blackcurrant_Shrimp_breastmilk.zip")
res_Blackcurrant_Soybean_breastmilk = grow(manifest, model_folder="models_cplex", medium=Blackcurrant_Soybean_breastmilk, tradeoff=0.9, threads=14) 
save_results(res_Blackcurrant_Soybean_breastmilk, "results/Blackcurrant_Soybean_breastmilk.zip") 
res_Blackcurrant_Splitpeas_breastmilk = grow(manifest, model_folder="models_cplex", medium=Blackcurrant_Splitpeas_breastmilk, tradeoff=0.7, threads=14) 
save_results(res_Blackcurrant_Splitpeas_breastmilk, "results/Blackcurrant_Splitpeas_breastmilk.zip")  
res_Blackcurrant_Strawberries_breastmilk = grow(manifest, model_folder="models_cplex", medium=Blackcurrant_Strawberries_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Blackcurrant_Strawberries_breastmilk, "results/Blackcurrant_Strawberries_breastmilk.zip") 
res_Blackcurrant_Sweetpotato_breastmilk = grow(manifest, model_folder="models_cplex", medium=Blackcurrant_Sweetpotato_breastmilk, tradeoff=0.9, threads=14) 
save_results(res_Blackcurrant_Sweetpotato_breastmilk, "results/Blackcurrant_Sweetpotato_breastmilk.zip") 
res_Chickpea_Couscous_breastmilk = grow(manifest, model_folder="models_cplex", medium=Chickpea_Couscous_breastmilk, tradeoff=0.9, threads=14) 
save_results(res_Chickpea_Couscous_breastmilk, "results/Chickpea_Couscous_breastmilk.zip")
res_Chickpea_Pork_breastmilk = grow(manifest, model_folder="models_cplex", medium=Chickpea_Pork_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Chickpea_Pork_breastmilk, "results/Chickpea_Pork_breastmilk.zip") 
res_Chickpea_Pumpkin_breastmilk = grow(manifest, model_folder="models_cplex", medium=Chickpea_Pumpkin_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Chickpea_Pumpkin_breastmilk, "results/Chickpea_Pumpkin_breastmilk.zip")  
res_Chickpea_Raspberries_breastmilk = grow(manifest, model_folder="models_cplex", medium=Chickpea_Raspberries_breastmilk, tradeoff=0.7, threads=14) 
save_results(res_Chickpea_Raspberries_breastmilk, "results/Chickpea_Raspberries_breastmilk.zip") 
res_Chickpea_Shrimp_breastmilk = grow(manifest, model_folder="models_cplex", medium=Chickpea_Shrimp_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Chickpea_Shrimp_breastmilk, "results/Chickpea_Shrimp_breastmilk.zip") 
res_Chickpea_Soybean_breastmilk = grow(manifest, model_folder="models_cplex", medium=Chickpea_Soybean_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Chickpea_Soybean_breastmilk, "results/Chickpea_Soybean_breastmilk.zip")
res_Chickpea_Splitpeas_breastmilk = grow(manifest, model_folder="models_cplex", medium=Chickpea_Splitpeas_breastmilk, tradeoff=0.4, threads=14) 
save_results(res_Chickpea_Splitpeas_breastmilk, "results/Chickpea_Splitpeas_breastmilk.zip") 
res_Chickpea_Strawberries_breastmilk = grow(manifest, model_folder="models_cplex", medium=Chickpea_Strawberries_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Chickpea_Strawberries_breastmilk, "results/Chickpea_Strawberries_breastmilk.zip")  
res_Chickpea_Sweetpotato_breastmilk = grow(manifest, model_folder="models_cplex", medium=Chickpea_Sweetpotato_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Chickpea_Sweetpotato_breastmilk, "results/Chickpea_Sweetpotato_breastmilk.zip") 
res_Couscous_Pork_breastmilk = grow(manifest, model_folder="models_cplex", medium=Couscous_Pork_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Couscous_Pork_breastmilk, "results/Couscous_Pork_breastmilk.zip") 
res_Couscous_Pumpkin_breastmilk = grow(manifest, model_folder="models_cplex", medium=Couscous_Pumpkin_breastmilk, tradeoff=0.7, threads=14) 
save_results(res_Couscous_Pumpkin_breastmilk, "results/Couscous_Pumpkin_breastmilk.zip")
res_Couscous_Raspberries_breastmilk = grow(manifest, model_folder="models_cplex", medium=Couscous_Raspberries_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Couscous_Raspberries_breastmilk, "results/Couscous_Raspberries_breastmilk.zip") 
res_Couscous_Shrimp_breastmilk = grow(manifest, model_folder="models_cplex", medium=Couscous_Shrimp_breastmilk, tradeoff=0.9, threads=14) 
save_results(res_Couscous_Shrimp_breastmilk, "results/Couscous_Shrimp_breastmilk.zip")  
res_Couscous_Soybean_breastmilk = grow(manifest, model_folder="models_cplex", medium=Couscous_Soybean_breastmilk, tradeoff=0.9, threads=14) 
save_results(res_Couscous_Soybean_breastmilk, "results/Couscous_Soybean_breastmilk.zip") 
res_Couscous_Splitpeas_breastmilk = grow(manifest, model_folder="models_cplex", medium=Couscous_Splitpeas_breastmilk, tradeoff=0.7, threads=14) 
save_results(res_Couscous_Splitpeas_breastmilk, "results/Couscous_Splitpeas_breastmilk.zip") 
res_Couscous_Strawberries_breastmilk = grow(manifest, model_folder="models_cplex", medium=Couscous_Strawberries_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Couscous_Strawberries_breastmilk, "results/Couscous_Strawberries_breastmilk.zip")
res_Couscous_Sweetpotato_breastmilk = grow(manifest, model_folder="models_cplex", medium=Couscous_Sweetpotato_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Couscous_Sweetpotato_breastmilk, "results/Couscous_Sweetpotato_breastmilk.zip") 
res_Pork_Pumpkin_breastmilk = grow(manifest, model_folder="models_cplex", medium=Pork_Pumpkin_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Pork_Pumpkin_breastmilk, "results/Pork_Pumpkin_breastmilk.zip")  
res_Pork_Raspberries_breastmilk = grow(manifest, model_folder="models_cplex", medium=Pork_Raspberries_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Pork_Raspberries_breastmilk, "results/Pork_Raspberries_breastmilk.zip") 
res_Pork_Shrimp_breastmilk = grow(manifest, model_folder="models_cplex", medium=Pork_Shrimp_breastmilk, tradeoff=0.6, threads=14) 
save_results(res_Pork_Shrimp_breastmilk, "results/Pork_Shrimp_breastmilk.zip") 
res_Pork_Soybean_breastmilk = grow(manifest, model_folder="models_cplex", medium=Pork_Soybean_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Pork_Soybean_breastmilk, "results/Pork_Soybean_breastmilk.zip")
res_Pork_Splitpeas_breastmilk = grow(manifest, model_folder="models_cplex", medium=Pork_Splitpeas_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Pork_Splitpeas_breastmilk, "results/Pork_Splitpeas_breastmilk.zip") 
res_Pork_Strawberries_breastmilk = grow(manifest, model_folder="models_cplex", medium=Pork_Strawberries_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Pork_Strawberries_breastmilk, "results/Pork_Strawberries_breastmilk.zip")  
res_Pork_Sweetpotato_breastmilk = grow(manifest, model_folder="models_cplex", medium=Pork_Sweetpotato_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Pork_Sweetpotato_breastmilk, "results/Pork_Sweetpotato_breastmilk.zip") 
res_Pumpkin_Raspberries_breastmilk = grow(manifest, model_folder="models_cplex", medium=Pumpkin_Raspberries_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Pumpkin_Raspberries_breastmilk, "results/Pumpkin_Raspberries_breastmilk.zip") 
res_Pumpkin_Shrimp_breastmilk = grow(manifest, model_folder="models_cplex", medium=Pumpkin_Shrimp_breastmilk, tradeoff=0.6, threads=14) 
save_results(res_Pumpkin_Shrimp_breastmilk, "results/Pumpkin_Shrimp_breastmilk.zip")
res_Pumpkin_Soybean_breastmilk = grow(manifest, model_folder="models_cplex", medium=Pumpkin_Soybean_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Pumpkin_Soybean_breastmilk, "results/Pumpkin_Soybean_breastmilk.zip") 
res_Pumpkin_Splitpeas_breastmilk = grow(manifest, model_folder="models_cplex", medium=Pumpkin_Splitpeas_breastmilk, tradeoff=0.9, threads=14) 
save_results(res_Pumpkin_Splitpeas_breastmilk, "results/Pumpkin_Splitpeas_breastmilk.zip")  
res_Pumpkin_Strawberries_breastmilk = grow(manifest, model_folder="models_cplex", medium=Pumpkin_Strawberries_breastmilk, tradeoff=0.9, threads=14) 
save_results(res_Pumpkin_Strawberries_breastmilk, "results/Pumpkin_Strawberries_breastmilk.zip") 
res_Pumpkin_Sweetpotato_breastmilk = grow(manifest, model_folder="models_cplex", medium=Pumpkin_Sweetpotato_breastmilk, tradeoff=0.9, threads=14) 
save_results(res_Pumpkin_Sweetpotato_breastmilk, "results/Pumpkin_Sweetpotato_breastmilk.zip") 
res_Raspberries_Shrimp_breastmilk = grow(manifest, model_folder="models_cplex", medium=Raspberries_Shrimp_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Raspberries_Shrimp_breastmilk, "results/Raspberries_Shrimp_breastmilk.zip")
res_Raspberries_Soybean_breastmilk = grow(manifest, model_folder="models_cplex", medium=Raspberries_Soybean_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Raspberries_Soybean_breastmilk, "results/Raspberries_Soybean_breastmilk.zip") 
res_Raspberries_Splitpeas_breastmilk = grow(manifest, model_folder="models_cplex", medium=Raspberries_Splitpeas_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Raspberries_Splitpeas_breastmilk, "results/Raspberries_Splitpeas_breastmilk.zip")  
res_Raspberries_Strawberries_breastmilk = grow(manifest, model_folder="models_cplex", medium=Raspberries_Strawberries_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Raspberries_Strawberries_breastmilk, "results/Raspberries_Strawberries_breastmilk.zip") 
res_Raspberries_Sweetpotato_breastmilk = grow(manifest, model_folder="models_cplex", medium=Raspberries_Sweetpotato_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Raspberries_Sweetpotato_breastmilk, "results/Raspberries_Sweetpotato_breastmilk.zip") 
res_Shrimp_Soybean_breastmilk = grow(manifest, model_folder="models_cplex", medium=Shrimp_Soybean_breastmilk, tradeoff=0.6, threads=14) 
save_results(res_Shrimp_Soybean_breastmilk, "results/Shrimp_Soybean_breastmilk.zip")
res_Shrimp_Splitpeas_breastmilk = grow(manifest, model_folder="models_cplex", medium=Shrimp_Splitpeas_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Shrimp_Splitpeas_breastmilk, "results/Shrimp_Splitpeas_breastmilk.zip") 
res_Shrimp_Strawberries_breastmilk = grow(manifest, model_folder="models_cplex", medium=Shrimp_Strawberries_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Shrimp_Strawberries_breastmilk, "results/Shrimp_Strawberries_breastmilk.zip")  
res_Shrimp_Sweetpotato_breastmilk = grow(manifest, model_folder="models_cplex", medium=Shrimp_Sweetpotato_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Shrimp_Sweetpotato_breastmilk, "results/Shrimp_Sweetpotato_breastmilk.zip") 
res_Soybean_Splitpeas_breastmilk = grow(manifest, model_folder="models_cplex", medium=Soybean_Splitpeas_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Soybean_Splitpeas_breastmilk, "results/Soybean_Splitpeas_breastmilk.zip") 
res_Soybean_Strawberries_breastmilk = grow(manifest, model_folder="models_cplex", medium=Soybean_Strawberries_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Soybean_Strawberries_breastmilk, "results/Soybean_Strawberries_breastmilk.zip")
res_Soybean_Sweetpotato_breastmilk = grow(manifest, model_folder="models_cplex", medium=Soybean_Sweetpotato_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Soybean_Sweetpotato_breastmilk, "results/Soybean_Sweetpotato_breastmilk.zip") 
res_Splitpeas_Strawberries_breastmilk = grow(manifest, model_folder="models_cplex", medium=Splitpeas_Strawberries_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Splitpeas_Strawberries_breastmilk, "results/Splitpeas_Strawberries_breastmilk.zip")  
res_Splitpeas_Sweetpotato_breastmilk = grow(manifest, model_folder="models_cplex", medium=Splitpeas_Sweetpotato_breastmilk, tradeoff=0.9, threads=14) 
save_results(res_Splitpeas_Sweetpotato_breastmilk, "results/Splitpeas_Sweetpotato_breastmilk.zip") 
res_Strawberries_Sweetpotato_breastmilk = grow(manifest, model_folder="models_cplex", medium=Strawberries_Sweetpotato_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Strawberries_Sweetpotato_breastmilk, "results/Strawberries_Sweetpotato_breastmilk.zip") 
res_Control_Breastmilk = grow(manifest, model_folder="models_cplex", medium=Control_Breastmilk, tradeoff=0.9, threads=14) 
save_results(res_Control_Breastmilk, "results/Control_Breastmilk.zip")
res_Control_Infant_formula = grow(manifest, model_folder="models_cplex", medium=Control_Infant_formula, tradeoff=0.8, threads=14) 
save_results(res_Control_Infant_formula, "results/Control_Infant_formula.zip") 

#Visualisations
from micom.viz import plot_growth
#Growth rates

plot_growth(res_Blackbeans_Blackcurrant_breastmilk, filename="results/growth_rates_Blackbeans_Blackcurrant_breastmilk.html")  
plot_growth(res_Blackbeans_Chickpea_breastmilk, filename="results/growth_rates_Blackbeans_Chickpea_breastmilk.html") 
plot_growth(res_Blackbeans_Couscous_breastmilk, filename="results/growth_rates_Blackbeans_Couscous_breastmilk.html")  
plot_growth(res_Blackbeans_Pork_breastmilk, filename="results/growth_rates_Blackbeans_Pork_breastmilk.html") 
plot_growth(res_Blackbeans_Pumpkin_breastmilk, filename="results/growth_rates_Blackbeans_Pumpkin_breastmilk.html") 
plot_growth(res_Blackbeans_Raspberries_breastmilk, filename="results/growth_rates_Blackbeans_Raspberries_breastmilk.html")  
plot_growth(res_Blackbeans_Shrimp_breastmilk, filename="results/growth_rates_Blackbeans_Shrimp_breastmilk.html") 
plot_growth(res_Blackbeans_Soybean_breastmilk, filename="results/growth_rates_Blackbeans_Soybean_breastmilk.html")  
plot_growth(res_Blackbeans_Splitpeas_breastmilk, filename="results/growth_rates_Blackbeans_Splitpeas_breastmilk.html") 
plot_growth(res_Blackbeans_Strawberries_breastmilk, filename="results/growth_rates_Blackbeans_Strawberries_breastmilk.html")
plot_growth(res_Blackbeans_Sweetpotato_breastmilk, filename="results/growth_rates_Blackbeans_Sweetpotato_breastmilk.html")  
plot_growth(res_Blackcurrant_Chickpea_breastmilk, filename="results/growth_rates_Blackcurrant_Chickpea_breastmilk.html") 
plot_growth(res_Blackcurrant_Couscous_breastmilk, filename="results/growth_rates_Blackcurrant_Couscous_breastmilk.html")  
plot_growth(res_Blackcurrant_Pork_breastmilk, filename="results/growth_rates_Blackcurrant_Pork_breastmilk.html") 
plot_growth(res_Blackcurrant_Pumpkin_breastmilk, filename="results/growth_rates_Blackcurrant_Pumpkin_breastmilk.html") 
plot_growth(res_Blackcurrant_Raspberries_breastmilk, filename="results/growth_rates_Blackcurrant_Raspberries_breastmilk.html")  
plot_growth(res_Blackcurrant_Shrimp_breastmilk, filename="results/growth_rates_Blackcurrant_Shrimp_breastmilk.html") 
plot_growth(res_Blackcurrant_Soybean_breastmilk, filename="results/growth_rates_Blackcurrant_Soybean_breastmilk.html")  
plot_growth(res_Blackcurrant_Splitpeas_breastmilk, filename="results/growth_rates_Blackcurrant_Splitpeas_breastmilk.html") 
plot_growth(res_Blackcurrant_Strawberries_breastmilk, filename="results/growth_rates_Blackcurrant_Strawberries_breastmilk.html") 
plot_growth(res_Blackcurrant_Sweetpotato_breastmilk, filename="results/growth_rates_Blackcurrant_Sweetpotato_breastmilk.html")  
plot_growth(res_Chickpea_Couscous_breastmilk, filename="results/growth_rates_Chickpea_Couscous_breastmilk.html") 
plot_growth(res_Chickpea_Pork_breastmilk, filename="results/growth_rates_Chickpea_Pork_breastmilk.html")  
plot_growth(res_Chickpea_Pumpkin_breastmilk, filename="results/growth_rates_Chickpea_Pumpkin_breastmilk.html") 
plot_growth(res_Chickpea_Raspberries_breastmilk, filename="results/growth_rates_Chickpea_Raspberries_breastmilk.html")
plot_growth(res_Chickpea_Shrimp_breastmilk, filename="results/growth_rates_Chickpea_Shrimp_breastmilk.html")  
plot_growth(res_Chickpea_Soybean_breastmilk, filename="results/growth_rates_Chickpea_Soybean_breastmilk.html") 
plot_growth(res_Chickpea_Splitpeas_breastmilk, filename="results/growth_rates_Chickpea_Splitpeas_breastmilk.html")  
plot_growth(res_Chickpea_Strawberries_breastmilk, filename="results/growth_rates_Chickpea_Strawberries_breastmilk.html") 
plot_growth(res_Chickpea_Sweetpotato_breastmilk, filename="results/growth_rates_Chickpea_Sweetpotato_breastmilk.html") 
plot_growth(res_Couscous_Pork_breastmilk, filename="results/growth_rates_Couscous_Pork_breastmilk.html")  
plot_growth(res_Couscous_Pumpkin_breastmilk, filename="results/growth_rates_Couscous_Pumpkin_breastmilk.html") 
plot_growth(res_Couscous_Raspberries_breastmilk, filename="results/growth_rates_Couscous_Raspberries_breastmilk.html")  
plot_growth(res_Couscous_Shrimp_breastmilk, filename="results/growth_rates_Couscous_Shrimp_breastmilk.html") 
plot_growth(res_Couscous_Soybean_breastmilk, filename="results/growth_rates_Couscous_Soybean_breastmilk.html") 
plot_growth(res_Couscous_Splitpeas_breastmilk, filename="results/growth_rates_Couscous_Splitpeas_breastmilk.html")  
plot_growth(res_Couscous_Strawberries_breastmilk, filename="results/growth_rates_Couscous_Strawberries_breastmilk.html") 
plot_growth(res_Couscous_Sweetpotato_breastmilk, filename="results/growth_rates_Couscous_Sweetpotato_breastmilk.html")  
plot_growth(res_Pork_Pumpkin_breastmilk, filename="results/growth_rates_Pork_Pumpkin_breastmilk.html") 
plot_growth(res_Pork_Raspberries_breastmilk, filename="results/growth_rates_Pork_Raspberries_breastmilk.html")
plot_growth(res_Pork_Shrimp_breastmilk, filename="results/growth_rates_Pork_Shrimp_breastmilk.html")  
plot_growth(res_Pork_Soybean_breastmilk, filename="results/growth_rates_Pork_Soybean_breastmilk.html") 
plot_growth(res_Pork_Splitpeas_breastmilk, filename="results/growth_rates_Pork_Splitpeas_breastmilk.html")  
plot_growth(res_Pork_Strawberries_breastmilk, filename="results/growth_rates_Pork_Strawberries_breastmilk.html") 
plot_growth(res_Pork_Sweetpotato_breastmilk, filename="results/growth_rates_Pork_Sweetpotato_breastmilk.html") 
plot_growth(res_Pumpkin_Raspberries_breastmilk, filename="results/growth_rates_Pumpkin_Raspberries_breastmilk.html")  
plot_growth(res_Pumpkin_Shrimp_breastmilk, filename="results/growth_rates_Pumpkin_Shrimp_breastmilk.html") 
plot_growth(res_Pumpkin_Soybean_breastmilk, filename="results/growth_rates_Pumpkin_Soybean_breastmilk.html")  
plot_growth(res_Pumpkin_Splitpeas_breastmilk, filename="results/growth_rates_Pumpkin_Splitpeas_breastmilk.html") 
plot_growth(res_Pumpkin_Strawberries_breastmilk, filename="results/growth_rates_Pumpkin_Strawberries_breastmilk.html") 
plot_growth(res_Pumpkin_Sweetpotato_breastmilk, filename="results/growth_rates_Pumpkin_Sweetpotato_breastmilk.html")  
plot_growth(res_Raspberries_Shrimp_breastmilk, filename="results/growth_rates_Raspberries_Shrimp_breastmilk.html") 
plot_growth(res_Raspberries_Soybean_breastmilk, filename="results/growth_rates_Raspberries_Soybean_breastmilk.html")  
plot_growth(res_Raspberries_Splitpeas_breastmilk, filename="results/growth_rates_Raspberries_Splitpeas_breastmilk.html") 
plot_growth(res_Raspberries_Strawberries_breastmilk, filename="results/growth_rates_Raspberries_Strawberries_breastmilk.html")
plot_growth(res_Raspberries_Sweetpotato_breastmilk, filename="results/growth_rates_Raspberries_Sweetpotato_breastmilk.html")  
plot_growth(res_Shrimp_Soybean_breastmilk, filename="results/growth_rates_Shrimp_Soybean_breastmilk.html") 
plot_growth(res_Shrimp_Splitpeas_breastmilk, filename="results/growth_rates_Shrimp_Splitpeas_breastmilk.html")  
plot_growth(res_Shrimp_Strawberries_breastmilk, filename="results/growth_rates_Shrimp_Strawberries_breastmilk.html") 
plot_growth(res_Shrimp_Sweetpotato_breastmilk, filename="results/growth_rates_Shrimp_Sweetpotato_breastmilk.html")
plot_growth(res_Soybean_Splitpeas_breastmilk, filename="results/growth_rates_Soybean_Splitpeas_breastmilk.html")  
plot_growth(res_Soybean_Strawberries_breastmilk, filename="results/growth_rates_Soybean_Strawberries_breastmilk.html") 
plot_growth(res_Soybean_Sweetpotato_breastmilk, filename="results/growth_rates_Soybean_Sweetpotato_breastmilk.html")  
plot_growth(res_Splitpeas_Strawberries_breastmilk, filename="results/growth_rates_Splitpeas_Strawberries_breastmilk.html") 
plot_growth(res_Splitpeas_Sweetpotato_breastmilk, filename="results/growth_rates_Splitpeas_Sweetpotato_breastmilk.html") 
plot_growth(res_Strawberries_Sweetpotato_breastmilk, filename="results/growth_rates_Strawberries_Sweetpotato_breastmilk.html")  
plot_growth(res_Control_Breastmilk, filename="results/growth_rates_Control_Breastmilk.html") 
plot_growth(res_Control_Infant_formula, filename="results/growth_rates_Control_Infant_formula.html")  

#Production rate
from micom.measures import production_rates
import pandas as pd

prod_Blackbeans_Blackcurrant_breastmilk = production_rates(res_Blackbeans_Blackcurrant_breastmilk)
prod_Blackbeans_Chickpea_breastmilk = production_rates(res_Blackbeans_Chickpea_breastmilk)
prod_Blackbeans_Couscous_breastmilk = production_rates(res_Blackbeans_Couscous_breastmilk)
prod_Blackbeans_Pork_breastmilk = production_rates(res_Blackbeans_Pork_breastmilk)
prod_Blackbeans_Pumpkin_breastmilk = production_rates(res_Blackbeans_Pumpkin_breastmilk)
prod_Blackbeans_Raspberries_breastmilk = production_rates(res_Blackbeans_Raspberries_breastmilk)
prod_Blackbeans_Shrimp_breastmilk = production_rates(res_Blackbeans_Shrimp_breastmilk)
prod_Blackbeans_Soybean_breastmilk = production_rates(res_Blackbeans_Soybean_breastmilk)
prod_Blackbeans_Splitpeas_breastmilk = production_rates(res_Blackbeans_Splitpeas_breastmilk)
prod_Blackbeans_Strawberries_breastmilk = production_rates(res_Blackbeans_Strawberries_breastmilk)
prod_Blackbeans_Sweetpotato_breastmilk = production_rates(res_Blackbeans_Sweetpotato_breastmilk)
prod_Blackcurrant_Chickpea_breastmilk = production_rates(res_Blackcurrant_Chickpea_breastmilk)
prod_Blackcurrant_Couscous_breastmilk = production_rates(res_Blackcurrant_Couscous_breastmilk)
prod_Blackcurrant_Pork_breastmilk = production_rates(res_Blackcurrant_Pork_breastmilk)
prod_Blackcurrant_Pumpkin_breastmilk = production_rates(res_Blackcurrant_Pumpkin_breastmilk)
prod_Blackcurrant_Raspberries_breastmilk = production_rates(res_Blackcurrant_Raspberries_breastmilk)
prod_Blackcurrant_Shrimp_breastmilk = production_rates(res_Blackcurrant_Shrimp_breastmilk)
prod_Blackcurrant_Soybean_breastmilk = production_rates(res_Blackcurrant_Soybean_breastmilk)
prod_Blackcurrant_Splitpeas_breastmilk = production_rates(res_Blackcurrant_Splitpeas_breastmilk)
prod_Blackcurrant_Strawberries_breastmilk = production_rates(res_Blackcurrant_Strawberries_breastmilk)
prod_Blackcurrant_Sweetpotato_breastmilk = production_rates(res_Blackcurrant_Sweetpotato_breastmilk)
prod_Chickpea_Couscous_breastmilk = production_rates(res_Chickpea_Couscous_breastmilk)
prod_Chickpea_Pork_breastmilk = production_rates(res_Chickpea_Pork_breastmilk)
prod_Chickpea_Pumpkin_breastmilk = production_rates(res_Chickpea_Pumpkin_breastmilk)
prod_Chickpea_Raspberries_breastmilk = production_rates(res_Chickpea_Raspberries_breastmilk)
prod_Chickpea_Shrimp_breastmilk = production_rates(res_Chickpea_Shrimp_breastmilk)
prod_Chickpea_Soybean_breastmilk = production_rates(res_Chickpea_Soybean_breastmilk)
prod_Chickpea_Splitpeas_breastmilk = production_rates(res_Chickpea_Splitpeas_breastmilk)
prod_Chickpea_Strawberries_breastmilk = production_rates(res_Chickpea_Strawberries_breastmilk)
prod_Chickpea_Sweetpotato_breastmilk = production_rates(res_Chickpea_Sweetpotato_breastmilk)
prod_Couscous_Pork_breastmilk = production_rates(res_Couscous_Pork_breastmilk)
prod_Couscous_Pumpkin_breastmilk = production_rates(res_Couscous_Pumpkin_breastmilk)
prod_Couscous_Raspberries_breastmilk = production_rates(res_Couscous_Raspberries_breastmilk)
prod_Couscous_Shrimp_breastmilk = production_rates(res_Couscous_Shrimp_breastmilk)
prod_Couscous_Soybean_breastmilk = production_rates(res_Couscous_Soybean_breastmilk)
prod_Couscous_Splitpeas_breastmilk = production_rates(res_Couscous_Splitpeas_breastmilk)
prod_Couscous_Strawberries_breastmilk = production_rates(res_Couscous_Strawberries_breastmilk)
prod_Couscous_Sweetpotato_breastmilk = production_rates(res_Couscous_Sweetpotato_breastmilk)
prod_Pork_Pumpkin_breastmilk = production_rates(res_Pork_Pumpkin_breastmilk)
prod_Pork_Raspberries_breastmilk = production_rates(res_Pork_Raspberries_breastmilk)
prod_Pork_Shrimp_breastmilk = production_rates(res_Pork_Shrimp_breastmilk)
prod_Pork_Soybean_breastmilk = production_rates(res_Pork_Soybean_breastmilk)
prod_Pork_Splitpeas_breastmilk = production_rates(res_Pork_Splitpeas_breastmilk)
prod_Pork_Strawberries_breastmilk = production_rates(res_Pork_Strawberries_breastmilk)
prod_Pork_Sweetpotato_breastmilk = production_rates(res_Pork_Sweetpotato_breastmilk)
prod_Pumpkin_Raspberries_breastmilk = production_rates(res_Pumpkin_Raspberries_breastmilk)
prod_Pumpkin_Shrimp_breastmilk = production_rates(res_Pumpkin_Shrimp_breastmilk)
prod_Pumpkin_Soybean_breastmilk = production_rates(res_Pumpkin_Soybean_breastmilk)
prod_Pumpkin_Splitpeas_breastmilk = production_rates(res_Pumpkin_Splitpeas_breastmilk)
prod_Pumpkin_Strawberries_breastmilk = production_rates(res_Pumpkin_Strawberries_breastmilk)
prod_Pumpkin_Sweetpotato_breastmilk = production_rates(res_Pumpkin_Sweetpotato_breastmilk)
prod_Raspberries_Shrimp_breastmilk = production_rates(res_Raspberries_Shrimp_breastmilk)
prod_Raspberries_Soybean_breastmilk = production_rates(res_Raspberries_Soybean_breastmilk)
prod_Raspberries_Splitpeas_breastmilk = production_rates(res_Raspberries_Splitpeas_breastmilk)
prod_Raspberries_Strawberries_breastmilk = production_rates(res_Raspberries_Strawberries_breastmilk)
prod_Raspberries_Sweetpotato_breastmilk = production_rates(res_Raspberries_Sweetpotato_breastmilk)
prod_Shrimp_Soybean_breastmilk = production_rates(res_Shrimp_Soybean_breastmilk)
prod_Shrimp_Splitpeas_breastmilk = production_rates(res_Shrimp_Splitpeas_breastmilk)
prod_Shrimp_Strawberries_breastmilk = production_rates(res_Shrimp_Strawberries_breastmilk)
prod_Shrimp_Sweetpotato_breastmilk = production_rates(res_Shrimp_Sweetpotato_breastmilk)
prod_Soybean_Splitpeas_breastmilk = production_rates(res_Soybean_Splitpeas_breastmilk)
prod_Soybean_Strawberries_breastmilk = production_rates(res_Soybean_Strawberries_breastmilk)
prod_Soybean_Sweetpotato_breastmilk = production_rates(res_Soybean_Sweetpotato_breastmilk)
prod_Splitpeas_Strawberries_breastmilk = production_rates(res_Splitpeas_Strawberries_breastmilk)
prod_Splitpeas_Sweetpotato_breastmilk = production_rates(res_Splitpeas_Sweetpotato_breastmilk)
prod_Strawberries_Sweetpotato_breastmilk = production_rates(res_Strawberries_Sweetpotato_breastmilk)
prod_Control_Breastmilk = production_rates(res_Control_Breastmilk)
prod_Control_Infant_formula = production_rates(res_Control_Infant_formula)

prod_Blackbeans_Blackcurrant_breastmilk['diet'] = 'Blackbeans_Blackcurrant_breastmilk' #create new colum
prod_Blackbeans_Chickpea_breastmilk['diet'] = 'Blackbeans_Chickpea_breastmilk' #create new colum
prod_Blackbeans_Couscous_breastmilk['diet'] = 'Blackbeans_Couscous_breastmilk' #create new colum
prod_Blackbeans_Pork_breastmilk['diet'] = 'Blackbeans_Pork_breastmilk' #create new colum
prod_Blackbeans_Pumpkin_breastmilk['diet'] = 'Blackbeans_Pumpkin_breastmilk' #create new colum
prod_Blackbeans_Raspberries_breastmilk['diet'] = 'Blackbeans_Raspberries_breastmilk' #create new colum
prod_Blackbeans_Shrimp_breastmilk['diet'] = 'Blackbeans_Shrimp_breastmilk' #create new colum
prod_Blackbeans_Soybean_breastmilk['diet'] = 'Blackbeans_Soybean_breastmilk' #create new colum
prod_Blackbeans_Splitpeas_breastmilk['diet'] = 'Blackbeans_Splitpeas_breastmilk' #create new colum
prod_Blackbeans_Strawberries_breastmilk['diet'] = 'Blackbeans_Strawberries_breastmilk' #create new colum
prod_Blackbeans_Sweetpotato_breastmilk['diet'] = 'Blackbeans_Sweetpotato_breastmilk' #create new colum
prod_Blackcurrant_Chickpea_breastmilk['diet'] = 'Blackcurrant_Chickpea_breastmilk' #create new colum
prod_Blackcurrant_Couscous_breastmilk['diet'] = 'Blackcurrant_Couscous_breastmilk' #create new colum
prod_Blackcurrant_Pork_breastmilk['diet'] = 'Blackcurrant_Pork_breastmilk' #create new colum
prod_Blackcurrant_Pumpkin_breastmilk['diet'] = 'Blackcurrant_Pumpkin_breastmilk' #create new colum
prod_Blackcurrant_Raspberries_breastmilk['diet'] = 'Blackcurrant_Raspberries_breastmilk' #create new colum
prod_Blackcurrant_Shrimp_breastmilk['diet'] = 'Blackcurrant_Shrimp_breastmilk' #create new colum
prod_Blackcurrant_Soybean_breastmilk['diet'] = 'Blackcurrant_Soybean_breastmilk' #create new colum
prod_Blackcurrant_Splitpeas_breastmilk['diet'] = 'Blackcurrant_Splitpeas_breastmilk' #create new colum
prod_Blackcurrant_Strawberries_breastmilk['diet'] = 'Blackcurrant_Strawberries_breastmilk' #create new colum
prod_Blackcurrant_Sweetpotato_breastmilk['diet'] = 'Blackcurrant_Sweetpotato_breastmilk' #create new colum
prod_Chickpea_Couscous_breastmilk['diet'] = 'Chickpea_Couscous_breastmilk' #create new colum
prod_Chickpea_Pork_breastmilk['diet'] = 'Chickpea_Pork_breastmilk' #create new colum
prod_Chickpea_Pumpkin_breastmilk['diet'] = 'Chickpea_Pumpkin_breastmilk' #create new colum
prod_Chickpea_Raspberries_breastmilk['diet'] = 'Chickpea_Raspberries_breastmilk' #create new colum
prod_Chickpea_Shrimp_breastmilk['diet'] = 'Chickpea_Shrimp_breastmilk' #create new colum
prod_Chickpea_Soybean_breastmilk['diet'] = 'Chickpea_Soybean_breastmilk' #create new colum
prod_Chickpea_Splitpeas_breastmilk['diet'] = 'Chickpea_Splitpeas_breastmilk' #create new colum
prod_Chickpea_Strawberries_breastmilk['diet'] = 'Chickpea_Strawberries_breastmilk' #create new colum
prod_Chickpea_Sweetpotato_breastmilk['diet'] = 'Chickpea_Sweetpotato_breastmilk' #create new colum
prod_Couscous_Pork_breastmilk['diet'] = 'Couscous_Pork_breastmilk' #create new colum
prod_Couscous_Pumpkin_breastmilk['diet'] = 'Couscous_Pumpkin_breastmilk' #create new colum
prod_Couscous_Raspberries_breastmilk['diet'] = 'Couscous_Raspberries_breastmilk' #create new colum
prod_Couscous_Shrimp_breastmilk['diet'] = 'Couscous_Shrimp_breastmilk' #create new colum
prod_Couscous_Soybean_breastmilk['diet'] = 'Couscous_Soybean_breastmilk' #create new colum
prod_Couscous_Splitpeas_breastmilk['diet'] = 'Couscous_Splitpeas_breastmilk' #create new colum
prod_Couscous_Strawberries_breastmilk['diet'] = 'Couscous_Strawberries_breastmilk' #create new colum
prod_Couscous_Sweetpotato_breastmilk['diet'] = 'Couscous_Sweetpotato_breastmilk' #create new colum
prod_Pork_Pumpkin_breastmilk['diet'] = 'Pork_Pumpkin_breastmilk' #create new colum
prod_Pork_Raspberries_breastmilk['diet'] = 'Pork_Raspberries_breastmilk' #create new colum
prod_Pork_Shrimp_breastmilk['diet'] = 'Pork_Shrimp_breastmilk' #create new colum
prod_Pork_Soybean_breastmilk['diet'] = 'Pork_Soybean_breastmilk' #create new colum
prod_Pork_Splitpeas_breastmilk['diet'] = 'Pork_Splitpeas_breastmilk' #create new colum
prod_Pork_Strawberries_breastmilk['diet'] = 'Pork_Strawberries_breastmilk' #create new colum
prod_Pork_Sweetpotato_breastmilk['diet'] = 'Pork_Sweetpotato_breastmilk' #create new colum
prod_Pumpkin_Raspberries_breastmilk['diet'] = 'Pumpkin_Raspberries_breastmilk' #create new colum
prod_Pumpkin_Shrimp_breastmilk['diet'] = 'Pumpkin_Shrimp_breastmilk' #create new colum
prod_Pumpkin_Soybean_breastmilk['diet'] = 'Pumpkin_Soybean_breastmilk' #create new colum
prod_Pumpkin_Splitpeas_breastmilk['diet'] = 'Pumpkin_Splitpeas_breastmilk' #create new colum
prod_Pumpkin_Strawberries_breastmilk['diet'] = 'Pumpkin_Strawberries_breastmilk' #create new colum
prod_Pumpkin_Sweetpotato_breastmilk['diet'] = 'Pumpkin_Sweetpotato_breastmilk' #create new colum
prod_Raspberries_Shrimp_breastmilk['diet'] = 'Raspberries_Shrimp_breastmilk' #create new colum
prod_Raspberries_Soybean_breastmilk['diet'] = 'Raspberries_Soybean_breastmilk' #create new colum
prod_Raspberries_Splitpeas_breastmilk['diet'] = 'Raspberries_Splitpeas_breastmilk' #create new colum
prod_Raspberries_Strawberries_breastmilk['diet'] = 'Raspberries_Strawberries_breastmilk' #create new colum
prod_Raspberries_Sweetpotato_breastmilk['diet'] = 'Raspberries_Sweetpotato_breastmilk' #create new colum
prod_Shrimp_Soybean_breastmilk['diet'] = 'Shrimp_Soybean_breastmilk' #create new colum
prod_Shrimp_Splitpeas_breastmilk['diet'] = 'Shrimp_Splitpeas_breastmilk' #create new colum
prod_Shrimp_Strawberries_breastmilk['diet'] = 'Shrimp_Strawberries_breastmilk' #create new colum
prod_Shrimp_Sweetpotato_breastmilk['diet'] = 'Shrimp_Sweetpotato_breastmilk' #create new colum
prod_Soybean_Splitpeas_breastmilk['diet'] = 'Soybean_Splitpeas_breastmilk' #create new colum
prod_Soybean_Strawberries_breastmilk['diet'] = 'Soybean_Strawberries_breastmilk' #create new colum
prod_Soybean_Sweetpotato_breastmilk['diet'] = 'Soybean_Sweetpotato_breastmilk' #create new colum
prod_Splitpeas_Strawberries_breastmilk['diet'] = 'Splitpeas_Strawberries_breastmilk' #create new colum
prod_Splitpeas_Sweetpotato_breastmilk['diet'] = 'Splitpeas_Sweetpotato_breastmilk' #create new colum
prod_Strawberries_Sweetpotato_breastmilk['diet'] = 'Strawberries_Sweetpotato_breastmilk' #create new colum
prod_Control_Breastmilk['diet'] = 'Control_Breastmilk' #create new colum
prod_Control_Infant_formula['diet'] = 'Control_Infant_formula' #create new colum

exchanges = pd.concat([prod_Blackbeans_Blackcurrant_breastmilk,prod_Blackbeans_Chickpea_breastmilk,prod_Blackbeans_Couscous_breastmilk,prod_Blackbeans_Pork_breastmilk,prod_Blackbeans_Pumpkin_breastmilk,
                       prod_Blackbeans_Raspberries_breastmilk,prod_Blackbeans_Shrimp_breastmilk,prod_Blackbeans_Soybean_breastmilk,prod_Blackbeans_Splitpeas_breastmilk,prod_Blackbeans_Strawberries_breastmilk,
                       prod_Blackbeans_Sweetpotato_breastmilk,prod_Blackcurrant_Chickpea_breastmilk,prod_Blackcurrant_Couscous_breastmilk,prod_Blackcurrant_Pork_breastmilk,prod_Blackcurrant_Pumpkin_breastmilk,
                       prod_Blackcurrant_Raspberries_breastmilk,prod_Blackcurrant_Shrimp_breastmilk,prod_Blackcurrant_Soybean_breastmilk,prod_Blackcurrant_Splitpeas_breastmilk,prod_Blackcurrant_Strawberries_breastmilk,
                       prod_Blackcurrant_Sweetpotato_breastmilk,prod_Chickpea_Couscous_breastmilk,prod_Chickpea_Pork_breastmilk,prod_Chickpea_Pumpkin_breastmilk,prod_Chickpea_Raspberries_breastmilk,
                       prod_Chickpea_Shrimp_breastmilk,prod_Chickpea_Soybean_breastmilk,prod_Chickpea_Splitpeas_breastmilk,prod_Chickpea_Strawberries_breastmilk,prod_Chickpea_Sweetpotato_breastmilk,
                       prod_Couscous_Pork_breastmilk,prod_Couscous_Pumpkin_breastmilk,prod_Couscous_Raspberries_breastmilk,prod_Couscous_Shrimp_breastmilk,prod_Couscous_Soybean_breastmilk,
                       prod_Couscous_Splitpeas_breastmilk,prod_Couscous_Strawberries_breastmilk,prod_Couscous_Sweetpotato_breastmilk,prod_Pork_Pumpkin_breastmilk,prod_Pork_Raspberries_breastmilk,
                       prod_Pork_Shrimp_breastmilk,prod_Pork_Soybean_breastmilk,prod_Pork_Splitpeas_breastmilk,prod_Pork_Strawberries_breastmilk,prod_Pork_Sweetpotato_breastmilk,
                       prod_Pumpkin_Raspberries_breastmilk,prod_Pumpkin_Shrimp_breastmilk,prod_Pumpkin_Soybean_breastmilk,prod_Pumpkin_Splitpeas_breastmilk,prod_Pumpkin_Strawberries_breastmilk,
                       prod_Pumpkin_Sweetpotato_breastmilk,prod_Raspberries_Shrimp_breastmilk,prod_Raspberries_Soybean_breastmilk,prod_Raspberries_Splitpeas_breastmilk,prod_Raspberries_Strawberries_breastmilk,
                       prod_Raspberries_Sweetpotato_breastmilk,prod_Shrimp_Soybean_breastmilk,prod_Shrimp_Splitpeas_breastmilk,prod_Shrimp_Strawberries_breastmilk,prod_Shrimp_Sweetpotato_breastmilk,
                       prod_Soybean_Splitpeas_breastmilk,prod_Soybean_Strawberries_breastmilk,prod_Soybean_Sweetpotato_breastmilk,prod_Splitpeas_Strawberries_breastmilk,prod_Splitpeas_Sweetpotato_breastmilk,
                       prod_Strawberries_Sweetpotato_breastmilk,prod_Control_Breastmilk,prod_Control_Infant_formula])  # merge the production rates

exchanges = pd.pivot_table(exchanges, index = ['diet'], columns = 'name', values = 'flux') #converting into matrix
exchanges.to_csv("results/exchanges.csv")
exchanges_reduced = exchanges[["Acetate", "Propionate", "Butyrate","Isobutyrate, 2-Methylpropanoate", "Isovalerate, 3-Methylbutanoate"]] #selecting the metabolites of interest
exchanges_reduced.to_csv("results/exchanges_reduced.csv")

#Plotting growth rates
import pandas as pd
import seaborn as sns

growth_Blackbeans_Blackcurrant_breastmilk = pd.read_csv('results/growth_rates_Blackbeans_Blackcurrant_breastmilk.csv')
growth_Blackbeans_Chickpea_breastmilk = pd.read_csv('results/growth_rates_Blackbeans_Chickpea_breastmilk.csv')
growth_Blackbeans_Couscous_breastmilk = pd.read_csv('results/growth_rates_Blackbeans_Couscous_breastmilk.csv')
growth_Blackbeans_Pork_breastmilk = pd.read_csv('results/growth_rates_Blackbeans_Pork_breastmilk.csv')
growth_Blackbeans_Pumpkin_breastmilk = pd.read_csv('results/growth_rates_Blackbeans_Pumpkin_breastmilk.csv')
growth_Blackbeans_Raspberries_breastmilk = pd.read_csv('results/growth_rates_Blackbeans_Raspberries_breastmilk.csv')
growth_Blackbeans_Shrimp_breastmilk = pd.read_csv('results/growth_rates_Blackbeans_Shrimp_breastmilk.csv')
growth_Blackbeans_Soybean_breastmilk = pd.read_csv('results/growth_rates_Blackbeans_Soybean_breastmilk.csv')
growth_Blackbeans_Splitpeas_breastmilk = pd.read_csv('results/growth_rates_Blackbeans_Splitpeas_breastmilk.csv')
growth_Blackbeans_Strawberries_breastmilk = pd.read_csv('results/growth_rates_Blackbeans_Strawberries_breastmilk.csv')
growth_Blackbeans_Sweetpotato_breastmilk = pd.read_csv('results/growth_rates_Blackbeans_Sweetpotato_breastmilk.csv')
growth_Blackcurrant_Chickpea_breastmilk = pd.read_csv('results/growth_rates_Blackcurrant_Chickpea_breastmilk.csv')
growth_Blackcurrant_Couscous_breastmilk = pd.read_csv('results/growth_rates_Blackcurrant_Couscous_breastmilk.csv')
growth_Blackcurrant_Pork_breastmilk = pd.read_csv('results/growth_rates_Blackcurrant_Pork_breastmilk.csv')
growth_Blackcurrant_Pumpkin_breastmilk = pd.read_csv('results/growth_rates_Blackcurrant_Pumpkin_breastmilk.csv')
growth_Blackcurrant_Raspberries_breastmilk = pd.read_csv('results/growth_rates_Blackcurrant_Raspberries_breastmilk.csv')
growth_Blackcurrant_Shrimp_breastmilk = pd.read_csv('results/growth_rates_Blackcurrant_Shrimp_breastmilk.csv')
growth_Blackcurrant_Soybean_breastmilk = pd.read_csv('results/growth_rates_Blackcurrant_Soybean_breastmilk.csv')
growth_Blackcurrant_Splitpeas_breastmilk = pd.read_csv('results/growth_rates_Blackcurrant_Splitpeas_breastmilk.csv')
growth_Blackcurrant_Strawberries_breastmilk = pd.read_csv('results/growth_rates_Blackcurrant_Strawberries_breastmilk.csv')
growth_Blackcurrant_Sweetpotato_breastmilk = pd.read_csv('results/growth_rates_Blackcurrant_Sweetpotato_breastmilk.csv')
growth_Chickpea_Couscous_breastmilk = pd.read_csv('results/growth_rates_Chickpea_Couscous_breastmilk.csv')
growth_Chickpea_Pork_breastmilk = pd.read_csv('results/growth_rates_Chickpea_Pork_breastmilk.csv')
growth_Chickpea_Pumpkin_breastmilk = pd.read_csv('results/growth_rates_Chickpea_Pumpkin_breastmilk.csv')
growth_Chickpea_Raspberries_breastmilk = pd.read_csv('results/growth_rates_Chickpea_Raspberries_breastmilk.csv')
growth_Chickpea_Shrimp_breastmilk = pd.read_csv('results/growth_rates_Chickpea_Shrimp_breastmilk.csv')
growth_Chickpea_Soybean_breastmilk = pd.read_csv('results/growth_rates_Chickpea_Soybean_breastmilk.csv')
growth_Chickpea_Splitpeas_breastmilk = pd.read_csv('results/growth_rates_Chickpea_Splitpeas_breastmilk.csv')
growth_Chickpea_Strawberries_breastmilk = pd.read_csv('results/growth_rates_Chickpea_Strawberries_breastmilk.csv')
growth_Chickpea_Sweetpotato_breastmilk = pd.read_csv('results/growth_rates_Chickpea_Sweetpotato_breastmilk.csv')
growth_Couscous_Pork_breastmilk = pd.read_csv('results/growth_rates_Couscous_Pork_breastmilk.csv')
growth_Couscous_Pumpkin_breastmilk = pd.read_csv('results/growth_rates_Couscous_Pumpkin_breastmilk.csv')
growth_Couscous_Raspberries_breastmilk = pd.read_csv('results/growth_rates_Couscous_Raspberries_breastmilk.csv')
growth_Couscous_Shrimp_breastmilk = pd.read_csv('results/growth_rates_Couscous_Shrimp_breastmilk.csv')
growth_Couscous_Soybean_breastmilk = pd.read_csv('results/growth_rates_Couscous_Soybean_breastmilk.csv')
growth_Couscous_Splitpeas_breastmilk = pd.read_csv('results/growth_rates_Couscous_Splitpeas_breastmilk.csv')
growth_Couscous_Strawberries_breastmilk = pd.read_csv('results/growth_rates_Couscous_Strawberries_breastmilk.csv')
growth_Couscous_Sweetpotato_breastmilk = pd.read_csv('results/growth_rates_Couscous_Sweetpotato_breastmilk.csv')
growth_Pork_Pumpkin_breastmilk = pd.read_csv('results/growth_rates_Pork_Pumpkin_breastmilk.csv')
growth_Pork_Raspberries_breastmilk = pd.read_csv('results/growth_rates_Pork_Raspberries_breastmilk.csv')
growth_Pork_Shrimp_breastmilk = pd.read_csv('results/growth_rates_Pork_Shrimp_breastmilk.csv')
growth_Pork_Soybean_breastmilk = pd.read_csv('results/growth_rates_Pork_Soybean_breastmilk.csv')
growth_Pork_Splitpeas_breastmilk = pd.read_csv('results/growth_rates_Pork_Splitpeas_breastmilk.csv')
growth_Pork_Strawberries_breastmilk = pd.read_csv('results/growth_rates_Pork_Strawberries_breastmilk.csv')
growth_Pork_Sweetpotato_breastmilk = pd.read_csv('results/growth_rates_Pork_Sweetpotato_breastmilk.csv')
growth_Pumpkin_Raspberries_breastmilk = pd.read_csv('results/growth_rates_Pumpkin_Raspberries_breastmilk.csv')
growth_Pumpkin_Shrimp_breastmilk = pd.read_csv('results/growth_rates_Pumpkin_Shrimp_breastmilk.csv')
growth_Pumpkin_Soybean_breastmilk = pd.read_csv('results/growth_rates_Pumpkin_Soybean_breastmilk.csv')
growth_Pumpkin_Splitpeas_breastmilk = pd.read_csv('results/growth_rates_Pumpkin_Splitpeas_breastmilk.csv')
growth_Pumpkin_Strawberries_breastmilk = pd.read_csv('results/growth_rates_Pumpkin_Strawberries_breastmilk.csv')
growth_Pumpkin_Sweetpotato_breastmilk = pd.read_csv('results/growth_rates_Pumpkin_Sweetpotato_breastmilk.csv')
growth_Raspberries_Shrimp_breastmilk = pd.read_csv('results/growth_rates_Raspberries_Shrimp_breastmilk.csv')
growth_Raspberries_Soybean_breastmilk = pd.read_csv('results/growth_rates_Raspberries_Soybean_breastmilk.csv')
growth_Raspberries_Splitpeas_breastmilk = pd.read_csv('results/growth_rates_Raspberries_Splitpeas_breastmilk.csv')
growth_Raspberries_Strawberries_breastmilk = pd.read_csv('results/growth_rates_Raspberries_Strawberries_breastmilk.csv')
growth_Raspberries_Sweetpotato_breastmilk = pd.read_csv('results/growth_rates_Raspberries_Sweetpotato_breastmilk.csv')
growth_Shrimp_Soybean_breastmilk = pd.read_csv('results/growth_rates_Shrimp_Soybean_breastmilk.csv')
growth_Shrimp_Splitpeas_breastmilk = pd.read_csv('results/growth_rates_Shrimp_Splitpeas_breastmilk.csv')
growth_Shrimp_Strawberries_breastmilk = pd.read_csv('results/growth_rates_Shrimp_Strawberries_breastmilk.csv')
growth_Shrimp_Sweetpotato_breastmilk = pd.read_csv('results/growth_rates_Shrimp_Sweetpotato_breastmilk.csv')
growth_Soybean_Splitpeas_breastmilk = pd.read_csv('results/growth_rates_Soybean_Splitpeas_breastmilk.csv')
growth_Soybean_Strawberries_breastmilk = pd.read_csv('results/growth_rates_Soybean_Strawberries_breastmilk.csv')
growth_Soybean_Sweetpotato_breastmilk = pd.read_csv('results/growth_rates_Soybean_Sweetpotato_breastmilk.csv')
growth_Splitpeas_Strawberries_breastmilk = pd.read_csv('results/growth_rates_Splitpeas_Strawberries_breastmilk.csv')
growth_Splitpeas_Sweetpotato_breastmilk = pd.read_csv('results/growth_rates_Splitpeas_Sweetpotato_breastmilk.csv')
growth_Strawberries_Sweetpotato_breastmilk = pd.read_csv('results/growth_rates_Strawberries_Sweetpotato_breastmilk.csv')
growth_Control_Breastmilk = pd.read_csv('results/growth_rates_Control_Breastmilk.csv')
growth_Control_Infant_formula = pd.read_csv('results/growth_rates_Control_Infant_formula.csv')

growth_Blackbeans_Blackcurrant_breastmilk['diet'] = 'Blackbeans_Blackcurrant_breastmilk' 
growth_Blackbeans_Chickpea_breastmilk['diet'] = 'Blackbeans_Chickpea_breastmilk' 
growth_Blackbeans_Couscous_breastmilk['diet'] = 'Blackbeans_Couscous_breastmilk' 
growth_Blackbeans_Pork_breastmilk['diet'] = 'Blackbeans_Pork_breastmilk' 
growth_Blackbeans_Pumpkin_breastmilk['diet'] = 'Blackbeans_Pumpkin_breastmilk' 
growth_Blackbeans_Raspberries_breastmilk['diet'] = 'Blackbeans_Raspberries_breastmilk' 
growth_Blackbeans_Shrimp_breastmilk['diet'] = 'Blackbeans_Shrimp_breastmilk' 
growth_Blackbeans_Soybean_breastmilk['diet'] = 'Blackbeans_Soybean_breastmilk' 
growth_Blackbeans_Splitpeas_breastmilk['diet'] = 'Blackbeans_Splitpeas_breastmilk' 
growth_Blackbeans_Strawberries_breastmilk['diet'] = 'Blackbeans_Strawberries_breastmilk' 
growth_Blackbeans_Sweetpotato_breastmilk['diet'] = 'Blackbeans_Sweetpotato_breastmilk' 
growth_Blackcurrant_Chickpea_breastmilk['diet'] = 'Blackcurrant_Chickpea_breastmilk' 
growth_Blackcurrant_Couscous_breastmilk['diet'] = 'Blackcurrant_Couscous_breastmilk' 
growth_Blackcurrant_Pork_breastmilk['diet'] = 'Blackcurrant_Pork_breastmilk' 
growth_Blackcurrant_Pumpkin_breastmilk['diet'] = 'Blackcurrant_Pumpkin_breastmilk' 
growth_Blackcurrant_Raspberries_breastmilk['diet'] = 'Blackcurrant_Raspberries_breastmilk' 
growth_Blackcurrant_Shrimp_breastmilk['diet'] = 'Blackcurrant_Shrimp_breastmilk' 
growth_Blackcurrant_Soybean_breastmilk['diet'] = 'Blackcurrant_Soybean_breastmilk' 
growth_Blackcurrant_Splitpeas_breastmilk['diet'] = 'Blackcurrant_Splitpeas_breastmilk' 
growth_Blackcurrant_Strawberries_breastmilk['diet'] = 'Blackcurrant_Strawberries_breastmilk' 
growth_Blackcurrant_Sweetpotato_breastmilk['diet'] = 'Blackcurrant_Sweetpotato_breastmilk' 
growth_Chickpea_Couscous_breastmilk['diet'] = 'Chickpea_Couscous_breastmilk' 
growth_Chickpea_Pork_breastmilk['diet'] = 'Chickpea_Pork_breastmilk' 
growth_Chickpea_Pumpkin_breastmilk['diet'] = 'Chickpea_Pumpkin_breastmilk' 
growth_Chickpea_Raspberries_breastmilk['diet'] = 'Chickpea_Raspberries_breastmilk' 
growth_Chickpea_Shrimp_breastmilk['diet'] = 'Chickpea_Shrimp_breastmilk' 
growth_Chickpea_Soybean_breastmilk['diet'] = 'Chickpea_Soybean_breastmilk' 
growth_Chickpea_Splitpeas_breastmilk['diet'] = 'Chickpea_Splitpeas_breastmilk' 
growth_Chickpea_Strawberries_breastmilk['diet'] = 'Chickpea_Strawberries_breastmilk' 
growth_Chickpea_Sweetpotato_breastmilk['diet'] = 'Chickpea_Sweetpotato_breastmilk' 
growth_Couscous_Pork_breastmilk['diet'] = 'Couscous_Pork_breastmilk' 
growth_Couscous_Pumpkin_breastmilk['diet'] = 'Couscous_Pumpkin_breastmilk' 
growth_Couscous_Raspberries_breastmilk['diet'] = 'Couscous_Raspberries_breastmilk' 
growth_Couscous_Shrimp_breastmilk['diet'] = 'Couscous_Shrimp_breastmilk' 
growth_Couscous_Soybean_breastmilk['diet'] = 'Couscous_Soybean_breastmilk' 
growth_Couscous_Splitpeas_breastmilk['diet'] = 'Couscous_Splitpeas_breastmilk' 
growth_Couscous_Strawberries_breastmilk['diet'] = 'Couscous_Strawberries_breastmilk' 
growth_Couscous_Sweetpotato_breastmilk['diet'] = 'Couscous_Sweetpotato_breastmilk' 
growth_Pork_Pumpkin_breastmilk['diet'] = 'Pork_Pumpkin_breastmilk' 
growth_Pork_Raspberries_breastmilk['diet'] = 'Pork_Raspberries_breastmilk' 
growth_Pork_Shrimp_breastmilk['diet'] = 'Pork_Shrimp_breastmilk' 
growth_Pork_Soybean_breastmilk['diet'] = 'Pork_Soybean_breastmilk' 
growth_Pork_Splitpeas_breastmilk['diet'] = 'Pork_Splitpeas_breastmilk' 
growth_Pork_Strawberries_breastmilk['diet'] = 'Pork_Strawberries_breastmilk' 
growth_Pork_Sweetpotato_breastmilk['diet'] = 'Pork_Sweetpotato_breastmilk' 
growth_Pumpkin_Raspberries_breastmilk['diet'] = 'Pumpkin_Raspberries_breastmilk' 
growth_Pumpkin_Shrimp_breastmilk['diet'] = 'Pumpkin_Shrimp_breastmilk' 
growth_Pumpkin_Soybean_breastmilk['diet'] = 'Pumpkin_Soybean_breastmilk' 
growth_Pumpkin_Splitpeas_breastmilk['diet'] = 'Pumpkin_Splitpeas_breastmilk' 
growth_Pumpkin_Strawberries_breastmilk['diet'] = 'Pumpkin_Strawberries_breastmilk' 
growth_Pumpkin_Sweetpotato_breastmilk['diet'] = 'Pumpkin_Sweetpotato_breastmilk' 
growth_Raspberries_Shrimp_breastmilk['diet'] = 'Raspberries_Shrimp_breastmilk' 
growth_Raspberries_Soybean_breastmilk['diet'] = 'Raspberries_Soybean_breastmilk' 
growth_Raspberries_Splitpeas_breastmilk['diet'] = 'Raspberries_Splitpeas_breastmilk' 
growth_Raspberries_Strawberries_breastmilk['diet'] = 'Raspberries_Strawberries_breastmilk' 
growth_Raspberries_Sweetpotato_breastmilk['diet'] = 'Raspberries_Sweetpotato_breastmilk' 
growth_Shrimp_Soybean_breastmilk['diet'] = 'Shrimp_Soybean_breastmilk' 
growth_Shrimp_Splitpeas_breastmilk['diet'] = 'Shrimp_Splitpeas_breastmilk' 
growth_Shrimp_Strawberries_breastmilk['diet'] = 'Shrimp_Strawberries_breastmilk' 
growth_Shrimp_Sweetpotato_breastmilk['diet'] = 'Shrimp_Sweetpotato_breastmilk' 
growth_Soybean_Splitpeas_breastmilk['diet'] = 'Soybean_Splitpeas_breastmilk' 
growth_Soybean_Strawberries_breastmilk['diet'] = 'Soybean_Strawberries_breastmilk' 
growth_Soybean_Sweetpotato_breastmilk['diet'] = 'Soybean_Sweetpotato_breastmilk' 
growth_Splitpeas_Strawberries_breastmilk['diet'] = 'Splitpeas_Strawberries_breastmilk' 
growth_Splitpeas_Sweetpotato_breastmilk['diet'] = 'Splitpeas_Sweetpotato_breastmilk' 
growth_Strawberries_Sweetpotato_breastmilk['diet'] = 'Strawberries_Sweetpotato_breastmilk' 
growth_Control_Breastmilk['diet'] = 'Control_Breastmilk' 
growth_Control_Infant_formula['diet'] = 'Control_Infant_formula' 

growth_rates = pd.concat([growth_Blackbeans_Blackcurrant_breastmilk,growth_Blackbeans_Chickpea_breastmilk,growth_Blackbeans_Couscous_breastmilk,growth_Blackbeans_Pork_breastmilk,growth_Blackbeans_Pumpkin_breastmilk,
                          growth_Blackbeans_Raspberries_breastmilk,growth_Blackbeans_Shrimp_breastmilk,growth_Blackbeans_Soybean_breastmilk,growth_Blackbeans_Splitpeas_breastmilk,growth_Blackbeans_Strawberries_breastmilk,
                          growth_Blackbeans_Sweetpotato_breastmilk,growth_Blackcurrant_Chickpea_breastmilk,growth_Blackcurrant_Couscous_breastmilk,growth_Blackcurrant_Pork_breastmilk,growth_Blackcurrant_Pumpkin_breastmilk,
                          growth_Blackcurrant_Raspberries_breastmilk,growth_Blackcurrant_Shrimp_breastmilk,growth_Blackcurrant_Soybean_breastmilk,growth_Blackcurrant_Splitpeas_breastmilk,growth_Blackcurrant_Strawberries_breastmilk,
                          growth_Blackcurrant_Sweetpotato_breastmilk,growth_Chickpea_Couscous_breastmilk,growth_Chickpea_Pork_breastmilk,growth_Chickpea_Pumpkin_breastmilk,growth_Chickpea_Raspberries_breastmilk,
                          growth_Chickpea_Shrimp_breastmilk,growth_Chickpea_Soybean_breastmilk,growth_Chickpea_Splitpeas_breastmilk,growth_Chickpea_Strawberries_breastmilk,growth_Chickpea_Sweetpotato_breastmilk,
                          growth_Couscous_Pork_breastmilk,growth_Couscous_Pumpkin_breastmilk,growth_Couscous_Raspberries_breastmilk,growth_Couscous_Shrimp_breastmilk,growth_Couscous_Soybean_breastmilk,
                          growth_Couscous_Splitpeas_breastmilk,growth_Couscous_Strawberries_breastmilk,growth_Couscous_Sweetpotato_breastmilk,growth_Pork_Pumpkin_breastmilk,growth_Pork_Raspberries_breastmilk,
                          growth_Pork_Shrimp_breastmilk,growth_Pork_Soybean_breastmilk,growth_Pork_Splitpeas_breastmilk,growth_Pork_Strawberries_breastmilk,growth_Pork_Sweetpotato_breastmilk,
                          growth_Pumpkin_Raspberries_breastmilk,growth_Pumpkin_Shrimp_breastmilk,growth_Pumpkin_Soybean_breastmilk,growth_Pumpkin_Splitpeas_breastmilk,growth_Pumpkin_Strawberries_breastmilk,
                          growth_Pumpkin_Sweetpotato_breastmilk,growth_Raspberries_Shrimp_breastmilk,growth_Raspberries_Soybean_breastmilk,growth_Raspberries_Splitpeas_breastmilk,growth_Raspberries_Strawberries_breastmilk,
                          growth_Raspberries_Sweetpotato_breastmilk,growth_Shrimp_Soybean_breastmilk,growth_Shrimp_Splitpeas_breastmilk,growth_Shrimp_Strawberries_breastmilk,growth_Shrimp_Sweetpotato_breastmilk,
                          growth_Soybean_Splitpeas_breastmilk,growth_Soybean_Strawberries_breastmilk,growth_Soybean_Sweetpotato_breastmilk,growth_Splitpeas_Strawberries_breastmilk,growth_Splitpeas_Sweetpotato_breastmilk,
                          growth_Strawberries_Sweetpotato_breastmilk,growth_Control_Breastmilk,growth_Control_Infant_formula])  # merging the growth rates
growth_rates = pd.pivot_table(growth_rates, index = ["diet"], columns = "taxon", values = "growth_rate") #pivoting the table
growth_rates.to_csv("results/growth_rates.csv")