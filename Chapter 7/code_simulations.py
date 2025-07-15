##Simulating foods on the microbiota of weaning infants
#Foods designed to match in vitro work, with same dry mass (150g)
#Daily fluxes, CPLEX 22.1, AGORA2, genus
#fluxes are diluted to 10% to mimic fecal fermentations (~10% of digested food was actually fermented)

#Importing taxnomic data
import pandas as pd
tax = pd.read_csv('data/relative_abundance_genus.csv') 

#Building models using AGORA2 reconstructions
from micom.workflows import build
import pandas as pd
manifest = build(tax, model_db="data/agora201_genus_1.qza", out_folder="models_cplex", solver="cplex", cutoff=0.001, threads=14) #keeping taxa with at least 0.1% relative abundance
manifest #to check the fraction of the taxa that matches the AGORA2 database

##Defining the diets
import pandas as pd
#foods
black_beans = pd.read_csv('data/black_beans.csv')
blackcurrants = pd.read_csv('data/blackcurrants.csv')
chickpeas = pd.read_csv('data/chickpeas.csv')
couscous = pd.read_csv('data/couscous.csv')
infant_formula = pd.read_csv('data/infant_formula.csv')
kumara_with_skin = pd.read_csv('data/kumara_with_skin.csv')
kumara_without_skin = pd.read_csv('data/kumara_without_skin.csv')
pork = pd.read_csv('data/pork.csv')
prawn = pd.read_csv('data/prawn.csv')
pumpkin = pd.read_csv('data/pumpkin.csv')
raspberries = pd.read_csv('data/raspberries.csv')
soybeans = pd.read_csv('data/soybeans.csv')
strawberries = pd.read_csv('data/strawberries.csv')
yellow_peas = pd.read_csv('data/yellow_peas.csv')
#food_formula
formula_black_beans = pd.read_csv('data/formula_black_beans.csv')
formula_blackcurrants = pd.read_csv('data/formula_blackcurrants.csv')
formula_chickpeas = pd.read_csv('data/formula_chickpeas.csv')
formula_couscous = pd.read_csv('data/formula_couscous.csv')
formula_kumara_with_skin = pd.read_csv('data/formula_kumara_with_skin.csv')
formula_kumara_without_skin = pd.read_csv('data/formula_kumara_without_skin.csv')
formula_pork = pd.read_csv('data/formula_pork.csv')
formula_prawn = pd.read_csv('data/formula_prawn.csv')
formula_pumpkin = pd.read_csv('data/formula_pumpkin.csv')
formula_raspberries = pd.read_csv('data/formula_raspberries.csv')
formula_soybeans = pd.read_csv('data/formula_soybeans.csv')
formula_strawberries = pd.read_csv('data/formula_strawberries.csv')
formula_yellow_peas = pd.read_csv('data/formula_yellow_peas.csv')
#food_foods
black_beans_blackcurrants = pd.read_csv('data/black_beans_blackcurrants.csv')
black_beans_pumpkin = pd.read_csv('data/black_beans_pumpkin.csv')
blackcurrants_kumara_with_skin = pd.read_csv('data/blackcurrants_kumara_with_skin.csv')
blackcurrants_kumara_without_skin = pd.read_csv('data/blackcurrants_kumara_without_skin.csv')
blackcurrants_pork = pd.read_csv('data/blackcurrants_pork.csv')
blackcurrants_soybeans = pd.read_csv('data/blackcurrants_soybeans.csv')
blackcurrants_strawberries = pd.read_csv('data/blackcurrants_strawberries.csv')
chickpeas_pork = pd.read_csv('data/chickpeas_pork.csv')
chickpeas_yellow_peas = pd.read_csv('data/chickpeas_yellow_peas.csv')
couscous_pork = pd.read_csv('data/couscous_pork.csv')
couscous_pumpkin = pd.read_csv('data/couscous_pumpkin.csv')
pork_raspberries = pd.read_csv('data/pork_raspberries.csv')
pumpkin_yellow_peas = pd.read_csv('data/pumpkin_yellow_peas.csv')
#food_food_formula
formula_black_beans_blackcurrants = pd.read_csv('data/formula_black_beans_blackcurrants.csv')
formula_black_beans_pumpkin = pd.read_csv('data/formula_black_beans_pumpkin.csv')
formula_blackcurrants_kumara_with_skin = pd.read_csv('data/formula_blackcurrants_kumara_with_skin.csv')
formula_blackcurrants_kumara_without_skin = pd.read_csv('data/formula_blackcurrants_kumara_without_skin.csv')
formula_blackcurrants_pork = pd.read_csv('data/formula_blackcurrants_pork.csv')
formula_blackcurrants_soybeans = pd.read_csv('data/formula_blackcurrants_soybeans.csv')
formula_blackcurrants_strawberries = pd.read_csv('data/formula_blackcurrants_strawberries.csv')
formula_chickpeas_pork = pd.read_csv('data/formula_chickpeas_pork.csv')
formula_chickpeas_yellow_peas = pd.read_csv('data/formula_chickpeas_yellow_peas.csv')
formula_couscous_pork = pd.read_csv('data/formula_couscous_pork.csv')
formula_couscous_pumpkin = pd.read_csv('data/formula_couscous_pumpkin.csv')
formula_pork_raspberries = pd.read_csv('data/formula_pork_raspberries.csv')
formula_pumpkin_yellow_peas = pd.read_csv('data/formula_pumpkin_yellow_peas.csv')

#Diluting fluxes to 10%
black_beans["flux"] = black_beans["flux"] / 10
blackcurrants["flux"] = blackcurrants["flux"] / 10
chickpeas["flux"] = chickpeas["flux"] / 10
couscous["flux"] = couscous["flux"] / 10
infant_formula["flux"] = infant_formula["flux"] / 10
kumara_with_skin["flux"] = kumara_with_skin["flux"] / 10
kumara_without_skin["flux"] = kumara_without_skin["flux"] / 10
pork["flux"] = pork["flux"] / 10
prawn["flux"] = prawn["flux"] / 10
pumpkin["flux"] = pumpkin["flux"] / 10
raspberries["flux"] = raspberries["flux"] / 10
soybeans["flux"] = soybeans["flux"] / 10
strawberries["flux"] = strawberries["flux"] / 10
yellow_peas["flux"] = yellow_peas["flux"] / 10
formula_black_beans["flux"] = formula_black_beans["flux"] / 10
formula_blackcurrants["flux"] = formula_blackcurrants["flux"] / 10
formula_chickpeas["flux"] = formula_chickpeas["flux"] / 10
formula_couscous["flux"] = formula_couscous["flux"] / 10
formula_kumara_with_skin["flux"] = formula_kumara_with_skin["flux"] / 10
formula_kumara_without_skin["flux"] = formula_kumara_without_skin["flux"] / 10
formula_pork["flux"] = formula_pork["flux"] / 10
formula_prawn["flux"] = formula_prawn["flux"] / 10
formula_pumpkin["flux"] = formula_pumpkin["flux"] / 10
formula_raspberries["flux"] = formula_raspberries["flux"] / 10
formula_soybeans["flux"] = formula_soybeans["flux"] / 10
formula_strawberries["flux"] = formula_strawberries["flux"] / 10
formula_yellow_peas["flux"] = formula_yellow_peas["flux"] / 10
black_beans_blackcurrants["flux"] = black_beans_blackcurrants["flux"] / 10
black_beans_pumpkin["flux"] = black_beans_pumpkin["flux"] / 10
blackcurrants_kumara_with_skin["flux"] = blackcurrants_kumara_with_skin["flux"] / 10
blackcurrants_kumara_without_skin["flux"] = blackcurrants_kumara_without_skin["flux"] / 10
blackcurrants_pork["flux"] = blackcurrants_pork["flux"] / 10
blackcurrants_soybeans["flux"] = blackcurrants_soybeans["flux"] / 10
blackcurrants_strawberries["flux"] = blackcurrants_strawberries["flux"] / 10
chickpeas_pork["flux"] = chickpeas_pork["flux"] / 10
chickpeas_yellow_peas["flux"] = chickpeas_yellow_peas["flux"] / 10
couscous_pork["flux"] = couscous_pork["flux"] / 10
couscous_pumpkin["flux"] = couscous_pumpkin["flux"] / 10
pork_raspberries["flux"] = pork_raspberries["flux"] / 10
pumpkin_yellow_peas["flux"] = pumpkin_yellow_peas["flux"] / 10
formula_black_beans_blackcurrants["flux"] = formula_black_beans_blackcurrants["flux"] / 10
formula_black_beans_pumpkin["flux"] = formula_black_beans_pumpkin["flux"] / 10
formula_blackcurrants_kumara_with_skin["flux"] = formula_blackcurrants_kumara_with_skin["flux"] / 10
formula_blackcurrants_kumara_without_skin["flux"] = formula_blackcurrants_kumara_without_skin["flux"] / 10
formula_blackcurrants_pork["flux"] = formula_blackcurrants_pork["flux"] / 10
formula_blackcurrants_soybeans["flux"] = formula_blackcurrants_soybeans["flux"] / 10
formula_blackcurrants_strawberries["flux"] = formula_blackcurrants_strawberries["flux"] / 10
formula_chickpeas_pork["flux"] = formula_chickpeas_pork["flux"] / 10
formula_chickpeas_yellow_peas["flux"] = formula_chickpeas_yellow_peas["flux"] / 10
formula_couscous_pork["flux"] = formula_couscous_pork["flux"] / 10
formula_couscous_pumpkin["flux"] = formula_couscous_pumpkin["flux"] / 10
formula_pork_raspberries["flux"] = formula_pork_raspberries["flux"] / 10
formula_pumpkin_yellow_peas["flux"] = formula_pumpkin_yellow_peas["flux"] / 10

#Choosing the tradeoff
#normally 0.3-0.6 works good
#largest tradeoff that allows the majority of the bacteria to grow 
#compromise between individual and cooperative growth
from micom.workflows import tradeoff
from micom.viz import plot_tradeoff

tradeoff_black_beans = tradeoff(manifest, model_folder="models_cplex", medium=black_beans, threads=14) 
plot_tradeoff(tradeoff_black_beans, filename="results/tradeoff_black_beans.html")
tradeoff_blackcurrants = tradeoff(manifest, model_folder="models_cplex", medium=blackcurrants, threads=14) 
plot_tradeoff(tradeoff_blackcurrants, filename="results/tradeoff_blackcurrants.html")
tradeoff_chickpeas = tradeoff(manifest, model_folder="models_cplex", medium=chickpeas, threads=14) 
plot_tradeoff(tradeoff_chickpeas, filename="results/tradeoff_chickpeas.html")
tradeoff_couscous = tradeoff(manifest, model_folder="models_cplex", medium=couscous, threads=14) 
plot_tradeoff(tradeoff_couscous, filename="results/tradeoff_couscous.html")
tradeoff_infant_formula = tradeoff(manifest, model_folder="models_cplex", medium=infant_formula, threads=14) 
plot_tradeoff(tradeoff_infant_formula, filename="results/tradeoff_infant_formula.html")
tradeoff_kumara_with_skin = tradeoff(manifest, model_folder="models_cplex", medium=kumara_with_skin, threads=14) 
plot_tradeoff(tradeoff_kumara_with_skin, filename="results/tradeoff_kumara_with_skin.html")
tradeoff_kumara_without_skin = tradeoff(manifest, model_folder="models_cplex", medium=kumara_without_skin, threads=14) 
plot_tradeoff(tradeoff_kumara_without_skin, filename="results/tradeoff_kumara_without_skin.html")
tradeoff_pork = tradeoff(manifest, model_folder="models_cplex", medium=pork, threads=14) 
plot_tradeoff(tradeoff_pork, filename="results/tradeoff_pork.html")
tradeoff_prawn = tradeoff(manifest, model_folder="models_cplex", medium=prawn, threads=14) 
plot_tradeoff(tradeoff_prawn, filename="results/tradeoff_prawn.html")
tradeoff_pumpkin = tradeoff(manifest, model_folder="models_cplex", medium=pumpkin, threads=14) 
plot_tradeoff(tradeoff_pumpkin, filename="results/tradeoff_pumpkin.html")
tradeoff_raspberries = tradeoff(manifest, model_folder="models_cplex", medium=raspberries, threads=14) 
plot_tradeoff(tradeoff_raspberries, filename="results/tradeoff_raspberries.html")
tradeoff_soybeans = tradeoff(manifest, model_folder="models_cplex", medium=soybeans, threads=14) 
plot_tradeoff(tradeoff_soybeans, filename="results/tradeoff_soybeans.html")
tradeoff_strawberries = tradeoff(manifest, model_folder="models_cplex", medium=strawberries, threads=14) 
plot_tradeoff(tradeoff_strawberries, filename="results/tradeoff_strawberries.html")
tradeoff_yellow_peas = tradeoff(manifest, model_folder="models_cplex", medium=yellow_peas, threads=14) 
plot_tradeoff(tradeoff_yellow_peas, filename="results/tradeoff_yellow_peas.html")
tradeoff_formula_black_beans = tradeoff(manifest, model_folder="models_cplex", medium=formula_black_beans, threads=14) 
plot_tradeoff(tradeoff_formula_black_beans, filename="results/tradeoff_formula_black_beans.html")
tradeoff_formula_blackcurrants = tradeoff(manifest, model_folder="models_cplex", medium=formula_blackcurrants, threads=14) 
plot_tradeoff(tradeoff_formula_blackcurrants, filename="results/tradeoff_formula_blackcurrants.html")
tradeoff_formula_chickpeas = tradeoff(manifest, model_folder="models_cplex", medium=formula_chickpeas, threads=14) 
plot_tradeoff(tradeoff_formula_chickpeas, filename="results/tradeoff_formula_chickpeas.html")
tradeoff_formula_couscous = tradeoff(manifest, model_folder="models_cplex", medium=formula_couscous, threads=14) 
plot_tradeoff(tradeoff_formula_couscous, filename="results/tradeoff_formula_couscous.html")
tradeoff_formula_kumara_with_skin = tradeoff(manifest, model_folder="models_cplex", medium=formula_kumara_with_skin, threads=14) 
plot_tradeoff(tradeoff_formula_kumara_with_skin, filename="results/tradeoff_formula_kumara_with_skin.html")
tradeoff_formula_kumara_without_skin = tradeoff(manifest, model_folder="models_cplex", medium=formula_kumara_without_skin, threads=14) 
plot_tradeoff(tradeoff_formula_kumara_without_skin, filename="results/tradeoff_formula_kumara_without_skin.html")
tradeoff_formula_pork = tradeoff(manifest, model_folder="models_cplex", medium=formula_pork, threads=14) 
plot_tradeoff(tradeoff_formula_pork, filename="results/tradeoff_formula_pork.html")
tradeoff_formula_prawn = tradeoff(manifest, model_folder="models_cplex", medium=formula_prawn, threads=14) 
plot_tradeoff(tradeoff_formula_prawn, filename="results/tradeoff_formula_prawn.html")
tradeoff_formula_pumpkin = tradeoff(manifest, model_folder="models_cplex", medium=formula_pumpkin, threads=14) 
plot_tradeoff(tradeoff_formula_pumpkin, filename="results/tradeoff_formula_pumpkin.html")
tradeoff_formula_raspberries = tradeoff(manifest, model_folder="models_cplex", medium=formula_raspberries, threads=14) 
plot_tradeoff(tradeoff_formula_raspberries, filename="results/tradeoff_formula_raspberries.html")
tradeoff_formula_soybeans = tradeoff(manifest, model_folder="models_cplex", medium=formula_soybeans, threads=14) 
plot_tradeoff(tradeoff_formula_soybeans, filename="results/tradeoff_formula_soybeans.html")
tradeoff_formula_strawberries = tradeoff(manifest, model_folder="models_cplex", medium=formula_strawberries, threads=14) 
plot_tradeoff(tradeoff_formula_strawberries, filename="results/tradeoff_formula_strawberries.html")
tradeoff_formula_yellow_peas = tradeoff(manifest, model_folder="models_cplex", medium=formula_yellow_peas, threads=14) 
plot_tradeoff(tradeoff_formula_yellow_peas, filename="results/tradeoff_formula_yellow_peas.html")
tradeoff_black_beans_blackcurrants = tradeoff(manifest, model_folder="models_cplex", medium=black_beans_blackcurrants, threads=14) 
plot_tradeoff(tradeoff_black_beans_blackcurrants, filename="results/tradeoff_black_beans_blackcurrants.html")
tradeoff_black_beans_pumpkin = tradeoff(manifest, model_folder="models_cplex", medium=black_beans_pumpkin, threads=14) 
plot_tradeoff(tradeoff_black_beans_pumpkin, filename="results/tradeoff_black_beans_pumpkin.html")
tradeoff_blackcurrants_kumara_with_skin = tradeoff(manifest, model_folder="models_cplex", medium=blackcurrants_kumara_with_skin, threads=14) 
plot_tradeoff(tradeoff_blackcurrants_kumara_with_skin, filename="results/tradeoff_blackcurrants_kumara_with_skin.html")
tradeoff_blackcurrants_kumara_without_skin = tradeoff(manifest, model_folder="models_cplex", medium=blackcurrants_kumara_without_skin, threads=14) 
plot_tradeoff(tradeoff_blackcurrants_kumara_without_skin, filename="results/tradeoff_blackcurrants_kumara_without_skin.html")
tradeoff_blackcurrants_pork = tradeoff(manifest, model_folder="models_cplex", medium=blackcurrants_pork, threads=14) 
plot_tradeoff(tradeoff_blackcurrants_pork, filename="results/tradeoff_blackcurrants_pork.html")
tradeoff_blackcurrants_soybeans = tradeoff(manifest, model_folder="models_cplex", medium=blackcurrants_soybeans, threads=14) 
plot_tradeoff(tradeoff_blackcurrants_soybeans, filename="results/tradeoff_blackcurrants_soybeans.html")
tradeoff_blackcurrants_strawberries = tradeoff(manifest, model_folder="models_cplex", medium=blackcurrants_strawberries, threads=14) 
plot_tradeoff(tradeoff_blackcurrants_strawberries, filename="results/tradeoff_blackcurrants_strawberries.html")
tradeoff_chickpeas_pork = tradeoff(manifest, model_folder="models_cplex", medium=chickpeas_pork, threads=14) 
plot_tradeoff(tradeoff_chickpeas_pork, filename="results/tradeoff_chickpeas_pork.html")
tradeoff_chickpeas_yellow_peas = tradeoff(manifest, model_folder="models_cplex", medium=chickpeas_yellow_peas, threads=14) 
plot_tradeoff(tradeoff_chickpeas_yellow_peas, filename="results/tradeoff_chickpeas_yellow_peas.html")
tradeoff_couscous_pork = tradeoff(manifest, model_folder="models_cplex", medium=couscous_pork, threads=14) 
plot_tradeoff(tradeoff_couscous_pork, filename="results/tradeoff_couscous_pork.html")
tradeoff_couscous_pumpkin = tradeoff(manifest, model_folder="models_cplex", medium=couscous_pumpkin, threads=14) 
plot_tradeoff(tradeoff_couscous_pumpkin, filename="results/tradeoff_couscous_pumpkin.html")
tradeoff_pork_raspberries = tradeoff(manifest, model_folder="models_cplex", medium=pork_raspberries, threads=14) 
plot_tradeoff(tradeoff_pork_raspberries, filename="results/tradeoff_pork_raspberries.html")
tradeoff_pumpkin_yellow_peas = tradeoff(manifest, model_folder="models_cplex", medium=pumpkin_yellow_peas, threads=14) 
plot_tradeoff(tradeoff_pumpkin_yellow_peas, filename="results/tradeoff_pumpkin_yellow_peas.html")
tradeoff_formula_black_beans_blackcurrants = tradeoff(manifest, model_folder="models_cplex", medium=formula_black_beans_blackcurrants, threads=14) 
plot_tradeoff(tradeoff_formula_black_beans_blackcurrants, filename="results/tradeoff_formula_black_beans_blackcurrants.html")
tradeoff_formula_black_beans_pumpkin = tradeoff(manifest, model_folder="models_cplex", medium=formula_black_beans_pumpkin, threads=14) 
plot_tradeoff(tradeoff_formula_black_beans_pumpkin, filename="results/tradeoff_formula_black_beans_pumpkin.html")
tradeoff_formula_blackcurrants_kumara_with_skin = tradeoff(manifest, model_folder="models_cplex", medium=formula_blackcurrants_kumara_with_skin, threads=14) 
plot_tradeoff(tradeoff_formula_blackcurrants_kumara_with_skin, filename="results/tradeoff_formula_blackcurrants_kumara_with_skin.html")
tradeoff_formula_blackcurrants_kumara_without_skin = tradeoff(manifest, model_folder="models_cplex", medium=formula_blackcurrants_kumara_without_skin, threads=14) 
plot_tradeoff(tradeoff_formula_blackcurrants_kumara_without_skin, filename="results/tradeoff_formula_blackcurrants_kumara_without_skin.html")
tradeoff_formula_blackcurrants_pork = tradeoff(manifest, model_folder="models_cplex", medium=formula_blackcurrants_pork, threads=14) 
plot_tradeoff(tradeoff_formula_blackcurrants_pork, filename="results/tradeoff_formula_blackcurrants_pork.html")
tradeoff_formula_blackcurrants_soybeans = tradeoff(manifest, model_folder="models_cplex", medium=formula_blackcurrants_soybeans, threads=14) 
plot_tradeoff(tradeoff_formula_blackcurrants_soybeans, filename="results/tradeoff_formula_blackcurrants_soybeans.html")
tradeoff_formula_blackcurrants_strawberries = tradeoff(manifest, model_folder="models_cplex", medium=formula_blackcurrants_strawberries, threads=14) 
plot_tradeoff(tradeoff_formula_blackcurrants_strawberries, filename="results/tradeoff_formula_blackcurrants_strawberries.html")
tradeoff_formula_chickpeas_pork = tradeoff(manifest, model_folder="models_cplex", medium=formula_chickpeas_pork, threads=14) 
plot_tradeoff(tradeoff_formula_chickpeas_pork, filename="results/tradeoff_formula_chickpeas_pork.html")
tradeoff_formula_chickpeas_yellow_peas = tradeoff(manifest, model_folder="models_cplex", medium=formula_chickpeas_yellow_peas, threads=14) 
plot_tradeoff(tradeoff_formula_chickpeas_yellow_peas, filename="results/tradeoff_formula_chickpeas_yellow_peas.html")
tradeoff_formula_couscous_pork = tradeoff(manifest, model_folder="models_cplex", medium=formula_couscous_pork, threads=14) 
plot_tradeoff(tradeoff_formula_couscous_pork, filename="results/tradeoff_formula_couscous_pork.html")
tradeoff_formula_couscous_pumpkin = tradeoff(manifest, model_folder="models_cplex", medium=formula_couscous_pumpkin, threads=14) 
plot_tradeoff(tradeoff_formula_couscous_pumpkin, filename="results/tradeoff_formula_couscous_pumpkin.html")
tradeoff_formula_pork_raspberries = tradeoff(manifest, model_folder="models_cplex", medium=formula_pork_raspberries, threads=14) 
plot_tradeoff(tradeoff_formula_pork_raspberries, filename="results/tradeoff_formula_pork_raspberries.html")
tradeoff_formula_pumpkin_yellow_peas = tradeoff(manifest, model_folder="models_cplex", medium=formula_pumpkin_yellow_peas, threads=14) 
plot_tradeoff(tradeoff_formula_pumpkin_yellow_peas, filename="results/tradeoff_formula_pumpkin_yellow_peas.html")

##Growing the models
#tradeoff was decided based on the previously generated plots
from micom.workflows import grow, save_results

res_black_beans = grow(manifest, model_folder="models_cplex", medium=black_beans, tradeoff=0.7, threads=14) 
save_results(res_black_beans, "results/black_beans.zip") 
res_blackcurrants = grow(manifest, model_folder="models_cplex", medium=blackcurrants, tradeoff=0.7, threads=14) 
save_results(res_blackcurrants, "results/blackcurrants.zip")
res_chickpeas = grow(manifest, model_folder="models_cplex", medium=chickpeas, tradeoff=0.7, threads=14) 
save_results(res_chickpeas, "results/chickpeas.zip") 
res_couscous = grow(manifest, model_folder="models_cplex", medium=couscous, tradeoff=0.7, threads=14) 
save_results(res_couscous, "results/couscous.zip")  
res_infant_formula = grow(manifest, model_folder="models_cplex", medium=infant_formula, tradeoff=0.7, threads=14) 
save_results(res_infant_formula, "results/infant_formula.zip") 
res_kumara_with_skin = grow(manifest, model_folder="models_cplex", medium=kumara_with_skin, tradeoff=0.7, threads=14) 
save_results(res_kumara_with_skin, "results/kumara_with_skin.zip") 
res_kumara_without_skin = grow(manifest, model_folder="models_cplex", medium=kumara_without_skin, tradeoff=0.6, threads=14) 
save_results(res_kumara_without_skin, "results/kumara_without_skin.zip") 
res_pork = grow(manifest, model_folder="models_cplex", medium=pork, tradeoff=0.5, threads=14) 
save_results(res_pork, "results/pork.zip")
res_prawn = grow(manifest, model_folder="models_cplex", medium=prawn, tradeoff=0.5, threads=14) 
save_results(res_prawn, "results/prawn.zip") 
res_pumpkin = grow(manifest, model_folder="models_cplex", medium=pumpkin, tradeoff=0.7, threads=14) 
save_results(res_pumpkin, "results/pumpkin.zip")  
res_raspberries = grow(manifest, model_folder="models_cplex", medium=raspberries, tradeoff=0.7, threads=14) 
save_results(res_raspberries, "results/raspberries.zip") 
res_soybeans = grow(manifest, model_folder="models_cplex", medium=soybeans, tradeoff=0.7, threads=14) 
save_results(res_soybeans, "results/soybeans.zip") 
res_strawberries = grow(manifest, model_folder="models_cplex", medium=strawberries, tradeoff=0.7, threads=14) 
save_results(res_strawberries, "results/strawberries.zip")
res_yellow_peas = grow(manifest, model_folder="models_cplex", medium=yellow_peas, tradeoff=0.7, threads=14) 
save_results(res_yellow_peas, "results/yellow_peas.zip") 
res_formula_black_beans = grow(manifest, model_folder="models_cplex", medium=formula_black_beans, tradeoff=0.7, threads=14) 
save_results(res_formula_black_beans, "results/formula_black_beans.zip") 
res_formula_blackcurrants = grow(manifest, model_folder="models_cplex", medium=formula_blackcurrants, tradeoff=0.6, threads=14) 
save_results(res_formula_blackcurrants, "results/formula_blackcurrants.zip")
res_formula_chickpeas = grow(manifest, model_folder="models_cplex", medium=formula_chickpeas, tradeoff=0.6, threads=14) 
save_results(res_formula_chickpeas, "results/formula_chickpeas.zip") 
res_formula_couscous = grow(manifest, model_folder="models_cplex", medium=formula_couscous, tradeoff=0.4, threads=14) 
save_results(res_formula_couscous, "results/formula_couscous.zip")  
res_formula_kumara_with_skin = grow(manifest, model_folder="models_cplex", medium=formula_kumara_with_skin, tradeoff=0.6, threads=14) 
save_results(res_formula_kumara_with_skin, "results/formula_kumara_with_skin.zip") 
res_formula_kumara_without_skin = grow(manifest, model_folder="models_cplex", medium=formula_kumara_without_skin, tradeoff=0.7, threads=14) 
save_results(res_formula_kumara_without_skin, "results/formula_kumara_without_skin.zip") 
res_formula_pork = grow(manifest, model_folder="models_cplex", medium=formula_pork, tradeoff=0.3, threads=14) 
save_results(res_formula_pork, "results/formula_pork.zip")
res_formula_prawn = grow(manifest, model_folder="models_cplex", medium=formula_prawn, tradeoff=0.6, threads=14) 
save_results(res_formula_prawn, "results/formula_prawn.zip") 
res_formula_pumpkin = grow(manifest, model_folder="models_cplex", medium=formula_pumpkin, tradeoff=0.7, threads=14) 
save_results(res_formula_pumpkin, "results/formula_pumpkin.zip")  
res_formula_raspberries = grow(manifest, model_folder="models_cplex", medium=formula_raspberries, tradeoff=0.7, threads=14) 
save_results(res_formula_raspberries, "results/formula_raspberries.zip") 
res_formula_soybeans = grow(manifest, model_folder="models_cplex", medium=formula_soybeans, tradeoff=0.6, threads=14) 
save_results(res_formula_soybeans, "results/formula_soybeans.zip") 
res_formula_strawberries = grow(manifest, model_folder="models_cplex", medium=formula_strawberries, tradeoff=0.7, threads=14) 
save_results(res_formula_strawberries, "results/formula_strawberries.zip")
res_formula_yellow_peas = grow(manifest, model_folder="models_cplex", medium=formula_yellow_peas, tradeoff=0.7, threads=14) 
save_results(res_formula_yellow_peas, "results/formula_yellow_peas.zip") 
res_black_beans_blackcurrants = grow(manifest, model_folder="models_cplex", medium=black_beans_blackcurrants, tradeoff=0.7, threads=14) 
save_results(res_black_beans_blackcurrants, "results/black_beans_blackcurrants.zip") 
res_black_beans_pumpkin = grow(manifest, model_folder="models_cplex", medium=black_beans_pumpkin, tradeoff=0.7, threads=14) 
save_results(res_black_beans_pumpkin, "results/black_beans_pumpkin.zip")
res_blackcurrants_kumara_with_skin = grow(manifest, model_folder="models_cplex", medium=blackcurrants_kumara_with_skin, tradeoff=0.7, threads=14) 
save_results(res_blackcurrants_kumara_with_skin, "results/blackcurrants_kumara_with_skin.zip") 
res_blackcurrants_kumara_without_skin = grow(manifest, model_folder="models_cplex", medium=blackcurrants_kumara_without_skin, tradeoff=0.7, threads=14) 
save_results(res_blackcurrants_kumara_without_skin, "results/blackcurrants_kumara_without_skin.zip")  
res_blackcurrants_pork = grow(manifest, model_folder="models_cplex", medium=blackcurrants_pork, tradeoff=0.7, threads=14) 
save_results(res_blackcurrants_pork, "results/blackcurrants_pork.zip") 
res_blackcurrants_soybeans = grow(manifest, model_folder="models_cplex", medium=blackcurrants_soybeans, tradeoff=0.7, threads=14) 
save_results(res_blackcurrants_soybeans, "results/blackcurrants_soybeans.zip") 
res_blackcurrants_strawberries = grow(manifest, model_folder="models_cplex", medium=blackcurrants_strawberries, tradeoff=0.6, threads=14) 
save_results(res_blackcurrants_strawberries, "results/blackcurrants_strawberries.zip")
res_chickpeas_pork = grow(manifest, model_folder="models_cplex", medium=chickpeas_pork, tradeoff=0.7, threads=14) 
save_results(res_chickpeas_pork, "results/chickpeas_pork.zip") 
res_chickpeas_yellow_peas = grow(manifest, model_folder="models_cplex", medium=chickpeas_yellow_peas, tradeoff=0.7, threads=14) 
save_results(res_chickpeas_yellow_peas, "results/chickpeas_yellow_peas.zip")  
res_couscous_pork = grow(manifest, model_folder="models_cplex", medium=couscous_pork, tradeoff=0.7, threads=14) 
save_results(res_couscous_pork, "results/couscous_pork.zip") 
res_couscous_pumpkin = grow(manifest, model_folder="models_cplex", medium=couscous_pumpkin, tradeoff=0.7, threads=14) 
save_results(res_couscous_pumpkin, "results/couscous_pumpkin.zip") 
res_pork_raspberries = grow(manifest, model_folder="models_cplex", medium=pork_raspberries, tradeoff=0.6, threads=14) 
save_results(res_pork_raspberries, "results/pork_raspberries.zip")
res_pumpkin_yellow_peas = grow(manifest, model_folder="models_cplex", medium=pumpkin_yellow_peas, tradeoff=0.7, threads=14) 
save_results(res_pumpkin_yellow_peas, "results/pumpkin_yellow_peas.zip") 
res_formula_black_beans_blackcurrants = grow(manifest, model_folder="models_cplex", medium=formula_black_beans_blackcurrants, tradeoff=0.7, threads=14) 
save_results(res_formula_black_beans_blackcurrants, "results/formula_black_beans_blackcurrants.zip") 
res_formula_black_beans_pumpkin = grow(manifest, model_folder="models_cplex", medium=formula_black_beans_pumpkin, tradeoff=0.7, threads=14) 
save_results(res_formula_black_beans_pumpkin, "results/formula_black_beans_pumpkin.zip")
res_formula_blackcurrants_kumara_with_skin = grow(manifest, model_folder="models_cplex", medium=formula_blackcurrants_kumara_with_skin, tradeoff=0.7, threads=14) 
save_results(res_formula_blackcurrants_kumara_with_skin, "results/formula_blackcurrants_kumara_with_skin.zip") 
res_formula_blackcurrants_kumara_without_skin = grow(manifest, model_folder="models_cplex", medium=formula_blackcurrants_kumara_without_skin, tradeoff=0.6, threads=14) 
save_results(res_formula_blackcurrants_kumara_without_skin, "results/formula_blackcurrants_kumara_without_skin.zip")  
res_formula_blackcurrants_pork = grow(manifest, model_folder="models_cplex", medium=formula_blackcurrants_pork, tradeoff=0.7, threads=14) 
save_results(res_formula_blackcurrants_pork, "results/formula_blackcurrants_pork.zip") 
res_formula_blackcurrants_soybeans = grow(manifest, model_folder="models_cplex", medium=formula_blackcurrants_soybeans, tradeoff=0.7, threads=14) 
save_results(res_formula_blackcurrants_soybeans, "results/formula_blackcurrants_soybeans.zip") 
res_formula_blackcurrants_strawberries = grow(manifest, model_folder="models_cplex", medium=formula_blackcurrants_strawberries, tradeoff=0.7, threads=14) 
save_results(res_formula_blackcurrants_strawberries, "results/formula_blackcurrants_strawberries.zip")
res_formula_chickpeas_pork = grow(manifest, model_folder="models_cplex", medium=formula_chickpeas_pork, tradeoff=0.7, threads=14) 
save_results(res_formula_chickpeas_pork, "results/formula_chickpeas_pork.zip") 
res_formula_chickpeas_yellow_peas = grow(manifest, model_folder="models_cplex", medium=formula_chickpeas_yellow_peas, tradeoff=0.7, threads=14) 
save_results(res_formula_chickpeas_yellow_peas, "results/formula_chickpeas_yellow_peas.zip")  
res_formula_couscous_pork = grow(manifest, model_folder="models_cplex", medium=formula_couscous_pork, tradeoff=0.4, threads=14) 
save_results(res_formula_couscous_pork, "results/formula_couscous_pork.zip") 
res_formula_couscous_pumpkin = grow(manifest, model_folder="models_cplex", medium=formula_couscous_pumpkin, tradeoff=0.7, threads=14) 
save_results(res_formula_couscous_pumpkin, "results/formula_couscous_pumpkin.zip") 
res_formula_pork_raspberries = grow(manifest, model_folder="models_cplex", medium=formula_pork_raspberries, tradeoff=0.7, threads=14) 
save_results(res_formula_pork_raspberries, "results/formula_pork_raspberries.zip")
res_formula_pumpkin_yellow_peas = grow(manifest, model_folder="models_cplex", medium=formula_pumpkin_yellow_peas, tradeoff=0.7, threads=14) 
save_results(res_formula_pumpkin_yellow_peas, "results/formula_pumpkin_yellow_peas.zip") 

#Production rate
from micom.measures import production_rates
import pandas as pd

prod_black_beans = production_rates(res_black_beans)
prod_blackcurrants = production_rates(res_blackcurrants)
prod_chickpeas = production_rates(res_chickpeas)
prod_couscous = production_rates(res_couscous)
prod_infant_formula = production_rates(res_infant_formula)
prod_kumara_with_skin = production_rates(res_kumara_with_skin)
prod_kumara_without_skin = production_rates(res_kumara_without_skin)
prod_pork = production_rates(res_pork)
prod_prawn = production_rates(res_prawn)
prod_pumpkin = production_rates(res_pumpkin)
prod_raspberries = production_rates(res_raspberries)
prod_soybeans = production_rates(res_soybeans)
prod_strawberries = production_rates(res_strawberries)
prod_yellow_peas = production_rates(res_yellow_peas)
prod_formula_black_beans = production_rates(res_formula_black_beans)
prod_formula_blackcurrants = production_rates(res_formula_blackcurrants)
prod_formula_chickpeas = production_rates(res_formula_chickpeas)
prod_formula_couscous = production_rates(res_formula_couscous)
prod_formula_kumara_with_skin = production_rates(res_formula_kumara_with_skin)
prod_formula_kumara_without_skin = production_rates(res_formula_kumara_without_skin)
prod_formula_pork = production_rates(res_formula_pork)
prod_formula_prawn = production_rates(res_formula_prawn)
prod_formula_pumpkin = production_rates(res_formula_pumpkin)
prod_formula_raspberries = production_rates(res_formula_raspberries)
prod_formula_soybeans = production_rates(res_formula_soybeans)
prod_formula_strawberries = production_rates(res_formula_strawberries)
prod_formula_yellow_peas = production_rates(res_formula_yellow_peas)
prod_black_beans_blackcurrants = production_rates(res_black_beans_blackcurrants)
prod_black_beans_pumpkin = production_rates(res_black_beans_pumpkin)
prod_blackcurrants_kumara_with_skin = production_rates(res_blackcurrants_kumara_with_skin)
prod_blackcurrants_kumara_without_skin = production_rates(res_blackcurrants_kumara_without_skin)
prod_blackcurrants_pork = production_rates(res_blackcurrants_pork)
prod_blackcurrants_soybeans = production_rates(res_blackcurrants_soybeans)
prod_blackcurrants_strawberries = production_rates(res_blackcurrants_strawberries)
prod_chickpeas_pork = production_rates(res_chickpeas_pork)
prod_chickpeas_yellow_peas = production_rates(res_chickpeas_yellow_peas)
prod_couscous_pork = production_rates(res_couscous_pork)
prod_couscous_pumpkin = production_rates(res_couscous_pumpkin)
prod_pork_raspberries = production_rates(res_pork_raspberries)
prod_pumpkin_yellow_peas = production_rates(res_pumpkin_yellow_peas)
prod_formula_black_beans_blackcurrants = production_rates(res_formula_black_beans_blackcurrants)
prod_formula_black_beans_pumpkin = production_rates(res_formula_black_beans_pumpkin)
prod_formula_blackcurrants_kumara_with_skin = production_rates(res_formula_blackcurrants_kumara_with_skin)
prod_formula_blackcurrants_kumara_without_skin = production_rates(res_formula_blackcurrants_kumara_without_skin)
prod_formula_blackcurrants_pork = production_rates(res_formula_blackcurrants_pork)
prod_formula_blackcurrants_soybeans = production_rates(res_formula_blackcurrants_soybeans)
prod_formula_blackcurrants_strawberries = production_rates(res_formula_blackcurrants_strawberries)
prod_formula_chickpeas_pork = production_rates(res_formula_chickpeas_pork)
prod_formula_chickpeas_yellow_peas = production_rates(res_formula_chickpeas_yellow_peas)
prod_formula_couscous_pork = production_rates(res_formula_couscous_pork)
prod_formula_couscous_pumpkin = production_rates(res_formula_couscous_pumpkin)
prod_formula_pork_raspberries = production_rates(res_formula_pork_raspberries)
prod_formula_pumpkin_yellow_peas = production_rates(res_formula_pumpkin_yellow_peas)

prod_black_beans['diet'] = 'black_beans' #create new colum
prod_blackcurrants['diet'] = 'blackcurrants' #create new colum
prod_chickpeas['diet'] = 'chickpeas' #create new colum
prod_couscous['diet'] = 'couscous' #create new colum
prod_infant_formula['diet'] = 'infant_formula' #create new colum
prod_kumara_with_skin['diet'] = 'kumara_with_skin' #create new colum
prod_kumara_without_skin['diet'] = 'kumara_without_skin' #create new colum
prod_pork['diet'] = 'pork' #create new colum
prod_prawn['diet'] = 'prawn' #create new colum
prod_pumpkin['diet'] = 'pumpkin' #create new colum
prod_raspberries['diet'] = 'raspberries' #create new colum
prod_soybeans['diet'] = 'soybeans' #create new colum
prod_strawberries['diet'] = 'strawberries' #create new colum
prod_yellow_peas['diet'] = 'yellow_peas' #create new colum
prod_formula_black_beans['diet'] = 'formula_black_beans' #create new colum
prod_formula_blackcurrants['diet'] = 'formula_blackcurrants' #create new colum
prod_formula_chickpeas['diet'] = 'formula_chickpeas' #create new colum
prod_formula_couscous['diet'] = 'formula_couscous' #create new colum
prod_formula_kumara_with_skin['diet'] = 'formula_kumara_with_skin' #create new colum
prod_formula_kumara_without_skin['diet'] = 'formula_kumara_without_skin' #create new colum
prod_formula_pork['diet'] = 'formula_pork' #create new colum
prod_formula_prawn['diet'] = 'formula_prawn' #create new colum
prod_formula_pumpkin['diet'] = 'formula_pumpkin' #create new colum
prod_formula_raspberries['diet'] = 'formula_raspberries' #create new colum
prod_formula_soybeans['diet'] = 'formula_soybeans' #create new colum
prod_formula_strawberries['diet'] = 'formula_strawberries' #create new colum
prod_formula_yellow_peas['diet'] = 'formula_yellow_peas' #create new colum
prod_black_beans_blackcurrants['diet'] = 'black_beans_blackcurrants' #create new colum
prod_black_beans_pumpkin['diet'] = 'black_beans_pumpkin' #create new colum
prod_blackcurrants_kumara_with_skin['diet'] = 'blackcurrants_kumara_with_skin' #create new colum
prod_blackcurrants_kumara_without_skin['diet'] = 'blackcurrants_kumara_without_skin' #create new colum
prod_blackcurrants_pork['diet'] = 'blackcurrants_pork' #create new colum
prod_blackcurrants_soybeans['diet'] = 'blackcurrants_soybeans' #create new colum
prod_blackcurrants_strawberries['diet'] = 'blackcurrants_strawberries' #create new colum
prod_chickpeas_pork['diet'] = 'chickpeas_pork' #create new colum
prod_chickpeas_yellow_peas['diet'] = 'chickpeas_yellow_peas' #create new colum
prod_couscous_pork['diet'] = 'couscous_pork' #create new colum
prod_couscous_pumpkin['diet'] = 'couscous_pumpkin' #create new colum
prod_pork_raspberries['diet'] = 'pork_raspberries' #create new colum
prod_pumpkin_yellow_peas['diet'] = 'pumpkin_yellow_peas' #create new colum
prod_formula_black_beans_blackcurrants['diet'] = 'formula_black_beans_blackcurrants' #create new colum
prod_formula_black_beans_pumpkin['diet'] = 'formula_black_beans_pumpkin' #create new colum
prod_formula_blackcurrants_kumara_with_skin['diet'] = 'formula_blackcurrants_kumara_with_skin' #create new colum
prod_formula_blackcurrants_kumara_without_skin['diet'] = 'formula_blackcurrants_kumara_without_skin' #create new colum
prod_formula_blackcurrants_pork['diet'] = 'formula_blackcurrants_pork' #create new colum
prod_formula_blackcurrants_soybeans['diet'] = 'formula_blackcurrants_soybeans' #create new colum
prod_formula_blackcurrants_strawberries['diet'] = 'formula_blackcurrants_strawberries' #create new colum
prod_formula_chickpeas_pork['diet'] = 'formula_chickpeas_pork' #create new colum
prod_formula_chickpeas_yellow_peas['diet'] = 'formula_chickpeas_yellow_peas' #create new colum
prod_formula_couscous_pork['diet'] = 'formula_couscous_pork' #create new colum
prod_formula_couscous_pumpkin['diet'] = 'formula_couscous_pumpkin' #create new colum
prod_formula_pork_raspberries['diet'] = 'formula_pork_raspberries' #create new colum
prod_formula_pumpkin_yellow_peas['diet'] = 'formula_pumpkin_yellow_peas' #create new colum

exchanges = pd.concat([prod_black_beans,prod_blackcurrants,prod_chickpeas,prod_couscous,prod_infant_formula,
                       prod_kumara_with_skin,prod_kumara_without_skin,prod_pork,prod_prawn,prod_pumpkin,prod_raspberries,
                       prod_soybeans,prod_strawberries,prod_yellow_peas])  # merge the production rates

exchanges = pd.pivot_table(exchanges, index = ['diet'], columns = 'name', values = 'flux') #converting into matrix
exchanges_reduced = exchanges[["Acetate", "Propionate", "Butyrate"]] #selecting the metabolites of interest
exchanges_reduced.to_csv("results_foods/exchanges_reduced.csv")

exchanges_formula_food = pd.concat([prod_formula_black_beans,prod_formula_blackcurrants,prod_formula_chickpeas,prod_formula_couscous,prod_formula_kumara_with_skin,
                       prod_formula_kumara_without_skin,prod_formula_pork,prod_formula_prawn,prod_formula_pumpkin,prod_formula_raspberries,
                       prod_formula_soybeans,prod_formula_strawberries,prod_formula_yellow_peas])  # merge the production rates

exchanges_formula_food = pd.pivot_table(exchanges_formula_food, index = ['diet'], columns = 'name', values = 'flux') #converting into matrix
exchanges_formula_food_reduced = exchanges_formula_food[["Acetate", "Propionate", "Butyrate"]] #selecting the metabolites of interest
exchanges_formula_food_reduced.to_csv("results/exchanges_formula_food_reduced.csv")

exchanges_food_foods = pd.concat([prod_black_beans_blackcurrants,prod_black_beans_pumpkin,prod_blackcurrants_kumara_with_skin,prod_blackcurrants_kumara_without_skin,prod_blackcurrants_pork,
                       prod_blackcurrants_soybeans,prod_blackcurrants_strawberries,prod_chickpeas_pork,prod_chickpeas_yellow_peas,prod_couscous_pork,
                       prod_couscous_pumpkin,prod_pork_raspberries,prod_pumpkin_yellow_peas])  # merge the production rates

exchanges_food_foods = pd.pivot_table(exchanges_food_foods, index = ['diet'], columns = 'name', values = 'flux') #converting into matrix
exchanges_food_foods_reduced = exchanges_food_foods[["Acetate", "Propionate", "Butyrate"]] #selecting the metabolites of interest
exchanges_food_foods_reduced.to_csv("results/exchanges_food_foods_reduced.csv")

exchanges_formula_food_foods = pd.concat([prod_formula_black_beans_blackcurrants,prod_formula_black_beans_pumpkin,prod_formula_blackcurrants_kumara_with_skin,prod_formula_blackcurrants_kumara_without_skin,prod_formula_blackcurrants_pork,
                       prod_formula_blackcurrants_soybeans,prod_formula_blackcurrants_strawberries,prod_formula_chickpeas_pork,prod_formula_chickpeas_yellow_peas,prod_formula_couscous_pork,
                       prod_formula_couscous_pumpkin,prod_formula_pork_raspberries,prod_formula_pumpkin_yellow_peas])  # merge the production rates

exchanges_formula_food_foods = pd.pivot_table(exchanges_formula_food_foods, index = ['diet'], columns = 'name', values = 'flux') #converting into matrix
exchanges_formula_food_foods_reduced = exchanges_formula_food_foods[["Acetate", "Propionate", "Butyrate"]] #selecting the metabolites of interest
exchanges_formula_food_foods_reduced.to_csv("results/exchanges_formula_food_foods_reduced.csv")