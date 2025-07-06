##Diets for NZ infants (6-12 months old)

#6 months = 7.15% food1 + 7.15% food2 + 85% breatsmilk (608 kcal/d)
#AGORA2

#04/08/23

#Importing the dietary fluxes and converting then
import pandas as pd

diet_Blackbeans_Blackcurrant = pd.read_csv("data/Blackbeans_Blackcurrant.tsv", sep="\t", header=None) #importing fluxes
diet_Blackbeans_Blackcurrant.columns = ["reaction", "flux"] #changing the name of the columns
diet_Blackbeans_Chickpea = pd.read_csv("data/Blackbeans_Chickpea.tsv", sep="\t", header=None) #importing fluxes
diet_Blackbeans_Chickpea.columns = ["reaction", "flux"] #changing the name of the columns
diet_Blackbeans_Couscous = pd.read_csv("data/Blackbeans_Couscous.tsv", sep="\t", header=None) #importing fluxes
diet_Blackbeans_Couscous.columns = ["reaction", "flux"] #changing the name of the columns
diet_Blackbeans_Pork = pd.read_csv("data/Blackbeans_Pork.tsv", sep="\t", header=None) #importing fluxes
diet_Blackbeans_Pork.columns = ["reaction", "flux"] #changing the name of the columns
diet_Blackbeans_Pumpkin = pd.read_csv("data/Blackbeans_Pumpkin.tsv", sep="\t", header=None) #importing fluxes
diet_Blackbeans_Pumpkin.columns = ["reaction", "flux"] #changing the name of the columns
diet_Blackbeans_Raspberries = pd.read_csv("data/Blackbeans_Raspberries.tsv", sep="\t", header=None) #importing fluxes
diet_Blackbeans_Raspberries.columns = ["reaction", "flux"] #changing the name of the columns
diet_Blackbeans_Shrimp = pd.read_csv("data/Blackbeans_Shrimp.tsv", sep="\t", header=None) #importing fluxes
diet_Blackbeans_Shrimp.columns = ["reaction", "flux"] #changing the name of the columns
diet_Blackbeans_Soybean = pd.read_csv("data/Blackbeans_Soybean.tsv", sep="\t", header=None) #importing fluxes
diet_Blackbeans_Soybean.columns = ["reaction", "flux"] #changing the name of the columns
diet_Blackbeans_Splitpeas = pd.read_csv("data/Blackbeans_Splitpeas.tsv", sep="\t", header=None) #importing fluxes
diet_Blackbeans_Splitpeas.columns = ["reaction", "flux"] #changing the name of the columns
diet_Blackbeans_Strawberries = pd.read_csv("data/Blackbeans_Strawberries.tsv", sep="\t", header=None) #importing fluxes
diet_Blackbeans_Strawberries.columns = ["reaction", "flux"] #changing the name of the columns
diet_Blackbeans_Sweetpotato = pd.read_csv("data/Blackbeans_Sweetpotato.tsv", sep="\t", header=None) #importing fluxes
diet_Blackbeans_Sweetpotato.columns = ["reaction", "flux"] #changing the name of the columns
diet_Blackcurrant_Chickpea = pd.read_csv("data/Blackcurrant_Chickpea.tsv", sep="\t", header=None) #importing fluxes
diet_Blackcurrant_Chickpea.columns = ["reaction", "flux"] #changing the name of the columns
diet_Blackcurrant_Couscous = pd.read_csv("data/Blackcurrant_Couscous.tsv", sep="\t", header=None) #importing fluxes
diet_Blackcurrant_Couscous.columns = ["reaction", "flux"] #changing the name of the columns
diet_Blackcurrant_Pork = pd.read_csv("data/Blackcurrant_Pork.tsv", sep="\t", header=None) #importing fluxes
diet_Blackcurrant_Pork.columns = ["reaction", "flux"] #changing the name of the columns
diet_Blackcurrant_Pumpkin = pd.read_csv("data/Blackcurrant_Pumpkin.tsv", sep="\t", header=None) #importing fluxes
diet_Blackcurrant_Pumpkin.columns = ["reaction", "flux"] #changing the name of the columns
diet_Blackcurrant_Raspberries = pd.read_csv("data/Blackcurrant_Raspberries.tsv", sep="\t", header=None) #importing fluxes
diet_Blackcurrant_Raspberries.columns = ["reaction", "flux"] #changing the name of the columns
diet_Blackcurrant_Shrimp = pd.read_csv("data/Blackcurrant_Shrimp.tsv", sep="\t", header=None) #importing fluxes
diet_Blackcurrant_Shrimp.columns = ["reaction", "flux"] #changing the name of the columns
diet_Blackcurrant_Soybean = pd.read_csv("data/Blackcurrant_Soybean.tsv", sep="\t", header=None) #importing fluxes
diet_Blackcurrant_Soybean.columns = ["reaction", "flux"] #changing the name of the columns
diet_Blackcurrant_Splitpeas = pd.read_csv("data/Blackcurrant_Splitpeas.tsv", sep="\t", header=None) #importing fluxes
diet_Blackcurrant_Splitpeas.columns = ["reaction", "flux"] #changing the name of the columns
diet_Blackcurrant_Strawberries = pd.read_csv("data/Blackcurrant_Strawberries.tsv", sep="\t", header=None) #importing fluxes
diet_Blackcurrant_Strawberries.columns = ["reaction", "flux"] #changing the name of the columns
diet_Blackcurrant_Sweetpotato = pd.read_csv("data/Blackcurrant_Sweetpotato.tsv", sep="\t", header=None) #importing fluxes
diet_Blackcurrant_Sweetpotato.columns = ["reaction", "flux"] #changing the name of the columns
diet_Chickpea_Couscous = pd.read_csv("data/Chickpea_Couscous.tsv", sep="\t", header=None) #importing fluxes
diet_Chickpea_Couscous.columns = ["reaction", "flux"] #changing the name of the columns
diet_Chickpea_Pork = pd.read_csv("data/Chickpea_Pork.tsv", sep="\t", header=None) #importing fluxes
diet_Chickpea_Pork.columns = ["reaction", "flux"] #changing the name of the columns
diet_Chickpea_Pumpkin = pd.read_csv("data/Chickpea_Pumpkin.tsv", sep="\t", header=None) #importing fluxes
diet_Chickpea_Pumpkin.columns = ["reaction", "flux"] #changing the name of the columns
diet_Chickpea_Raspberries = pd.read_csv("data/Chickpea_Raspberries.tsv", sep="\t", header=None) #importing fluxes
diet_Chickpea_Raspberries.columns = ["reaction", "flux"] #changing the name of the columns
diet_Chickpea_Shrimp = pd.read_csv("data/Chickpea_Shrimp.tsv", sep="\t", header=None) #importing fluxes
diet_Chickpea_Shrimp.columns = ["reaction", "flux"] #changing the name of the columns
diet_Chickpea_Soybean = pd.read_csv("data/Chickpea_Soybean.tsv", sep="\t", header=None) #importing fluxes
diet_Chickpea_Soybean.columns = ["reaction", "flux"] #changing the name of the columns
diet_Chickpea_Splitpeas = pd.read_csv("data/Chickpea_Splitpeas.tsv", sep="\t", header=None) #importing fluxes
diet_Chickpea_Splitpeas.columns = ["reaction", "flux"] #changing the name of the columns
diet_Chickpea_Strawberries = pd.read_csv("data/Chickpea_Strawberries.tsv", sep="\t", header=None) #importing fluxes
diet_Chickpea_Strawberries.columns = ["reaction", "flux"] #changing the name of the columns
diet_Chickpea_Sweetpotato = pd.read_csv("data/Chickpea_Sweetpotato.tsv", sep="\t", header=None) #importing fluxes
diet_Chickpea_Sweetpotato.columns = ["reaction", "flux"] #changing the name of the columns
diet_Couscous_Pork = pd.read_csv("data/Couscous_Pork.tsv", sep="\t", header=None) #importing fluxes
diet_Couscous_Pork.columns = ["reaction", "flux"] #changing the name of the columns
diet_Couscous_Pumpkin = pd.read_csv("data/Couscous_Pumpkin.tsv", sep="\t", header=None) #importing fluxes
diet_Couscous_Pumpkin.columns = ["reaction", "flux"] #changing the name of the columns
diet_Couscous_Raspberries = pd.read_csv("data/Couscous_Raspberries.tsv", sep="\t", header=None) #importing fluxes
diet_Couscous_Raspberries.columns = ["reaction", "flux"] #changing the name of the columns
diet_Couscous_Shrimp = pd.read_csv("data/Couscous_Shrimp.tsv", sep="\t", header=None) #importing fluxes
diet_Couscous_Shrimp.columns = ["reaction", "flux"] #changing the name of the columns
diet_Couscous_Soybean = pd.read_csv("data/Couscous_Soybean.tsv", sep="\t", header=None) #importing fluxes
diet_Couscous_Soybean.columns = ["reaction", "flux"] #changing the name of the columns
diet_Couscous_Splitpeas = pd.read_csv("data/Couscous_Splitpeas.tsv", sep="\t", header=None) #importing fluxes
diet_Couscous_Splitpeas.columns = ["reaction", "flux"] #changing the name of the columns
diet_Couscous_Strawberries = pd.read_csv("data/Couscous_Strawberries.tsv", sep="\t", header=None) #importing fluxes
diet_Couscous_Strawberries.columns = ["reaction", "flux"] #changing the name of the columns
diet_Couscous_Sweetpotato = pd.read_csv("data/Couscous_Sweetpotato.tsv", sep="\t", header=None) #importing fluxes
diet_Couscous_Sweetpotato.columns = ["reaction", "flux"] #changing the name of the columns
diet_Pork_Pumpkin = pd.read_csv("data/Pork_Pumpkin.tsv", sep="\t", header=None) #importing fluxes
diet_Pork_Pumpkin.columns = ["reaction", "flux"] #changing the name of the columns
diet_Pork_Raspberries = pd.read_csv("data/Pork_Raspberries.tsv", sep="\t", header=None) #importing fluxes
diet_Pork_Raspberries.columns = ["reaction", "flux"] #changing the name of the columns
diet_Pork_Shrimp = pd.read_csv("data/Pork_Shrimp.tsv", sep="\t", header=None) #importing fluxes
diet_Pork_Shrimp.columns = ["reaction", "flux"] #changing the name of the columns
diet_Pork_Soybean = pd.read_csv("data/Pork_Soybean.tsv", sep="\t", header=None) #importing fluxes
diet_Pork_Soybean.columns = ["reaction", "flux"] #changing the name of the columns
diet_Pork_Splitpeas = pd.read_csv("data/Pork_Splitpeas.tsv", sep="\t", header=None) #importing fluxes
diet_Pork_Splitpeas.columns = ["reaction", "flux"] #changing the name of the columns
diet_Pork_Strawberries = pd.read_csv("data/Pork_Strawberries.tsv", sep="\t", header=None) #importing fluxes
diet_Pork_Strawberries.columns = ["reaction", "flux"] #changing the name of the columns
diet_Pork_Sweetpotato = pd.read_csv("data/Pork_Sweetpotato.tsv", sep="\t", header=None) #importing fluxes
diet_Pork_Sweetpotato.columns = ["reaction", "flux"] #changing the name of the columns
diet_Pumpkin_Raspberries = pd.read_csv("data/Pumpkin_Raspberries.tsv", sep="\t", header=None) #importing fluxes
diet_Pumpkin_Raspberries.columns = ["reaction", "flux"] #changing the name of the columns
diet_Pumpkin_Shrimp = pd.read_csv("data/Pumpkin_Shrimp.tsv", sep="\t", header=None) #importing fluxes
diet_Pumpkin_Shrimp.columns = ["reaction", "flux"] #changing the name of the columns
diet_Pumpkin_Soybean = pd.read_csv("data/Pumpkin_Soybean.tsv", sep="\t", header=None) #importing fluxes
diet_Pumpkin_Soybean.columns = ["reaction", "flux"] #changing the name of the columns
diet_Pumpkin_Splitpeas = pd.read_csv("data/Pumpkin_Splitpeas.tsv", sep="\t", header=None) #importing fluxes
diet_Pumpkin_Splitpeas.columns = ["reaction", "flux"] #changing the name of the columns
diet_Pumpkin_Strawberries = pd.read_csv("data/Pumpkin_Strawberries.tsv", sep="\t", header=None) #importing fluxes
diet_Pumpkin_Strawberries.columns = ["reaction", "flux"] #changing the name of the columns
diet_Pumpkin_Sweetpotato = pd.read_csv("data/Pumpkin_Sweetpotato.tsv", sep="\t", header=None) #importing fluxes
diet_Pumpkin_Sweetpotato.columns = ["reaction", "flux"] #changing the name of the columns
diet_Raspberries_Shrimp = pd.read_csv("data/Raspberries_Shrimp.tsv", sep="\t", header=None) #importing fluxes
diet_Raspberries_Shrimp.columns = ["reaction", "flux"] #changing the name of the columns
diet_Raspberries_Soybean = pd.read_csv("data/Raspberries_Soybean.tsv", sep="\t", header=None) #importing fluxes
diet_Raspberries_Soybean.columns = ["reaction", "flux"] #changing the name of the columns
diet_Raspberries_Splitpeas = pd.read_csv("data/Raspberries_Splitpeas.tsv", sep="\t", header=None) #importing fluxes
diet_Raspberries_Splitpeas.columns = ["reaction", "flux"] #changing the name of the columns
diet_Raspberries_Strawberries = pd.read_csv("data/Raspberries_Strawberries.tsv", sep="\t", header=None) #importing fluxes
diet_Raspberries_Strawberries.columns = ["reaction", "flux"] #changing the name of the columns
diet_Raspberries_Sweetpotato = pd.read_csv("data/Raspberries_Sweetpotato.tsv", sep="\t", header=None) #importing fluxes
diet_Raspberries_Sweetpotato.columns = ["reaction", "flux"] #changing the name of the columns
diet_Shrimp_Soybean = pd.read_csv("data/Shrimp_Soybean.tsv", sep="\t", header=None) #importing fluxes
diet_Shrimp_Soybean.columns = ["reaction", "flux"] #changing the name of the columns
diet_Shrimp_Splitpeas = pd.read_csv("data/Shrimp_Splitpeas.tsv", sep="\t", header=None) #importing fluxes
diet_Shrimp_Splitpeas.columns = ["reaction", "flux"] #changing the name of the columns
diet_Shrimp_Strawberries = pd.read_csv("data/Shrimp_Strawberries.tsv", sep="\t", header=None) #importing fluxes
diet_Shrimp_Strawberries.columns = ["reaction", "flux"] #changing the name of the columns
diet_Shrimp_Sweetpotato = pd.read_csv("data/Shrimp_Sweetpotato.tsv", sep="\t", header=None) #importing fluxes
diet_Shrimp_Sweetpotato.columns = ["reaction", "flux"] #changing the name of the columns
diet_Soybean_Splitpeas = pd.read_csv("data/Soybean_Splitpeas.tsv", sep="\t", header=None) #importing fluxes
diet_Soybean_Splitpeas.columns = ["reaction", "flux"] #changing the name of the columns
diet_Soybean_Strawberries = pd.read_csv("data/Soybean_Strawberries.tsv", sep="\t", header=None) #importing fluxes
diet_Soybean_Strawberries.columns = ["reaction", "flux"] #changing the name of the columns
diet_Soybean_Sweetpotato = pd.read_csv("data/Soybean_Sweetpotato.tsv", sep="\t", header=None) #importing fluxes
diet_Soybean_Sweetpotato.columns = ["reaction", "flux"] #changing the name of the columns
diet_Splitpeas_Strawberries = pd.read_csv("data/Splitpeas_Strawberries.tsv", sep="\t", header=None) #importing fluxes
diet_Splitpeas_Strawberries.columns = ["reaction", "flux"] #changing the name of the columns
diet_Splitpeas_Sweetpotato = pd.read_csv("data/Splitpeas_Sweetpotato.tsv", sep="\t", header=None) #importing fluxes
diet_Splitpeas_Sweetpotato.columns = ["reaction", "flux"] #changing the name of the columns
diet_Strawberries_Sweetpotato = pd.read_csv("data/Strawberries_Sweetpotato.tsv", sep="\t", header=None) #importing fluxes
diet_Strawberries_Sweetpotato.columns = ["reaction", "flux"] #changing the name of the columns

annotations = pd.read_csv("data/agora_metabolites.csv") #importing a table with the description of agora metabolites
 
diet_Blackbeans_Blackcurrant = diet_Blackbeans_Blackcurrant.rename(columns={diet_Blackbeans_Blackcurrant.columns[0]: "reaction"})
diet_Blackbeans_Blackcurrant["metabolite"] = diet_Blackbeans_Blackcurrant.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Blackbeans_Blackcurrant.loc[diet_Blackbeans_Blackcurrant.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Blackbeans_Blackcurrant.loc[diet_Blackbeans_Blackcurrant.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Blackbeans_Chickpea = diet_Blackbeans_Chickpea.rename(columns={diet_Blackbeans_Chickpea.columns[0]: "reaction"})
diet_Blackbeans_Chickpea["metabolite"] = diet_Blackbeans_Chickpea.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Blackbeans_Chickpea.loc[diet_Blackbeans_Chickpea.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Blackbeans_Chickpea.loc[diet_Blackbeans_Chickpea.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Blackbeans_Couscous = diet_Blackbeans_Couscous.rename(columns={diet_Blackbeans_Couscous.columns[0]: "reaction"})
diet_Blackbeans_Couscous["metabolite"] = diet_Blackbeans_Couscous.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Blackbeans_Couscous.loc[diet_Blackbeans_Couscous.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Blackbeans_Couscous.loc[diet_Blackbeans_Couscous.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Blackbeans_Pork = diet_Blackbeans_Pork.rename(columns={diet_Blackbeans_Pork.columns[0]: "reaction"})
diet_Blackbeans_Pork["metabolite"] = diet_Blackbeans_Pork.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Blackbeans_Pork.loc[diet_Blackbeans_Pork.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Blackbeans_Pork.loc[diet_Blackbeans_Pork.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Blackbeans_Pumpkin = diet_Blackbeans_Pumpkin.rename(columns={diet_Blackbeans_Pumpkin.columns[0]: "reaction"})
diet_Blackbeans_Pumpkin["metabolite"] = diet_Blackbeans_Pumpkin.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Blackbeans_Pumpkin.loc[diet_Blackbeans_Pumpkin.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Blackbeans_Pumpkin.loc[diet_Blackbeans_Pumpkin.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Blackbeans_Raspberries = diet_Blackbeans_Raspberries.rename(columns={diet_Blackbeans_Raspberries.columns[0]: "reaction"})
diet_Blackbeans_Raspberries["metabolite"] = diet_Blackbeans_Raspberries.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Blackbeans_Raspberries.loc[diet_Blackbeans_Raspberries.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Blackbeans_Raspberries.loc[diet_Blackbeans_Raspberries.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Blackbeans_Shrimp = diet_Blackbeans_Shrimp.rename(columns={diet_Blackbeans_Shrimp.columns[0]: "reaction"})
diet_Blackbeans_Shrimp["metabolite"] = diet_Blackbeans_Shrimp.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Blackbeans_Shrimp.loc[diet_Blackbeans_Shrimp.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Blackbeans_Shrimp.loc[diet_Blackbeans_Shrimp.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Blackbeans_Soybean = diet_Blackbeans_Soybean.rename(columns={diet_Blackbeans_Soybean.columns[0]: "reaction"})
diet_Blackbeans_Soybean["metabolite"] = diet_Blackbeans_Soybean.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Blackbeans_Soybean.loc[diet_Blackbeans_Soybean.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Blackbeans_Soybean.loc[diet_Blackbeans_Soybean.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Blackbeans_Splitpeas = diet_Blackbeans_Splitpeas.rename(columns={diet_Blackbeans_Splitpeas.columns[0]: "reaction"})
diet_Blackbeans_Splitpeas["metabolite"] = diet_Blackbeans_Splitpeas.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Blackbeans_Splitpeas.loc[diet_Blackbeans_Splitpeas.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Blackbeans_Splitpeas.loc[diet_Blackbeans_Splitpeas.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Blackbeans_Strawberries = diet_Blackbeans_Strawberries.rename(columns={diet_Blackbeans_Strawberries.columns[0]: "reaction"})
diet_Blackbeans_Strawberries["metabolite"] = diet_Blackbeans_Strawberries.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Blackbeans_Strawberries.loc[diet_Blackbeans_Strawberries.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Blackbeans_Strawberries.loc[diet_Blackbeans_Strawberries.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Blackbeans_Sweetpotato = diet_Blackbeans_Sweetpotato.rename(columns={diet_Blackbeans_Sweetpotato.columns[0]: "reaction"})
diet_Blackbeans_Sweetpotato["metabolite"] = diet_Blackbeans_Sweetpotato.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Blackbeans_Sweetpotato.loc[diet_Blackbeans_Sweetpotato.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Blackbeans_Sweetpotato.loc[diet_Blackbeans_Sweetpotato.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Blackcurrant_Chickpea = diet_Blackcurrant_Chickpea.rename(columns={diet_Blackcurrant_Chickpea.columns[0]: "reaction"})
diet_Blackcurrant_Chickpea["metabolite"] = diet_Blackcurrant_Chickpea.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Blackcurrant_Chickpea.loc[diet_Blackcurrant_Chickpea.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Blackcurrant_Chickpea.loc[diet_Blackcurrant_Chickpea.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Blackcurrant_Couscous = diet_Blackcurrant_Couscous.rename(columns={diet_Blackcurrant_Couscous.columns[0]: "reaction"})
diet_Blackcurrant_Couscous["metabolite"] = diet_Blackcurrant_Couscous.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Blackcurrant_Couscous.loc[diet_Blackcurrant_Couscous.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Blackcurrant_Couscous.loc[diet_Blackcurrant_Couscous.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Blackcurrant_Pork = diet_Blackcurrant_Pork.rename(columns={diet_Blackcurrant_Pork.columns[0]: "reaction"})
diet_Blackcurrant_Pork["metabolite"] = diet_Blackcurrant_Pork.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Blackcurrant_Pork.loc[diet_Blackcurrant_Pork.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Blackcurrant_Pork.loc[diet_Blackcurrant_Pork.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Blackcurrant_Pumpkin = diet_Blackcurrant_Pumpkin.rename(columns={diet_Blackcurrant_Pumpkin.columns[0]: "reaction"})
diet_Blackcurrant_Pumpkin["metabolite"] = diet_Blackcurrant_Pumpkin.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Blackcurrant_Pumpkin.loc[diet_Blackcurrant_Pumpkin.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Blackcurrant_Pumpkin.loc[diet_Blackcurrant_Pumpkin.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Blackcurrant_Raspberries = diet_Blackcurrant_Raspberries.rename(columns={diet_Blackcurrant_Raspberries.columns[0]: "reaction"})
diet_Blackcurrant_Raspberries["metabolite"] = diet_Blackcurrant_Raspberries.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Blackcurrant_Raspberries.loc[diet_Blackcurrant_Raspberries.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Blackcurrant_Raspberries.loc[diet_Blackcurrant_Raspberries.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Blackcurrant_Shrimp = diet_Blackcurrant_Shrimp.rename(columns={diet_Blackcurrant_Shrimp.columns[0]: "reaction"})
diet_Blackcurrant_Shrimp["metabolite"] = diet_Blackcurrant_Shrimp.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Blackcurrant_Shrimp.loc[diet_Blackcurrant_Shrimp.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Blackcurrant_Shrimp.loc[diet_Blackcurrant_Shrimp.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Blackcurrant_Soybean = diet_Blackcurrant_Soybean.rename(columns={diet_Blackcurrant_Soybean.columns[0]: "reaction"})
diet_Blackcurrant_Soybean["metabolite"] = diet_Blackcurrant_Soybean.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Blackcurrant_Soybean.loc[diet_Blackcurrant_Soybean.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Blackcurrant_Soybean.loc[diet_Blackcurrant_Soybean.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Blackcurrant_Splitpeas = diet_Blackcurrant_Splitpeas.rename(columns={diet_Blackcurrant_Splitpeas.columns[0]: "reaction"})
diet_Blackcurrant_Splitpeas["metabolite"] = diet_Blackcurrant_Splitpeas.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Blackcurrant_Splitpeas.loc[diet_Blackcurrant_Splitpeas.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Blackcurrant_Splitpeas.loc[diet_Blackcurrant_Splitpeas.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Blackcurrant_Strawberries = diet_Blackcurrant_Strawberries.rename(columns={diet_Blackcurrant_Strawberries.columns[0]: "reaction"})
diet_Blackcurrant_Strawberries["metabolite"] = diet_Blackcurrant_Strawberries.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Blackcurrant_Strawberries.loc[diet_Blackcurrant_Strawberries.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Blackcurrant_Strawberries.loc[diet_Blackcurrant_Strawberries.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Blackcurrant_Sweetpotato = diet_Blackcurrant_Sweetpotato.rename(columns={diet_Blackcurrant_Sweetpotato.columns[0]: "reaction"})
diet_Blackcurrant_Sweetpotato["metabolite"] = diet_Blackcurrant_Sweetpotato.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Blackcurrant_Sweetpotato.loc[diet_Blackcurrant_Sweetpotato.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Blackcurrant_Sweetpotato.loc[diet_Blackcurrant_Sweetpotato.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Chickpea_Couscous = diet_Chickpea_Couscous.rename(columns={diet_Chickpea_Couscous.columns[0]: "reaction"})
diet_Chickpea_Couscous["metabolite"] = diet_Chickpea_Couscous.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Chickpea_Couscous.loc[diet_Chickpea_Couscous.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Chickpea_Couscous.loc[diet_Chickpea_Couscous.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Chickpea_Pork = diet_Chickpea_Pork.rename(columns={diet_Chickpea_Pork.columns[0]: "reaction"})
diet_Chickpea_Pork["metabolite"] = diet_Chickpea_Pork.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Chickpea_Pork.loc[diet_Chickpea_Pork.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Chickpea_Pork.loc[diet_Chickpea_Pork.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Chickpea_Pumpkin = diet_Chickpea_Pumpkin.rename(columns={diet_Chickpea_Pumpkin.columns[0]: "reaction"})
diet_Chickpea_Pumpkin["metabolite"] = diet_Chickpea_Pumpkin.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Chickpea_Pumpkin.loc[diet_Chickpea_Pumpkin.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Chickpea_Pumpkin.loc[diet_Chickpea_Pumpkin.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Chickpea_Raspberries = diet_Chickpea_Raspberries.rename(columns={diet_Chickpea_Raspberries.columns[0]: "reaction"})
diet_Chickpea_Raspberries["metabolite"] = diet_Chickpea_Raspberries.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Chickpea_Raspberries.loc[diet_Chickpea_Raspberries.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Chickpea_Raspberries.loc[diet_Chickpea_Raspberries.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Chickpea_Shrimp = diet_Chickpea_Shrimp.rename(columns={diet_Chickpea_Shrimp.columns[0]: "reaction"})
diet_Chickpea_Shrimp["metabolite"] = diet_Chickpea_Shrimp.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Chickpea_Shrimp.loc[diet_Chickpea_Shrimp.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Chickpea_Shrimp.loc[diet_Chickpea_Shrimp.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Chickpea_Soybean = diet_Chickpea_Soybean.rename(columns={diet_Chickpea_Soybean.columns[0]: "reaction"})
diet_Chickpea_Soybean["metabolite"] = diet_Chickpea_Soybean.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Chickpea_Soybean.loc[diet_Chickpea_Soybean.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Chickpea_Soybean.loc[diet_Chickpea_Soybean.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Chickpea_Splitpeas = diet_Chickpea_Splitpeas.rename(columns={diet_Chickpea_Splitpeas.columns[0]: "reaction"})
diet_Chickpea_Splitpeas["metabolite"] = diet_Chickpea_Splitpeas.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Chickpea_Splitpeas.loc[diet_Chickpea_Splitpeas.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Chickpea_Splitpeas.loc[diet_Chickpea_Splitpeas.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Chickpea_Strawberries = diet_Chickpea_Strawberries.rename(columns={diet_Chickpea_Strawberries.columns[0]: "reaction"})
diet_Chickpea_Strawberries["metabolite"] = diet_Chickpea_Strawberries.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Chickpea_Strawberries.loc[diet_Chickpea_Strawberries.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Chickpea_Strawberries.loc[diet_Chickpea_Strawberries.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Chickpea_Sweetpotato = diet_Chickpea_Sweetpotato.rename(columns={diet_Chickpea_Sweetpotato.columns[0]: "reaction"})
diet_Chickpea_Sweetpotato["metabolite"] = diet_Chickpea_Sweetpotato.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Chickpea_Sweetpotato.loc[diet_Chickpea_Sweetpotato.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Chickpea_Sweetpotato.loc[diet_Chickpea_Sweetpotato.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Couscous_Pork = diet_Couscous_Pork.rename(columns={diet_Couscous_Pork.columns[0]: "reaction"})
diet_Couscous_Pork["metabolite"] = diet_Couscous_Pork.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Couscous_Pork.loc[diet_Couscous_Pork.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Couscous_Pork.loc[diet_Couscous_Pork.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Couscous_Pumpkin = diet_Couscous_Pumpkin.rename(columns={diet_Couscous_Pumpkin.columns[0]: "reaction"})
diet_Couscous_Pumpkin["metabolite"] = diet_Couscous_Pumpkin.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Couscous_Pumpkin.loc[diet_Couscous_Pumpkin.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Couscous_Pumpkin.loc[diet_Couscous_Pumpkin.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Couscous_Raspberries = diet_Couscous_Raspberries.rename(columns={diet_Couscous_Raspberries.columns[0]: "reaction"})
diet_Couscous_Raspberries["metabolite"] = diet_Couscous_Raspberries.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Couscous_Raspberries.loc[diet_Couscous_Raspberries.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Couscous_Raspberries.loc[diet_Couscous_Raspberries.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Couscous_Shrimp = diet_Couscous_Shrimp.rename(columns={diet_Couscous_Shrimp.columns[0]: "reaction"})
diet_Couscous_Shrimp["metabolite"] = diet_Couscous_Shrimp.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Couscous_Shrimp.loc[diet_Couscous_Shrimp.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Couscous_Shrimp.loc[diet_Couscous_Shrimp.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Couscous_Soybean = diet_Couscous_Soybean.rename(columns={diet_Couscous_Soybean.columns[0]: "reaction"})
diet_Couscous_Soybean["metabolite"] = diet_Couscous_Soybean.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Couscous_Soybean.loc[diet_Couscous_Soybean.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Couscous_Soybean.loc[diet_Couscous_Soybean.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Couscous_Splitpeas = diet_Couscous_Splitpeas.rename(columns={diet_Couscous_Splitpeas.columns[0]: "reaction"})
diet_Couscous_Splitpeas["metabolite"] = diet_Couscous_Splitpeas.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Couscous_Splitpeas.loc[diet_Couscous_Splitpeas.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Couscous_Splitpeas.loc[diet_Couscous_Splitpeas.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Couscous_Strawberries = diet_Couscous_Strawberries.rename(columns={diet_Couscous_Strawberries.columns[0]: "reaction"})
diet_Couscous_Strawberries["metabolite"] = diet_Couscous_Strawberries.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Couscous_Strawberries.loc[diet_Couscous_Strawberries.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Couscous_Strawberries.loc[diet_Couscous_Strawberries.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Couscous_Sweetpotato = diet_Couscous_Sweetpotato.rename(columns={diet_Couscous_Sweetpotato.columns[0]: "reaction"})
diet_Couscous_Sweetpotato["metabolite"] = diet_Couscous_Sweetpotato.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Couscous_Sweetpotato.loc[diet_Couscous_Sweetpotato.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Couscous_Sweetpotato.loc[diet_Couscous_Sweetpotato.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Pork_Pumpkin = diet_Pork_Pumpkin.rename(columns={diet_Pork_Pumpkin.columns[0]: "reaction"})
diet_Pork_Pumpkin["metabolite"] = diet_Pork_Pumpkin.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Pork_Pumpkin.loc[diet_Pork_Pumpkin.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Pork_Pumpkin.loc[diet_Pork_Pumpkin.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Pork_Raspberries = diet_Pork_Raspberries.rename(columns={diet_Pork_Raspberries.columns[0]: "reaction"})
diet_Pork_Raspberries["metabolite"] = diet_Pork_Raspberries.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Pork_Raspberries.loc[diet_Pork_Raspberries.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Pork_Raspberries.loc[diet_Pork_Raspberries.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Pork_Shrimp = diet_Pork_Shrimp.rename(columns={diet_Pork_Shrimp.columns[0]: "reaction"})
diet_Pork_Shrimp["metabolite"] = diet_Pork_Shrimp.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Pork_Shrimp.loc[diet_Pork_Shrimp.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Pork_Shrimp.loc[diet_Pork_Shrimp.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Pork_Soybean = diet_Pork_Soybean.rename(columns={diet_Pork_Soybean.columns[0]: "reaction"})
diet_Pork_Soybean["metabolite"] = diet_Pork_Soybean.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Pork_Soybean.loc[diet_Pork_Soybean.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Pork_Soybean.loc[diet_Pork_Soybean.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Pork_Splitpeas = diet_Pork_Splitpeas.rename(columns={diet_Pork_Splitpeas.columns[0]: "reaction"})
diet_Pork_Splitpeas["metabolite"] = diet_Pork_Splitpeas.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Pork_Splitpeas.loc[diet_Pork_Splitpeas.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Pork_Splitpeas.loc[diet_Pork_Splitpeas.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Pork_Strawberries = diet_Pork_Strawberries.rename(columns={diet_Pork_Strawberries.columns[0]: "reaction"})
diet_Pork_Strawberries["metabolite"] = diet_Pork_Strawberries.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Pork_Strawberries.loc[diet_Pork_Strawberries.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Pork_Strawberries.loc[diet_Pork_Strawberries.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Pork_Sweetpotato = diet_Pork_Sweetpotato.rename(columns={diet_Pork_Sweetpotato.columns[0]: "reaction"})
diet_Pork_Sweetpotato["metabolite"] = diet_Pork_Sweetpotato.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Pork_Sweetpotato.loc[diet_Pork_Sweetpotato.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Pork_Sweetpotato.loc[diet_Pork_Sweetpotato.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Pumpkin_Raspberries = diet_Pumpkin_Raspberries.rename(columns={diet_Pumpkin_Raspberries.columns[0]: "reaction"})
diet_Pumpkin_Raspberries["metabolite"] = diet_Pumpkin_Raspberries.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Pumpkin_Raspberries.loc[diet_Pumpkin_Raspberries.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Pumpkin_Raspberries.loc[diet_Pumpkin_Raspberries.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Pumpkin_Shrimp = diet_Pumpkin_Shrimp.rename(columns={diet_Pumpkin_Shrimp.columns[0]: "reaction"})
diet_Pumpkin_Shrimp["metabolite"] = diet_Pumpkin_Shrimp.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Pumpkin_Shrimp.loc[diet_Pumpkin_Shrimp.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Pumpkin_Shrimp.loc[diet_Pumpkin_Shrimp.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Pumpkin_Soybean = diet_Pumpkin_Soybean.rename(columns={diet_Pumpkin_Soybean.columns[0]: "reaction"})
diet_Pumpkin_Soybean["metabolite"] = diet_Pumpkin_Soybean.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Pumpkin_Soybean.loc[diet_Pumpkin_Soybean.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Pumpkin_Soybean.loc[diet_Pumpkin_Soybean.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Pumpkin_Splitpeas = diet_Pumpkin_Splitpeas.rename(columns={diet_Pumpkin_Splitpeas.columns[0]: "reaction"})
diet_Pumpkin_Splitpeas["metabolite"] = diet_Pumpkin_Splitpeas.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Pumpkin_Splitpeas.loc[diet_Pumpkin_Splitpeas.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Pumpkin_Splitpeas.loc[diet_Pumpkin_Splitpeas.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Pumpkin_Strawberries = diet_Pumpkin_Strawberries.rename(columns={diet_Pumpkin_Strawberries.columns[0]: "reaction"})
diet_Pumpkin_Strawberries["metabolite"] = diet_Pumpkin_Strawberries.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Pumpkin_Strawberries.loc[diet_Pumpkin_Strawberries.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Pumpkin_Strawberries.loc[diet_Pumpkin_Strawberries.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Pumpkin_Sweetpotato = diet_Pumpkin_Sweetpotato.rename(columns={diet_Pumpkin_Sweetpotato.columns[0]: "reaction"})
diet_Pumpkin_Sweetpotato["metabolite"] = diet_Pumpkin_Sweetpotato.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Pumpkin_Sweetpotato.loc[diet_Pumpkin_Sweetpotato.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Pumpkin_Sweetpotato.loc[diet_Pumpkin_Sweetpotato.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Raspberries_Shrimp = diet_Raspberries_Shrimp.rename(columns={diet_Raspberries_Shrimp.columns[0]: "reaction"})
diet_Raspberries_Shrimp["metabolite"] = diet_Raspberries_Shrimp.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Raspberries_Shrimp.loc[diet_Raspberries_Shrimp.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Raspberries_Shrimp.loc[diet_Raspberries_Shrimp.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Raspberries_Soybean = diet_Raspberries_Soybean.rename(columns={diet_Raspberries_Soybean.columns[0]: "reaction"})
diet_Raspberries_Soybean["metabolite"] = diet_Raspberries_Soybean.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Raspberries_Soybean.loc[diet_Raspberries_Soybean.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Raspberries_Soybean.loc[diet_Raspberries_Soybean.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Raspberries_Splitpeas = diet_Raspberries_Splitpeas.rename(columns={diet_Raspberries_Splitpeas.columns[0]: "reaction"})
diet_Raspberries_Splitpeas["metabolite"] = diet_Raspberries_Splitpeas.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Raspberries_Splitpeas.loc[diet_Raspberries_Splitpeas.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Raspberries_Splitpeas.loc[diet_Raspberries_Splitpeas.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Raspberries_Strawberries = diet_Raspberries_Strawberries.rename(columns={diet_Raspberries_Strawberries.columns[0]: "reaction"})
diet_Raspberries_Strawberries["metabolite"] = diet_Raspberries_Strawberries.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Raspberries_Strawberries.loc[diet_Raspberries_Strawberries.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Raspberries_Strawberries.loc[diet_Raspberries_Strawberries.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Raspberries_Sweetpotato = diet_Raspberries_Sweetpotato.rename(columns={diet_Raspberries_Sweetpotato.columns[0]: "reaction"})
diet_Raspberries_Sweetpotato["metabolite"] = diet_Raspberries_Sweetpotato.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Raspberries_Sweetpotato.loc[diet_Raspberries_Sweetpotato.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Raspberries_Sweetpotato.loc[diet_Raspberries_Sweetpotato.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Shrimp_Soybean = diet_Shrimp_Soybean.rename(columns={diet_Shrimp_Soybean.columns[0]: "reaction"})
diet_Shrimp_Soybean["metabolite"] = diet_Shrimp_Soybean.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Shrimp_Soybean.loc[diet_Shrimp_Soybean.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Shrimp_Soybean.loc[diet_Shrimp_Soybean.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Shrimp_Splitpeas = diet_Shrimp_Splitpeas.rename(columns={diet_Shrimp_Splitpeas.columns[0]: "reaction"})
diet_Shrimp_Splitpeas["metabolite"] = diet_Shrimp_Splitpeas.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Shrimp_Splitpeas.loc[diet_Shrimp_Splitpeas.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Shrimp_Splitpeas.loc[diet_Shrimp_Splitpeas.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Shrimp_Strawberries = diet_Shrimp_Strawberries.rename(columns={diet_Shrimp_Strawberries.columns[0]: "reaction"})
diet_Shrimp_Strawberries["metabolite"] = diet_Shrimp_Strawberries.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Shrimp_Strawberries.loc[diet_Shrimp_Strawberries.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Shrimp_Strawberries.loc[diet_Shrimp_Strawberries.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Shrimp_Sweetpotato = diet_Shrimp_Sweetpotato.rename(columns={diet_Shrimp_Sweetpotato.columns[0]: "reaction"})
diet_Shrimp_Sweetpotato["metabolite"] = diet_Shrimp_Sweetpotato.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Shrimp_Sweetpotato.loc[diet_Shrimp_Sweetpotato.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Shrimp_Sweetpotato.loc[diet_Shrimp_Sweetpotato.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Soybean_Splitpeas = diet_Soybean_Splitpeas.rename(columns={diet_Soybean_Splitpeas.columns[0]: "reaction"})
diet_Soybean_Splitpeas["metabolite"] = diet_Soybean_Splitpeas.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Soybean_Splitpeas.loc[diet_Soybean_Splitpeas.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Soybean_Splitpeas.loc[diet_Soybean_Splitpeas.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Soybean_Strawberries = diet_Soybean_Strawberries.rename(columns={diet_Soybean_Strawberries.columns[0]: "reaction"})
diet_Soybean_Strawberries["metabolite"] = diet_Soybean_Strawberries.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Soybean_Strawberries.loc[diet_Soybean_Strawberries.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Soybean_Strawberries.loc[diet_Soybean_Strawberries.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Soybean_Sweetpotato = diet_Soybean_Sweetpotato.rename(columns={diet_Soybean_Sweetpotato.columns[0]: "reaction"})
diet_Soybean_Sweetpotato["metabolite"] = diet_Soybean_Sweetpotato.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Soybean_Sweetpotato.loc[diet_Soybean_Sweetpotato.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Soybean_Sweetpotato.loc[diet_Soybean_Sweetpotato.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Splitpeas_Strawberries = diet_Splitpeas_Strawberries.rename(columns={diet_Splitpeas_Strawberries.columns[0]: "reaction"})
diet_Splitpeas_Strawberries["metabolite"] = diet_Splitpeas_Strawberries.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Splitpeas_Strawberries.loc[diet_Splitpeas_Strawberries.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Splitpeas_Strawberries.loc[diet_Splitpeas_Strawberries.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Splitpeas_Sweetpotato = diet_Splitpeas_Sweetpotato.rename(columns={diet_Splitpeas_Sweetpotato.columns[0]: "reaction"})
diet_Splitpeas_Sweetpotato["metabolite"] = diet_Splitpeas_Sweetpotato.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Splitpeas_Sweetpotato.loc[diet_Splitpeas_Sweetpotato.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Splitpeas_Sweetpotato.loc[diet_Splitpeas_Sweetpotato.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Strawberries_Sweetpotato = diet_Strawberries_Sweetpotato.rename(columns={diet_Strawberries_Sweetpotato.columns[0]: "reaction"})
diet_Strawberries_Sweetpotato["metabolite"] = diet_Strawberries_Sweetpotato.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Strawberries_Sweetpotato.loc[diet_Strawberries_Sweetpotato.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Strawberries_Sweetpotato.loc[diet_Strawberries_Sweetpotato.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0

from cobra.io import read_sbml_model
import pandas as pd

recon3 = read_sbml_model("data/Recon3D.xml.gz") #importing Recon3D model
exchanges = pd.Series([r.id for r in recon3.exchanges])
exchanges = exchanges.str.replace("__", "_").str.replace("_e$|EX_", "", regex=True) #list with the nutrients that are absrobed

diet_Blackbeans_Blackcurrant["dilution"] = 1.0
diet_Blackbeans_Blackcurrant.loc[diet_Blackbeans_Blackcurrant.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Blackbeans_Blackcurrant["flux"] = diet_Blackbeans_Blackcurrant["flux"] * diet_Blackbeans_Blackcurrant["dilution"] #updaing the flux, considering the dilution
diet_Blackbeans_Blackcurrant[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Blackbeans_Chickpea["dilution"] = 1.0
diet_Blackbeans_Chickpea.loc[diet_Blackbeans_Chickpea.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Blackbeans_Chickpea["flux"] = diet_Blackbeans_Chickpea["flux"] * diet_Blackbeans_Chickpea["dilution"] #updaing the flux, considering the dilution
diet_Blackbeans_Chickpea[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Blackbeans_Couscous["dilution"] = 1.0
diet_Blackbeans_Couscous.loc[diet_Blackbeans_Couscous.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Blackbeans_Couscous["flux"] = diet_Blackbeans_Couscous["flux"] * diet_Blackbeans_Couscous["dilution"] #updaing the flux, considering the dilution
diet_Blackbeans_Couscous[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Blackbeans_Pork["dilution"] = 1.0
diet_Blackbeans_Pork.loc[diet_Blackbeans_Pork.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Blackbeans_Pork["flux"] = diet_Blackbeans_Pork["flux"] * diet_Blackbeans_Pork["dilution"] #updaing the flux, considering the dilution
diet_Blackbeans_Pork[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Blackbeans_Pumpkin["dilution"] = 1.0
diet_Blackbeans_Pumpkin.loc[diet_Blackbeans_Pumpkin.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Blackbeans_Pumpkin["flux"] = diet_Blackbeans_Pumpkin["flux"] * diet_Blackbeans_Pumpkin["dilution"] #updaing the flux, considering the dilution
diet_Blackbeans_Pumpkin[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Blackbeans_Raspberries["dilution"] = 1.0
diet_Blackbeans_Raspberries.loc[diet_Blackbeans_Raspberries.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Blackbeans_Raspberries["flux"] = diet_Blackbeans_Raspberries["flux"] * diet_Blackbeans_Raspberries["dilution"] #updaing the flux, considering the dilution
diet_Blackbeans_Raspberries[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Blackbeans_Shrimp["dilution"] = 1.0
diet_Blackbeans_Shrimp.loc[diet_Blackbeans_Shrimp.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Blackbeans_Shrimp["flux"] = diet_Blackbeans_Shrimp["flux"] * diet_Blackbeans_Shrimp["dilution"] #updaing the flux, considering the dilution
diet_Blackbeans_Shrimp[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Blackbeans_Soybean["dilution"] = 1.0
diet_Blackbeans_Soybean.loc[diet_Blackbeans_Soybean.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Blackbeans_Soybean["flux"] = diet_Blackbeans_Soybean["flux"] * diet_Blackbeans_Soybean["dilution"] #updaing the flux, considering the dilution
diet_Blackbeans_Soybean[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Blackbeans_Splitpeas["dilution"] = 1.0
diet_Blackbeans_Splitpeas.loc[diet_Blackbeans_Splitpeas.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Blackbeans_Splitpeas["flux"] = diet_Blackbeans_Splitpeas["flux"] * diet_Blackbeans_Splitpeas["dilution"] #updaing the flux, considering the dilution
diet_Blackbeans_Splitpeas[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Blackbeans_Strawberries["dilution"] = 1.0
diet_Blackbeans_Strawberries.loc[diet_Blackbeans_Strawberries.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Blackbeans_Strawberries["flux"] = diet_Blackbeans_Strawberries["flux"] * diet_Blackbeans_Strawberries["dilution"] #updaing the flux, considering the dilution
diet_Blackbeans_Strawberries[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Blackbeans_Sweetpotato["dilution"] = 1.0
diet_Blackbeans_Sweetpotato.loc[diet_Blackbeans_Sweetpotato.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Blackbeans_Sweetpotato["flux"] = diet_Blackbeans_Sweetpotato["flux"] * diet_Blackbeans_Sweetpotato["dilution"] #updaing the flux, considering the dilution
diet_Blackbeans_Sweetpotato[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Blackcurrant_Chickpea["dilution"] = 1.0
diet_Blackcurrant_Chickpea.loc[diet_Blackcurrant_Chickpea.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Blackcurrant_Chickpea["flux"] = diet_Blackcurrant_Chickpea["flux"] * diet_Blackcurrant_Chickpea["dilution"] #updaing the flux, considering the dilution
diet_Blackcurrant_Chickpea[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Blackcurrant_Couscous["dilution"] = 1.0
diet_Blackcurrant_Couscous.loc[diet_Blackcurrant_Couscous.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Blackcurrant_Couscous["flux"] = diet_Blackcurrant_Couscous["flux"] * diet_Blackcurrant_Couscous["dilution"] #updaing the flux, considering the dilution
diet_Blackcurrant_Couscous[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Blackcurrant_Pork["dilution"] = 1.0
diet_Blackcurrant_Pork.loc[diet_Blackcurrant_Pork.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Blackcurrant_Pork["flux"] = diet_Blackcurrant_Pork["flux"] * diet_Blackcurrant_Pork["dilution"] #updaing the flux, considering the dilution
diet_Blackcurrant_Pork[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Blackcurrant_Pumpkin["dilution"] = 1.0
diet_Blackcurrant_Pumpkin.loc[diet_Blackcurrant_Pumpkin.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Blackcurrant_Pumpkin["flux"] = diet_Blackcurrant_Pumpkin["flux"] * diet_Blackcurrant_Pumpkin["dilution"] #updaing the flux, considering the dilution
diet_Blackcurrant_Pumpkin[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Blackcurrant_Raspberries["dilution"] = 1.0
diet_Blackcurrant_Raspberries.loc[diet_Blackcurrant_Raspberries.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Blackcurrant_Raspberries["flux"] = diet_Blackcurrant_Raspberries["flux"] * diet_Blackcurrant_Raspberries["dilution"] #updaing the flux, considering the dilution
diet_Blackcurrant_Raspberries[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Blackcurrant_Shrimp["dilution"] = 1.0
diet_Blackcurrant_Shrimp.loc[diet_Blackcurrant_Shrimp.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Blackcurrant_Shrimp["flux"] = diet_Blackcurrant_Shrimp["flux"] * diet_Blackcurrant_Shrimp["dilution"] #updaing the flux, considering the dilution
diet_Blackcurrant_Shrimp[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Blackcurrant_Soybean["dilution"] = 1.0
diet_Blackcurrant_Soybean.loc[diet_Blackcurrant_Soybean.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Blackcurrant_Soybean["flux"] = diet_Blackcurrant_Soybean["flux"] * diet_Blackcurrant_Soybean["dilution"] #updaing the flux, considering the dilution
diet_Blackcurrant_Soybean[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Blackcurrant_Splitpeas["dilution"] = 1.0
diet_Blackcurrant_Splitpeas.loc[diet_Blackcurrant_Splitpeas.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Blackcurrant_Splitpeas["flux"] = diet_Blackcurrant_Splitpeas["flux"] * diet_Blackcurrant_Splitpeas["dilution"] #updaing the flux, considering the dilution
diet_Blackcurrant_Splitpeas[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Blackcurrant_Strawberries["dilution"] = 1.0
diet_Blackcurrant_Strawberries.loc[diet_Blackcurrant_Strawberries.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Blackcurrant_Strawberries["flux"] = diet_Blackcurrant_Strawberries["flux"] * diet_Blackcurrant_Strawberries["dilution"] #updaing the flux, considering the dilution
diet_Blackcurrant_Strawberries[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Blackcurrant_Sweetpotato["dilution"] = 1.0
diet_Blackcurrant_Sweetpotato.loc[diet_Blackcurrant_Sweetpotato.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Blackcurrant_Sweetpotato["flux"] = diet_Blackcurrant_Sweetpotato["flux"] * diet_Blackcurrant_Sweetpotato["dilution"] #updaing the flux, considering the dilution
diet_Blackcurrant_Sweetpotato[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Chickpea_Couscous["dilution"] = 1.0
diet_Chickpea_Couscous.loc[diet_Chickpea_Couscous.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Chickpea_Couscous["flux"] = diet_Chickpea_Couscous["flux"] * diet_Chickpea_Couscous["dilution"] #updaing the flux, considering the dilution
diet_Chickpea_Couscous[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Chickpea_Pork["dilution"] = 1.0
diet_Chickpea_Pork.loc[diet_Chickpea_Pork.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Chickpea_Pork["flux"] = diet_Chickpea_Pork["flux"] * diet_Chickpea_Pork["dilution"] #updaing the flux, considering the dilution
diet_Chickpea_Pork[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Chickpea_Pumpkin["dilution"] = 1.0
diet_Chickpea_Pumpkin.loc[diet_Chickpea_Pumpkin.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Chickpea_Pumpkin["flux"] = diet_Chickpea_Pumpkin["flux"] * diet_Chickpea_Pumpkin["dilution"] #updaing the flux, considering the dilution
diet_Chickpea_Pumpkin[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Chickpea_Raspberries["dilution"] = 1.0
diet_Chickpea_Raspberries.loc[diet_Chickpea_Raspberries.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Chickpea_Raspberries["flux"] = diet_Chickpea_Raspberries["flux"] * diet_Chickpea_Raspberries["dilution"] #updaing the flux, considering the dilution
diet_Chickpea_Raspberries[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Chickpea_Shrimp["dilution"] = 1.0
diet_Chickpea_Shrimp.loc[diet_Chickpea_Shrimp.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Chickpea_Shrimp["flux"] = diet_Chickpea_Shrimp["flux"] * diet_Chickpea_Shrimp["dilution"] #updaing the flux, considering the dilution
diet_Chickpea_Shrimp[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Chickpea_Soybean["dilution"] = 1.0
diet_Chickpea_Soybean.loc[diet_Chickpea_Soybean.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Chickpea_Soybean["flux"] = diet_Chickpea_Soybean["flux"] * diet_Chickpea_Soybean["dilution"] #updaing the flux, considering the dilution
diet_Chickpea_Soybean[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Chickpea_Splitpeas["dilution"] = 1.0
diet_Chickpea_Splitpeas.loc[diet_Chickpea_Splitpeas.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Chickpea_Splitpeas["flux"] = diet_Chickpea_Splitpeas["flux"] * diet_Chickpea_Splitpeas["dilution"] #updaing the flux, considering the dilution
diet_Chickpea_Splitpeas[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Chickpea_Strawberries["dilution"] = 1.0
diet_Chickpea_Strawberries.loc[diet_Chickpea_Strawberries.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Chickpea_Strawberries["flux"] = diet_Chickpea_Strawberries["flux"] * diet_Chickpea_Strawberries["dilution"] #updaing the flux, considering the dilution
diet_Chickpea_Strawberries[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Chickpea_Sweetpotato["dilution"] = 1.0
diet_Chickpea_Sweetpotato.loc[diet_Chickpea_Sweetpotato.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Chickpea_Sweetpotato["flux"] = diet_Chickpea_Sweetpotato["flux"] * diet_Chickpea_Sweetpotato["dilution"] #updaing the flux, considering the dilution
diet_Chickpea_Sweetpotato[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Couscous_Pork["dilution"] = 1.0
diet_Couscous_Pork.loc[diet_Couscous_Pork.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Couscous_Pork["flux"] = diet_Couscous_Pork["flux"] * diet_Couscous_Pork["dilution"] #updaing the flux, considering the dilution
diet_Couscous_Pork[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Couscous_Pumpkin["dilution"] = 1.0
diet_Couscous_Pumpkin.loc[diet_Couscous_Pumpkin.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Couscous_Pumpkin["flux"] = diet_Couscous_Pumpkin["flux"] * diet_Couscous_Pumpkin["dilution"] #updaing the flux, considering the dilution
diet_Couscous_Pumpkin[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Couscous_Raspberries["dilution"] = 1.0
diet_Couscous_Raspberries.loc[diet_Couscous_Raspberries.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Couscous_Raspberries["flux"] = diet_Couscous_Raspberries["flux"] * diet_Couscous_Raspberries["dilution"] #updaing the flux, considering the dilution
diet_Couscous_Raspberries[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Couscous_Shrimp["dilution"] = 1.0
diet_Couscous_Shrimp.loc[diet_Couscous_Shrimp.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Couscous_Shrimp["flux"] = diet_Couscous_Shrimp["flux"] * diet_Couscous_Shrimp["dilution"] #updaing the flux, considering the dilution
diet_Couscous_Shrimp[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Couscous_Soybean["dilution"] = 1.0
diet_Couscous_Soybean.loc[diet_Couscous_Soybean.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Couscous_Soybean["flux"] = diet_Couscous_Soybean["flux"] * diet_Couscous_Soybean["dilution"] #updaing the flux, considering the dilution
diet_Couscous_Soybean[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Couscous_Splitpeas["dilution"] = 1.0
diet_Couscous_Splitpeas.loc[diet_Couscous_Splitpeas.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Couscous_Splitpeas["flux"] = diet_Couscous_Splitpeas["flux"] * diet_Couscous_Splitpeas["dilution"] #updaing the flux, considering the dilution
diet_Couscous_Splitpeas[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Couscous_Strawberries["dilution"] = 1.0
diet_Couscous_Strawberries.loc[diet_Couscous_Strawberries.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Couscous_Strawberries["flux"] = diet_Couscous_Strawberries["flux"] * diet_Couscous_Strawberries["dilution"] #updaing the flux, considering the dilution
diet_Couscous_Strawberries[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Couscous_Sweetpotato["dilution"] = 1.0
diet_Couscous_Sweetpotato.loc[diet_Couscous_Sweetpotato.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Couscous_Sweetpotato["flux"] = diet_Couscous_Sweetpotato["flux"] * diet_Couscous_Sweetpotato["dilution"] #updaing the flux, considering the dilution
diet_Couscous_Sweetpotato[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Pork_Pumpkin["dilution"] = 1.0
diet_Pork_Pumpkin.loc[diet_Pork_Pumpkin.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Pork_Pumpkin["flux"] = diet_Pork_Pumpkin["flux"] * diet_Pork_Pumpkin["dilution"] #updaing the flux, considering the dilution
diet_Pork_Pumpkin[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Pork_Raspberries["dilution"] = 1.0
diet_Pork_Raspberries.loc[diet_Pork_Raspberries.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Pork_Raspberries["flux"] = diet_Pork_Raspberries["flux"] * diet_Pork_Raspberries["dilution"] #updaing the flux, considering the dilution
diet_Pork_Raspberries[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Pork_Shrimp["dilution"] = 1.0
diet_Pork_Shrimp.loc[diet_Pork_Shrimp.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Pork_Shrimp["flux"] = diet_Pork_Shrimp["flux"] * diet_Pork_Shrimp["dilution"] #updaing the flux, considering the dilution
diet_Pork_Shrimp[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Pork_Soybean["dilution"] = 1.0
diet_Pork_Soybean.loc[diet_Pork_Soybean.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Pork_Soybean["flux"] = diet_Pork_Soybean["flux"] * diet_Pork_Soybean["dilution"] #updaing the flux, considering the dilution
diet_Pork_Soybean[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Pork_Splitpeas["dilution"] = 1.0
diet_Pork_Splitpeas.loc[diet_Pork_Splitpeas.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Pork_Splitpeas["flux"] = diet_Pork_Splitpeas["flux"] * diet_Pork_Splitpeas["dilution"] #updaing the flux, considering the dilution
diet_Pork_Splitpeas[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Pork_Strawberries["dilution"] = 1.0
diet_Pork_Strawberries.loc[diet_Pork_Strawberries.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Pork_Strawberries["flux"] = diet_Pork_Strawberries["flux"] * diet_Pork_Strawberries["dilution"] #updaing the flux, considering the dilution
diet_Pork_Strawberries[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Pork_Sweetpotato["dilution"] = 1.0
diet_Pork_Sweetpotato.loc[diet_Pork_Sweetpotato.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Pork_Sweetpotato["flux"] = diet_Pork_Sweetpotato["flux"] * diet_Pork_Sweetpotato["dilution"] #updaing the flux, considering the dilution
diet_Pork_Sweetpotato[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Pumpkin_Raspberries["dilution"] = 1.0
diet_Pumpkin_Raspberries.loc[diet_Pumpkin_Raspberries.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Pumpkin_Raspberries["flux"] = diet_Pumpkin_Raspberries["flux"] * diet_Pumpkin_Raspberries["dilution"] #updaing the flux, considering the dilution
diet_Pumpkin_Raspberries[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Pumpkin_Shrimp["dilution"] = 1.0
diet_Pumpkin_Shrimp.loc[diet_Pumpkin_Shrimp.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Pumpkin_Shrimp["flux"] = diet_Pumpkin_Shrimp["flux"] * diet_Pumpkin_Shrimp["dilution"] #updaing the flux, considering the dilution
diet_Pumpkin_Shrimp[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Pumpkin_Soybean["dilution"] = 1.0
diet_Pumpkin_Soybean.loc[diet_Pumpkin_Soybean.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Pumpkin_Soybean["flux"] = diet_Pumpkin_Soybean["flux"] * diet_Pumpkin_Soybean["dilution"] #updaing the flux, considering the dilution
diet_Pumpkin_Soybean[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Pumpkin_Splitpeas["dilution"] = 1.0
diet_Pumpkin_Splitpeas.loc[diet_Pumpkin_Splitpeas.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Pumpkin_Splitpeas["flux"] = diet_Pumpkin_Splitpeas["flux"] * diet_Pumpkin_Splitpeas["dilution"] #updaing the flux, considering the dilution
diet_Pumpkin_Splitpeas[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Pumpkin_Strawberries["dilution"] = 1.0
diet_Pumpkin_Strawberries.loc[diet_Pumpkin_Strawberries.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Pumpkin_Strawberries["flux"] = diet_Pumpkin_Strawberries["flux"] * diet_Pumpkin_Strawberries["dilution"] #updaing the flux, considering the dilution
diet_Pumpkin_Strawberries[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Pumpkin_Sweetpotato["dilution"] = 1.0
diet_Pumpkin_Sweetpotato.loc[diet_Pumpkin_Sweetpotato.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Pumpkin_Sweetpotato["flux"] = diet_Pumpkin_Sweetpotato["flux"] * diet_Pumpkin_Sweetpotato["dilution"] #updaing the flux, considering the dilution
diet_Pumpkin_Sweetpotato[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Raspberries_Shrimp["dilution"] = 1.0
diet_Raspberries_Shrimp.loc[diet_Raspberries_Shrimp.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Raspberries_Shrimp["flux"] = diet_Raspberries_Shrimp["flux"] * diet_Raspberries_Shrimp["dilution"] #updaing the flux, considering the dilution
diet_Raspberries_Shrimp[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Raspberries_Soybean["dilution"] = 1.0
diet_Raspberries_Soybean.loc[diet_Raspberries_Soybean.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Raspberries_Soybean["flux"] = diet_Raspberries_Soybean["flux"] * diet_Raspberries_Soybean["dilution"] #updaing the flux, considering the dilution
diet_Raspberries_Soybean[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Raspberries_Splitpeas["dilution"] = 1.0
diet_Raspberries_Splitpeas.loc[diet_Raspberries_Splitpeas.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Raspberries_Splitpeas["flux"] = diet_Raspberries_Splitpeas["flux"] * diet_Raspberries_Splitpeas["dilution"] #updaing the flux, considering the dilution
diet_Raspberries_Splitpeas[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Raspberries_Strawberries["dilution"] = 1.0
diet_Raspberries_Strawberries.loc[diet_Raspberries_Strawberries.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Raspberries_Strawberries["flux"] = diet_Raspberries_Strawberries["flux"] * diet_Raspberries_Strawberries["dilution"] #updaing the flux, considering the dilution
diet_Raspberries_Strawberries[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Raspberries_Sweetpotato["dilution"] = 1.0
diet_Raspberries_Sweetpotato.loc[diet_Raspberries_Sweetpotato.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Raspberries_Sweetpotato["flux"] = diet_Raspberries_Sweetpotato["flux"] * diet_Raspberries_Sweetpotato["dilution"] #updaing the flux, considering the dilution
diet_Raspberries_Sweetpotato[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Shrimp_Soybean["dilution"] = 1.0
diet_Shrimp_Soybean.loc[diet_Shrimp_Soybean.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Shrimp_Soybean["flux"] = diet_Shrimp_Soybean["flux"] * diet_Shrimp_Soybean["dilution"] #updaing the flux, considering the dilution
diet_Shrimp_Soybean[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Shrimp_Splitpeas["dilution"] = 1.0
diet_Shrimp_Splitpeas.loc[diet_Shrimp_Splitpeas.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Shrimp_Splitpeas["flux"] = diet_Shrimp_Splitpeas["flux"] * diet_Shrimp_Splitpeas["dilution"] #updaing the flux, considering the dilution
diet_Shrimp_Splitpeas[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Shrimp_Strawberries["dilution"] = 1.0
diet_Shrimp_Strawberries.loc[diet_Shrimp_Strawberries.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Shrimp_Strawberries["flux"] = diet_Shrimp_Strawberries["flux"] * diet_Shrimp_Strawberries["dilution"] #updaing the flux, considering the dilution
diet_Shrimp_Strawberries[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Shrimp_Sweetpotato["dilution"] = 1.0
diet_Shrimp_Sweetpotato.loc[diet_Shrimp_Sweetpotato.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Shrimp_Sweetpotato["flux"] = diet_Shrimp_Sweetpotato["flux"] * diet_Shrimp_Sweetpotato["dilution"] #updaing the flux, considering the dilution
diet_Shrimp_Sweetpotato[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Soybean_Splitpeas["dilution"] = 1.0
diet_Soybean_Splitpeas.loc[diet_Soybean_Splitpeas.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Soybean_Splitpeas["flux"] = diet_Soybean_Splitpeas["flux"] * diet_Soybean_Splitpeas["dilution"] #updaing the flux, considering the dilution
diet_Soybean_Splitpeas[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Soybean_Strawberries["dilution"] = 1.0
diet_Soybean_Strawberries.loc[diet_Soybean_Strawberries.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Soybean_Strawberries["flux"] = diet_Soybean_Strawberries["flux"] * diet_Soybean_Strawberries["dilution"] #updaing the flux, considering the dilution
diet_Soybean_Strawberries[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Soybean_Sweetpotato["dilution"] = 1.0
diet_Soybean_Sweetpotato.loc[diet_Soybean_Sweetpotato.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Soybean_Sweetpotato["flux"] = diet_Soybean_Sweetpotato["flux"] * diet_Soybean_Sweetpotato["dilution"] #updaing the flux, considering the dilution
diet_Soybean_Sweetpotato[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Splitpeas_Strawberries["dilution"] = 1.0
diet_Splitpeas_Strawberries.loc[diet_Splitpeas_Strawberries.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Splitpeas_Strawberries["flux"] = diet_Splitpeas_Strawberries["flux"] * diet_Splitpeas_Strawberries["dilution"] #updaing the flux, considering the dilution
diet_Splitpeas_Strawberries[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Splitpeas_Sweetpotato["dilution"] = 1.0
diet_Splitpeas_Sweetpotato.loc[diet_Splitpeas_Sweetpotato.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Splitpeas_Sweetpotato["flux"] = diet_Splitpeas_Sweetpotato["flux"] * diet_Splitpeas_Sweetpotato["dilution"] #updaing the flux, considering the dilution
diet_Splitpeas_Sweetpotato[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Strawberries_Sweetpotato["dilution"] = 1.0
diet_Strawberries_Sweetpotato.loc[diet_Strawberries_Sweetpotato.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Strawberries_Sweetpotato["flux"] = diet_Strawberries_Sweetpotato["flux"] * diet_Strawberries_Sweetpotato["dilution"] #updaing the flux, considering the dilution
diet_Strawberries_Sweetpotato[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()

#Adding host secreted substrates
#we consider the flux of these compounds as 1 mmol/h

diet_Blackbeans_Blackcurrant.set_index("metabolite", inplace=True)
diet_Blackbeans_Chickpea.set_index("metabolite", inplace=True)
diet_Blackbeans_Couscous.set_index("metabolite", inplace=True)
diet_Blackbeans_Pork.set_index("metabolite", inplace=True)
diet_Blackbeans_Pumpkin.set_index("metabolite", inplace=True)
diet_Blackbeans_Raspberries.set_index("metabolite", inplace=True)
diet_Blackbeans_Shrimp.set_index("metabolite", inplace=True)
diet_Blackbeans_Soybean.set_index("metabolite", inplace=True)
diet_Blackbeans_Splitpeas.set_index("metabolite", inplace=True)
diet_Blackbeans_Strawberries.set_index("metabolite", inplace=True)
diet_Blackbeans_Sweetpotato.set_index("metabolite", inplace=True)
diet_Blackcurrant_Chickpea.set_index("metabolite", inplace=True)
diet_Blackcurrant_Couscous.set_index("metabolite", inplace=True)
diet_Blackcurrant_Pork.set_index("metabolite", inplace=True)
diet_Blackcurrant_Pumpkin.set_index("metabolite", inplace=True)
diet_Blackcurrant_Raspberries.set_index("metabolite", inplace=True)
diet_Blackcurrant_Shrimp.set_index("metabolite", inplace=True)
diet_Blackcurrant_Soybean.set_index("metabolite", inplace=True)
diet_Blackcurrant_Splitpeas.set_index("metabolite", inplace=True)
diet_Blackcurrant_Strawberries.set_index("metabolite", inplace=True)
diet_Blackcurrant_Sweetpotato.set_index("metabolite", inplace=True)
diet_Chickpea_Couscous.set_index("metabolite", inplace=True)
diet_Chickpea_Pork.set_index("metabolite", inplace=True)
diet_Chickpea_Pumpkin.set_index("metabolite", inplace=True)
diet_Chickpea_Raspberries.set_index("metabolite", inplace=True)
diet_Chickpea_Shrimp.set_index("metabolite", inplace=True)
diet_Chickpea_Soybean.set_index("metabolite", inplace=True)
diet_Chickpea_Splitpeas.set_index("metabolite", inplace=True)
diet_Chickpea_Strawberries.set_index("metabolite", inplace=True)
diet_Chickpea_Sweetpotato.set_index("metabolite", inplace=True)
diet_Couscous_Pork.set_index("metabolite", inplace=True)
diet_Couscous_Pumpkin.set_index("metabolite", inplace=True)
diet_Couscous_Raspberries.set_index("metabolite", inplace=True)
diet_Couscous_Shrimp.set_index("metabolite", inplace=True)
diet_Couscous_Soybean.set_index("metabolite", inplace=True)
diet_Couscous_Splitpeas.set_index("metabolite", inplace=True)
diet_Couscous_Strawberries.set_index("metabolite", inplace=True)
diet_Couscous_Sweetpotato.set_index("metabolite", inplace=True)
diet_Pork_Pumpkin.set_index("metabolite", inplace=True)
diet_Pork_Raspberries.set_index("metabolite", inplace=True)
diet_Pork_Shrimp.set_index("metabolite", inplace=True)
diet_Pork_Soybean.set_index("metabolite", inplace=True)
diet_Pork_Splitpeas.set_index("metabolite", inplace=True)
diet_Pork_Strawberries.set_index("metabolite", inplace=True)
diet_Pork_Sweetpotato.set_index("metabolite", inplace=True)
diet_Pumpkin_Raspberries.set_index("metabolite", inplace=True)
diet_Pumpkin_Shrimp.set_index("metabolite", inplace=True)
diet_Pumpkin_Soybean.set_index("metabolite", inplace=True)
diet_Pumpkin_Splitpeas.set_index("metabolite", inplace=True)
diet_Pumpkin_Strawberries.set_index("metabolite", inplace=True)
diet_Pumpkin_Sweetpotato.set_index("metabolite", inplace=True)
diet_Raspberries_Shrimp.set_index("metabolite", inplace=True)
diet_Raspberries_Soybean.set_index("metabolite", inplace=True)
diet_Raspberries_Splitpeas.set_index("metabolite", inplace=True)
diet_Raspberries_Strawberries.set_index("metabolite", inplace=True)
diet_Raspberries_Sweetpotato.set_index("metabolite", inplace=True)
diet_Shrimp_Soybean.set_index("metabolite", inplace=True)
diet_Shrimp_Splitpeas.set_index("metabolite", inplace=True)
diet_Shrimp_Strawberries.set_index("metabolite", inplace=True)
diet_Shrimp_Sweetpotato.set_index("metabolite", inplace=True)
diet_Soybean_Splitpeas.set_index("metabolite", inplace=True)
diet_Soybean_Strawberries.set_index("metabolite", inplace=True)
diet_Soybean_Sweetpotato.set_index("metabolite", inplace=True)
diet_Splitpeas_Strawberries.set_index("metabolite", inplace=True)
diet_Splitpeas_Sweetpotato.set_index("metabolite", inplace=True)
diet_Strawberries_Sweetpotato.set_index("metabolite", inplace=True)

for met in annotations.loc[annotations.metabolite.str.contains("core"), "metabolite"]: # mucins
    diet_Blackbeans_Blackcurrant.loc[met, "flux"] = 1
    diet_Blackbeans_Chickpea.loc[met, "flux"] = 1
    diet_Blackbeans_Couscous.loc[met, "flux"] = 1
    diet_Blackbeans_Pork.loc[met, "flux"] = 1
    diet_Blackbeans_Pumpkin.loc[met, "flux"] = 1
    diet_Blackbeans_Raspberries.loc[met, "flux"] = 1
    diet_Blackbeans_Shrimp.loc[met, "flux"] = 1
    diet_Blackbeans_Soybean.loc[met, "flux"] = 1
    diet_Blackbeans_Splitpeas.loc[met, "flux"] = 1
    diet_Blackbeans_Strawberries.loc[met, "flux"] = 1
    diet_Blackbeans_Sweetpotato.loc[met, "flux"] = 1
    diet_Blackcurrant_Chickpea.loc[met, "flux"] = 1
    diet_Blackcurrant_Couscous.loc[met, "flux"] = 1
    diet_Blackcurrant_Pork.loc[met, "flux"] = 1
    diet_Blackcurrant_Pumpkin.loc[met, "flux"] = 1
    diet_Blackcurrant_Raspberries.loc[met, "flux"] = 1
    diet_Blackcurrant_Shrimp.loc[met, "flux"] = 1
    diet_Blackcurrant_Soybean.loc[met, "flux"] = 1
    diet_Blackcurrant_Splitpeas.loc[met, "flux"] = 1
    diet_Blackcurrant_Strawberries.loc[met, "flux"] = 1
    diet_Blackcurrant_Sweetpotato.loc[met, "flux"] = 1
    diet_Chickpea_Couscous.loc[met, "flux"] = 1
    diet_Chickpea_Pork.loc[met, "flux"] = 1
    diet_Chickpea_Pumpkin.loc[met, "flux"] = 1
    diet_Chickpea_Raspberries.loc[met, "flux"] = 1
    diet_Chickpea_Shrimp.loc[met, "flux"] = 1
    diet_Chickpea_Soybean.loc[met, "flux"] = 1
    diet_Chickpea_Splitpeas.loc[met, "flux"] = 1
    diet_Chickpea_Strawberries.loc[met, "flux"] = 1
    diet_Chickpea_Sweetpotato.loc[met, "flux"] = 1
    diet_Couscous_Pork.loc[met, "flux"] = 1
    diet_Couscous_Pumpkin.loc[met, "flux"] = 1
    diet_Couscous_Raspberries.loc[met, "flux"] = 1
    diet_Couscous_Shrimp.loc[met, "flux"] = 1
    diet_Couscous_Soybean.loc[met, "flux"] = 1
    diet_Couscous_Splitpeas.loc[met, "flux"] = 1
    diet_Couscous_Strawberries.loc[met, "flux"] = 1
    diet_Couscous_Sweetpotato.loc[met, "flux"] = 1
    diet_Pork_Pumpkin.loc[met, "flux"] = 1
    diet_Pork_Raspberries.loc[met, "flux"] = 1
    diet_Pork_Shrimp.loc[met, "flux"] = 1
    diet_Pork_Soybean.loc[met, "flux"] = 1
    diet_Pork_Splitpeas.loc[met, "flux"] = 1
    diet_Pork_Strawberries.loc[met, "flux"] = 1
    diet_Pork_Sweetpotato.loc[met, "flux"] = 1
    diet_Pumpkin_Raspberries.loc[met, "flux"] = 1
    diet_Pumpkin_Shrimp.loc[met, "flux"] = 1
    diet_Pumpkin_Soybean.loc[met, "flux"] = 1
    diet_Pumpkin_Splitpeas.loc[met, "flux"] = 1
    diet_Pumpkin_Strawberries.loc[met, "flux"] = 1
    diet_Pumpkin_Sweetpotato.loc[met, "flux"] = 1
    diet_Raspberries_Shrimp.loc[met, "flux"] = 1
    diet_Raspberries_Soybean.loc[met, "flux"] = 1
    diet_Raspberries_Splitpeas.loc[met, "flux"] = 1
    diet_Raspberries_Strawberries.loc[met, "flux"] = 1
    diet_Raspberries_Sweetpotato.loc[met, "flux"] = 1
    diet_Shrimp_Soybean.loc[met, "flux"] = 1
    diet_Shrimp_Splitpeas.loc[met, "flux"] = 1
    diet_Shrimp_Strawberries.loc[met, "flux"] = 1
    diet_Shrimp_Sweetpotato.loc[met, "flux"] = 1
    diet_Soybean_Splitpeas.loc[met, "flux"] = 1
    diet_Soybean_Strawberries.loc[met, "flux"] = 1
    diet_Soybean_Sweetpotato.loc[met, "flux"] = 1
    diet_Splitpeas_Strawberries.loc[met, "flux"] = 1
    diet_Splitpeas_Sweetpotato.loc[met, "flux"] = 1
    diet_Strawberries_Sweetpotato.loc[met, "flux"] = 1

for met in ["gchola", "tchola"]: # primary BAs
    diet_Blackbeans_Blackcurrant.loc[met, "flux"] = 1
    diet_Blackbeans_Chickpea.loc[met, "flux"] = 1
    diet_Blackbeans_Couscous.loc[met, "flux"] = 1
    diet_Blackbeans_Pork.loc[met, "flux"] = 1
    diet_Blackbeans_Pumpkin.loc[met, "flux"] = 1
    diet_Blackbeans_Raspberries.loc[met, "flux"] = 1
    diet_Blackbeans_Shrimp.loc[met, "flux"] = 1
    diet_Blackbeans_Soybean.loc[met, "flux"] = 1
    diet_Blackbeans_Splitpeas.loc[met, "flux"] = 1
    diet_Blackbeans_Strawberries.loc[met, "flux"] = 1
    diet_Blackbeans_Sweetpotato.loc[met, "flux"] = 1
    diet_Blackcurrant_Chickpea.loc[met, "flux"] = 1
    diet_Blackcurrant_Couscous.loc[met, "flux"] = 1
    diet_Blackcurrant_Pork.loc[met, "flux"] = 1
    diet_Blackcurrant_Pumpkin.loc[met, "flux"] = 1
    diet_Blackcurrant_Raspberries.loc[met, "flux"] = 1
    diet_Blackcurrant_Shrimp.loc[met, "flux"] = 1
    diet_Blackcurrant_Soybean.loc[met, "flux"] = 1
    diet_Blackcurrant_Splitpeas.loc[met, "flux"] = 1
    diet_Blackcurrant_Strawberries.loc[met, "flux"] = 1
    diet_Blackcurrant_Sweetpotato.loc[met, "flux"] = 1
    diet_Chickpea_Couscous.loc[met, "flux"] = 1
    diet_Chickpea_Pork.loc[met, "flux"] = 1
    diet_Chickpea_Pumpkin.loc[met, "flux"] = 1
    diet_Chickpea_Raspberries.loc[met, "flux"] = 1
    diet_Chickpea_Shrimp.loc[met, "flux"] = 1
    diet_Chickpea_Soybean.loc[met, "flux"] = 1
    diet_Chickpea_Splitpeas.loc[met, "flux"] = 1
    diet_Chickpea_Strawberries.loc[met, "flux"] = 1
    diet_Chickpea_Sweetpotato.loc[met, "flux"] = 1
    diet_Couscous_Pork.loc[met, "flux"] = 1
    diet_Couscous_Pumpkin.loc[met, "flux"] = 1
    diet_Couscous_Raspberries.loc[met, "flux"] = 1
    diet_Couscous_Shrimp.loc[met, "flux"] = 1
    diet_Couscous_Soybean.loc[met, "flux"] = 1
    diet_Couscous_Splitpeas.loc[met, "flux"] = 1
    diet_Couscous_Strawberries.loc[met, "flux"] = 1
    diet_Couscous_Sweetpotato.loc[met, "flux"] = 1
    diet_Pork_Pumpkin.loc[met, "flux"] = 1
    diet_Pork_Raspberries.loc[met, "flux"] = 1
    diet_Pork_Shrimp.loc[met, "flux"] = 1
    diet_Pork_Soybean.loc[met, "flux"] = 1
    diet_Pork_Splitpeas.loc[met, "flux"] = 1
    diet_Pork_Strawberries.loc[met, "flux"] = 1
    diet_Pork_Sweetpotato.loc[met, "flux"] = 1
    diet_Pumpkin_Raspberries.loc[met, "flux"] = 1
    diet_Pumpkin_Shrimp.loc[met, "flux"] = 1
    diet_Pumpkin_Soybean.loc[met, "flux"] = 1
    diet_Pumpkin_Splitpeas.loc[met, "flux"] = 1
    diet_Pumpkin_Strawberries.loc[met, "flux"] = 1
    diet_Pumpkin_Sweetpotato.loc[met, "flux"] = 1
    diet_Raspberries_Shrimp.loc[met, "flux"] = 1
    diet_Raspberries_Soybean.loc[met, "flux"] = 1
    diet_Raspberries_Splitpeas.loc[met, "flux"] = 1
    diet_Raspberries_Strawberries.loc[met, "flux"] = 1
    diet_Raspberries_Sweetpotato.loc[met, "flux"] = 1
    diet_Shrimp_Soybean.loc[met, "flux"] = 1
    diet_Shrimp_Splitpeas.loc[met, "flux"] = 1
    diet_Shrimp_Strawberries.loc[met, "flux"] = 1
    diet_Shrimp_Sweetpotato.loc[met, "flux"] = 1
    diet_Soybean_Splitpeas.loc[met, "flux"] = 1
    diet_Soybean_Strawberries.loc[met, "flux"] = 1
    diet_Soybean_Sweetpotato.loc[met, "flux"] = 1
    diet_Splitpeas_Strawberries.loc[met, "flux"] = 1
    diet_Splitpeas_Sweetpotato.loc[met, "flux"] = 1
    diet_Strawberries_Sweetpotato.loc[met, "flux"] = 1

diet_Blackbeans_Blackcurrant.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Blackbeans_Chickpea.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Blackbeans_Couscous.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Blackbeans_Pork.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Blackbeans_Pumpkin.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Blackbeans_Raspberries.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Blackbeans_Shrimp.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Blackbeans_Soybean.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Blackbeans_Splitpeas.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Blackbeans_Strawberries.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Blackbeans_Sweetpotato.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Blackcurrant_Chickpea.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Blackcurrant_Couscous.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Blackcurrant_Pork.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Blackcurrant_Pumpkin.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Blackcurrant_Raspberries.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Blackcurrant_Shrimp.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Blackcurrant_Soybean.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Blackcurrant_Splitpeas.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Blackcurrant_Strawberries.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Blackcurrant_Sweetpotato.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Chickpea_Couscous.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Chickpea_Pork.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Chickpea_Pumpkin.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Chickpea_Raspberries.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Chickpea_Shrimp.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Chickpea_Soybean.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Chickpea_Splitpeas.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Chickpea_Strawberries.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Chickpea_Sweetpotato.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Couscous_Pork.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Couscous_Pumpkin.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Couscous_Raspberries.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Couscous_Shrimp.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Couscous_Soybean.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Couscous_Splitpeas.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Couscous_Strawberries.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Couscous_Sweetpotato.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Pork_Pumpkin.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Pork_Raspberries.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Pork_Shrimp.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Pork_Soybean.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Pork_Splitpeas.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Pork_Strawberries.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Pork_Sweetpotato.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Pumpkin_Raspberries.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Pumpkin_Shrimp.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Pumpkin_Soybean.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Pumpkin_Splitpeas.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Pumpkin_Strawberries.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Pumpkin_Sweetpotato.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Raspberries_Shrimp.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Raspberries_Soybean.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Raspberries_Splitpeas.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Raspberries_Strawberries.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Raspberries_Sweetpotato.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Shrimp_Soybean.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Shrimp_Splitpeas.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Shrimp_Strawberries.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Shrimp_Sweetpotato.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Soybean_Splitpeas.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Soybean_Strawberries.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Soybean_Sweetpotato.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Splitpeas_Strawberries.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Splitpeas_Sweetpotato.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Strawberries_Sweetpotato.loc["o2", "flux"] = 0.001 # anaerobic environment

diet_Blackbeans_Blackcurrant.reset_index(inplace=True)
diet_Blackbeans_Blackcurrant["reaction"] = "EX_" + diet_Blackbeans_Blackcurrant.metabolite + "(e)"
diet_Blackbeans_Chickpea.reset_index(inplace=True)
diet_Blackbeans_Chickpea["reaction"] = "EX_" + diet_Blackbeans_Chickpea.metabolite + "(e)"
diet_Blackbeans_Couscous.reset_index(inplace=True)
diet_Blackbeans_Couscous["reaction"] = "EX_" + diet_Blackbeans_Couscous.metabolite + "(e)"
diet_Blackbeans_Pork.reset_index(inplace=True)
diet_Blackbeans_Pork["reaction"] = "EX_" + diet_Blackbeans_Pork.metabolite + "(e)"
diet_Blackbeans_Pumpkin.reset_index(inplace=True)
diet_Blackbeans_Pumpkin["reaction"] = "EX_" + diet_Blackbeans_Pumpkin.metabolite + "(e)"
diet_Blackbeans_Raspberries.reset_index(inplace=True)
diet_Blackbeans_Raspberries["reaction"] = "EX_" + diet_Blackbeans_Raspberries.metabolite + "(e)"
diet_Blackbeans_Shrimp.reset_index(inplace=True)
diet_Blackbeans_Shrimp["reaction"] = "EX_" + diet_Blackbeans_Shrimp.metabolite + "(e)"
diet_Blackbeans_Soybean.reset_index(inplace=True)
diet_Blackbeans_Soybean["reaction"] = "EX_" + diet_Blackbeans_Soybean.metabolite + "(e)"
diet_Blackbeans_Splitpeas.reset_index(inplace=True)
diet_Blackbeans_Splitpeas["reaction"] = "EX_" + diet_Blackbeans_Splitpeas.metabolite + "(e)"
diet_Blackbeans_Strawberries.reset_index(inplace=True)
diet_Blackbeans_Strawberries["reaction"] = "EX_" + diet_Blackbeans_Strawberries.metabolite + "(e)"
diet_Blackbeans_Sweetpotato.reset_index(inplace=True)
diet_Blackbeans_Sweetpotato["reaction"] = "EX_" + diet_Blackbeans_Sweetpotato.metabolite + "(e)"
diet_Blackcurrant_Chickpea.reset_index(inplace=True)
diet_Blackcurrant_Chickpea["reaction"] = "EX_" + diet_Blackcurrant_Chickpea.metabolite + "(e)"
diet_Blackcurrant_Couscous.reset_index(inplace=True)
diet_Blackcurrant_Couscous["reaction"] = "EX_" + diet_Blackcurrant_Couscous.metabolite + "(e)"
diet_Blackcurrant_Pork.reset_index(inplace=True)
diet_Blackcurrant_Pork["reaction"] = "EX_" + diet_Blackcurrant_Pork.metabolite + "(e)"
diet_Blackcurrant_Pumpkin.reset_index(inplace=True)
diet_Blackcurrant_Pumpkin["reaction"] = "EX_" + diet_Blackcurrant_Pumpkin.metabolite + "(e)"
diet_Blackcurrant_Raspberries.reset_index(inplace=True)
diet_Blackcurrant_Raspberries["reaction"] = "EX_" + diet_Blackcurrant_Raspberries.metabolite + "(e)"
diet_Blackcurrant_Shrimp.reset_index(inplace=True)
diet_Blackcurrant_Shrimp["reaction"] = "EX_" + diet_Blackcurrant_Shrimp.metabolite + "(e)"
diet_Blackcurrant_Soybean.reset_index(inplace=True)
diet_Blackcurrant_Soybean["reaction"] = "EX_" + diet_Blackcurrant_Soybean.metabolite + "(e)"
diet_Blackcurrant_Splitpeas.reset_index(inplace=True)
diet_Blackcurrant_Splitpeas["reaction"] = "EX_" + diet_Blackcurrant_Splitpeas.metabolite + "(e)"
diet_Blackcurrant_Strawberries.reset_index(inplace=True)
diet_Blackcurrant_Strawberries["reaction"] = "EX_" + diet_Blackcurrant_Strawberries.metabolite + "(e)"
diet_Blackcurrant_Sweetpotato.reset_index(inplace=True)
diet_Blackcurrant_Sweetpotato["reaction"] = "EX_" + diet_Blackcurrant_Sweetpotato.metabolite + "(e)"
diet_Chickpea_Couscous.reset_index(inplace=True)
diet_Chickpea_Couscous["reaction"] = "EX_" + diet_Chickpea_Couscous.metabolite + "(e)"
diet_Chickpea_Pork.reset_index(inplace=True)
diet_Chickpea_Pork["reaction"] = "EX_" + diet_Chickpea_Pork.metabolite + "(e)"
diet_Chickpea_Pumpkin.reset_index(inplace=True)
diet_Chickpea_Pumpkin["reaction"] = "EX_" + diet_Chickpea_Pumpkin.metabolite + "(e)"
diet_Chickpea_Raspberries.reset_index(inplace=True)
diet_Chickpea_Raspberries["reaction"] = "EX_" + diet_Chickpea_Raspberries.metabolite + "(e)"
diet_Chickpea_Shrimp.reset_index(inplace=True)
diet_Chickpea_Shrimp["reaction"] = "EX_" + diet_Chickpea_Shrimp.metabolite + "(e)"
diet_Chickpea_Soybean.reset_index(inplace=True)
diet_Chickpea_Soybean["reaction"] = "EX_" + diet_Chickpea_Soybean.metabolite + "(e)"
diet_Chickpea_Splitpeas.reset_index(inplace=True)
diet_Chickpea_Splitpeas["reaction"] = "EX_" + diet_Chickpea_Splitpeas.metabolite + "(e)"
diet_Chickpea_Strawberries.reset_index(inplace=True)
diet_Chickpea_Strawberries["reaction"] = "EX_" + diet_Chickpea_Strawberries.metabolite + "(e)"
diet_Chickpea_Sweetpotato.reset_index(inplace=True)
diet_Chickpea_Sweetpotato["reaction"] = "EX_" + diet_Chickpea_Sweetpotato.metabolite + "(e)"
diet_Couscous_Pork.reset_index(inplace=True)
diet_Couscous_Pork["reaction"] = "EX_" + diet_Couscous_Pork.metabolite + "(e)"
diet_Couscous_Pumpkin.reset_index(inplace=True)
diet_Couscous_Pumpkin["reaction"] = "EX_" + diet_Couscous_Pumpkin.metabolite + "(e)"
diet_Couscous_Raspberries.reset_index(inplace=True)
diet_Couscous_Raspberries["reaction"] = "EX_" + diet_Couscous_Raspberries.metabolite + "(e)"
diet_Couscous_Shrimp.reset_index(inplace=True)
diet_Couscous_Shrimp["reaction"] = "EX_" + diet_Couscous_Shrimp.metabolite + "(e)"
diet_Couscous_Soybean.reset_index(inplace=True)
diet_Couscous_Soybean["reaction"] = "EX_" + diet_Couscous_Soybean.metabolite + "(e)"
diet_Couscous_Splitpeas.reset_index(inplace=True)
diet_Couscous_Splitpeas["reaction"] = "EX_" + diet_Couscous_Splitpeas.metabolite + "(e)"
diet_Couscous_Strawberries.reset_index(inplace=True)
diet_Couscous_Strawberries["reaction"] = "EX_" + diet_Couscous_Strawberries.metabolite + "(e)"
diet_Couscous_Sweetpotato.reset_index(inplace=True)
diet_Couscous_Sweetpotato["reaction"] = "EX_" + diet_Couscous_Sweetpotato.metabolite + "(e)"
diet_Pork_Pumpkin.reset_index(inplace=True)
diet_Pork_Pumpkin["reaction"] = "EX_" + diet_Pork_Pumpkin.metabolite + "(e)"
diet_Pork_Raspberries.reset_index(inplace=True)
diet_Pork_Raspberries["reaction"] = "EX_" + diet_Pork_Raspberries.metabolite + "(e)"
diet_Pork_Shrimp.reset_index(inplace=True)
diet_Pork_Shrimp["reaction"] = "EX_" + diet_Pork_Shrimp.metabolite + "(e)"
diet_Pork_Soybean.reset_index(inplace=True)
diet_Pork_Soybean["reaction"] = "EX_" + diet_Pork_Soybean.metabolite + "(e)"
diet_Pork_Splitpeas.reset_index(inplace=True)
diet_Pork_Splitpeas["reaction"] = "EX_" + diet_Pork_Splitpeas.metabolite + "(e)"
diet_Pork_Strawberries.reset_index(inplace=True)
diet_Pork_Strawberries["reaction"] = "EX_" + diet_Pork_Strawberries.metabolite + "(e)"
diet_Pork_Sweetpotato.reset_index(inplace=True)
diet_Pork_Sweetpotato["reaction"] = "EX_" + diet_Pork_Sweetpotato.metabolite + "(e)"
diet_Pumpkin_Raspberries.reset_index(inplace=True)
diet_Pumpkin_Raspberries["reaction"] = "EX_" + diet_Pumpkin_Raspberries.metabolite + "(e)"
diet_Pumpkin_Shrimp.reset_index(inplace=True)
diet_Pumpkin_Shrimp["reaction"] = "EX_" + diet_Pumpkin_Shrimp.metabolite + "(e)"
diet_Pumpkin_Soybean.reset_index(inplace=True)
diet_Pumpkin_Soybean["reaction"] = "EX_" + diet_Pumpkin_Soybean.metabolite + "(e)"
diet_Pumpkin_Splitpeas.reset_index(inplace=True)
diet_Pumpkin_Splitpeas["reaction"] = "EX_" + diet_Pumpkin_Splitpeas.metabolite + "(e)"
diet_Pumpkin_Strawberries.reset_index(inplace=True)
diet_Pumpkin_Strawberries["reaction"] = "EX_" + diet_Pumpkin_Strawberries.metabolite + "(e)"
diet_Pumpkin_Sweetpotato.reset_index(inplace=True)
diet_Pumpkin_Sweetpotato["reaction"] = "EX_" + diet_Pumpkin_Sweetpotato.metabolite + "(e)"
diet_Raspberries_Shrimp.reset_index(inplace=True)
diet_Raspberries_Shrimp["reaction"] = "EX_" + diet_Raspberries_Shrimp.metabolite + "(e)"
diet_Raspberries_Soybean.reset_index(inplace=True)
diet_Raspberries_Soybean["reaction"] = "EX_" + diet_Raspberries_Soybean.metabolite + "(e)"
diet_Raspberries_Splitpeas.reset_index(inplace=True)
diet_Raspberries_Splitpeas["reaction"] = "EX_" + diet_Raspberries_Splitpeas.metabolite + "(e)"
diet_Raspberries_Strawberries.reset_index(inplace=True)
diet_Raspberries_Strawberries["reaction"] = "EX_" + diet_Raspberries_Strawberries.metabolite + "(e)"
diet_Raspberries_Sweetpotato.reset_index(inplace=True)
diet_Raspberries_Sweetpotato["reaction"] = "EX_" + diet_Raspberries_Sweetpotato.metabolite + "(e)"
diet_Shrimp_Soybean.reset_index(inplace=True)
diet_Shrimp_Soybean["reaction"] = "EX_" + diet_Shrimp_Soybean.metabolite + "(e)"
diet_Shrimp_Splitpeas.reset_index(inplace=True)
diet_Shrimp_Splitpeas["reaction"] = "EX_" + diet_Shrimp_Splitpeas.metabolite + "(e)"
diet_Shrimp_Strawberries.reset_index(inplace=True)
diet_Shrimp_Strawberries["reaction"] = "EX_" + diet_Shrimp_Strawberries.metabolite + "(e)"
diet_Shrimp_Sweetpotato.reset_index(inplace=True)
diet_Shrimp_Sweetpotato["reaction"] = "EX_" + diet_Shrimp_Sweetpotato.metabolite + "(e)"
diet_Soybean_Splitpeas.reset_index(inplace=True)
diet_Soybean_Splitpeas["reaction"] = "EX_" + diet_Soybean_Splitpeas.metabolite + "(e)"
diet_Soybean_Strawberries.reset_index(inplace=True)
diet_Soybean_Strawberries["reaction"] = "EX_" + diet_Soybean_Strawberries.metabolite + "(e)"
diet_Soybean_Sweetpotato.reset_index(inplace=True)
diet_Soybean_Sweetpotato["reaction"] = "EX_" + diet_Soybean_Sweetpotato.metabolite + "(e)"
diet_Splitpeas_Strawberries.reset_index(inplace=True)
diet_Splitpeas_Strawberries["reaction"] = "EX_" + diet_Splitpeas_Strawberries.metabolite + "(e)"
diet_Splitpeas_Sweetpotato.reset_index(inplace=True)
diet_Splitpeas_Sweetpotato["reaction"] = "EX_" + diet_Splitpeas_Sweetpotato.metabolite + "(e)"
diet_Strawberries_Sweetpotato.reset_index(inplace=True)
diet_Strawberries_Sweetpotato["reaction"] = "EX_" + diet_Strawberries_Sweetpotato.metabolite + "(e)"

#Adding information in our diet table
skeleton_Blackbeans_Blackcurrant = pd.merge(diet_Blackbeans_Blackcurrant, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Blackbeans_Blackcurrant["global_id"] = skeleton_Blackbeans_Blackcurrant.reaction
skeleton_Blackbeans_Blackcurrant["reaction"] = "EX_" + skeleton_Blackbeans_Blackcurrant.metabolite + "_m"
skeleton_Blackbeans_Chickpea = pd.merge(diet_Blackbeans_Chickpea, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Blackbeans_Chickpea["global_id"] = skeleton_Blackbeans_Chickpea.reaction
skeleton_Blackbeans_Chickpea["reaction"] = "EX_" + skeleton_Blackbeans_Chickpea.metabolite + "_m"
skeleton_Blackbeans_Couscous = pd.merge(diet_Blackbeans_Couscous, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Blackbeans_Couscous["global_id"] = skeleton_Blackbeans_Couscous.reaction
skeleton_Blackbeans_Couscous["reaction"] = "EX_" + skeleton_Blackbeans_Couscous.metabolite + "_m"
skeleton_Blackbeans_Pork = pd.merge(diet_Blackbeans_Pork, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Blackbeans_Pork["global_id"] = skeleton_Blackbeans_Pork.reaction
skeleton_Blackbeans_Pork["reaction"] = "EX_" + skeleton_Blackbeans_Pork.metabolite + "_m"
skeleton_Blackbeans_Pumpkin = pd.merge(diet_Blackbeans_Pumpkin, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Blackbeans_Pumpkin["global_id"] = skeleton_Blackbeans_Pumpkin.reaction
skeleton_Blackbeans_Pumpkin["reaction"] = "EX_" + skeleton_Blackbeans_Pumpkin.metabolite + "_m"
skeleton_Blackbeans_Raspberries = pd.merge(diet_Blackbeans_Raspberries, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Blackbeans_Raspberries["global_id"] = skeleton_Blackbeans_Raspberries.reaction
skeleton_Blackbeans_Raspberries["reaction"] = "EX_" + skeleton_Blackbeans_Raspberries.metabolite + "_m"
skeleton_Blackbeans_Shrimp = pd.merge(diet_Blackbeans_Shrimp, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Blackbeans_Shrimp["global_id"] = skeleton_Blackbeans_Shrimp.reaction
skeleton_Blackbeans_Shrimp["reaction"] = "EX_" + skeleton_Blackbeans_Shrimp.metabolite + "_m"
skeleton_Blackbeans_Soybean = pd.merge(diet_Blackbeans_Soybean, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Blackbeans_Soybean["global_id"] = skeleton_Blackbeans_Soybean.reaction
skeleton_Blackbeans_Soybean["reaction"] = "EX_" + skeleton_Blackbeans_Soybean.metabolite + "_m"
skeleton_Blackbeans_Splitpeas = pd.merge(diet_Blackbeans_Splitpeas, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Blackbeans_Splitpeas["global_id"] = skeleton_Blackbeans_Splitpeas.reaction
skeleton_Blackbeans_Splitpeas["reaction"] = "EX_" + skeleton_Blackbeans_Splitpeas.metabolite + "_m"
skeleton_Blackbeans_Strawberries = pd.merge(diet_Blackbeans_Strawberries, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Blackbeans_Strawberries["global_id"] = skeleton_Blackbeans_Strawberries.reaction
skeleton_Blackbeans_Strawberries["reaction"] = "EX_" + skeleton_Blackbeans_Strawberries.metabolite + "_m"
skeleton_Blackbeans_Sweetpotato = pd.merge(diet_Blackbeans_Sweetpotato, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Blackbeans_Sweetpotato["global_id"] = skeleton_Blackbeans_Sweetpotato.reaction
skeleton_Blackbeans_Sweetpotato["reaction"] = "EX_" + skeleton_Blackbeans_Sweetpotato.metabolite + "_m"
skeleton_Blackcurrant_Chickpea = pd.merge(diet_Blackcurrant_Chickpea, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Blackcurrant_Chickpea["global_id"] = skeleton_Blackcurrant_Chickpea.reaction
skeleton_Blackcurrant_Chickpea["reaction"] = "EX_" + skeleton_Blackcurrant_Chickpea.metabolite + "_m"
skeleton_Blackcurrant_Couscous = pd.merge(diet_Blackcurrant_Couscous, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Blackcurrant_Couscous["global_id"] = skeleton_Blackcurrant_Couscous.reaction
skeleton_Blackcurrant_Couscous["reaction"] = "EX_" + skeleton_Blackcurrant_Couscous.metabolite + "_m"
skeleton_Blackcurrant_Pork = pd.merge(diet_Blackcurrant_Pork, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Blackcurrant_Pork["global_id"] = skeleton_Blackcurrant_Pork.reaction
skeleton_Blackcurrant_Pork["reaction"] = "EX_" + skeleton_Blackcurrant_Pork.metabolite + "_m"
skeleton_Blackcurrant_Pumpkin = pd.merge(diet_Blackcurrant_Pumpkin, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Blackcurrant_Pumpkin["global_id"] = skeleton_Blackcurrant_Pumpkin.reaction
skeleton_Blackcurrant_Pumpkin["reaction"] = "EX_" + skeleton_Blackcurrant_Pumpkin.metabolite + "_m"
skeleton_Blackcurrant_Raspberries = pd.merge(diet_Blackcurrant_Raspberries, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Blackcurrant_Raspberries["global_id"] = skeleton_Blackcurrant_Raspberries.reaction
skeleton_Blackcurrant_Raspberries["reaction"] = "EX_" + skeleton_Blackcurrant_Raspberries.metabolite + "_m"
skeleton_Blackcurrant_Shrimp = pd.merge(diet_Blackcurrant_Shrimp, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Blackcurrant_Shrimp["global_id"] = skeleton_Blackcurrant_Shrimp.reaction
skeleton_Blackcurrant_Shrimp["reaction"] = "EX_" + skeleton_Blackcurrant_Shrimp.metabolite + "_m"
skeleton_Blackcurrant_Soybean = pd.merge(diet_Blackcurrant_Soybean, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Blackcurrant_Soybean["global_id"] = skeleton_Blackcurrant_Soybean.reaction
skeleton_Blackcurrant_Soybean["reaction"] = "EX_" + skeleton_Blackcurrant_Soybean.metabolite + "_m"
skeleton_Blackcurrant_Splitpeas = pd.merge(diet_Blackcurrant_Splitpeas, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Blackcurrant_Splitpeas["global_id"] = skeleton_Blackcurrant_Splitpeas.reaction
skeleton_Blackcurrant_Splitpeas["reaction"] = "EX_" + skeleton_Blackcurrant_Splitpeas.metabolite + "_m"
skeleton_Blackcurrant_Strawberries = pd.merge(diet_Blackcurrant_Strawberries, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Blackcurrant_Strawberries["global_id"] = skeleton_Blackcurrant_Strawberries.reaction
skeleton_Blackcurrant_Strawberries["reaction"] = "EX_" + skeleton_Blackcurrant_Strawberries.metabolite + "_m"
skeleton_Blackcurrant_Sweetpotato = pd.merge(diet_Blackcurrant_Sweetpotato, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Blackcurrant_Sweetpotato["global_id"] = skeleton_Blackcurrant_Sweetpotato.reaction
skeleton_Blackcurrant_Sweetpotato["reaction"] = "EX_" + skeleton_Blackcurrant_Sweetpotato.metabolite + "_m"
skeleton_Chickpea_Couscous = pd.merge(diet_Chickpea_Couscous, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Chickpea_Couscous["global_id"] = skeleton_Chickpea_Couscous.reaction
skeleton_Chickpea_Couscous["reaction"] = "EX_" + skeleton_Chickpea_Couscous.metabolite + "_m"
skeleton_Chickpea_Pork = pd.merge(diet_Chickpea_Pork, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Chickpea_Pork["global_id"] = skeleton_Chickpea_Pork.reaction
skeleton_Chickpea_Pork["reaction"] = "EX_" + skeleton_Chickpea_Pork.metabolite + "_m"
skeleton_Chickpea_Pumpkin = pd.merge(diet_Chickpea_Pumpkin, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Chickpea_Pumpkin["global_id"] = skeleton_Chickpea_Pumpkin.reaction
skeleton_Chickpea_Pumpkin["reaction"] = "EX_" + skeleton_Chickpea_Pumpkin.metabolite + "_m"
skeleton_Chickpea_Raspberries = pd.merge(diet_Chickpea_Raspberries, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Chickpea_Raspberries["global_id"] = skeleton_Chickpea_Raspberries.reaction
skeleton_Chickpea_Raspberries["reaction"] = "EX_" + skeleton_Chickpea_Raspberries.metabolite + "_m"
skeleton_Chickpea_Shrimp = pd.merge(diet_Chickpea_Shrimp, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Chickpea_Shrimp["global_id"] = skeleton_Chickpea_Shrimp.reaction
skeleton_Chickpea_Shrimp["reaction"] = "EX_" + skeleton_Chickpea_Shrimp.metabolite + "_m"
skeleton_Chickpea_Soybean = pd.merge(diet_Chickpea_Soybean, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Chickpea_Soybean["global_id"] = skeleton_Chickpea_Soybean.reaction
skeleton_Chickpea_Soybean["reaction"] = "EX_" + skeleton_Chickpea_Soybean.metabolite + "_m"
skeleton_Chickpea_Splitpeas = pd.merge(diet_Chickpea_Splitpeas, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Chickpea_Splitpeas["global_id"] = skeleton_Chickpea_Splitpeas.reaction
skeleton_Chickpea_Splitpeas["reaction"] = "EX_" + skeleton_Chickpea_Splitpeas.metabolite + "_m"
skeleton_Chickpea_Strawberries = pd.merge(diet_Chickpea_Strawberries, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Chickpea_Strawberries["global_id"] = skeleton_Chickpea_Strawberries.reaction
skeleton_Chickpea_Strawberries["reaction"] = "EX_" + skeleton_Chickpea_Strawberries.metabolite + "_m"
skeleton_Chickpea_Sweetpotato = pd.merge(diet_Chickpea_Sweetpotato, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Chickpea_Sweetpotato["global_id"] = skeleton_Chickpea_Sweetpotato.reaction
skeleton_Chickpea_Sweetpotato["reaction"] = "EX_" + skeleton_Chickpea_Sweetpotato.metabolite + "_m"
skeleton_Couscous_Pork = pd.merge(diet_Couscous_Pork, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Couscous_Pork["global_id"] = skeleton_Couscous_Pork.reaction
skeleton_Couscous_Pork["reaction"] = "EX_" + skeleton_Couscous_Pork.metabolite + "_m"
skeleton_Couscous_Pumpkin = pd.merge(diet_Couscous_Pumpkin, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Couscous_Pumpkin["global_id"] = skeleton_Couscous_Pumpkin.reaction
skeleton_Couscous_Pumpkin["reaction"] = "EX_" + skeleton_Couscous_Pumpkin.metabolite + "_m"
skeleton_Couscous_Raspberries = pd.merge(diet_Couscous_Raspberries, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Couscous_Raspberries["global_id"] = skeleton_Couscous_Raspberries.reaction
skeleton_Couscous_Raspberries["reaction"] = "EX_" + skeleton_Couscous_Raspberries.metabolite + "_m"
skeleton_Couscous_Shrimp = pd.merge(diet_Couscous_Shrimp, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Couscous_Shrimp["global_id"] = skeleton_Couscous_Shrimp.reaction
skeleton_Couscous_Shrimp["reaction"] = "EX_" + skeleton_Couscous_Shrimp.metabolite + "_m"
skeleton_Couscous_Soybean = pd.merge(diet_Couscous_Soybean, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Couscous_Soybean["global_id"] = skeleton_Couscous_Soybean.reaction
skeleton_Couscous_Soybean["reaction"] = "EX_" + skeleton_Couscous_Soybean.metabolite + "_m"
skeleton_Couscous_Splitpeas = pd.merge(diet_Couscous_Splitpeas, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Couscous_Splitpeas["global_id"] = skeleton_Couscous_Splitpeas.reaction
skeleton_Couscous_Splitpeas["reaction"] = "EX_" + skeleton_Couscous_Splitpeas.metabolite + "_m"
skeleton_Couscous_Strawberries = pd.merge(diet_Couscous_Strawberries, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Couscous_Strawberries["global_id"] = skeleton_Couscous_Strawberries.reaction
skeleton_Couscous_Strawberries["reaction"] = "EX_" + skeleton_Couscous_Strawberries.metabolite + "_m"
skeleton_Couscous_Sweetpotato = pd.merge(diet_Couscous_Sweetpotato, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Couscous_Sweetpotato["global_id"] = skeleton_Couscous_Sweetpotato.reaction
skeleton_Couscous_Sweetpotato["reaction"] = "EX_" + skeleton_Couscous_Sweetpotato.metabolite + "_m"
skeleton_Pork_Pumpkin = pd.merge(diet_Pork_Pumpkin, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Pork_Pumpkin["global_id"] = skeleton_Pork_Pumpkin.reaction
skeleton_Pork_Pumpkin["reaction"] = "EX_" + skeleton_Pork_Pumpkin.metabolite + "_m"
skeleton_Pork_Raspberries = pd.merge(diet_Pork_Raspberries, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Pork_Raspberries["global_id"] = skeleton_Pork_Raspberries.reaction
skeleton_Pork_Raspberries["reaction"] = "EX_" + skeleton_Pork_Raspberries.metabolite + "_m"
skeleton_Pork_Shrimp = pd.merge(diet_Pork_Shrimp, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Pork_Shrimp["global_id"] = skeleton_Pork_Shrimp.reaction
skeleton_Pork_Shrimp["reaction"] = "EX_" + skeleton_Pork_Shrimp.metabolite + "_m"
skeleton_Pork_Soybean = pd.merge(diet_Pork_Soybean, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Pork_Soybean["global_id"] = skeleton_Pork_Soybean.reaction
skeleton_Pork_Soybean["reaction"] = "EX_" + skeleton_Pork_Soybean.metabolite + "_m"
skeleton_Pork_Splitpeas = pd.merge(diet_Pork_Splitpeas, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Pork_Splitpeas["global_id"] = skeleton_Pork_Splitpeas.reaction
skeleton_Pork_Splitpeas["reaction"] = "EX_" + skeleton_Pork_Splitpeas.metabolite + "_m"
skeleton_Pork_Strawberries = pd.merge(diet_Pork_Strawberries, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Pork_Strawberries["global_id"] = skeleton_Pork_Strawberries.reaction
skeleton_Pork_Strawberries["reaction"] = "EX_" + skeleton_Pork_Strawberries.metabolite + "_m"
skeleton_Pork_Sweetpotato = pd.merge(diet_Pork_Sweetpotato, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Pork_Sweetpotato["global_id"] = skeleton_Pork_Sweetpotato.reaction
skeleton_Pork_Sweetpotato["reaction"] = "EX_" + skeleton_Pork_Sweetpotato.metabolite + "_m"
skeleton_Pumpkin_Raspberries = pd.merge(diet_Pumpkin_Raspberries, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Pumpkin_Raspberries["global_id"] = skeleton_Pumpkin_Raspberries.reaction
skeleton_Pumpkin_Raspberries["reaction"] = "EX_" + skeleton_Pumpkin_Raspberries.metabolite + "_m"
skeleton_Pumpkin_Shrimp = pd.merge(diet_Pumpkin_Shrimp, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Pumpkin_Shrimp["global_id"] = skeleton_Pumpkin_Shrimp.reaction
skeleton_Pumpkin_Shrimp["reaction"] = "EX_" + skeleton_Pumpkin_Shrimp.metabolite + "_m"
skeleton_Pumpkin_Soybean = pd.merge(diet_Pumpkin_Soybean, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Pumpkin_Soybean["global_id"] = skeleton_Pumpkin_Soybean.reaction
skeleton_Pumpkin_Soybean["reaction"] = "EX_" + skeleton_Pumpkin_Soybean.metabolite + "_m"
skeleton_Pumpkin_Splitpeas = pd.merge(diet_Pumpkin_Splitpeas, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Pumpkin_Splitpeas["global_id"] = skeleton_Pumpkin_Splitpeas.reaction
skeleton_Pumpkin_Splitpeas["reaction"] = "EX_" + skeleton_Pumpkin_Splitpeas.metabolite + "_m"
skeleton_Pumpkin_Strawberries = pd.merge(diet_Pumpkin_Strawberries, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Pumpkin_Strawberries["global_id"] = skeleton_Pumpkin_Strawberries.reaction
skeleton_Pumpkin_Strawberries["reaction"] = "EX_" + skeleton_Pumpkin_Strawberries.metabolite + "_m"
skeleton_Pumpkin_Sweetpotato = pd.merge(diet_Pumpkin_Sweetpotato, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Pumpkin_Sweetpotato["global_id"] = skeleton_Pumpkin_Sweetpotato.reaction
skeleton_Pumpkin_Sweetpotato["reaction"] = "EX_" + skeleton_Pumpkin_Sweetpotato.metabolite + "_m"
skeleton_Raspberries_Shrimp = pd.merge(diet_Raspberries_Shrimp, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Raspberries_Shrimp["global_id"] = skeleton_Raspberries_Shrimp.reaction
skeleton_Raspberries_Shrimp["reaction"] = "EX_" + skeleton_Raspberries_Shrimp.metabolite + "_m"
skeleton_Raspberries_Soybean = pd.merge(diet_Raspberries_Soybean, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Raspberries_Soybean["global_id"] = skeleton_Raspberries_Soybean.reaction
skeleton_Raspberries_Soybean["reaction"] = "EX_" + skeleton_Raspberries_Soybean.metabolite + "_m"
skeleton_Raspberries_Splitpeas = pd.merge(diet_Raspberries_Splitpeas, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Raspberries_Splitpeas["global_id"] = skeleton_Raspberries_Splitpeas.reaction
skeleton_Raspberries_Splitpeas["reaction"] = "EX_" + skeleton_Raspberries_Splitpeas.metabolite + "_m"
skeleton_Raspberries_Strawberries = pd.merge(diet_Raspberries_Strawberries, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Raspberries_Strawberries["global_id"] = skeleton_Raspberries_Strawberries.reaction
skeleton_Raspberries_Strawberries["reaction"] = "EX_" + skeleton_Raspberries_Strawberries.metabolite + "_m"
skeleton_Raspberries_Sweetpotato = pd.merge(diet_Raspberries_Sweetpotato, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Raspberries_Sweetpotato["global_id"] = skeleton_Raspberries_Sweetpotato.reaction
skeleton_Raspberries_Sweetpotato["reaction"] = "EX_" + skeleton_Raspberries_Sweetpotato.metabolite + "_m"
skeleton_Shrimp_Soybean = pd.merge(diet_Shrimp_Soybean, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Shrimp_Soybean["global_id"] = skeleton_Shrimp_Soybean.reaction
skeleton_Shrimp_Soybean["reaction"] = "EX_" + skeleton_Shrimp_Soybean.metabolite + "_m"
skeleton_Shrimp_Splitpeas = pd.merge(diet_Shrimp_Splitpeas, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Shrimp_Splitpeas["global_id"] = skeleton_Shrimp_Splitpeas.reaction
skeleton_Shrimp_Splitpeas["reaction"] = "EX_" + skeleton_Shrimp_Splitpeas.metabolite + "_m"
skeleton_Shrimp_Strawberries = pd.merge(diet_Shrimp_Strawberries, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Shrimp_Strawberries["global_id"] = skeleton_Shrimp_Strawberries.reaction
skeleton_Shrimp_Strawberries["reaction"] = "EX_" + skeleton_Shrimp_Strawberries.metabolite + "_m"
skeleton_Shrimp_Sweetpotato = pd.merge(diet_Shrimp_Sweetpotato, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Shrimp_Sweetpotato["global_id"] = skeleton_Shrimp_Sweetpotato.reaction
skeleton_Shrimp_Sweetpotato["reaction"] = "EX_" + skeleton_Shrimp_Sweetpotato.metabolite + "_m"
skeleton_Soybean_Splitpeas = pd.merge(diet_Soybean_Splitpeas, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Soybean_Splitpeas["global_id"] = skeleton_Soybean_Splitpeas.reaction
skeleton_Soybean_Splitpeas["reaction"] = "EX_" + skeleton_Soybean_Splitpeas.metabolite + "_m"
skeleton_Soybean_Strawberries = pd.merge(diet_Soybean_Strawberries, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Soybean_Strawberries["global_id"] = skeleton_Soybean_Strawberries.reaction
skeleton_Soybean_Strawberries["reaction"] = "EX_" + skeleton_Soybean_Strawberries.metabolite + "_m"
skeleton_Soybean_Sweetpotato = pd.merge(diet_Soybean_Sweetpotato, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Soybean_Sweetpotato["global_id"] = skeleton_Soybean_Sweetpotato.reaction
skeleton_Soybean_Sweetpotato["reaction"] = "EX_" + skeleton_Soybean_Sweetpotato.metabolite + "_m"
skeleton_Splitpeas_Strawberries = pd.merge(diet_Splitpeas_Strawberries, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Splitpeas_Strawberries["global_id"] = skeleton_Splitpeas_Strawberries.reaction
skeleton_Splitpeas_Strawberries["reaction"] = "EX_" + skeleton_Splitpeas_Strawberries.metabolite + "_m"
skeleton_Splitpeas_Sweetpotato = pd.merge(diet_Splitpeas_Sweetpotato, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Splitpeas_Sweetpotato["global_id"] = skeleton_Splitpeas_Sweetpotato.reaction
skeleton_Splitpeas_Sweetpotato["reaction"] = "EX_" + skeleton_Splitpeas_Sweetpotato.metabolite + "_m"
skeleton_Strawberries_Sweetpotato = pd.merge(diet_Strawberries_Sweetpotato, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Strawberries_Sweetpotato["global_id"] = skeleton_Strawberries_Sweetpotato.reaction
skeleton_Strawberries_Sweetpotato["reaction"] = "EX_" + skeleton_Strawberries_Sweetpotato.metabolite + "_m"

#Supplementing the medium with essential nutrietns for microbial growth
from micom.workflows.db_media import complete_db_medium

manifest_Blackbeans_Blackcurrant, imports_Blackbeans_Blackcurrant = complete_db_medium("data/agora201__species.qza", skeleton_Blackbeans_Blackcurrant, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Blackbeans_Chickpea, imports_Blackbeans_Chickpea = complete_db_medium("data/agora201__species.qza", skeleton_Blackbeans_Chickpea, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Blackbeans_Couscous, imports_Blackbeans_Couscous = complete_db_medium("data/agora201__species.qza", skeleton_Blackbeans_Couscous, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Blackbeans_Pork, imports_Blackbeans_Pork = complete_db_medium("data/agora201__species.qza", skeleton_Blackbeans_Pork, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Blackbeans_Pumpkin, imports_Blackbeans_Pumpkin = complete_db_medium("data/agora201__species.qza", skeleton_Blackbeans_Pumpkin, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Blackbeans_Raspberries, imports_Blackbeans_Raspberries = complete_db_medium("data/agora201__species.qza", skeleton_Blackbeans_Raspberries, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Blackbeans_Shrimp, imports_Blackbeans_Shrimp = complete_db_medium("data/agora201__species.qza", skeleton_Blackbeans_Shrimp, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Blackbeans_Soybean, imports_Blackbeans_Soybean = complete_db_medium("data/agora201__species.qza", skeleton_Blackbeans_Soybean, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Blackbeans_Splitpeas, imports_Blackbeans_Splitpeas = complete_db_medium("data/agora201__species.qza", skeleton_Blackbeans_Splitpeas, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Blackbeans_Strawberries, imports_Blackbeans_Strawberries = complete_db_medium("data/agora201__species.qza", skeleton_Blackbeans_Strawberries, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Blackbeans_Sweetpotato, imports_Blackbeans_Sweetpotato = complete_db_medium("data/agora201__species.qza", skeleton_Blackbeans_Sweetpotato, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Blackcurrant_Chickpea, imports_Blackcurrant_Chickpea = complete_db_medium("data/agora201__species.qza", skeleton_Blackcurrant_Chickpea, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Blackcurrant_Couscous, imports_Blackcurrant_Couscous = complete_db_medium("data/agora201__species.qza", skeleton_Blackcurrant_Couscous, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Blackcurrant_Pork, imports_Blackcurrant_Pork = complete_db_medium("data/agora201__species.qza", skeleton_Blackcurrant_Pork, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Blackcurrant_Pumpkin, imports_Blackcurrant_Pumpkin = complete_db_medium("data/agora201__species.qza", skeleton_Blackcurrant_Pumpkin, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Blackcurrant_Raspberries, imports_Blackcurrant_Raspberries = complete_db_medium("data/agora201__species.qza", skeleton_Blackcurrant_Raspberries, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Blackcurrant_Shrimp, imports_Blackcurrant_Shrimp = complete_db_medium("data/agora201__species.qza", skeleton_Blackcurrant_Shrimp, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Blackcurrant_Soybean, imports_Blackcurrant_Soybean = complete_db_medium("data/agora201__species.qza", skeleton_Blackcurrant_Soybean, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Blackcurrant_Splitpeas, imports_Blackcurrant_Splitpeas = complete_db_medium("data/agora201__species.qza", skeleton_Blackcurrant_Splitpeas, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Blackcurrant_Strawberries, imports_Blackcurrant_Strawberries = complete_db_medium("data/agora201__species.qza", skeleton_Blackcurrant_Strawberries, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Blackcurrant_Sweetpotato, imports_Blackcurrant_Sweetpotato = complete_db_medium("data/agora201__species.qza", skeleton_Blackcurrant_Sweetpotato, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Chickpea_Couscous, imports_Chickpea_Couscous = complete_db_medium("data/agora201__species.qza", skeleton_Chickpea_Couscous, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Chickpea_Pork, imports_Chickpea_Pork = complete_db_medium("data/agora201__species.qza", skeleton_Chickpea_Pork, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Chickpea_Pumpkin, imports_Chickpea_Pumpkin = complete_db_medium("data/agora201__species.qza", skeleton_Chickpea_Pumpkin, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Chickpea_Raspberries, imports_Chickpea_Raspberries = complete_db_medium("data/agora201__species.qza", skeleton_Chickpea_Raspberries, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Chickpea_Shrimp, imports_Chickpea_Shrimp = complete_db_medium("data/agora201__species.qza", skeleton_Chickpea_Shrimp, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Chickpea_Soybean, imports_Chickpea_Soybean = complete_db_medium("data/agora201__species.qza", skeleton_Chickpea_Soybean, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Chickpea_Splitpeas, imports_Chickpea_Splitpeas = complete_db_medium("data/agora201__species.qza", skeleton_Chickpea_Splitpeas, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Chickpea_Strawberries, imports_Chickpea_Strawberries = complete_db_medium("data/agora201__species.qza", skeleton_Chickpea_Strawberries, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Chickpea_Sweetpotato, imports_Chickpea_Sweetpotato = complete_db_medium("data/agora201__species.qza", skeleton_Chickpea_Sweetpotato, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Couscous_Pork, imports_Couscous_Pork = complete_db_medium("data/agora201__species.qza", skeleton_Couscous_Pork, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Couscous_Pumpkin, imports_Couscous_Pumpkin = complete_db_medium("data/agora201__species.qza", skeleton_Couscous_Pumpkin, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Couscous_Raspberries, imports_Couscous_Raspberries = complete_db_medium("data/agora201__species.qza", skeleton_Couscous_Raspberries, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Couscous_Shrimp, imports_Couscous_Shrimp = complete_db_medium("data/agora201__species.qza", skeleton_Couscous_Shrimp, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Couscous_Soybean, imports_Couscous_Soybean = complete_db_medium("data/agora201__species.qza", skeleton_Couscous_Soybean, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Couscous_Splitpeas, imports_Couscous_Splitpeas = complete_db_medium("data/agora201__species.qza", skeleton_Couscous_Splitpeas, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Couscous_Strawberries, imports_Couscous_Strawberries = complete_db_medium("data/agora201__species.qza", skeleton_Couscous_Strawberries, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Couscous_Sweetpotato, imports_Couscous_Sweetpotato = complete_db_medium("data/agora201__species.qza", skeleton_Couscous_Sweetpotato, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Pork_Pumpkin, imports_Pork_Pumpkin = complete_db_medium("data/agora201__species.qza", skeleton_Pork_Pumpkin, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Pork_Raspberries, imports_Pork_Raspberries = complete_db_medium("data/agora201__species.qza", skeleton_Pork_Raspberries, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Pork_Shrimp, imports_Pork_Shrimp = complete_db_medium("data/agora201__species.qza", skeleton_Pork_Shrimp, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Pork_Soybean, imports_Pork_Soybean = complete_db_medium("data/agora201__species.qza", skeleton_Pork_Soybean, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Pork_Splitpeas, imports_Pork_Splitpeas = complete_db_medium("data/agora201__species.qza", skeleton_Pork_Splitpeas, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Pork_Strawberries, imports_Pork_Strawberries = complete_db_medium("data/agora201__species.qza", skeleton_Pork_Strawberries, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Pork_Sweetpotato, imports_Pork_Sweetpotato = complete_db_medium("data/agora201__species.qza", skeleton_Pork_Sweetpotato, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Pumpkin_Raspberries, imports_Pumpkin_Raspberries = complete_db_medium("data/agora201__species.qza", skeleton_Pumpkin_Raspberries, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Pumpkin_Shrimp, imports_Pumpkin_Shrimp = complete_db_medium("data/agora201__species.qza", skeleton_Pumpkin_Shrimp, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Pumpkin_Soybean, imports_Pumpkin_Soybean = complete_db_medium("data/agora201__species.qza", skeleton_Pumpkin_Soybean, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Pumpkin_Splitpeas, imports_Pumpkin_Splitpeas = complete_db_medium("data/agora201__species.qza", skeleton_Pumpkin_Splitpeas, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Pumpkin_Strawberries, imports_Pumpkin_Strawberries = complete_db_medium("data/agora201__species.qza", skeleton_Pumpkin_Strawberries, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Pumpkin_Sweetpotato, imports_Pumpkin_Sweetpotato = complete_db_medium("data/agora201__species.qza", skeleton_Pumpkin_Sweetpotato, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Raspberries_Shrimp, imports_Raspberries_Shrimp = complete_db_medium("data/agora201__species.qza", skeleton_Raspberries_Shrimp, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Raspberries_Soybean, imports_Raspberries_Soybean = complete_db_medium("data/agora201__species.qza", skeleton_Raspberries_Soybean, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Raspberries_Splitpeas, imports_Raspberries_Splitpeas = complete_db_medium("data/agora201__species.qza", skeleton_Raspberries_Splitpeas, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Raspberries_Strawberries, imports_Raspberries_Strawberries = complete_db_medium("data/agora201__species.qza", skeleton_Raspberries_Strawberries, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Raspberries_Sweetpotato, imports_Raspberries_Sweetpotato = complete_db_medium("data/agora201__species.qza", skeleton_Raspberries_Sweetpotato, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Shrimp_Soybean, imports_Shrimp_Soybean = complete_db_medium("data/agora201__species.qza", skeleton_Shrimp_Soybean, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Shrimp_Splitpeas, imports_Shrimp_Splitpeas = complete_db_medium("data/agora201__species.qza", skeleton_Shrimp_Splitpeas, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Shrimp_Strawberries, imports_Shrimp_Strawberries = complete_db_medium("data/agora201__species.qza", skeleton_Shrimp_Strawberries, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Shrimp_Sweetpotato, imports_Shrimp_Sweetpotato = complete_db_medium("data/agora201__species.qza", skeleton_Shrimp_Sweetpotato, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Soybean_Splitpeas, imports_Soybean_Splitpeas = complete_db_medium("data/agora201__species.qza", skeleton_Soybean_Splitpeas, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Soybean_Strawberries, imports_Soybean_Strawberries = complete_db_medium("data/agora201__species.qza", skeleton_Soybean_Strawberries, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Soybean_Sweetpotato, imports_Soybean_Sweetpotato = complete_db_medium("data/agora201__species.qza", skeleton_Soybean_Sweetpotato, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Splitpeas_Strawberries, imports_Splitpeas_Strawberries = complete_db_medium("data/agora201__species.qza", skeleton_Splitpeas_Strawberries, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Splitpeas_Sweetpotato, imports_Splitpeas_Sweetpotato = complete_db_medium("data/agora201__species.qza", skeleton_Splitpeas_Sweetpotato, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Strawberries_Sweetpotato, imports_Strawberries_Sweetpotato = complete_db_medium("data/agora201__species.qza", skeleton_Strawberries_Sweetpotato, growth=0.01, threads=14, max_added_import=10, minimize_components=True)

manifest_Blackbeans_Blackcurrant.can_grow.value_counts() #checking the microbial growth
filled_Blackbeans_Blackcurrant = imports_Blackbeans_Blackcurrant.max()
added_Blackbeans_Blackcurrant = filled_Blackbeans_Blackcurrant[~filled_Blackbeans_Blackcurrant.index.isin(skeleton_Blackbeans_Blackcurrant.reaction)] #fluxes that were added
manifest_Blackbeans_Chickpea.can_grow.value_counts() #checking the microbial growth
filled_Blackbeans_Chickpea = imports_Blackbeans_Chickpea.max()
added_Blackbeans_Chickpea = filled_Blackbeans_Chickpea[~filled_Blackbeans_Chickpea.index.isin(skeleton_Blackbeans_Chickpea.reaction)] #fluxes that were added
manifest_Blackbeans_Couscous.can_grow.value_counts() #checking the microbial growth
filled_Blackbeans_Couscous = imports_Blackbeans_Couscous.max()
added_Blackbeans_Couscous = filled_Blackbeans_Couscous[~filled_Blackbeans_Couscous.index.isin(skeleton_Blackbeans_Couscous.reaction)] #fluxes that were added
manifest_Blackbeans_Pork.can_grow.value_counts() #checking the microbial growth
filled_Blackbeans_Pork = imports_Blackbeans_Pork.max()
added_Blackbeans_Pork = filled_Blackbeans_Pork[~filled_Blackbeans_Pork.index.isin(skeleton_Blackbeans_Pork.reaction)] #fluxes that were added
manifest_Blackbeans_Pumpkin.can_grow.value_counts() #checking the microbial growth
filled_Blackbeans_Pumpkin = imports_Blackbeans_Pumpkin.max()
added_Blackbeans_Pumpkin = filled_Blackbeans_Pumpkin[~filled_Blackbeans_Pumpkin.index.isin(skeleton_Blackbeans_Pumpkin.reaction)] #fluxes that were added
manifest_Blackbeans_Raspberries.can_grow.value_counts() #checking the microbial growth
filled_Blackbeans_Raspberries = imports_Blackbeans_Raspberries.max()
added_Blackbeans_Raspberries = filled_Blackbeans_Raspberries[~filled_Blackbeans_Raspberries.index.isin(skeleton_Blackbeans_Raspberries.reaction)] #fluxes that were added
manifest_Blackbeans_Shrimp.can_grow.value_counts() #checking the microbial growth
filled_Blackbeans_Shrimp = imports_Blackbeans_Shrimp.max()
added_Blackbeans_Shrimp = filled_Blackbeans_Shrimp[~filled_Blackbeans_Shrimp.index.isin(skeleton_Blackbeans_Shrimp.reaction)] #fluxes that were added
manifest_Blackbeans_Soybean.can_grow.value_counts() #checking the microbial growth
filled_Blackbeans_Soybean = imports_Blackbeans_Soybean.max()
added_Blackbeans_Soybean = filled_Blackbeans_Soybean[~filled_Blackbeans_Soybean.index.isin(skeleton_Blackbeans_Soybean.reaction)] #fluxes that were added
manifest_Blackbeans_Splitpeas.can_grow.value_counts() #checking the microbial growth
filled_Blackbeans_Splitpeas = imports_Blackbeans_Splitpeas.max()
added_Blackbeans_Splitpeas = filled_Blackbeans_Splitpeas[~filled_Blackbeans_Splitpeas.index.isin(skeleton_Blackbeans_Splitpeas.reaction)] #fluxes that were added
manifest_Blackbeans_Strawberries.can_grow.value_counts() #checking the microbial growth
filled_Blackbeans_Strawberries = imports_Blackbeans_Strawberries.max()
added_Blackbeans_Strawberries = filled_Blackbeans_Strawberries[~filled_Blackbeans_Strawberries.index.isin(skeleton_Blackbeans_Strawberries.reaction)] #fluxes that were added
manifest_Blackbeans_Sweetpotato.can_grow.value_counts() #checking the microbial growth
filled_Blackbeans_Sweetpotato = imports_Blackbeans_Sweetpotato.max()
added_Blackbeans_Sweetpotato = filled_Blackbeans_Sweetpotato[~filled_Blackbeans_Sweetpotato.index.isin(skeleton_Blackbeans_Sweetpotato.reaction)] #fluxes that were added
manifest_Blackcurrant_Chickpea.can_grow.value_counts() #checking the microbial growth
filled_Blackcurrant_Chickpea = imports_Blackcurrant_Chickpea.max()
added_Blackcurrant_Chickpea = filled_Blackcurrant_Chickpea[~filled_Blackcurrant_Chickpea.index.isin(skeleton_Blackcurrant_Chickpea.reaction)] #fluxes that were added
manifest_Blackcurrant_Couscous.can_grow.value_counts() #checking the microbial growth
filled_Blackcurrant_Couscous = imports_Blackcurrant_Couscous.max()
added_Blackcurrant_Couscous = filled_Blackcurrant_Couscous[~filled_Blackcurrant_Couscous.index.isin(skeleton_Blackcurrant_Couscous.reaction)] #fluxes that were added
manifest_Blackcurrant_Pork.can_grow.value_counts() #checking the microbial growth
filled_Blackcurrant_Pork = imports_Blackcurrant_Pork.max()
added_Blackcurrant_Pork = filled_Blackcurrant_Pork[~filled_Blackcurrant_Pork.index.isin(skeleton_Blackcurrant_Pork.reaction)] #fluxes that were added
manifest_Blackcurrant_Pumpkin.can_grow.value_counts() #checking the microbial growth
filled_Blackcurrant_Pumpkin = imports_Blackcurrant_Pumpkin.max()
added_Blackcurrant_Pumpkin = filled_Blackcurrant_Pumpkin[~filled_Blackcurrant_Pumpkin.index.isin(skeleton_Blackcurrant_Pumpkin.reaction)] #fluxes that were added
manifest_Blackcurrant_Raspberries.can_grow.value_counts() #checking the microbial growth
filled_Blackcurrant_Raspberries = imports_Blackcurrant_Raspberries.max()
added_Blackcurrant_Raspberries = filled_Blackcurrant_Raspberries[~filled_Blackcurrant_Raspberries.index.isin(skeleton_Blackcurrant_Raspberries.reaction)] #fluxes that were added
manifest_Blackcurrant_Shrimp.can_grow.value_counts() #checking the microbial growth
filled_Blackcurrant_Shrimp = imports_Blackcurrant_Shrimp.max()
added_Blackcurrant_Shrimp = filled_Blackcurrant_Shrimp[~filled_Blackcurrant_Shrimp.index.isin(skeleton_Blackcurrant_Shrimp.reaction)] #fluxes that were added
manifest_Blackcurrant_Soybean.can_grow.value_counts() #checking the microbial growth
filled_Blackcurrant_Soybean = imports_Blackcurrant_Soybean.max()
added_Blackcurrant_Soybean = filled_Blackcurrant_Soybean[~filled_Blackcurrant_Soybean.index.isin(skeleton_Blackcurrant_Soybean.reaction)] #fluxes that were added
manifest_Blackcurrant_Splitpeas.can_grow.value_counts() #checking the microbial growth
filled_Blackcurrant_Splitpeas = imports_Blackcurrant_Splitpeas.max()
added_Blackcurrant_Splitpeas = filled_Blackcurrant_Splitpeas[~filled_Blackcurrant_Splitpeas.index.isin(skeleton_Blackcurrant_Splitpeas.reaction)] #fluxes that were added
manifest_Blackcurrant_Strawberries.can_grow.value_counts() #checking the microbial growth
filled_Blackcurrant_Strawberries = imports_Blackcurrant_Strawberries.max()
added_Blackcurrant_Strawberries = filled_Blackcurrant_Strawberries[~filled_Blackcurrant_Strawberries.index.isin(skeleton_Blackcurrant_Strawberries.reaction)] #fluxes that were added
manifest_Blackcurrant_Sweetpotato.can_grow.value_counts() #checking the microbial growth
filled_Blackcurrant_Sweetpotato = imports_Blackcurrant_Sweetpotato.max()
added_Blackcurrant_Sweetpotato = filled_Blackcurrant_Sweetpotato[~filled_Blackcurrant_Sweetpotato.index.isin(skeleton_Blackcurrant_Sweetpotato.reaction)] #fluxes that were added
manifest_Chickpea_Couscous.can_grow.value_counts() #checking the microbial growth
filled_Chickpea_Couscous = imports_Chickpea_Couscous.max()
added_Chickpea_Couscous = filled_Chickpea_Couscous[~filled_Chickpea_Couscous.index.isin(skeleton_Chickpea_Couscous.reaction)] #fluxes that were added
manifest_Chickpea_Pork.can_grow.value_counts() #checking the microbial growth
filled_Chickpea_Pork = imports_Chickpea_Pork.max()
added_Chickpea_Pork = filled_Chickpea_Pork[~filled_Chickpea_Pork.index.isin(skeleton_Chickpea_Pork.reaction)] #fluxes that were added
manifest_Chickpea_Pumpkin.can_grow.value_counts() #checking the microbial growth
filled_Chickpea_Pumpkin = imports_Chickpea_Pumpkin.max()
added_Chickpea_Pumpkin = filled_Chickpea_Pumpkin[~filled_Chickpea_Pumpkin.index.isin(skeleton_Chickpea_Pumpkin.reaction)] #fluxes that were added
manifest_Chickpea_Raspberries.can_grow.value_counts() #checking the microbial growth
filled_Chickpea_Raspberries = imports_Chickpea_Raspberries.max()
added_Chickpea_Raspberries = filled_Chickpea_Raspberries[~filled_Chickpea_Raspberries.index.isin(skeleton_Chickpea_Raspberries.reaction)] #fluxes that were added
manifest_Chickpea_Shrimp.can_grow.value_counts() #checking the microbial growth
filled_Chickpea_Shrimp = imports_Chickpea_Shrimp.max()
added_Chickpea_Shrimp = filled_Chickpea_Shrimp[~filled_Chickpea_Shrimp.index.isin(skeleton_Chickpea_Shrimp.reaction)] #fluxes that were added
manifest_Chickpea_Soybean.can_grow.value_counts() #checking the microbial growth
filled_Chickpea_Soybean = imports_Chickpea_Soybean.max()
added_Chickpea_Soybean = filled_Chickpea_Soybean[~filled_Chickpea_Soybean.index.isin(skeleton_Chickpea_Soybean.reaction)] #fluxes that were added
manifest_Chickpea_Splitpeas.can_grow.value_counts() #checking the microbial growth
filled_Chickpea_Splitpeas = imports_Chickpea_Splitpeas.max()
added_Chickpea_Splitpeas = filled_Chickpea_Splitpeas[~filled_Chickpea_Splitpeas.index.isin(skeleton_Chickpea_Splitpeas.reaction)] #fluxes that were added
manifest_Chickpea_Strawberries.can_grow.value_counts() #checking the microbial growth
filled_Chickpea_Strawberries = imports_Chickpea_Strawberries.max()
added_Chickpea_Strawberries = filled_Chickpea_Strawberries[~filled_Chickpea_Strawberries.index.isin(skeleton_Chickpea_Strawberries.reaction)] #fluxes that were added
manifest_Chickpea_Sweetpotato.can_grow.value_counts() #checking the microbial growth
filled_Chickpea_Sweetpotato = imports_Chickpea_Sweetpotato.max()
added_Chickpea_Sweetpotato = filled_Chickpea_Sweetpotato[~filled_Chickpea_Sweetpotato.index.isin(skeleton_Chickpea_Sweetpotato.reaction)] #fluxes that were added
manifest_Couscous_Pork.can_grow.value_counts() #checking the microbial growth
filled_Couscous_Pork = imports_Couscous_Pork.max()
added_Couscous_Pork = filled_Couscous_Pork[~filled_Couscous_Pork.index.isin(skeleton_Couscous_Pork.reaction)] #fluxes that were added
manifest_Couscous_Pumpkin.can_grow.value_counts() #checking the microbial growth
filled_Couscous_Pumpkin = imports_Couscous_Pumpkin.max()
added_Couscous_Pumpkin = filled_Couscous_Pumpkin[~filled_Couscous_Pumpkin.index.isin(skeleton_Couscous_Pumpkin.reaction)] #fluxes that were added
manifest_Couscous_Raspberries.can_grow.value_counts() #checking the microbial growth
filled_Couscous_Raspberries = imports_Couscous_Raspberries.max()
added_Couscous_Raspberries = filled_Couscous_Raspberries[~filled_Couscous_Raspberries.index.isin(skeleton_Couscous_Raspberries.reaction)] #fluxes that were added
manifest_Couscous_Shrimp.can_grow.value_counts() #checking the microbial growth
filled_Couscous_Shrimp = imports_Couscous_Shrimp.max()
added_Couscous_Shrimp = filled_Couscous_Shrimp[~filled_Couscous_Shrimp.index.isin(skeleton_Couscous_Shrimp.reaction)] #fluxes that were added
manifest_Couscous_Soybean.can_grow.value_counts() #checking the microbial growth
filled_Couscous_Soybean = imports_Couscous_Soybean.max()
added_Couscous_Soybean = filled_Couscous_Soybean[~filled_Couscous_Soybean.index.isin(skeleton_Couscous_Soybean.reaction)] #fluxes that were added
manifest_Couscous_Splitpeas.can_grow.value_counts() #checking the microbial growth
filled_Couscous_Splitpeas = imports_Couscous_Splitpeas.max()
added_Couscous_Splitpeas = filled_Couscous_Splitpeas[~filled_Couscous_Splitpeas.index.isin(skeleton_Couscous_Splitpeas.reaction)] #fluxes that were added
manifest_Couscous_Strawberries.can_grow.value_counts() #checking the microbial growth
filled_Couscous_Strawberries = imports_Couscous_Strawberries.max()
added_Couscous_Strawberries = filled_Couscous_Strawberries[~filled_Couscous_Strawberries.index.isin(skeleton_Couscous_Strawberries.reaction)] #fluxes that were added
manifest_Couscous_Sweetpotato.can_grow.value_counts() #checking the microbial growth
filled_Couscous_Sweetpotato = imports_Couscous_Sweetpotato.max()
added_Couscous_Sweetpotato = filled_Couscous_Sweetpotato[~filled_Couscous_Sweetpotato.index.isin(skeleton_Couscous_Sweetpotato.reaction)] #fluxes that were added
manifest_Pork_Pumpkin.can_grow.value_counts() #checking the microbial growth
filled_Pork_Pumpkin = imports_Pork_Pumpkin.max()
added_Pork_Pumpkin = filled_Pork_Pumpkin[~filled_Pork_Pumpkin.index.isin(skeleton_Pork_Pumpkin.reaction)] #fluxes that were added
manifest_Pork_Raspberries.can_grow.value_counts() #checking the microbial growth
filled_Pork_Raspberries = imports_Pork_Raspberries.max()
added_Pork_Raspberries = filled_Pork_Raspberries[~filled_Pork_Raspberries.index.isin(skeleton_Pork_Raspberries.reaction)] #fluxes that were added
manifest_Pork_Shrimp.can_grow.value_counts() #checking the microbial growth
filled_Pork_Shrimp = imports_Pork_Shrimp.max()
added_Pork_Shrimp = filled_Pork_Shrimp[~filled_Pork_Shrimp.index.isin(skeleton_Pork_Shrimp.reaction)] #fluxes that were added
manifest_Pork_Soybean.can_grow.value_counts() #checking the microbial growth
filled_Pork_Soybean = imports_Pork_Soybean.max()
added_Pork_Soybean = filled_Pork_Soybean[~filled_Pork_Soybean.index.isin(skeleton_Pork_Soybean.reaction)] #fluxes that were added
manifest_Pork_Splitpeas.can_grow.value_counts() #checking the microbial growth
filled_Pork_Splitpeas = imports_Pork_Splitpeas.max()
added_Pork_Splitpeas = filled_Pork_Splitpeas[~filled_Pork_Splitpeas.index.isin(skeleton_Pork_Splitpeas.reaction)] #fluxes that were added
manifest_Pork_Strawberries.can_grow.value_counts() #checking the microbial growth
filled_Pork_Strawberries = imports_Pork_Strawberries.max()
added_Pork_Strawberries = filled_Pork_Strawberries[~filled_Pork_Strawberries.index.isin(skeleton_Pork_Strawberries.reaction)] #fluxes that were added
manifest_Pork_Sweetpotato.can_grow.value_counts() #checking the microbial growth
filled_Pork_Sweetpotato = imports_Pork_Sweetpotato.max()
added_Pork_Sweetpotato = filled_Pork_Sweetpotato[~filled_Pork_Sweetpotato.index.isin(skeleton_Pork_Sweetpotato.reaction)] #fluxes that were added
manifest_Pumpkin_Raspberries.can_grow.value_counts() #checking the microbial growth
filled_Pumpkin_Raspberries = imports_Pumpkin_Raspberries.max()
added_Pumpkin_Raspberries = filled_Pumpkin_Raspberries[~filled_Pumpkin_Raspberries.index.isin(skeleton_Pumpkin_Raspberries.reaction)] #fluxes that were added
manifest_Pumpkin_Shrimp.can_grow.value_counts() #checking the microbial growth
filled_Pumpkin_Shrimp = imports_Pumpkin_Shrimp.max()
added_Pumpkin_Shrimp = filled_Pumpkin_Shrimp[~filled_Pumpkin_Shrimp.index.isin(skeleton_Pumpkin_Shrimp.reaction)] #fluxes that were added
manifest_Pumpkin_Soybean.can_grow.value_counts() #checking the microbial growth
filled_Pumpkin_Soybean = imports_Pumpkin_Soybean.max()
added_Pumpkin_Soybean = filled_Pumpkin_Soybean[~filled_Pumpkin_Soybean.index.isin(skeleton_Pumpkin_Soybean.reaction)] #fluxes that were added
manifest_Pumpkin_Splitpeas.can_grow.value_counts() #checking the microbial growth
filled_Pumpkin_Splitpeas = imports_Pumpkin_Splitpeas.max()
added_Pumpkin_Splitpeas = filled_Pumpkin_Splitpeas[~filled_Pumpkin_Splitpeas.index.isin(skeleton_Pumpkin_Splitpeas.reaction)] #fluxes that were added
manifest_Pumpkin_Strawberries.can_grow.value_counts() #checking the microbial growth
filled_Pumpkin_Strawberries = imports_Pumpkin_Strawberries.max()
added_Pumpkin_Strawberries = filled_Pumpkin_Strawberries[~filled_Pumpkin_Strawberries.index.isin(skeleton_Pumpkin_Strawberries.reaction)] #fluxes that were added
manifest_Pumpkin_Sweetpotato.can_grow.value_counts() #checking the microbial growth
filled_Pumpkin_Sweetpotato = imports_Pumpkin_Sweetpotato.max()
added_Pumpkin_Sweetpotato = filled_Pumpkin_Sweetpotato[~filled_Pumpkin_Sweetpotato.index.isin(skeleton_Pumpkin_Sweetpotato.reaction)] #fluxes that were added
manifest_Raspberries_Shrimp.can_grow.value_counts() #checking the microbial growth
filled_Raspberries_Shrimp = imports_Raspberries_Shrimp.max()
added_Raspberries_Shrimp = filled_Raspberries_Shrimp[~filled_Raspberries_Shrimp.index.isin(skeleton_Raspberries_Shrimp.reaction)] #fluxes that were added
manifest_Raspberries_Soybean.can_grow.value_counts() #checking the microbial growth
filled_Raspberries_Soybean = imports_Raspberries_Soybean.max()
added_Raspberries_Soybean = filled_Raspberries_Soybean[~filled_Raspberries_Soybean.index.isin(skeleton_Raspberries_Soybean.reaction)] #fluxes that were added
manifest_Raspberries_Splitpeas.can_grow.value_counts() #checking the microbial growth
filled_Raspberries_Splitpeas = imports_Raspberries_Splitpeas.max()
added_Raspberries_Splitpeas = filled_Raspberries_Splitpeas[~filled_Raspberries_Splitpeas.index.isin(skeleton_Raspberries_Splitpeas.reaction)] #fluxes that were added
manifest_Raspberries_Strawberries.can_grow.value_counts() #checking the microbial growth
filled_Raspberries_Strawberries = imports_Raspberries_Strawberries.max()
added_Raspberries_Strawberries = filled_Raspberries_Strawberries[~filled_Raspberries_Strawberries.index.isin(skeleton_Raspberries_Strawberries.reaction)] #fluxes that were added
manifest_Raspberries_Sweetpotato.can_grow.value_counts() #checking the microbial growth
filled_Raspberries_Sweetpotato = imports_Raspberries_Sweetpotato.max()
added_Raspberries_Sweetpotato = filled_Raspberries_Sweetpotato[~filled_Raspberries_Sweetpotato.index.isin(skeleton_Raspberries_Sweetpotato.reaction)] #fluxes that were added
manifest_Shrimp_Soybean.can_grow.value_counts() #checking the microbial growth
filled_Shrimp_Soybean = imports_Shrimp_Soybean.max()
added_Shrimp_Soybean = filled_Shrimp_Soybean[~filled_Shrimp_Soybean.index.isin(skeleton_Shrimp_Soybean.reaction)] #fluxes that were added
manifest_Shrimp_Splitpeas.can_grow.value_counts() #checking the microbial growth
filled_Shrimp_Splitpeas = imports_Shrimp_Splitpeas.max()
added_Shrimp_Splitpeas = filled_Shrimp_Splitpeas[~filled_Shrimp_Splitpeas.index.isin(skeleton_Shrimp_Splitpeas.reaction)] #fluxes that were added
manifest_Shrimp_Strawberries.can_grow.value_counts() #checking the microbial growth
filled_Shrimp_Strawberries = imports_Shrimp_Strawberries.max()
added_Shrimp_Strawberries = filled_Shrimp_Strawberries[~filled_Shrimp_Strawberries.index.isin(skeleton_Shrimp_Strawberries.reaction)] #fluxes that were added
manifest_Shrimp_Sweetpotato.can_grow.value_counts() #checking the microbial growth
filled_Shrimp_Sweetpotato = imports_Shrimp_Sweetpotato.max()
added_Shrimp_Sweetpotato = filled_Shrimp_Sweetpotato[~filled_Shrimp_Sweetpotato.index.isin(skeleton_Shrimp_Sweetpotato.reaction)] #fluxes that were added
manifest_Soybean_Splitpeas.can_grow.value_counts() #checking the microbial growth
filled_Soybean_Splitpeas = imports_Soybean_Splitpeas.max()
added_Soybean_Splitpeas = filled_Soybean_Splitpeas[~filled_Soybean_Splitpeas.index.isin(skeleton_Soybean_Splitpeas.reaction)] #fluxes that were added
manifest_Soybean_Strawberries.can_grow.value_counts() #checking the microbial growth
filled_Soybean_Strawberries = imports_Soybean_Strawberries.max()
added_Soybean_Strawberries = filled_Soybean_Strawberries[~filled_Soybean_Strawberries.index.isin(skeleton_Soybean_Strawberries.reaction)] #fluxes that were added
manifest_Soybean_Sweetpotato.can_grow.value_counts() #checking the microbial growth
filled_Soybean_Sweetpotato = imports_Soybean_Sweetpotato.max()
added_Soybean_Sweetpotato = filled_Soybean_Sweetpotato[~filled_Soybean_Sweetpotato.index.isin(skeleton_Soybean_Sweetpotato.reaction)] #fluxes that were added
manifest_Splitpeas_Strawberries.can_grow.value_counts() #checking the microbial growth
filled_Splitpeas_Strawberries = imports_Splitpeas_Strawberries.max()
added_Splitpeas_Strawberries = filled_Splitpeas_Strawberries[~filled_Splitpeas_Strawberries.index.isin(skeleton_Splitpeas_Strawberries.reaction)] #fluxes that were added
manifest_Splitpeas_Sweetpotato.can_grow.value_counts() #checking the microbial growth
filled_Splitpeas_Sweetpotato = imports_Splitpeas_Sweetpotato.max()
added_Splitpeas_Sweetpotato = filled_Splitpeas_Sweetpotato[~filled_Splitpeas_Sweetpotato.index.isin(skeleton_Splitpeas_Sweetpotato.reaction)] #fluxes that were added
manifest_Strawberries_Sweetpotato.can_grow.value_counts() #checking the microbial growth
filled_Strawberries_Sweetpotato = imports_Strawberries_Sweetpotato.max()
added_Strawberries_Sweetpotato = filled_Strawberries_Sweetpotato[~filled_Strawberries_Sweetpotato.index.isin(skeleton_Strawberries_Sweetpotato.reaction)] #fluxes that were added

#Assembling the final medium

added_df_Blackbeans_Blackcurrant = added_Blackbeans_Blackcurrant.reset_index() 
added_df_Blackbeans_Blackcurrant.iloc[:, 0] = added_df_Blackbeans_Blackcurrant.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Blackbeans_Blackcurrant.columns = ["metabolite", "flux"]
added_df_Blackbeans_Blackcurrant = pd.concat([skeleton_Blackbeans_Blackcurrant[["metabolite", "flux"]], added_df_Blackbeans_Blackcurrant])
added_df_Blackbeans_Chickpea = added_Blackbeans_Chickpea.reset_index() 
added_df_Blackbeans_Chickpea.iloc[:, 0] = added_df_Blackbeans_Chickpea.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Blackbeans_Chickpea.columns = ["metabolite", "flux"]
added_df_Blackbeans_Chickpea = pd.concat([skeleton_Blackbeans_Chickpea[["metabolite", "flux"]], added_df_Blackbeans_Chickpea])
added_df_Blackbeans_Couscous = added_Blackbeans_Couscous.reset_index() 
added_df_Blackbeans_Couscous.iloc[:, 0] = added_df_Blackbeans_Couscous.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Blackbeans_Couscous.columns = ["metabolite", "flux"]
added_df_Blackbeans_Couscous = pd.concat([skeleton_Blackbeans_Couscous[["metabolite", "flux"]], added_df_Blackbeans_Couscous])
added_df_Blackbeans_Pork = added_Blackbeans_Pork.reset_index() 
added_df_Blackbeans_Pork.iloc[:, 0] = added_df_Blackbeans_Pork.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Blackbeans_Pork.columns = ["metabolite", "flux"]
added_df_Blackbeans_Pork = pd.concat([skeleton_Blackbeans_Pork[["metabolite", "flux"]], added_df_Blackbeans_Pork])
added_df_Blackbeans_Pumpkin = added_Blackbeans_Pumpkin.reset_index() 
added_df_Blackbeans_Pumpkin.iloc[:, 0] = added_df_Blackbeans_Pumpkin.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Blackbeans_Pumpkin.columns = ["metabolite", "flux"]
added_df_Blackbeans_Pumpkin = pd.concat([skeleton_Blackbeans_Pumpkin[["metabolite", "flux"]], added_df_Blackbeans_Pumpkin])
added_df_Blackbeans_Raspberries = added_Blackbeans_Raspberries.reset_index() 
added_df_Blackbeans_Raspberries.iloc[:, 0] = added_df_Blackbeans_Raspberries.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Blackbeans_Raspberries.columns = ["metabolite", "flux"]
added_df_Blackbeans_Raspberries = pd.concat([skeleton_Blackbeans_Raspberries[["metabolite", "flux"]], added_df_Blackbeans_Raspberries])
added_df_Blackbeans_Shrimp = added_Blackbeans_Shrimp.reset_index() 
added_df_Blackbeans_Shrimp.iloc[:, 0] = added_df_Blackbeans_Shrimp.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Blackbeans_Shrimp.columns = ["metabolite", "flux"]
added_df_Blackbeans_Shrimp = pd.concat([skeleton_Blackbeans_Shrimp[["metabolite", "flux"]], added_df_Blackbeans_Shrimp])
added_df_Blackbeans_Soybean = added_Blackbeans_Soybean.reset_index() 
added_df_Blackbeans_Soybean.iloc[:, 0] = added_df_Blackbeans_Soybean.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Blackbeans_Soybean.columns = ["metabolite", "flux"]
added_df_Blackbeans_Soybean = pd.concat([skeleton_Blackbeans_Soybean[["metabolite", "flux"]], added_df_Blackbeans_Soybean])
added_df_Blackbeans_Splitpeas = added_Blackbeans_Splitpeas.reset_index() 
added_df_Blackbeans_Splitpeas.iloc[:, 0] = added_df_Blackbeans_Splitpeas.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Blackbeans_Splitpeas.columns = ["metabolite", "flux"]
added_df_Blackbeans_Splitpeas = pd.concat([skeleton_Blackbeans_Splitpeas[["metabolite", "flux"]], added_df_Blackbeans_Splitpeas])
added_df_Blackbeans_Strawberries = added_Blackbeans_Strawberries.reset_index() 
added_df_Blackbeans_Strawberries.iloc[:, 0] = added_df_Blackbeans_Strawberries.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Blackbeans_Strawberries.columns = ["metabolite", "flux"]
added_df_Blackbeans_Strawberries = pd.concat([skeleton_Blackbeans_Strawberries[["metabolite", "flux"]], added_df_Blackbeans_Strawberries])
added_df_Blackbeans_Sweetpotato = added_Blackbeans_Sweetpotato.reset_index() 
added_df_Blackbeans_Sweetpotato.iloc[:, 0] = added_df_Blackbeans_Sweetpotato.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Blackbeans_Sweetpotato.columns = ["metabolite", "flux"]
added_df_Blackbeans_Sweetpotato = pd.concat([skeleton_Blackbeans_Sweetpotato[["metabolite", "flux"]], added_df_Blackbeans_Sweetpotato])
added_df_Blackcurrant_Chickpea = added_Blackcurrant_Chickpea.reset_index() 
added_df_Blackcurrant_Chickpea.iloc[:, 0] = added_df_Blackcurrant_Chickpea.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Blackcurrant_Chickpea.columns = ["metabolite", "flux"]
added_df_Blackcurrant_Chickpea = pd.concat([skeleton_Blackcurrant_Chickpea[["metabolite", "flux"]], added_df_Blackcurrant_Chickpea])
added_df_Blackcurrant_Couscous = added_Blackcurrant_Couscous.reset_index() 
added_df_Blackcurrant_Couscous.iloc[:, 0] = added_df_Blackcurrant_Couscous.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Blackcurrant_Couscous.columns = ["metabolite", "flux"]
added_df_Blackcurrant_Couscous = pd.concat([skeleton_Blackcurrant_Couscous[["metabolite", "flux"]], added_df_Blackcurrant_Couscous])
added_df_Blackcurrant_Pork = added_Blackcurrant_Pork.reset_index() 
added_df_Blackcurrant_Pork.iloc[:, 0] = added_df_Blackcurrant_Pork.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Blackcurrant_Pork.columns = ["metabolite", "flux"]
added_df_Blackcurrant_Pork = pd.concat([skeleton_Blackcurrant_Pork[["metabolite", "flux"]], added_df_Blackcurrant_Pork])
added_df_Blackcurrant_Pumpkin = added_Blackcurrant_Pumpkin.reset_index() 
added_df_Blackcurrant_Pumpkin.iloc[:, 0] = added_df_Blackcurrant_Pumpkin.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Blackcurrant_Pumpkin.columns = ["metabolite", "flux"]
added_df_Blackcurrant_Pumpkin = pd.concat([skeleton_Blackcurrant_Pumpkin[["metabolite", "flux"]], added_df_Blackcurrant_Pumpkin])
added_df_Blackcurrant_Raspberries = added_Blackcurrant_Raspberries.reset_index() 
added_df_Blackcurrant_Raspberries.iloc[:, 0] = added_df_Blackcurrant_Raspberries.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Blackcurrant_Raspberries.columns = ["metabolite", "flux"]
added_df_Blackcurrant_Raspberries = pd.concat([skeleton_Blackcurrant_Raspberries[["metabolite", "flux"]], added_df_Blackcurrant_Raspberries])
added_df_Blackcurrant_Shrimp = added_Blackcurrant_Shrimp.reset_index() 
added_df_Blackcurrant_Shrimp.iloc[:, 0] = added_df_Blackcurrant_Shrimp.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Blackcurrant_Shrimp.columns = ["metabolite", "flux"]
added_df_Blackcurrant_Shrimp = pd.concat([skeleton_Blackcurrant_Shrimp[["metabolite", "flux"]], added_df_Blackcurrant_Shrimp])
added_df_Blackcurrant_Soybean = added_Blackcurrant_Soybean.reset_index() 
added_df_Blackcurrant_Soybean.iloc[:, 0] = added_df_Blackcurrant_Soybean.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Blackcurrant_Soybean.columns = ["metabolite", "flux"]
added_df_Blackcurrant_Soybean = pd.concat([skeleton_Blackcurrant_Soybean[["metabolite", "flux"]], added_df_Blackcurrant_Soybean])
added_df_Blackcurrant_Splitpeas = added_Blackcurrant_Splitpeas.reset_index() 
added_df_Blackcurrant_Splitpeas.iloc[:, 0] = added_df_Blackcurrant_Splitpeas.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Blackcurrant_Splitpeas.columns = ["metabolite", "flux"]
added_df_Blackcurrant_Splitpeas = pd.concat([skeleton_Blackcurrant_Splitpeas[["metabolite", "flux"]], added_df_Blackcurrant_Splitpeas])
added_df_Blackcurrant_Strawberries = added_Blackcurrant_Strawberries.reset_index() 
added_df_Blackcurrant_Strawberries.iloc[:, 0] = added_df_Blackcurrant_Strawberries.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Blackcurrant_Strawberries.columns = ["metabolite", "flux"]
added_df_Blackcurrant_Strawberries = pd.concat([skeleton_Blackcurrant_Strawberries[["metabolite", "flux"]], added_df_Blackcurrant_Strawberries])
added_df_Blackcurrant_Sweetpotato = added_Blackcurrant_Sweetpotato.reset_index() 
added_df_Blackcurrant_Sweetpotato.iloc[:, 0] = added_df_Blackcurrant_Sweetpotato.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Blackcurrant_Sweetpotato.columns = ["metabolite", "flux"]
added_df_Blackcurrant_Sweetpotato = pd.concat([skeleton_Blackcurrant_Sweetpotato[["metabolite", "flux"]], added_df_Blackcurrant_Sweetpotato])
added_df_Chickpea_Couscous = added_Chickpea_Couscous.reset_index() 
added_df_Chickpea_Couscous.iloc[:, 0] = added_df_Chickpea_Couscous.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Chickpea_Couscous.columns = ["metabolite", "flux"]
added_df_Chickpea_Couscous = pd.concat([skeleton_Chickpea_Couscous[["metabolite", "flux"]], added_df_Chickpea_Couscous])
added_df_Chickpea_Pork = added_Chickpea_Pork.reset_index() 
added_df_Chickpea_Pork.iloc[:, 0] = added_df_Chickpea_Pork.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Chickpea_Pork.columns = ["metabolite", "flux"]
added_df_Chickpea_Pork = pd.concat([skeleton_Chickpea_Pork[["metabolite", "flux"]], added_df_Chickpea_Pork])
added_df_Chickpea_Pumpkin = added_Chickpea_Pumpkin.reset_index() 
added_df_Chickpea_Pumpkin.iloc[:, 0] = added_df_Chickpea_Pumpkin.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Chickpea_Pumpkin.columns = ["metabolite", "flux"]
added_df_Chickpea_Pumpkin = pd.concat([skeleton_Chickpea_Pumpkin[["metabolite", "flux"]], added_df_Chickpea_Pumpkin])
added_df_Chickpea_Raspberries = added_Chickpea_Raspberries.reset_index() 
added_df_Chickpea_Raspberries.iloc[:, 0] = added_df_Chickpea_Raspberries.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Chickpea_Raspberries.columns = ["metabolite", "flux"]
added_df_Chickpea_Raspberries = pd.concat([skeleton_Chickpea_Raspberries[["metabolite", "flux"]], added_df_Chickpea_Raspberries])
added_df_Chickpea_Shrimp = added_Chickpea_Shrimp.reset_index() 
added_df_Chickpea_Shrimp.iloc[:, 0] = added_df_Chickpea_Shrimp.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Chickpea_Shrimp.columns = ["metabolite", "flux"]
added_df_Chickpea_Shrimp = pd.concat([skeleton_Chickpea_Shrimp[["metabolite", "flux"]], added_df_Chickpea_Shrimp])
added_df_Chickpea_Soybean = added_Chickpea_Soybean.reset_index() 
added_df_Chickpea_Soybean.iloc[:, 0] = added_df_Chickpea_Soybean.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Chickpea_Soybean.columns = ["metabolite", "flux"]
added_df_Chickpea_Soybean = pd.concat([skeleton_Chickpea_Soybean[["metabolite", "flux"]], added_df_Chickpea_Soybean])
added_df_Chickpea_Splitpeas = added_Chickpea_Splitpeas.reset_index() 
added_df_Chickpea_Splitpeas.iloc[:, 0] = added_df_Chickpea_Splitpeas.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Chickpea_Splitpeas.columns = ["metabolite", "flux"]
added_df_Chickpea_Splitpeas = pd.concat([skeleton_Chickpea_Splitpeas[["metabolite", "flux"]], added_df_Chickpea_Splitpeas])
added_df_Chickpea_Strawberries = added_Chickpea_Strawberries.reset_index() 
added_df_Chickpea_Strawberries.iloc[:, 0] = added_df_Chickpea_Strawberries.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Chickpea_Strawberries.columns = ["metabolite", "flux"]
added_df_Chickpea_Strawberries = pd.concat([skeleton_Chickpea_Strawberries[["metabolite", "flux"]], added_df_Chickpea_Strawberries])
added_df_Chickpea_Sweetpotato = added_Chickpea_Sweetpotato.reset_index() 
added_df_Chickpea_Sweetpotato.iloc[:, 0] = added_df_Chickpea_Sweetpotato.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Chickpea_Sweetpotato.columns = ["metabolite", "flux"]
added_df_Chickpea_Sweetpotato = pd.concat([skeleton_Chickpea_Sweetpotato[["metabolite", "flux"]], added_df_Chickpea_Sweetpotato])
added_df_Couscous_Pork = added_Couscous_Pork.reset_index() 
added_df_Couscous_Pork.iloc[:, 0] = added_df_Couscous_Pork.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Couscous_Pork.columns = ["metabolite", "flux"]
added_df_Couscous_Pork = pd.concat([skeleton_Couscous_Pork[["metabolite", "flux"]], added_df_Couscous_Pork])
added_df_Couscous_Pumpkin = added_Couscous_Pumpkin.reset_index() 
added_df_Couscous_Pumpkin.iloc[:, 0] = added_df_Couscous_Pumpkin.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Couscous_Pumpkin.columns = ["metabolite", "flux"]
added_df_Couscous_Pumpkin = pd.concat([skeleton_Couscous_Pumpkin[["metabolite", "flux"]], added_df_Couscous_Pumpkin])
added_df_Couscous_Raspberries = added_Couscous_Raspberries.reset_index() 
added_df_Couscous_Raspberries.iloc[:, 0] = added_df_Couscous_Raspberries.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Couscous_Raspberries.columns = ["metabolite", "flux"]
added_df_Couscous_Raspberries = pd.concat([skeleton_Couscous_Raspberries[["metabolite", "flux"]], added_df_Couscous_Raspberries])
added_df_Couscous_Shrimp = added_Couscous_Shrimp.reset_index() 
added_df_Couscous_Shrimp.iloc[:, 0] = added_df_Couscous_Shrimp.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Couscous_Shrimp.columns = ["metabolite", "flux"]
added_df_Couscous_Shrimp = pd.concat([skeleton_Couscous_Shrimp[["metabolite", "flux"]], added_df_Couscous_Shrimp])
added_df_Couscous_Soybean = added_Couscous_Soybean.reset_index() 
added_df_Couscous_Soybean.iloc[:, 0] = added_df_Couscous_Soybean.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Couscous_Soybean.columns = ["metabolite", "flux"]
added_df_Couscous_Soybean = pd.concat([skeleton_Couscous_Soybean[["metabolite", "flux"]], added_df_Couscous_Soybean])
added_df_Couscous_Splitpeas = added_Couscous_Splitpeas.reset_index() 
added_df_Couscous_Splitpeas.iloc[:, 0] = added_df_Couscous_Splitpeas.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Couscous_Splitpeas.columns = ["metabolite", "flux"]
added_df_Couscous_Splitpeas = pd.concat([skeleton_Couscous_Splitpeas[["metabolite", "flux"]], added_df_Couscous_Splitpeas])
added_df_Couscous_Strawberries = added_Couscous_Strawberries.reset_index() 
added_df_Couscous_Strawberries.iloc[:, 0] = added_df_Couscous_Strawberries.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Couscous_Strawberries.columns = ["metabolite", "flux"]
added_df_Couscous_Strawberries = pd.concat([skeleton_Couscous_Strawberries[["metabolite", "flux"]], added_df_Couscous_Strawberries])
added_df_Couscous_Sweetpotato = added_Couscous_Sweetpotato.reset_index() 
added_df_Couscous_Sweetpotato.iloc[:, 0] = added_df_Couscous_Sweetpotato.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Couscous_Sweetpotato.columns = ["metabolite", "flux"]
added_df_Couscous_Sweetpotato = pd.concat([skeleton_Couscous_Sweetpotato[["metabolite", "flux"]], added_df_Couscous_Sweetpotato])
added_df_Pork_Pumpkin = added_Pork_Pumpkin.reset_index() 
added_df_Pork_Pumpkin.iloc[:, 0] = added_df_Pork_Pumpkin.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Pork_Pumpkin.columns = ["metabolite", "flux"]
added_df_Pork_Pumpkin = pd.concat([skeleton_Pork_Pumpkin[["metabolite", "flux"]], added_df_Pork_Pumpkin])
added_df_Pork_Raspberries = added_Pork_Raspberries.reset_index() 
added_df_Pork_Raspberries.iloc[:, 0] = added_df_Pork_Raspberries.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Pork_Raspberries.columns = ["metabolite", "flux"]
added_df_Pork_Raspberries = pd.concat([skeleton_Pork_Raspberries[["metabolite", "flux"]], added_df_Pork_Raspberries])
added_df_Pork_Shrimp = added_Pork_Shrimp.reset_index() 
added_df_Pork_Shrimp.iloc[:, 0] = added_df_Pork_Shrimp.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Pork_Shrimp.columns = ["metabolite", "flux"]
added_df_Pork_Shrimp = pd.concat([skeleton_Pork_Shrimp[["metabolite", "flux"]], added_df_Pork_Shrimp])
added_df_Pork_Soybean = added_Pork_Soybean.reset_index() 
added_df_Pork_Soybean.iloc[:, 0] = added_df_Pork_Soybean.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Pork_Soybean.columns = ["metabolite", "flux"]
added_df_Pork_Soybean = pd.concat([skeleton_Pork_Soybean[["metabolite", "flux"]], added_df_Pork_Soybean])
added_df_Pork_Splitpeas = added_Pork_Splitpeas.reset_index() 
added_df_Pork_Splitpeas.iloc[:, 0] = added_df_Pork_Splitpeas.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Pork_Splitpeas.columns = ["metabolite", "flux"]
added_df_Pork_Splitpeas = pd.concat([skeleton_Pork_Splitpeas[["metabolite", "flux"]], added_df_Pork_Splitpeas])
added_df_Pork_Strawberries = added_Pork_Strawberries.reset_index() 
added_df_Pork_Strawberries.iloc[:, 0] = added_df_Pork_Strawberries.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Pork_Strawberries.columns = ["metabolite", "flux"]
added_df_Pork_Strawberries = pd.concat([skeleton_Pork_Strawberries[["metabolite", "flux"]], added_df_Pork_Strawberries])
added_df_Pork_Sweetpotato = added_Pork_Sweetpotato.reset_index() 
added_df_Pork_Sweetpotato.iloc[:, 0] = added_df_Pork_Sweetpotato.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Pork_Sweetpotato.columns = ["metabolite", "flux"]
added_df_Pork_Sweetpotato = pd.concat([skeleton_Pork_Sweetpotato[["metabolite", "flux"]], added_df_Pork_Sweetpotato])
added_df_Pumpkin_Raspberries = added_Pumpkin_Raspberries.reset_index() 
added_df_Pumpkin_Raspberries.iloc[:, 0] = added_df_Pumpkin_Raspberries.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Pumpkin_Raspberries.columns = ["metabolite", "flux"]
added_df_Pumpkin_Raspberries = pd.concat([skeleton_Pumpkin_Raspberries[["metabolite", "flux"]], added_df_Pumpkin_Raspberries])
added_df_Pumpkin_Shrimp = added_Pumpkin_Shrimp.reset_index() 
added_df_Pumpkin_Shrimp.iloc[:, 0] = added_df_Pumpkin_Shrimp.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Pumpkin_Shrimp.columns = ["metabolite", "flux"]
added_df_Pumpkin_Shrimp = pd.concat([skeleton_Pumpkin_Shrimp[["metabolite", "flux"]], added_df_Pumpkin_Shrimp])
added_df_Pumpkin_Soybean = added_Pumpkin_Soybean.reset_index() 
added_df_Pumpkin_Soybean.iloc[:, 0] = added_df_Pumpkin_Soybean.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Pumpkin_Soybean.columns = ["metabolite", "flux"]
added_df_Pumpkin_Soybean = pd.concat([skeleton_Pumpkin_Soybean[["metabolite", "flux"]], added_df_Pumpkin_Soybean])
added_df_Pumpkin_Splitpeas = added_Pumpkin_Splitpeas.reset_index() 
added_df_Pumpkin_Splitpeas.iloc[:, 0] = added_df_Pumpkin_Splitpeas.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Pumpkin_Splitpeas.columns = ["metabolite", "flux"]
added_df_Pumpkin_Splitpeas = pd.concat([skeleton_Pumpkin_Splitpeas[["metabolite", "flux"]], added_df_Pumpkin_Splitpeas])
added_df_Pumpkin_Strawberries = added_Pumpkin_Strawberries.reset_index() 
added_df_Pumpkin_Strawberries.iloc[:, 0] = added_df_Pumpkin_Strawberries.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Pumpkin_Strawberries.columns = ["metabolite", "flux"]
added_df_Pumpkin_Strawberries = pd.concat([skeleton_Pumpkin_Strawberries[["metabolite", "flux"]], added_df_Pumpkin_Strawberries])
added_df_Pumpkin_Sweetpotato = added_Pumpkin_Sweetpotato.reset_index() 
added_df_Pumpkin_Sweetpotato.iloc[:, 0] = added_df_Pumpkin_Sweetpotato.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Pumpkin_Sweetpotato.columns = ["metabolite", "flux"]
added_df_Pumpkin_Sweetpotato = pd.concat([skeleton_Pumpkin_Sweetpotato[["metabolite", "flux"]], added_df_Pumpkin_Sweetpotato])
added_df_Raspberries_Shrimp = added_Raspberries_Shrimp.reset_index() 
added_df_Raspberries_Shrimp.iloc[:, 0] = added_df_Raspberries_Shrimp.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Raspberries_Shrimp.columns = ["metabolite", "flux"]
added_df_Raspberries_Shrimp = pd.concat([skeleton_Raspberries_Shrimp[["metabolite", "flux"]], added_df_Raspberries_Shrimp])
added_df_Raspberries_Soybean = added_Raspberries_Soybean.reset_index() 
added_df_Raspberries_Soybean.iloc[:, 0] = added_df_Raspberries_Soybean.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Raspberries_Soybean.columns = ["metabolite", "flux"]
added_df_Raspberries_Soybean = pd.concat([skeleton_Raspberries_Soybean[["metabolite", "flux"]], added_df_Raspberries_Soybean])
added_df_Raspberries_Splitpeas = added_Raspberries_Splitpeas.reset_index() 
added_df_Raspberries_Splitpeas.iloc[:, 0] = added_df_Raspberries_Splitpeas.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Raspberries_Splitpeas.columns = ["metabolite", "flux"]
added_df_Raspberries_Splitpeas = pd.concat([skeleton_Raspberries_Splitpeas[["metabolite", "flux"]], added_df_Raspberries_Splitpeas])
added_df_Raspberries_Strawberries = added_Raspberries_Strawberries.reset_index() 
added_df_Raspberries_Strawberries.iloc[:, 0] = added_df_Raspberries_Strawberries.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Raspberries_Strawberries.columns = ["metabolite", "flux"]
added_df_Raspberries_Strawberries = pd.concat([skeleton_Raspberries_Strawberries[["metabolite", "flux"]], added_df_Raspberries_Strawberries])
added_df_Raspberries_Sweetpotato = added_Raspberries_Sweetpotato.reset_index() 
added_df_Raspberries_Sweetpotato.iloc[:, 0] = added_df_Raspberries_Sweetpotato.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Raspberries_Sweetpotato.columns = ["metabolite", "flux"]
added_df_Raspberries_Sweetpotato = pd.concat([skeleton_Raspberries_Sweetpotato[["metabolite", "flux"]], added_df_Raspberries_Sweetpotato])
added_df_Shrimp_Soybean = added_Shrimp_Soybean.reset_index() 
added_df_Shrimp_Soybean.iloc[:, 0] = added_df_Shrimp_Soybean.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Shrimp_Soybean.columns = ["metabolite", "flux"]
added_df_Shrimp_Soybean = pd.concat([skeleton_Shrimp_Soybean[["metabolite", "flux"]], added_df_Shrimp_Soybean])
added_df_Shrimp_Splitpeas = added_Shrimp_Splitpeas.reset_index() 
added_df_Shrimp_Splitpeas.iloc[:, 0] = added_df_Shrimp_Splitpeas.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Shrimp_Splitpeas.columns = ["metabolite", "flux"]
added_df_Shrimp_Splitpeas = pd.concat([skeleton_Shrimp_Splitpeas[["metabolite", "flux"]], added_df_Shrimp_Splitpeas])
added_df_Shrimp_Strawberries = added_Shrimp_Strawberries.reset_index() 
added_df_Shrimp_Strawberries.iloc[:, 0] = added_df_Shrimp_Strawberries.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Shrimp_Strawberries.columns = ["metabolite", "flux"]
added_df_Shrimp_Strawberries = pd.concat([skeleton_Shrimp_Strawberries[["metabolite", "flux"]], added_df_Shrimp_Strawberries])
added_df_Shrimp_Sweetpotato = added_Shrimp_Sweetpotato.reset_index() 
added_df_Shrimp_Sweetpotato.iloc[:, 0] = added_df_Shrimp_Sweetpotato.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Shrimp_Sweetpotato.columns = ["metabolite", "flux"]
added_df_Shrimp_Sweetpotato = pd.concat([skeleton_Shrimp_Sweetpotato[["metabolite", "flux"]], added_df_Shrimp_Sweetpotato])
added_df_Soybean_Splitpeas = added_Soybean_Splitpeas.reset_index() 
added_df_Soybean_Splitpeas.iloc[:, 0] = added_df_Soybean_Splitpeas.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Soybean_Splitpeas.columns = ["metabolite", "flux"]
added_df_Soybean_Splitpeas = pd.concat([skeleton_Soybean_Splitpeas[["metabolite", "flux"]], added_df_Soybean_Splitpeas])
added_df_Soybean_Strawberries = added_Soybean_Strawberries.reset_index() 
added_df_Soybean_Strawberries.iloc[:, 0] = added_df_Soybean_Strawberries.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Soybean_Strawberries.columns = ["metabolite", "flux"]
added_df_Soybean_Strawberries = pd.concat([skeleton_Soybean_Strawberries[["metabolite", "flux"]], added_df_Soybean_Strawberries])
added_df_Soybean_Sweetpotato = added_Soybean_Sweetpotato.reset_index() 
added_df_Soybean_Sweetpotato.iloc[:, 0] = added_df_Soybean_Sweetpotato.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Soybean_Sweetpotato.columns = ["metabolite", "flux"]
added_df_Soybean_Sweetpotato = pd.concat([skeleton_Soybean_Sweetpotato[["metabolite", "flux"]], added_df_Soybean_Sweetpotato])
added_df_Splitpeas_Strawberries = added_Splitpeas_Strawberries.reset_index() 
added_df_Splitpeas_Strawberries.iloc[:, 0] = added_df_Splitpeas_Strawberries.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Splitpeas_Strawberries.columns = ["metabolite", "flux"]
added_df_Splitpeas_Strawberries = pd.concat([skeleton_Splitpeas_Strawberries[["metabolite", "flux"]], added_df_Splitpeas_Strawberries])
added_df_Splitpeas_Sweetpotato = added_Splitpeas_Sweetpotato.reset_index() 
added_df_Splitpeas_Sweetpotato.iloc[:, 0] = added_df_Splitpeas_Sweetpotato.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Splitpeas_Sweetpotato.columns = ["metabolite", "flux"]
added_df_Splitpeas_Sweetpotato = pd.concat([skeleton_Splitpeas_Sweetpotato[["metabolite", "flux"]], added_df_Splitpeas_Sweetpotato])
added_df_Strawberries_Sweetpotato = added_Strawberries_Sweetpotato.reset_index() 
added_df_Strawberries_Sweetpotato.iloc[:, 0] = added_df_Strawberries_Sweetpotato.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Strawberries_Sweetpotato.columns = ["metabolite", "flux"]
added_df_Strawberries_Sweetpotato = pd.concat([skeleton_Strawberries_Sweetpotato[["metabolite", "flux"]], added_df_Strawberries_Sweetpotato])

completed_Blackbeans_Blackcurrant = pd.merge(added_df_Blackbeans_Blackcurrant, annotations, on="metabolite", how="left")
completed_Blackbeans_Blackcurrant["reaction"] = "EX_" + completed_Blackbeans_Blackcurrant.metabolite + "_m"
completed_Blackbeans_Blackcurrant["global_id"] = "EX_" + completed_Blackbeans_Blackcurrant.metabolite + "(e)"
completed_Blackbeans_Chickpea = pd.merge(added_df_Blackbeans_Chickpea, annotations, on="metabolite", how="left")
completed_Blackbeans_Chickpea["reaction"] = "EX_" + completed_Blackbeans_Chickpea.metabolite + "_m"
completed_Blackbeans_Chickpea["global_id"] = "EX_" + completed_Blackbeans_Chickpea.metabolite + "(e)"
completed_Blackbeans_Couscous = pd.merge(added_df_Blackbeans_Couscous, annotations, on="metabolite", how="left")
completed_Blackbeans_Couscous["reaction"] = "EX_" + completed_Blackbeans_Couscous.metabolite + "_m"
completed_Blackbeans_Couscous["global_id"] = "EX_" + completed_Blackbeans_Couscous.metabolite + "(e)"
completed_Blackbeans_Pork = pd.merge(added_df_Blackbeans_Pork, annotations, on="metabolite", how="left")
completed_Blackbeans_Pork["reaction"] = "EX_" + completed_Blackbeans_Pork.metabolite + "_m"
completed_Blackbeans_Pork["global_id"] = "EX_" + completed_Blackbeans_Pork.metabolite + "(e)"
completed_Blackbeans_Pumpkin = pd.merge(added_df_Blackbeans_Pumpkin, annotations, on="metabolite", how="left")
completed_Blackbeans_Pumpkin["reaction"] = "EX_" + completed_Blackbeans_Pumpkin.metabolite + "_m"
completed_Blackbeans_Pumpkin["global_id"] = "EX_" + completed_Blackbeans_Pumpkin.metabolite + "(e)"
completed_Blackbeans_Raspberries = pd.merge(added_df_Blackbeans_Raspberries, annotations, on="metabolite", how="left")
completed_Blackbeans_Raspberries["reaction"] = "EX_" + completed_Blackbeans_Raspberries.metabolite + "_m"
completed_Blackbeans_Raspberries["global_id"] = "EX_" + completed_Blackbeans_Raspberries.metabolite + "(e)"
completed_Blackbeans_Shrimp = pd.merge(added_df_Blackbeans_Shrimp, annotations, on="metabolite", how="left")
completed_Blackbeans_Shrimp["reaction"] = "EX_" + completed_Blackbeans_Shrimp.metabolite + "_m"
completed_Blackbeans_Shrimp["global_id"] = "EX_" + completed_Blackbeans_Shrimp.metabolite + "(e)"
completed_Blackbeans_Soybean = pd.merge(added_df_Blackbeans_Soybean, annotations, on="metabolite", how="left")
completed_Blackbeans_Soybean["reaction"] = "EX_" + completed_Blackbeans_Soybean.metabolite + "_m"
completed_Blackbeans_Soybean["global_id"] = "EX_" + completed_Blackbeans_Soybean.metabolite + "(e)"
completed_Blackbeans_Splitpeas = pd.merge(added_df_Blackbeans_Splitpeas, annotations, on="metabolite", how="left")
completed_Blackbeans_Splitpeas["reaction"] = "EX_" + completed_Blackbeans_Splitpeas.metabolite + "_m"
completed_Blackbeans_Splitpeas["global_id"] = "EX_" + completed_Blackbeans_Splitpeas.metabolite + "(e)"
completed_Blackbeans_Strawberries = pd.merge(added_df_Blackbeans_Strawberries, annotations, on="metabolite", how="left")
completed_Blackbeans_Strawberries["reaction"] = "EX_" + completed_Blackbeans_Strawberries.metabolite + "_m"
completed_Blackbeans_Strawberries["global_id"] = "EX_" + completed_Blackbeans_Strawberries.metabolite + "(e)"
completed_Blackbeans_Sweetpotato = pd.merge(added_df_Blackbeans_Sweetpotato, annotations, on="metabolite", how="left")
completed_Blackbeans_Sweetpotato["reaction"] = "EX_" + completed_Blackbeans_Sweetpotato.metabolite + "_m"
completed_Blackbeans_Sweetpotato["global_id"] = "EX_" + completed_Blackbeans_Sweetpotato.metabolite + "(e)"
completed_Blackcurrant_Chickpea = pd.merge(added_df_Blackcurrant_Chickpea, annotations, on="metabolite", how="left")
completed_Blackcurrant_Chickpea["reaction"] = "EX_" + completed_Blackcurrant_Chickpea.metabolite + "_m"
completed_Blackcurrant_Chickpea["global_id"] = "EX_" + completed_Blackcurrant_Chickpea.metabolite + "(e)"
completed_Blackcurrant_Couscous = pd.merge(added_df_Blackcurrant_Couscous, annotations, on="metabolite", how="left")
completed_Blackcurrant_Couscous["reaction"] = "EX_" + completed_Blackcurrant_Couscous.metabolite + "_m"
completed_Blackcurrant_Couscous["global_id"] = "EX_" + completed_Blackcurrant_Couscous.metabolite + "(e)"
completed_Blackcurrant_Pork = pd.merge(added_df_Blackcurrant_Pork, annotations, on="metabolite", how="left")
completed_Blackcurrant_Pork["reaction"] = "EX_" + completed_Blackcurrant_Pork.metabolite + "_m"
completed_Blackcurrant_Pork["global_id"] = "EX_" + completed_Blackcurrant_Pork.metabolite + "(e)"
completed_Blackcurrant_Pumpkin = pd.merge(added_df_Blackcurrant_Pumpkin, annotations, on="metabolite", how="left")
completed_Blackcurrant_Pumpkin["reaction"] = "EX_" + completed_Blackcurrant_Pumpkin.metabolite + "_m"
completed_Blackcurrant_Pumpkin["global_id"] = "EX_" + completed_Blackcurrant_Pumpkin.metabolite + "(e)"
completed_Blackcurrant_Raspberries = pd.merge(added_df_Blackcurrant_Raspberries, annotations, on="metabolite", how="left")
completed_Blackcurrant_Raspberries["reaction"] = "EX_" + completed_Blackcurrant_Raspberries.metabolite + "_m"
completed_Blackcurrant_Raspberries["global_id"] = "EX_" + completed_Blackcurrant_Raspberries.metabolite + "(e)"
completed_Blackcurrant_Shrimp = pd.merge(added_df_Blackcurrant_Shrimp, annotations, on="metabolite", how="left")
completed_Blackcurrant_Shrimp["reaction"] = "EX_" + completed_Blackcurrant_Shrimp.metabolite + "_m"
completed_Blackcurrant_Shrimp["global_id"] = "EX_" + completed_Blackcurrant_Shrimp.metabolite + "(e)"
completed_Blackcurrant_Soybean = pd.merge(added_df_Blackcurrant_Soybean, annotations, on="metabolite", how="left")
completed_Blackcurrant_Soybean["reaction"] = "EX_" + completed_Blackcurrant_Soybean.metabolite + "_m"
completed_Blackcurrant_Soybean["global_id"] = "EX_" + completed_Blackcurrant_Soybean.metabolite + "(e)"
completed_Blackcurrant_Splitpeas = pd.merge(added_df_Blackcurrant_Splitpeas, annotations, on="metabolite", how="left")
completed_Blackcurrant_Splitpeas["reaction"] = "EX_" + completed_Blackcurrant_Splitpeas.metabolite + "_m"
completed_Blackcurrant_Splitpeas["global_id"] = "EX_" + completed_Blackcurrant_Splitpeas.metabolite + "(e)"
completed_Blackcurrant_Strawberries = pd.merge(added_df_Blackcurrant_Strawberries, annotations, on="metabolite", how="left")
completed_Blackcurrant_Strawberries["reaction"] = "EX_" + completed_Blackcurrant_Strawberries.metabolite + "_m"
completed_Blackcurrant_Strawberries["global_id"] = "EX_" + completed_Blackcurrant_Strawberries.metabolite + "(e)"
completed_Blackcurrant_Sweetpotato = pd.merge(added_df_Blackcurrant_Sweetpotato, annotations, on="metabolite", how="left")
completed_Blackcurrant_Sweetpotato["reaction"] = "EX_" + completed_Blackcurrant_Sweetpotato.metabolite + "_m"
completed_Blackcurrant_Sweetpotato["global_id"] = "EX_" + completed_Blackcurrant_Sweetpotato.metabolite + "(e)"
completed_Chickpea_Couscous = pd.merge(added_df_Chickpea_Couscous, annotations, on="metabolite", how="left")
completed_Chickpea_Couscous["reaction"] = "EX_" + completed_Chickpea_Couscous.metabolite + "_m"
completed_Chickpea_Couscous["global_id"] = "EX_" + completed_Chickpea_Couscous.metabolite + "(e)"
completed_Chickpea_Pork = pd.merge(added_df_Chickpea_Pork, annotations, on="metabolite", how="left")
completed_Chickpea_Pork["reaction"] = "EX_" + completed_Chickpea_Pork.metabolite + "_m"
completed_Chickpea_Pork["global_id"] = "EX_" + completed_Chickpea_Pork.metabolite + "(e)"
completed_Chickpea_Pumpkin = pd.merge(added_df_Chickpea_Pumpkin, annotations, on="metabolite", how="left")
completed_Chickpea_Pumpkin["reaction"] = "EX_" + completed_Chickpea_Pumpkin.metabolite + "_m"
completed_Chickpea_Pumpkin["global_id"] = "EX_" + completed_Chickpea_Pumpkin.metabolite + "(e)"
completed_Chickpea_Raspberries = pd.merge(added_df_Chickpea_Raspberries, annotations, on="metabolite", how="left")
completed_Chickpea_Raspberries["reaction"] = "EX_" + completed_Chickpea_Raspberries.metabolite + "_m"
completed_Chickpea_Raspberries["global_id"] = "EX_" + completed_Chickpea_Raspberries.metabolite + "(e)"
completed_Chickpea_Shrimp = pd.merge(added_df_Chickpea_Shrimp, annotations, on="metabolite", how="left")
completed_Chickpea_Shrimp["reaction"] = "EX_" + completed_Chickpea_Shrimp.metabolite + "_m"
completed_Chickpea_Shrimp["global_id"] = "EX_" + completed_Chickpea_Shrimp.metabolite + "(e)"
completed_Chickpea_Soybean = pd.merge(added_df_Chickpea_Soybean, annotations, on="metabolite", how="left")
completed_Chickpea_Soybean["reaction"] = "EX_" + completed_Chickpea_Soybean.metabolite + "_m"
completed_Chickpea_Soybean["global_id"] = "EX_" + completed_Chickpea_Soybean.metabolite + "(e)"
completed_Chickpea_Splitpeas = pd.merge(added_df_Chickpea_Splitpeas, annotations, on="metabolite", how="left")
completed_Chickpea_Splitpeas["reaction"] = "EX_" + completed_Chickpea_Splitpeas.metabolite + "_m"
completed_Chickpea_Splitpeas["global_id"] = "EX_" + completed_Chickpea_Splitpeas.metabolite + "(e)"
completed_Chickpea_Strawberries = pd.merge(added_df_Chickpea_Strawberries, annotations, on="metabolite", how="left")
completed_Chickpea_Strawberries["reaction"] = "EX_" + completed_Chickpea_Strawberries.metabolite + "_m"
completed_Chickpea_Strawberries["global_id"] = "EX_" + completed_Chickpea_Strawberries.metabolite + "(e)"
completed_Chickpea_Sweetpotato = pd.merge(added_df_Chickpea_Sweetpotato, annotations, on="metabolite", how="left")
completed_Chickpea_Sweetpotato["reaction"] = "EX_" + completed_Chickpea_Sweetpotato.metabolite + "_m"
completed_Chickpea_Sweetpotato["global_id"] = "EX_" + completed_Chickpea_Sweetpotato.metabolite + "(e)"
completed_Couscous_Pork = pd.merge(added_df_Couscous_Pork, annotations, on="metabolite", how="left")
completed_Couscous_Pork["reaction"] = "EX_" + completed_Couscous_Pork.metabolite + "_m"
completed_Couscous_Pork["global_id"] = "EX_" + completed_Couscous_Pork.metabolite + "(e)"
completed_Couscous_Pumpkin = pd.merge(added_df_Couscous_Pumpkin, annotations, on="metabolite", how="left")
completed_Couscous_Pumpkin["reaction"] = "EX_" + completed_Couscous_Pumpkin.metabolite + "_m"
completed_Couscous_Pumpkin["global_id"] = "EX_" + completed_Couscous_Pumpkin.metabolite + "(e)"
completed_Couscous_Raspberries = pd.merge(added_df_Couscous_Raspberries, annotations, on="metabolite", how="left")
completed_Couscous_Raspberries["reaction"] = "EX_" + completed_Couscous_Raspberries.metabolite + "_m"
completed_Couscous_Raspberries["global_id"] = "EX_" + completed_Couscous_Raspberries.metabolite + "(e)"
completed_Couscous_Shrimp = pd.merge(added_df_Couscous_Shrimp, annotations, on="metabolite", how="left")
completed_Couscous_Shrimp["reaction"] = "EX_" + completed_Couscous_Shrimp.metabolite + "_m"
completed_Couscous_Shrimp["global_id"] = "EX_" + completed_Couscous_Shrimp.metabolite + "(e)"
completed_Couscous_Soybean = pd.merge(added_df_Couscous_Soybean, annotations, on="metabolite", how="left")
completed_Couscous_Soybean["reaction"] = "EX_" + completed_Couscous_Soybean.metabolite + "_m"
completed_Couscous_Soybean["global_id"] = "EX_" + completed_Couscous_Soybean.metabolite + "(e)"
completed_Couscous_Splitpeas = pd.merge(added_df_Couscous_Splitpeas, annotations, on="metabolite", how="left")
completed_Couscous_Splitpeas["reaction"] = "EX_" + completed_Couscous_Splitpeas.metabolite + "_m"
completed_Couscous_Splitpeas["global_id"] = "EX_" + completed_Couscous_Splitpeas.metabolite + "(e)"
completed_Couscous_Strawberries = pd.merge(added_df_Couscous_Strawberries, annotations, on="metabolite", how="left")
completed_Couscous_Strawberries["reaction"] = "EX_" + completed_Couscous_Strawberries.metabolite + "_m"
completed_Couscous_Strawberries["global_id"] = "EX_" + completed_Couscous_Strawberries.metabolite + "(e)"
completed_Couscous_Sweetpotato = pd.merge(added_df_Couscous_Sweetpotato, annotations, on="metabolite", how="left")
completed_Couscous_Sweetpotato["reaction"] = "EX_" + completed_Couscous_Sweetpotato.metabolite + "_m"
completed_Couscous_Sweetpotato["global_id"] = "EX_" + completed_Couscous_Sweetpotato.metabolite + "(e)"
completed_Pork_Pumpkin = pd.merge(added_df_Pork_Pumpkin, annotations, on="metabolite", how="left")
completed_Pork_Pumpkin["reaction"] = "EX_" + completed_Pork_Pumpkin.metabolite + "_m"
completed_Pork_Pumpkin["global_id"] = "EX_" + completed_Pork_Pumpkin.metabolite + "(e)"
completed_Pork_Raspberries = pd.merge(added_df_Pork_Raspberries, annotations, on="metabolite", how="left")
completed_Pork_Raspberries["reaction"] = "EX_" + completed_Pork_Raspberries.metabolite + "_m"
completed_Pork_Raspberries["global_id"] = "EX_" + completed_Pork_Raspberries.metabolite + "(e)"
completed_Pork_Shrimp = pd.merge(added_df_Pork_Shrimp, annotations, on="metabolite", how="left")
completed_Pork_Shrimp["reaction"] = "EX_" + completed_Pork_Shrimp.metabolite + "_m"
completed_Pork_Shrimp["global_id"] = "EX_" + completed_Pork_Shrimp.metabolite + "(e)"
completed_Pork_Soybean = pd.merge(added_df_Pork_Soybean, annotations, on="metabolite", how="left")
completed_Pork_Soybean["reaction"] = "EX_" + completed_Pork_Soybean.metabolite + "_m"
completed_Pork_Soybean["global_id"] = "EX_" + completed_Pork_Soybean.metabolite + "(e)"
completed_Pork_Splitpeas = pd.merge(added_df_Pork_Splitpeas, annotations, on="metabolite", how="left")
completed_Pork_Splitpeas["reaction"] = "EX_" + completed_Pork_Splitpeas.metabolite + "_m"
completed_Pork_Splitpeas["global_id"] = "EX_" + completed_Pork_Splitpeas.metabolite + "(e)"
completed_Pork_Strawberries = pd.merge(added_df_Pork_Strawberries, annotations, on="metabolite", how="left")
completed_Pork_Strawberries["reaction"] = "EX_" + completed_Pork_Strawberries.metabolite + "_m"
completed_Pork_Strawberries["global_id"] = "EX_" + completed_Pork_Strawberries.metabolite + "(e)"
completed_Pork_Sweetpotato = pd.merge(added_df_Pork_Sweetpotato, annotations, on="metabolite", how="left")
completed_Pork_Sweetpotato["reaction"] = "EX_" + completed_Pork_Sweetpotato.metabolite + "_m"
completed_Pork_Sweetpotato["global_id"] = "EX_" + completed_Pork_Sweetpotato.metabolite + "(e)"
completed_Pumpkin_Raspberries = pd.merge(added_df_Pumpkin_Raspberries, annotations, on="metabolite", how="left")
completed_Pumpkin_Raspberries["reaction"] = "EX_" + completed_Pumpkin_Raspberries.metabolite + "_m"
completed_Pumpkin_Raspberries["global_id"] = "EX_" + completed_Pumpkin_Raspberries.metabolite + "(e)"
completed_Pumpkin_Shrimp = pd.merge(added_df_Pumpkin_Shrimp, annotations, on="metabolite", how="left")
completed_Pumpkin_Shrimp["reaction"] = "EX_" + completed_Pumpkin_Shrimp.metabolite + "_m"
completed_Pumpkin_Shrimp["global_id"] = "EX_" + completed_Pumpkin_Shrimp.metabolite + "(e)"
completed_Pumpkin_Soybean = pd.merge(added_df_Pumpkin_Soybean, annotations, on="metabolite", how="left")
completed_Pumpkin_Soybean["reaction"] = "EX_" + completed_Pumpkin_Soybean.metabolite + "_m"
completed_Pumpkin_Soybean["global_id"] = "EX_" + completed_Pumpkin_Soybean.metabolite + "(e)"
completed_Pumpkin_Splitpeas = pd.merge(added_df_Pumpkin_Splitpeas, annotations, on="metabolite", how="left")
completed_Pumpkin_Splitpeas["reaction"] = "EX_" + completed_Pumpkin_Splitpeas.metabolite + "_m"
completed_Pumpkin_Splitpeas["global_id"] = "EX_" + completed_Pumpkin_Splitpeas.metabolite + "(e)"
completed_Pumpkin_Strawberries = pd.merge(added_df_Pumpkin_Strawberries, annotations, on="metabolite", how="left")
completed_Pumpkin_Strawberries["reaction"] = "EX_" + completed_Pumpkin_Strawberries.metabolite + "_m"
completed_Pumpkin_Strawberries["global_id"] = "EX_" + completed_Pumpkin_Strawberries.metabolite + "(e)"
completed_Pumpkin_Sweetpotato = pd.merge(added_df_Pumpkin_Sweetpotato, annotations, on="metabolite", how="left")
completed_Pumpkin_Sweetpotato["reaction"] = "EX_" + completed_Pumpkin_Sweetpotato.metabolite + "_m"
completed_Pumpkin_Sweetpotato["global_id"] = "EX_" + completed_Pumpkin_Sweetpotato.metabolite + "(e)"
completed_Raspberries_Shrimp = pd.merge(added_df_Raspberries_Shrimp, annotations, on="metabolite", how="left")
completed_Raspberries_Shrimp["reaction"] = "EX_" + completed_Raspberries_Shrimp.metabolite + "_m"
completed_Raspberries_Shrimp["global_id"] = "EX_" + completed_Raspberries_Shrimp.metabolite + "(e)"
completed_Raspberries_Soybean = pd.merge(added_df_Raspberries_Soybean, annotations, on="metabolite", how="left")
completed_Raspberries_Soybean["reaction"] = "EX_" + completed_Raspberries_Soybean.metabolite + "_m"
completed_Raspberries_Soybean["global_id"] = "EX_" + completed_Raspberries_Soybean.metabolite + "(e)"
completed_Raspberries_Splitpeas = pd.merge(added_df_Raspberries_Splitpeas, annotations, on="metabolite", how="left")
completed_Raspberries_Splitpeas["reaction"] = "EX_" + completed_Raspberries_Splitpeas.metabolite + "_m"
completed_Raspberries_Splitpeas["global_id"] = "EX_" + completed_Raspberries_Splitpeas.metabolite + "(e)"
completed_Raspberries_Strawberries = pd.merge(added_df_Raspberries_Strawberries, annotations, on="metabolite", how="left")
completed_Raspberries_Strawberries["reaction"] = "EX_" + completed_Raspberries_Strawberries.metabolite + "_m"
completed_Raspberries_Strawberries["global_id"] = "EX_" + completed_Raspberries_Strawberries.metabolite + "(e)"
completed_Raspberries_Sweetpotato = pd.merge(added_df_Raspberries_Sweetpotato, annotations, on="metabolite", how="left")
completed_Raspberries_Sweetpotato["reaction"] = "EX_" + completed_Raspberries_Sweetpotato.metabolite + "_m"
completed_Raspberries_Sweetpotato["global_id"] = "EX_" + completed_Raspberries_Sweetpotato.metabolite + "(e)"
completed_Shrimp_Soybean = pd.merge(added_df_Shrimp_Soybean, annotations, on="metabolite", how="left")
completed_Shrimp_Soybean["reaction"] = "EX_" + completed_Shrimp_Soybean.metabolite + "_m"
completed_Shrimp_Soybean["global_id"] = "EX_" + completed_Shrimp_Soybean.metabolite + "(e)"
completed_Shrimp_Splitpeas = pd.merge(added_df_Shrimp_Splitpeas, annotations, on="metabolite", how="left")
completed_Shrimp_Splitpeas["reaction"] = "EX_" + completed_Shrimp_Splitpeas.metabolite + "_m"
completed_Shrimp_Splitpeas["global_id"] = "EX_" + completed_Shrimp_Splitpeas.metabolite + "(e)"
completed_Shrimp_Strawberries = pd.merge(added_df_Shrimp_Strawberries, annotations, on="metabolite", how="left")
completed_Shrimp_Strawberries["reaction"] = "EX_" + completed_Shrimp_Strawberries.metabolite + "_m"
completed_Shrimp_Strawberries["global_id"] = "EX_" + completed_Shrimp_Strawberries.metabolite + "(e)"
completed_Shrimp_Sweetpotato = pd.merge(added_df_Shrimp_Sweetpotato, annotations, on="metabolite", how="left")
completed_Shrimp_Sweetpotato["reaction"] = "EX_" + completed_Shrimp_Sweetpotato.metabolite + "_m"
completed_Shrimp_Sweetpotato["global_id"] = "EX_" + completed_Shrimp_Sweetpotato.metabolite + "(e)"
completed_Soybean_Splitpeas = pd.merge(added_df_Soybean_Splitpeas, annotations, on="metabolite", how="left")
completed_Soybean_Splitpeas["reaction"] = "EX_" + completed_Soybean_Splitpeas.metabolite + "_m"
completed_Soybean_Splitpeas["global_id"] = "EX_" + completed_Soybean_Splitpeas.metabolite + "(e)"
completed_Soybean_Strawberries = pd.merge(added_df_Soybean_Strawberries, annotations, on="metabolite", how="left")
completed_Soybean_Strawberries["reaction"] = "EX_" + completed_Soybean_Strawberries.metabolite + "_m"
completed_Soybean_Strawberries["global_id"] = "EX_" + completed_Soybean_Strawberries.metabolite + "(e)"
completed_Soybean_Sweetpotato = pd.merge(added_df_Soybean_Sweetpotato, annotations, on="metabolite", how="left")
completed_Soybean_Sweetpotato["reaction"] = "EX_" + completed_Soybean_Sweetpotato.metabolite + "_m"
completed_Soybean_Sweetpotato["global_id"] = "EX_" + completed_Soybean_Sweetpotato.metabolite + "(e)"
completed_Splitpeas_Strawberries = pd.merge(added_df_Splitpeas_Strawberries, annotations, on="metabolite", how="left")
completed_Splitpeas_Strawberries["reaction"] = "EX_" + completed_Splitpeas_Strawberries.metabolite + "_m"
completed_Splitpeas_Strawberries["global_id"] = "EX_" + completed_Splitpeas_Strawberries.metabolite + "(e)"
completed_Splitpeas_Sweetpotato = pd.merge(added_df_Splitpeas_Sweetpotato, annotations, on="metabolite", how="left")
completed_Splitpeas_Sweetpotato["reaction"] = "EX_" + completed_Splitpeas_Sweetpotato.metabolite + "_m"
completed_Splitpeas_Sweetpotato["global_id"] = "EX_" + completed_Splitpeas_Sweetpotato.metabolite + "(e)"
completed_Strawberries_Sweetpotato = pd.merge(added_df_Strawberries_Sweetpotato, annotations, on="metabolite", how="left")
completed_Strawberries_Sweetpotato["reaction"] = "EX_" + completed_Strawberries_Sweetpotato.metabolite + "_m"
completed_Strawberries_Sweetpotato["global_id"] = "EX_" + completed_Strawberries_Sweetpotato.metabolite + "(e)"

#Saving the medium
completed_Blackbeans_Blackcurrant.to_csv("media/Blackbeans_Blackcurrant_breastmilk.csv") 
completed_Blackbeans_Chickpea.to_csv("media/Blackbeans_Chickpea_breastmilk.csv") 
completed_Blackbeans_Couscous.to_csv("media/Blackbeans_Couscous_breastmilk.csv") 
completed_Blackbeans_Pork.to_csv("media/Blackbeans_Pork_breastmilk.csv") 
completed_Blackbeans_Pumpkin.to_csv("media/Blackbeans_Pumpkin_breastmilk.csv") 
completed_Blackbeans_Raspberries.to_csv("media/Blackbeans_Raspberries_breastmilk.csv") 
completed_Blackbeans_Shrimp.to_csv("media/Blackbeans_Shrimp_breastmilk.csv") 
completed_Blackbeans_Soybean.to_csv("media/Blackbeans_Soybean_breastmilk.csv") 
completed_Blackbeans_Splitpeas.to_csv("media/Blackbeans_Splitpeas_breastmilk.csv") 
completed_Blackbeans_Strawberries.to_csv("media/Blackbeans_Strawberries_breastmilk.csv") 
completed_Blackbeans_Sweetpotato.to_csv("media/Blackbeans_Sweetpotato_breastmilk.csv") 
completed_Blackcurrant_Chickpea.to_csv("media/Blackcurrant_Chickpea_breastmilk.csv") 
completed_Blackcurrant_Couscous.to_csv("media/Blackcurrant_Couscous_breastmilk.csv") 
completed_Blackcurrant_Pork.to_csv("media/Blackcurrant_Pork_breastmilk.csv") 
completed_Blackcurrant_Pumpkin.to_csv("media/Blackcurrant_Pumpkin_breastmilk.csv") 
completed_Blackcurrant_Raspberries.to_csv("media/Blackcurrant_Raspberries_breastmilk.csv") 
completed_Blackcurrant_Shrimp.to_csv("media/Blackcurrant_Shrimp_breastmilk.csv") 
completed_Blackcurrant_Soybean.to_csv("media/Blackcurrant_Soybean_breastmilk.csv") 
completed_Blackcurrant_Splitpeas.to_csv("media/Blackcurrant_Splitpeas_breastmilk.csv") 
completed_Blackcurrant_Strawberries.to_csv("media/Blackcurrant_Strawberries_breastmilk.csv") 
completed_Blackcurrant_Sweetpotato.to_csv("media/Blackcurrant_Sweetpotato_breastmilk.csv") 
completed_Chickpea_Couscous.to_csv("media/Chickpea_Couscous_breastmilk.csv") 
completed_Chickpea_Pork.to_csv("media/Chickpea_Pork_breastmilk.csv") 
completed_Chickpea_Pumpkin.to_csv("media/Chickpea_Pumpkin_breastmilk.csv") 
completed_Chickpea_Raspberries.to_csv("media/Chickpea_Raspberries_breastmilk.csv") 
completed_Chickpea_Shrimp.to_csv("media/Chickpea_Shrimp_breastmilk.csv") 
completed_Chickpea_Soybean.to_csv("media/Chickpea_Soybean_breastmilk.csv") 
completed_Chickpea_Splitpeas.to_csv("media/Chickpea_Splitpeas_breastmilk.csv") 
completed_Chickpea_Strawberries.to_csv("media/Chickpea_Strawberries_breastmilk.csv") 
completed_Chickpea_Sweetpotato.to_csv("media/Chickpea_Sweetpotato_breastmilk.csv") 
completed_Couscous_Pork.to_csv("media/Couscous_Pork_breastmilk.csv") 
completed_Couscous_Pumpkin.to_csv("media/Couscous_Pumpkin_breastmilk.csv") 
completed_Couscous_Raspberries.to_csv("media/Couscous_Raspberries_breastmilk.csv") 
completed_Couscous_Shrimp.to_csv("media/Couscous_Shrimp_breastmilk.csv") 
completed_Couscous_Soybean.to_csv("media/Couscous_Soybean_breastmilk.csv") 
completed_Couscous_Splitpeas.to_csv("media/Couscous_Splitpeas_breastmilk.csv") 
completed_Couscous_Strawberries.to_csv("media/Couscous_Strawberries_breastmilk.csv") 
completed_Couscous_Sweetpotato.to_csv("media/Couscous_Sweetpotato_breastmilk.csv") 
completed_Pork_Pumpkin.to_csv("media/Pork_Pumpkin_breastmilk.csv") 
completed_Pork_Raspberries.to_csv("media/Pork_Raspberries_breastmilk.csv") 
completed_Pork_Shrimp.to_csv("media/Pork_Shrimp_breastmilk.csv") 
completed_Pork_Soybean.to_csv("media/Pork_Soybean_breastmilk.csv") 
completed_Pork_Splitpeas.to_csv("media/Pork_Splitpeas_breastmilk.csv") 
completed_Pork_Strawberries.to_csv("media/Pork_Strawberries_breastmilk.csv") 
completed_Pork_Sweetpotato.to_csv("media/Pork_Sweetpotato_breastmilk.csv") 
completed_Pumpkin_Raspberries.to_csv("media/Pumpkin_Raspberries_breastmilk.csv") 
completed_Pumpkin_Shrimp.to_csv("media/Pumpkin_Shrimp_breastmilk.csv") 
completed_Pumpkin_Soybean.to_csv("media/Pumpkin_Soybean_breastmilk.csv") 
completed_Pumpkin_Splitpeas.to_csv("media/Pumpkin_Splitpeas_breastmilk.csv") 
completed_Pumpkin_Strawberries.to_csv("media/Pumpkin_Strawberries_breastmilk.csv") 
completed_Pumpkin_Sweetpotato.to_csv("media/Pumpkin_Sweetpotato_breastmilk.csv") 
completed_Raspberries_Shrimp.to_csv("media/Raspberries_Shrimp_breastmilk.csv") 
completed_Raspberries_Soybean.to_csv("media/Raspberries_Soybean_breastmilk.csv")
completed_Raspberries_Splitpeas.to_csv("media/Raspberries_Splitpeas_breastmilk.csv") 
completed_Raspberries_Strawberries.to_csv("media/Raspberries_Strawberries_breastmilk.csv") 
completed_Raspberries_Sweetpotato.to_csv("media/Raspberries_Sweetpotato_breastmilk.csv") 
completed_Shrimp_Soybean.to_csv("media/Shrimp_Soybean_breastmilk.csv") 
completed_Shrimp_Splitpeas.to_csv("media/Shrimp_Splitpeas_breastmilk.csv") 
completed_Shrimp_Strawberries.to_csv("media/Shrimp_Strawberries_breastmilk.csv") 
completed_Shrimp_Sweetpotato.to_csv("media/Shrimp_Sweetpotato_breastmilk.csv") 
completed_Soybean_Splitpeas.to_csv("media/Soybean_Splitpeas_breastmilk.csv") 
completed_Soybean_Strawberries.to_csv("media/Soybean_Strawberries_breastmilk.csv") 
completed_Soybean_Sweetpotato.to_csv("media/Soybean_Sweetpotato_breastmilk.csv") 
completed_Splitpeas_Strawberries.to_csv("media/Splitpeas_Strawberries_breastmilk.csv") 
completed_Splitpeas_Sweetpotato.to_csv("media/Splitpeas_Sweetpotato_breastmilk.csv") 
completed_Strawberries_Sweetpotato.to_csv("media/Strawberries_Sweetpotato_breastmilk.csv") 

#importing medium
#import pandas as pd

#completed_Blackbeans_Blackcurrant = pd.read_csv("media/Blackbeans_Blackcurrant_breastmilk.csv") 
#completed_Blackbeans_Chickpea = pd.read_csv("media/Blackbeans_Chickpea_breastmilk.csv") 
#completed_Blackbeans_Couscous = pd.read_csv("media/Blackbeans_Couscous_breastmilk.csv") 
#completed_Blackbeans_Pork = pd.read_csv("media/Blackbeans_Pork_breastmilk.csv") 
#completed_Blackbeans_Pumpkin = pd.read_csv("media/Blackbeans_Pumpkin_breastmilk.csv") 
#completed_Blackbeans_Raspberries = pd.read_csv("media/Blackbeans_Raspberries_breastmilk.csv") 
#completed_Blackbeans_Shrimp = pd.read_csv("media/Blackbeans_Shrimp_breastmilk.csv") 
#completed_Blackbeans_Soybean = pd.read_csv("media/Blackbeans_Soybean_breastmilk.csv") 
#completed_Blackbeans_Splitpeas = pd.read_csv("media/Blackbeans_Splitpeas_breastmilk.csv") 
#completed_Blackbeans_Strawberries = pd.read_csv("media/Blackbeans_Strawberries_breastmilk.csv") 
#completed_Blackbeans_Sweetpotato = pd.read_csv("media/Blackbeans_Sweetpotato_breastmilk.csv") 
#completed_Blackcurrant_Chickpea = pd.read_csv("media/Blackcurrant_Chickpea_breastmilk.csv") 
#completed_Blackcurrant_Couscous = pd.read_csv("media/Blackcurrant_Couscous_breastmilk.csv") 
#completed_Blackcurrant_Pork = pd.read_csv("media/Blackcurrant_Pork_breastmilk.csv") 
#completed_Blackcurrant_Pumpkin = pd.read_csv("media/Blackcurrant_Pumpkin_breastmilk.csv") 
#completed_Blackcurrant_Raspberries = pd.read_csv("media/Blackcurrant_Raspberries_breastmilk.csv") 
#completed_Blackcurrant_Shrimp = pd.read_csv("media/Blackcurrant_Shrimp_breastmilk.csv") 
#completed_Blackcurrant_Soybean = pd.read_csv("media/Blackcurrant_Soybean_breastmilk.csv") 
#completed_Blackcurrant_Splitpeas = pd.read_csv("media/Blackcurrant_Splitpeas_breastmilk.csv") 
#completed_Blackcurrant_Strawberries = pd.read_csv("media/Blackcurrant_Strawberries_breastmilk.csv") 
#completed_Blackcurrant_Sweetpotato = pd.read_csv("media/Blackcurrant_Sweetpotato_breastmilk.csv") 
#completed_Chickpea_Couscous = pd.read_csv("media/Chickpea_Couscous_breastmilk.csv") 
#completed_Chickpea_Pork = pd.read_csv("media/Chickpea_Pork_breastmilk.csv") 
#completed_Chickpea_Pumpkin = pd.read_csv("media/Chickpea_Pumpkin_breastmilk.csv") 
#completed_Chickpea_Raspberries = pd.read_csv("media/Chickpea_Raspberries_breastmilk.csv") 
#completed_Chickpea_Shrimp = pd.read_csv("media/Chickpea_Shrimp_breastmilk.csv") 
#completed_Chickpea_Soybean = pd.read_csv("media/Chickpea_Soybean_breastmilk.csv") 
#completed_Chickpea_Splitpeas = pd.read_csv("media/Chickpea_Splitpeas_breastmilk.csv") 
#completed_Chickpea_Strawberries = pd.read_csv("media/Chickpea_Strawberries_breastmilk.csv") 
#completed_Chickpea_Sweetpotato = pd.read_csv("media/Chickpea_Sweetpotato_breastmilk.csv") 
#completed_Couscous_Pork = pd.read_csv("media/Couscous_Pork_breastmilk.csv") 
#completed_Couscous_Pumpkin = pd.read_csv("media/Couscous_Pumpkin_breastmilk.csv") 
#completed_Couscous_Raspberries = pd.read_csv("media/Couscous_Raspberries_breastmilk.csv") 
#completed_Couscous_Shrimp = pd.read_csv("media/Couscous_Shrimp_breastmilk.csv") 
#completed_Couscous_Soybean = pd.read_csv("media/Couscous_Soybean_breastmilk.csv") 
#completed_Couscous_Splitpeas = pd.read_csv("media/Couscous_Splitpeas_breastmilk.csv") 
#completed_Couscous_Strawberries = pd.read_csv("media/Couscous_Strawberries_breastmilk.csv") 
#completed_Couscous_Sweetpotato = pd.read_csv("media/Couscous_Sweetpotato_breastmilk.csv") 
#completed_Pork_Pumpkin = pd.read_csv("media/Pork_Pumpkin_breastmilk.csv") 
#completed_Pork_Raspberries = pd.read_csv("media/Pork_Raspberries_breastmilk.csv") 
#completed_Pork_Shrimp = pd.read_csv("media/Pork_Shrimp_breastmilk.csv") 
#completed_Pork_Soybean = pd.read_csv("media/Pork_Soybean_breastmilk.csv") 
#completed_Pork_Splitpeas = pd.read_csv("media/Pork_Splitpeas_breastmilk.csv") 
#completed_Pork_Strawberries = pd.read_csv("media/Pork_Strawberries_breastmilk.csv") 
#completed_Pork_Sweetpotato = pd.read_csv("media/Pork_Sweetpotato_breastmilk.csv") 
#completed_Pumpkin_Raspberries = pd.read_csv("media/Pumpkin_Raspberries_breastmilk.csv") 
#completed_Pumpkin_Shrimp = pd.read_csv("media/Pumpkin_Shrimp_breastmilk.csv") 
#completed_Pumpkin_Soybean = pd.read_csv("media/Pumpkin_Soybean_breastmilk.csv") 
#completed_Pumpkin_Splitpeas = pd.read_csv("media/Pumpkin_Splitpeas_breastmilk.csv") 
#completed_Pumpkin_Strawberries = pd.read_csv("media/Pumpkin_Strawberries_breastmilk.csv") 
#completed_Pumpkin_Sweetpotato = pd.read_csv("media/Pumpkin_Sweetpotato_breastmilk.csv") 
#completed_Raspberries_Shrimp = pd.read_csv("media/Raspberries_Shrimp_breastmilk.csv") 
#completed_Raspberries_Soybean = pd.read_csv("media/Raspberries_Soybean_breastmilk.csv")
#completed_Raspberries_Splitpeas = pd.read_csv("media/Raspberries_Splitpeas_breastmilk.csv") 
#completed_Raspberries_Strawberries = pd.read_csv("media/Raspberries_Strawberries_breastmilk.csv") 
#completed_Raspberries_Sweetpotato = pd.read_csv("media/Raspberries_Sweetpotato_breastmilk.csv") 
#completed_Shrimp_Soybean = pd.read_csv("media/Shrimp_Soybean_breastmilk.csv") 
#completed_Shrimp_Splitpeas = pd.read_csv("media/Shrimp_Splitpeas_breastmilk.csv") 
#completed_Shrimp_Strawberries = pd.read_csv("media/Shrimp_Strawberries_breastmilk.csv") 
#completed_Shrimp_Sweetpotato = pd.read_csv("media/Shrimp_Sweetpotato_breastmilk.csv") 
#completed_Soybean_Splitpeas = pd.read_csv("media/Soybean_Splitpeas_breastmilk.csv") 
#completed_Soybean_Strawberries = pd.read_csv("media/Soybean_Strawberries_breastmilk.csv") 
#completed_Soybean_Sweetpotato = pd.read_csv("media/Soybean_Sweetpotato_breastmilk.csv") 
#completed_Splitpeas_Strawberries = pd.read_csv("media/Splitpeas_Strawberries_breastmilk.csv") 
#completed_Splitpeas_Sweetpotato = pd.read_csv("media/Splitpeas_Sweetpotato_breastmilk.csv") 
#completed_Strawberries_Sweetpotato = pd.read_csv("media/Strawberries_Sweetpotato_breastmilk.csv") 

#Checking the medium
from micom.workflows.db_media import check_db_medium

check_Blackbeans_Blackcurrant = check_db_medium("data/agora201__species.qza", medium=completed_Blackbeans_Blackcurrant, threads=14)
check_Blackbeans_Chickpea = check_db_medium("data/agora201__species.qza", medium=completed_Blackbeans_Chickpea, threads=14)
check_Blackbeans_Couscous = check_db_medium("data/agora201__species.qza", medium=completed_Blackbeans_Couscous, threads=14)
check_Blackbeans_Pork = check_db_medium("data/agora201__species.qza", medium=completed_Blackbeans_Pork, threads=14)
check_Blackbeans_Pumpkin = check_db_medium("data/agora201__species.qza", medium=completed_Blackbeans_Pumpkin, threads=14)
check_Blackbeans_Raspberries = check_db_medium("data/agora201__species.qza", medium=completed_Blackbeans_Raspberries, threads=14)
check_Blackbeans_Shrimp = check_db_medium("data/agora201__species.qza", medium=completed_Blackbeans_Shrimp, threads=14)
check_Blackbeans_Soybean = check_db_medium("data/agora201__species.qza", medium=completed_Blackbeans_Soybean, threads=14)
check_Blackbeans_Splitpeas = check_db_medium("data/agora201__species.qza", medium=completed_Blackbeans_Splitpeas, threads=14)
check_Blackbeans_Strawberries = check_db_medium("data/agora201__species.qza", medium=completed_Blackbeans_Strawberries, threads=14)
check_Blackbeans_Sweetpotato = check_db_medium("data/agora201__species.qza", medium=completed_Blackbeans_Sweetpotato, threads=14)
check_Blackcurrant_Chickpea = check_db_medium("data/agora201__species.qza", medium=completed_Blackcurrant_Chickpea, threads=14)
check_Blackcurrant_Couscous = check_db_medium("data/agora201__species.qza", medium=completed_Blackcurrant_Couscous, threads=14)
check_Blackcurrant_Pork = check_db_medium("data/agora201__species.qza", medium=completed_Blackcurrant_Pork, threads=14)
check_Blackcurrant_Pumpkin = check_db_medium("data/agora201__species.qza", medium=completed_Blackcurrant_Pumpkin, threads=14)
check_Blackcurrant_Raspberries = check_db_medium("data/agora201__species.qza", medium=completed_Blackcurrant_Raspberries, threads=14)
check_Blackcurrant_Shrimp = check_db_medium("data/agora201__species.qza", medium=completed_Blackcurrant_Shrimp, threads=14)
check_Blackcurrant_Soybean = check_db_medium("data/agora201__species.qza", medium=completed_Blackcurrant_Soybean, threads=14)
check_Blackcurrant_Splitpeas = check_db_medium("data/agora201__species.qza", medium=completed_Blackcurrant_Splitpeas, threads=14)
check_Blackcurrant_Strawberries = check_db_medium("data/agora201__species.qza", medium=completed_Blackcurrant_Strawberries, threads=14)
check_Blackcurrant_Sweetpotato = check_db_medium("data/agora201__species.qza", medium=completed_Blackcurrant_Sweetpotato, threads=14)
check_Chickpea_Couscous = check_db_medium("data/agora201__species.qza", medium=completed_Chickpea_Couscous, threads=14)
check_Chickpea_Pork = check_db_medium("data/agora201__species.qza", medium=completed_Chickpea_Pork, threads=14)
check_Chickpea_Pumpkin = check_db_medium("data/agora201__species.qza", medium=completed_Chickpea_Pumpkin, threads=14)
check_Chickpea_Raspberries = check_db_medium("data/agora201__species.qza", medium=completed_Chickpea_Raspberries, threads=14)
check_Chickpea_Shrimp = check_db_medium("data/agora201__species.qza", medium=completed_Chickpea_Shrimp, threads=14)
check_Chickpea_Soybean = check_db_medium("data/agora201__species.qza", medium=completed_Chickpea_Soybean, threads=14)
check_Chickpea_Splitpeas = check_db_medium("data/agora201__species.qza", medium=completed_Chickpea_Splitpeas, threads=14)
check_Chickpea_Strawberries = check_db_medium("data/agora201__species.qza", medium=completed_Chickpea_Strawberries, threads=14)
check_Chickpea_Sweetpotato = check_db_medium("data/agora201__species.qza", medium=completed_Chickpea_Sweetpotato, threads=14)
check_Couscous_Pork = check_db_medium("data/agora201__species.qza", medium=completed_Couscous_Pork, threads=14)
check_Couscous_Pumpkin = check_db_medium("data/agora201__species.qza", medium=completed_Couscous_Pumpkin, threads=14)
check_Couscous_Raspberries = check_db_medium("data/agora201__species.qza", medium=completed_Couscous_Raspberries, threads=14)
check_Couscous_Shrimp = check_db_medium("data/agora201__species.qza", medium=completed_Couscous_Shrimp, threads=14)
check_Couscous_Soybean = check_db_medium("data/agora201__species.qza", medium=completed_Couscous_Soybean, threads=14)
check_Couscous_Splitpeas = check_db_medium("data/agora201__species.qza", medium=completed_Couscous_Splitpeas, threads=14)
check_Couscous_Strawberries = check_db_medium("data/agora201__species.qza", medium=completed_Couscous_Strawberries, threads=14)
check_Couscous_Sweetpotato = check_db_medium("data/agora201__species.qza", medium=completed_Couscous_Sweetpotato, threads=14)
check_Pork_Pumpkin = check_db_medium("data/agora201__species.qza", medium=completed_Pork_Pumpkin, threads=14)
check_Pork_Raspberries = check_db_medium("data/agora201__species.qza", medium=completed_Pork_Raspberries, threads=14)
check_Pork_Shrimp = check_db_medium("data/agora201__species.qza", medium=completed_Pork_Shrimp, threads=14)
check_Pork_Soybean = check_db_medium("data/agora201__species.qza", medium=completed_Pork_Soybean, threads=14)
check_Pork_Splitpeas = check_db_medium("data/agora201__species.qza", medium=completed_Pork_Splitpeas, threads=14)
check_Pork_Strawberries = check_db_medium("data/agora201__species.qza", medium=completed_Pork_Strawberries, threads=14)
check_Pork_Sweetpotato = check_db_medium("data/agora201__species.qza", medium=completed_Pork_Sweetpotato, threads=14)
check_Pumpkin_Raspberries = check_db_medium("data/agora201__species.qza", medium=completed_Pumpkin_Raspberries, threads=14)
check_Pumpkin_Shrimp = check_db_medium("data/agora201__species.qza", medium=completed_Pumpkin_Shrimp, threads=14)
check_Pumpkin_Soybean = check_db_medium("data/agora201__species.qza", medium=completed_Pumpkin_Soybean, threads=14)
check_Pumpkin_Splitpeas = check_db_medium("data/agora201__species.qza", medium=completed_Pumpkin_Splitpeas, threads=14)
check_Pumpkin_Strawberries = check_db_medium("data/agora201__species.qza", medium=completed_Pumpkin_Strawberries, threads=14)
check_Pumpkin_Sweetpotato = check_db_medium("data/agora201__species.qza", medium=completed_Pumpkin_Sweetpotato, threads=14)
check_Raspberries_Shrimp = check_db_medium("data/agora201__species.qza", medium=completed_Raspberries_Shrimp, threads=14)
check_Raspberries_Soybean = check_db_medium("data/agora201__species.qza", medium=completed_Raspberries_Soybean, threads=14)
check_Raspberries_Splitpeas = check_db_medium("data/agora201__species.qza", medium=completed_Raspberries_Splitpeas, threads=14)
check_Raspberries_Strawberries = check_db_medium("data/agora201__species.qza", medium=completed_Raspberries_Strawberries, threads=14)
check_Raspberries_Sweetpotato = check_db_medium("data/agora201__species.qza", medium=completed_Raspberries_Sweetpotato, threads=14)
check_Shrimp_Soybean = check_db_medium("data/agora201__species.qza", medium=completed_Shrimp_Soybean, threads=14)
check_Shrimp_Splitpeas = check_db_medium("data/agora201__species.qza", medium=completed_Shrimp_Splitpeas, threads=14)
check_Shrimp_Strawberries = check_db_medium("data/agora201__species.qza", medium=completed_Shrimp_Strawberries, threads=14)
check_Shrimp_Sweetpotato = check_db_medium("data/agora201__species.qza", medium=completed_Shrimp_Sweetpotato, threads=14)
check_Soybean_Splitpeas = check_db_medium("data/agora201__species.qza", medium=completed_Soybean_Splitpeas, threads=14)
check_Soybean_Strawberries = check_db_medium("data/agora201__species.qza", medium=completed_Soybean_Strawberries, threads=14)
check_Soybean_Sweetpotato = check_db_medium("data/agora201__species.qza", medium=completed_Soybean_Sweetpotato, threads=14)
check_Splitpeas_Strawberries = check_db_medium("data/agora201__species.qza", medium=completed_Splitpeas_Strawberries, threads=14)
check_Splitpeas_Sweetpotato = check_db_medium("data/agora201__species.qza", medium=completed_Splitpeas_Sweetpotato, threads=14)
check_Strawberries_Sweetpotato = check_db_medium("data/agora201__species.qza", medium=completed_Strawberries_Sweetpotato, threads=14)

check_Blackbeans_Blackcurrant.growth_rate.describe()
check_Blackbeans_Chickpea.growth_rate.describe()
check_Blackbeans_Couscous.growth_rate.describe()
check_Blackbeans_Pork.growth_rate.describe()
check_Blackbeans_Pumpkin.growth_rate.describe()
check_Blackbeans_Raspberries.growth_rate.describe()
check_Blackbeans_Shrimp.growth_rate.describe()
check_Blackbeans_Soybean.growth_rate.describe()
check_Blackbeans_Splitpeas.growth_rate.describe()
check_Blackbeans_Strawberries.growth_rate.describe()
check_Blackbeans_Sweetpotato.growth_rate.describe()
check_Blackcurrant_Chickpea.growth_rate.describe()
check_Blackcurrant_Couscous.growth_rate.describe()
check_Blackcurrant_Pork.growth_rate.describe()
check_Blackcurrant_Pumpkin.growth_rate.describe()
check_Blackcurrant_Raspberries.growth_rate.describe()
check_Blackcurrant_Shrimp.growth_rate.describe()
check_Blackcurrant_Soybean.growth_rate.describe()
check_Blackcurrant_Splitpeas.growth_rate.describe()
check_Blackcurrant_Strawberries.growth_rate.describe()
check_Blackcurrant_Sweetpotato.growth_rate.describe()
check_Chickpea_Couscous.growth_rate.describe()
check_Chickpea_Pork.growth_rate.describe()
check_Chickpea_Pumpkin.growth_rate.describe()
check_Chickpea_Raspberries.growth_rate.describe()
check_Chickpea_Shrimp.growth_rate.describe()
check_Chickpea_Soybean.growth_rate.describe()
check_Chickpea_Splitpeas.growth_rate.describe()
check_Chickpea_Strawberries.growth_rate.describe()
check_Chickpea_Sweetpotato.growth_rate.describe()
check_Couscous_Pork.growth_rate.describe()
check_Couscous_Pumpkin.growth_rate.describe()
check_Couscous_Raspberries.growth_rate.describe()
check_Couscous_Shrimp.growth_rate.describe()
check_Couscous_Soybean.growth_rate.describe()
check_Couscous_Splitpeas.growth_rate.describe()
check_Couscous_Strawberries.growth_rate.describe()
check_Couscous_Sweetpotato.growth_rate.describe()
check_Pork_Pumpkin.growth_rate.describe()
check_Pork_Raspberries.growth_rate.describe()
check_Pork_Shrimp.growth_rate.describe()
check_Pork_Soybean.growth_rate.describe()
check_Pork_Splitpeas.growth_rate.describe()
check_Pork_Strawberries.growth_rate.describe()
check_Pork_Sweetpotato.growth_rate.describe()
check_Pumpkin_Raspberries.growth_rate.describe()
check_Pumpkin_Shrimp.growth_rate.describe()
check_Pumpkin_Soybean.growth_rate.describe()
check_Pumpkin_Splitpeas.growth_rate.describe()
check_Pumpkin_Strawberries.growth_rate.describe()
check_Pumpkin_Sweetpotato.growth_rate.describe()
check_Raspberries_Shrimp.growth_rate.describe()
check_Raspberries_Soybean.growth_rate.describe()
check_Raspberries_Splitpeas.growth_rate.describe()
check_Raspberries_Strawberries.growth_rate.describe()
check_Raspberries_Sweetpotato.growth_rate.describe()
check_Shrimp_Soybean.growth_rate.describe()
check_Shrimp_Splitpeas.growth_rate.describe()
check_Shrimp_Strawberries.growth_rate.describe()
check_Shrimp_Sweetpotato.growth_rate.describe()
check_Soybean_Splitpeas.growth_rate.describe()
check_Soybean_Strawberries.growth_rate.describe()
check_Soybean_Sweetpotato.growth_rate.describe()
check_Splitpeas_Strawberries.growth_rate.describe()
check_Splitpeas_Sweetpotato.growth_rate.describe()
check_Strawberries_Sweetpotato.growth_rate.describe()

