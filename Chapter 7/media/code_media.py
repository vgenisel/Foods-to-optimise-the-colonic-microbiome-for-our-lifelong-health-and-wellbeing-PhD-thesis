##Diets for comparison in silico vs in vitro
#AGORA2
#growth rate to 0.3

#Foods: 150g of dry mass
#Food-formula: 120g DW formula + 30g DW food
#Food-food : 75g DW food1 + 75g DW food2
#Food-food-formula: 15g DW food1 + 15g DW food2 + 120g formula

#Importing the dietary fluxes and converting then
import pandas as pd

diet_black_beans = pd.read_csv("data/black_beans.tsv", sep="\t", header=None) #importing fluxes
diet_black_beans.columns = ["reaction", "flux"] #changing the name of the columns
diet_blackcurrants = pd.read_csv("data/blackcurrants.tsv", sep="\t", header=None) #importing fluxes
diet_blackcurrants.columns = ["reaction", "flux"] #changing the name of the columns
diet_chickpeas = pd.read_csv("data/chickpeas.tsv", sep="\t", header=None) #importing fluxes
diet_chickpeas.columns = ["reaction", "flux"] #changing the name of the columns
diet_couscous = pd.read_csv("data/couscous.tsv", sep="\t", header=None) #importing fluxes
diet_couscous.columns = ["reaction", "flux"] #changing the name of the columns
diet_infant_formula = pd.read_csv("data/infant_formula.tsv", sep="\t", header=None) #importing fluxes
diet_infant_formula.columns = ["reaction", "flux"] #changing the name of the columns
diet_kumara_with_skin = pd.read_csv("data/kumara_with_skin.tsv", sep="\t", header=None) #importing fluxes
diet_kumara_with_skin.columns = ["reaction", "flux"] #changing the name of the columns
diet_kumara_without_skin = pd.read_csv("data/kumara_without_skin.tsv", sep="\t", header=None) #importing fluxes
diet_kumara_without_skin.columns = ["reaction", "flux"] #changing the name of the columns
diet_pork = pd.read_csv("data/pork.tsv", sep="\t", header=None) #importing fluxes
diet_pork.columns = ["reaction", "flux"] #changing the name of the columns
diet_prawn = pd.read_csv("data/prawn.tsv", sep="\t", header=None) #importing fluxes
diet_prawn.columns = ["reaction", "flux"] #changing the name of the columns
diet_pumpkin = pd.read_csv("data/pumpkin.tsv", sep="\t", header=None) #importing fluxes
diet_pumpkin.columns = ["reaction", "flux"] #changing the name of the columns
diet_raspberries = pd.read_csv("data/raspberries.tsv", sep="\t", header=None) #importing fluxes
diet_raspberries.columns = ["reaction", "flux"] #changing the name of the columns
diet_soybeans = pd.read_csv("data/soybeans.tsv", sep="\t", header=None) #importing fluxes
diet_soybeans.columns = ["reaction", "flux"] #changing the name of the columns
diet_strawberries = pd.read_csv("data/strawberries.tsv", sep="\t", header=None) #importing fluxes
diet_strawberries.columns = ["reaction", "flux"] #changing the name of the columns
diet_yellow_peas = pd.read_csv("data/yellow_peas.tsv", sep="\t", header=None) #importing fluxes
diet_yellow_peas.columns = ["reaction", "flux"] #changing the name of the columns
diet_formula_black_beans = pd.read_csv("data/formula_black_beans.tsv", sep="\t", header=None) #importing fluxes
diet_formula_black_beans.columns = ["reaction", "flux"] #changing the name of the columns
diet_formula_blackcurrants = pd.read_csv("data/formula_blackcurrants.tsv", sep="\t", header=None) #importing fluxes
diet_formula_blackcurrants.columns = ["reaction", "flux"] #changing the name of the columns
diet_formula_chickpeas = pd.read_csv("data/formula_chickpeas.tsv", sep="\t", header=None) #importing fluxes
diet_formula_chickpeas.columns = ["reaction", "flux"] #changing the name of the columns
diet_formula_couscous = pd.read_csv("data/formula_couscous.tsv", sep="\t", header=None) #importing fluxes
diet_formula_couscous.columns = ["reaction", "flux"] #changing the name of the columns
diet_formula_kumara_with_skin = pd.read_csv("data/formula_kumara_with_skin.tsv", sep="\t", header=None) #importing fluxes
diet_formula_kumara_with_skin.columns = ["reaction", "flux"] #changing the name of the columns
diet_formula_kumara_without_skin = pd.read_csv("data/formula_kumara_without_skin.tsv", sep="\t", header=None) #importing fluxes
diet_formula_kumara_without_skin.columns = ["reaction", "flux"] #changing the name of the columns
diet_formula_pork = pd.read_csv("data/formula_pork.tsv", sep="\t", header=None) #importing fluxes
diet_formula_pork.columns = ["reaction", "flux"] #changing the name of the columns
diet_formula_prawn = pd.read_csv("data/formula_prawn.tsv", sep="\t", header=None) #importing fluxes
diet_formula_prawn.columns = ["reaction", "flux"] #changing the name of the columns
diet_formula_pumpkin = pd.read_csv("data/formula_pumpkin.tsv", sep="\t", header=None) #importing fluxes
diet_formula_pumpkin.columns = ["reaction", "flux"] #changing the name of the columns
diet_formula_raspberries = pd.read_csv("data/formula_raspberries.tsv", sep="\t", header=None) #importing fluxes
diet_formula_raspberries.columns = ["reaction", "flux"] #changing the name of the columns
diet_formula_soybeans = pd.read_csv("data/formula_soybeans.tsv", sep="\t", header=None) #importing fluxes
diet_formula_soybeans.columns = ["reaction", "flux"] #changing the name of the columns
diet_formula_strawberries = pd.read_csv("data/formula_strawberries.tsv", sep="\t", header=None) #importing fluxes
diet_formula_strawberries.columns = ["reaction", "flux"] #changing the name of the columns
diet_formula_yellow_peas = pd.read_csv("data/formula_yellow_peas.tsv", sep="\t", header=None) #importing fluxes
diet_formula_yellow_peas.columns = ["reaction", "flux"] #changing the name of the columns
diet_black_beans_blackcurrants = pd.read_csv("data/black_beans_blackcurrants.tsv", sep="\t", header=None) #importing fluxes
diet_black_beans_blackcurrants.columns = ["reaction", "flux"] #changing the name of the columns
diet_black_beans_pumpkin = pd.read_csv("data/black_beans_pumpkin.tsv", sep="\t", header=None) #importing fluxes
diet_black_beans_pumpkin.columns = ["reaction", "flux"] #changing the name of the columns
diet_blackcurrants_kumara_with_skin = pd.read_csv("data/blackcurrants_kumara_with_skin.tsv", sep="\t", header=None) #importing fluxes
diet_blackcurrants_kumara_with_skin.columns = ["reaction", "flux"] #changing the name of the columns
diet_blackcurrants_kumara_without_skin = pd.read_csv("data/blackcurrants_kumara_without_skin.tsv", sep="\t", header=None) #importing fluxes
diet_blackcurrants_kumara_without_skin.columns = ["reaction", "flux"] #changing the name of the columns
diet_blackcurrants_pork = pd.read_csv("data/blackcurrants_pork.tsv", sep="\t", header=None) #importing fluxes
diet_blackcurrants_pork.columns = ["reaction", "flux"] #changing the name of the columns
diet_blackcurrants_soybeans = pd.read_csv("data/blackcurrants_soybeans.tsv", sep="\t", header=None) #importing fluxes
diet_blackcurrants_soybeans.columns = ["reaction", "flux"] #changing the name of the columns
diet_blackcurrants_strawberries = pd.read_csv("data/blackcurrants_strawberries.tsv", sep="\t", header=None) #importing fluxes
diet_blackcurrants_strawberries.columns = ["reaction", "flux"] #changing the name of the columns
diet_chickpeas_pork = pd.read_csv("data/chickpeas_pork.tsv", sep="\t", header=None) #importing fluxes
diet_chickpeas_pork.columns = ["reaction", "flux"] #changing the name of the columns
diet_chickpeas_yellow_peas = pd.read_csv("data/chickpeas_yellow_peas.tsv", sep="\t", header=None) #importing fluxes
diet_chickpeas_yellow_peas.columns = ["reaction", "flux"] #changing the name of the columns
diet_couscous_pork = pd.read_csv("data/couscous_pork.tsv", sep="\t", header=None) #importing fluxes
diet_couscous_pork.columns = ["reaction", "flux"] #changing the name of the columns
diet_couscous_pumpkin = pd.read_csv("data/couscous_pumpkin.tsv", sep="\t", header=None) #importing fluxes
diet_couscous_pumpkin.columns = ["reaction", "flux"] #changing the name of the columns
diet_pork_raspberries = pd.read_csv("data/pork_raspberries.tsv", sep="\t", header=None) #importing fluxes
diet_pork_raspberries.columns = ["reaction", "flux"] #changing the name of the columns
diet_pumpkin_yellow_peas = pd.read_csv("data/pumpkin_yellow_peas.tsv", sep="\t", header=None) #importing fluxes
diet_pumpkin_yellow_peas.columns = ["reaction", "flux"] #changing the name of the columns
diet_formula_black_beans_blackcurrants = pd.read_csv("data/formula_black_beans_blackcurrants.tsv", sep="\t", header=None) #importing fluxes
diet_formula_black_beans_blackcurrants.columns = ["reaction", "flux"] #changing the name of the columns
diet_formula_black_beans_pumpkin = pd.read_csv("data/formula_black_beans_pumpkin.tsv", sep="\t", header=None) #importing fluxes
diet_formula_black_beans_pumpkin.columns = ["reaction", "flux"] #changing the name of the columns
diet_formula_blackcurrants_kumara_with_skin = pd.read_csv("data/formula_blackcurrants_kumara_with_skin.tsv", sep="\t", header=None) #importing fluxes
diet_formula_blackcurrants_kumara_with_skin.columns = ["reaction", "flux"] #changing the name of the columns
diet_formula_blackcurrants_kumara_without_skin = pd.read_csv("data/formula_blackcurrants_kumara_without_skin.tsv", sep="\t", header=None) #importing fluxes
diet_formula_blackcurrants_kumara_without_skin.columns = ["reaction", "flux"] #changing the name of the columns
diet_formula_blackcurrants_pork = pd.read_csv("data/formula_blackcurrants_pork.tsv", sep="\t", header=None) #importing fluxes
diet_formula_blackcurrants_pork.columns = ["reaction", "flux"] #changing the name of the columns
diet_formula_blackcurrants_soybeans = pd.read_csv("data/formula_blackcurrants_soybeans.tsv", sep="\t", header=None) #importing fluxes
diet_formula_blackcurrants_soybeans.columns = ["reaction", "flux"] #changing the name of the columns
diet_formula_blackcurrants_strawberries = pd.read_csv("data/formula_blackcurrants_strawberries.tsv", sep="\t", header=None) #importing fluxes
diet_formula_blackcurrants_strawberries.columns = ["reaction", "flux"] #changing the name of the columns
diet_formula_chickpeas_pork = pd.read_csv("data/formula_chickpeas_pork.tsv", sep="\t", header=None) #importing fluxes
diet_formula_chickpeas_pork.columns = ["reaction", "flux"] #changing the name of the columns
diet_formula_chickpeas_yellow_peas = pd.read_csv("data/formula_chickpeas_yellow_peas.tsv", sep="\t", header=None) #importing fluxes
diet_formula_chickpeas_yellow_peas.columns = ["reaction", "flux"] #changing the name of the columns
diet_formula_couscous_pork = pd.read_csv("data/formula_couscous_pork.tsv", sep="\t", header=None) #importing fluxes
diet_formula_couscous_pork.columns = ["reaction", "flux"] #changing the name of the columns
diet_formula_couscous_pumpkin = pd.read_csv("data/formula_couscous_pumpkin.tsv", sep="\t", header=None) #importing fluxes
diet_formula_couscous_pumpkin.columns = ["reaction", "flux"] #changing the name of the columns
diet_formula_pork_raspberries = pd.read_csv("data/formula_pork_raspberries.tsv", sep="\t", header=None) #importing fluxes
diet_formula_pork_raspberries.columns = ["reaction", "flux"] #changing the name of the columns
diet_formula_pumpkin_yellow_peas = pd.read_csv("data/formula_pumpkin_yellow_peas.tsv", sep="\t", header=None) #importing fluxes
diet_formula_pumpkin_yellow_peas.columns = ["reaction", "flux"] #changing the name of the columns

annotations = pd.read_csv("data/agora_metabolites.csv") #importing a table with the description of agora metabolites
 
diet_black_beans = diet_black_beans.rename(columns={diet_black_beans.columns[0]: "reaction"})
diet_black_beans["metabolite"] = diet_black_beans.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_black_beans.loc[diet_black_beans.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_black_beans.loc[diet_black_beans.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_blackcurrants = diet_blackcurrants.rename(columns={diet_blackcurrants.columns[0]: "reaction"})
diet_blackcurrants["metabolite"] = diet_blackcurrants.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_blackcurrants.loc[diet_blackcurrants.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_blackcurrants.loc[diet_blackcurrants.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_chickpeas = diet_chickpeas.rename(columns={diet_chickpeas.columns[0]: "reaction"})
diet_chickpeas["metabolite"] = diet_chickpeas.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_chickpeas.loc[diet_chickpeas.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_chickpeas.loc[diet_chickpeas.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_couscous = diet_couscous.rename(columns={diet_couscous.columns[0]: "reaction"})
diet_couscous["metabolite"] = diet_couscous.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_couscous.loc[diet_couscous.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_couscous.loc[diet_couscous.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_infant_formula = diet_infant_formula.rename(columns={diet_infant_formula.columns[0]: "reaction"})
diet_infant_formula["metabolite"] = diet_infant_formula.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_infant_formula.loc[diet_infant_formula.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_infant_formula.loc[diet_infant_formula.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_kumara_with_skin = diet_kumara_with_skin.rename(columns={diet_kumara_with_skin.columns[0]: "reaction"})
diet_kumara_with_skin["metabolite"] = diet_kumara_with_skin.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_kumara_with_skin.loc[diet_kumara_with_skin.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_kumara_with_skin.loc[diet_kumara_with_skin.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_kumara_without_skin = diet_kumara_without_skin.rename(columns={diet_kumara_without_skin.columns[0]: "reaction"})
diet_kumara_without_skin["metabolite"] = diet_kumara_without_skin.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_kumara_without_skin.loc[diet_kumara_without_skin.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_kumara_without_skin.loc[diet_kumara_without_skin.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_pork = diet_pork.rename(columns={diet_pork.columns[0]: "reaction"})
diet_pork["metabolite"] = diet_pork.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_pork.loc[diet_pork.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_pork.loc[diet_pork.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_prawn = diet_prawn.rename(columns={diet_prawn.columns[0]: "reaction"})
diet_prawn["metabolite"] = diet_prawn.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_prawn.loc[diet_prawn.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_prawn.loc[diet_prawn.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_pumpkin = diet_pumpkin.rename(columns={diet_pumpkin.columns[0]: "reaction"})
diet_pumpkin["metabolite"] = diet_pumpkin.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_pumpkin.loc[diet_pumpkin.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_pumpkin.loc[diet_pumpkin.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_raspberries = diet_raspberries.rename(columns={diet_raspberries.columns[0]: "reaction"})
diet_raspberries["metabolite"] = diet_raspberries.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_raspberries.loc[diet_raspberries.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_raspberries.loc[diet_raspberries.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_soybeans = diet_soybeans.rename(columns={diet_soybeans.columns[0]: "reaction"})
diet_soybeans["metabolite"] = diet_soybeans.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_soybeans.loc[diet_soybeans.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_soybeans.loc[diet_soybeans.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_strawberries = diet_strawberries.rename(columns={diet_strawberries.columns[0]: "reaction"})
diet_strawberries["metabolite"] = diet_strawberries.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_strawberries.loc[diet_strawberries.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_strawberries.loc[diet_strawberries.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_yellow_peas = diet_yellow_peas.rename(columns={diet_yellow_peas.columns[0]: "reaction"})
diet_yellow_peas["metabolite"] = diet_yellow_peas.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_yellow_peas.loc[diet_yellow_peas.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_yellow_peas.loc[diet_yellow_peas.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_formula_black_beans = diet_formula_black_beans.rename(columns={diet_formula_black_beans.columns[0]: "reaction"})
diet_formula_black_beans["metabolite"] = diet_formula_black_beans.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_formula_black_beans.loc[diet_formula_black_beans.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_formula_black_beans.loc[diet_formula_black_beans.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_formula_blackcurrants = diet_formula_blackcurrants.rename(columns={diet_formula_blackcurrants.columns[0]: "reaction"})
diet_formula_blackcurrants["metabolite"] = diet_formula_blackcurrants.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_formula_blackcurrants.loc[diet_formula_blackcurrants.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_formula_blackcurrants.loc[diet_formula_blackcurrants.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_formula_chickpeas = diet_formula_chickpeas.rename(columns={diet_formula_chickpeas.columns[0]: "reaction"})
diet_formula_chickpeas["metabolite"] = diet_formula_chickpeas.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_formula_chickpeas.loc[diet_formula_chickpeas.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_formula_chickpeas.loc[diet_formula_chickpeas.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_formula_couscous = diet_formula_couscous.rename(columns={diet_formula_couscous.columns[0]: "reaction"})
diet_formula_couscous["metabolite"] = diet_formula_couscous.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_formula_couscous.loc[diet_formula_couscous.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_formula_couscous.loc[diet_formula_couscous.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_formula_kumara_with_skin = diet_formula_kumara_with_skin.rename(columns={diet_formula_kumara_with_skin.columns[0]: "reaction"})
diet_formula_kumara_with_skin["metabolite"] = diet_formula_kumara_with_skin.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_formula_kumara_with_skin.loc[diet_formula_kumara_with_skin.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_formula_kumara_with_skin.loc[diet_formula_kumara_with_skin.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_formula_kumara_without_skin = diet_formula_kumara_without_skin.rename(columns={diet_formula_kumara_without_skin.columns[0]: "reaction"})
diet_formula_kumara_without_skin["metabolite"] = diet_formula_kumara_without_skin.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_formula_kumara_without_skin.loc[diet_formula_kumara_without_skin.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_formula_kumara_without_skin.loc[diet_formula_kumara_without_skin.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_formula_pork = diet_formula_pork.rename(columns={diet_formula_pork.columns[0]: "reaction"})
diet_formula_pork["metabolite"] = diet_formula_pork.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_formula_pork.loc[diet_formula_pork.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_formula_pork.loc[diet_formula_pork.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_formula_prawn = diet_formula_prawn.rename(columns={diet_formula_prawn.columns[0]: "reaction"})
diet_formula_prawn["metabolite"] = diet_formula_prawn.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_formula_prawn.loc[diet_formula_prawn.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_formula_prawn.loc[diet_formula_prawn.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_formula_pumpkin = diet_formula_pumpkin.rename(columns={diet_formula_pumpkin.columns[0]: "reaction"})
diet_formula_pumpkin["metabolite"] = diet_formula_pumpkin.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_formula_pumpkin.loc[diet_formula_pumpkin.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_formula_pumpkin.loc[diet_formula_pumpkin.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_formula_raspberries = diet_formula_raspberries.rename(columns={diet_formula_raspberries.columns[0]: "reaction"})
diet_formula_raspberries["metabolite"] = diet_formula_raspberries.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_formula_raspberries.loc[diet_formula_raspberries.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_formula_raspberries.loc[diet_formula_raspberries.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_formula_soybeans = diet_formula_soybeans.rename(columns={diet_formula_soybeans.columns[0]: "reaction"})
diet_formula_soybeans["metabolite"] = diet_formula_soybeans.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_formula_soybeans.loc[diet_formula_soybeans.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_formula_soybeans.loc[diet_formula_soybeans.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_formula_strawberries = diet_formula_strawberries.rename(columns={diet_formula_strawberries.columns[0]: "reaction"})
diet_formula_strawberries["metabolite"] = diet_formula_strawberries.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_formula_strawberries.loc[diet_formula_strawberries.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_formula_strawberries.loc[diet_formula_strawberries.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_formula_yellow_peas = diet_formula_yellow_peas.rename(columns={diet_formula_yellow_peas.columns[0]: "reaction"})
diet_formula_yellow_peas["metabolite"] = diet_formula_yellow_peas.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_formula_yellow_peas.loc[diet_formula_yellow_peas.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_formula_yellow_peas.loc[diet_formula_yellow_peas.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_black_beans_blackcurrants = diet_black_beans_blackcurrants.rename(columns={diet_black_beans_blackcurrants.columns[0]: "reaction"})
diet_black_beans_blackcurrants["metabolite"] = diet_black_beans_blackcurrants.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_black_beans_blackcurrants.loc[diet_black_beans_blackcurrants.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_black_beans_blackcurrants.loc[diet_black_beans_blackcurrants.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_black_beans_pumpkin = diet_black_beans_pumpkin.rename(columns={diet_black_beans_pumpkin.columns[0]: "reaction"})
diet_black_beans_pumpkin["metabolite"] = diet_black_beans_pumpkin.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_black_beans_pumpkin.loc[diet_black_beans_pumpkin.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_black_beans_pumpkin.loc[diet_black_beans_pumpkin.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_blackcurrants_kumara_with_skin = diet_blackcurrants_kumara_with_skin.rename(columns={diet_blackcurrants_kumara_with_skin.columns[0]: "reaction"})
diet_blackcurrants_kumara_with_skin["metabolite"] = diet_blackcurrants_kumara_with_skin.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_blackcurrants_kumara_with_skin.loc[diet_blackcurrants_kumara_with_skin.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_blackcurrants_kumara_with_skin.loc[diet_blackcurrants_kumara_with_skin.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_blackcurrants_kumara_without_skin = diet_blackcurrants_kumara_without_skin.rename(columns={diet_blackcurrants_kumara_without_skin.columns[0]: "reaction"})
diet_blackcurrants_kumara_without_skin["metabolite"] = diet_blackcurrants_kumara_without_skin.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_blackcurrants_kumara_without_skin.loc[diet_blackcurrants_kumara_without_skin.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_blackcurrants_kumara_without_skin.loc[diet_blackcurrants_kumara_without_skin.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_blackcurrants_pork = diet_blackcurrants_pork.rename(columns={diet_blackcurrants_pork.columns[0]: "reaction"})
diet_blackcurrants_pork["metabolite"] = diet_blackcurrants_pork.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_blackcurrants_pork.loc[diet_blackcurrants_pork.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_blackcurrants_pork.loc[diet_blackcurrants_pork.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_blackcurrants_soybeans = diet_blackcurrants_soybeans.rename(columns={diet_blackcurrants_soybeans.columns[0]: "reaction"})
diet_blackcurrants_soybeans["metabolite"] = diet_blackcurrants_soybeans.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_blackcurrants_soybeans.loc[diet_blackcurrants_soybeans.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_blackcurrants_soybeans.loc[diet_blackcurrants_soybeans.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_blackcurrants_strawberries = diet_blackcurrants_strawberries.rename(columns={diet_blackcurrants_strawberries.columns[0]: "reaction"})
diet_blackcurrants_strawberries["metabolite"] = diet_blackcurrants_strawberries.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_blackcurrants_strawberries.loc[diet_blackcurrants_strawberries.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_blackcurrants_strawberries.loc[diet_blackcurrants_strawberries.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_chickpeas_pork = diet_chickpeas_pork.rename(columns={diet_chickpeas_pork.columns[0]: "reaction"})
diet_chickpeas_pork["metabolite"] = diet_chickpeas_pork.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_chickpeas_pork.loc[diet_chickpeas_pork.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_chickpeas_pork.loc[diet_chickpeas_pork.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_chickpeas_yellow_peas = diet_chickpeas_yellow_peas.rename(columns={diet_chickpeas_yellow_peas.columns[0]: "reaction"})
diet_chickpeas_yellow_peas["metabolite"] = diet_chickpeas_yellow_peas.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_chickpeas_yellow_peas.loc[diet_chickpeas_yellow_peas.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_chickpeas_yellow_peas.loc[diet_chickpeas_yellow_peas.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_couscous_pork = diet_couscous_pork.rename(columns={diet_couscous_pork.columns[0]: "reaction"})
diet_couscous_pork["metabolite"] = diet_couscous_pork.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_couscous_pork.loc[diet_couscous_pork.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_couscous_pork.loc[diet_couscous_pork.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_couscous_pumpkin = diet_couscous_pumpkin.rename(columns={diet_couscous_pumpkin.columns[0]: "reaction"})
diet_couscous_pumpkin["metabolite"] = diet_couscous_pumpkin.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_couscous_pumpkin.loc[diet_couscous_pumpkin.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_couscous_pumpkin.loc[diet_couscous_pumpkin.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_pork_raspberries = diet_pork_raspberries.rename(columns={diet_pork_raspberries.columns[0]: "reaction"})
diet_pork_raspberries["metabolite"] = diet_pork_raspberries.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_pork_raspberries.loc[diet_pork_raspberries.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_pork_raspberries.loc[diet_pork_raspberries.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_pumpkin_yellow_peas = diet_pumpkin_yellow_peas.rename(columns={diet_pumpkin_yellow_peas.columns[0]: "reaction"})
diet_pumpkin_yellow_peas["metabolite"] = diet_pumpkin_yellow_peas.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_pumpkin_yellow_peas.loc[diet_pumpkin_yellow_peas.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_pumpkin_yellow_peas.loc[diet_pumpkin_yellow_peas.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_formula_black_beans_blackcurrants = diet_formula_black_beans_blackcurrants.rename(columns={diet_formula_black_beans_blackcurrants.columns[0]: "reaction"})
diet_formula_black_beans_blackcurrants["metabolite"] = diet_formula_black_beans_blackcurrants.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_formula_black_beans_blackcurrants.loc[diet_formula_black_beans_blackcurrants.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_formula_black_beans_blackcurrants.loc[diet_formula_black_beans_blackcurrants.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_formula_black_beans_pumpkin = diet_formula_black_beans_pumpkin.rename(columns={diet_formula_black_beans_pumpkin.columns[0]: "reaction"})
diet_formula_black_beans_pumpkin["metabolite"] = diet_formula_black_beans_pumpkin.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_formula_black_beans_pumpkin.loc[diet_formula_black_beans_pumpkin.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_formula_black_beans_pumpkin.loc[diet_formula_black_beans_pumpkin.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_formula_blackcurrants_kumara_with_skin = diet_formula_blackcurrants_kumara_with_skin.rename(columns={diet_formula_blackcurrants_kumara_with_skin.columns[0]: "reaction"})
diet_formula_blackcurrants_kumara_with_skin["metabolite"] = diet_formula_blackcurrants_kumara_with_skin.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_formula_blackcurrants_kumara_with_skin.loc[diet_formula_blackcurrants_kumara_with_skin.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_formula_blackcurrants_kumara_with_skin.loc[diet_formula_blackcurrants_kumara_with_skin.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_formula_blackcurrants_kumara_without_skin = diet_formula_blackcurrants_kumara_without_skin.rename(columns={diet_formula_blackcurrants_kumara_without_skin.columns[0]: "reaction"})
diet_formula_blackcurrants_kumara_without_skin["metabolite"] = diet_formula_blackcurrants_kumara_without_skin.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_formula_blackcurrants_kumara_without_skin.loc[diet_formula_blackcurrants_kumara_without_skin.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_formula_blackcurrants_kumara_without_skin.loc[diet_formula_blackcurrants_kumara_without_skin.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_formula_blackcurrants_pork = diet_formula_blackcurrants_pork.rename(columns={diet_formula_blackcurrants_pork.columns[0]: "reaction"})
diet_formula_blackcurrants_pork["metabolite"] = diet_formula_blackcurrants_pork.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_formula_blackcurrants_pork.loc[diet_formula_blackcurrants_pork.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_formula_blackcurrants_pork.loc[diet_formula_blackcurrants_pork.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_formula_blackcurrants_soybeans = diet_formula_blackcurrants_soybeans.rename(columns={diet_formula_blackcurrants_soybeans.columns[0]: "reaction"})
diet_formula_blackcurrants_soybeans["metabolite"] = diet_formula_blackcurrants_soybeans.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_formula_blackcurrants_soybeans.loc[diet_formula_blackcurrants_soybeans.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_formula_blackcurrants_soybeans.loc[diet_formula_blackcurrants_soybeans.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_formula_blackcurrants_strawberries = diet_formula_blackcurrants_strawberries.rename(columns={diet_formula_blackcurrants_strawberries.columns[0]: "reaction"})
diet_formula_blackcurrants_strawberries["metabolite"] = diet_formula_blackcurrants_strawberries.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_formula_blackcurrants_strawberries.loc[diet_formula_blackcurrants_strawberries.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_formula_blackcurrants_strawberries.loc[diet_formula_blackcurrants_strawberries.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_formula_chickpeas_pork = diet_formula_chickpeas_pork.rename(columns={diet_formula_chickpeas_pork.columns[0]: "reaction"})
diet_formula_chickpeas_pork["metabolite"] = diet_formula_chickpeas_pork.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_formula_chickpeas_pork.loc[diet_formula_chickpeas_pork.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_formula_chickpeas_pork.loc[diet_formula_chickpeas_pork.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_formula_chickpeas_yellow_peas = diet_formula_chickpeas_yellow_peas.rename(columns={diet_formula_chickpeas_yellow_peas.columns[0]: "reaction"})
diet_formula_chickpeas_yellow_peas["metabolite"] = diet_formula_chickpeas_yellow_peas.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_formula_chickpeas_yellow_peas.loc[diet_formula_chickpeas_yellow_peas.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_formula_chickpeas_yellow_peas.loc[diet_formula_chickpeas_yellow_peas.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_formula_couscous_pork = diet_formula_couscous_pork.rename(columns={diet_formula_couscous_pork.columns[0]: "reaction"})
diet_formula_couscous_pork["metabolite"] = diet_formula_couscous_pork.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_formula_couscous_pork.loc[diet_formula_couscous_pork.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_formula_couscous_pork.loc[diet_formula_couscous_pork.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_formula_couscous_pumpkin = diet_formula_couscous_pumpkin.rename(columns={diet_formula_couscous_pumpkin.columns[0]: "reaction"})
diet_formula_couscous_pumpkin["metabolite"] = diet_formula_couscous_pumpkin.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_formula_couscous_pumpkin.loc[diet_formula_couscous_pumpkin.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_formula_couscous_pumpkin.loc[diet_formula_couscous_pumpkin.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_formula_pork_raspberries = diet_formula_pork_raspberries.rename(columns={diet_formula_pork_raspberries.columns[0]: "reaction"})
diet_formula_pork_raspberries["metabolite"] = diet_formula_pork_raspberries.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_formula_pork_raspberries.loc[diet_formula_pork_raspberries.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_formula_pork_raspberries.loc[diet_formula_pork_raspberries.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_formula_pumpkin_yellow_peas = diet_formula_pumpkin_yellow_peas.rename(columns={diet_formula_pumpkin_yellow_peas.columns[0]: "reaction"})
diet_formula_pumpkin_yellow_peas["metabolite"] = diet_formula_pumpkin_yellow_peas.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_formula_pumpkin_yellow_peas.loc[diet_formula_pumpkin_yellow_peas.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_formula_pumpkin_yellow_peas.loc[diet_formula_pumpkin_yellow_peas.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0

from cobra.io import read_sbml_model
import pandas as pd

recon3 = read_sbml_model("data/Recon3D.xml.gz") #importing Recon3D model
exchanges = pd.Series([r.id for r in recon3.exchanges])
exchanges = exchanges.str.replace("__", "_").str.replace("_e$|EX_", "", regex=True) #list with the nutrients that are absrobed

diet_black_beans["dilution"] = 1.0
diet_black_beans.loc[diet_black_beans.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_black_beans["flux"] = diet_black_beans["flux"] * diet_black_beans["dilution"] #updaing the flux, considering the dilution
diet_black_beans[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_blackcurrants["dilution"] = 1.0
diet_blackcurrants.loc[diet_blackcurrants.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_blackcurrants["flux"] = diet_blackcurrants["flux"] * diet_blackcurrants["dilution"] #updaing the flux, considering the dilution
diet_blackcurrants[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_chickpeas["dilution"] = 1.0
diet_chickpeas.loc[diet_chickpeas.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_chickpeas["flux"] = diet_chickpeas["flux"] * diet_chickpeas["dilution"] #updaing the flux, considering the dilution
diet_chickpeas[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_couscous["dilution"] = 1.0
diet_couscous.loc[diet_couscous.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_couscous["flux"] = diet_couscous["flux"] * diet_couscous["dilution"] #updaing the flux, considering the dilution
diet_couscous[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_infant_formula["dilution"] = 1.0
diet_infant_formula.loc[diet_infant_formula.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_infant_formula["flux"] = diet_infant_formula["flux"] * diet_infant_formula["dilution"] #updaing the flux, considering the dilution
diet_infant_formula[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_kumara_with_skin["dilution"] = 1.0
diet_kumara_with_skin.loc[diet_kumara_with_skin.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_kumara_with_skin["flux"] = diet_kumara_with_skin["flux"] * diet_kumara_with_skin["dilution"] #updaing the flux, considering the dilution
diet_kumara_with_skin[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_kumara_without_skin["dilution"] = 1.0
diet_kumara_without_skin.loc[diet_kumara_without_skin.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_kumara_without_skin["flux"] = diet_kumara_without_skin["flux"] * diet_kumara_without_skin["dilution"] #updaing the flux, considering the dilution
diet_kumara_without_skin[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_pork["dilution"] = 1.0
diet_pork.loc[diet_pork.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_pork["flux"] = diet_pork["flux"] * diet_pork["dilution"] #updaing the flux, considering the dilution
diet_pork[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_prawn["dilution"] = 1.0
diet_prawn.loc[diet_prawn.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_prawn["flux"] = diet_prawn["flux"] * diet_prawn["dilution"] #updaing the flux, considering the dilution
diet_prawn[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_pumpkin["dilution"] = 1.0
diet_pumpkin.loc[diet_pumpkin.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_pumpkin["flux"] = diet_pumpkin["flux"] * diet_pumpkin["dilution"] #updaing the flux, considering the dilution
diet_pumpkin[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_raspberries["dilution"] = 1.0
diet_raspberries.loc[diet_raspberries.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_raspberries["flux"] = diet_raspberries["flux"] * diet_raspberries["dilution"] #updaing the flux, considering the dilution
diet_raspberries[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_soybeans["dilution"] = 1.0
diet_soybeans.loc[diet_soybeans.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_soybeans["flux"] = diet_soybeans["flux"] * diet_soybeans["dilution"] #updaing the flux, considering the dilution
diet_soybeans[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_strawberries["dilution"] = 1.0
diet_strawberries.loc[diet_strawberries.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_strawberries["flux"] = diet_strawberries["flux"] * diet_strawberries["dilution"] #updaing the flux, considering the dilution
diet_strawberries[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_yellow_peas["dilution"] = 1.0
diet_yellow_peas.loc[diet_yellow_peas.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_yellow_peas["flux"] = diet_yellow_peas["flux"] * diet_yellow_peas["dilution"] #updaing the flux, considering the dilution
diet_yellow_peas[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_formula_black_beans["dilution"] = 1.0
diet_formula_black_beans.loc[diet_formula_black_beans.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_formula_black_beans["flux"] = diet_formula_black_beans["flux"] * diet_formula_black_beans["dilution"] #updaing the flux, considering the dilution
diet_formula_black_beans[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_formula_blackcurrants["dilution"] = 1.0
diet_formula_blackcurrants.loc[diet_formula_blackcurrants.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_formula_blackcurrants["flux"] = diet_formula_blackcurrants["flux"] * diet_formula_blackcurrants["dilution"] #updaing the flux, considering the dilution
diet_formula_blackcurrants[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_formula_chickpeas["dilution"] = 1.0
diet_formula_chickpeas.loc[diet_formula_chickpeas.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_formula_chickpeas["flux"] = diet_formula_chickpeas["flux"] * diet_formula_chickpeas["dilution"] #updaing the flux, considering the dilution
diet_formula_chickpeas[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_formula_couscous["dilution"] = 1.0
diet_formula_couscous.loc[diet_formula_couscous.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_formula_couscous["flux"] = diet_formula_couscous["flux"] * diet_formula_couscous["dilution"] #updaing the flux, considering the dilution
diet_formula_couscous[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_formula_kumara_with_skin["dilution"] = 1.0
diet_formula_kumara_with_skin.loc[diet_formula_kumara_with_skin.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_formula_kumara_with_skin["flux"] = diet_formula_kumara_with_skin["flux"] * diet_formula_kumara_with_skin["dilution"] #updaing the flux, considering the dilution
diet_formula_kumara_with_skin[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_formula_kumara_without_skin["dilution"] = 1.0
diet_formula_kumara_without_skin.loc[diet_formula_kumara_without_skin.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_formula_kumara_without_skin["flux"] = diet_formula_kumara_without_skin["flux"] * diet_formula_kumara_without_skin["dilution"] #updaing the flux, considering the dilution
diet_formula_kumara_without_skin[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_formula_pork["dilution"] = 1.0
diet_formula_pork.loc[diet_formula_pork.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_formula_pork["flux"] = diet_formula_pork["flux"] * diet_formula_pork["dilution"] #updaing the flux, considering the dilution
diet_formula_pork[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_formula_prawn["dilution"] = 1.0
diet_formula_prawn.loc[diet_formula_prawn.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_formula_prawn["flux"] = diet_formula_prawn["flux"] * diet_formula_prawn["dilution"] #updaing the flux, considering the dilution
diet_formula_prawn[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_formula_pumpkin["dilution"] = 1.0
diet_formula_pumpkin.loc[diet_formula_pumpkin.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_formula_pumpkin["flux"] = diet_formula_pumpkin["flux"] * diet_formula_pumpkin["dilution"] #updaing the flux, considering the dilution
diet_formula_pumpkin[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_formula_raspberries["dilution"] = 1.0
diet_formula_raspberries.loc[diet_formula_raspberries.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_formula_raspberries["flux"] = diet_formula_raspberries["flux"] * diet_formula_raspberries["dilution"] #updaing the flux, considering the dilution
diet_formula_raspberries[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_formula_soybeans["dilution"] = 1.0
diet_formula_soybeans.loc[diet_formula_soybeans.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_formula_soybeans["flux"] = diet_formula_soybeans["flux"] * diet_formula_soybeans["dilution"] #updaing the flux, considering the dilution
diet_formula_soybeans[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_formula_strawberries["dilution"] = 1.0
diet_formula_strawberries.loc[diet_formula_strawberries.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_formula_strawberries["flux"] = diet_formula_strawberries["flux"] * diet_formula_strawberries["dilution"] #updaing the flux, considering the dilution
diet_formula_strawberries[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_formula_yellow_peas["dilution"] = 1.0
diet_formula_yellow_peas.loc[diet_formula_yellow_peas.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_formula_yellow_peas["flux"] = diet_formula_yellow_peas["flux"] * diet_formula_yellow_peas["dilution"] #updaing the flux, considering the dilution
diet_formula_yellow_peas[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_black_beans_blackcurrants["dilution"] = 1.0
diet_black_beans_blackcurrants.loc[diet_black_beans_blackcurrants.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_black_beans_blackcurrants["flux"] = diet_black_beans_blackcurrants["flux"] * diet_black_beans_blackcurrants["dilution"] #updaing the flux, considering the dilution
diet_black_beans_blackcurrants[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_black_beans_pumpkin["dilution"] = 1.0
diet_black_beans_pumpkin.loc[diet_black_beans_pumpkin.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_black_beans_pumpkin["flux"] = diet_black_beans_pumpkin["flux"] * diet_black_beans_pumpkin["dilution"] #updaing the flux, considering the dilution
diet_black_beans_pumpkin[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_blackcurrants_kumara_with_skin["dilution"] = 1.0
diet_blackcurrants_kumara_with_skin.loc[diet_blackcurrants_kumara_with_skin.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_blackcurrants_kumara_with_skin["flux"] = diet_blackcurrants_kumara_with_skin["flux"] * diet_blackcurrants_kumara_with_skin["dilution"] #updaing the flux, considering the dilution
diet_blackcurrants_kumara_with_skin[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_blackcurrants_kumara_without_skin["dilution"] = 1.0
diet_blackcurrants_kumara_without_skin.loc[diet_blackcurrants_kumara_without_skin.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_blackcurrants_kumara_without_skin["flux"] = diet_blackcurrants_kumara_without_skin["flux"] * diet_blackcurrants_kumara_without_skin["dilution"] #updaing the flux, considering the dilution
diet_blackcurrants_kumara_without_skin[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_blackcurrants_pork["dilution"] = 1.0
diet_blackcurrants_pork.loc[diet_blackcurrants_pork.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_blackcurrants_pork["flux"] = diet_blackcurrants_pork["flux"] * diet_blackcurrants_pork["dilution"] #updaing the flux, considering the dilution
diet_blackcurrants_pork[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_blackcurrants_soybeans["dilution"] = 1.0
diet_blackcurrants_soybeans.loc[diet_blackcurrants_soybeans.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_blackcurrants_soybeans["flux"] = diet_blackcurrants_soybeans["flux"] * diet_blackcurrants_soybeans["dilution"] #updaing the flux, considering the dilution
diet_blackcurrants_soybeans[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_blackcurrants_strawberries["dilution"] = 1.0
diet_blackcurrants_strawberries.loc[diet_blackcurrants_strawberries.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_blackcurrants_strawberries["flux"] = diet_blackcurrants_strawberries["flux"] * diet_blackcurrants_strawberries["dilution"] #updaing the flux, considering the dilution
diet_blackcurrants_strawberries[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_chickpeas_pork["dilution"] = 1.0
diet_chickpeas_pork.loc[diet_chickpeas_pork.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_chickpeas_pork["flux"] = diet_chickpeas_pork["flux"] * diet_chickpeas_pork["dilution"] #updaing the flux, considering the dilution
diet_chickpeas_pork[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_chickpeas_yellow_peas["dilution"] = 1.0
diet_chickpeas_yellow_peas.loc[diet_chickpeas_yellow_peas.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_chickpeas_yellow_peas["flux"] = diet_chickpeas_yellow_peas["flux"] * diet_chickpeas_yellow_peas["dilution"] #updaing the flux, considering the dilution
diet_chickpeas_yellow_peas[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_couscous_pork["dilution"] = 1.0
diet_couscous_pork.loc[diet_couscous_pork.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_couscous_pork["flux"] = diet_couscous_pork["flux"] * diet_couscous_pork["dilution"] #updaing the flux, considering the dilution
diet_couscous_pork[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_couscous_pumpkin["dilution"] = 1.0
diet_couscous_pumpkin.loc[diet_couscous_pumpkin.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_couscous_pumpkin["flux"] = diet_couscous_pumpkin["flux"] * diet_couscous_pumpkin["dilution"] #updaing the flux, considering the dilution
diet_couscous_pumpkin[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_pork_raspberries["dilution"] = 1.0
diet_pork_raspberries.loc[diet_pork_raspberries.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_pork_raspberries["flux"] = diet_pork_raspberries["flux"] * diet_pork_raspberries["dilution"] #updaing the flux, considering the dilution
diet_pork_raspberries[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_pumpkin_yellow_peas["dilution"] = 1.0
diet_pumpkin_yellow_peas.loc[diet_pumpkin_yellow_peas.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_pumpkin_yellow_peas["flux"] = diet_pumpkin_yellow_peas["flux"] * diet_pumpkin_yellow_peas["dilution"] #updaing the flux, considering the dilution
diet_pumpkin_yellow_peas[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_formula_black_beans_blackcurrants["dilution"] = 1.0
diet_formula_black_beans_blackcurrants.loc[diet_formula_black_beans_blackcurrants.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_formula_black_beans_blackcurrants["flux"] = diet_formula_black_beans_blackcurrants["flux"] * diet_formula_black_beans_blackcurrants["dilution"] #updaing the flux, considering the dilution
diet_formula_black_beans_blackcurrants[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_formula_black_beans_pumpkin["dilution"] = 1.0
diet_formula_black_beans_pumpkin.loc[diet_formula_black_beans_pumpkin.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_formula_black_beans_pumpkin["flux"] = diet_formula_black_beans_pumpkin["flux"] * diet_formula_black_beans_pumpkin["dilution"] #updaing the flux, considering the dilution
diet_formula_black_beans_pumpkin[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_formula_blackcurrants_kumara_with_skin["dilution"] = 1.0
diet_formula_blackcurrants_kumara_with_skin.loc[diet_formula_blackcurrants_kumara_with_skin.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_formula_blackcurrants_kumara_with_skin["flux"] = diet_formula_blackcurrants_kumara_with_skin["flux"] * diet_formula_blackcurrants_kumara_with_skin["dilution"] #updaing the flux, considering the dilution
diet_formula_blackcurrants_kumara_with_skin[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_formula_blackcurrants_kumara_without_skin["dilution"] = 1.0
diet_formula_blackcurrants_kumara_without_skin.loc[diet_formula_blackcurrants_kumara_without_skin.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_formula_blackcurrants_kumara_without_skin["flux"] = diet_formula_blackcurrants_kumara_without_skin["flux"] * diet_formula_blackcurrants_kumara_without_skin["dilution"] #updaing the flux, considering the dilution
diet_formula_blackcurrants_kumara_without_skin[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_formula_blackcurrants_pork["dilution"] = 1.0
diet_formula_blackcurrants_pork.loc[diet_formula_blackcurrants_pork.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_formula_blackcurrants_pork["flux"] = diet_formula_blackcurrants_pork["flux"] * diet_formula_blackcurrants_pork["dilution"] #updaing the flux, considering the dilution
diet_formula_blackcurrants_pork[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_formula_blackcurrants_soybeans["dilution"] = 1.0
diet_formula_blackcurrants_soybeans.loc[diet_formula_blackcurrants_soybeans.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_formula_blackcurrants_soybeans["flux"] = diet_formula_blackcurrants_soybeans["flux"] * diet_formula_blackcurrants_soybeans["dilution"] #updaing the flux, considering the dilution
diet_formula_blackcurrants_soybeans[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_formula_blackcurrants_strawberries["dilution"] = 1.0
diet_formula_blackcurrants_strawberries.loc[diet_formula_blackcurrants_strawberries.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_formula_blackcurrants_strawberries["flux"] = diet_formula_blackcurrants_strawberries["flux"] * diet_formula_blackcurrants_strawberries["dilution"] #updaing the flux, considering the dilution
diet_formula_blackcurrants_strawberries[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_formula_chickpeas_pork["dilution"] = 1.0
diet_formula_chickpeas_pork.loc[diet_formula_chickpeas_pork.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_formula_chickpeas_pork["flux"] = diet_formula_chickpeas_pork["flux"] * diet_formula_chickpeas_pork["dilution"] #updaing the flux, considering the dilution
diet_formula_chickpeas_pork[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_formula_chickpeas_yellow_peas["dilution"] = 1.0
diet_formula_chickpeas_yellow_peas.loc[diet_formula_chickpeas_yellow_peas.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_formula_chickpeas_yellow_peas["flux"] = diet_formula_chickpeas_yellow_peas["flux"] * diet_formula_chickpeas_yellow_peas["dilution"] #updaing the flux, considering the dilution
diet_formula_chickpeas_yellow_peas[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_formula_couscous_pork["dilution"] = 1.0
diet_formula_couscous_pork.loc[diet_formula_couscous_pork.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_formula_couscous_pork["flux"] = diet_formula_couscous_pork["flux"] * diet_formula_couscous_pork["dilution"] #updaing the flux, considering the dilution
diet_formula_couscous_pork[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_formula_couscous_pumpkin["dilution"] = 1.0
diet_formula_couscous_pumpkin.loc[diet_formula_couscous_pumpkin.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_formula_couscous_pumpkin["flux"] = diet_formula_couscous_pumpkin["flux"] * diet_formula_couscous_pumpkin["dilution"] #updaing the flux, considering the dilution
diet_formula_couscous_pumpkin[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_formula_pork_raspberries["dilution"] = 1.0
diet_formula_pork_raspberries.loc[diet_formula_pork_raspberries.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_formula_pork_raspberries["flux"] = diet_formula_pork_raspberries["flux"] * diet_formula_pork_raspberries["dilution"] #updaing the flux, considering the dilution
diet_formula_pork_raspberries[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_formula_pumpkin_yellow_peas["dilution"] = 1.0
diet_formula_pumpkin_yellow_peas.loc[diet_formula_pumpkin_yellow_peas.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_formula_pumpkin_yellow_peas["flux"] = diet_formula_pumpkin_yellow_peas["flux"] * diet_formula_pumpkin_yellow_peas["dilution"] #updaing the flux, considering the dilution
diet_formula_pumpkin_yellow_peas[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()

#Adding host secreted substrates
#we consider the flux of these compounds as 1 mmol/h

diet_black_beans.set_index("metabolite", inplace=True)
diet_blackcurrants.set_index("metabolite", inplace=True)
diet_chickpeas.set_index("metabolite", inplace=True)
diet_couscous.set_index("metabolite", inplace=True)
diet_infant_formula.set_index("metabolite", inplace=True)
diet_kumara_with_skin.set_index("metabolite", inplace=True)
diet_kumara_without_skin.set_index("metabolite", inplace=True)
diet_pork.set_index("metabolite", inplace=True)
diet_prawn.set_index("metabolite", inplace=True)
diet_pumpkin.set_index("metabolite", inplace=True)
diet_raspberries.set_index("metabolite", inplace=True)
diet_soybeans.set_index("metabolite", inplace=True)
diet_strawberries.set_index("metabolite", inplace=True)
diet_yellow_peas.set_index("metabolite", inplace=True)
diet_formula_black_beans.set_index("metabolite", inplace=True)
diet_formula_blackcurrants.set_index("metabolite", inplace=True)
diet_formula_chickpeas.set_index("metabolite", inplace=True)
diet_formula_couscous.set_index("metabolite", inplace=True)
diet_formula_kumara_with_skin.set_index("metabolite", inplace=True)
diet_formula_kumara_without_skin.set_index("metabolite", inplace=True)
diet_formula_pork.set_index("metabolite", inplace=True)
diet_formula_prawn.set_index("metabolite", inplace=True)
diet_formula_pumpkin.set_index("metabolite", inplace=True)
diet_formula_raspberries.set_index("metabolite", inplace=True)
diet_formula_soybeans.set_index("metabolite", inplace=True)
diet_formula_strawberries.set_index("metabolite", inplace=True)
diet_formula_yellow_peas.set_index("metabolite", inplace=True)
diet_black_beans_blackcurrants.set_index("metabolite", inplace=True)
diet_black_beans_pumpkin.set_index("metabolite", inplace=True)
diet_blackcurrants_kumara_with_skin.set_index("metabolite", inplace=True)
diet_blackcurrants_kumara_without_skin.set_index("metabolite", inplace=True)
diet_blackcurrants_pork.set_index("metabolite", inplace=True)
diet_blackcurrants_soybeans.set_index("metabolite", inplace=True)
diet_blackcurrants_strawberries.set_index("metabolite", inplace=True)
diet_chickpeas_pork.set_index("metabolite", inplace=True)
diet_chickpeas_yellow_peas.set_index("metabolite", inplace=True)
diet_couscous_pork.set_index("metabolite", inplace=True)
diet_couscous_pumpkin.set_index("metabolite", inplace=True)
diet_pork_raspberries.set_index("metabolite", inplace=True)
diet_pumpkin_yellow_peas.set_index("metabolite", inplace=True)
diet_formula_black_beans_blackcurrants.set_index("metabolite", inplace=True)
diet_formula_black_beans_pumpkin.set_index("metabolite", inplace=True)
diet_formula_blackcurrants_kumara_with_skin.set_index("metabolite", inplace=True)
diet_formula_blackcurrants_kumara_without_skin.set_index("metabolite", inplace=True)
diet_formula_blackcurrants_pork.set_index("metabolite", inplace=True)
diet_formula_blackcurrants_soybeans.set_index("metabolite", inplace=True)
diet_formula_blackcurrants_strawberries.set_index("metabolite", inplace=True)
diet_formula_chickpeas_pork.set_index("metabolite", inplace=True)
diet_formula_chickpeas_yellow_peas.set_index("metabolite", inplace=True)
diet_formula_couscous_pork.set_index("metabolite", inplace=True)
diet_formula_couscous_pumpkin.set_index("metabolite", inplace=True)
diet_formula_pork_raspberries.set_index("metabolite", inplace=True)
diet_formula_pumpkin_yellow_peas.set_index("metabolite", inplace=True)

for met in annotations.loc[annotations.metabolite.str.contains("core"), "metabolite"]: # mucins
    diet_black_beans.loc[met, "flux"] = 1
    diet_blackcurrants.loc[met, "flux"] = 1
    diet_chickpeas.loc[met, "flux"] = 1
    diet_couscous.loc[met, "flux"] = 1
    diet_infant_formula.loc[met, "flux"] = 1
    diet_kumara_with_skin.loc[met, "flux"] = 1
    diet_kumara_without_skin.loc[met, "flux"] = 1
    diet_pork.loc[met, "flux"] = 1
    diet_prawn.loc[met, "flux"] = 1
    diet_pumpkin.loc[met, "flux"] = 1
    diet_raspberries.loc[met, "flux"] = 1
    diet_soybeans.loc[met, "flux"] = 1
    diet_strawberries.loc[met, "flux"] = 1
    diet_yellow_peas.loc[met, "flux"] = 1
    diet_formula_black_beans.loc[met, "flux"] = 1
    diet_formula_blackcurrants.loc[met, "flux"] = 1
    diet_formula_chickpeas.loc[met, "flux"] = 1
    diet_formula_couscous.loc[met, "flux"] = 1
    diet_formula_kumara_with_skin.loc[met, "flux"] = 1
    diet_formula_kumara_without_skin.loc[met, "flux"] = 1
    diet_formula_pork.loc[met, "flux"] = 1
    diet_formula_prawn.loc[met, "flux"] = 1
    diet_formula_pumpkin.loc[met, "flux"] = 1
    diet_formula_raspberries.loc[met, "flux"] = 1
    diet_formula_soybeans.loc[met, "flux"] = 1
    diet_formula_strawberries.loc[met, "flux"] = 1
    diet_formula_yellow_peas.loc[met, "flux"] = 1
    diet_black_beans_blackcurrants.loc[met, "flux"] = 1
    diet_black_beans_pumpkin.loc[met, "flux"] = 1
    diet_blackcurrants_kumara_with_skin.loc[met, "flux"] = 1
    diet_blackcurrants_kumara_without_skin.loc[met, "flux"] = 1
    diet_blackcurrants_pork.loc[met, "flux"] = 1
    diet_blackcurrants_soybeans.loc[met, "flux"] = 1
    diet_blackcurrants_strawberries.loc[met, "flux"] = 1
    diet_chickpeas_pork.loc[met, "flux"] = 1
    diet_chickpeas_yellow_peas.loc[met, "flux"] = 1
    diet_couscous_pork.loc[met, "flux"] = 1
    diet_couscous_pumpkin.loc[met, "flux"] = 1
    diet_pork_raspberries.loc[met, "flux"] = 1
    diet_pumpkin_yellow_peas.loc[met, "flux"] = 1
    diet_formula_black_beans_blackcurrants.loc[met, "flux"] = 1
    diet_formula_black_beans_pumpkin.loc[met, "flux"] = 1
    diet_formula_blackcurrants_kumara_with_skin.loc[met, "flux"] = 1
    diet_formula_blackcurrants_kumara_without_skin.loc[met, "flux"] = 1
    diet_formula_blackcurrants_pork.loc[met, "flux"] = 1
    diet_formula_blackcurrants_soybeans.loc[met, "flux"] = 1
    diet_formula_blackcurrants_strawberries.loc[met, "flux"] = 1
    diet_formula_chickpeas_pork.loc[met, "flux"] = 1
    diet_formula_chickpeas_yellow_peas.loc[met, "flux"] = 1
    diet_formula_couscous_pork.loc[met, "flux"] = 1
    diet_formula_couscous_pumpkin.loc[met, "flux"] = 1
    diet_formula_pork_raspberries.loc[met, "flux"] = 1
    diet_formula_pumpkin_yellow_peas.loc[met, "flux"] = 1
    
for met in ["gchola", "tchola"]: # primary BAs
    diet_black_beans.loc[met, "flux"] = 1
    diet_blackcurrants.loc[met, "flux"] = 1
    diet_chickpeas.loc[met, "flux"] = 1
    diet_couscous.loc[met, "flux"] = 1
    diet_infant_formula.loc[met, "flux"] = 1
    diet_kumara_with_skin.loc[met, "flux"] = 1
    diet_kumara_without_skin.loc[met, "flux"] = 1
    diet_pork.loc[met, "flux"] = 1
    diet_prawn.loc[met, "flux"] = 1
    diet_pumpkin.loc[met, "flux"] = 1
    diet_raspberries.loc[met, "flux"] = 1
    diet_soybeans.loc[met, "flux"] = 1
    diet_strawberries.loc[met, "flux"] = 1
    diet_yellow_peas.loc[met, "flux"] = 1
    diet_formula_black_beans.loc[met, "flux"] = 1
    diet_formula_blackcurrants.loc[met, "flux"] = 1
    diet_formula_chickpeas.loc[met, "flux"] = 1
    diet_formula_couscous.loc[met, "flux"] = 1
    diet_formula_kumara_with_skin.loc[met, "flux"] = 1
    diet_formula_kumara_without_skin.loc[met, "flux"] = 1
    diet_formula_pork.loc[met, "flux"] = 1
    diet_formula_prawn.loc[met, "flux"] = 1
    diet_formula_pumpkin.loc[met, "flux"] = 1
    diet_formula_raspberries.loc[met, "flux"] = 1
    diet_formula_soybeans.loc[met, "flux"] = 1
    diet_formula_strawberries.loc[met, "flux"] = 1
    diet_formula_yellow_peas.loc[met, "flux"] = 1
    diet_black_beans_blackcurrants.loc[met, "flux"] = 1
    diet_black_beans_pumpkin.loc[met, "flux"] = 1
    diet_blackcurrants_kumara_with_skin.loc[met, "flux"] = 1
    diet_blackcurrants_kumara_without_skin.loc[met, "flux"] = 1
    diet_blackcurrants_pork.loc[met, "flux"] = 1
    diet_blackcurrants_soybeans.loc[met, "flux"] = 1
    diet_blackcurrants_strawberries.loc[met, "flux"] = 1
    diet_chickpeas_pork.loc[met, "flux"] = 1
    diet_chickpeas_yellow_peas.loc[met, "flux"] = 1
    diet_couscous_pork.loc[met, "flux"] = 1
    diet_couscous_pumpkin.loc[met, "flux"] = 1
    diet_pork_raspberries.loc[met, "flux"] = 1
    diet_pumpkin_yellow_peas.loc[met, "flux"] = 1
    diet_formula_black_beans_blackcurrants.loc[met, "flux"] = 1
    diet_formula_black_beans_pumpkin.loc[met, "flux"] = 1
    diet_formula_blackcurrants_kumara_with_skin.loc[met, "flux"] = 1
    diet_formula_blackcurrants_kumara_without_skin.loc[met, "flux"] = 1
    diet_formula_blackcurrants_pork.loc[met, "flux"] = 1
    diet_formula_blackcurrants_soybeans.loc[met, "flux"] = 1
    diet_formula_blackcurrants_strawberries.loc[met, "flux"] = 1
    diet_formula_chickpeas_pork.loc[met, "flux"] = 1
    diet_formula_chickpeas_yellow_peas.loc[met, "flux"] = 1
    diet_formula_couscous_pork.loc[met, "flux"] = 1
    diet_formula_couscous_pumpkin.loc[met, "flux"] = 1
    diet_formula_pork_raspberries.loc[met, "flux"] = 1
    diet_formula_pumpkin_yellow_peas.loc[met, "flux"] = 1
    
diet_black_beans.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_blackcurrants.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_chickpeas.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_couscous.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_infant_formula.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_kumara_with_skin.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_kumara_without_skin.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_pork.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_prawn.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_pumpkin.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_raspberries.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_soybeans.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_strawberries.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_yellow_peas.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_formula_black_beans.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_formula_blackcurrants.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_formula_chickpeas.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_formula_couscous.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_formula_kumara_with_skin.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_formula_kumara_without_skin.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_formula_pork.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_formula_prawn.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_formula_pumpkin.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_formula_raspberries.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_formula_soybeans.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_formula_strawberries.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_formula_yellow_peas.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_black_beans_blackcurrants.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_black_beans_pumpkin.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_blackcurrants_kumara_with_skin.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_blackcurrants_kumara_without_skin.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_blackcurrants_pork.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_blackcurrants_soybeans.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_blackcurrants_strawberries.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_chickpeas_pork.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_chickpeas_yellow_peas.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_couscous_pork.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_couscous_pumpkin.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_pork_raspberries.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_pumpkin_yellow_peas.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_formula_black_beans_blackcurrants.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_formula_black_beans_pumpkin.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_formula_blackcurrants_kumara_with_skin.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_formula_blackcurrants_kumara_without_skin.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_formula_blackcurrants_pork.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_formula_blackcurrants_soybeans.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_formula_blackcurrants_strawberries.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_formula_chickpeas_pork.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_formula_chickpeas_yellow_peas.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_formula_couscous_pork.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_formula_couscous_pumpkin.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_formula_pork_raspberries.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_formula_pumpkin_yellow_peas.loc["o2", "flux"] = 0.001 # anaerobic environment

diet_black_beans.reset_index(inplace=True)
diet_black_beans["reaction"] = "EX_" + diet_black_beans.metabolite + "(e)"
diet_blackcurrants.reset_index(inplace=True)
diet_blackcurrants["reaction"] = "EX_" + diet_blackcurrants.metabolite + "(e)"
diet_chickpeas.reset_index(inplace=True)
diet_chickpeas["reaction"] = "EX_" + diet_chickpeas.metabolite + "(e)"
diet_couscous.reset_index(inplace=True)
diet_couscous["reaction"] = "EX_" + diet_couscous.metabolite + "(e)"
diet_infant_formula.reset_index(inplace=True)
diet_infant_formula["reaction"] = "EX_" + diet_infant_formula.metabolite + "(e)"
diet_kumara_with_skin.reset_index(inplace=True)
diet_kumara_with_skin["reaction"] = "EX_" + diet_kumara_with_skin.metabolite + "(e)"
diet_kumara_without_skin.reset_index(inplace=True)
diet_kumara_without_skin["reaction"] = "EX_" + diet_kumara_without_skin.metabolite + "(e)"
diet_pork.reset_index(inplace=True)
diet_pork["reaction"] = "EX_" + diet_pork.metabolite + "(e)"
diet_prawn.reset_index(inplace=True)
diet_prawn["reaction"] = "EX_" + diet_prawn.metabolite + "(e)"
diet_pumpkin.reset_index(inplace=True)
diet_pumpkin["reaction"] = "EX_" + diet_pumpkin.metabolite + "(e)"
diet_raspberries.reset_index(inplace=True)
diet_raspberries["reaction"] = "EX_" + diet_raspberries.metabolite + "(e)"
diet_soybeans.reset_index(inplace=True)
diet_soybeans["reaction"] = "EX_" + diet_soybeans.metabolite + "(e)"
diet_strawberries.reset_index(inplace=True)
diet_strawberries["reaction"] = "EX_" + diet_strawberries.metabolite + "(e)"
diet_yellow_peas.reset_index(inplace=True)
diet_yellow_peas["reaction"] = "EX_" + diet_yellow_peas.metabolite + "(e)"
diet_formula_black_beans.reset_index(inplace=True)
diet_formula_black_beans["reaction"] = "EX_" + diet_formula_black_beans.metabolite + "(e)"
diet_formula_blackcurrants.reset_index(inplace=True)
diet_formula_blackcurrants["reaction"] = "EX_" + diet_formula_blackcurrants.metabolite + "(e)"
diet_formula_chickpeas.reset_index(inplace=True)
diet_formula_chickpeas["reaction"] = "EX_" + diet_formula_chickpeas.metabolite + "(e)"
diet_formula_couscous.reset_index(inplace=True)
diet_formula_couscous["reaction"] = "EX_" + diet_formula_couscous.metabolite + "(e)"
diet_formula_kumara_with_skin.reset_index(inplace=True)
diet_formula_kumara_with_skin["reaction"] = "EX_" + diet_formula_kumara_with_skin.metabolite + "(e)"
diet_formula_kumara_without_skin.reset_index(inplace=True)
diet_formula_kumara_without_skin["reaction"] = "EX_" + diet_formula_kumara_without_skin.metabolite + "(e)"
diet_formula_pork.reset_index(inplace=True)
diet_formula_pork["reaction"] = "EX_" + diet_formula_pork.metabolite + "(e)"
diet_formula_prawn.reset_index(inplace=True)
diet_formula_prawn["reaction"] = "EX_" + diet_formula_prawn.metabolite + "(e)"
diet_formula_pumpkin.reset_index(inplace=True)
diet_formula_pumpkin["reaction"] = "EX_" + diet_formula_pumpkin.metabolite + "(e)"
diet_formula_raspberries.reset_index(inplace=True)
diet_formula_raspberries["reaction"] = "EX_" + diet_formula_raspberries.metabolite + "(e)"
diet_formula_soybeans.reset_index(inplace=True)
diet_formula_soybeans["reaction"] = "EX_" + diet_formula_soybeans.metabolite + "(e)"
diet_formula_strawberries.reset_index(inplace=True)
diet_formula_strawberries["reaction"] = "EX_" + diet_formula_strawberries.metabolite + "(e)"
diet_formula_yellow_peas.reset_index(inplace=True)
diet_formula_yellow_peas["reaction"] = "EX_" + diet_formula_yellow_peas.metabolite + "(e)"
diet_black_beans_blackcurrants.reset_index(inplace=True)
diet_black_beans_blackcurrants["reaction"] = "EX_" + diet_black_beans_blackcurrants.metabolite + "(e)"
diet_black_beans_pumpkin.reset_index(inplace=True)
diet_black_beans_pumpkin["reaction"] = "EX_" + diet_black_beans_pumpkin.metabolite + "(e)"
diet_blackcurrants_kumara_with_skin.reset_index(inplace=True)
diet_blackcurrants_kumara_with_skin["reaction"] = "EX_" + diet_blackcurrants_kumara_with_skin.metabolite + "(e)"
diet_blackcurrants_kumara_without_skin.reset_index(inplace=True)
diet_blackcurrants_kumara_without_skin["reaction"] = "EX_" + diet_blackcurrants_kumara_without_skin.metabolite + "(e)"
diet_blackcurrants_pork.reset_index(inplace=True)
diet_blackcurrants_pork["reaction"] = "EX_" + diet_blackcurrants_pork.metabolite + "(e)"
diet_blackcurrants_soybeans.reset_index(inplace=True)
diet_blackcurrants_soybeans["reaction"] = "EX_" + diet_blackcurrants_soybeans.metabolite + "(e)"
diet_blackcurrants_strawberries.reset_index(inplace=True)
diet_blackcurrants_strawberries["reaction"] = "EX_" + diet_blackcurrants_strawberries.metabolite + "(e)"
diet_chickpeas_pork.reset_index(inplace=True)
diet_chickpeas_pork["reaction"] = "EX_" + diet_chickpeas_pork.metabolite + "(e)"
diet_chickpeas_yellow_peas.reset_index(inplace=True)
diet_chickpeas_yellow_peas["reaction"] = "EX_" + diet_chickpeas_yellow_peas.metabolite + "(e)"
diet_couscous_pork.reset_index(inplace=True)
diet_couscous_pork["reaction"] = "EX_" + diet_couscous_pork.metabolite + "(e)"
diet_couscous_pumpkin.reset_index(inplace=True)
diet_couscous_pumpkin["reaction"] = "EX_" + diet_couscous_pumpkin.metabolite + "(e)"
diet_pork_raspberries.reset_index(inplace=True)
diet_pork_raspberries["reaction"] = "EX_" + diet_pork_raspberries.metabolite + "(e)"
diet_pumpkin_yellow_peas.reset_index(inplace=True)
diet_pumpkin_yellow_peas["reaction"] = "EX_" + diet_pumpkin_yellow_peas.metabolite + "(e)"
diet_formula_black_beans_blackcurrants.reset_index(inplace=True)
diet_formula_black_beans_blackcurrants["reaction"] = "EX_" + diet_formula_black_beans_blackcurrants.metabolite + "(e)"
diet_formula_black_beans_pumpkin.reset_index(inplace=True)
diet_formula_black_beans_pumpkin["reaction"] = "EX_" + diet_formula_black_beans_pumpkin.metabolite + "(e)"
diet_formula_blackcurrants_kumara_with_skin.reset_index(inplace=True)
diet_formula_blackcurrants_kumara_with_skin["reaction"] = "EX_" + diet_formula_blackcurrants_kumara_with_skin.metabolite + "(e)"
diet_formula_blackcurrants_kumara_without_skin.reset_index(inplace=True)
diet_formula_blackcurrants_kumara_without_skin["reaction"] = "EX_" + diet_formula_blackcurrants_kumara_without_skin.metabolite + "(e)"
diet_formula_blackcurrants_pork.reset_index(inplace=True)
diet_formula_blackcurrants_pork["reaction"] = "EX_" + diet_formula_blackcurrants_pork.metabolite + "(e)"
diet_formula_blackcurrants_soybeans.reset_index(inplace=True)
diet_formula_blackcurrants_soybeans["reaction"] = "EX_" + diet_formula_blackcurrants_soybeans.metabolite + "(e)"
diet_formula_blackcurrants_strawberries.reset_index(inplace=True)
diet_formula_blackcurrants_strawberries["reaction"] = "EX_" + diet_formula_blackcurrants_strawberries.metabolite + "(e)"
diet_formula_chickpeas_pork.reset_index(inplace=True)
diet_formula_chickpeas_pork["reaction"] = "EX_" + diet_formula_chickpeas_pork.metabolite + "(e)"
diet_formula_chickpeas_yellow_peas.reset_index(inplace=True)
diet_formula_chickpeas_yellow_peas["reaction"] = "EX_" + diet_formula_chickpeas_yellow_peas.metabolite + "(e)"
diet_formula_couscous_pork.reset_index(inplace=True)
diet_formula_couscous_pork["reaction"] = "EX_" + diet_formula_couscous_pork.metabolite + "(e)"
diet_formula_couscous_pumpkin.reset_index(inplace=True)
diet_formula_couscous_pumpkin["reaction"] = "EX_" + diet_formula_couscous_pumpkin.metabolite + "(e)"
diet_formula_pork_raspberries.reset_index(inplace=True)
diet_formula_pork_raspberries["reaction"] = "EX_" + diet_formula_pork_raspberries.metabolite + "(e)"
diet_formula_pumpkin_yellow_peas.reset_index(inplace=True)
diet_formula_pumpkin_yellow_peas["reaction"] = "EX_" + diet_formula_pumpkin_yellow_peas.metabolite + "(e)"

#Adding information in our diet table
skeleton_black_beans = pd.merge(diet_black_beans, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_black_beans["global_id"] = skeleton_black_beans.reaction
skeleton_black_beans["reaction"] = "EX_" + skeleton_black_beans.metabolite + "_m"
skeleton_blackcurrants = pd.merge(diet_blackcurrants, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_blackcurrants["global_id"] = skeleton_blackcurrants.reaction
skeleton_blackcurrants["reaction"] = "EX_" + skeleton_blackcurrants.metabolite + "_m"
skeleton_chickpeas = pd.merge(diet_chickpeas, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_chickpeas["global_id"] = skeleton_chickpeas.reaction
skeleton_chickpeas["reaction"] = "EX_" + skeleton_chickpeas.metabolite + "_m"
skeleton_couscous = pd.merge(diet_couscous, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_couscous["global_id"] = skeleton_couscous.reaction
skeleton_couscous["reaction"] = "EX_" + skeleton_couscous.metabolite + "_m"
skeleton_infant_formula = pd.merge(diet_infant_formula, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_infant_formula["global_id"] = skeleton_infant_formula.reaction
skeleton_infant_formula["reaction"] = "EX_" + skeleton_infant_formula.metabolite + "_m"
skeleton_kumara_with_skin = pd.merge(diet_kumara_with_skin, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_kumara_with_skin["global_id"] = skeleton_kumara_with_skin.reaction
skeleton_kumara_with_skin["reaction"] = "EX_" + skeleton_kumara_with_skin.metabolite + "_m"
skeleton_kumara_without_skin = pd.merge(diet_kumara_without_skin, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_kumara_without_skin["global_id"] = skeleton_kumara_without_skin.reaction
skeleton_kumara_without_skin["reaction"] = "EX_" + skeleton_kumara_without_skin.metabolite + "_m"
skeleton_pork = pd.merge(diet_pork, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_pork["global_id"] = skeleton_pork.reaction
skeleton_pork["reaction"] = "EX_" + skeleton_pork.metabolite + "_m"
skeleton_prawn = pd.merge(diet_prawn, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_prawn["global_id"] = skeleton_prawn.reaction
skeleton_prawn["reaction"] = "EX_" + skeleton_prawn.metabolite + "_m"
skeleton_pumpkin = pd.merge(diet_pumpkin, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_pumpkin["global_id"] = skeleton_pumpkin.reaction
skeleton_pumpkin["reaction"] = "EX_" + skeleton_pumpkin.metabolite + "_m"
skeleton_raspberries = pd.merge(diet_raspberries, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_raspberries["global_id"] = skeleton_raspberries.reaction
skeleton_raspberries["reaction"] = "EX_" + skeleton_raspberries.metabolite + "_m"
skeleton_soybeans = pd.merge(diet_soybeans, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_soybeans["global_id"] = skeleton_soybeans.reaction
skeleton_soybeans["reaction"] = "EX_" + skeleton_soybeans.metabolite + "_m"
skeleton_strawberries = pd.merge(diet_strawberries, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_strawberries["global_id"] = skeleton_strawberries.reaction
skeleton_strawberries["reaction"] = "EX_" + skeleton_strawberries.metabolite + "_m"
skeleton_yellow_peas = pd.merge(diet_yellow_peas, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_yellow_peas["global_id"] = skeleton_yellow_peas.reaction
skeleton_yellow_peas["reaction"] = "EX_" + skeleton_yellow_peas.metabolite + "_m"
skeleton_formula_black_beans = pd.merge(diet_formula_black_beans, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_formula_black_beans["global_id"] = skeleton_formula_black_beans.reaction
skeleton_formula_black_beans["reaction"] = "EX_" + skeleton_formula_black_beans.metabolite + "_m"
skeleton_formula_blackcurrants = pd.merge(diet_formula_blackcurrants, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_formula_blackcurrants["global_id"] = skeleton_formula_blackcurrants.reaction
skeleton_formula_blackcurrants["reaction"] = "EX_" + skeleton_formula_blackcurrants.metabolite + "_m"
skeleton_formula_chickpeas = pd.merge(diet_formula_chickpeas, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_formula_chickpeas["global_id"] = skeleton_formula_chickpeas.reaction
skeleton_formula_chickpeas["reaction"] = "EX_" + skeleton_formula_chickpeas.metabolite + "_m"
skeleton_formula_couscous = pd.merge(diet_formula_couscous, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_formula_couscous["global_id"] = skeleton_formula_couscous.reaction
skeleton_formula_couscous["reaction"] = "EX_" + skeleton_formula_couscous.metabolite + "_m"
skeleton_formula_kumara_with_skin = pd.merge(diet_formula_kumara_with_skin, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_formula_kumara_with_skin["global_id"] = skeleton_formula_kumara_with_skin.reaction
skeleton_formula_kumara_with_skin["reaction"] = "EX_" + skeleton_formula_kumara_with_skin.metabolite + "_m"
skeleton_formula_kumara_without_skin = pd.merge(diet_formula_kumara_without_skin, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_formula_kumara_without_skin["global_id"] = skeleton_formula_kumara_without_skin.reaction
skeleton_formula_kumara_without_skin["reaction"] = "EX_" + skeleton_formula_kumara_without_skin.metabolite + "_m"
skeleton_formula_pork = pd.merge(diet_formula_pork, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_formula_pork["global_id"] = skeleton_formula_pork.reaction
skeleton_formula_pork["reaction"] = "EX_" + skeleton_formula_pork.metabolite + "_m"
skeleton_formula_prawn = pd.merge(diet_formula_prawn, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_formula_prawn["global_id"] = skeleton_formula_prawn.reaction
skeleton_formula_prawn["reaction"] = "EX_" + skeleton_formula_prawn.metabolite + "_m"
skeleton_formula_pumpkin = pd.merge(diet_formula_pumpkin, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_formula_pumpkin["global_id"] = skeleton_formula_pumpkin.reaction
skeleton_formula_pumpkin["reaction"] = "EX_" + skeleton_formula_pumpkin.metabolite + "_m"
skeleton_formula_raspberries = pd.merge(diet_formula_raspberries, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_formula_raspberries["global_id"] = skeleton_formula_raspberries.reaction
skeleton_formula_raspberries["reaction"] = "EX_" + skeleton_formula_raspberries.metabolite + "_m"
skeleton_formula_soybeans = pd.merge(diet_formula_soybeans, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_formula_soybeans["global_id"] = skeleton_formula_soybeans.reaction
skeleton_formula_soybeans["reaction"] = "EX_" + skeleton_formula_soybeans.metabolite + "_m"
skeleton_formula_strawberries = pd.merge(diet_formula_strawberries, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_formula_strawberries["global_id"] = skeleton_formula_strawberries.reaction
skeleton_formula_strawberries["reaction"] = "EX_" + skeleton_formula_strawberries.metabolite + "_m"
skeleton_formula_yellow_peas = pd.merge(diet_formula_yellow_peas, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_formula_yellow_peas["global_id"] = skeleton_formula_yellow_peas.reaction
skeleton_formula_yellow_peas["reaction"] = "EX_" + skeleton_formula_yellow_peas.metabolite + "_m"
skeleton_black_beans_blackcurrants = pd.merge(diet_black_beans_blackcurrants, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_black_beans_blackcurrants["global_id"] = skeleton_black_beans_blackcurrants.reaction
skeleton_black_beans_blackcurrants["reaction"] = "EX_" + skeleton_black_beans_blackcurrants.metabolite + "_m"
skeleton_black_beans_pumpkin = pd.merge(diet_black_beans_pumpkin, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_black_beans_pumpkin["global_id"] = skeleton_black_beans_pumpkin.reaction
skeleton_black_beans_pumpkin["reaction"] = "EX_" + skeleton_black_beans_pumpkin.metabolite + "_m"
skeleton_blackcurrants_kumara_with_skin = pd.merge(diet_blackcurrants_kumara_with_skin, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_blackcurrants_kumara_with_skin["global_id"] = skeleton_blackcurrants_kumara_with_skin.reaction
skeleton_blackcurrants_kumara_with_skin["reaction"] = "EX_" + skeleton_blackcurrants_kumara_with_skin.metabolite + "_m"
skeleton_blackcurrants_kumara_without_skin = pd.merge(diet_blackcurrants_kumara_without_skin, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_blackcurrants_kumara_without_skin["global_id"] = skeleton_blackcurrants_kumara_without_skin.reaction
skeleton_blackcurrants_kumara_without_skin["reaction"] = "EX_" + skeleton_blackcurrants_kumara_without_skin.metabolite + "_m"
skeleton_blackcurrants_pork = pd.merge(diet_blackcurrants_pork, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_blackcurrants_pork["global_id"] = skeleton_blackcurrants_pork.reaction
skeleton_blackcurrants_pork["reaction"] = "EX_" + skeleton_blackcurrants_pork.metabolite + "_m"
skeleton_blackcurrants_soybeans = pd.merge(diet_blackcurrants_soybeans, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_blackcurrants_soybeans["global_id"] = skeleton_blackcurrants_soybeans.reaction
skeleton_blackcurrants_soybeans["reaction"] = "EX_" + skeleton_blackcurrants_soybeans.metabolite + "_m"
skeleton_blackcurrants_strawberries = pd.merge(diet_blackcurrants_strawberries, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_blackcurrants_strawberries["global_id"] = skeleton_blackcurrants_strawberries.reaction
skeleton_blackcurrants_strawberries["reaction"] = "EX_" + skeleton_blackcurrants_strawberries.metabolite + "_m"
skeleton_chickpeas_pork = pd.merge(diet_chickpeas_pork, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_chickpeas_pork["global_id"] = skeleton_chickpeas_pork.reaction
skeleton_chickpeas_pork["reaction"] = "EX_" + skeleton_chickpeas_pork.metabolite + "_m"
skeleton_chickpeas_yellow_peas = pd.merge(diet_chickpeas_yellow_peas, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_chickpeas_yellow_peas["global_id"] = skeleton_chickpeas_yellow_peas.reaction
skeleton_chickpeas_yellow_peas["reaction"] = "EX_" + skeleton_chickpeas_yellow_peas.metabolite + "_m"
skeleton_couscous_pork = pd.merge(diet_couscous_pork, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_couscous_pork["global_id"] = skeleton_couscous_pork.reaction
skeleton_couscous_pork["reaction"] = "EX_" + skeleton_couscous_pork.metabolite + "_m"
skeleton_couscous_pumpkin = pd.merge(diet_couscous_pumpkin, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_couscous_pumpkin["global_id"] = skeleton_couscous_pumpkin.reaction
skeleton_couscous_pumpkin["reaction"] = "EX_" + skeleton_couscous_pumpkin.metabolite + "_m"
skeleton_pork_raspberries = pd.merge(diet_pork_raspberries, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_pork_raspberries["global_id"] = skeleton_pork_raspberries.reaction
skeleton_pork_raspberries["reaction"] = "EX_" + skeleton_pork_raspberries.metabolite + "_m"
skeleton_pumpkin_yellow_peas = pd.merge(diet_pumpkin_yellow_peas, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_pumpkin_yellow_peas["global_id"] = skeleton_pumpkin_yellow_peas.reaction
skeleton_pumpkin_yellow_peas["reaction"] = "EX_" + skeleton_pumpkin_yellow_peas.metabolite + "_m"
skeleton_formula_black_beans_blackcurrants = pd.merge(diet_formula_black_beans_blackcurrants, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_formula_black_beans_blackcurrants["global_id"] = skeleton_formula_black_beans_blackcurrants.reaction
skeleton_formula_black_beans_blackcurrants["reaction"] = "EX_" + skeleton_formula_black_beans_blackcurrants.metabolite + "_m"
skeleton_formula_black_beans_pumpkin = pd.merge(diet_formula_black_beans_pumpkin, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_formula_black_beans_pumpkin["global_id"] = skeleton_formula_black_beans_pumpkin.reaction
skeleton_formula_black_beans_pumpkin["reaction"] = "EX_" + skeleton_formula_black_beans_pumpkin.metabolite + "_m"
skeleton_formula_blackcurrants_kumara_with_skin = pd.merge(diet_formula_blackcurrants_kumara_with_skin, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_formula_blackcurrants_kumara_with_skin["global_id"] = skeleton_formula_blackcurrants_kumara_with_skin.reaction
skeleton_formula_blackcurrants_kumara_with_skin["reaction"] = "EX_" + skeleton_formula_blackcurrants_kumara_with_skin.metabolite + "_m"
skeleton_formula_blackcurrants_kumara_without_skin = pd.merge(diet_formula_blackcurrants_kumara_without_skin, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_formula_blackcurrants_kumara_without_skin["global_id"] = skeleton_formula_blackcurrants_kumara_without_skin.reaction
skeleton_formula_blackcurrants_kumara_without_skin["reaction"] = "EX_" + skeleton_formula_blackcurrants_kumara_without_skin.metabolite + "_m"
skeleton_formula_blackcurrants_pork = pd.merge(diet_formula_blackcurrants_pork, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_formula_blackcurrants_pork["global_id"] = skeleton_formula_blackcurrants_pork.reaction
skeleton_formula_blackcurrants_pork["reaction"] = "EX_" + skeleton_formula_blackcurrants_pork.metabolite + "_m"
skeleton_formula_blackcurrants_soybeans = pd.merge(diet_formula_blackcurrants_soybeans, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_formula_blackcurrants_soybeans["global_id"] = skeleton_formula_blackcurrants_soybeans.reaction
skeleton_formula_blackcurrants_soybeans["reaction"] = "EX_" + skeleton_formula_blackcurrants_soybeans.metabolite + "_m"
skeleton_formula_blackcurrants_strawberries = pd.merge(diet_formula_blackcurrants_strawberries, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_formula_blackcurrants_strawberries["global_id"] = skeleton_formula_blackcurrants_strawberries.reaction
skeleton_formula_blackcurrants_strawberries["reaction"] = "EX_" + skeleton_formula_blackcurrants_strawberries.metabolite + "_m"
skeleton_formula_chickpeas_pork = pd.merge(diet_formula_chickpeas_pork, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_formula_chickpeas_pork["global_id"] = skeleton_formula_chickpeas_pork.reaction
skeleton_formula_chickpeas_pork["reaction"] = "EX_" + skeleton_formula_chickpeas_pork.metabolite + "_m"
skeleton_formula_chickpeas_yellow_peas = pd.merge(diet_formula_chickpeas_yellow_peas, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_formula_chickpeas_yellow_peas["global_id"] = skeleton_formula_chickpeas_yellow_peas.reaction
skeleton_formula_chickpeas_yellow_peas["reaction"] = "EX_" + skeleton_formula_chickpeas_yellow_peas.metabolite + "_m"
skeleton_formula_couscous_pork = pd.merge(diet_formula_couscous_pork, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_formula_couscous_pork["global_id"] = skeleton_formula_couscous_pork.reaction
skeleton_formula_couscous_pork["reaction"] = "EX_" + skeleton_formula_couscous_pork.metabolite + "_m"
skeleton_formula_couscous_pumpkin = pd.merge(diet_formula_couscous_pumpkin, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_formula_couscous_pumpkin["global_id"] = skeleton_formula_couscous_pumpkin.reaction
skeleton_formula_couscous_pumpkin["reaction"] = "EX_" + skeleton_formula_couscous_pumpkin.metabolite + "_m"
skeleton_formula_pork_raspberries = pd.merge(diet_formula_pork_raspberries, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_formula_pork_raspberries["global_id"] = skeleton_formula_pork_raspberries.reaction
skeleton_formula_pork_raspberries["reaction"] = "EX_" + skeleton_formula_pork_raspberries.metabolite + "_m"
skeleton_formula_pumpkin_yellow_peas = pd.merge(diet_formula_pumpkin_yellow_peas, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_formula_pumpkin_yellow_peas["global_id"] = skeleton_formula_pumpkin_yellow_peas.reaction
skeleton_formula_pumpkin_yellow_peas["reaction"] = "EX_" + skeleton_formula_pumpkin_yellow_peas.metabolite + "_m"

#Supplementing the medium with essential nutrietns for microbial growth
from micom.workflows.db_media import complete_db_medium

manifest_black_beans, imports_black_beans = complete_db_medium("data/agora201__species.qza", skeleton_black_beans, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_blackcurrants, imports_blackcurrants = complete_db_medium("data/agora201__species.qza", skeleton_blackcurrants, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_chickpeas, imports_chickpeas = complete_db_medium("data/agora201__species.qza", skeleton_chickpeas, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_couscous, imports_couscous = complete_db_medium("data/agora201__species.qza", skeleton_couscous, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_infant_formula, imports_infant_formula = complete_db_medium("data/agora201__species.qza", skeleton_infant_formula, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_kumara_with_skin, imports_kumara_with_skin = complete_db_medium("data/agora201__species.qza", skeleton_kumara_with_skin, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_kumara_without_skin, imports_kumara_without_skin = complete_db_medium("data/agora201__species.qza", skeleton_kumara_without_skin, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_pork, imports_pork = complete_db_medium("data/agora201__species.qza", skeleton_pork, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_prawn, imports_prawn = complete_db_medium("data/agora201__species.qza", skeleton_prawn, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_pumpkin, imports_pumpkin = complete_db_medium("data/agora201__species.qza", skeleton_pumpkin, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_raspberries, imports_raspberries = complete_db_medium("data/agora201__species.qza", skeleton_raspberries, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_soybeans, imports_soybeans = complete_db_medium("data/agora201__species.qza", skeleton_soybeans, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_strawberries, imports_strawberries = complete_db_medium("data/agora201__species.qza", skeleton_strawberries, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_yellow_peas, imports_yellow_peas = complete_db_medium("data/agora201__species.qza", skeleton_yellow_peas, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_formula_black_beans, imports_formula_black_beans = complete_db_medium("data/agora201__species.qza", skeleton_formula_black_beans, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_formula_blackcurrants, imports_formula_blackcurrants = complete_db_medium("data/agora201__species.qza", skeleton_formula_blackcurrants, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_formula_chickpeas, imports_formula_chickpeas = complete_db_medium("data/agora201__species.qza", skeleton_formula_chickpeas, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_formula_couscous, imports_formula_couscous = complete_db_medium("data/agora201__species.qza", skeleton_formula_couscous, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_formula_kumara_with_skin, imports_formula_kumara_with_skin = complete_db_medium("data/agora201__species.qza", skeleton_formula_kumara_with_skin, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_formula_kumara_without_skin, imports_formula_kumara_without_skin = complete_db_medium("data/agora201__species.qza", skeleton_formula_kumara_without_skin, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_formula_pork, imports_formula_pork = complete_db_medium("data/agora201__species.qza", skeleton_formula_pork, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_formula_prawn, imports_formula_prawn = complete_db_medium("data/agora201__species.qza", skeleton_formula_prawn, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_formula_pumpkin, imports_formula_pumpkin = complete_db_medium("data/agora201__species.qza", skeleton_formula_pumpkin, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_formula_raspberries, imports_formula_raspberries = complete_db_medium("data/agora201__species.qza", skeleton_formula_raspberries, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_formula_soybeans, imports_formula_soybeans = complete_db_medium("data/agora201__species.qza", skeleton_formula_soybeans, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_formula_strawberries, imports_formula_strawberries = complete_db_medium("data/agora201__species.qza", skeleton_formula_strawberries, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_formula_yellow_peas, imports_formula_yellow_peas = complete_db_medium("data/agora201__species.qza", skeleton_formula_yellow_peas, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_black_beans_blackcurrants, imports_black_beans_blackcurrants = complete_db_medium("data/agora201__species.qza", skeleton_black_beans_blackcurrants, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_black_beans_pumpkin, imports_black_beans_pumpkin = complete_db_medium("data/agora201__species.qza", skeleton_black_beans_pumpkin, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_blackcurrants_kumara_with_skin, imports_blackcurrants_kumara_with_skin = complete_db_medium("data/agora201__species.qza", skeleton_blackcurrants_kumara_with_skin, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_blackcurrants_kumara_without_skin, imports_blackcurrants_kumara_without_skin = complete_db_medium("data/agora201__species.qza", skeleton_blackcurrants_kumara_without_skin, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_blackcurrants_pork, imports_blackcurrants_pork = complete_db_medium("data/agora201__species.qza", skeleton_blackcurrants_pork, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_blackcurrants_soybeans, imports_blackcurrants_soybeans = complete_db_medium("data/agora201__species.qza", skeleton_blackcurrants_soybeans, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_blackcurrants_strawberries, imports_blackcurrants_strawberries = complete_db_medium("data/agora201__species.qza", skeleton_blackcurrants_strawberries, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_chickpeas_pork, imports_chickpeas_pork = complete_db_medium("data/agora201__species.qza", skeleton_chickpeas_pork, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_chickpeas_yellow_peas, imports_chickpeas_yellow_peas = complete_db_medium("data/agora201__species.qza", skeleton_chickpeas_yellow_peas, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_couscous_pork, imports_couscous_pork = complete_db_medium("data/agora201__species.qza", skeleton_couscous_pork, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_couscous_pumpkin, imports_couscous_pumpkin = complete_db_medium("data/agora201__species.qza", skeleton_couscous_pumpkin, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_pork_raspberries, imports_pork_raspberries = complete_db_medium("data/agora201__species.qza", skeleton_pork_raspberries, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_pumpkin_yellow_peas, imports_pumpkin_yellow_peas = complete_db_medium("data/agora201__species.qza", skeleton_pumpkin_yellow_peas, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_formula_black_beans_blackcurrants, imports_formula_black_beans_blackcurrants = complete_db_medium("data/agora201__species.qza", skeleton_formula_black_beans_blackcurrants, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_formula_black_beans_pumpkin, imports_formula_black_beans_pumpkin = complete_db_medium("data/agora201__species.qza", skeleton_formula_black_beans_pumpkin, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_formula_blackcurrants_kumara_with_skin, imports_formula_blackcurrants_kumara_with_skin = complete_db_medium("data/agora201__species.qza", skeleton_formula_blackcurrants_kumara_with_skin, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_formula_blackcurrants_kumara_without_skin, imports_formula_blackcurrants_kumara_without_skin = complete_db_medium("data/agora201__species.qza", skeleton_formula_blackcurrants_kumara_without_skin, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_formula_blackcurrants_pork, imports_formula_blackcurrants_pork = complete_db_medium("data/agora201__species.qza", skeleton_formula_blackcurrants_pork, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_formula_blackcurrants_soybeans, imports_formula_blackcurrants_soybeans = complete_db_medium("data/agora201__species.qza", skeleton_formula_blackcurrants_soybeans, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_formula_blackcurrants_strawberries, imports_formula_blackcurrants_strawberries = complete_db_medium("data/agora201__species.qza", skeleton_formula_blackcurrants_strawberries, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_formula_chickpeas_pork, imports_formula_chickpeas_pork = complete_db_medium("data/agora201__species.qza", skeleton_formula_chickpeas_pork, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_formula_chickpeas_yellow_peas, imports_formula_chickpeas_yellow_peas = complete_db_medium("data/agora201__species.qza", skeleton_formula_chickpeas_yellow_peas, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_formula_couscous_pork, imports_formula_couscous_pork = complete_db_medium("data/agora201__species.qza", skeleton_formula_couscous_pork, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_formula_couscous_pumpkin, imports_formula_couscous_pumpkin = complete_db_medium("data/agora201__species.qza", skeleton_formula_couscous_pumpkin, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_formula_pork_raspberries, imports_formula_pork_raspberries = complete_db_medium("data/agora201__species.qza", skeleton_formula_pork_raspberries, growth=0.3, threads=14, max_added_import=10, minimize_components=True)
manifest_formula_pumpkin_yellow_peas, imports_formula_pumpkin_yellow_peas = complete_db_medium("data/agora201__species.qza", skeleton_formula_pumpkin_yellow_peas, growth=0.3, threads=14, max_added_import=10, minimize_components=True)

manifest_black_beans.can_grow.value_counts() #checking the microbial growth
filled_black_beans = imports_black_beans.max()
added_black_beans = filled_black_beans[~filled_black_beans.index.isin(skeleton_black_beans.reaction)] #fluxes that were added
manifest_blackcurrants.can_grow.value_counts() #checking the microbial growth
filled_blackcurrants = imports_blackcurrants.max()
added_blackcurrants = filled_blackcurrants[~filled_blackcurrants.index.isin(skeleton_blackcurrants.reaction)] #fluxes that were added
manifest_chickpeas.can_grow.value_counts() #checking the microbial growth
filled_chickpeas = imports_chickpeas.max()
added_chickpeas = filled_chickpeas[~filled_chickpeas.index.isin(skeleton_chickpeas.reaction)] #fluxes that were added
manifest_couscous.can_grow.value_counts() #checking the microbial growth
filled_couscous = imports_couscous.max()
added_couscous = filled_couscous[~filled_couscous.index.isin(skeleton_couscous.reaction)] #fluxes that were added
manifest_infant_formula.can_grow.value_counts() #checking the microbial growth
filled_infant_formula = imports_infant_formula.max()
added_infant_formula = filled_infant_formula[~filled_infant_formula.index.isin(skeleton_infant_formula.reaction)] #fluxes that were added
manifest_kumara_with_skin.can_grow.value_counts() #checking the microbial growth
filled_kumara_with_skin = imports_kumara_with_skin.max()
added_kumara_with_skin = filled_kumara_with_skin[~filled_kumara_with_skin.index.isin(skeleton_kumara_with_skin.reaction)] #fluxes that were added
manifest_kumara_without_skin.can_grow.value_counts() #checking the microbial growth
filled_kumara_without_skin = imports_kumara_without_skin.max()
added_kumara_without_skin = filled_kumara_without_skin[~filled_kumara_without_skin.index.isin(skeleton_kumara_without_skin.reaction)] #fluxes that were added
manifest_pork.can_grow.value_counts() #checking the microbial growth
filled_pork = imports_pork.max()
added_pork = filled_pork[~filled_pork.index.isin(skeleton_pork.reaction)] #fluxes that were added
manifest_prawn.can_grow.value_counts() #checking the microbial growth
filled_prawn = imports_prawn.max()
added_prawn = filled_prawn[~filled_prawn.index.isin(skeleton_prawn.reaction)] #fluxes that were added
manifest_pumpkin.can_grow.value_counts() #checking the microbial growth
filled_pumpkin = imports_pumpkin.max()
added_pumpkin = filled_pumpkin[~filled_pumpkin.index.isin(skeleton_pumpkin.reaction)] #fluxes that were added
manifest_raspberries.can_grow.value_counts() #checking the microbial growth
filled_raspberries = imports_raspberries.max()
added_raspberries = filled_raspberries[~filled_raspberries.index.isin(skeleton_raspberries.reaction)] #fluxes that were added
manifest_soybeans.can_grow.value_counts() #checking the microbial growth
filled_soybeans = imports_soybeans.max()
added_soybeans = filled_soybeans[~filled_soybeans.index.isin(skeleton_soybeans.reaction)] #fluxes that were added
manifest_strawberries.can_grow.value_counts() #checking the microbial growth
filled_strawberries = imports_strawberries.max()
added_strawberries = filled_strawberries[~filled_strawberries.index.isin(skeleton_strawberries.reaction)] #fluxes that were added
manifest_yellow_peas.can_grow.value_counts() #checking the microbial growth
filled_yellow_peas = imports_yellow_peas.max()
added_yellow_peas = filled_yellow_peas[~filled_yellow_peas.index.isin(skeleton_yellow_peas.reaction)] #fluxes that were added
manifest_formula_black_beans.can_grow.value_counts() #checking the microbial growth
filled_formula_black_beans = imports_formula_black_beans.max()
added_formula_black_beans = filled_formula_black_beans[~filled_formula_black_beans.index.isin(skeleton_formula_black_beans.reaction)] #fluxes that were added
manifest_formula_blackcurrants.can_grow.value_counts() #checking the microbial growth
filled_formula_blackcurrants = imports_formula_blackcurrants.max()
added_formula_blackcurrants = filled_formula_blackcurrants[~filled_formula_blackcurrants.index.isin(skeleton_formula_blackcurrants.reaction)] #fluxes that were added
manifest_formula_chickpeas.can_grow.value_counts() #checking the microbial growth
filled_formula_chickpeas = imports_formula_chickpeas.max()
added_formula_chickpeas = filled_formula_chickpeas[~filled_formula_chickpeas.index.isin(skeleton_formula_chickpeas.reaction)] #fluxes that were added
manifest_formula_couscous.can_grow.value_counts() #checking the microbial growth
filled_formula_couscous = imports_formula_couscous.max()
added_formula_couscous = filled_formula_couscous[~filled_formula_couscous.index.isin(skeleton_formula_couscous.reaction)] #fluxes that were added
manifest_formula_kumara_with_skin.can_grow.value_counts() #checking the microbial growth
filled_formula_kumara_with_skin = imports_formula_kumara_with_skin.max()
added_formula_kumara_with_skin = filled_formula_kumara_with_skin[~filled_formula_kumara_with_skin.index.isin(skeleton_formula_kumara_with_skin.reaction)] #fluxes that were added
manifest_formula_kumara_without_skin.can_grow.value_counts() #checking the microbial growth
filled_formula_kumara_without_skin = imports_formula_kumara_without_skin.max()
added_formula_kumara_without_skin = filled_formula_kumara_without_skin[~filled_formula_kumara_without_skin.index.isin(skeleton_formula_kumara_without_skin.reaction)] #fluxes that were added
manifest_formula_pork.can_grow.value_counts() #checking the microbial growth
filled_formula_pork = imports_formula_pork.max()
added_formula_pork = filled_formula_pork[~filled_formula_pork.index.isin(skeleton_formula_pork.reaction)] #fluxes that were added
manifest_formula_prawn.can_grow.value_counts() #checking the microbial growth
filled_formula_prawn = imports_formula_prawn.max()
added_formula_prawn = filled_formula_prawn[~filled_formula_prawn.index.isin(skeleton_formula_prawn.reaction)] #fluxes that were added
manifest_formula_pumpkin.can_grow.value_counts() #checking the microbial growth
filled_formula_pumpkin = imports_formula_pumpkin.max()
added_formula_pumpkin = filled_formula_pumpkin[~filled_formula_pumpkin.index.isin(skeleton_formula_pumpkin.reaction)] #fluxes that were added
manifest_formula_raspberries.can_grow.value_counts() #checking the microbial growth
filled_formula_raspberries = imports_formula_raspberries.max()
added_formula_raspberries = filled_formula_raspberries[~filled_formula_raspberries.index.isin(skeleton_formula_raspberries.reaction)] #fluxes that were added
manifest_formula_soybeans.can_grow.value_counts() #checking the microbial growth
filled_formula_soybeans = imports_formula_soybeans.max()
added_formula_soybeans = filled_formula_soybeans[~filled_formula_soybeans.index.isin(skeleton_formula_soybeans.reaction)] #fluxes that were added
manifest_formula_strawberries.can_grow.value_counts() #checking the microbial growth
filled_formula_strawberries = imports_formula_strawberries.max()
added_formula_strawberries = filled_formula_strawberries[~filled_formula_strawberries.index.isin(skeleton_formula_strawberries.reaction)] #fluxes that were added
manifest_formula_yellow_peas.can_grow.value_counts() #checking the microbial growth
filled_formula_yellow_peas = imports_formula_yellow_peas.max()
added_formula_yellow_peas = filled_formula_yellow_peas[~filled_formula_yellow_peas.index.isin(skeleton_formula_yellow_peas.reaction)] #fluxes that were added
manifest_black_beans_blackcurrants.can_grow.value_counts() #checking the microbial growth
filled_black_beans_blackcurrants = imports_black_beans_blackcurrants.max()
added_black_beans_blackcurrants = filled_black_beans_blackcurrants[~filled_black_beans_blackcurrants.index.isin(skeleton_black_beans_blackcurrants.reaction)] #fluxes that were added
manifest_black_beans_pumpkin.can_grow.value_counts() #checking the microbial growth
filled_black_beans_pumpkin = imports_black_beans_pumpkin.max()
added_black_beans_pumpkin = filled_black_beans_pumpkin[~filled_black_beans_pumpkin.index.isin(skeleton_black_beans_pumpkin.reaction)] #fluxes that were added
manifest_blackcurrants_kumara_with_skin.can_grow.value_counts() #checking the microbial growth
filled_blackcurrants_kumara_with_skin = imports_blackcurrants_kumara_with_skin.max()
added_blackcurrants_kumara_with_skin = filled_blackcurrants_kumara_with_skin[~filled_blackcurrants_kumara_with_skin.index.isin(skeleton_blackcurrants_kumara_with_skin.reaction)] #fluxes that were added
manifest_blackcurrants_kumara_without_skin.can_grow.value_counts() #checking the microbial growth
filled_blackcurrants_kumara_without_skin = imports_blackcurrants_kumara_without_skin.max()
added_blackcurrants_kumara_without_skin = filled_blackcurrants_kumara_without_skin[~filled_blackcurrants_kumara_without_skin.index.isin(skeleton_blackcurrants_kumara_without_skin.reaction)] #fluxes that were added
manifest_blackcurrants_pork.can_grow.value_counts() #checking the microbial growth
filled_blackcurrants_pork = imports_blackcurrants_pork.max()
added_blackcurrants_pork = filled_blackcurrants_pork[~filled_blackcurrants_pork.index.isin(skeleton_blackcurrants_pork.reaction)] #fluxes that were added
manifest_blackcurrants_soybeans.can_grow.value_counts() #checking the microbial growth
filled_blackcurrants_soybeans = imports_blackcurrants_soybeans.max()
added_blackcurrants_soybeans = filled_blackcurrants_soybeans[~filled_blackcurrants_soybeans.index.isin(skeleton_blackcurrants_soybeans.reaction)] #fluxes that were added
manifest_blackcurrants_strawberries.can_grow.value_counts() #checking the microbial growth
filled_blackcurrants_strawberries = imports_blackcurrants_strawberries.max()
added_blackcurrants_strawberries = filled_blackcurrants_strawberries[~filled_blackcurrants_strawberries.index.isin(skeleton_blackcurrants_strawberries.reaction)] #fluxes that were added
manifest_chickpeas_pork.can_grow.value_counts() #checking the microbial growth
filled_chickpeas_pork = imports_chickpeas_pork.max()
added_chickpeas_pork = filled_chickpeas_pork[~filled_chickpeas_pork.index.isin(skeleton_chickpeas_pork.reaction)] #fluxes that were added
manifest_chickpeas_yellow_peas.can_grow.value_counts() #checking the microbial growth
filled_chickpeas_yellow_peas = imports_chickpeas_yellow_peas.max()
added_chickpeas_yellow_peas = filled_chickpeas_yellow_peas[~filled_chickpeas_yellow_peas.index.isin(skeleton_chickpeas_yellow_peas.reaction)] #fluxes that were added
manifest_couscous_pork.can_grow.value_counts() #checking the microbial growth
filled_couscous_pork = imports_couscous_pork.max()
added_couscous_pork = filled_couscous_pork[~filled_couscous_pork.index.isin(skeleton_couscous_pork.reaction)] #fluxes that were added
manifest_couscous_pumpkin.can_grow.value_counts() #checking the microbial growth
filled_couscous_pumpkin = imports_couscous_pumpkin.max()
added_couscous_pumpkin = filled_couscous_pumpkin[~filled_couscous_pumpkin.index.isin(skeleton_couscous_pumpkin.reaction)] #fluxes that were added
manifest_pork_raspberries.can_grow.value_counts() #checking the microbial growth
filled_pork_raspberries = imports_pork_raspberries.max()
added_pork_raspberries = filled_pork_raspberries[~filled_pork_raspberries.index.isin(skeleton_pork_raspberries.reaction)] #fluxes that were added
manifest_pumpkin_yellow_peas.can_grow.value_counts() #checking the microbial growth
filled_pumpkin_yellow_peas = imports_pumpkin_yellow_peas.max()
added_pumpkin_yellow_peas = filled_pumpkin_yellow_peas[~filled_pumpkin_yellow_peas.index.isin(skeleton_pumpkin_yellow_peas.reaction)] #fluxes that were added
manifest_formula_black_beans_blackcurrants.can_grow.value_counts() #checking the microbial growth
filled_formula_black_beans_blackcurrants = imports_formula_black_beans_blackcurrants.max()
added_formula_black_beans_blackcurrants = filled_formula_black_beans_blackcurrants[~filled_formula_black_beans_blackcurrants.index.isin(skeleton_formula_black_beans_blackcurrants.reaction)] #fluxes that were added
manifest_formula_black_beans_pumpkin.can_grow.value_counts() #checking the microbial growth
filled_formula_black_beans_pumpkin = imports_formula_black_beans_pumpkin.max()
added_formula_black_beans_pumpkin = filled_formula_black_beans_pumpkin[~filled_formula_black_beans_pumpkin.index.isin(skeleton_formula_black_beans_pumpkin.reaction)] #fluxes that were added
manifest_formula_blackcurrants_kumara_with_skin.can_grow.value_counts() #checking the microbial growth
filled_formula_blackcurrants_kumara_with_skin = imports_formula_blackcurrants_kumara_with_skin.max()
added_formula_blackcurrants_kumara_with_skin = filled_formula_blackcurrants_kumara_with_skin[~filled_formula_blackcurrants_kumara_with_skin.index.isin(skeleton_formula_blackcurrants_kumara_with_skin.reaction)] #fluxes that were added
manifest_formula_blackcurrants_kumara_without_skin.can_grow.value_counts() #checking the microbial growth
filled_formula_blackcurrants_kumara_without_skin = imports_formula_blackcurrants_kumara_without_skin.max()
added_formula_blackcurrants_kumara_without_skin = filled_formula_blackcurrants_kumara_without_skin[~filled_formula_blackcurrants_kumara_without_skin.index.isin(skeleton_formula_blackcurrants_kumara_without_skin.reaction)] #fluxes that were added
manifest_formula_blackcurrants_pork.can_grow.value_counts() #checking the microbial growth
filled_formula_blackcurrants_pork = imports_formula_blackcurrants_pork.max()
added_formula_blackcurrants_pork = filled_formula_blackcurrants_pork[~filled_formula_blackcurrants_pork.index.isin(skeleton_formula_blackcurrants_pork.reaction)] #fluxes that were added
manifest_formula_blackcurrants_soybeans.can_grow.value_counts() #checking the microbial growth
filled_formula_blackcurrants_soybeans = imports_formula_blackcurrants_soybeans.max()
added_formula_blackcurrants_soybeans = filled_formula_blackcurrants_soybeans[~filled_formula_blackcurrants_soybeans.index.isin(skeleton_formula_blackcurrants_soybeans.reaction)] #fluxes that were added
manifest_formula_blackcurrants_strawberries.can_grow.value_counts() #checking the microbial growth
filled_formula_blackcurrants_strawberries = imports_formula_blackcurrants_strawberries.max()
added_formula_blackcurrants_strawberries = filled_formula_blackcurrants_strawberries[~filled_formula_blackcurrants_strawberries.index.isin(skeleton_formula_blackcurrants_strawberries.reaction)] #fluxes that were added
manifest_formula_chickpeas_pork.can_grow.value_counts() #checking the microbial growth
filled_formula_chickpeas_pork = imports_formula_chickpeas_pork.max()
added_formula_chickpeas_pork = filled_formula_chickpeas_pork[~filled_formula_chickpeas_pork.index.isin(skeleton_formula_chickpeas_pork.reaction)] #fluxes that were added
manifest_formula_chickpeas_yellow_peas.can_grow.value_counts() #checking the microbial growth
filled_formula_chickpeas_yellow_peas = imports_formula_chickpeas_yellow_peas.max()
added_formula_chickpeas_yellow_peas = filled_formula_chickpeas_yellow_peas[~filled_formula_chickpeas_yellow_peas.index.isin(skeleton_formula_chickpeas_yellow_peas.reaction)] #fluxes that were added
manifest_formula_couscous_pork.can_grow.value_counts() #checking the microbial growth
filled_formula_couscous_pork = imports_formula_couscous_pork.max()
added_formula_couscous_pork = filled_formula_couscous_pork[~filled_formula_couscous_pork.index.isin(skeleton_formula_couscous_pork.reaction)] #fluxes that were added
manifest_formula_couscous_pumpkin.can_grow.value_counts() #checking the microbial growth
filled_formula_couscous_pumpkin = imports_formula_couscous_pumpkin.max()
added_formula_couscous_pumpkin = filled_formula_couscous_pumpkin[~filled_formula_couscous_pumpkin.index.isin(skeleton_formula_couscous_pumpkin.reaction)] #fluxes that were added
manifest_formula_pork_raspberries.can_grow.value_counts() #checking the microbial growth
filled_formula_pork_raspberries = imports_formula_pork_raspberries.max()
added_formula_pork_raspberries = filled_formula_pork_raspberries[~filled_formula_pork_raspberries.index.isin(skeleton_formula_pork_raspberries.reaction)] #fluxes that were added
manifest_formula_pumpkin_yellow_peas.can_grow.value_counts() #checking the microbial growth
filled_formula_pumpkin_yellow_peas = imports_formula_pumpkin_yellow_peas.max()
added_formula_pumpkin_yellow_peas = filled_formula_pumpkin_yellow_peas[~filled_formula_pumpkin_yellow_peas.index.isin(skeleton_formula_pumpkin_yellow_peas.reaction)] #fluxes that were added

#Assembling the final medium

added_df_black_beans = added_black_beans.reset_index() 
added_df_black_beans.iloc[:, 0] = added_df_black_beans.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_black_beans.columns = ["metabolite", "flux"]
added_df_black_beans = pd.concat([skeleton_black_beans[["metabolite", "flux"]], added_df_black_beans])
added_df_blackcurrants = added_blackcurrants.reset_index() 
added_df_blackcurrants.iloc[:, 0] = added_df_blackcurrants.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_blackcurrants.columns = ["metabolite", "flux"]
added_df_blackcurrants = pd.concat([skeleton_blackcurrants[["metabolite", "flux"]], added_df_blackcurrants])
added_df_chickpeas = added_chickpeas.reset_index() 
added_df_chickpeas.iloc[:, 0] = added_df_chickpeas.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_chickpeas.columns = ["metabolite", "flux"]
added_df_chickpeas = pd.concat([skeleton_chickpeas[["metabolite", "flux"]], added_df_chickpeas])
added_df_couscous = added_couscous.reset_index() 
added_df_couscous.iloc[:, 0] = added_df_couscous.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_couscous.columns = ["metabolite", "flux"]
added_df_couscous = pd.concat([skeleton_couscous[["metabolite", "flux"]], added_df_couscous])
added_df_infant_formula = added_infant_formula.reset_index() 
added_df_infant_formula.iloc[:, 0] = added_df_infant_formula.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_infant_formula.columns = ["metabolite", "flux"]
added_df_infant_formula = pd.concat([skeleton_infant_formula[["metabolite", "flux"]], added_df_infant_formula])
added_df_kumara_with_skin = added_kumara_with_skin.reset_index() 
added_df_kumara_with_skin.iloc[:, 0] = added_df_kumara_with_skin.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_kumara_with_skin.columns = ["metabolite", "flux"]
added_df_kumara_with_skin = pd.concat([skeleton_kumara_with_skin[["metabolite", "flux"]], added_df_kumara_with_skin])
added_df_kumara_without_skin = added_kumara_without_skin.reset_index() 
added_df_kumara_without_skin.iloc[:, 0] = added_df_kumara_without_skin.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_kumara_without_skin.columns = ["metabolite", "flux"]
added_df_kumara_without_skin = pd.concat([skeleton_kumara_without_skin[["metabolite", "flux"]], added_df_kumara_without_skin])
added_df_pork = added_pork.reset_index() 
added_df_pork.iloc[:, 0] = added_df_pork.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_pork.columns = ["metabolite", "flux"]
added_df_pork = pd.concat([skeleton_pork[["metabolite", "flux"]], added_df_pork])
added_df_prawn = added_prawn.reset_index() 
added_df_prawn.iloc[:, 0] = added_df_prawn.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_prawn.columns = ["metabolite", "flux"]
added_df_prawn = pd.concat([skeleton_prawn[["metabolite", "flux"]], added_df_prawn])
added_df_pumpkin = added_pumpkin.reset_index() 
added_df_pumpkin.iloc[:, 0] = added_df_pumpkin.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_pumpkin.columns = ["metabolite", "flux"]
added_df_pumpkin = pd.concat([skeleton_pumpkin[["metabolite", "flux"]], added_df_pumpkin])
added_df_raspberries = added_raspberries.reset_index() 
added_df_raspberries.iloc[:, 0] = added_df_raspberries.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_raspberries.columns = ["metabolite", "flux"]
added_df_raspberries = pd.concat([skeleton_raspberries[["metabolite", "flux"]], added_df_raspberries])
added_df_soybeans = added_soybeans.reset_index() 
added_df_soybeans.iloc[:, 0] = added_df_soybeans.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_soybeans.columns = ["metabolite", "flux"]
added_df_soybeans = pd.concat([skeleton_soybeans[["metabolite", "flux"]], added_df_soybeans])
added_df_strawberries = added_strawberries.reset_index() 
added_df_strawberries.iloc[:, 0] = added_df_strawberries.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_strawberries.columns = ["metabolite", "flux"]
added_df_strawberries = pd.concat([skeleton_strawberries[["metabolite", "flux"]], added_df_strawberries])
added_df_yellow_peas = added_yellow_peas.reset_index() 
added_df_yellow_peas.iloc[:, 0] = added_df_yellow_peas.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_yellow_peas.columns = ["metabolite", "flux"]
added_df_yellow_peas = pd.concat([skeleton_yellow_peas[["metabolite", "flux"]], added_df_yellow_peas])
added_df_formula_black_beans = added_formula_black_beans.reset_index() 
added_df_formula_black_beans.iloc[:, 0] = added_df_formula_black_beans.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_formula_black_beans.columns = ["metabolite", "flux"]
added_df_formula_black_beans = pd.concat([skeleton_formula_black_beans[["metabolite", "flux"]], added_df_formula_black_beans])
added_df_formula_blackcurrants = added_formula_blackcurrants.reset_index() 
added_df_formula_blackcurrants.iloc[:, 0] = added_df_formula_blackcurrants.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_formula_blackcurrants.columns = ["metabolite", "flux"]
added_df_formula_blackcurrants = pd.concat([skeleton_formula_blackcurrants[["metabolite", "flux"]], added_df_formula_blackcurrants])
added_df_formula_chickpeas = added_formula_chickpeas.reset_index() 
added_df_formula_chickpeas.iloc[:, 0] = added_df_formula_chickpeas.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_formula_chickpeas.columns = ["metabolite", "flux"]
added_df_formula_chickpeas = pd.concat([skeleton_formula_chickpeas[["metabolite", "flux"]], added_df_formula_chickpeas])
added_df_formula_couscous = added_formula_couscous.reset_index() 
added_df_formula_couscous.iloc[:, 0] = added_df_formula_couscous.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_formula_couscous.columns = ["metabolite", "flux"]
added_df_formula_couscous = pd.concat([skeleton_formula_couscous[["metabolite", "flux"]], added_df_formula_couscous])
added_df_formula_kumara_with_skin = added_formula_kumara_with_skin.reset_index() 
added_df_formula_kumara_with_skin.iloc[:, 0] = added_df_formula_kumara_with_skin.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_formula_kumara_with_skin.columns = ["metabolite", "flux"]
added_df_formula_kumara_with_skin = pd.concat([skeleton_formula_kumara_with_skin[["metabolite", "flux"]], added_df_formula_kumara_with_skin])
added_df_formula_kumara_without_skin = added_formula_kumara_without_skin.reset_index() 
added_df_formula_kumara_without_skin.iloc[:, 0] = added_df_formula_kumara_without_skin.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_formula_kumara_without_skin.columns = ["metabolite", "flux"]
added_df_formula_kumara_without_skin = pd.concat([skeleton_formula_kumara_without_skin[["metabolite", "flux"]], added_df_formula_kumara_without_skin])
added_df_formula_pork = added_formula_pork.reset_index() 
added_df_formula_pork.iloc[:, 0] = added_df_formula_pork.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_formula_pork.columns = ["metabolite", "flux"]
added_df_formula_pork = pd.concat([skeleton_formula_pork[["metabolite", "flux"]], added_df_formula_pork])
added_df_formula_prawn = added_formula_prawn.reset_index() 
added_df_formula_prawn.iloc[:, 0] = added_df_formula_prawn.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_formula_prawn.columns = ["metabolite", "flux"]
added_df_formula_prawn = pd.concat([skeleton_formula_prawn[["metabolite", "flux"]], added_df_formula_prawn])
added_df_formula_pumpkin = added_formula_pumpkin.reset_index() 
added_df_formula_pumpkin.iloc[:, 0] = added_df_formula_pumpkin.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_formula_pumpkin.columns = ["metabolite", "flux"]
added_df_formula_pumpkin = pd.concat([skeleton_formula_pumpkin[["metabolite", "flux"]], added_df_formula_pumpkin])
added_df_formula_raspberries = added_formula_raspberries.reset_index() 
added_df_formula_raspberries.iloc[:, 0] = added_df_formula_raspberries.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_formula_raspberries.columns = ["metabolite", "flux"]
added_df_formula_raspberries = pd.concat([skeleton_formula_raspberries[["metabolite", "flux"]], added_df_formula_raspberries])
added_df_formula_soybeans = added_formula_soybeans.reset_index() 
added_df_formula_soybeans.iloc[:, 0] = added_df_formula_soybeans.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_formula_soybeans.columns = ["metabolite", "flux"]
added_df_formula_soybeans = pd.concat([skeleton_formula_soybeans[["metabolite", "flux"]], added_df_formula_soybeans])
added_df_formula_strawberries = added_formula_strawberries.reset_index() 
added_df_formula_strawberries.iloc[:, 0] = added_df_formula_strawberries.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_formula_strawberries.columns = ["metabolite", "flux"]
added_df_formula_strawberries = pd.concat([skeleton_formula_strawberries[["metabolite", "flux"]], added_df_formula_strawberries])
added_df_formula_yellow_peas = added_formula_yellow_peas.reset_index() 
added_df_formula_yellow_peas.iloc[:, 0] = added_df_formula_yellow_peas.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_formula_yellow_peas.columns = ["metabolite", "flux"]
added_df_formula_yellow_peas = pd.concat([skeleton_formula_yellow_peas[["metabolite", "flux"]], added_df_formula_yellow_peas])
added_df_black_beans_blackcurrants = added_black_beans_blackcurrants.reset_index() 
added_df_black_beans_blackcurrants.iloc[:, 0] = added_df_black_beans_blackcurrants.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_black_beans_blackcurrants.columns = ["metabolite", "flux"]
added_df_black_beans_blackcurrants = pd.concat([skeleton_black_beans_blackcurrants[["metabolite", "flux"]], added_df_black_beans_blackcurrants])
added_df_black_beans_pumpkin = added_black_beans_pumpkin.reset_index() 
added_df_black_beans_pumpkin.iloc[:, 0] = added_df_black_beans_pumpkin.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_black_beans_pumpkin.columns = ["metabolite", "flux"]
added_df_black_beans_pumpkin = pd.concat([skeleton_black_beans_pumpkin[["metabolite", "flux"]], added_df_black_beans_pumpkin])
added_df_blackcurrants_kumara_with_skin = added_blackcurrants_kumara_with_skin.reset_index() 
added_df_blackcurrants_kumara_with_skin.iloc[:, 0] = added_df_blackcurrants_kumara_with_skin.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_blackcurrants_kumara_with_skin.columns = ["metabolite", "flux"]
added_df_blackcurrants_kumara_with_skin = pd.concat([skeleton_blackcurrants_kumara_with_skin[["metabolite", "flux"]], added_df_blackcurrants_kumara_with_skin])
added_df_blackcurrants_kumara_without_skin = added_blackcurrants_kumara_without_skin.reset_index() 
added_df_blackcurrants_kumara_without_skin.iloc[:, 0] = added_df_blackcurrants_kumara_without_skin.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_blackcurrants_kumara_without_skin.columns = ["metabolite", "flux"]
added_df_blackcurrants_kumara_without_skin = pd.concat([skeleton_blackcurrants_kumara_without_skin[["metabolite", "flux"]], added_df_blackcurrants_kumara_without_skin])
added_df_blackcurrants_pork = added_blackcurrants_pork.reset_index() 
added_df_blackcurrants_pork.iloc[:, 0] = added_df_blackcurrants_pork.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_blackcurrants_pork.columns = ["metabolite", "flux"]
added_df_blackcurrants_pork = pd.concat([skeleton_blackcurrants_pork[["metabolite", "flux"]], added_df_blackcurrants_pork])
added_df_blackcurrants_soybeans = added_blackcurrants_soybeans.reset_index() 
added_df_blackcurrants_soybeans.iloc[:, 0] = added_df_blackcurrants_soybeans.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_blackcurrants_soybeans.columns = ["metabolite", "flux"]
added_df_blackcurrants_soybeans = pd.concat([skeleton_blackcurrants_soybeans[["metabolite", "flux"]], added_df_blackcurrants_soybeans])
added_df_blackcurrants_strawberries = added_blackcurrants_strawberries.reset_index() 
added_df_blackcurrants_strawberries.iloc[:, 0] = added_df_blackcurrants_strawberries.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_blackcurrants_strawberries.columns = ["metabolite", "flux"]
added_df_blackcurrants_strawberries = pd.concat([skeleton_blackcurrants_strawberries[["metabolite", "flux"]], added_df_blackcurrants_strawberries])
added_df_chickpeas_pork = added_chickpeas_pork.reset_index() 
added_df_chickpeas_pork.iloc[:, 0] = added_df_chickpeas_pork.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_chickpeas_pork.columns = ["metabolite", "flux"]
added_df_chickpeas_pork = pd.concat([skeleton_chickpeas_pork[["metabolite", "flux"]], added_df_chickpeas_pork])
added_df_chickpeas_yellow_peas = added_chickpeas_yellow_peas.reset_index() 
added_df_chickpeas_yellow_peas.iloc[:, 0] = added_df_chickpeas_yellow_peas.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_chickpeas_yellow_peas.columns = ["metabolite", "flux"]
added_df_chickpeas_yellow_peas = pd.concat([skeleton_chickpeas_yellow_peas[["metabolite", "flux"]], added_df_chickpeas_yellow_peas])
added_df_couscous_pork = added_couscous_pork.reset_index() 
added_df_couscous_pork.iloc[:, 0] = added_df_couscous_pork.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_couscous_pork.columns = ["metabolite", "flux"]
added_df_couscous_pork = pd.concat([skeleton_couscous_pork[["metabolite", "flux"]], added_df_couscous_pork])
added_df_couscous_pumpkin = added_couscous_pumpkin.reset_index() 
added_df_couscous_pumpkin.iloc[:, 0] = added_df_couscous_pumpkin.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_couscous_pumpkin.columns = ["metabolite", "flux"]
added_df_couscous_pumpkin = pd.concat([skeleton_couscous_pumpkin[["metabolite", "flux"]], added_df_couscous_pumpkin])
added_df_pork_raspberries = added_pork_raspberries.reset_index() 
added_df_pork_raspberries.iloc[:, 0] = added_df_pork_raspberries.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_pork_raspberries.columns = ["metabolite", "flux"]
added_df_pork_raspberries = pd.concat([skeleton_pork_raspberries[["metabolite", "flux"]], added_df_pork_raspberries])
added_df_pumpkin_yellow_peas = added_pumpkin_yellow_peas.reset_index() 
added_df_pumpkin_yellow_peas.iloc[:, 0] = added_df_pumpkin_yellow_peas.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_pumpkin_yellow_peas.columns = ["metabolite", "flux"]
added_df_pumpkin_yellow_peas = pd.concat([skeleton_pumpkin_yellow_peas[["metabolite", "flux"]], added_df_pumpkin_yellow_peas])
added_df_formula_black_beans_blackcurrants = added_formula_black_beans_blackcurrants.reset_index() 
added_df_formula_black_beans_blackcurrants.iloc[:, 0] = added_df_formula_black_beans_blackcurrants.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_formula_black_beans_blackcurrants.columns = ["metabolite", "flux"]
added_df_formula_black_beans_blackcurrants = pd.concat([skeleton_formula_black_beans_blackcurrants[["metabolite", "flux"]], added_df_formula_black_beans_blackcurrants])
added_df_formula_black_beans_pumpkin = added_formula_black_beans_pumpkin.reset_index() 
added_df_formula_black_beans_pumpkin.iloc[:, 0] = added_df_formula_black_beans_pumpkin.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_formula_black_beans_pumpkin.columns = ["metabolite", "flux"]
added_df_formula_black_beans_pumpkin = pd.concat([skeleton_formula_black_beans_pumpkin[["metabolite", "flux"]], added_df_formula_black_beans_pumpkin])
added_df_formula_blackcurrants_kumara_with_skin = added_formula_blackcurrants_kumara_with_skin.reset_index() 
added_df_formula_blackcurrants_kumara_with_skin.iloc[:, 0] = added_df_formula_blackcurrants_kumara_with_skin.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_formula_blackcurrants_kumara_with_skin.columns = ["metabolite", "flux"]
added_df_formula_blackcurrants_kumara_with_skin = pd.concat([skeleton_formula_blackcurrants_kumara_with_skin[["metabolite", "flux"]], added_df_formula_blackcurrants_kumara_with_skin])
added_df_formula_blackcurrants_kumara_without_skin = added_formula_blackcurrants_kumara_without_skin.reset_index() 
added_df_formula_blackcurrants_kumara_without_skin.iloc[:, 0] = added_df_formula_blackcurrants_kumara_without_skin.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_formula_blackcurrants_kumara_without_skin.columns = ["metabolite", "flux"]
added_df_formula_blackcurrants_kumara_without_skin = pd.concat([skeleton_formula_blackcurrants_kumara_without_skin[["metabolite", "flux"]], added_df_formula_blackcurrants_kumara_without_skin])
added_df_formula_blackcurrants_pork = added_formula_blackcurrants_pork.reset_index() 
added_df_formula_blackcurrants_pork.iloc[:, 0] = added_df_formula_blackcurrants_pork.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_formula_blackcurrants_pork.columns = ["metabolite", "flux"]
added_df_formula_blackcurrants_pork = pd.concat([skeleton_formula_blackcurrants_pork[["metabolite", "flux"]], added_df_formula_blackcurrants_pork])
added_df_formula_blackcurrants_soybeans = added_formula_blackcurrants_soybeans.reset_index() 
added_df_formula_blackcurrants_soybeans.iloc[:, 0] = added_df_formula_blackcurrants_soybeans.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_formula_blackcurrants_soybeans.columns = ["metabolite", "flux"]
added_df_formula_blackcurrants_soybeans = pd.concat([skeleton_formula_blackcurrants_soybeans[["metabolite", "flux"]], added_df_formula_blackcurrants_soybeans])
added_df_formula_blackcurrants_strawberries = added_formula_blackcurrants_strawberries.reset_index() 
added_df_formula_blackcurrants_strawberries.iloc[:, 0] = added_df_formula_blackcurrants_strawberries.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_formula_blackcurrants_strawberries.columns = ["metabolite", "flux"]
added_df_formula_blackcurrants_strawberries = pd.concat([skeleton_formula_blackcurrants_strawberries[["metabolite", "flux"]], added_df_formula_blackcurrants_strawberries])
added_df_formula_chickpeas_pork = added_formula_chickpeas_pork.reset_index() 
added_df_formula_chickpeas_pork.iloc[:, 0] = added_df_formula_chickpeas_pork.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_formula_chickpeas_pork.columns = ["metabolite", "flux"]
added_df_formula_chickpeas_pork = pd.concat([skeleton_formula_chickpeas_pork[["metabolite", "flux"]], added_df_formula_chickpeas_pork])
added_df_formula_chickpeas_yellow_peas = added_formula_chickpeas_yellow_peas.reset_index() 
added_df_formula_chickpeas_yellow_peas.iloc[:, 0] = added_df_formula_chickpeas_yellow_peas.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_formula_chickpeas_yellow_peas.columns = ["metabolite", "flux"]
added_df_formula_chickpeas_yellow_peas = pd.concat([skeleton_formula_chickpeas_yellow_peas[["metabolite", "flux"]], added_df_formula_chickpeas_yellow_peas])
added_df_formula_couscous_pork = added_formula_couscous_pork.reset_index() 
added_df_formula_couscous_pork.iloc[:, 0] = added_df_formula_couscous_pork.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_formula_couscous_pork.columns = ["metabolite", "flux"]
added_df_formula_couscous_pork = pd.concat([skeleton_formula_couscous_pork[["metabolite", "flux"]], added_df_formula_couscous_pork])
added_df_formula_couscous_pumpkin = added_formula_couscous_pumpkin.reset_index() 
added_df_formula_couscous_pumpkin.iloc[:, 0] = added_df_formula_couscous_pumpkin.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_formula_couscous_pumpkin.columns = ["metabolite", "flux"]
added_df_formula_couscous_pumpkin = pd.concat([skeleton_formula_couscous_pumpkin[["metabolite", "flux"]], added_df_formula_couscous_pumpkin])
added_df_formula_pork_raspberries = added_formula_pork_raspberries.reset_index() 
added_df_formula_pork_raspberries.iloc[:, 0] = added_df_formula_pork_raspberries.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_formula_pork_raspberries.columns = ["metabolite", "flux"]
added_df_formula_pork_raspberries = pd.concat([skeleton_formula_pork_raspberries[["metabolite", "flux"]], added_df_formula_pork_raspberries])
added_df_formula_pumpkin_yellow_peas = added_formula_pumpkin_yellow_peas.reset_index() 
added_df_formula_pumpkin_yellow_peas.iloc[:, 0] = added_df_formula_pumpkin_yellow_peas.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_formula_pumpkin_yellow_peas.columns = ["metabolite", "flux"]
added_df_formula_pumpkin_yellow_peas = pd.concat([skeleton_formula_pumpkin_yellow_peas[["metabolite", "flux"]], added_df_formula_pumpkin_yellow_peas])

completed_black_beans = pd.merge(added_df_black_beans, annotations, on="metabolite", how="left")
completed_black_beans["reaction"] = "EX_" + completed_black_beans.metabolite + "_m"
completed_black_beans["global_id"] = "EX_" + completed_black_beans.metabolite + "(e)"
completed_blackcurrants = pd.merge(added_df_blackcurrants, annotations, on="metabolite", how="left")
completed_blackcurrants["reaction"] = "EX_" + completed_blackcurrants.metabolite + "_m"
completed_blackcurrants["global_id"] = "EX_" + completed_blackcurrants.metabolite + "(e)"
completed_chickpeas = pd.merge(added_df_chickpeas, annotations, on="metabolite", how="left")
completed_chickpeas["reaction"] = "EX_" + completed_chickpeas.metabolite + "_m"
completed_chickpeas["global_id"] = "EX_" + completed_chickpeas.metabolite + "(e)"
completed_couscous = pd.merge(added_df_couscous, annotations, on="metabolite", how="left")
completed_couscous["reaction"] = "EX_" + completed_couscous.metabolite + "_m"
completed_couscous["global_id"] = "EX_" + completed_couscous.metabolite + "(e)"
completed_infant_formula = pd.merge(added_df_infant_formula, annotations, on="metabolite", how="left")
completed_infant_formula["reaction"] = "EX_" + completed_infant_formula.metabolite + "_m"
completed_infant_formula["global_id"] = "EX_" + completed_infant_formula.metabolite + "(e)"
completed_kumara_with_skin = pd.merge(added_df_kumara_with_skin, annotations, on="metabolite", how="left")
completed_kumara_with_skin["reaction"] = "EX_" + completed_kumara_with_skin.metabolite + "_m"
completed_kumara_with_skin["global_id"] = "EX_" + completed_kumara_with_skin.metabolite + "(e)"
completed_kumara_without_skin = pd.merge(added_df_kumara_without_skin, annotations, on="metabolite", how="left")
completed_kumara_without_skin["reaction"] = "EX_" + completed_kumara_without_skin.metabolite + "_m"
completed_kumara_without_skin["global_id"] = "EX_" + completed_kumara_without_skin.metabolite + "(e)"
completed_pork = pd.merge(added_df_pork, annotations, on="metabolite", how="left")
completed_pork["reaction"] = "EX_" + completed_pork.metabolite + "_m"
completed_pork["global_id"] = "EX_" + completed_pork.metabolite + "(e)"
completed_prawn = pd.merge(added_df_prawn, annotations, on="metabolite", how="left")
completed_prawn["reaction"] = "EX_" + completed_prawn.metabolite + "_m"
completed_prawn["global_id"] = "EX_" + completed_prawn.metabolite + "(e)"
completed_pumpkin = pd.merge(added_df_pumpkin, annotations, on="metabolite", how="left")
completed_pumpkin["reaction"] = "EX_" + completed_pumpkin.metabolite + "_m"
completed_pumpkin["global_id"] = "EX_" + completed_pumpkin.metabolite + "(e)"
completed_raspberries = pd.merge(added_df_raspberries, annotations, on="metabolite", how="left")
completed_raspberries["reaction"] = "EX_" + completed_raspberries.metabolite + "_m"
completed_raspberries["global_id"] = "EX_" + completed_raspberries.metabolite + "(e)"
completed_soybeans = pd.merge(added_df_soybeans, annotations, on="metabolite", how="left")
completed_soybeans["reaction"] = "EX_" + completed_soybeans.metabolite + "_m"
completed_soybeans["global_id"] = "EX_" + completed_soybeans.metabolite + "(e)"
completed_strawberries = pd.merge(added_df_strawberries, annotations, on="metabolite", how="left")
completed_strawberries["reaction"] = "EX_" + completed_strawberries.metabolite + "_m"
completed_strawberries["global_id"] = "EX_" + completed_strawberries.metabolite + "(e)"
completed_yellow_peas = pd.merge(added_df_yellow_peas, annotations, on="metabolite", how="left")
completed_yellow_peas["reaction"] = "EX_" + completed_yellow_peas.metabolite + "_m"
completed_yellow_peas["global_id"] = "EX_" + completed_yellow_peas.metabolite + "(e)"
completed_formula_black_beans = pd.merge(added_df_formula_black_beans, annotations, on="metabolite", how="left")
completed_formula_black_beans["reaction"] = "EX_" + completed_formula_black_beans.metabolite + "_m"
completed_formula_black_beans["global_id"] = "EX_" + completed_formula_black_beans.metabolite + "(e)"
completed_formula_blackcurrants = pd.merge(added_df_formula_blackcurrants, annotations, on="metabolite", how="left")
completed_formula_blackcurrants["reaction"] = "EX_" + completed_formula_blackcurrants.metabolite + "_m"
completed_formula_blackcurrants["global_id"] = "EX_" + completed_formula_blackcurrants.metabolite + "(e)"
completed_formula_chickpeas = pd.merge(added_df_formula_chickpeas, annotations, on="metabolite", how="left")
completed_formula_chickpeas["reaction"] = "EX_" + completed_formula_chickpeas.metabolite + "_m"
completed_formula_chickpeas["global_id"] = "EX_" + completed_formula_chickpeas.metabolite + "(e)"
completed_formula_couscous = pd.merge(added_df_formula_couscous, annotations, on="metabolite", how="left")
completed_formula_couscous["reaction"] = "EX_" + completed_formula_couscous.metabolite + "_m"
completed_formula_couscous["global_id"] = "EX_" + completed_formula_couscous.metabolite + "(e)"
completed_formula_kumara_with_skin = pd.merge(added_df_formula_kumara_with_skin, annotations, on="metabolite", how="left")
completed_formula_kumara_with_skin["reaction"] = "EX_" + completed_formula_kumara_with_skin.metabolite + "_m"
completed_formula_kumara_with_skin["global_id"] = "EX_" + completed_formula_kumara_with_skin.metabolite + "(e)"
completed_formula_kumara_without_skin = pd.merge(added_df_formula_kumara_without_skin, annotations, on="metabolite", how="left")
completed_formula_kumara_without_skin["reaction"] = "EX_" + completed_formula_kumara_without_skin.metabolite + "_m"
completed_formula_kumara_without_skin["global_id"] = "EX_" + completed_formula_kumara_without_skin.metabolite + "(e)"
completed_formula_pork = pd.merge(added_df_formula_pork, annotations, on="metabolite", how="left")
completed_formula_pork["reaction"] = "EX_" + completed_formula_pork.metabolite + "_m"
completed_formula_pork["global_id"] = "EX_" + completed_formula_pork.metabolite + "(e)"
completed_formula_prawn = pd.merge(added_df_formula_prawn, annotations, on="metabolite", how="left")
completed_formula_prawn["reaction"] = "EX_" + completed_formula_prawn.metabolite + "_m"
completed_formula_prawn["global_id"] = "EX_" + completed_formula_prawn.metabolite + "(e)"
completed_formula_pumpkin = pd.merge(added_df_formula_pumpkin, annotations, on="metabolite", how="left")
completed_formula_pumpkin["reaction"] = "EX_" + completed_formula_pumpkin.metabolite + "_m"
completed_formula_pumpkin["global_id"] = "EX_" + completed_formula_pumpkin.metabolite + "(e)"
completed_formula_raspberries = pd.merge(added_df_formula_raspberries, annotations, on="metabolite", how="left")
completed_formula_raspberries["reaction"] = "EX_" + completed_formula_raspberries.metabolite + "_m"
completed_formula_raspberries["global_id"] = "EX_" + completed_formula_raspberries.metabolite + "(e)"
completed_formula_soybeans = pd.merge(added_df_formula_soybeans, annotations, on="metabolite", how="left")
completed_formula_soybeans["reaction"] = "EX_" + completed_formula_soybeans.metabolite + "_m"
completed_formula_soybeans["global_id"] = "EX_" + completed_formula_soybeans.metabolite + "(e)"
completed_formula_strawberries = pd.merge(added_df_formula_strawberries, annotations, on="metabolite", how="left")
completed_formula_strawberries["reaction"] = "EX_" + completed_formula_strawberries.metabolite + "_m"
completed_formula_strawberries["global_id"] = "EX_" + completed_formula_strawberries.metabolite + "(e)"
completed_formula_yellow_peas = pd.merge(added_df_formula_yellow_peas, annotations, on="metabolite", how="left")
completed_formula_yellow_peas["reaction"] = "EX_" + completed_formula_yellow_peas.metabolite + "_m"
completed_formula_yellow_peas["global_id"] = "EX_" + completed_formula_yellow_peas.metabolite + "(e)"
completed_black_beans_blackcurrants = pd.merge(added_df_black_beans_blackcurrants, annotations, on="metabolite", how="left")
completed_black_beans_blackcurrants["reaction"] = "EX_" + completed_black_beans_blackcurrants.metabolite + "_m"
completed_black_beans_blackcurrants["global_id"] = "EX_" + completed_black_beans_blackcurrants.metabolite + "(e)"
completed_black_beans_pumpkin = pd.merge(added_df_black_beans_pumpkin, annotations, on="metabolite", how="left")
completed_black_beans_pumpkin["reaction"] = "EX_" + completed_black_beans_pumpkin.metabolite + "_m"
completed_black_beans_pumpkin["global_id"] = "EX_" + completed_black_beans_pumpkin.metabolite + "(e)"
completed_blackcurrants_kumara_with_skin = pd.merge(added_df_blackcurrants_kumara_with_skin, annotations, on="metabolite", how="left")
completed_blackcurrants_kumara_with_skin["reaction"] = "EX_" + completed_blackcurrants_kumara_with_skin.metabolite + "_m"
completed_blackcurrants_kumara_with_skin["global_id"] = "EX_" + completed_blackcurrants_kumara_with_skin.metabolite + "(e)"
completed_blackcurrants_kumara_without_skin = pd.merge(added_df_blackcurrants_kumara_without_skin, annotations, on="metabolite", how="left")
completed_blackcurrants_kumara_without_skin["reaction"] = "EX_" + completed_blackcurrants_kumara_without_skin.metabolite + "_m"
completed_blackcurrants_kumara_without_skin["global_id"] = "EX_" + completed_blackcurrants_kumara_without_skin.metabolite + "(e)"
completed_blackcurrants_pork = pd.merge(added_df_blackcurrants_pork, annotations, on="metabolite", how="left")
completed_blackcurrants_pork["reaction"] = "EX_" + completed_blackcurrants_pork.metabolite + "_m"
completed_blackcurrants_pork["global_id"] = "EX_" + completed_blackcurrants_pork.metabolite + "(e)"
completed_blackcurrants_soybeans = pd.merge(added_df_blackcurrants_soybeans, annotations, on="metabolite", how="left")
completed_blackcurrants_soybeans["reaction"] = "EX_" + completed_blackcurrants_soybeans.metabolite + "_m"
completed_blackcurrants_soybeans["global_id"] = "EX_" + completed_blackcurrants_soybeans.metabolite + "(e)"
completed_blackcurrants_strawberries = pd.merge(added_df_blackcurrants_strawberries, annotations, on="metabolite", how="left")
completed_blackcurrants_strawberries["reaction"] = "EX_" + completed_blackcurrants_strawberries.metabolite + "_m"
completed_blackcurrants_strawberries["global_id"] = "EX_" + completed_blackcurrants_strawberries.metabolite + "(e)"
completed_chickpeas_pork = pd.merge(added_df_chickpeas_pork, annotations, on="metabolite", how="left")
completed_chickpeas_pork["reaction"] = "EX_" + completed_chickpeas_pork.metabolite + "_m"
completed_chickpeas_pork["global_id"] = "EX_" + completed_chickpeas_pork.metabolite + "(e)"
completed_chickpeas_yellow_peas = pd.merge(added_df_chickpeas_yellow_peas, annotations, on="metabolite", how="left")
completed_chickpeas_yellow_peas["reaction"] = "EX_" + completed_chickpeas_yellow_peas.metabolite + "_m"
completed_chickpeas_yellow_peas["global_id"] = "EX_" + completed_chickpeas_yellow_peas.metabolite + "(e)"
completed_couscous_pork = pd.merge(added_df_couscous_pork, annotations, on="metabolite", how="left")
completed_couscous_pork["reaction"] = "EX_" + completed_couscous_pork.metabolite + "_m"
completed_couscous_pork["global_id"] = "EX_" + completed_couscous_pork.metabolite + "(e)"
completed_couscous_pumpkin = pd.merge(added_df_couscous_pumpkin, annotations, on="metabolite", how="left")
completed_couscous_pumpkin["reaction"] = "EX_" + completed_couscous_pumpkin.metabolite + "_m"
completed_couscous_pumpkin["global_id"] = "EX_" + completed_couscous_pumpkin.metabolite + "(e)"
completed_pork_raspberries = pd.merge(added_df_pork_raspberries, annotations, on="metabolite", how="left")
completed_pork_raspberries["reaction"] = "EX_" + completed_pork_raspberries.metabolite + "_m"
completed_pork_raspberries["global_id"] = "EX_" + completed_pork_raspberries.metabolite + "(e)"
completed_pumpkin_yellow_peas = pd.merge(added_df_pumpkin_yellow_peas, annotations, on="metabolite", how="left")
completed_pumpkin_yellow_peas["reaction"] = "EX_" + completed_pumpkin_yellow_peas.metabolite + "_m"
completed_pumpkin_yellow_peas["global_id"] = "EX_" + completed_pumpkin_yellow_peas.metabolite + "(e)"
completed_formula_black_beans_blackcurrants = pd.merge(added_df_formula_black_beans_blackcurrants, annotations, on="metabolite", how="left")
completed_formula_black_beans_blackcurrants["reaction"] = "EX_" + completed_formula_black_beans_blackcurrants.metabolite + "_m"
completed_formula_black_beans_blackcurrants["global_id"] = "EX_" + completed_formula_black_beans_blackcurrants.metabolite + "(e)"
completed_formula_black_beans_pumpkin = pd.merge(added_df_formula_black_beans_pumpkin, annotations, on="metabolite", how="left")
completed_formula_black_beans_pumpkin["reaction"] = "EX_" + completed_formula_black_beans_pumpkin.metabolite + "_m"
completed_formula_black_beans_pumpkin["global_id"] = "EX_" + completed_formula_black_beans_pumpkin.metabolite + "(e)"
completed_formula_blackcurrants_kumara_with_skin = pd.merge(added_df_formula_blackcurrants_kumara_with_skin, annotations, on="metabolite", how="left")
completed_formula_blackcurrants_kumara_with_skin["reaction"] = "EX_" + completed_formula_blackcurrants_kumara_with_skin.metabolite + "_m"
completed_formula_blackcurrants_kumara_with_skin["global_id"] = "EX_" + completed_formula_blackcurrants_kumara_with_skin.metabolite + "(e)"
completed_formula_blackcurrants_kumara_without_skin = pd.merge(added_df_formula_blackcurrants_kumara_without_skin, annotations, on="metabolite", how="left")
completed_formula_blackcurrants_kumara_without_skin["reaction"] = "EX_" + completed_formula_blackcurrants_kumara_without_skin.metabolite + "_m"
completed_formula_blackcurrants_kumara_without_skin["global_id"] = "EX_" + completed_formula_blackcurrants_kumara_without_skin.metabolite + "(e)"
completed_formula_blackcurrants_pork = pd.merge(added_df_formula_blackcurrants_pork, annotations, on="metabolite", how="left")
completed_formula_blackcurrants_pork["reaction"] = "EX_" + completed_formula_blackcurrants_pork.metabolite + "_m"
completed_formula_blackcurrants_pork["global_id"] = "EX_" + completed_formula_blackcurrants_pork.metabolite + "(e)"
completed_formula_blackcurrants_soybeans = pd.merge(added_df_formula_blackcurrants_soybeans, annotations, on="metabolite", how="left")
completed_formula_blackcurrants_soybeans["reaction"] = "EX_" + completed_formula_blackcurrants_soybeans.metabolite + "_m"
completed_formula_blackcurrants_soybeans["global_id"] = "EX_" + completed_formula_blackcurrants_soybeans.metabolite + "(e)"
completed_formula_blackcurrants_strawberries = pd.merge(added_df_formula_blackcurrants_strawberries, annotations, on="metabolite", how="left")
completed_formula_blackcurrants_strawberries["reaction"] = "EX_" + completed_formula_blackcurrants_strawberries.metabolite + "_m"
completed_formula_blackcurrants_strawberries["global_id"] = "EX_" + completed_formula_blackcurrants_strawberries.metabolite + "(e)"
completed_formula_chickpeas_pork = pd.merge(added_df_formula_chickpeas_pork, annotations, on="metabolite", how="left")
completed_formula_chickpeas_pork["reaction"] = "EX_" + completed_formula_chickpeas_pork.metabolite + "_m"
completed_formula_chickpeas_pork["global_id"] = "EX_" + completed_formula_chickpeas_pork.metabolite + "(e)"
completed_formula_chickpeas_yellow_peas = pd.merge(added_df_formula_chickpeas_yellow_peas, annotations, on="metabolite", how="left")
completed_formula_chickpeas_yellow_peas["reaction"] = "EX_" + completed_formula_chickpeas_yellow_peas.metabolite + "_m"
completed_formula_chickpeas_yellow_peas["global_id"] = "EX_" + completed_formula_chickpeas_yellow_peas.metabolite + "(e)"
completed_formula_couscous_pork = pd.merge(added_df_formula_couscous_pork, annotations, on="metabolite", how="left")
completed_formula_couscous_pork["reaction"] = "EX_" + completed_formula_couscous_pork.metabolite + "_m"
completed_formula_couscous_pork["global_id"] = "EX_" + completed_formula_couscous_pork.metabolite + "(e)"
completed_formula_couscous_pumpkin = pd.merge(added_df_formula_couscous_pumpkin, annotations, on="metabolite", how="left")
completed_formula_couscous_pumpkin["reaction"] = "EX_" + completed_formula_couscous_pumpkin.metabolite + "_m"
completed_formula_couscous_pumpkin["global_id"] = "EX_" + completed_formula_couscous_pumpkin.metabolite + "(e)"
completed_formula_pork_raspberries = pd.merge(added_df_formula_pork_raspberries, annotations, on="metabolite", how="left")
completed_formula_pork_raspberries["reaction"] = "EX_" + completed_formula_pork_raspberries.metabolite + "_m"
completed_formula_pork_raspberries["global_id"] = "EX_" + completed_formula_pork_raspberries.metabolite + "(e)"
completed_formula_pumpkin_yellow_peas = pd.merge(added_df_formula_pumpkin_yellow_peas, annotations, on="metabolite", how="left")
completed_formula_pumpkin_yellow_peas["reaction"] = "EX_" + completed_formula_pumpkin_yellow_peas.metabolite + "_m"
completed_formula_pumpkin_yellow_peas["global_id"] = "EX_" + completed_formula_pumpkin_yellow_peas.metabolite + "(e)"

#Saving the medium
completed_black_beans.to_csv("media/black_beans.csv") 
completed_blackcurrants.to_csv("media/blackcurrants.csv") 
completed_chickpeas.to_csv("media/chickpeas.csv") 
completed_couscous.to_csv("media/couscous.csv") 
completed_infant_formula.to_csv("media/infant_formula.csv") 
completed_kumara_with_skin.to_csv("media/kumara_with_skin.csv") 
completed_kumara_without_skin.to_csv("media/kumara_without_skin.csv") 
completed_pork.to_csv("media/pork.csv") 
completed_prawn.to_csv("media/prawn.csv") 
completed_pumpkin.to_csv("media/pumpkin.csv") 
completed_raspberries.to_csv("media/raspberries.csv") 
completed_soybeans.to_csv("media/soybeans.csv") 
completed_strawberries.to_csv("media/strawberries.csv") 
completed_yellow_peas.to_csv("media/yellow_peas.csv") 
completed_formula_black_beans.to_csv("media/formula_black_beans.csv") 
completed_formula_blackcurrants.to_csv("media/formula_blackcurrants.csv") 
completed_formula_chickpeas.to_csv("media/formula_chickpeas.csv") 
completed_formula_couscous.to_csv("media/formula_couscous.csv") 
completed_formula_kumara_with_skin.to_csv("media/formula_kumara_with_skin.csv") 
completed_formula_kumara_without_skin.to_csv("media/formula_kumara_without_skin.csv") 
completed_formula_pork.to_csv("media/formula_pork.csv") 
completed_formula_prawn.to_csv("media/formula_prawn.csv") 
completed_formula_pumpkin.to_csv("media/formula_pumpkin.csv") 
completed_formula_raspberries.to_csv("media/formula_raspberries.csv") 
completed_formula_soybeans.to_csv("media/formula_soybeans.csv") 
completed_formula_strawberries.to_csv("media/formula_strawberries.csv") 
completed_formula_yellow_peas.to_csv("media/formula_yellow_peas.csv") 
completed_black_beans_blackcurrants.to_csv("media/black_beans_blackcurrants.csv") 
completed_black_beans_pumpkin.to_csv("media/black_beans_pumpkin.csv") 
completed_blackcurrants_kumara_with_skin.to_csv("media/blackcurrants_kumara_with_skin.csv") 
completed_blackcurrants_kumara_without_skin.to_csv("media/blackcurrants_kumara_without_skin.csv") 
completed_blackcurrants_pork.to_csv("media/blackcurrants_pork.csv") 
completed_blackcurrants_soybeans.to_csv("media/blackcurrants_soybeans.csv") 
completed_blackcurrants_strawberries.to_csv("media/blackcurrants_strawberries.csv") 
completed_chickpeas_pork.to_csv("media/chickpeas_pork.csv") 
completed_chickpeas_yellow_peas.to_csv("media/chickpeas_yellow_peas.csv") 
completed_couscous_pork.to_csv("media/couscous_pork.csv") 
completed_couscous_pumpkin.to_csv("media/couscous_pumpkin.csv") 
completed_pork_raspberries.to_csv("media/pork_raspberries.csv") 
completed_pumpkin_yellow_peas.to_csv("media/pumpkin_yellow_peas.csv") 
completed_formula_black_beans_blackcurrants.to_csv("media/formula_black_beans_blackcurrants.csv") 
completed_formula_black_beans_pumpkin.to_csv("media/formula_black_beans_pumpkin.csv") 
completed_formula_blackcurrants_kumara_with_skin.to_csv("media/formula_blackcurrants_kumara_with_skin.csv") 
completed_formula_blackcurrants_kumara_without_skin.to_csv("media/formula_blackcurrants_kumara_without_skin.csv") 
completed_formula_blackcurrants_pork.to_csv("media/formula_blackcurrants_pork.csv") 
completed_formula_blackcurrants_soybeans.to_csv("media/formula_blackcurrants_soybeans.csv") 
completed_formula_blackcurrants_strawberries.to_csv("media/formula_blackcurrants_strawberries.csv") 
completed_formula_chickpeas_pork.to_csv("media/formula_chickpeas_pork.csv") 
completed_formula_chickpeas_yellow_peas.to_csv("media/formula_chickpeas_yellow_peas.csv") 
completed_formula_couscous_pork.to_csv("media/formula_couscous_pork.csv") 
completed_formula_couscous_pumpkin.to_csv("media/formula_couscous_pumpkin.csv") 
completed_formula_pork_raspberries.to_csv("media/formula_pork_raspberries.csv") 
completed_formula_pumpkin_yellow_peas.to_csv("media/formula_pumpkin_yellow_peas.csv") 

#importing medium
import pandas as pd

completed_black_beans = pd.read_csv("media/black_beans.csv") 
completed_blackcurrants = pd.read_csv("media/blackcurrants.csv") 
completed_chickpeas = pd.read_csv("media/chickpeas.csv") 
completed_couscous = pd.read_csv("media/couscous.csv") 
completed_infant_formula = pd.read_csv("media/infant_formula.csv") 
completed_kumara_with_skin = pd.read_csv("media/kumara_with_skin.csv") 
completed_kumara_without_skin = pd.read_csv("media/kumara_without_skin.csv") 
completed_pork = pd.read_csv("media/pork.csv") 
completed_prawn = pd.read_csv("media/prawn.csv") 
completed_pumpkin = pd.read_csv("media/pumpkin.csv") 
completed_raspberries = pd.read_csv("media/raspberries.csv") 
completed_soybeans = pd.read_csv("media/soybeans.csv") 
completed_strawberries = pd.read_csv("media/strawberries.csv") 
completed_yellow_peas = pd.read_csv("media/yellow_peas.csv") 
completed_formula_black_beans = pd.read_csv("media/formula_black_beans.csv") 
completed_formula_blackcurrants = pd.read_csv("media/formula_blackcurrants.csv") 
completed_formula_chickpeas = pd.read_csv("media/formula_chickpeas.csv") 
completed_formula_couscous = pd.read_csv("media/formula_couscous.csv") 
completed_formula_kumara_with_skin = pd.read_csv("media/formula_kumara_with_skin.csv") 
completed_formula_kumara_without_skin = pd.read_csv("media/formula_kumara_without_skin.csv") 
completed_formula_pork = pd.read_csv("media/formula_pork.csv") 
completed_formula_prawn = pd.read_csv("media/formula_prawn.csv") 
completed_formula_pumpkin = pd.read_csv("media/formula_pumpkin.csv") 
completed_formula_raspberries = pd.read_csv("media/formula_raspberries.csv") 
completed_formula_soybeans = pd.read_csv("media/formula_soybeans.csv") 
completed_formula_strawberries = pd.read_csv("media/formula_strawberries.csv") 
completed_formula_yellow_peas = pd.read_csv("media/formula_yellow_peas.csv") 
completed_black_beans_blackcurrants = pd.read_csv("media/black_beans_blackcurrants.csv") 
completed_black_beans_pumpkin = pd.read_csv("media/black_beans_pumpkin.csv") 
completed_blackcurrants_kumara_with_skin = pd.read_csv("media/blackcurrants_kumara_with_skin.csv") 
completed_blackcurrants_kumara_without_skin = pd.read_csv("media/blackcurrants_kumara_without_skin.csv") 
completed_blackcurrants_pork = pd.read_csv("media/blackcurrants_pork.csv") 
completed_blackcurrants_soybeans = pd.read_csv("media/blackcurrants_soybeans.csv") 
completed_blackcurrants_strawberries = pd.read_csv("media/blackcurrants_strawberries.csv") 
completed_chickpeas_pork = pd.read_csv("media/chickpeas_pork.csv") 
completed_chickpeas_yellow_peas = pd.read_csv("media/chickpeas_yellow_peas.csv") 
completed_couscous_pork = pd.read_csv("media/couscous_pork.csv") 
completed_couscous_pumpkin = pd.read_csv("media/couscous_pumpkin.csv") 
completed_pork_raspberries = pd.read_csv("media/pork_raspberries.csv") 
completed_pumpkin_yellow_peas = pd.read_csv("media/pumpkin_yellow_peas.csv") 
completed_formula_black_beans_blackcurrants = pd.read_csv("media/formula_black_beans_blackcurrants.csv") 
completed_formula_black_beans_pumpkin = pd.read_csv("media/formula_black_beans_pumpkin.csv") 
completed_formula_blackcurrants_kumara_with_skin = pd.read_csv("media/formula_blackcurrants_kumara_with_skin.csv") 
completed_formula_blackcurrants_kumara_without_skin = pd.read_csv("media/formula_blackcurrants_kumara_without_skin.csv") 
completed_formula_blackcurrants_pork = pd.read_csv("media/formula_blackcurrants_pork.csv") 
completed_formula_blackcurrants_soybeans = pd.read_csv("media/formula_blackcurrants_soybeans.csv") 
completed_formula_blackcurrants_strawberries = pd.read_csv("media/formula_blackcurrants_strawberries.csv") 
completed_formula_chickpeas_pork = pd.read_csv("media/formula_chickpeas_pork.csv") 
completed_formula_chickpeas_yellow_peas = pd.read_csv("media/formula_chickpeas_yellow_peas.csv") 
completed_formula_couscous_pork = pd.read_csv("media/formula_couscous_pork.csv") 
completed_formula_couscous_pumpkin = pd.read_csv("media/formula_couscous_pumpkin.csv") 
completed_formula_pork_raspberries = pd.read_csv("media/formula_pork_raspberries.csv") 
completed_formula_pumpkin_yellow_peas = pd.read_csv("media/formula_pumpkin_yellow_peas.csv") 

#Checking the medium
from micom.workflows.db_media import check_db_medium

check_black_beans = check_db_medium("data/agora201_genus.qza", medium=completed_black_beans, threads=14)
check_blackcurrants = check_db_medium("data/agora201_genus.qza", medium=completed_blackcurrants, threads=14)
check_chickpeas = check_db_medium("data/agora201_genus.qza", medium=completed_chickpeas, threads=14)
check_couscous = check_db_medium("data/agora201_genus.qza", medium=completed_couscous, threads=14)
check_infant_formula = check_db_medium("data/agora201_genus.qza", medium=completed_infant_formula, threads=14)
check_kumara_with_skin = check_db_medium("data/agora201_genus.qza", medium=completed_kumara_with_skin, threads=14)
check_kumara_without_skin = check_db_medium("data/agora201_genus.qza", medium=completed_kumara_without_skin, threads=14)
check_pork = check_db_medium("data/agora201_genus.qza", medium=completed_pork, threads=14)
check_prawn = check_db_medium("data/agora201_genus.qza", medium=completed_prawn, threads=14)
check_pumpkin = check_db_medium("data/agora201_genus.qza", medium=completed_pumpkin, threads=14)
check_raspberries = check_db_medium("data/agora201_genus.qza", medium=completed_raspberries, threads=14)
check_soybeans = check_db_medium("data/agora201_genus.qza", medium=completed_soybeans, threads=14)
check_strawberries = check_db_medium("data/agora201_genus.qza", medium=completed_strawberries, threads=14)
check_yellow_peas = check_db_medium("data/agora201_genus.qza", medium=completed_yellow_peas, threads=14)
check_formula_black_beans = check_db_medium("data/agora201_genus.qza", medium=completed_formula_black_beans, threads=14)
check_formula_blackcurrants = check_db_medium("data/agora201_genus.qza", medium=completed_formula_blackcurrants, threads=14)
check_formula_chickpeas = check_db_medium("data/agora201_genus.qza", medium=completed_formula_chickpeas, threads=14)
check_formula_couscous = check_db_medium("data/agora201_genus.qza", medium=completed_formula_couscous, threads=14)
check_formula_kumara_with_skin = check_db_medium("data/agora201_genus.qza", medium=completed_formula_kumara_with_skin, threads=14)
check_formula_kumara_without_skin = check_db_medium("data/agora201_genus.qza", medium=completed_formula_kumara_without_skin, threads=14)
check_formula_pork = check_db_medium("data/agora201_genus.qza", medium=completed_formula_pork, threads=14)
check_formula_prawn = check_db_medium("data/agora201_genus.qza", medium=completed_formula_prawn, threads=14)
check_formula_pumpkin = check_db_medium("data/agora201_genus.qza", medium=completed_formula_pumpkin, threads=14)
check_formula_raspberries = check_db_medium("data/agora201_genus.qza", medium=completed_formula_raspberries, threads=14)
check_formula_soybeans = check_db_medium("data/agora201_genus.qza", medium=completed_formula_soybeans, threads=14)
check_formula_strawberries = check_db_medium("data/agora201_genus.qza", medium=completed_formula_strawberries, threads=14)
check_formula_yellow_peas = check_db_medium("data/agora201_genus.qza", medium=completed_formula_yellow_peas, threads=14)
check_black_beans_blackcurrants = check_db_medium("data/agora201_genus.qza", medium=completed_black_beans_blackcurrants, threads=14)
check_black_beans_pumpkin = check_db_medium("data/agora201_genus.qza", medium=completed_black_beans_pumpkin, threads=14)
check_blackcurrants_kumara_with_skin = check_db_medium("data/agora201_genus.qza", medium=completed_blackcurrants_kumara_with_skin, threads=14)
check_blackcurrants_kumara_without_skin = check_db_medium("data/agora201_genus.qza", medium=completed_blackcurrants_kumara_without_skin, threads=14)
check_blackcurrants_pork = check_db_medium("data/agora201_genus.qza", medium=completed_blackcurrants_pork, threads=14)
check_blackcurrants_soybeans = check_db_medium("data/agora201_genus.qza", medium=completed_blackcurrants_soybeans, threads=14)
check_blackcurrants_strawberries = check_db_medium("data/agora201_genus.qza", medium=completed_blackcurrants_strawberries, threads=14)
check_chickpeas_pork = check_db_medium("data/agora201_genus.qza", medium=completed_chickpeas_pork, threads=14)
check_chickpeas_yellow_peas = check_db_medium("data/agora201_genus.qza", medium=completed_chickpeas_yellow_peas, threads=14)
check_couscous_pork = check_db_medium("data/agora201_genus.qza", medium=completed_couscous_pork, threads=14)
check_couscous_pumpkin = check_db_medium("data/agora201_genus.qza", medium=completed_couscous_pumpkin, threads=14)
check_pork_raspberries = check_db_medium("data/agora201_genus.qza", medium=completed_pork_raspberries, threads=14)
check_pumpkin_yellow_peas = check_db_medium("data/agora201_genus.qza", medium=completed_pumpkin_yellow_peas, threads=14)
check_formula_black_beans_blackcurrants = check_db_medium("data/agora201_genus.qza", medium=completed_formula_black_beans_blackcurrants, threads=14)
check_formula_black_beans_pumpkin = check_db_medium("data/agora201_genus.qza", medium=completed_formula_black_beans_pumpkin, threads=14)
check_formula_blackcurrants_kumara_with_skin = check_db_medium("data/agora201_genus.qza", medium=completed_formula_blackcurrants_kumara_with_skin, threads=14)
check_formula_blackcurrants_kumara_without_skin = check_db_medium("data/agora201_genus.qza", medium=completed_formula_blackcurrants_kumara_without_skin, threads=14)
check_formula_blackcurrants_pork = check_db_medium("data/agora201_genus.qza", medium=completed_formula_blackcurrants_pork, threads=14)
check_formula_blackcurrants_soybeans = check_db_medium("data/agora201_genus.qza", medium=completed_formula_blackcurrants_soybeans, threads=14)
check_formula_blackcurrants_strawberries = check_db_medium("data/agora201_genus.qza", medium=completed_formula_blackcurrants_strawberries, threads=14)
check_formula_chickpeas_pork = check_db_medium("data/agora201_genus.qza", medium=completed_formula_chickpeas_pork, threads=14)
check_formula_chickpeas_yellow_peas = check_db_medium("data/agora201_genus.qza", medium=completed_formula_chickpeas_yellow_peas, threads=14)
check_formula_couscous_pork = check_db_medium("data/agora201_genus.qza", medium=completed_formula_couscous_pork, threads=14)
check_formula_couscous_pumpkin = check_db_medium("data/agora201_genus.qza", medium=completed_formula_couscous_pumpkin, threads=14)
check_formula_pork_raspberries = check_db_medium("data/agora201_genus.qza", medium=completed_formula_pork_raspberries, threads=14)
check_formula_pumpkin_yellow_peas = check_db_medium("data/agora201_genus.qza", medium=completed_formula_pumpkin_yellow_peas, threads=14)

check_black_beans.growth_rate.describe()
check_blackcurrants.growth_rate.describe()
check_chickpeas.growth_rate.describe()
check_couscous.growth_rate.describe()
check_infant_formula.growth_rate.describe()
check_kumara_with_skin.growth_rate.describe()
check_kumara_without_skin.growth_rate.describe()
check_pork.growth_rate.describe()
check_prawn.growth_rate.describe()
check_pumpkin.growth_rate.describe()
check_raspberries.growth_rate.describe()
check_soybeans.growth_rate.describe()
check_strawberries.growth_rate.describe()
check_yellow_peas.growth_rate.describe()
check_formula_black_beans.growth_rate.describe()
check_formula_blackcurrants.growth_rate.describe()
check_formula_chickpeas.growth_rate.describe()
check_formula_couscous.growth_rate.describe()
check_formula_kumara_with_skin.growth_rate.describe()
check_formula_kumara_without_skin.growth_rate.describe()
check_formula_pork.growth_rate.describe()
check_formula_prawn.growth_rate.describe()
check_formula_pumpkin.growth_rate.describe()
check_formula_raspberries.growth_rate.describe()
check_formula_soybeans.growth_rate.describe()
check_formula_strawberries.growth_rate.describe()
check_formula_yellow_peas.growth_rate.describe()
check_black_beans_blackcurrants.growth_rate.describe()
check_black_beans_pumpkin.growth_rate.describe()
check_blackcurrants_kumara_with_skin.growth_rate.describe()
check_blackcurrants_kumara_without_skin.growth_rate.describe()
check_blackcurrants_pork.growth_rate.describe()
check_blackcurrants_soybeans.growth_rate.describe()
check_blackcurrants_strawberries.growth_rate.describe()
check_chickpeas_pork.growth_rate.describe()
check_chickpeas_yellow_peas.growth_rate.describe()
check_couscous_pork.growth_rate.describe()
check_couscous_pumpkin.growth_rate.describe()
check_pork_raspberries.growth_rate.describe()
check_pumpkin_yellow_peas.growth_rate.describe()
check_formula_black_beans_blackcurrants.growth_rate.describe()
check_formula_black_beans_pumpkin.growth_rate.describe()
check_formula_blackcurrants_kumara_with_skin.growth_rate.describe()
check_formula_blackcurrants_kumara_without_skin.growth_rate.describe()
check_formula_blackcurrants_pork.growth_rate.describe()
check_formula_blackcurrants_soybeans.growth_rate.describe()
check_formula_blackcurrants_strawberries.growth_rate.describe()
check_formula_chickpeas_pork.growth_rate.describe()
check_formula_chickpeas_yellow_peas.growth_rate.describe()
check_formula_couscous_pork.growth_rate.describe()
check_formula_couscous_pumpkin.growth_rate.describe()
check_formula_pork_raspberries.growth_rate.describe()
check_formula_pumpkin_yellow_peas.growth_rate.describe()