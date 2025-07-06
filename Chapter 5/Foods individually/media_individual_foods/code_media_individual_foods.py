##Diets for NZ infants (6-12 months old)

#6 months = 100% food (608 kcal/d)
#AGORA2

#27/07/23

#Importing the dietary fluxes and converting then
import pandas as pd

diet_Broccoli = pd.read_csv("data/Broccoli.tsv", sep="\t", header=None) #importing fluxes
diet_Broccoli.columns = ["reaction", "flux"] #changing the name of the columns
diet_Brussel = pd.read_csv("data/Brussel.tsv", sep="\t", header=None) #importing fluxes
diet_Brussel.columns = ["reaction", "flux"] #changing the name of the columns
diet_Cabbage = pd.read_csv("data/Cabbage.tsv", sep="\t", header=None) #importing fluxes
diet_Cabbage.columns = ["reaction", "flux"] #changing the name of the columns
diet_Carrot = pd.read_csv("data/Carrot.tsv", sep="\t", header=None) #importing fluxes
diet_Carrot.columns = ["reaction", "flux"] #changing the name of the columns
diet_Cauliflower = pd.read_csv("data/Cauliflower.tsv", sep="\t", header=None) #importing fluxes
diet_Cauliflower.columns = ["reaction", "flux"] #changing the name of the columns
diet_Celery = pd.read_csv("data/Celery.tsv", sep="\t", header=None) #importing fluxes
diet_Celery.columns = ["reaction", "flux"] #changing the name of the columns
diet_Cucumber = pd.read_csv("data/Cucumber.tsv", sep="\t", header=None) #importing fluxes
diet_Cucumber.columns = ["reaction", "flux"] #changing the name of the columns
diet_Eggplant = pd.read_csv("data/Eggplant.tsv", sep="\t", header=None) #importing fluxes
diet_Eggplant.columns = ["reaction", "flux"] #changing the name of the columns
diet_Green_beans = pd.read_csv("data/Green_beans.tsv", sep="\t", header=None) #importing fluxes
diet_Green_beans.columns = ["reaction", "flux"] #changing the name of the columns
diet_Green_capsicum = pd.read_csv("data/Green_capsicum.tsv", sep="\t", header=None) #importing fluxes
diet_Green_capsicum.columns = ["reaction", "flux"] #changing the name of the columns
diet_Lettuce = pd.read_csv("data/Lettuce.tsv", sep="\t", header=None) #importing fluxes
diet_Lettuce.columns = ["reaction", "flux"] #changing the name of the columns
diet_Mushroom = pd.read_csv("data/Mushroom.tsv", sep="\t", header=None) #importing fluxes
diet_Mushroom.columns = ["reaction", "flux"] #changing the name of the columns
diet_Onion = pd.read_csv("data/Onion.tsv", sep="\t", header=None) #importing fluxes
diet_Onion.columns = ["reaction", "flux"] #changing the name of the columns
diet_Pak_choi = pd.read_csv("data/Pak_choi.tsv", sep="\t", header=None) #importing fluxes
diet_Pak_choi.columns = ["reaction", "flux"] #changing the name of the columns
diet_Potato = pd.read_csv("data/Potato.tsv", sep="\t", header=None) #importing fluxes
diet_Potato.columns = ["reaction", "flux"] #changing the name of the columns
diet_Pumpkin = pd.read_csv("data/Pumpkin.tsv", sep="\t", header=None) #importing fluxes
diet_Pumpkin.columns = ["reaction", "flux"] #changing the name of the columns
diet_Sweetcorn = pd.read_csv("data/Sweetcorn.tsv", sep="\t", header=None) #importing fluxes
diet_Sweetcorn.columns = ["reaction", "flux"] #changing the name of the columns
diet_Spinach = pd.read_csv("data/Spinach.tsv", sep="\t", header=None) #importing fluxes
diet_Spinach.columns = ["reaction", "flux"] #changing the name of the columns
diet_Squash = pd.read_csv("data/Squash.tsv", sep="\t", header=None) #importing fluxes
diet_Squash.columns = ["reaction", "flux"] #changing the name of the columns
diet_Sweet_potato = pd.read_csv("data/Sweet_potato.tsv", sep="\t", header=None) #importing fluxes
diet_Sweet_potato.columns = ["reaction", "flux"] #changing the name of the columns
diet_Tomato = pd.read_csv("data/Tomato.tsv", sep="\t", header=None) #importing fluxes
diet_Tomato.columns = ["reaction", "flux"] #changing the name of the columns
diet_Yam = pd.read_csv("data/Yam.tsv", sep="\t", header=None) #importing fluxes
diet_Yam.columns = ["reaction", "flux"] #changing the name of the columns
diet_Zucchini = pd.read_csv("data/Zucchini.tsv", sep="\t", header=None) #importing fluxes
diet_Zucchini.columns = ["reaction", "flux"] #changing the name of the columns
diet_Apple = pd.read_csv("data/Apple.tsv", sep="\t", header=None) #importing fluxes
diet_Apple.columns = ["reaction", "flux"] #changing the name of the columns
diet_Banana = pd.read_csv("data/Banana.tsv", sep="\t", header=None) #importing fluxes
diet_Banana.columns = ["reaction", "flux"] #changing the name of the columns
diet_Blackcurrant = pd.read_csv("data/Blackcurrant.tsv", sep="\t", header=None) #importing fluxes
diet_Blackcurrant.columns = ["reaction", "flux"] #changing the name of the columns
diet_Blueberries = pd.read_csv("data/Blueberries.tsv", sep="\t", header=None) #importing fluxes
diet_Blueberries.columns = ["reaction", "flux"] #changing the name of the columns
diet_Cherry = pd.read_csv("data/Cherry.tsv", sep="\t", header=None) #importing fluxes
diet_Cherry.columns = ["reaction", "flux"] #changing the name of the columns
diet_Feijoa = pd.read_csv("data/Feijoa.tsv", sep="\t", header=None) #importing fluxes
diet_Feijoa.columns = ["reaction", "flux"] #changing the name of the columns
diet_Gold_kiwifruit = pd.read_csv("data/Gold_kiwifruit.tsv", sep="\t", header=None) #importing fluxes
diet_Gold_kiwifruit.columns = ["reaction", "flux"] #changing the name of the columns
diet_Grape = pd.read_csv("data/Grape.tsv", sep="\t", header=None) #importing fluxes
diet_Grape.columns = ["reaction", "flux"] #changing the name of the columns
diet_Grapefruit = pd.read_csv("data/Grapefruit.tsv", sep="\t", header=None) #importing fluxes
diet_Grapefruit.columns = ["reaction", "flux"] #changing the name of the columns
diet_Green_kiwifruit = pd.read_csv("data/Green_kiwifruit.tsv", sep="\t", header=None) #importing fluxes
diet_Green_kiwifruit.columns = ["reaction", "flux"] #changing the name of the columns
diet_Mandarin = pd.read_csv("data/Mandarin.tsv", sep="\t", header=None) #importing fluxes
diet_Mandarin.columns = ["reaction", "flux"] #changing the name of the columns
diet_Mango = pd.read_csv("data/Mango.tsv", sep="\t", header=None) #importing fluxes
diet_Mango.columns = ["reaction", "flux"] #changing the name of the columns
diet_Melon = pd.read_csv("data/Melon.tsv", sep="\t", header=None) #importing fluxes
diet_Melon.columns = ["reaction", "flux"] #changing the name of the columns
diet_Nectarine = pd.read_csv("data/Nectarine.tsv", sep="\t", header=None) #importing fluxes
diet_Nectarine.columns = ["reaction", "flux"] #changing the name of the columns
diet_Orange = pd.read_csv("data/Orange.tsv", sep="\t", header=None) #importing fluxes
diet_Orange.columns = ["reaction", "flux"] #changing the name of the columns
diet_Peache = pd.read_csv("data/Peache.tsv", sep="\t", header=None) #importing fluxes
diet_Peache.columns = ["reaction", "flux"] #changing the name of the columns
diet_Pear = pd.read_csv("data/Pear.tsv", sep="\t", header=None) #importing fluxes
diet_Pear.columns = ["reaction", "flux"] #changing the name of the columns
diet_Pineapple = pd.read_csv("data/Pineapple.tsv", sep="\t", header=None) #importing fluxes
diet_Pineapple.columns = ["reaction", "flux"] #changing the name of the columns
diet_Plum = pd.read_csv("data/Plum.tsv", sep="\t", header=None) #importing fluxes
diet_Plum.columns = ["reaction", "flux"] #changing the name of the columns
diet_Raspberries = pd.read_csv("data/Raspberries.tsv", sep="\t", header=None) #importing fluxes
diet_Raspberries.columns = ["reaction", "flux"] #changing the name of the columns
diet_Strawberries = pd.read_csv("data/Strawberries.tsv", sep="\t", header=None) #importing fluxes
diet_Strawberries.columns = ["reaction", "flux"] #changing the name of the columns
diet_Barley = pd.read_csv("data/Barley.tsv", sep="\t", header=None) #importing fluxes
diet_Barley.columns = ["reaction", "flux"] #changing the name of the columns
diet_Barley_cereal = pd.read_csv("data/Barley_cereal.tsv", sep="\t", header=None) #importing fluxes
diet_Barley_cereal.columns = ["reaction", "flux"] #changing the name of the columns
diet_Couscous = pd.read_csv("data/Couscous.tsv", sep="\t", header=None) #importing fluxes
diet_Couscous.columns = ["reaction", "flux"] #changing the name of the columns
diet_Noodles = pd.read_csv("data/Noodles.tsv", sep="\t", header=None) #importing fluxes
diet_Noodles.columns = ["reaction", "flux"] #changing the name of the columns
diet_Oat_cereal = pd.read_csv("data/Oat_cereal.tsv", sep="\t", header=None) #importing fluxes
diet_Oat_cereal.columns = ["reaction", "flux"] #changing the name of the columns
diet_Pasta = pd.read_csv("data/Pasta.tsv", sep="\t", header=None) #importing fluxes
diet_Pasta.columns = ["reaction", "flux"] #changing the name of the columns
diet_Rice = pd.read_csv("data/Rice.tsv", sep="\t", header=None) #importing fluxes
diet_Rice.columns = ["reaction", "flux"] #changing the name of the columns
diet_Rice_cereal = pd.read_csv("data/Rice_cereal.tsv", sep="\t", header=None) #importing fluxes
diet_Rice_cereal.columns = ["reaction", "flux"] #changing the name of the columns
diet_Tapioca_pudding = pd.read_csv("data/Tapioca_pudding.tsv", sep="\t", header=None) #importing fluxes
diet_Tapioca_pudding.columns = ["reaction", "flux"] #changing the name of the columns
diet_White_bread = pd.read_csv("data/White_bread.tsv", sep="\t", header=None) #importing fluxes
diet_White_bread.columns = ["reaction", "flux"] #changing the name of the columns
diet_Wholegrain_bread = pd.read_csv("data/Wholegrain_bread.tsv", sep="\t", header=None) #importing fluxes
diet_Wholegrain_bread.columns = ["reaction", "flux"] #changing the name of the columns
diet_Cottage_cheese = pd.read_csv("data/Cottage_cheese.tsv", sep="\t", header=None) #importing fluxes
diet_Cottage_cheese.columns = ["reaction", "flux"] #changing the name of the columns
diet_Eggs = pd.read_csv("data/Eggs.tsv", sep="\t", header=None) #importing fluxes
diet_Eggs.columns = ["reaction", "flux"] #changing the name of the columns
diet_Mozzarella_cheese = pd.read_csv("data/Mozzarella_cheese.tsv", sep="\t", header=None) #importing fluxes
diet_Mozzarella_cheese.columns = ["reaction", "flux"] #changing the name of the columns
diet_Soymilk = pd.read_csv("data/Soymilk.tsv", sep="\t", header=None) #importing fluxes
diet_Soymilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Tofu = pd.read_csv("data/Tofu.tsv", sep="\t", header=None) #importing fluxes
diet_Tofu.columns = ["reaction", "flux"] #changing the name of the columns
diet_Whole_milk = pd.read_csv("data/Whole_milk.tsv", sep="\t", header=None) #importing fluxes
diet_Whole_milk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Yoghurt = pd.read_csv("data/Yoghurt.tsv", sep="\t", header=None) #importing fluxes
diet_Yoghurt.columns = ["reaction", "flux"] #changing the name of the columns
diet_Beef = pd.read_csv("data/Beef.tsv", sep="\t", header=None) #importing fluxes
diet_Beef.columns = ["reaction", "flux"] #changing the name of the columns
diet_Chicken = pd.read_csv("data/Chicken.tsv", sep="\t", header=None) #importing fluxes
diet_Chicken.columns = ["reaction", "flux"] #changing the name of the columns
diet_Codfish = pd.read_csv("data/Codfish.tsv", sep="\t", header=None) #importing fluxes
diet_Codfish.columns = ["reaction", "flux"] #changing the name of the columns
diet_Lamb = pd.read_csv("data/Lamb.tsv", sep="\t", header=None) #importing fluxes
diet_Lamb.columns = ["reaction", "flux"] #changing the name of the columns
diet_Mackerel = pd.read_csv("data/Mackerel.tsv", sep="\t", header=None) #importing fluxes
diet_Mackerel.columns = ["reaction", "flux"] #changing the name of the columns
diet_Mussels = pd.read_csv("data/Mussels.tsv", sep="\t", header=None) #importing fluxes
diet_Mussels.columns = ["reaction", "flux"] #changing the name of the columns
diet_Pork = pd.read_csv("data/Pork.tsv", sep="\t", header=None) #importing fluxes
diet_Pork.columns = ["reaction", "flux"] #changing the name of the columns
diet_Salmon = pd.read_csv("data/Salmon.tsv", sep="\t", header=None) #importing fluxes
diet_Salmon.columns = ["reaction", "flux"] #changing the name of the columns
diet_Shrimp = pd.read_csv("data/Shrimp.tsv", sep="\t", header=None) #importing fluxes
diet_Shrimp.columns = ["reaction", "flux"] #changing the name of the columns
diet_Tuna = pd.read_csv("data/Tuna.tsv", sep="\t", header=None) #importing fluxes
diet_Tuna.columns = ["reaction", "flux"] #changing the name of the columns
diet_Turkey = pd.read_csv("data/Turkey.tsv", sep="\t", header=None) #importing fluxes
diet_Turkey.columns = ["reaction", "flux"] #changing the name of the columns
diet_Almond = pd.read_csv("data/Almond.tsv", sep="\t", header=None) #importing fluxes
diet_Almond.columns = ["reaction", "flux"] #changing the name of the columns
diet_Black_beans = pd.read_csv("data/Black_beans.tsv", sep="\t", header=None) #importing fluxes
diet_Black_beans.columns = ["reaction", "flux"] #changing the name of the columns
diet_Cashew = pd.read_csv("data/Cashew.tsv", sep="\t", header=None) #importing fluxes
diet_Cashew.columns = ["reaction", "flux"] #changing the name of the columns
diet_Chia = pd.read_csv("data/Chia.tsv", sep="\t", header=None) #importing fluxes
diet_Chia.columns = ["reaction", "flux"] #changing the name of the columns
diet_Chickpea = pd.read_csv("data/Chickpea.tsv", sep="\t", header=None) #importing fluxes
diet_Chickpea.columns = ["reaction", "flux"] #changing the name of the columns
diet_Green_peas = pd.read_csv("data/Green_peas.tsv", sep="\t", header=None) #importing fluxes
diet_Green_peas.columns = ["reaction", "flux"] #changing the name of the columns
diet_Hazelnut = pd.read_csv("data/Hazelnut.tsv", sep="\t", header=None) #importing fluxes
diet_Hazelnut.columns = ["reaction", "flux"] #changing the name of the columns
diet_Lentils = pd.read_csv("data/Lentils.tsv", sep="\t", header=None) #importing fluxes
diet_Lentils.columns = ["reaction", "flux"] #changing the name of the columns
diet_Peanut = pd.read_csv("data/Peanut.tsv", sep="\t", header=None) #importing fluxes
diet_Peanut.columns = ["reaction", "flux"] #changing the name of the columns
diet_Pecans = pd.read_csv("data/Pecans.tsv", sep="\t", header=None) #importing fluxes
diet_Pecans.columns = ["reaction", "flux"] #changing the name of the columns
diet_Pumpkin_seed = pd.read_csv("data/Pumpkin_seed.tsv", sep="\t", header=None) #importing fluxes
diet_Pumpkin_seed.columns = ["reaction", "flux"] #changing the name of the columns
diet_Red_beans = pd.read_csv("data/Red_beans.tsv", sep="\t", header=None) #importing fluxes
diet_Red_beans.columns = ["reaction", "flux"] #changing the name of the columns
diet_Soybean = pd.read_csv("data/Soybean.tsv", sep="\t", header=None) #importing fluxes
diet_Soybean.columns = ["reaction", "flux"] #changing the name of the columns
diet_Split_peas = pd.read_csv("data/Split_peas.tsv", sep="\t", header=None) #importing fluxes
diet_Split_peas.columns = ["reaction", "flux"] #changing the name of the columns
diet_Sunflower_seed = pd.read_csv("data/Sunflower_seed.tsv", sep="\t", header=None) #importing fluxes
diet_Sunflower_seed.columns = ["reaction", "flux"] #changing the name of the columns
diet_White_beans = pd.read_csv("data/White_beans.tsv", sep="\t", header=None) #importing fluxes
diet_White_beans.columns = ["reaction", "flux"] #changing the name of the columns
diet_Breastmilk = pd.read_csv("data/Breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Infant_formula = pd.read_csv("data/Infant_formula.tsv", sep="\t", header=None) #importing fluxes
diet_Infant_formula.columns = ["reaction", "flux"] #changing the name of the columns

annotations = pd.read_csv("data/agora_metabolites.csv") #importing a table with the description of agora metabolites
 
diet_Broccoli = diet_Broccoli.rename(columns={diet_Broccoli.columns[0]: "reaction"})
diet_Broccoli["metabolite"] = diet_Broccoli.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Broccoli.loc[diet_Broccoli.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Broccoli.loc[diet_Broccoli.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Brussel = diet_Brussel.rename(columns={diet_Brussel.columns[0]: "reaction"})
diet_Brussel["metabolite"] = diet_Brussel.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Brussel.loc[diet_Brussel.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Brussel.loc[diet_Brussel.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Cabbage = diet_Cabbage.rename(columns={diet_Cabbage.columns[0]: "reaction"})
diet_Cabbage["metabolite"] = diet_Cabbage.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Cabbage.loc[diet_Cabbage.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Cabbage.loc[diet_Cabbage.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Carrot = diet_Carrot.rename(columns={diet_Carrot.columns[0]: "reaction"})
diet_Carrot["metabolite"] = diet_Carrot.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Carrot.loc[diet_Carrot.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Carrot.loc[diet_Carrot.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Cauliflower = diet_Cauliflower.rename(columns={diet_Cauliflower.columns[0]: "reaction"})
diet_Cauliflower["metabolite"] = diet_Cauliflower.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Cauliflower.loc[diet_Cauliflower.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Cauliflower.loc[diet_Cauliflower.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Celery = diet_Celery.rename(columns={diet_Celery.columns[0]: "reaction"})
diet_Celery["metabolite"] = diet_Celery.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Celery.loc[diet_Celery.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Celery.loc[diet_Celery.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Cucumber = diet_Cucumber.rename(columns={diet_Cucumber.columns[0]: "reaction"})
diet_Cucumber["metabolite"] = diet_Cucumber.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Cucumber.loc[diet_Cucumber.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Cucumber.loc[diet_Cucumber.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Eggplant = diet_Eggplant.rename(columns={diet_Eggplant.columns[0]: "reaction"})
diet_Eggplant["metabolite"] = diet_Eggplant.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Eggplant.loc[diet_Eggplant.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Eggplant.loc[diet_Eggplant.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Green_beans = diet_Green_beans.rename(columns={diet_Green_beans.columns[0]: "reaction"})
diet_Green_beans["metabolite"] = diet_Green_beans.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Green_beans.loc[diet_Green_beans.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Green_beans.loc[diet_Green_beans.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Green_capsicum = diet_Green_capsicum.rename(columns={diet_Green_capsicum.columns[0]: "reaction"})
diet_Green_capsicum["metabolite"] = diet_Green_capsicum.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Green_capsicum.loc[diet_Green_capsicum.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Green_capsicum.loc[diet_Green_capsicum.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Lettuce = diet_Lettuce.rename(columns={diet_Lettuce.columns[0]: "reaction"})
diet_Lettuce["metabolite"] = diet_Lettuce.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Lettuce.loc[diet_Lettuce.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Lettuce.loc[diet_Lettuce.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Mushroom = diet_Mushroom.rename(columns={diet_Mushroom.columns[0]: "reaction"})
diet_Mushroom["metabolite"] = diet_Mushroom.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Mushroom.loc[diet_Mushroom.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Mushroom.loc[diet_Mushroom.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Onion = diet_Onion.rename(columns={diet_Onion.columns[0]: "reaction"})
diet_Onion["metabolite"] = diet_Onion.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Onion.loc[diet_Onion.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Onion.loc[diet_Onion.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Pak_choi = diet_Pak_choi.rename(columns={diet_Pak_choi.columns[0]: "reaction"})
diet_Pak_choi["metabolite"] = diet_Pak_choi.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Pak_choi.loc[diet_Pak_choi.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Pak_choi.loc[diet_Pak_choi.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Potato = diet_Potato.rename(columns={diet_Potato.columns[0]: "reaction"})
diet_Potato["metabolite"] = diet_Potato.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Potato.loc[diet_Potato.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Potato.loc[diet_Potato.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Pumpkin = diet_Pumpkin.rename(columns={diet_Pumpkin.columns[0]: "reaction"})
diet_Pumpkin["metabolite"] = diet_Pumpkin.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Pumpkin.loc[diet_Pumpkin.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Pumpkin.loc[diet_Pumpkin.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Sweetcorn = diet_Sweetcorn.rename(columns={diet_Sweetcorn.columns[0]: "reaction"})
diet_Sweetcorn["metabolite"] = diet_Sweetcorn.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Sweetcorn.loc[diet_Sweetcorn.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Sweetcorn.loc[diet_Sweetcorn.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Spinach = diet_Spinach.rename(columns={diet_Spinach.columns[0]: "reaction"})
diet_Spinach["metabolite"] = diet_Spinach.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Spinach.loc[diet_Spinach.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Spinach.loc[diet_Spinach.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Squash = diet_Squash.rename(columns={diet_Squash.columns[0]: "reaction"})
diet_Squash["metabolite"] = diet_Squash.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Squash.loc[diet_Squash.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Squash.loc[diet_Squash.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Sweet_potato = diet_Sweet_potato.rename(columns={diet_Sweet_potato.columns[0]: "reaction"})
diet_Sweet_potato["metabolite"] = diet_Sweet_potato.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Sweet_potato.loc[diet_Sweet_potato.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Sweet_potato.loc[diet_Sweet_potato.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Tomato = diet_Tomato.rename(columns={diet_Tomato.columns[0]: "reaction"})
diet_Tomato["metabolite"] = diet_Tomato.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Tomato.loc[diet_Tomato.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Tomato.loc[diet_Tomato.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Yam = diet_Yam.rename(columns={diet_Yam.columns[0]: "reaction"})
diet_Yam["metabolite"] = diet_Yam.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Yam.loc[diet_Yam.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Yam.loc[diet_Yam.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Zucchini = diet_Zucchini.rename(columns={diet_Zucchini.columns[0]: "reaction"})
diet_Zucchini["metabolite"] = diet_Zucchini.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Zucchini.loc[diet_Zucchini.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Zucchini.loc[diet_Zucchini.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Apple = diet_Apple.rename(columns={diet_Apple.columns[0]: "reaction"})
diet_Apple["metabolite"] = diet_Apple.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Apple.loc[diet_Apple.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Apple.loc[diet_Apple.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Banana = diet_Banana.rename(columns={diet_Banana.columns[0]: "reaction"})
diet_Banana["metabolite"] = diet_Banana.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Banana.loc[diet_Banana.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Banana.loc[diet_Banana.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Blackcurrant = diet_Blackcurrant.rename(columns={diet_Blackcurrant.columns[0]: "reaction"})
diet_Blackcurrant["metabolite"] = diet_Blackcurrant.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Blackcurrant.loc[diet_Blackcurrant.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Blackcurrant.loc[diet_Blackcurrant.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Blueberries = diet_Blueberries.rename(columns={diet_Blueberries.columns[0]: "reaction"})
diet_Blueberries["metabolite"] = diet_Blueberries.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Blueberries.loc[diet_Blueberries.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Blueberries.loc[diet_Blueberries.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Cherry = diet_Cherry.rename(columns={diet_Cherry.columns[0]: "reaction"})
diet_Cherry["metabolite"] = diet_Cherry.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Cherry.loc[diet_Cherry.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Cherry.loc[diet_Cherry.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Feijoa = diet_Feijoa.rename(columns={diet_Feijoa.columns[0]: "reaction"})
diet_Feijoa["metabolite"] = diet_Feijoa.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Feijoa.loc[diet_Feijoa.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Feijoa.loc[diet_Feijoa.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Gold_kiwifruit = diet_Gold_kiwifruit.rename(columns={diet_Gold_kiwifruit.columns[0]: "reaction"})
diet_Gold_kiwifruit["metabolite"] = diet_Gold_kiwifruit.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Gold_kiwifruit.loc[diet_Gold_kiwifruit.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Gold_kiwifruit.loc[diet_Gold_kiwifruit.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Grape = diet_Grape.rename(columns={diet_Grape.columns[0]: "reaction"})
diet_Grape["metabolite"] = diet_Grape.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Grape.loc[diet_Grape.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Grape.loc[diet_Grape.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Grapefruit = diet_Grapefruit.rename(columns={diet_Grapefruit.columns[0]: "reaction"})
diet_Grapefruit["metabolite"] = diet_Grapefruit.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Grapefruit.loc[diet_Grapefruit.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Grapefruit.loc[diet_Grapefruit.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Green_kiwifruit = diet_Green_kiwifruit.rename(columns={diet_Green_kiwifruit.columns[0]: "reaction"})
diet_Green_kiwifruit["metabolite"] = diet_Green_kiwifruit.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Green_kiwifruit.loc[diet_Green_kiwifruit.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Green_kiwifruit.loc[diet_Green_kiwifruit.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Mandarin = diet_Mandarin.rename(columns={diet_Mandarin.columns[0]: "reaction"})
diet_Mandarin["metabolite"] = diet_Mandarin.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Mandarin.loc[diet_Mandarin.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Mandarin.loc[diet_Mandarin.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Mango = diet_Mango.rename(columns={diet_Mango.columns[0]: "reaction"})
diet_Mango["metabolite"] = diet_Mango.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Mango.loc[diet_Mango.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Mango.loc[diet_Mango.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Melon = diet_Melon.rename(columns={diet_Melon.columns[0]: "reaction"})
diet_Melon["metabolite"] = diet_Melon.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Melon.loc[diet_Melon.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Melon.loc[diet_Melon.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Nectarine = diet_Nectarine.rename(columns={diet_Nectarine.columns[0]: "reaction"})
diet_Nectarine["metabolite"] = diet_Nectarine.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Nectarine.loc[diet_Nectarine.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Nectarine.loc[diet_Nectarine.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Orange = diet_Orange.rename(columns={diet_Orange.columns[0]: "reaction"})
diet_Orange["metabolite"] = diet_Orange.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Orange.loc[diet_Orange.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Orange.loc[diet_Orange.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Peache = diet_Peache.rename(columns={diet_Peache.columns[0]: "reaction"})
diet_Peache["metabolite"] = diet_Peache.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Peache.loc[diet_Peache.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Peache.loc[diet_Peache.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Pear = diet_Pear.rename(columns={diet_Pear.columns[0]: "reaction"})
diet_Pear["metabolite"] = diet_Pear.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Pear.loc[diet_Pear.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Pear.loc[diet_Pear.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Pineapple = diet_Pineapple.rename(columns={diet_Pineapple.columns[0]: "reaction"})
diet_Pineapple["metabolite"] = diet_Pineapple.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Pineapple.loc[diet_Pineapple.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Pineapple.loc[diet_Pineapple.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Plum = diet_Plum.rename(columns={diet_Plum.columns[0]: "reaction"})
diet_Plum["metabolite"] = diet_Plum.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Plum.loc[diet_Plum.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Plum.loc[diet_Plum.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Raspberries = diet_Raspberries.rename(columns={diet_Raspberries.columns[0]: "reaction"})
diet_Raspberries["metabolite"] = diet_Raspberries.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Raspberries.loc[diet_Raspberries.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Raspberries.loc[diet_Raspberries.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Strawberries = diet_Strawberries.rename(columns={diet_Strawberries.columns[0]: "reaction"})
diet_Strawberries["metabolite"] = diet_Strawberries.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Strawberries.loc[diet_Strawberries.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Strawberries.loc[diet_Strawberries.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Barley = diet_Barley.rename(columns={diet_Barley.columns[0]: "reaction"})
diet_Barley["metabolite"] = diet_Barley.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Barley.loc[diet_Barley.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Barley.loc[diet_Barley.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Barley_cereal = diet_Barley_cereal.rename(columns={diet_Barley_cereal.columns[0]: "reaction"})
diet_Barley_cereal["metabolite"] = diet_Barley_cereal.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Barley_cereal.loc[diet_Barley_cereal.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Barley_cereal.loc[diet_Barley_cereal.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Couscous = diet_Couscous.rename(columns={diet_Couscous.columns[0]: "reaction"})
diet_Couscous["metabolite"] = diet_Couscous.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Couscous.loc[diet_Couscous.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Couscous.loc[diet_Couscous.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Noodles = diet_Noodles.rename(columns={diet_Noodles.columns[0]: "reaction"})
diet_Noodles["metabolite"] = diet_Noodles.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Noodles.loc[diet_Noodles.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Noodles.loc[diet_Noodles.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Oat_cereal = diet_Oat_cereal.rename(columns={diet_Oat_cereal.columns[0]: "reaction"})
diet_Oat_cereal["metabolite"] = diet_Oat_cereal.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Oat_cereal.loc[diet_Oat_cereal.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Oat_cereal.loc[diet_Oat_cereal.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Pasta = diet_Pasta.rename(columns={diet_Pasta.columns[0]: "reaction"})
diet_Pasta["metabolite"] = diet_Pasta.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Pasta.loc[diet_Pasta.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Pasta.loc[diet_Pasta.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Rice = diet_Rice.rename(columns={diet_Rice.columns[0]: "reaction"})
diet_Rice["metabolite"] = diet_Rice.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Rice.loc[diet_Rice.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Rice.loc[diet_Rice.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Rice_cereal = diet_Rice_cereal.rename(columns={diet_Rice_cereal.columns[0]: "reaction"})
diet_Rice_cereal["metabolite"] = diet_Rice_cereal.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Rice_cereal.loc[diet_Rice_cereal.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Rice_cereal.loc[diet_Rice_cereal.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Tapioca_pudding = diet_Tapioca_pudding.rename(columns={diet_Tapioca_pudding.columns[0]: "reaction"})
diet_Tapioca_pudding["metabolite"] = diet_Tapioca_pudding.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Tapioca_pudding.loc[diet_Tapioca_pudding.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Tapioca_pudding.loc[diet_Tapioca_pudding.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_White_bread = diet_White_bread.rename(columns={diet_White_bread.columns[0]: "reaction"})
diet_White_bread["metabolite"] = diet_White_bread.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_White_bread.loc[diet_White_bread.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_White_bread.loc[diet_White_bread.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Wholegrain_bread = diet_Wholegrain_bread.rename(columns={diet_Wholegrain_bread.columns[0]: "reaction"})
diet_Wholegrain_bread["metabolite"] = diet_Wholegrain_bread.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Wholegrain_bread.loc[diet_Wholegrain_bread.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Wholegrain_bread.loc[diet_Wholegrain_bread.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Cottage_cheese = diet_Cottage_cheese.rename(columns={diet_Cottage_cheese.columns[0]: "reaction"})
diet_Cottage_cheese["metabolite"] = diet_Cottage_cheese.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Cottage_cheese.loc[diet_Cottage_cheese.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Cottage_cheese.loc[diet_Cottage_cheese.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Eggs = diet_Eggs.rename(columns={diet_Eggs.columns[0]: "reaction"})
diet_Eggs["metabolite"] = diet_Eggs.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Eggs.loc[diet_Eggs.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Eggs.loc[diet_Eggs.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Mozzarella_cheese = diet_Mozzarella_cheese.rename(columns={diet_Mozzarella_cheese.columns[0]: "reaction"})
diet_Mozzarella_cheese["metabolite"] = diet_Mozzarella_cheese.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Mozzarella_cheese.loc[diet_Mozzarella_cheese.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Mozzarella_cheese.loc[diet_Mozzarella_cheese.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Soymilk = diet_Soymilk.rename(columns={diet_Soymilk.columns[0]: "reaction"})
diet_Soymilk["metabolite"] = diet_Soymilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Soymilk.loc[diet_Soymilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Soymilk.loc[diet_Soymilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Tofu = diet_Tofu.rename(columns={diet_Tofu.columns[0]: "reaction"})
diet_Tofu["metabolite"] = diet_Tofu.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Tofu.loc[diet_Tofu.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Tofu.loc[diet_Tofu.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Whole_milk = diet_Whole_milk.rename(columns={diet_Whole_milk.columns[0]: "reaction"})
diet_Whole_milk["metabolite"] = diet_Whole_milk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Whole_milk.loc[diet_Whole_milk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Whole_milk.loc[diet_Whole_milk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Yoghurt = diet_Yoghurt.rename(columns={diet_Yoghurt.columns[0]: "reaction"})
diet_Yoghurt["metabolite"] = diet_Yoghurt.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Yoghurt.loc[diet_Yoghurt.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Yoghurt.loc[diet_Yoghurt.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Beef = diet_Beef.rename(columns={diet_Beef.columns[0]: "reaction"})
diet_Beef["metabolite"] = diet_Beef.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Beef.loc[diet_Beef.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Beef.loc[diet_Beef.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Chicken = diet_Chicken.rename(columns={diet_Chicken.columns[0]: "reaction"})
diet_Chicken["metabolite"] = diet_Chicken.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Chicken.loc[diet_Chicken.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Chicken.loc[diet_Chicken.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Codfish = diet_Codfish.rename(columns={diet_Codfish.columns[0]: "reaction"})
diet_Codfish["metabolite"] = diet_Codfish.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Codfish.loc[diet_Codfish.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Codfish.loc[diet_Codfish.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Lamb = diet_Lamb.rename(columns={diet_Lamb.columns[0]: "reaction"})
diet_Lamb["metabolite"] = diet_Lamb.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Lamb.loc[diet_Lamb.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Lamb.loc[diet_Lamb.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Mackerel = diet_Mackerel.rename(columns={diet_Mackerel.columns[0]: "reaction"})
diet_Mackerel["metabolite"] = diet_Mackerel.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Mackerel.loc[diet_Mackerel.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Mackerel.loc[diet_Mackerel.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Mussels = diet_Mussels.rename(columns={diet_Mussels.columns[0]: "reaction"})
diet_Mussels["metabolite"] = diet_Mussels.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Mussels.loc[diet_Mussels.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Mussels.loc[diet_Mussels.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Pork = diet_Pork.rename(columns={diet_Pork.columns[0]: "reaction"})
diet_Pork["metabolite"] = diet_Pork.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Pork.loc[diet_Pork.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Pork.loc[diet_Pork.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Salmon = diet_Salmon.rename(columns={diet_Salmon.columns[0]: "reaction"})
diet_Salmon["metabolite"] = diet_Salmon.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Salmon.loc[diet_Salmon.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Salmon.loc[diet_Salmon.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Shrimp = diet_Shrimp.rename(columns={diet_Shrimp.columns[0]: "reaction"})
diet_Shrimp["metabolite"] = diet_Shrimp.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Shrimp.loc[diet_Shrimp.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Shrimp.loc[diet_Shrimp.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Tuna = diet_Tuna.rename(columns={diet_Tuna.columns[0]: "reaction"})
diet_Tuna["metabolite"] = diet_Tuna.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Tuna.loc[diet_Tuna.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Tuna.loc[diet_Tuna.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Turkey = diet_Turkey.rename(columns={diet_Turkey.columns[0]: "reaction"})
diet_Turkey["metabolite"] = diet_Turkey.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Turkey.loc[diet_Turkey.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Turkey.loc[diet_Turkey.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Almond = diet_Almond.rename(columns={diet_Almond.columns[0]: "reaction"})
diet_Almond["metabolite"] = diet_Almond.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Almond.loc[diet_Almond.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Almond.loc[diet_Almond.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Black_beans = diet_Black_beans.rename(columns={diet_Black_beans.columns[0]: "reaction"})
diet_Black_beans["metabolite"] = diet_Black_beans.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Black_beans.loc[diet_Black_beans.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Black_beans.loc[diet_Black_beans.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Cashew = diet_Cashew.rename(columns={diet_Cashew.columns[0]: "reaction"})
diet_Cashew["metabolite"] = diet_Cashew.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Cashew.loc[diet_Cashew.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Cashew.loc[diet_Cashew.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Chia = diet_Chia.rename(columns={diet_Chia.columns[0]: "reaction"})
diet_Chia["metabolite"] = diet_Chia.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Chia.loc[diet_Chia.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Chia.loc[diet_Chia.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Chickpea = diet_Chickpea.rename(columns={diet_Chickpea.columns[0]: "reaction"})
diet_Chickpea["metabolite"] = diet_Chickpea.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Chickpea.loc[diet_Chickpea.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Chickpea.loc[diet_Chickpea.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Green_peas = diet_Green_peas.rename(columns={diet_Green_peas.columns[0]: "reaction"})
diet_Green_peas["metabolite"] = diet_Green_peas.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Green_peas.loc[diet_Green_peas.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Green_peas.loc[diet_Green_peas.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Hazelnut = diet_Hazelnut.rename(columns={diet_Hazelnut.columns[0]: "reaction"})
diet_Hazelnut["metabolite"] = diet_Hazelnut.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Hazelnut.loc[diet_Hazelnut.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Hazelnut.loc[diet_Hazelnut.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Lentils = diet_Lentils.rename(columns={diet_Lentils.columns[0]: "reaction"})
diet_Lentils["metabolite"] = diet_Lentils.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Lentils.loc[diet_Lentils.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Lentils.loc[diet_Lentils.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Peanut = diet_Peanut.rename(columns={diet_Peanut.columns[0]: "reaction"})
diet_Peanut["metabolite"] = diet_Peanut.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Peanut.loc[diet_Peanut.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Peanut.loc[diet_Peanut.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Pecans = diet_Pecans.rename(columns={diet_Pecans.columns[0]: "reaction"})
diet_Pecans["metabolite"] = diet_Pecans.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Pecans.loc[diet_Pecans.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Pecans.loc[diet_Pecans.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Pumpkin_seed = diet_Pumpkin_seed.rename(columns={diet_Pumpkin_seed.columns[0]: "reaction"})
diet_Pumpkin_seed["metabolite"] = diet_Pumpkin_seed.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Pumpkin_seed.loc[diet_Pumpkin_seed.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Pumpkin_seed.loc[diet_Pumpkin_seed.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Red_beans = diet_Red_beans.rename(columns={diet_Red_beans.columns[0]: "reaction"})
diet_Red_beans["metabolite"] = diet_Red_beans.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Red_beans.loc[diet_Red_beans.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Red_beans.loc[diet_Red_beans.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Soybean = diet_Soybean.rename(columns={diet_Soybean.columns[0]: "reaction"})
diet_Soybean["metabolite"] = diet_Soybean.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Soybean.loc[diet_Soybean.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Soybean.loc[diet_Soybean.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Split_peas = diet_Split_peas.rename(columns={diet_Split_peas.columns[0]: "reaction"})
diet_Split_peas["metabolite"] = diet_Split_peas.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Split_peas.loc[diet_Split_peas.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Split_peas.loc[diet_Split_peas.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Sunflower_seed = diet_Sunflower_seed.rename(columns={diet_Sunflower_seed.columns[0]: "reaction"})
diet_Sunflower_seed["metabolite"] = diet_Sunflower_seed.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Sunflower_seed.loc[diet_Sunflower_seed.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Sunflower_seed.loc[diet_Sunflower_seed.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_White_beans = diet_White_beans.rename(columns={diet_White_beans.columns[0]: "reaction"})
diet_White_beans["metabolite"] = diet_White_beans.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_White_beans.loc[diet_White_beans.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_White_beans.loc[diet_White_beans.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Breastmilk = diet_Breastmilk.rename(columns={diet_Breastmilk.columns[0]: "reaction"})
diet_Breastmilk["metabolite"] = diet_Breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Breastmilk.loc[diet_Breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Breastmilk.loc[diet_Breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Infant_formula = diet_Infant_formula.rename(columns={diet_Infant_formula.columns[0]: "reaction"})
diet_Infant_formula["metabolite"] = diet_Infant_formula.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Infant_formula.loc[diet_Infant_formula.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Infant_formula.loc[diet_Infant_formula.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0

from cobra.io import read_sbml_model
import pandas as pd

recon3 = read_sbml_model("data/Recon3D.xml.gz") #importing Recon3D model
exchanges = pd.Series([r.id for r in recon3.exchanges])
exchanges = exchanges.str.replace("__", "_").str.replace("_e$|EX_", "", regex=True) #list with the nutrients that are absrobed

diet_Broccoli["dilution"] = 1.0
diet_Broccoli.loc[diet_Broccoli.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Broccoli["flux"] = diet_Broccoli["flux"] * diet_Broccoli["dilution"] #updaing the flux, considering the dilution
diet_Broccoli[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Brussel["dilution"] = 1.0
diet_Brussel.loc[diet_Brussel.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Brussel["flux"] = diet_Brussel["flux"] * diet_Brussel["dilution"] #updaing the flux, considering the dilution
diet_Brussel[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Cabbage["dilution"] = 1.0
diet_Cabbage.loc[diet_Cabbage.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Cabbage["flux"] = diet_Cabbage["flux"] * diet_Cabbage["dilution"] #updaing the flux, considering the dilution
diet_Cabbage[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Carrot["dilution"] = 1.0
diet_Carrot.loc[diet_Carrot.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Carrot["flux"] = diet_Carrot["flux"] * diet_Carrot["dilution"] #updaing the flux, considering the dilution
diet_Carrot[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Cauliflower["dilution"] = 1.0
diet_Cauliflower.loc[diet_Cauliflower.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Cauliflower["flux"] = diet_Cauliflower["flux"] * diet_Cauliflower["dilution"] #updaing the flux, considering the dilution
diet_Cauliflower[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Celery["dilution"] = 1.0
diet_Celery.loc[diet_Celery.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Celery["flux"] = diet_Celery["flux"] * diet_Celery["dilution"] #updaing the flux, considering the dilution
diet_Celery[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Cucumber["dilution"] = 1.0
diet_Cucumber.loc[diet_Cucumber.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Cucumber["flux"] = diet_Cucumber["flux"] * diet_Cucumber["dilution"] #updaing the flux, considering the dilution
diet_Cucumber[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Eggplant["dilution"] = 1.0
diet_Eggplant.loc[diet_Eggplant.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Eggplant["flux"] = diet_Eggplant["flux"] * diet_Eggplant["dilution"] #updaing the flux, considering the dilution
diet_Eggplant[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Green_beans["dilution"] = 1.0
diet_Green_beans.loc[diet_Green_beans.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Green_beans["flux"] = diet_Green_beans["flux"] * diet_Green_beans["dilution"] #updaing the flux, considering the dilution
diet_Green_beans[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Green_capsicum["dilution"] = 1.0
diet_Green_capsicum.loc[diet_Green_capsicum.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Green_capsicum["flux"] = diet_Green_capsicum["flux"] * diet_Green_capsicum["dilution"] #updaing the flux, considering the dilution
diet_Green_capsicum[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Lettuce["dilution"] = 1.0
diet_Lettuce.loc[diet_Lettuce.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Lettuce["flux"] = diet_Lettuce["flux"] * diet_Lettuce["dilution"] #updaing the flux, considering the dilution
diet_Lettuce[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Mushroom["dilution"] = 1.0
diet_Mushroom.loc[diet_Mushroom.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Mushroom["flux"] = diet_Mushroom["flux"] * diet_Mushroom["dilution"] #updaing the flux, considering the dilution
diet_Mushroom[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Onion["dilution"] = 1.0
diet_Onion.loc[diet_Onion.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Onion["flux"] = diet_Onion["flux"] * diet_Onion["dilution"] #updaing the flux, considering the dilution
diet_Onion[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Pak_choi["dilution"] = 1.0
diet_Pak_choi.loc[diet_Pak_choi.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Pak_choi["flux"] = diet_Pak_choi["flux"] * diet_Pak_choi["dilution"] #updaing the flux, considering the dilution
diet_Pak_choi[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Potato["dilution"] = 1.0
diet_Potato.loc[diet_Potato.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Potato["flux"] = diet_Potato["flux"] * diet_Potato["dilution"] #updaing the flux, considering the dilution
diet_Potato[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Pumpkin["dilution"] = 1.0
diet_Pumpkin.loc[diet_Pumpkin.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Pumpkin["flux"] = diet_Pumpkin["flux"] * diet_Pumpkin["dilution"] #updaing the flux, considering the dilution
diet_Pumpkin[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Sweetcorn["dilution"] = 1.0
diet_Sweetcorn.loc[diet_Sweetcorn.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Sweetcorn["flux"] = diet_Sweetcorn["flux"] * diet_Sweetcorn["dilution"] #updaing the flux, considering the dilution
diet_Sweetcorn[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Spinach["dilution"] = 1.0
diet_Spinach.loc[diet_Spinach.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Spinach["flux"] = diet_Spinach["flux"] * diet_Spinach["dilution"] #updaing the flux, considering the dilution
diet_Spinach[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Squash["dilution"] = 1.0
diet_Squash.loc[diet_Squash.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Squash["flux"] = diet_Squash["flux"] * diet_Squash["dilution"] #updaing the flux, considering the dilution
diet_Squash[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Sweet_potato["dilution"] = 1.0
diet_Sweet_potato.loc[diet_Sweet_potato.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Sweet_potato["flux"] = diet_Sweet_potato["flux"] * diet_Sweet_potato["dilution"] #updaing the flux, considering the dilution
diet_Sweet_potato[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Tomato["dilution"] = 1.0
diet_Tomato.loc[diet_Tomato.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Tomato["flux"] = diet_Tomato["flux"] * diet_Tomato["dilution"] #updaing the flux, considering the dilution
diet_Tomato[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Yam["dilution"] = 1.0
diet_Yam.loc[diet_Yam.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Yam["flux"] = diet_Yam["flux"] * diet_Yam["dilution"] #updaing the flux, considering the dilution
diet_Yam[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Zucchini["dilution"] = 1.0
diet_Zucchini.loc[diet_Zucchini.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Zucchini["flux"] = diet_Zucchini["flux"] * diet_Zucchini["dilution"] #updaing the flux, considering the dilution
diet_Zucchini[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Apple["dilution"] = 1.0
diet_Apple.loc[diet_Apple.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Apple["flux"] = diet_Apple["flux"] * diet_Apple["dilution"] #updaing the flux, considering the dilution
diet_Apple[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Banana["dilution"] = 1.0
diet_Banana.loc[diet_Banana.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Banana["flux"] = diet_Banana["flux"] * diet_Banana["dilution"] #updaing the flux, considering the dilution
diet_Banana[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Blackcurrant["dilution"] = 1.0
diet_Blackcurrant.loc[diet_Blackcurrant.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Blackcurrant["flux"] = diet_Blackcurrant["flux"] * diet_Blackcurrant["dilution"] #updaing the flux, considering the dilution
diet_Blackcurrant[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Blueberries["dilution"] = 1.0
diet_Blueberries.loc[diet_Blueberries.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Blueberries["flux"] = diet_Blueberries["flux"] * diet_Blueberries["dilution"] #updaing the flux, considering the dilution
diet_Blueberries[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Cherry["dilution"] = 1.0
diet_Cherry.loc[diet_Cherry.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Cherry["flux"] = diet_Cherry["flux"] * diet_Cherry["dilution"] #updaing the flux, considering the dilution
diet_Cherry[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Feijoa["dilution"] = 1.0
diet_Feijoa.loc[diet_Feijoa.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Feijoa["flux"] = diet_Feijoa["flux"] * diet_Feijoa["dilution"] #updaing the flux, considering the dilution
diet_Feijoa[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Gold_kiwifruit["dilution"] = 1.0
diet_Gold_kiwifruit.loc[diet_Gold_kiwifruit.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Gold_kiwifruit["flux"] = diet_Gold_kiwifruit["flux"] * diet_Gold_kiwifruit["dilution"] #updaing the flux, considering the dilution
diet_Gold_kiwifruit[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Grape["dilution"] = 1.0
diet_Grape.loc[diet_Grape.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Grape["flux"] = diet_Grape["flux"] * diet_Grape["dilution"] #updaing the flux, considering the dilution
diet_Grape[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Grapefruit["dilution"] = 1.0
diet_Grapefruit.loc[diet_Grapefruit.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Grapefruit["flux"] = diet_Grapefruit["flux"] * diet_Grapefruit["dilution"] #updaing the flux, considering the dilution
diet_Grapefruit[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Green_kiwifruit["dilution"] = 1.0
diet_Green_kiwifruit.loc[diet_Green_kiwifruit.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Green_kiwifruit["flux"] = diet_Green_kiwifruit["flux"] * diet_Green_kiwifruit["dilution"] #updaing the flux, considering the dilution
diet_Green_kiwifruit[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Mandarin["dilution"] = 1.0
diet_Mandarin.loc[diet_Mandarin.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Mandarin["flux"] = diet_Mandarin["flux"] * diet_Mandarin["dilution"] #updaing the flux, considering the dilution
diet_Mandarin[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Mango["dilution"] = 1.0
diet_Mango.loc[diet_Mango.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Mango["flux"] = diet_Mango["flux"] * diet_Mango["dilution"] #updaing the flux, considering the dilution
diet_Mango[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Melon["dilution"] = 1.0
diet_Melon.loc[diet_Melon.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Melon["flux"] = diet_Melon["flux"] * diet_Melon["dilution"] #updaing the flux, considering the dilution
diet_Melon[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Nectarine["dilution"] = 1.0
diet_Nectarine.loc[diet_Nectarine.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Nectarine["flux"] = diet_Nectarine["flux"] * diet_Nectarine["dilution"] #updaing the flux, considering the dilution
diet_Nectarine[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Orange["dilution"] = 1.0
diet_Orange.loc[diet_Orange.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Orange["flux"] = diet_Orange["flux"] * diet_Orange["dilution"] #updaing the flux, considering the dilution
diet_Orange[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Peache["dilution"] = 1.0
diet_Peache.loc[diet_Peache.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Peache["flux"] = diet_Peache["flux"] * diet_Peache["dilution"] #updaing the flux, considering the dilution
diet_Peache[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Pear["dilution"] = 1.0
diet_Pear.loc[diet_Pear.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Pear["flux"] = diet_Pear["flux"] * diet_Pear["dilution"] #updaing the flux, considering the dilution
diet_Pear[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Pineapple["dilution"] = 1.0
diet_Pineapple.loc[diet_Pineapple.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Pineapple["flux"] = diet_Pineapple["flux"] * diet_Pineapple["dilution"] #updaing the flux, considering the dilution
diet_Pineapple[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Plum["dilution"] = 1.0
diet_Plum.loc[diet_Plum.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Plum["flux"] = diet_Plum["flux"] * diet_Plum["dilution"] #updaing the flux, considering the dilution
diet_Plum[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Raspberries["dilution"] = 1.0
diet_Raspberries.loc[diet_Raspberries.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Raspberries["flux"] = diet_Raspberries["flux"] * diet_Raspberries["dilution"] #updaing the flux, considering the dilution
diet_Raspberries[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Strawberries["dilution"] = 1.0
diet_Strawberries.loc[diet_Strawberries.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Strawberries["flux"] = diet_Strawberries["flux"] * diet_Strawberries["dilution"] #updaing the flux, considering the dilution
diet_Strawberries[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Barley["dilution"] = 1.0
diet_Barley.loc[diet_Barley.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Barley["flux"] = diet_Barley["flux"] * diet_Barley["dilution"] #updaing the flux, considering the dilution
diet_Barley[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Barley_cereal["dilution"] = 1.0
diet_Barley_cereal.loc[diet_Barley_cereal.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Barley_cereal["flux"] = diet_Barley_cereal["flux"] * diet_Barley_cereal["dilution"] #updaing the flux, considering the dilution
diet_Barley_cereal[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Couscous["dilution"] = 1.0
diet_Couscous.loc[diet_Couscous.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Couscous["flux"] = diet_Couscous["flux"] * diet_Couscous["dilution"] #updaing the flux, considering the dilution
diet_Couscous[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Noodles["dilution"] = 1.0
diet_Noodles.loc[diet_Noodles.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Noodles["flux"] = diet_Noodles["flux"] * diet_Noodles["dilution"] #updaing the flux, considering the dilution
diet_Noodles[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Oat_cereal["dilution"] = 1.0
diet_Oat_cereal.loc[diet_Oat_cereal.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Oat_cereal["flux"] = diet_Oat_cereal["flux"] * diet_Oat_cereal["dilution"] #updaing the flux, considering the dilution
diet_Oat_cereal[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Pasta["dilution"] = 1.0
diet_Pasta.loc[diet_Pasta.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Pasta["flux"] = diet_Pasta["flux"] * diet_Pasta["dilution"] #updaing the flux, considering the dilution
diet_Pasta[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Rice["dilution"] = 1.0
diet_Rice.loc[diet_Rice.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Rice["flux"] = diet_Rice["flux"] * diet_Rice["dilution"] #updaing the flux, considering the dilution
diet_Rice[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Rice_cereal["dilution"] = 1.0
diet_Rice_cereal.loc[diet_Rice_cereal.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Rice_cereal["flux"] = diet_Rice_cereal["flux"] * diet_Rice_cereal["dilution"] #updaing the flux, considering the dilution
diet_Rice_cereal[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Tapioca_pudding["dilution"] = 1.0
diet_Tapioca_pudding.loc[diet_Tapioca_pudding.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Tapioca_pudding["flux"] = diet_Tapioca_pudding["flux"] * diet_Tapioca_pudding["dilution"] #updaing the flux, considering the dilution
diet_Tapioca_pudding[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_White_bread["dilution"] = 1.0
diet_White_bread.loc[diet_White_bread.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_White_bread["flux"] = diet_White_bread["flux"] * diet_White_bread["dilution"] #updaing the flux, considering the dilution
diet_White_bread[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Wholegrain_bread["dilution"] = 1.0
diet_Wholegrain_bread.loc[diet_Wholegrain_bread.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Wholegrain_bread["flux"] = diet_Wholegrain_bread["flux"] * diet_Wholegrain_bread["dilution"] #updaing the flux, considering the dilution
diet_Wholegrain_bread[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Cottage_cheese["dilution"] = 1.0
diet_Cottage_cheese.loc[diet_Cottage_cheese.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Cottage_cheese["flux"] = diet_Cottage_cheese["flux"] * diet_Cottage_cheese["dilution"] #updaing the flux, considering the dilution
diet_Cottage_cheese[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Eggs["dilution"] = 1.0
diet_Eggs.loc[diet_Eggs.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Eggs["flux"] = diet_Eggs["flux"] * diet_Eggs["dilution"] #updaing the flux, considering the dilution
diet_Eggs[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Mozzarella_cheese["dilution"] = 1.0
diet_Mozzarella_cheese.loc[diet_Mozzarella_cheese.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Mozzarella_cheese["flux"] = diet_Mozzarella_cheese["flux"] * diet_Mozzarella_cheese["dilution"] #updaing the flux, considering the dilution
diet_Mozzarella_cheese[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Soymilk["dilution"] = 1.0
diet_Soymilk.loc[diet_Soymilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Soymilk["flux"] = diet_Soymilk["flux"] * diet_Soymilk["dilution"] #updaing the flux, considering the dilution
diet_Soymilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Tofu["dilution"] = 1.0
diet_Tofu.loc[diet_Tofu.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Tofu["flux"] = diet_Tofu["flux"] * diet_Tofu["dilution"] #updaing the flux, considering the dilution
diet_Tofu[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Whole_milk["dilution"] = 1.0
diet_Whole_milk.loc[diet_Whole_milk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Whole_milk["flux"] = diet_Whole_milk["flux"] * diet_Whole_milk["dilution"] #updaing the flux, considering the dilution
diet_Whole_milk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Yoghurt["dilution"] = 1.0
diet_Yoghurt.loc[diet_Yoghurt.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Yoghurt["flux"] = diet_Yoghurt["flux"] * diet_Yoghurt["dilution"] #updaing the flux, considering the dilution
diet_Yoghurt[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Beef["dilution"] = 1.0
diet_Beef.loc[diet_Beef.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Beef["flux"] = diet_Beef["flux"] * diet_Beef["dilution"] #updaing the flux, considering the dilution
diet_Beef[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Chicken["dilution"] = 1.0
diet_Chicken.loc[diet_Chicken.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Chicken["flux"] = diet_Chicken["flux"] * diet_Chicken["dilution"] #updaing the flux, considering the dilution
diet_Chicken[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Codfish["dilution"] = 1.0
diet_Codfish.loc[diet_Codfish.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Codfish["flux"] = diet_Codfish["flux"] * diet_Codfish["dilution"] #updaing the flux, considering the dilution
diet_Codfish[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Lamb["dilution"] = 1.0
diet_Lamb.loc[diet_Lamb.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Lamb["flux"] = diet_Lamb["flux"] * diet_Lamb["dilution"] #updaing the flux, considering the dilution
diet_Lamb[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Mackerel["dilution"] = 1.0
diet_Mackerel.loc[diet_Mackerel.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Mackerel["flux"] = diet_Mackerel["flux"] * diet_Mackerel["dilution"] #updaing the flux, considering the dilution
diet_Mackerel[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Mussels["dilution"] = 1.0
diet_Mussels.loc[diet_Mussels.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Mussels["flux"] = diet_Mussels["flux"] * diet_Mussels["dilution"] #updaing the flux, considering the dilution
diet_Mussels[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Pork["dilution"] = 1.0
diet_Pork.loc[diet_Pork.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Pork["flux"] = diet_Pork["flux"] * diet_Pork["dilution"] #updaing the flux, considering the dilution
diet_Pork[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Salmon["dilution"] = 1.0
diet_Salmon.loc[diet_Salmon.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Salmon["flux"] = diet_Salmon["flux"] * diet_Salmon["dilution"] #updaing the flux, considering the dilution
diet_Salmon[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Shrimp["dilution"] = 1.0
diet_Shrimp.loc[diet_Shrimp.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Shrimp["flux"] = diet_Shrimp["flux"] * diet_Shrimp["dilution"] #updaing the flux, considering the dilution
diet_Shrimp[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Tuna["dilution"] = 1.0
diet_Tuna.loc[diet_Tuna.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Tuna["flux"] = diet_Tuna["flux"] * diet_Tuna["dilution"] #updaing the flux, considering the dilution
diet_Tuna[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Turkey["dilution"] = 1.0
diet_Turkey.loc[diet_Turkey.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Turkey["flux"] = diet_Turkey["flux"] * diet_Turkey["dilution"] #updaing the flux, considering the dilution
diet_Turkey[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Almond["dilution"] = 1.0
diet_Almond.loc[diet_Almond.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Almond["flux"] = diet_Almond["flux"] * diet_Almond["dilution"] #updaing the flux, considering the dilution
diet_Almond[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Black_beans["dilution"] = 1.0
diet_Black_beans.loc[diet_Black_beans.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Black_beans["flux"] = diet_Black_beans["flux"] * diet_Black_beans["dilution"] #updaing the flux, considering the dilution
diet_Black_beans[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Cashew["dilution"] = 1.0
diet_Cashew.loc[diet_Cashew.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Cashew["flux"] = diet_Cashew["flux"] * diet_Cashew["dilution"] #updaing the flux, considering the dilution
diet_Cashew[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Chia["dilution"] = 1.0
diet_Chia.loc[diet_Chia.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Chia["flux"] = diet_Chia["flux"] * diet_Chia["dilution"] #updaing the flux, considering the dilution
diet_Chia[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Chickpea["dilution"] = 1.0
diet_Chickpea.loc[diet_Chickpea.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Chickpea["flux"] = diet_Chickpea["flux"] * diet_Chickpea["dilution"] #updaing the flux, considering the dilution
diet_Chickpea[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Green_peas["dilution"] = 1.0
diet_Green_peas.loc[diet_Green_peas.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Green_peas["flux"] = diet_Green_peas["flux"] * diet_Green_peas["dilution"] #updaing the flux, considering the dilution
diet_Green_peas[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Hazelnut["dilution"] = 1.0
diet_Hazelnut.loc[diet_Hazelnut.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Hazelnut["flux"] = diet_Hazelnut["flux"] * diet_Hazelnut["dilution"] #updaing the flux, considering the dilution
diet_Hazelnut[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Lentils["dilution"] = 1.0
diet_Lentils.loc[diet_Lentils.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Lentils["flux"] = diet_Lentils["flux"] * diet_Lentils["dilution"] #updaing the flux, considering the dilution
diet_Lentils[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Peanut["dilution"] = 1.0
diet_Peanut.loc[diet_Peanut.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Peanut["flux"] = diet_Peanut["flux"] * diet_Peanut["dilution"] #updaing the flux, considering the dilution
diet_Peanut[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Pecans["dilution"] = 1.0
diet_Pecans.loc[diet_Pecans.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Pecans["flux"] = diet_Pecans["flux"] * diet_Pecans["dilution"] #updaing the flux, considering the dilution
diet_Pecans[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Pumpkin_seed["dilution"] = 1.0
diet_Pumpkin_seed.loc[diet_Pumpkin_seed.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Pumpkin_seed["flux"] = diet_Pumpkin_seed["flux"] * diet_Pumpkin_seed["dilution"] #updaing the flux, considering the dilution
diet_Pumpkin_seed[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Red_beans["dilution"] = 1.0
diet_Red_beans.loc[diet_Red_beans.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Red_beans["flux"] = diet_Red_beans["flux"] * diet_Red_beans["dilution"] #updaing the flux, considering the dilution
diet_Red_beans[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Soybean["dilution"] = 1.0
diet_Soybean.loc[diet_Soybean.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Soybean["flux"] = diet_Soybean["flux"] * diet_Soybean["dilution"] #updaing the flux, considering the dilution
diet_Soybean[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Split_peas["dilution"] = 1.0
diet_Split_peas.loc[diet_Split_peas.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Split_peas["flux"] = diet_Split_peas["flux"] * diet_Split_peas["dilution"] #updaing the flux, considering the dilution
diet_Split_peas[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Sunflower_seed["dilution"] = 1.0
diet_Sunflower_seed.loc[diet_Sunflower_seed.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Sunflower_seed["flux"] = diet_Sunflower_seed["flux"] * diet_Sunflower_seed["dilution"] #updaing the flux, considering the dilution
diet_Sunflower_seed[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_White_beans["dilution"] = 1.0
diet_White_beans.loc[diet_White_beans.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_White_beans["flux"] = diet_White_beans["flux"] * diet_White_beans["dilution"] #updaing the flux, considering the dilution
diet_White_beans[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Breastmilk["dilution"] = 1.0
diet_Breastmilk.loc[diet_Breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Breastmilk["flux"] = diet_Breastmilk["flux"] * diet_Breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Infant_formula["dilution"] = 1.0
diet_Infant_formula.loc[diet_Infant_formula.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Infant_formula["flux"] = diet_Infant_formula["flux"] * diet_Infant_formula["dilution"] #updaing the flux, considering the dilution
diet_Infant_formula[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()

#Adding host secreted substrates
#we consider the flux of these compounds as 1 mmol/h

diet_Broccoli.set_index("metabolite", inplace=True)
diet_Brussel.set_index("metabolite", inplace=True)
diet_Cabbage.set_index("metabolite", inplace=True)
diet_Carrot.set_index("metabolite", inplace=True)
diet_Cauliflower.set_index("metabolite", inplace=True)
diet_Celery.set_index("metabolite", inplace=True)
diet_Cucumber.set_index("metabolite", inplace=True)
diet_Eggplant.set_index("metabolite", inplace=True)
diet_Green_beans.set_index("metabolite", inplace=True)
diet_Green_capsicum.set_index("metabolite", inplace=True)
diet_Lettuce.set_index("metabolite", inplace=True)
diet_Mushroom.set_index("metabolite", inplace=True)
diet_Onion.set_index("metabolite", inplace=True)
diet_Pak_choi.set_index("metabolite", inplace=True)
diet_Potato.set_index("metabolite", inplace=True)
diet_Pumpkin.set_index("metabolite", inplace=True)
diet_Sweetcorn.set_index("metabolite", inplace=True)
diet_Spinach.set_index("metabolite", inplace=True)
diet_Squash.set_index("metabolite", inplace=True)
diet_Sweet_potato.set_index("metabolite", inplace=True)
diet_Tomato.set_index("metabolite", inplace=True)
diet_Yam.set_index("metabolite", inplace=True)
diet_Zucchini.set_index("metabolite", inplace=True)
diet_Apple.set_index("metabolite", inplace=True)
diet_Banana.set_index("metabolite", inplace=True)
diet_Blackcurrant.set_index("metabolite", inplace=True)
diet_Blueberries.set_index("metabolite", inplace=True)
diet_Cherry.set_index("metabolite", inplace=True)
diet_Feijoa.set_index("metabolite", inplace=True)
diet_Gold_kiwifruit.set_index("metabolite", inplace=True)
diet_Grape.set_index("metabolite", inplace=True)
diet_Grapefruit.set_index("metabolite", inplace=True)
diet_Green_kiwifruit.set_index("metabolite", inplace=True)
diet_Mandarin.set_index("metabolite", inplace=True)
diet_Mango.set_index("metabolite", inplace=True)
diet_Melon.set_index("metabolite", inplace=True)
diet_Nectarine.set_index("metabolite", inplace=True)
diet_Orange.set_index("metabolite", inplace=True)
diet_Peache.set_index("metabolite", inplace=True)
diet_Pear.set_index("metabolite", inplace=True)
diet_Pineapple.set_index("metabolite", inplace=True)
diet_Plum.set_index("metabolite", inplace=True)
diet_Raspberries.set_index("metabolite", inplace=True)
diet_Strawberries.set_index("metabolite", inplace=True)
diet_Barley.set_index("metabolite", inplace=True)
diet_Barley_cereal.set_index("metabolite", inplace=True)
diet_Couscous.set_index("metabolite", inplace=True)
diet_Noodles.set_index("metabolite", inplace=True)
diet_Oat_cereal.set_index("metabolite", inplace=True)
diet_Pasta.set_index("metabolite", inplace=True)
diet_Rice.set_index("metabolite", inplace=True)
diet_Rice_cereal.set_index("metabolite", inplace=True)
diet_Tapioca_pudding.set_index("metabolite", inplace=True)
diet_White_bread.set_index("metabolite", inplace=True)
diet_Wholegrain_bread.set_index("metabolite", inplace=True)
diet_Cottage_cheese.set_index("metabolite", inplace=True)
diet_Eggs.set_index("metabolite", inplace=True)
diet_Mozzarella_cheese.set_index("metabolite", inplace=True)
diet_Soymilk.set_index("metabolite", inplace=True)
diet_Tofu.set_index("metabolite", inplace=True)
diet_Whole_milk.set_index("metabolite", inplace=True)
diet_Yoghurt.set_index("metabolite", inplace=True)
diet_Beef.set_index("metabolite", inplace=True)
diet_Chicken.set_index("metabolite", inplace=True)
diet_Codfish.set_index("metabolite", inplace=True)
diet_Lamb.set_index("metabolite", inplace=True)
diet_Mackerel.set_index("metabolite", inplace=True)
diet_Mussels.set_index("metabolite", inplace=True)
diet_Pork.set_index("metabolite", inplace=True)
diet_Salmon.set_index("metabolite", inplace=True)
diet_Shrimp.set_index("metabolite", inplace=True)
diet_Tuna.set_index("metabolite", inplace=True)
diet_Turkey.set_index("metabolite", inplace=True)
diet_Almond.set_index("metabolite", inplace=True)
diet_Black_beans.set_index("metabolite", inplace=True)
diet_Cashew.set_index("metabolite", inplace=True)
diet_Chia.set_index("metabolite", inplace=True)
diet_Chickpea.set_index("metabolite", inplace=True)
diet_Green_peas.set_index("metabolite", inplace=True)
diet_Hazelnut.set_index("metabolite", inplace=True)
diet_Lentils.set_index("metabolite", inplace=True)
diet_Peanut.set_index("metabolite", inplace=True)
diet_Pecans.set_index("metabolite", inplace=True)
diet_Pumpkin_seed.set_index("metabolite", inplace=True)
diet_Red_beans.set_index("metabolite", inplace=True)
diet_Soybean.set_index("metabolite", inplace=True)
diet_Split_peas.set_index("metabolite", inplace=True)
diet_Sunflower_seed.set_index("metabolite", inplace=True)
diet_White_beans.set_index("metabolite", inplace=True)
diet_Breastmilk.set_index("metabolite", inplace=True)
diet_Infant_formula.set_index("metabolite", inplace=True)

for met in annotations.loc[annotations.metabolite.str.contains("core"), "metabolite"]: # mucins
    diet_Broccoli.loc[met, "flux"] = 1
    diet_Brussel.loc[met, "flux"] = 1
    diet_Cabbage.loc[met, "flux"] = 1
    diet_Carrot.loc[met, "flux"] = 1
    diet_Cauliflower.loc[met, "flux"] = 1
    diet_Celery.loc[met, "flux"] = 1
    diet_Cucumber.loc[met, "flux"] = 1
    diet_Eggplant.loc[met, "flux"] = 1
    diet_Green_beans.loc[met, "flux"] = 1
    diet_Green_capsicum.loc[met, "flux"] = 1
    diet_Lettuce.loc[met, "flux"] = 1
    diet_Mushroom.loc[met, "flux"] = 1
    diet_Onion.loc[met, "flux"] = 1
    diet_Pak_choi.loc[met, "flux"] = 1
    diet_Potato.loc[met, "flux"] = 1
    diet_Pumpkin.loc[met, "flux"] = 1
    diet_Sweetcorn.loc[met, "flux"] = 1
    diet_Spinach.loc[met, "flux"] = 1
    diet_Squash.loc[met, "flux"] = 1
    diet_Sweet_potato.loc[met, "flux"] = 1
    diet_Tomato.loc[met, "flux"] = 1
    diet_Yam.loc[met, "flux"] = 1
    diet_Zucchini.loc[met, "flux"] = 1
    diet_Apple.loc[met, "flux"] = 1
    diet_Banana.loc[met, "flux"] = 1
    diet_Blackcurrant.loc[met, "flux"] = 1
    diet_Blueberries.loc[met, "flux"] = 1
    diet_Cherry.loc[met, "flux"] = 1
    diet_Feijoa.loc[met, "flux"] = 1
    diet_Gold_kiwifruit.loc[met, "flux"] = 1
    diet_Grape.loc[met, "flux"] = 1
    diet_Grapefruit.loc[met, "flux"] = 1
    diet_Green_kiwifruit.loc[met, "flux"] = 1
    diet_Mandarin.loc[met, "flux"] = 1
    diet_Mango.loc[met, "flux"] = 1
    diet_Melon.loc[met, "flux"] = 1
    diet_Nectarine.loc[met, "flux"] = 1
    diet_Orange.loc[met, "flux"] = 1
    diet_Peache.loc[met, "flux"] = 1
    diet_Pear.loc[met, "flux"] = 1
    diet_Pineapple.loc[met, "flux"] = 1
    diet_Plum.loc[met, "flux"] = 1
    diet_Raspberries.loc[met, "flux"] = 1
    diet_Strawberries.loc[met, "flux"] = 1
    diet_Barley.loc[met, "flux"] = 1
    diet_Barley_cereal.loc[met, "flux"] = 1
    diet_Couscous.loc[met, "flux"] = 1
    diet_Noodles.loc[met, "flux"] = 1
    diet_Oat_cereal.loc[met, "flux"] = 1
    diet_Pasta.loc[met, "flux"] = 1
    diet_Rice.loc[met, "flux"] = 1
    diet_Rice_cereal.loc[met, "flux"] = 1
    diet_Tapioca_pudding.loc[met, "flux"] = 1
    diet_White_bread.loc[met, "flux"] = 1
    diet_Wholegrain_bread.loc[met, "flux"] = 1
    diet_Cottage_cheese.loc[met, "flux"] = 1
    diet_Eggs.loc[met, "flux"] = 1
    diet_Mozzarella_cheese.loc[met, "flux"] = 1
    diet_Soymilk.loc[met, "flux"] = 1
    diet_Tofu.loc[met, "flux"] = 1
    diet_Whole_milk.loc[met, "flux"] = 1
    diet_Yoghurt.loc[met, "flux"] = 1
    diet_Beef.loc[met, "flux"] = 1
    diet_Chicken.loc[met, "flux"] = 1
    diet_Codfish.loc[met, "flux"] = 1
    diet_Lamb.loc[met, "flux"] = 1
    diet_Mackerel.loc[met, "flux"] = 1
    diet_Mussels.loc[met, "flux"] = 1
    diet_Pork.loc[met, "flux"] = 1
    diet_Salmon.loc[met, "flux"] = 1
    diet_Shrimp.loc[met, "flux"] = 1
    diet_Tuna.loc[met, "flux"] = 1
    diet_Turkey.loc[met, "flux"] = 1
    diet_Almond.loc[met, "flux"] = 1
    diet_Black_beans.loc[met, "flux"] = 1
    diet_Cashew.loc[met, "flux"] = 1
    diet_Chia.loc[met, "flux"] = 1
    diet_Chickpea.loc[met, "flux"] = 1
    diet_Green_peas.loc[met, "flux"] = 1
    diet_Hazelnut.loc[met, "flux"] = 1
    diet_Lentils.loc[met, "flux"] = 1
    diet_Peanut.loc[met, "flux"] = 1
    diet_Pecans.loc[met, "flux"] = 1
    diet_Pumpkin_seed.loc[met, "flux"] = 1
    diet_Red_beans.loc[met, "flux"] = 1
    diet_Soybean.loc[met, "flux"] = 1
    diet_Split_peas.loc[met, "flux"] = 1
    diet_Sunflower_seed.loc[met, "flux"] = 1
    diet_White_beans.loc[met, "flux"] = 1
    diet_Breastmilk.loc[met, "flux"] = 1
    diet_Infant_formula.loc[met, "flux"] = 1

for met in ["gchola", "tchola"]: # primary BAs
    diet_Broccoli.loc[met, "flux"] = 1
    diet_Brussel.loc[met, "flux"] = 1
    diet_Cabbage.loc[met, "flux"] = 1
    diet_Carrot.loc[met, "flux"] = 1
    diet_Cauliflower.loc[met, "flux"] = 1
    diet_Celery.loc[met, "flux"] = 1
    diet_Cucumber.loc[met, "flux"] = 1
    diet_Eggplant.loc[met, "flux"] = 1
    diet_Green_beans.loc[met, "flux"] = 1
    diet_Green_capsicum.loc[met, "flux"] = 1
    diet_Lettuce.loc[met, "flux"] = 1
    diet_Mushroom.loc[met, "flux"] = 1
    diet_Onion.loc[met, "flux"] = 1
    diet_Pak_choi.loc[met, "flux"] = 1
    diet_Potato.loc[met, "flux"] = 1
    diet_Pumpkin.loc[met, "flux"] = 1
    diet_Sweetcorn.loc[met, "flux"] = 1
    diet_Spinach.loc[met, "flux"] = 1
    diet_Squash.loc[met, "flux"] = 1
    diet_Sweet_potato.loc[met, "flux"] = 1
    diet_Tomato.loc[met, "flux"] = 1
    diet_Yam.loc[met, "flux"] = 1
    diet_Zucchini.loc[met, "flux"] = 1
    diet_Apple.loc[met, "flux"] = 1
    diet_Banana.loc[met, "flux"] = 1
    diet_Blackcurrant.loc[met, "flux"] = 1
    diet_Blueberries.loc[met, "flux"] = 1
    diet_Cherry.loc[met, "flux"] = 1
    diet_Feijoa.loc[met, "flux"] = 1
    diet_Gold_kiwifruit.loc[met, "flux"] = 1
    diet_Grape.loc[met, "flux"] = 1
    diet_Grapefruit.loc[met, "flux"] = 1
    diet_Green_kiwifruit.loc[met, "flux"] = 1
    diet_Mandarin.loc[met, "flux"] = 1
    diet_Mango.loc[met, "flux"] = 1
    diet_Melon.loc[met, "flux"] = 1
    diet_Nectarine.loc[met, "flux"] = 1
    diet_Orange.loc[met, "flux"] = 1
    diet_Peache.loc[met, "flux"] = 1
    diet_Pear.loc[met, "flux"] = 1
    diet_Pineapple.loc[met, "flux"] = 1
    diet_Plum.loc[met, "flux"] = 1
    diet_Raspberries.loc[met, "flux"] = 1
    diet_Strawberries.loc[met, "flux"] = 1
    diet_Barley.loc[met, "flux"] = 1
    diet_Barley_cereal.loc[met, "flux"] = 1
    diet_Couscous.loc[met, "flux"] = 1
    diet_Noodles.loc[met, "flux"] = 1
    diet_Oat_cereal.loc[met, "flux"] = 1
    diet_Pasta.loc[met, "flux"] = 1
    diet_Rice.loc[met, "flux"] = 1
    diet_Rice_cereal.loc[met, "flux"] = 1
    diet_Tapioca_pudding.loc[met, "flux"] = 1
    diet_White_bread.loc[met, "flux"] = 1
    diet_Wholegrain_bread.loc[met, "flux"] = 1
    diet_Cottage_cheese.loc[met, "flux"] = 1
    diet_Eggs.loc[met, "flux"] = 1
    diet_Mozzarella_cheese.loc[met, "flux"] = 1
    diet_Soymilk.loc[met, "flux"] = 1
    diet_Tofu.loc[met, "flux"] = 1
    diet_Whole_milk.loc[met, "flux"] = 1
    diet_Yoghurt.loc[met, "flux"] = 1
    diet_Beef.loc[met, "flux"] = 1
    diet_Chicken.loc[met, "flux"] = 1
    diet_Codfish.loc[met, "flux"] = 1
    diet_Lamb.loc[met, "flux"] = 1
    diet_Mackerel.loc[met, "flux"] = 1
    diet_Mussels.loc[met, "flux"] = 1
    diet_Pork.loc[met, "flux"] = 1
    diet_Salmon.loc[met, "flux"] = 1
    diet_Shrimp.loc[met, "flux"] = 1
    diet_Tuna.loc[met, "flux"] = 1
    diet_Turkey.loc[met, "flux"] = 1
    diet_Almond.loc[met, "flux"] = 1
    diet_Black_beans.loc[met, "flux"] = 1
    diet_Cashew.loc[met, "flux"] = 1
    diet_Chia.loc[met, "flux"] = 1
    diet_Chickpea.loc[met, "flux"] = 1
    diet_Green_peas.loc[met, "flux"] = 1
    diet_Hazelnut.loc[met, "flux"] = 1
    diet_Lentils.loc[met, "flux"] = 1
    diet_Peanut.loc[met, "flux"] = 1
    diet_Pecans.loc[met, "flux"] = 1
    diet_Pumpkin_seed.loc[met, "flux"] = 1
    diet_Red_beans.loc[met, "flux"] = 1
    diet_Soybean.loc[met, "flux"] = 1
    diet_Split_peas.loc[met, "flux"] = 1
    diet_Sunflower_seed.loc[met, "flux"] = 1
    diet_White_beans.loc[met, "flux"] = 1
    diet_Breastmilk.loc[met, "flux"] = 1
    diet_Infant_formula.loc[met, "flux"] = 1

diet_Broccoli.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Brussel.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Cabbage.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Carrot.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Cauliflower.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Celery.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Cucumber.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Eggplant.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Green_beans.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Green_capsicum.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Lettuce.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Mushroom.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Onion.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Pak_choi.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Potato.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Pumpkin.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Sweetcorn.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Spinach.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Squash.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Sweet_potato.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Tomato.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Yam.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Zucchini.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Apple.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Banana.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Blackcurrant.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Blueberries.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Cherry.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Feijoa.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Gold_kiwifruit.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Grape.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Grapefruit.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Green_kiwifruit.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Mandarin.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Mango.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Melon.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Nectarine.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Orange.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Peache.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Pear.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Pineapple.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Plum.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Raspberries.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Strawberries.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Barley.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Barley_cereal.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Couscous.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Noodles.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Oat_cereal.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Pasta.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Rice.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Rice_cereal.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Tapioca_pudding.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_White_bread.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Wholegrain_bread.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Cottage_cheese.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Eggs.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Mozzarella_cheese.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Soymilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Tofu.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Whole_milk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Yoghurt.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Beef.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Chicken.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Codfish.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Lamb.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Mackerel.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Mussels.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Pork.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Salmon.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Shrimp.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Tuna.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Turkey.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Almond.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Black_beans.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Cashew.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Chia.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Chickpea.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Green_peas.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Hazelnut.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Lentils.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Peanut.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Pecans.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Pumpkin_seed.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Red_beans.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Soybean.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Split_peas.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Sunflower_seed.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_White_beans.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Infant_formula.loc["o2", "flux"] = 0.001 # anaerobic environment

diet_Broccoli.reset_index(inplace=True)
diet_Broccoli["reaction"] = "EX_" + diet_Broccoli.metabolite + "(e)"
diet_Brussel.reset_index(inplace=True)
diet_Brussel["reaction"] = "EX_" + diet_Brussel.metabolite + "(e)"
diet_Cabbage.reset_index(inplace=True)
diet_Cabbage["reaction"] = "EX_" + diet_Cabbage.metabolite + "(e)"
diet_Carrot.reset_index(inplace=True)
diet_Carrot["reaction"] = "EX_" + diet_Carrot.metabolite + "(e)"
diet_Cauliflower.reset_index(inplace=True)
diet_Cauliflower["reaction"] = "EX_" + diet_Cauliflower.metabolite + "(e)"
diet_Celery.reset_index(inplace=True)
diet_Celery["reaction"] = "EX_" + diet_Celery.metabolite + "(e)"
diet_Cucumber.reset_index(inplace=True)
diet_Cucumber["reaction"] = "EX_" + diet_Cucumber.metabolite + "(e)"
diet_Eggplant.reset_index(inplace=True)
diet_Eggplant["reaction"] = "EX_" + diet_Eggplant.metabolite + "(e)"
diet_Green_beans.reset_index(inplace=True)
diet_Green_beans["reaction"] = "EX_" + diet_Green_beans.metabolite + "(e)"
diet_Green_capsicum.reset_index(inplace=True)
diet_Green_capsicum["reaction"] = "EX_" + diet_Green_capsicum.metabolite + "(e)"
diet_Lettuce.reset_index(inplace=True)
diet_Lettuce["reaction"] = "EX_" + diet_Lettuce.metabolite + "(e)"
diet_Mushroom.reset_index(inplace=True)
diet_Mushroom["reaction"] = "EX_" + diet_Mushroom.metabolite + "(e)"
diet_Onion.reset_index(inplace=True)
diet_Onion["reaction"] = "EX_" + diet_Onion.metabolite + "(e)"
diet_Pak_choi.reset_index(inplace=True)
diet_Pak_choi["reaction"] = "EX_" + diet_Pak_choi.metabolite + "(e)"
diet_Potato.reset_index(inplace=True)
diet_Potato["reaction"] = "EX_" + diet_Potato.metabolite + "(e)"
diet_Pumpkin.reset_index(inplace=True)
diet_Pumpkin["reaction"] = "EX_" + diet_Pumpkin.metabolite + "(e)"
diet_Sweetcorn.reset_index(inplace=True)
diet_Sweetcorn["reaction"] = "EX_" + diet_Sweetcorn.metabolite + "(e)"
diet_Spinach.reset_index(inplace=True)
diet_Spinach["reaction"] = "EX_" + diet_Spinach.metabolite + "(e)"
diet_Squash.reset_index(inplace=True)
diet_Squash["reaction"] = "EX_" + diet_Squash.metabolite + "(e)"
diet_Sweet_potato.reset_index(inplace=True)
diet_Sweet_potato["reaction"] = "EX_" + diet_Sweet_potato.metabolite + "(e)"
diet_Tomato.reset_index(inplace=True)
diet_Tomato["reaction"] = "EX_" + diet_Tomato.metabolite + "(e)"
diet_Yam.reset_index(inplace=True)
diet_Yam["reaction"] = "EX_" + diet_Yam.metabolite + "(e)"
diet_Zucchini.reset_index(inplace=True)
diet_Zucchini["reaction"] = "EX_" + diet_Zucchini.metabolite + "(e)"
diet_Apple.reset_index(inplace=True)
diet_Apple["reaction"] = "EX_" + diet_Apple.metabolite + "(e)"
diet_Banana.reset_index(inplace=True)
diet_Banana["reaction"] = "EX_" + diet_Banana.metabolite + "(e)"
diet_Blackcurrant.reset_index(inplace=True)
diet_Blackcurrant["reaction"] = "EX_" + diet_Blackcurrant.metabolite + "(e)"
diet_Blueberries.reset_index(inplace=True)
diet_Blueberries["reaction"] = "EX_" + diet_Blueberries.metabolite + "(e)"
diet_Cherry.reset_index(inplace=True)
diet_Cherry["reaction"] = "EX_" + diet_Cherry.metabolite + "(e)"
diet_Feijoa.reset_index(inplace=True)
diet_Feijoa["reaction"] = "EX_" + diet_Feijoa.metabolite + "(e)"
diet_Gold_kiwifruit.reset_index(inplace=True)
diet_Gold_kiwifruit["reaction"] = "EX_" + diet_Gold_kiwifruit.metabolite + "(e)"
diet_Grape.reset_index(inplace=True)
diet_Grape["reaction"] = "EX_" + diet_Grape.metabolite + "(e)"
diet_Grapefruit.reset_index(inplace=True)
diet_Grapefruit["reaction"] = "EX_" + diet_Grapefruit.metabolite + "(e)"
diet_Green_kiwifruit.reset_index(inplace=True)
diet_Green_kiwifruit["reaction"] = "EX_" + diet_Green_kiwifruit.metabolite + "(e)"
diet_Mandarin.reset_index(inplace=True)
diet_Mandarin["reaction"] = "EX_" + diet_Mandarin.metabolite + "(e)"
diet_Mango.reset_index(inplace=True)
diet_Mango["reaction"] = "EX_" + diet_Mango.metabolite + "(e)"
diet_Melon.reset_index(inplace=True)
diet_Melon["reaction"] = "EX_" + diet_Melon.metabolite + "(e)"
diet_Nectarine.reset_index(inplace=True)
diet_Nectarine["reaction"] = "EX_" + diet_Nectarine.metabolite + "(e)"
diet_Orange.reset_index(inplace=True)
diet_Orange["reaction"] = "EX_" + diet_Orange.metabolite + "(e)"
diet_Peache.reset_index(inplace=True)
diet_Peache["reaction"] = "EX_" + diet_Peache.metabolite + "(e)"
diet_Pear.reset_index(inplace=True)
diet_Pear["reaction"] = "EX_" + diet_Pear.metabolite + "(e)"
diet_Pineapple.reset_index(inplace=True)
diet_Pineapple["reaction"] = "EX_" + diet_Pineapple.metabolite + "(e)"
diet_Plum.reset_index(inplace=True)
diet_Plum["reaction"] = "EX_" + diet_Plum.metabolite + "(e)"
diet_Raspberries.reset_index(inplace=True)
diet_Raspberries["reaction"] = "EX_" + diet_Raspberries.metabolite + "(e)"
diet_Strawberries.reset_index(inplace=True)
diet_Strawberries["reaction"] = "EX_" + diet_Strawberries.metabolite + "(e)"
diet_Barley.reset_index(inplace=True)
diet_Barley["reaction"] = "EX_" + diet_Barley.metabolite + "(e)"
diet_Barley_cereal.reset_index(inplace=True)
diet_Barley_cereal["reaction"] = "EX_" + diet_Barley_cereal.metabolite + "(e)"
diet_Couscous.reset_index(inplace=True)
diet_Couscous["reaction"] = "EX_" + diet_Couscous.metabolite + "(e)"
diet_Noodles.reset_index(inplace=True)
diet_Noodles["reaction"] = "EX_" + diet_Noodles.metabolite + "(e)"
diet_Oat_cereal.reset_index(inplace=True)
diet_Oat_cereal["reaction"] = "EX_" + diet_Oat_cereal.metabolite + "(e)"
diet_Pasta.reset_index(inplace=True)
diet_Pasta["reaction"] = "EX_" + diet_Pasta.metabolite + "(e)"
diet_Rice.reset_index(inplace=True)
diet_Rice["reaction"] = "EX_" + diet_Rice.metabolite + "(e)"
diet_Rice_cereal.reset_index(inplace=True)
diet_Rice_cereal["reaction"] = "EX_" + diet_Rice_cereal.metabolite + "(e)"
diet_Tapioca_pudding.reset_index(inplace=True)
diet_Tapioca_pudding["reaction"] = "EX_" + diet_Tapioca_pudding.metabolite + "(e)"
diet_White_bread.reset_index(inplace=True)
diet_White_bread["reaction"] = "EX_" + diet_White_bread.metabolite + "(e)"
diet_Wholegrain_bread.reset_index(inplace=True)
diet_Wholegrain_bread["reaction"] = "EX_" + diet_Wholegrain_bread.metabolite + "(e)"
diet_Cottage_cheese.reset_index(inplace=True)
diet_Cottage_cheese["reaction"] = "EX_" + diet_Cottage_cheese.metabolite + "(e)"
diet_Eggs.reset_index(inplace=True)
diet_Eggs["reaction"] = "EX_" + diet_Eggs.metabolite + "(e)"
diet_Mozzarella_cheese.reset_index(inplace=True)
diet_Mozzarella_cheese["reaction"] = "EX_" + diet_Mozzarella_cheese.metabolite + "(e)"
diet_Soymilk.reset_index(inplace=True)
diet_Soymilk["reaction"] = "EX_" + diet_Soymilk.metabolite + "(e)"
diet_Tofu.reset_index(inplace=True)
diet_Tofu["reaction"] = "EX_" + diet_Tofu.metabolite + "(e)"
diet_Whole_milk.reset_index(inplace=True)
diet_Whole_milk["reaction"] = "EX_" + diet_Whole_milk.metabolite + "(e)"
diet_Yoghurt.reset_index(inplace=True)
diet_Yoghurt["reaction"] = "EX_" + diet_Yoghurt.metabolite + "(e)"
diet_Beef.reset_index(inplace=True)
diet_Beef["reaction"] = "EX_" + diet_Beef.metabolite + "(e)"
diet_Chicken.reset_index(inplace=True)
diet_Chicken["reaction"] = "EX_" + diet_Chicken.metabolite + "(e)"
diet_Codfish.reset_index(inplace=True)
diet_Codfish["reaction"] = "EX_" + diet_Codfish.metabolite + "(e)"
diet_Lamb.reset_index(inplace=True)
diet_Lamb["reaction"] = "EX_" + diet_Lamb.metabolite + "(e)"
diet_Mackerel.reset_index(inplace=True)
diet_Mackerel["reaction"] = "EX_" + diet_Mackerel.metabolite + "(e)"
diet_Mussels.reset_index(inplace=True)
diet_Mussels["reaction"] = "EX_" + diet_Mussels.metabolite + "(e)"
diet_Pork.reset_index(inplace=True)
diet_Pork["reaction"] = "EX_" + diet_Pork.metabolite + "(e)"
diet_Salmon.reset_index(inplace=True)
diet_Salmon["reaction"] = "EX_" + diet_Salmon.metabolite + "(e)"
diet_Shrimp.reset_index(inplace=True)
diet_Shrimp["reaction"] = "EX_" + diet_Shrimp.metabolite + "(e)"
diet_Tuna.reset_index(inplace=True)
diet_Tuna["reaction"] = "EX_" + diet_Tuna.metabolite + "(e)"
diet_Turkey.reset_index(inplace=True)
diet_Turkey["reaction"] = "EX_" + diet_Turkey.metabolite + "(e)"
diet_Almond.reset_index(inplace=True)
diet_Almond["reaction"] = "EX_" + diet_Almond.metabolite + "(e)"
diet_Black_beans.reset_index(inplace=True)
diet_Black_beans["reaction"] = "EX_" + diet_Black_beans.metabolite + "(e)"
diet_Cashew.reset_index(inplace=True)
diet_Cashew["reaction"] = "EX_" + diet_Cashew.metabolite + "(e)"
diet_Chia.reset_index(inplace=True)
diet_Chia["reaction"] = "EX_" + diet_Chia.metabolite + "(e)"
diet_Chickpea.reset_index(inplace=True)
diet_Chickpea["reaction"] = "EX_" + diet_Chickpea.metabolite + "(e)"
diet_Green_peas.reset_index(inplace=True)
diet_Green_peas["reaction"] = "EX_" + diet_Green_peas.metabolite + "(e)"
diet_Hazelnut.reset_index(inplace=True)
diet_Hazelnut["reaction"] = "EX_" + diet_Hazelnut.metabolite + "(e)"
diet_Lentils.reset_index(inplace=True)
diet_Lentils["reaction"] = "EX_" + diet_Lentils.metabolite + "(e)"
diet_Peanut.reset_index(inplace=True)
diet_Peanut["reaction"] = "EX_" + diet_Peanut.metabolite + "(e)"
diet_Pecans.reset_index(inplace=True)
diet_Pecans["reaction"] = "EX_" + diet_Pecans.metabolite + "(e)"
diet_Pumpkin_seed.reset_index(inplace=True)
diet_Pumpkin_seed["reaction"] = "EX_" + diet_Pumpkin_seed.metabolite + "(e)"
diet_Red_beans.reset_index(inplace=True)
diet_Red_beans["reaction"] = "EX_" + diet_Red_beans.metabolite + "(e)"
diet_Soybean.reset_index(inplace=True)
diet_Soybean["reaction"] = "EX_" + diet_Soybean.metabolite + "(e)"
diet_Split_peas.reset_index(inplace=True)
diet_Split_peas["reaction"] = "EX_" + diet_Split_peas.metabolite + "(e)"
diet_Sunflower_seed.reset_index(inplace=True)
diet_Sunflower_seed["reaction"] = "EX_" + diet_Sunflower_seed.metabolite + "(e)"
diet_White_beans.reset_index(inplace=True)
diet_White_beans["reaction"] = "EX_" + diet_White_beans.metabolite + "(e)"
diet_Breastmilk.reset_index(inplace=True)
diet_Breastmilk["reaction"] = "EX_" + diet_Breastmilk.metabolite + "(e)"
diet_Infant_formula.reset_index(inplace=True)
diet_Infant_formula["reaction"] = "EX_" + diet_Infant_formula.metabolite + "(e)"

#Adding information in our diet table
skeleton_Broccoli = pd.merge(diet_Broccoli, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Broccoli["global_id"] = skeleton_Broccoli.reaction
skeleton_Broccoli["reaction"] = "EX_" + skeleton_Broccoli.metabolite + "_m"
skeleton_Brussel = pd.merge(diet_Brussel, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Brussel["global_id"] = skeleton_Brussel.reaction
skeleton_Brussel["reaction"] = "EX_" + skeleton_Brussel.metabolite + "_m"
skeleton_Cabbage = pd.merge(diet_Cabbage, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Cabbage["global_id"] = skeleton_Cabbage.reaction
skeleton_Cabbage["reaction"] = "EX_" + skeleton_Cabbage.metabolite + "_m"
skeleton_Carrot = pd.merge(diet_Carrot, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Carrot["global_id"] = skeleton_Carrot.reaction
skeleton_Carrot["reaction"] = "EX_" + skeleton_Carrot.metabolite + "_m"
skeleton_Cauliflower = pd.merge(diet_Cauliflower, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Cauliflower["global_id"] = skeleton_Cauliflower.reaction
skeleton_Cauliflower["reaction"] = "EX_" + skeleton_Cauliflower.metabolite + "_m"
skeleton_Celery = pd.merge(diet_Celery, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Celery["global_id"] = skeleton_Celery.reaction
skeleton_Celery["reaction"] = "EX_" + skeleton_Celery.metabolite + "_m"
skeleton_Cucumber = pd.merge(diet_Cucumber, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Cucumber["global_id"] = skeleton_Cucumber.reaction
skeleton_Cucumber["reaction"] = "EX_" + skeleton_Cucumber.metabolite + "_m"
skeleton_Eggplant = pd.merge(diet_Eggplant, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Eggplant["global_id"] = skeleton_Eggplant.reaction
skeleton_Eggplant["reaction"] = "EX_" + skeleton_Eggplant.metabolite + "_m"
skeleton_Green_beans = pd.merge(diet_Green_beans, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Green_beans["global_id"] = skeleton_Green_beans.reaction
skeleton_Green_beans["reaction"] = "EX_" + skeleton_Green_beans.metabolite + "_m"
skeleton_Green_capsicum = pd.merge(diet_Green_capsicum, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Green_capsicum["global_id"] = skeleton_Green_capsicum.reaction
skeleton_Green_capsicum["reaction"] = "EX_" + skeleton_Green_capsicum.metabolite + "_m"
skeleton_Lettuce = pd.merge(diet_Lettuce, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Lettuce["global_id"] = skeleton_Lettuce.reaction
skeleton_Lettuce["reaction"] = "EX_" + skeleton_Lettuce.metabolite + "_m"
skeleton_Mushroom = pd.merge(diet_Mushroom, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Mushroom["global_id"] = skeleton_Mushroom.reaction
skeleton_Mushroom["reaction"] = "EX_" + skeleton_Mushroom.metabolite + "_m"
skeleton_Onion = pd.merge(diet_Onion, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Onion["global_id"] = skeleton_Onion.reaction
skeleton_Onion["reaction"] = "EX_" + skeleton_Onion.metabolite + "_m"
skeleton_Pak_choi = pd.merge(diet_Pak_choi, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Pak_choi["global_id"] = skeleton_Pak_choi.reaction
skeleton_Pak_choi["reaction"] = "EX_" + skeleton_Pak_choi.metabolite + "_m"
skeleton_Potato = pd.merge(diet_Potato, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Potato["global_id"] = skeleton_Potato.reaction
skeleton_Potato["reaction"] = "EX_" + skeleton_Potato.metabolite + "_m"
skeleton_Pumpkin = pd.merge(diet_Pumpkin, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Pumpkin["global_id"] = skeleton_Pumpkin.reaction
skeleton_Pumpkin["reaction"] = "EX_" + skeleton_Pumpkin.metabolite + "_m"
skeleton_Sweetcorn = pd.merge(diet_Sweetcorn, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Sweetcorn["global_id"] = skeleton_Sweetcorn.reaction
skeleton_Sweetcorn["reaction"] = "EX_" + skeleton_Sweetcorn.metabolite + "_m"
skeleton_Spinach = pd.merge(diet_Spinach, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Spinach["global_id"] = skeleton_Spinach.reaction
skeleton_Spinach["reaction"] = "EX_" + skeleton_Spinach.metabolite + "_m"
skeleton_Squash = pd.merge(diet_Squash, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Squash["global_id"] = skeleton_Squash.reaction
skeleton_Squash["reaction"] = "EX_" + skeleton_Squash.metabolite + "_m"
skeleton_Sweet_potato = pd.merge(diet_Sweet_potato, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Sweet_potato["global_id"] = skeleton_Sweet_potato.reaction
skeleton_Sweet_potato["reaction"] = "EX_" + skeleton_Sweet_potato.metabolite + "_m"
skeleton_Tomato = pd.merge(diet_Tomato, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Tomato["global_id"] = skeleton_Tomato.reaction
skeleton_Tomato["reaction"] = "EX_" + skeleton_Tomato.metabolite + "_m"
skeleton_Yam = pd.merge(diet_Yam, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Yam["global_id"] = skeleton_Yam.reaction
skeleton_Yam["reaction"] = "EX_" + skeleton_Yam.metabolite + "_m"
skeleton_Zucchini = pd.merge(diet_Zucchini, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Zucchini["global_id"] = skeleton_Zucchini.reaction
skeleton_Zucchini["reaction"] = "EX_" + skeleton_Zucchini.metabolite + "_m"
skeleton_Apple = pd.merge(diet_Apple, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Apple["global_id"] = skeleton_Apple.reaction
skeleton_Apple["reaction"] = "EX_" + skeleton_Apple.metabolite + "_m"
skeleton_Banana = pd.merge(diet_Banana, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Banana["global_id"] = skeleton_Banana.reaction
skeleton_Banana["reaction"] = "EX_" + skeleton_Banana.metabolite + "_m"
skeleton_Blackcurrant = pd.merge(diet_Blackcurrant, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Blackcurrant["global_id"] = skeleton_Blackcurrant.reaction
skeleton_Blackcurrant["reaction"] = "EX_" + skeleton_Blackcurrant.metabolite + "_m"
skeleton_Blueberries = pd.merge(diet_Blueberries, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Blueberries["global_id"] = skeleton_Blueberries.reaction
skeleton_Blueberries["reaction"] = "EX_" + skeleton_Blueberries.metabolite + "_m"
skeleton_Cherry = pd.merge(diet_Cherry, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Cherry["global_id"] = skeleton_Cherry.reaction
skeleton_Cherry["reaction"] = "EX_" + skeleton_Cherry.metabolite + "_m"
skeleton_Feijoa = pd.merge(diet_Feijoa, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Feijoa["global_id"] = skeleton_Feijoa.reaction
skeleton_Feijoa["reaction"] = "EX_" + skeleton_Feijoa.metabolite + "_m"
skeleton_Gold_kiwifruit = pd.merge(diet_Gold_kiwifruit, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Gold_kiwifruit["global_id"] = skeleton_Gold_kiwifruit.reaction
skeleton_Gold_kiwifruit["reaction"] = "EX_" + skeleton_Gold_kiwifruit.metabolite + "_m"
skeleton_Grape = pd.merge(diet_Grape, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Grape["global_id"] = skeleton_Grape.reaction
skeleton_Grape["reaction"] = "EX_" + skeleton_Grape.metabolite + "_m"
skeleton_Grapefruit = pd.merge(diet_Grapefruit, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Grapefruit["global_id"] = skeleton_Grapefruit.reaction
skeleton_Grapefruit["reaction"] = "EX_" + skeleton_Grapefruit.metabolite + "_m"
skeleton_Green_kiwifruit = pd.merge(diet_Green_kiwifruit, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Green_kiwifruit["global_id"] = skeleton_Green_kiwifruit.reaction
skeleton_Green_kiwifruit["reaction"] = "EX_" + skeleton_Green_kiwifruit.metabolite + "_m"
skeleton_Mandarin = pd.merge(diet_Mandarin, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Mandarin["global_id"] = skeleton_Mandarin.reaction
skeleton_Mandarin["reaction"] = "EX_" + skeleton_Mandarin.metabolite + "_m"
skeleton_Mango = pd.merge(diet_Mango, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Mango["global_id"] = skeleton_Mango.reaction
skeleton_Mango["reaction"] = "EX_" + skeleton_Mango.metabolite + "_m"
skeleton_Melon = pd.merge(diet_Melon, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Melon["global_id"] = skeleton_Melon.reaction
skeleton_Melon["reaction"] = "EX_" + skeleton_Melon.metabolite + "_m"
skeleton_Nectarine = pd.merge(diet_Nectarine, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Nectarine["global_id"] = skeleton_Nectarine.reaction
skeleton_Nectarine["reaction"] = "EX_" + skeleton_Nectarine.metabolite + "_m"
skeleton_Orange = pd.merge(diet_Orange, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Orange["global_id"] = skeleton_Orange.reaction
skeleton_Orange["reaction"] = "EX_" + skeleton_Orange.metabolite + "_m"
skeleton_Peache = pd.merge(diet_Peache, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Peache["global_id"] = skeleton_Peache.reaction
skeleton_Peache["reaction"] = "EX_" + skeleton_Peache.metabolite + "_m"
skeleton_Pear = pd.merge(diet_Pear, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Pear["global_id"] = skeleton_Pear.reaction
skeleton_Pear["reaction"] = "EX_" + skeleton_Pear.metabolite + "_m"
skeleton_Pineapple = pd.merge(diet_Pineapple, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Pineapple["global_id"] = skeleton_Pineapple.reaction
skeleton_Pineapple["reaction"] = "EX_" + skeleton_Pineapple.metabolite + "_m"
skeleton_Plum = pd.merge(diet_Plum, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Plum["global_id"] = skeleton_Plum.reaction
skeleton_Plum["reaction"] = "EX_" + skeleton_Plum.metabolite + "_m"
skeleton_Raspberries = pd.merge(diet_Raspberries, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Raspberries["global_id"] = skeleton_Raspberries.reaction
skeleton_Raspberries["reaction"] = "EX_" + skeleton_Raspberries.metabolite + "_m"
skeleton_Strawberries = pd.merge(diet_Strawberries, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Strawberries["global_id"] = skeleton_Strawberries.reaction
skeleton_Strawberries["reaction"] = "EX_" + skeleton_Strawberries.metabolite + "_m"
skeleton_Barley = pd.merge(diet_Barley, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Barley["global_id"] = skeleton_Barley.reaction
skeleton_Barley["reaction"] = "EX_" + skeleton_Barley.metabolite + "_m"
skeleton_Barley_cereal = pd.merge(diet_Barley_cereal, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Barley_cereal["global_id"] = skeleton_Barley_cereal.reaction
skeleton_Barley_cereal["reaction"] = "EX_" + skeleton_Barley_cereal.metabolite + "_m"
skeleton_Couscous = pd.merge(diet_Couscous, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Couscous["global_id"] = skeleton_Couscous.reaction
skeleton_Couscous["reaction"] = "EX_" + skeleton_Couscous.metabolite + "_m"
skeleton_Noodles = pd.merge(diet_Noodles, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Noodles["global_id"] = skeleton_Noodles.reaction
skeleton_Noodles["reaction"] = "EX_" + skeleton_Noodles.metabolite + "_m"
skeleton_Oat_cereal = pd.merge(diet_Oat_cereal, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Oat_cereal["global_id"] = skeleton_Oat_cereal.reaction
skeleton_Oat_cereal["reaction"] = "EX_" + skeleton_Oat_cereal.metabolite + "_m"
skeleton_Pasta = pd.merge(diet_Pasta, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Pasta["global_id"] = skeleton_Pasta.reaction
skeleton_Pasta["reaction"] = "EX_" + skeleton_Pasta.metabolite + "_m"
skeleton_Rice = pd.merge(diet_Rice, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Rice["global_id"] = skeleton_Rice.reaction
skeleton_Rice["reaction"] = "EX_" + skeleton_Rice.metabolite + "_m"
skeleton_Rice_cereal = pd.merge(diet_Rice_cereal, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Rice_cereal["global_id"] = skeleton_Rice_cereal.reaction
skeleton_Rice_cereal["reaction"] = "EX_" + skeleton_Rice_cereal.metabolite + "_m"
skeleton_Tapioca_pudding = pd.merge(diet_Tapioca_pudding, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Tapioca_pudding["global_id"] = skeleton_Tapioca_pudding.reaction
skeleton_Tapioca_pudding["reaction"] = "EX_" + skeleton_Tapioca_pudding.metabolite + "_m"
skeleton_White_bread = pd.merge(diet_White_bread, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_White_bread["global_id"] = skeleton_White_bread.reaction
skeleton_White_bread["reaction"] = "EX_" + skeleton_White_bread.metabolite + "_m"
skeleton_Wholegrain_bread = pd.merge(diet_Wholegrain_bread, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Wholegrain_bread["global_id"] = skeleton_Wholegrain_bread.reaction
skeleton_Wholegrain_bread["reaction"] = "EX_" + skeleton_Wholegrain_bread.metabolite + "_m"
skeleton_Cottage_cheese = pd.merge(diet_Cottage_cheese, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Cottage_cheese["global_id"] = skeleton_Cottage_cheese.reaction
skeleton_Cottage_cheese["reaction"] = "EX_" + skeleton_Cottage_cheese.metabolite + "_m"
skeleton_Eggs = pd.merge(diet_Eggs, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Eggs["global_id"] = skeleton_Eggs.reaction
skeleton_Eggs["reaction"] = "EX_" + skeleton_Eggs.metabolite + "_m"
skeleton_Mozzarella_cheese = pd.merge(diet_Mozzarella_cheese, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Mozzarella_cheese["global_id"] = skeleton_Mozzarella_cheese.reaction
skeleton_Mozzarella_cheese["reaction"] = "EX_" + skeleton_Mozzarella_cheese.metabolite + "_m"
skeleton_Soymilk = pd.merge(diet_Soymilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Soymilk["global_id"] = skeleton_Soymilk.reaction
skeleton_Soymilk["reaction"] = "EX_" + skeleton_Soymilk.metabolite + "_m"
skeleton_Tofu = pd.merge(diet_Tofu, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Tofu["global_id"] = skeleton_Tofu.reaction
skeleton_Tofu["reaction"] = "EX_" + skeleton_Tofu.metabolite + "_m"
skeleton_Whole_milk = pd.merge(diet_Whole_milk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Whole_milk["global_id"] = skeleton_Whole_milk.reaction
skeleton_Whole_milk["reaction"] = "EX_" + skeleton_Whole_milk.metabolite + "_m"
skeleton_Yoghurt = pd.merge(diet_Yoghurt, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Yoghurt["global_id"] = skeleton_Yoghurt.reaction
skeleton_Yoghurt["reaction"] = "EX_" + skeleton_Yoghurt.metabolite + "_m"
skeleton_Beef = pd.merge(diet_Beef, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Beef["global_id"] = skeleton_Beef.reaction
skeleton_Beef["reaction"] = "EX_" + skeleton_Beef.metabolite + "_m"
skeleton_Chicken = pd.merge(diet_Chicken, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Chicken["global_id"] = skeleton_Chicken.reaction
skeleton_Chicken["reaction"] = "EX_" + skeleton_Chicken.metabolite + "_m"
skeleton_Codfish = pd.merge(diet_Codfish, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Codfish["global_id"] = skeleton_Codfish.reaction
skeleton_Codfish["reaction"] = "EX_" + skeleton_Codfish.metabolite + "_m"
skeleton_Lamb = pd.merge(diet_Lamb, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Lamb["global_id"] = skeleton_Lamb.reaction
skeleton_Lamb["reaction"] = "EX_" + skeleton_Lamb.metabolite + "_m"
skeleton_Mackerel = pd.merge(diet_Mackerel, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Mackerel["global_id"] = skeleton_Mackerel.reaction
skeleton_Mackerel["reaction"] = "EX_" + skeleton_Mackerel.metabolite + "_m"
skeleton_Mussels = pd.merge(diet_Mussels, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Mussels["global_id"] = skeleton_Mussels.reaction
skeleton_Mussels["reaction"] = "EX_" + skeleton_Mussels.metabolite + "_m"
skeleton_Pork = pd.merge(diet_Pork, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Pork["global_id"] = skeleton_Pork.reaction
skeleton_Pork["reaction"] = "EX_" + skeleton_Pork.metabolite + "_m"
skeleton_Salmon = pd.merge(diet_Salmon, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Salmon["global_id"] = skeleton_Salmon.reaction
skeleton_Salmon["reaction"] = "EX_" + skeleton_Salmon.metabolite + "_m"
skeleton_Shrimp = pd.merge(diet_Shrimp, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Shrimp["global_id"] = skeleton_Shrimp.reaction
skeleton_Shrimp["reaction"] = "EX_" + skeleton_Shrimp.metabolite + "_m"
skeleton_Tuna = pd.merge(diet_Tuna, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Tuna["global_id"] = skeleton_Tuna.reaction
skeleton_Tuna["reaction"] = "EX_" + skeleton_Tuna.metabolite + "_m"
skeleton_Turkey = pd.merge(diet_Turkey, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Turkey["global_id"] = skeleton_Turkey.reaction
skeleton_Turkey["reaction"] = "EX_" + skeleton_Turkey.metabolite + "_m"
skeleton_Almond = pd.merge(diet_Almond, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Almond["global_id"] = skeleton_Almond.reaction
skeleton_Almond["reaction"] = "EX_" + skeleton_Almond.metabolite + "_m"
skeleton_Black_beans = pd.merge(diet_Black_beans, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Black_beans["global_id"] = skeleton_Black_beans.reaction
skeleton_Black_beans["reaction"] = "EX_" + skeleton_Black_beans.metabolite + "_m"
skeleton_Cashew = pd.merge(diet_Cashew, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Cashew["global_id"] = skeleton_Cashew.reaction
skeleton_Cashew["reaction"] = "EX_" + skeleton_Cashew.metabolite + "_m"
skeleton_Chia = pd.merge(diet_Chia, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Chia["global_id"] = skeleton_Chia.reaction
skeleton_Chia["reaction"] = "EX_" + skeleton_Chia.metabolite + "_m"
skeleton_Chickpea = pd.merge(diet_Chickpea, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Chickpea["global_id"] = skeleton_Chickpea.reaction
skeleton_Chickpea["reaction"] = "EX_" + skeleton_Chickpea.metabolite + "_m"
skeleton_Green_peas = pd.merge(diet_Green_peas, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Green_peas["global_id"] = skeleton_Green_peas.reaction
skeleton_Green_peas["reaction"] = "EX_" + skeleton_Green_peas.metabolite + "_m"
skeleton_Hazelnut = pd.merge(diet_Hazelnut, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Hazelnut["global_id"] = skeleton_Hazelnut.reaction
skeleton_Hazelnut["reaction"] = "EX_" + skeleton_Hazelnut.metabolite + "_m"
skeleton_Lentils = pd.merge(diet_Lentils, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Lentils["global_id"] = skeleton_Lentils.reaction
skeleton_Lentils["reaction"] = "EX_" + skeleton_Lentils.metabolite + "_m"
skeleton_Peanut = pd.merge(diet_Peanut, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Peanut["global_id"] = skeleton_Peanut.reaction
skeleton_Peanut["reaction"] = "EX_" + skeleton_Peanut.metabolite + "_m"
skeleton_Pecans = pd.merge(diet_Pecans, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Pecans["global_id"] = skeleton_Pecans.reaction
skeleton_Pecans["reaction"] = "EX_" + skeleton_Pecans.metabolite + "_m"
skeleton_Pumpkin_seed = pd.merge(diet_Pumpkin_seed, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Pumpkin_seed["global_id"] = skeleton_Pumpkin_seed.reaction
skeleton_Pumpkin_seed["reaction"] = "EX_" + skeleton_Pumpkin_seed.metabolite + "_m"
skeleton_Red_beans = pd.merge(diet_Red_beans, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Red_beans["global_id"] = skeleton_Red_beans.reaction
skeleton_Red_beans["reaction"] = "EX_" + skeleton_Red_beans.metabolite + "_m"
skeleton_Soybean = pd.merge(diet_Soybean, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Soybean["global_id"] = skeleton_Soybean.reaction
skeleton_Soybean["reaction"] = "EX_" + skeleton_Soybean.metabolite + "_m"
skeleton_Split_peas = pd.merge(diet_Split_peas, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Split_peas["global_id"] = skeleton_Split_peas.reaction
skeleton_Split_peas["reaction"] = "EX_" + skeleton_Split_peas.metabolite + "_m"
skeleton_Sunflower_seed = pd.merge(diet_Sunflower_seed, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Sunflower_seed["global_id"] = skeleton_Sunflower_seed.reaction
skeleton_Sunflower_seed["reaction"] = "EX_" + skeleton_Sunflower_seed.metabolite + "_m"
skeleton_White_beans = pd.merge(diet_White_beans, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_White_beans["global_id"] = skeleton_White_beans.reaction
skeleton_White_beans["reaction"] = "EX_" + skeleton_White_beans.metabolite + "_m"
skeleton_Breastmilk = pd.merge(diet_Breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Breastmilk["global_id"] = skeleton_Breastmilk.reaction
skeleton_Breastmilk["reaction"] = "EX_" + skeleton_Breastmilk.metabolite + "_m"
skeleton_Infant_formula = pd.merge(diet_Infant_formula, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Infant_formula["global_id"] = skeleton_Infant_formula.reaction
skeleton_Infant_formula["reaction"] = "EX_" + skeleton_Infant_formula.metabolite + "_m"

#Supplementing the medium with essential nutrietns for microbial growth
from micom.workflows.db_media import complete_db_medium

manifest_Broccoli, imports_Broccoli = complete_db_medium("data/agora201__species.qza", skeleton_Broccoli, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Brussel, imports_Brussel = complete_db_medium("data/agora201__species.qza", skeleton_Brussel, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Cabbage, imports_Cabbage = complete_db_medium("data/agora201__species.qza", skeleton_Cabbage, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Carrot, imports_Carrot = complete_db_medium("data/agora201__species.qza", skeleton_Carrot, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Cauliflower, imports_Cauliflower = complete_db_medium("data/agora201__species.qza", skeleton_Cauliflower, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Celery, imports_Celery = complete_db_medium("data/agora201__species.qza", skeleton_Celery, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Cucumber, imports_Cucumber = complete_db_medium("data/agora201__species.qza", skeleton_Cucumber, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Eggplant, imports_Eggplant = complete_db_medium("data/agora201__species.qza", skeleton_Eggplant, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Green_beans, imports_Green_beans = complete_db_medium("data/agora201__species.qza", skeleton_Green_beans, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Green_capsicum, imports_Green_capsicum = complete_db_medium("data/agora201__species.qza", skeleton_Green_capsicum, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Lettuce, imports_Lettuce = complete_db_medium("data/agora201__species.qza", skeleton_Lettuce, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Mushroom, imports_Mushroom = complete_db_medium("data/agora201__species.qza", skeleton_Mushroom, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Onion, imports_Onion = complete_db_medium("data/agora201__species.qza", skeleton_Onion, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Pak_choi, imports_Pak_choi = complete_db_medium("data/agora201__species.qza", skeleton_Pak_choi, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Potato, imports_Potato = complete_db_medium("data/agora201__species.qza", skeleton_Potato, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Pumpkin, importsPumpkin = complete_db_medium("data/agora201__species.qza", skeleton_Pumpkin, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Sweetcorn, imports_Sweetcorn = complete_db_medium("data/agora201__species.qza", skeleton_Sweetcorn, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Spinach, imports_Spinach = complete_db_medium("data/agora201__species.qza", skeleton_Spinach, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Squash, imports_Squash = complete_db_medium("data/agora201__species.qza", skeleton_Squash, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Sweet_potato, imports_Sweet_potato = complete_db_medium("data/agora201__species.qza", skeleton_Sweet_potato, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Tomato, imports_Tomato = complete_db_medium("data/agora201__species.qza", skeleton_Tomato, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Yam, imports_Yam = complete_db_medium("data/agora201__species.qza", skeleton_Yam, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Zucchini, imports_Zucchini = complete_db_medium("data/agora201__species.qza", skeleton_Zucchini, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Apple, imports_Apple = complete_db_medium("data/agora201__species.qza", skeleton_Apple, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Banana, imports_Banana = complete_db_medium("data/agora201__species.qza", skeleton_Banana, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Blackcurrant, imports_Blackcurrant = complete_db_medium("data/agora201__species.qza", skeleton_Blackcurrant, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Blueberries, imports_Blueberries = complete_db_medium("data/agora201__species.qza", skeleton_Blueberries, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Cherry, imports_Cherry = complete_db_medium("data/agora201__species.qza", skeleton_Cherry, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Feijoa, imports_Feijoa = complete_db_medium("data/agora201__species.qza", skeleton_Feijoa, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Gold_kiwifruit, imports_Gold_kiwifruit = complete_db_medium("data/agora201__species.qza", skeleton_Gold_kiwifruit, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Grape, imports_Grape = complete_db_medium("data/agora201__species.qza", skeleton_Grape, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Grapefruit, imports_Grapefruit = complete_db_medium("data/agora201__species.qza", skeleton_Grapefruit, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Green_kiwifruit, imports_Green_kiwifruit = complete_db_medium("data/agora201__species.qza", skeleton_Green_kiwifruit, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Mandarin, imports_Mandarin = complete_db_medium("data/agora201__species.qza", skeleton_Mandarin, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Mango, imports_Mango = complete_db_medium("data/agora201__species.qza", skeleton_Mango, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Melon, imports_Melon = complete_db_medium("data/agora201__species.qza", skeleton_Melon, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Nectarine, imports_Nectarine = complete_db_medium("data/agora201__species.qza", skeleton_Nectarine, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Orange, imports_Orange = complete_db_medium("data/agora201__species.qza", skeleton_Orange, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Peache, imports_Peache = complete_db_medium("data/agora201__species.qza", skeleton_Peache, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Pear, imports_Pear = complete_db_medium("data/agora201__species.qza", skeleton_Pear, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Pineapple, imports_Pineapple = complete_db_medium("data/agora201__species.qza", skeleton_Pineapple, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Plum, imports_Plum = complete_db_medium("data/agora201__species.qza", skeleton_Plum, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Raspberries, imports_Raspberries = complete_db_medium("data/agora201__species.qza", skeleton_Raspberries, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Strawberries, imports_Strawberries = complete_db_medium("data/agora201__species.qza", skeleton_Strawberries, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Barley, imports_Barley = complete_db_medium("data/agora201__species.qza", skeleton_Barley, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Barley_cereal, imports_Barley_cereal = complete_db_medium("data/agora201__species.qza", skeleton_Barley_cereal, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Couscous, imports_Couscous = complete_db_medium("data/agora201__species.qza", skeleton_Couscous, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Noodles, imports_Noodles = complete_db_medium("data/agora201__species.qza", skeleton_Noodles, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Oat_cereal, imports_Oat_cereal = complete_db_medium("data/agora201__species.qza", skeleton_Oat_cereal, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Pasta, imports_Pasta = complete_db_medium("data/agora201__species.qza", skeleton_Pasta, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Rice, imports_Rice = complete_db_medium("data/agora201__species.qza", skeleton_Rice, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Rice_cereal, imports_Rice_cereal = complete_db_medium("data/agora201__species.qza", skeleton_Rice_cereal, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Tapioca_pudding, imports_Tapioca_pudding = complete_db_medium("data/agora201__species.qza", skeleton_Tapioca_pudding, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_White_bread, imports_White_bread = complete_db_medium("data/agora201__species.qza", skeleton_White_bread, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Wholegrain_bread, imports_Wholegrain_bread = complete_db_medium("data/agora201__species.qza", skeleton_Wholegrain_bread, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Cottage_cheese, imports_Cottage_cheese = complete_db_medium("data/agora201__species.qza", skeleton_Cottage_cheese, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Eggs, imports_Eggs = complete_db_medium("data/agora201__species.qza", skeleton_Eggs, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Mozzarella_cheese, imports_Mozzarella_cheese = complete_db_medium("data/agora201__species.qza", skeleton_Mozzarella_cheese, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Soymilk, imports_Soymilk = complete_db_medium("data/agora201__species.qza", skeleton_Soymilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Tofu, imports_Tofu = complete_db_medium("data/agora201__species.qza", skeleton_Tofu, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Whole_milk, imports_Whole_milk = complete_db_medium("data/agora201__species.qza", skeleton_Whole_milk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Yoghurt, imports_Yoghurt = complete_db_medium("data/agora201__species.qza", skeleton_Yoghurt, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Beef, imports_Beef = complete_db_medium("data/agora201__species.qza", skeleton_Beef, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Chicken, imports_Chicken = complete_db_medium("data/agora201__species.qza", skeleton_Chicken, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Codfish, imports_Codfish = complete_db_medium("data/agora201__species.qza", skeleton_Codfish, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Lamb, imports_Lamb = complete_db_medium("data/agora201__species.qza", skeleton_Lamb, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Mackerel, imports_Mackerel = complete_db_medium("data/agora201__species.qza", skeleton_Mackerel, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Mussels, imports_Mussels = complete_db_medium("data/agora201__species.qza", skeleton_Mussels, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Pork, imports_Pork = complete_db_medium("data/agora201__species.qza", skeleton_Pork, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Salmon, imports_Salmon = complete_db_medium("data/agora201__species.qza", skeleton_Salmon, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Shrimp, imports_Shrimp = complete_db_medium("data/agora201__species.qza", skeleton_Shrimp, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Tuna, imports_Tuna = complete_db_medium("data/agora201__species.qza", skeleton_Tuna, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Turkey, imports_Turkey = complete_db_medium("data/agora201__species.qza", skeleton_Turkey, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Almond, imports_Almond = complete_db_medium("data/agora201__species.qza", skeleton_Almond, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Black_beans, imports_Black_beans = complete_db_medium("data/agora201__species.qza", skeleton_Black_beans, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Cashew, imports_Cashew = complete_db_medium("data/agora201__species.qza", skeleton_Cashew, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Chia, imports_Chia = complete_db_medium("data/agora201__species.qza", skeleton_Chia, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Chickpea, imports_Chickpea = complete_db_medium("data/agora201__species.qza", skeleton_Chickpea, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Green_peas, imports_Green_peas = complete_db_medium("data/agora201__species.qza", skeleton_Green_peas, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Hazelnut, imports_Hazelnut = complete_db_medium("data/agora201__species.qza", skeleton_Hazelnut, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Lentils, imports_Lentils = complete_db_medium("data/agora201__species.qza", skeleton_Lentils, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Peanut, imports_Peanut = complete_db_medium("data/agora201__species.qza", skeleton_Peanut, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Pecans, imports_Pecans = complete_db_medium("data/agora201__species.qza", skeleton_Pecans, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Pumpkin_seed, imports_Pumpkin_seed = complete_db_medium("data/agora201__species.qza", skeleton_Pumpkin_seed, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Red_beans, imports_Red_beans = complete_db_medium("data/agora201__species.qza", skeleton_Red_beans, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Soybean, imports_Soybean = complete_db_medium("data/agora201__species.qza", skeleton_Soybean, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Split_peas, imports_Split_peas = complete_db_medium("data/agora201__species.qza", skeleton_Split_peas, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Sunflower_seed, imports_Sunflower_seed = complete_db_medium("data/agora201__species.qza", skeleton_Sunflower_seed, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_White_beans, imports_White_beans = complete_db_medium("data/agora201__species.qza", skeleton_White_beans, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Breastmilk, imports_Breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Infant_formula, imports_Infant_formula = complete_db_medium("data/agora201__species.qza", skeleton_Infant_formula, growth=0.01, threads=14, max_added_import=10, minimize_components=True)

manifest_Broccoli.can_grow.value_counts() #checking the microbial growth
filled_Broccoli = imports_Broccoli.max()
added_Broccoli = filled_Broccoli[~filled_Broccoli.index.isin(skeleton_Broccoli.reaction)] #fluxes that were added
manifest_Brussel.can_grow.value_counts() #checking the microbial growth
filled_Brussel = imports_Brussel.max()
added_Brussel = filled_Brussel[~filled_Brussel.index.isin(skeleton_Brussel.reaction)] #fluxes that were added
manifest_Cabbage.can_grow.value_counts() #checking the microbial growth
filled_Cabbage = imports_Cabbage.max()
added_Cabbage = filled_Cabbage[~filled_Cabbage.index.isin(skeleton_Cabbage.reaction)] #fluxes that were added
manifest_Carrot.can_grow.value_counts() #checking the microbial growth
filled_Carrot = imports_Carrot.max()
added_Carrot = filled_Carrot[~filled_Carrot.index.isin(skeleton_Carrot.reaction)] #fluxes that were added
manifest_Cauliflower.can_grow.value_counts() #checking the microbial growth
filled_Cauliflower = imports_Cauliflower.max()
added_Cauliflower = filled_Cauliflower[~filled_Cauliflower.index.isin(skeleton_Cauliflower.reaction)] #fluxes that were added
manifest_Celery.can_grow.value_counts() #checking the microbial growth
filled_Celery = imports_Celery.max()
added_Celery = filled_Celery[~filled_Celery.index.isin(skeleton_Celery.reaction)] #fluxes that were added
manifest_Cucumber.can_grow.value_counts() #checking the microbial growth
filled_Cucumber = imports_Cucumber.max()
added_Cucumber = filled_Cucumber[~filled_Cucumber.index.isin(skeleton_Cucumber.reaction)] #fluxes that were added
manifest_Eggplant.can_grow.value_counts() #checking the microbial growth
filled_Eggplant = imports_Eggplant.max()
added_Eggplant = filled_Eggplant[~filled_Eggplant.index.isin(skeleton_Eggplant.reaction)] #fluxes that were added
manifest_Green_beans.can_grow.value_counts() #checking the microbial growth
filled_Green_beans = imports_Green_beans.max()
added_Green_beans = filled_Green_beans[~filled_Green_beans.index.isin(skeleton_Green_beans.reaction)] #fluxes that were added
manifest_Green_capsicum.can_grow.value_counts() #checking the microbial growth
filled_Green_capsicum = imports_Green_capsicum.max()
added_Green_capsicum = filled_Green_capsicum[~filled_Green_capsicum.index.isin(skeleton_Green_capsicum.reaction)] #fluxes that were added
manifest_Lettuce.can_grow.value_counts() #checking the microbial growth
filled_Lettuce = imports_Lettuce.max()
added_Lettuce = filled_Lettuce[~filled_Lettuce.index.isin(skeleton_Lettuce.reaction)] #fluxes that were added
manifest_Mushroom.can_grow.value_counts() #checking the microbial growth
filled_Mushroom = imports_Mushroom.max()
added_Mushroom = filled_Mushroom[~filled_Mushroom.index.isin(skeleton_Mushroom.reaction)] #fluxes that were added
manifest_Onion.can_grow.value_counts() #checking the microbial growth
filled_Onion = imports_Onion.max()
added_Onion = filled_Onion[~filled_Onion.index.isin(skeleton_Onion.reaction)] #fluxes that were added
manifest_Pak_choi.can_grow.value_counts() #checking the microbial growth
filled_Pak_choi = imports_Pak_choi.max()
added_Pak_choi = filled_Pak_choi[~filled_Pak_choi.index.isin(skeleton_Pak_choi.reaction)] #fluxes that were added
manifest_Potato.can_grow.value_counts() #checking the microbial growth
filled_Potato = imports_Potato.max()
added_Potato = filled_Potato[~filled_Potato.index.isin(skeleton_Potato.reaction)] #fluxes that were added
manifest_Pumpkin.can_grow.value_counts() #checking the microbial growth
filled_Pumpkin = importsPumpkin.max()
addedPumpkin = filled_Pumpkin[~filled_Pumpkin.index.isin(skeleton_Pumpkin.reaction)] #fluxes that were added
manifest_Sweetcorn.can_grow.value_counts() #checking the microbial growth
filled_Sweetcorn = imports_Sweetcorn.max()
added_Sweetcorn = filled_Sweetcorn[~filled_Sweetcorn.index.isin(skeleton_Sweetcorn.reaction)] #fluxes that were added
manifest_Spinach.can_grow.value_counts() #checking the microbial growth
filled_Spinach = imports_Spinach.max()
added_Spinach = filled_Spinach[~filled_Spinach.index.isin(skeleton_Spinach.reaction)] #fluxes that were added
manifest_Squash.can_grow.value_counts() #checking the microbial growth
filled_Squash = imports_Squash.max()
added_Squash = filled_Squash[~filled_Squash.index.isin(skeleton_Squash.reaction)] #fluxes that were added
manifest_Sweet_potato.can_grow.value_counts() #checking the microbial growth
filled_Sweet_potato = imports_Sweet_potato.max()
added_Sweet_potato = filled_Sweet_potato[~filled_Sweet_potato.index.isin(skeleton_Sweet_potato.reaction)] #fluxes that were added
manifest_Tomato.can_grow.value_counts() #checking the microbial growth
filled_Tomato = imports_Tomato.max()
added_Tomato = filled_Tomato[~filled_Tomato.index.isin(skeleton_Tomato.reaction)] #fluxes that were added
manifest_Yam.can_grow.value_counts() #checking the microbial growth
filled_Yam = imports_Yam.max()
added_Yam = filled_Yam[~filled_Yam.index.isin(skeleton_Yam.reaction)] #fluxes that were added
manifest_Zucchini.can_grow.value_counts() #checking the microbial growth
filled_Zucchini = imports_Zucchini.max()
added_Zucchini = filled_Zucchini[~filled_Zucchini.index.isin(skeleton_Zucchini.reaction)] #fluxes that were added
manifest_Apple.can_grow.value_counts() #checking the microbial growth
filled_Apple = imports_Apple.max()
added_Apple = filled_Apple[~filled_Apple.index.isin(skeleton_Apple.reaction)] #fluxes that were added
manifest_Banana.can_grow.value_counts() #checking the microbial growth
filled_Banana = imports_Banana.max()
added_Banana = filled_Banana[~filled_Banana.index.isin(skeleton_Banana.reaction)] #fluxes that were added
manifest_Blackcurrant.can_grow.value_counts() #checking the microbial growth
filled_Blackcurrant = imports_Blackcurrant.max()
added_Blackcurrant = filled_Blackcurrant[~filled_Blackcurrant.index.isin(skeleton_Blackcurrant.reaction)] #fluxes that were added
manifest_Blueberries.can_grow.value_counts() #checking the microbial growth
filled_Blueberries = imports_Blueberries.max()
added_Blueberries = filled_Blueberries[~filled_Blueberries.index.isin(skeleton_Blueberries.reaction)] #fluxes that were added
manifest_Cherry.can_grow.value_counts() #checking the microbial growth
filled_Cherry = imports_Cherry.max()
added_Cherry = filled_Cherry[~filled_Cherry.index.isin(skeleton_Cherry.reaction)] #fluxes that were added
manifest_Feijoa.can_grow.value_counts() #checking the microbial growth
filled_Feijoa = imports_Feijoa.max()
added_Feijoa = filled_Feijoa[~filled_Feijoa.index.isin(skeleton_Feijoa.reaction)] #fluxes that were added
manifest_Gold_kiwifruit.can_grow.value_counts() #checking the microbial growth
filled_Gold_kiwifruit = imports_Gold_kiwifruit.max()
added_Gold_kiwifruit = filled_Gold_kiwifruit[~filled_Gold_kiwifruit.index.isin(skeleton_Gold_kiwifruit.reaction)] #fluxes that were added
manifest_Grape.can_grow.value_counts() #checking the microbial growth
filled_Grape = imports_Grape.max()
added_Grape = filled_Grape[~filled_Grape.index.isin(skeleton_Grape.reaction)] #fluxes that were added
manifest_Grapefruit.can_grow.value_counts() #checking the microbial growth
filled_Grapefruit = imports_Grapefruit.max()
added_Grapefruit = filled_Grapefruit[~filled_Grapefruit.index.isin(skeleton_Grapefruit.reaction)] #fluxes that were added
manifest_Green_kiwifruit.can_grow.value_counts() #checking the microbial growth
filled_Green_kiwifruit = imports_Green_kiwifruit.max()
added_Green_kiwifruit = filled_Green_kiwifruit[~filled_Green_kiwifruit.index.isin(skeleton_Green_kiwifruit.reaction)] #fluxes that were added
manifest_Mandarin.can_grow.value_counts() #checking the microbial growth
filled_Mandarin = imports_Mandarin.max()
added_Mandarin = filled_Mandarin[~filled_Mandarin.index.isin(skeleton_Mandarin.reaction)] #fluxes that were added
manifest_Mango.can_grow.value_counts() #checking the microbial growth
filled_Mango = imports_Mango.max()
added_Mango = filled_Mango[~filled_Mango.index.isin(skeleton_Mango.reaction)] #fluxes that were added
manifest_Melon.can_grow.value_counts() #checking the microbial growth
filled_Melon = imports_Melon.max()
added_Melon = filled_Melon[~filled_Melon.index.isin(skeleton_Melon.reaction)] #fluxes that were added
manifest_Nectarine.can_grow.value_counts() #checking the microbial growth
filled_Nectarine = imports_Nectarine.max()
added_Nectarine = filled_Nectarine[~filled_Nectarine.index.isin(skeleton_Nectarine.reaction)] #fluxes that were added
manifest_Orange.can_grow.value_counts() #checking the microbial growth
filled_Orange = imports_Orange.max()
added_Orange = filled_Orange[~filled_Orange.index.isin(skeleton_Orange.reaction)] #fluxes that were added
manifest_Peache.can_grow.value_counts() #checking the microbial growth
filled_Peache = imports_Peache.max()
added_Peache = filled_Peache[~filled_Peache.index.isin(skeleton_Peache.reaction)] #fluxes that were added
manifest_Pear.can_grow.value_counts() #checking the microbial growth
filled_Pear = imports_Pear.max()
added_Pear = filled_Pear[~filled_Pear.index.isin(skeleton_Pear.reaction)] #fluxes that were added
manifest_Pineapple.can_grow.value_counts() #checking the microbial growth
filled_Pineapple = imports_Pineapple.max()
added_Pineapple = filled_Pineapple[~filled_Pineapple.index.isin(skeleton_Pineapple.reaction)] #fluxes that were added
manifest_Plum.can_grow.value_counts() #checking the microbial growth
filled_Plum = imports_Plum.max()
added_Plum = filled_Plum[~filled_Plum.index.isin(skeleton_Plum.reaction)] #fluxes that were added
manifest_Raspberries.can_grow.value_counts() #checking the microbial growth
filled_Raspberries = imports_Raspberries.max()
added_Raspberries = filled_Raspberries[~filled_Raspberries.index.isin(skeleton_Raspberries.reaction)] #fluxes that were added
manifest_Strawberries.can_grow.value_counts() #checking the microbial growth
filled_Strawberries = imports_Strawberries.max()
added_Strawberries = filled_Strawberries[~filled_Strawberries.index.isin(skeleton_Strawberries.reaction)] #fluxes that were added
manifest_Barley.can_grow.value_counts() #checking the microbial growth
filled_Barley = imports_Barley.max()
added_Barley = filled_Barley[~filled_Barley.index.isin(skeleton_Barley.reaction)] #fluxes that were added
manifest_Barley_cereal.can_grow.value_counts() #checking the microbial growth
filled_Barley_cereal = imports_Barley_cereal.max()
added_Barley_cereal = filled_Barley_cereal[~filled_Barley_cereal.index.isin(skeleton_Barley_cereal.reaction)] #fluxes that were added
manifest_Couscous.can_grow.value_counts() #checking the microbial growth
filled_Couscous = imports_Couscous.max()
added_Couscous = filled_Couscous[~filled_Couscous.index.isin(skeleton_Couscous.reaction)] #fluxes that were added
manifest_Noodles.can_grow.value_counts() #checking the microbial growth
filled_Noodles = imports_Noodles.max()
added_Noodles = filled_Noodles[~filled_Noodles.index.isin(skeleton_Noodles.reaction)] #fluxes that were added
manifest_Oat_cereal.can_grow.value_counts() #checking the microbial growth
filled_Oat_cereal = imports_Oat_cereal.max()
added_Oat_cereal = filled_Oat_cereal[~filled_Oat_cereal.index.isin(skeleton_Oat_cereal.reaction)] #fluxes that were added
manifest_Pasta.can_grow.value_counts() #checking the microbial growth
filled_Pasta = imports_Pasta.max()
added_Pasta = filled_Pasta[~filled_Pasta.index.isin(skeleton_Pasta.reaction)] #fluxes that were added
manifest_Rice.can_grow.value_counts() #checking the microbial growth
filled_Rice = imports_Rice.max()
added_Rice = filled_Rice[~filled_Rice.index.isin(skeleton_Rice.reaction)] #fluxes that were added
manifest_Rice_cereal.can_grow.value_counts() #checking the microbial growth
filled_Rice_cereal = imports_Rice_cereal.max()
added_Rice_cereal = filled_Rice_cereal[~filled_Rice_cereal.index.isin(skeleton_Rice_cereal.reaction)] #fluxes that were added
manifest_Tapioca_pudding.can_grow.value_counts() #checking the microbial growth
filled_Tapioca_pudding = imports_Tapioca_pudding.max()
added_Tapioca_pudding = filled_Tapioca_pudding[~filled_Tapioca_pudding.index.isin(skeleton_Tapioca_pudding.reaction)] #fluxes that were added
manifest_White_bread.can_grow.value_counts() #checking the microbial growth
filled_White_bread = imports_White_bread.max()
added_White_bread = filled_White_bread[~filled_White_bread.index.isin(skeleton_White_bread.reaction)] #fluxes that were added
manifest_Wholegrain_bread.can_grow.value_counts() #checking the microbial growth
filled_Wholegrain_bread = imports_Wholegrain_bread.max()
added_Wholegrain_bread = filled_Wholegrain_bread[~filled_Wholegrain_bread.index.isin(skeleton_Wholegrain_bread.reaction)] #fluxes that were added
manifest_Cottage_cheese.can_grow.value_counts() #checking the microbial growth
filled_Cottage_cheese = imports_Cottage_cheese.max()
added_Cottage_cheese = filled_Cottage_cheese[~filled_Cottage_cheese.index.isin(skeleton_Cottage_cheese.reaction)] #fluxes that were added
manifest_Eggs.can_grow.value_counts() #checking the microbial growth
filled_Eggs = imports_Eggs.max()
added_Eggs = filled_Eggs[~filled_Eggs.index.isin(skeleton_Eggs.reaction)] #fluxes that were added
manifest_Mozzarella_cheese.can_grow.value_counts() #checking the microbial growth
filled_Mozzarella_cheese = imports_Mozzarella_cheese.max()
added_Mozzarella_cheese = filled_Mozzarella_cheese[~filled_Mozzarella_cheese.index.isin(skeleton_Mozzarella_cheese.reaction)] #fluxes that were added
manifest_Soymilk.can_grow.value_counts() #checking the microbial growth
filled_Soymilk = imports_Soymilk.max()
added_Soymilk = filled_Soymilk[~filled_Soymilk.index.isin(skeleton_Soymilk.reaction)] #fluxes that were added
manifest_Tofu.can_grow.value_counts() #checking the microbial growth
filled_Tofu = imports_Tofu.max()
added_Tofu = filled_Tofu[~filled_Tofu.index.isin(skeleton_Tofu.reaction)] #fluxes that were added
manifest_Whole_milk.can_grow.value_counts() #checking the microbial growth
filled_Whole_milk = imports_Whole_milk.max()
added_Whole_milk = filled_Whole_milk[~filled_Whole_milk.index.isin(skeleton_Whole_milk.reaction)] #fluxes that were added
manifest_Yoghurt.can_grow.value_counts() #checking the microbial growth
filled_Yoghurt = imports_Yoghurt.max()
added_Yoghurt = filled_Yoghurt[~filled_Yoghurt.index.isin(skeleton_Yoghurt.reaction)] #fluxes that were added
manifest_Beef.can_grow.value_counts() #checking the microbial growth
filled_Beef = imports_Beef.max()
added_Beef = filled_Beef[~filled_Beef.index.isin(skeleton_Beef.reaction)] #fluxes that were added
manifest_Chicken.can_grow.value_counts() #checking the microbial growth
filled_Chicken = imports_Chicken.max()
added_Chicken = filled_Chicken[~filled_Chicken.index.isin(skeleton_Chicken.reaction)] #fluxes that were added
manifest_Codfish.can_grow.value_counts() #checking the microbial growth
filled_Codfish = imports_Codfish.max()
added_Codfish = filled_Codfish[~filled_Codfish.index.isin(skeleton_Codfish.reaction)] #fluxes that were added
manifest_Lamb.can_grow.value_counts() #checking the microbial growth
filled_Lamb = imports_Lamb.max()
added_Lamb = filled_Lamb[~filled_Lamb.index.isin(skeleton_Lamb.reaction)] #fluxes that were added
manifest_Mackerel.can_grow.value_counts() #checking the microbial growth
filled_Mackerel = imports_Mackerel.max()
added_Mackerel = filled_Mackerel[~filled_Mackerel.index.isin(skeleton_Mackerel.reaction)] #fluxes that were added
manifest_Mussels.can_grow.value_counts() #checking the microbial growth
filled_Mussels = imports_Mussels.max()
added_Mussels = filled_Mussels[~filled_Mussels.index.isin(skeleton_Mussels.reaction)] #fluxes that were added
manifest_Pork.can_grow.value_counts() #checking the microbial growth
filled_Pork = imports_Pork.max()
added_Pork = filled_Pork[~filled_Pork.index.isin(skeleton_Pork.reaction)] #fluxes that were added
manifest_Salmon.can_grow.value_counts() #checking the microbial growth
filled_Salmon = imports_Salmon.max()
added_Salmon = filled_Salmon[~filled_Salmon.index.isin(skeleton_Salmon.reaction)] #fluxes that were added
manifest_Shrimp.can_grow.value_counts() #checking the microbial growth
filled_Shrimp = imports_Shrimp.max()
added_Shrimp = filled_Shrimp[~filled_Shrimp.index.isin(skeleton_Shrimp.reaction)] #fluxes that were added
manifest_Tuna.can_grow.value_counts() #checking the microbial growth
filled_Tuna = imports_Tuna.max()
added_Tuna = filled_Tuna[~filled_Tuna.index.isin(skeleton_Tuna.reaction)] #fluxes that were added
manifest_Turkey.can_grow.value_counts() #checking the microbial growth
filled_Turkey = imports_Turkey.max()
added_Turkey = filled_Turkey[~filled_Turkey.index.isin(skeleton_Turkey.reaction)] #fluxes that were added
manifest_Almond.can_grow.value_counts() #checking the microbial growth
filled_Almond = imports_Almond.max()
added_Almond = filled_Almond[~filled_Almond.index.isin(skeleton_Almond.reaction)] #fluxes that were added
manifest_Black_beans.can_grow.value_counts() #checking the microbial growth
filled_Black_beans = imports_Black_beans.max()
added_Black_beans = filled_Black_beans[~filled_Black_beans.index.isin(skeleton_Black_beans.reaction)] #fluxes that were added
manifest_Cashew.can_grow.value_counts() #checking the microbial growth
filled_Cashew = imports_Cashew.max()
added_Cashew = filled_Cashew[~filled_Cashew.index.isin(skeleton_Cashew.reaction)] #fluxes that were added
manifest_Chia.can_grow.value_counts() #checking the microbial growth
filled_Chia = imports_Chia.max()
added_Chia = filled_Chia[~filled_Chia.index.isin(skeleton_Chia.reaction)] #fluxes that were added
manifest_Chickpea.can_grow.value_counts() #checking the microbial growth
filled_Chickpea = imports_Chickpea.max()
added_Chickpea = filled_Chickpea[~filled_Chickpea.index.isin(skeleton_Chickpea.reaction)] #fluxes that were added
manifest_Green_peas.can_grow.value_counts() #checking the microbial growth
filled_Green_peas = imports_Green_peas.max()
added_Green_peas = filled_Green_peas[~filled_Green_peas.index.isin(skeleton_Green_peas.reaction)] #fluxes that were added
manifest_Hazelnut.can_grow.value_counts() #checking the microbial growth
filled_Hazelnut = imports_Hazelnut.max()
added_Hazelnut = filled_Hazelnut[~filled_Hazelnut.index.isin(skeleton_Hazelnut.reaction)] #fluxes that were added
manifest_Lentils.can_grow.value_counts() #checking the microbial growth
filled_Lentils = imports_Lentils.max()
added_Lentils = filled_Lentils[~filled_Lentils.index.isin(skeleton_Lentils.reaction)] #fluxes that were added
manifest_Peanut.can_grow.value_counts() #checking the microbial growth
filled_Peanut = imports_Peanut.max()
added_Peanut = filled_Peanut[~filled_Peanut.index.isin(skeleton_Peanut.reaction)] #fluxes that were added
manifest_Pecans.can_grow.value_counts() #checking the microbial growth
filled_Pecans = imports_Pecans.max()
added_Pecans = filled_Pecans[~filled_Pecans.index.isin(skeleton_Pecans.reaction)] #fluxes that were added
manifest_Pumpkin_seed.can_grow.value_counts() #checking the microbial growth
filled_Pumpkin_seed = imports_Pumpkin_seed.max()
added_Pumpkin_seed = filled_Pumpkin_seed[~filled_Pumpkin_seed.index.isin(skeleton_Pumpkin_seed.reaction)] #fluxes that were added
manifest_Red_beans.can_grow.value_counts() #checking the microbial growth
filled_Red_beans = imports_Red_beans.max()
added_Red_beans = filled_Red_beans[~filled_Red_beans.index.isin(skeleton_Red_beans.reaction)] #fluxes that were added
manifest_Soybean.can_grow.value_counts() #checking the microbial growth
filled_Soybean = imports_Soybean.max()
added_Soybean = filled_Soybean[~filled_Soybean.index.isin(skeleton_Soybean.reaction)] #fluxes that were added
manifest_Split_peas.can_grow.value_counts() #checking the microbial growth
filled_Split_peas = imports_Split_peas.max()
added_Split_peas = filled_Split_peas[~filled_Split_peas.index.isin(skeleton_Split_peas.reaction)] #fluxes that were added
manifest_Sunflower_seed.can_grow.value_counts() #checking the microbial growth
filled_Sunflower_seed = imports_Sunflower_seed.max()
added_Sunflower_seed = filled_Sunflower_seed[~filled_Sunflower_seed.index.isin(skeleton_Sunflower_seed.reaction)] #fluxes that were added
manifest_White_beans.can_grow.value_counts() #checking the microbial growth
filled_White_beans = imports_White_beans.max()
added_White_beans = filled_White_beans[~filled_White_beans.index.isin(skeleton_White_beans.reaction)] #fluxes that were added
manifest_Breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Breastmilk = imports_Breastmilk.max()
added_Breastmilk = filled_Breastmilk[~filled_Breastmilk.index.isin(skeleton_Breastmilk.reaction)] #fluxes that were added
manifest_Infant_formula.can_grow.value_counts() #checking the microbial growth
filled_Infant_formula = imports_Infant_formula.max()
added_Infant_formula = filled_Infant_formula[~filled_Infant_formula.index.isin(skeleton_Infant_formula.reaction)] #fluxes that were added

#Assembling the final medium

added_df_Broccoli = added_Broccoli.reset_index() 
added_df_Broccoli.iloc[:, 0] = added_df_Broccoli.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Broccoli.columns = ["metabolite", "flux"]
added_df_Broccoli = pd.concat([skeleton_Broccoli[["metabolite", "flux"]], added_df_Broccoli])
added_df_Brussel = added_Brussel.reset_index() 
added_df_Brussel.iloc[:, 0] = added_df_Brussel.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Brussel.columns = ["metabolite", "flux"]
added_df_Brussel = pd.concat([skeleton_Brussel[["metabolite", "flux"]], added_df_Brussel])
added_df_Cabbage = added_Cabbage.reset_index() 
added_df_Cabbage.iloc[:, 0] = added_df_Cabbage.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Cabbage.columns = ["metabolite", "flux"]
added_df_Cabbage = pd.concat([skeleton_Cabbage[["metabolite", "flux"]], added_df_Cabbage])
added_df_Carrot = added_Carrot.reset_index() 
added_df_Carrot.iloc[:, 0] = added_df_Carrot.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Carrot.columns = ["metabolite", "flux"]
added_df_Carrot = pd.concat([skeleton_Carrot[["metabolite", "flux"]], added_df_Carrot])
added_df_Cauliflower = added_Cauliflower.reset_index() 
added_df_Cauliflower.iloc[:, 0] = added_df_Cauliflower.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Cauliflower.columns = ["metabolite", "flux"]
added_df_Cauliflower = pd.concat([skeleton_Cauliflower[["metabolite", "flux"]], added_df_Cauliflower])
added_df_Celery = added_Celery.reset_index() 
added_df_Celery.iloc[:, 0] = added_df_Celery.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Celery.columns = ["metabolite", "flux"]
added_df_Celery = pd.concat([skeleton_Celery[["metabolite", "flux"]], added_df_Celery])
added_df_Cucumber = added_Cucumber.reset_index() 
added_df_Cucumber.iloc[:, 0] = added_df_Cucumber.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Cucumber.columns = ["metabolite", "flux"]
added_df_Cucumber = pd.concat([skeleton_Cucumber[["metabolite", "flux"]], added_df_Cucumber])
added_df_Eggplant = added_Eggplant.reset_index() 
added_df_Eggplant.iloc[:, 0] = added_df_Eggplant.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Eggplant.columns = ["metabolite", "flux"]
added_df_Eggplant = pd.concat([skeleton_Eggplant[["metabolite", "flux"]], added_df_Eggplant])
added_df_Green_beans = added_Green_beans.reset_index() 
added_df_Green_beans.iloc[:, 0] = added_df_Green_beans.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Green_beans.columns = ["metabolite", "flux"]
added_df_Green_beans = pd.concat([skeleton_Green_beans[["metabolite", "flux"]], added_df_Green_beans])
added_df_Green_capsicum = added_Green_capsicum.reset_index() 
added_df_Green_capsicum.iloc[:, 0] = added_df_Green_capsicum.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Green_capsicum.columns = ["metabolite", "flux"]
added_df_Green_capsicum = pd.concat([skeleton_Green_capsicum[["metabolite", "flux"]], added_df_Green_capsicum])
added_df_Lettuce = added_Lettuce.reset_index() 
added_df_Lettuce.iloc[:, 0] = added_df_Lettuce.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Lettuce.columns = ["metabolite", "flux"]
added_df_Lettuce = pd.concat([skeleton_Lettuce[["metabolite", "flux"]], added_df_Lettuce])
added_df_Mushroom = added_Mushroom.reset_index() 
added_df_Mushroom.iloc[:, 0] = added_df_Mushroom.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Mushroom.columns = ["metabolite", "flux"]
added_df_Mushroom = pd.concat([skeleton_Mushroom[["metabolite", "flux"]], added_df_Mushroom])
added_df_Onion = added_Onion.reset_index() 
added_df_Onion.iloc[:, 0] = added_df_Onion.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Onion.columns = ["metabolite", "flux"]
added_df_Onion = pd.concat([skeleton_Onion[["metabolite", "flux"]], added_df_Onion])
added_df_Pak_choi = added_Pak_choi.reset_index() 
added_df_Pak_choi.iloc[:, 0] = added_df_Pak_choi.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Pak_choi.columns = ["metabolite", "flux"]
added_df_Pak_choi = pd.concat([skeleton_Pak_choi[["metabolite", "flux"]], added_df_Pak_choi])
added_df_Potato = added_Potato.reset_index() 
added_df_Potato.iloc[:, 0] = added_df_Potato.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Potato.columns = ["metabolite", "flux"]
added_df_Potato = pd.concat([skeleton_Potato[["metabolite", "flux"]], added_df_Potato])
added_df_Pumpkin = addedPumpkin.reset_index() 
added_df_Pumpkin.iloc[:, 0] = added_df_Pumpkin.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Pumpkin.columns = ["metabolite", "flux"]
added_df_Pumpkin = pd.concat([skeleton_Pumpkin[["metabolite", "flux"]], added_df_Pumpkin])
added_df_Sweetcorn = added_Sweetcorn.reset_index() 
added_df_Sweetcorn.iloc[:, 0] = added_df_Sweetcorn.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Sweetcorn.columns = ["metabolite", "flux"]
added_df_Sweetcorn = pd.concat([skeleton_Sweetcorn[["metabolite", "flux"]], added_df_Sweetcorn])
added_df_Spinach = added_Spinach.reset_index() 
added_df_Spinach.iloc[:, 0] = added_df_Spinach.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Spinach.columns = ["metabolite", "flux"]
added_df_Spinach = pd.concat([skeleton_Spinach[["metabolite", "flux"]], added_df_Spinach])
added_df_Squash = added_Squash.reset_index() 
added_df_Squash.iloc[:, 0] = added_df_Squash.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Squash.columns = ["metabolite", "flux"]
added_df_Squash = pd.concat([skeleton_Squash[["metabolite", "flux"]], added_df_Squash])
added_df_Sweet_potato = added_Sweet_potato.reset_index() 
added_df_Sweet_potato.iloc[:, 0] = added_df_Sweet_potato.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Sweet_potato.columns = ["metabolite", "flux"]
added_df_Sweet_potato = pd.concat([skeleton_Sweet_potato[["metabolite", "flux"]], added_df_Sweet_potato])
added_df_Tomato = added_Tomato.reset_index() 
added_df_Tomato.iloc[:, 0] = added_df_Tomato.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Tomato.columns = ["metabolite", "flux"]
added_df_Tomato = pd.concat([skeleton_Tomato[["metabolite", "flux"]], added_df_Tomato])
added_df_Yam = added_Yam.reset_index() 
added_df_Yam.iloc[:, 0] = added_df_Yam.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Yam.columns = ["metabolite", "flux"]
added_df_Yam = pd.concat([skeleton_Yam[["metabolite", "flux"]], added_df_Yam])
added_df_Zucchini = added_Zucchini.reset_index() 
added_df_Zucchini.iloc[:, 0] = added_df_Zucchini.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Zucchini.columns = ["metabolite", "flux"]
added_df_Zucchini = pd.concat([skeleton_Zucchini[["metabolite", "flux"]], added_df_Zucchini])
added_df_Apple = added_Apple.reset_index() 
added_df_Apple.iloc[:, 0] = added_df_Apple.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Apple.columns = ["metabolite", "flux"]
added_df_Apple = pd.concat([skeleton_Apple[["metabolite", "flux"]], added_df_Apple])
added_df_Banana = added_Banana.reset_index() 
added_df_Banana.iloc[:, 0] = added_df_Banana.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Banana.columns = ["metabolite", "flux"]
added_df_Banana = pd.concat([skeleton_Banana[["metabolite", "flux"]], added_df_Banana])
added_df_Blackcurrant = added_Blackcurrant.reset_index() 
added_df_Blackcurrant.iloc[:, 0] = added_df_Blackcurrant.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Blackcurrant.columns = ["metabolite", "flux"]
added_df_Blackcurrant = pd.concat([skeleton_Blackcurrant[["metabolite", "flux"]], added_df_Blackcurrant])
added_df_Blueberries = added_Blueberries.reset_index() 
added_df_Blueberries.iloc[:, 0] = added_df_Blueberries.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Blueberries.columns = ["metabolite", "flux"]
added_df_Blueberries = pd.concat([skeleton_Blueberries[["metabolite", "flux"]], added_df_Blueberries])
added_df_Cherry = added_Cherry.reset_index() 
added_df_Cherry.iloc[:, 0] = added_df_Cherry.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Cherry.columns = ["metabolite", "flux"]
added_df_Cherry = pd.concat([skeleton_Cherry[["metabolite", "flux"]], added_df_Cherry])
added_df_Feijoa = added_Feijoa.reset_index() 
added_df_Feijoa.iloc[:, 0] = added_df_Feijoa.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Feijoa.columns = ["metabolite", "flux"]
added_df_Feijoa = pd.concat([skeleton_Feijoa[["metabolite", "flux"]], added_df_Feijoa])
added_df_Gold_kiwifruit = added_Gold_kiwifruit.reset_index() 
added_df_Gold_kiwifruit.iloc[:, 0] = added_df_Gold_kiwifruit.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Gold_kiwifruit.columns = ["metabolite", "flux"]
added_df_Gold_kiwifruit = pd.concat([skeleton_Gold_kiwifruit[["metabolite", "flux"]], added_df_Gold_kiwifruit])
added_df_Grape = added_Grape.reset_index() 
added_df_Grape.iloc[:, 0] = added_df_Grape.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Grape.columns = ["metabolite", "flux"]
added_df_Grape = pd.concat([skeleton_Grape[["metabolite", "flux"]], added_df_Grape])
added_df_Grapefruit = added_Grapefruit.reset_index() 
added_df_Grapefruit.iloc[:, 0] = added_df_Grapefruit.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Grapefruit.columns = ["metabolite", "flux"]
added_df_Grapefruit = pd.concat([skeleton_Grapefruit[["metabolite", "flux"]], added_df_Grapefruit])
added_df_Green_kiwifruit = added_Green_kiwifruit.reset_index() 
added_df_Green_kiwifruit.iloc[:, 0] = added_df_Green_kiwifruit.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Green_kiwifruit.columns = ["metabolite", "flux"]
added_df_Green_kiwifruit = pd.concat([skeleton_Green_kiwifruit[["metabolite", "flux"]], added_df_Green_kiwifruit])
added_df_Mandarin = added_Mandarin.reset_index() 
added_df_Mandarin.iloc[:, 0] = added_df_Mandarin.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Mandarin.columns = ["metabolite", "flux"]
added_df_Mandarin = pd.concat([skeleton_Mandarin[["metabolite", "flux"]], added_df_Mandarin])
added_df_Mango = added_Mango.reset_index() 
added_df_Mango.iloc[:, 0] = added_df_Mango.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Mango.columns = ["metabolite", "flux"]
added_df_Mango = pd.concat([skeleton_Mango[["metabolite", "flux"]], added_df_Mango])
added_df_Melon = added_Melon.reset_index() 
added_df_Melon.iloc[:, 0] = added_df_Melon.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Melon.columns = ["metabolite", "flux"]
added_df_Melon = pd.concat([skeleton_Melon[["metabolite", "flux"]], added_df_Melon])
added_df_Nectarine = added_Nectarine.reset_index() 
added_df_Nectarine.iloc[:, 0] = added_df_Nectarine.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Nectarine.columns = ["metabolite", "flux"]
added_df_Nectarine = pd.concat([skeleton_Nectarine[["metabolite", "flux"]], added_df_Nectarine])
added_df_Orange = added_Orange.reset_index() 
added_df_Orange.iloc[:, 0] = added_df_Orange.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Orange.columns = ["metabolite", "flux"]
added_df_Orange = pd.concat([skeleton_Orange[["metabolite", "flux"]], added_df_Orange])
added_df_Peache = added_Peache.reset_index() 
added_df_Peache.iloc[:, 0] = added_df_Peache.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Peache.columns = ["metabolite", "flux"]
added_df_Peache = pd.concat([skeleton_Peache[["metabolite", "flux"]], added_df_Peache])
added_df_Pear = added_Pear.reset_index() 
added_df_Pear.iloc[:, 0] = added_df_Pear.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Pear.columns = ["metabolite", "flux"]
added_df_Pear = pd.concat([skeleton_Pear[["metabolite", "flux"]], added_df_Pear])
added_df_Pineapple = added_Pineapple.reset_index() 
added_df_Pineapple.iloc[:, 0] = added_df_Pineapple.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Pineapple.columns = ["metabolite", "flux"]
added_df_Pineapple = pd.concat([skeleton_Pineapple[["metabolite", "flux"]], added_df_Pineapple])
added_df_Plum = added_Plum.reset_index() 
added_df_Plum.iloc[:, 0] = added_df_Plum.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Plum.columns = ["metabolite", "flux"]
added_df_Plum = pd.concat([skeleton_Plum[["metabolite", "flux"]], added_df_Plum])
added_df_Raspberries = added_Raspberries.reset_index() 
added_df_Raspberries.iloc[:, 0] = added_df_Raspberries.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Raspberries.columns = ["metabolite", "flux"]
added_df_Raspberries = pd.concat([skeleton_Raspberries[["metabolite", "flux"]], added_df_Raspberries])
added_df_Strawberries = added_Strawberries.reset_index() 
added_df_Strawberries.iloc[:, 0] = added_df_Strawberries.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Strawberries.columns = ["metabolite", "flux"]
added_df_Strawberries = pd.concat([skeleton_Strawberries[["metabolite", "flux"]], added_df_Strawberries])
added_df_Barley = added_Barley.reset_index() 
added_df_Barley.iloc[:, 0] = added_df_Barley.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Barley.columns = ["metabolite", "flux"]
added_df_Barley = pd.concat([skeleton_Barley[["metabolite", "flux"]], added_df_Barley])
added_df_Barley_cereal = added_Barley_cereal.reset_index() 
added_df_Barley_cereal.iloc[:, 0] = added_df_Barley_cereal.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Barley_cereal.columns = ["metabolite", "flux"]
added_df_Barley_cereal = pd.concat([skeleton_Barley_cereal[["metabolite", "flux"]], added_df_Barley_cereal])
added_df_Couscous = added_Couscous.reset_index() 
added_df_Couscous.iloc[:, 0] = added_df_Couscous.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Couscous.columns = ["metabolite", "flux"]
added_df_Couscous = pd.concat([skeleton_Couscous[["metabolite", "flux"]], added_df_Couscous])
added_df_Noodles = added_Noodles.reset_index() 
added_df_Noodles.iloc[:, 0] = added_df_Noodles.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Noodles.columns = ["metabolite", "flux"]
added_df_Noodles = pd.concat([skeleton_Noodles[["metabolite", "flux"]], added_df_Noodles])
added_df_Oat_cereal = added_Oat_cereal.reset_index() 
added_df_Oat_cereal.iloc[:, 0] = added_df_Oat_cereal.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Oat_cereal.columns = ["metabolite", "flux"]
added_df_Oat_cereal = pd.concat([skeleton_Oat_cereal[["metabolite", "flux"]], added_df_Oat_cereal])
added_df_Pasta = added_Pasta.reset_index() 
added_df_Pasta.iloc[:, 0] = added_df_Pasta.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Pasta.columns = ["metabolite", "flux"]
added_df_Pasta = pd.concat([skeleton_Pasta[["metabolite", "flux"]], added_df_Pasta])
added_df_Rice = added_Rice.reset_index() 
added_df_Rice.iloc[:, 0] = added_df_Rice.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Rice.columns = ["metabolite", "flux"]
added_df_Rice = pd.concat([skeleton_Rice[["metabolite", "flux"]], added_df_Rice])
added_df_Rice_cereal = added_Rice_cereal.reset_index() 
added_df_Rice_cereal.iloc[:, 0] = added_df_Rice_cereal.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Rice_cereal.columns = ["metabolite", "flux"]
added_df_Rice_cereal = pd.concat([skeleton_Rice_cereal[["metabolite", "flux"]], added_df_Rice_cereal])
added_df_Tapioca_pudding = added_Tapioca_pudding.reset_index() 
added_df_Tapioca_pudding.iloc[:, 0] = added_df_Tapioca_pudding.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Tapioca_pudding.columns = ["metabolite", "flux"]
added_df_Tapioca_pudding = pd.concat([skeleton_Tapioca_pudding[["metabolite", "flux"]], added_df_Tapioca_pudding])
added_df_White_bread = added_White_bread.reset_index() 
added_df_White_bread.iloc[:, 0] = added_df_White_bread.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_White_bread.columns = ["metabolite", "flux"]
added_df_White_bread = pd.concat([skeleton_White_bread[["metabolite", "flux"]], added_df_White_bread])
added_df_Wholegrain_bread = added_Wholegrain_bread.reset_index() 
added_df_Wholegrain_bread.iloc[:, 0] = added_df_Wholegrain_bread.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Wholegrain_bread.columns = ["metabolite", "flux"]
added_df_Wholegrain_bread = pd.concat([skeleton_Wholegrain_bread[["metabolite", "flux"]], added_df_Wholegrain_bread])
added_df_Cottage_cheese = added_Cottage_cheese.reset_index() 
added_df_Cottage_cheese.iloc[:, 0] = added_df_Cottage_cheese.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Cottage_cheese.columns = ["metabolite", "flux"]
added_df_Cottage_cheese = pd.concat([skeleton_Cottage_cheese[["metabolite", "flux"]], added_df_Cottage_cheese])
added_df_Eggs = added_Eggs.reset_index() 
added_df_Eggs.iloc[:, 0] = added_df_Eggs.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Eggs.columns = ["metabolite", "flux"]
added_df_Eggs = pd.concat([skeleton_Eggs[["metabolite", "flux"]], added_df_Eggs])
added_df_Mozzarella_cheese = added_Mozzarella_cheese.reset_index() 
added_df_Mozzarella_cheese.iloc[:, 0] = added_df_Mozzarella_cheese.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Mozzarella_cheese.columns = ["metabolite", "flux"]
added_df_Mozzarella_cheese = pd.concat([skeleton_Mozzarella_cheese[["metabolite", "flux"]], added_df_Mozzarella_cheese])
added_df_Soymilk = added_Soymilk.reset_index() 
added_df_Soymilk.iloc[:, 0] = added_df_Soymilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Soymilk.columns = ["metabolite", "flux"]
added_df_Soymilk = pd.concat([skeleton_Soymilk[["metabolite", "flux"]], added_df_Soymilk])
added_df_Tofu = added_Tofu.reset_index() 
added_df_Tofu.iloc[:, 0] = added_df_Tofu.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Tofu.columns = ["metabolite", "flux"]
added_df_Tofu = pd.concat([skeleton_Tofu[["metabolite", "flux"]], added_df_Tofu])
added_df_Whole_milk = added_Whole_milk.reset_index() 
added_df_Whole_milk.iloc[:, 0] = added_df_Whole_milk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Whole_milk.columns = ["metabolite", "flux"]
added_df_Whole_milk = pd.concat([skeleton_Whole_milk[["metabolite", "flux"]], added_df_Whole_milk])
added_df_Yoghurt = added_Yoghurt.reset_index() 
added_df_Yoghurt.iloc[:, 0] = added_df_Yoghurt.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Yoghurt.columns = ["metabolite", "flux"]
added_df_Yoghurt = pd.concat([skeleton_Yoghurt[["metabolite", "flux"]], added_df_Yoghurt])
added_df_Beef = added_Beef.reset_index() 
added_df_Beef.iloc[:, 0] = added_df_Beef.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Beef.columns = ["metabolite", "flux"]
added_df_Beef = pd.concat([skeleton_Beef[["metabolite", "flux"]], added_df_Beef])
added_df_Chicken = added_Chicken.reset_index() 
added_df_Chicken.iloc[:, 0] = added_df_Chicken.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Chicken.columns = ["metabolite", "flux"]
added_df_Chicken = pd.concat([skeleton_Chicken[["metabolite", "flux"]], added_df_Chicken])
added_df_Codfish = added_Codfish.reset_index() 
added_df_Codfish.iloc[:, 0] = added_df_Codfish.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Codfish.columns = ["metabolite", "flux"]
added_df_Codfish = pd.concat([skeleton_Codfish[["metabolite", "flux"]], added_df_Codfish])
added_df_Lamb = added_Lamb.reset_index() 
added_df_Lamb.iloc[:, 0] = added_df_Lamb.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Lamb.columns = ["metabolite", "flux"]
added_df_Lamb = pd.concat([skeleton_Lamb[["metabolite", "flux"]], added_df_Lamb])
added_df_Mackerel = added_Mackerel.reset_index() 
added_df_Mackerel.iloc[:, 0] = added_df_Mackerel.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Mackerel.columns = ["metabolite", "flux"]
added_df_Mackerel = pd.concat([skeleton_Mackerel[["metabolite", "flux"]], added_df_Mackerel])
added_df_Mussels = added_Mussels.reset_index() 
added_df_Mussels.iloc[:, 0] = added_df_Mussels.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Mussels.columns = ["metabolite", "flux"]
added_df_Mussels = pd.concat([skeleton_Mussels[["metabolite", "flux"]], added_df_Mussels])
added_df_Pork = added_Pork.reset_index() 
added_df_Pork.iloc[:, 0] = added_df_Pork.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Pork.columns = ["metabolite", "flux"]
added_df_Pork = pd.concat([skeleton_Pork[["metabolite", "flux"]], added_df_Pork])
added_df_Salmon = added_Salmon.reset_index() 
added_df_Salmon.iloc[:, 0] = added_df_Salmon.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Salmon.columns = ["metabolite", "flux"]
added_df_Salmon = pd.concat([skeleton_Salmon[["metabolite", "flux"]], added_df_Salmon])
added_df_Shrimp = added_Shrimp.reset_index() 
added_df_Shrimp.iloc[:, 0] = added_df_Shrimp.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Shrimp.columns = ["metabolite", "flux"]
added_df_Shrimp = pd.concat([skeleton_Shrimp[["metabolite", "flux"]], added_df_Shrimp])
added_df_Tuna = added_Tuna.reset_index() 
added_df_Tuna.iloc[:, 0] = added_df_Tuna.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Tuna.columns = ["metabolite", "flux"]
added_df_Tuna = pd.concat([skeleton_Tuna[["metabolite", "flux"]], added_df_Tuna])
added_df_Turkey = added_Turkey.reset_index() 
added_df_Turkey.iloc[:, 0] = added_df_Turkey.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Turkey.columns = ["metabolite", "flux"]
added_df_Turkey = pd.concat([skeleton_Turkey[["metabolite", "flux"]], added_df_Turkey])
added_df_Almond = added_Almond.reset_index() 
added_df_Almond.iloc[:, 0] = added_df_Almond.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Almond.columns = ["metabolite", "flux"]
added_df_Almond = pd.concat([skeleton_Almond[["metabolite", "flux"]], added_df_Almond])
added_df_Black_beans = added_Black_beans.reset_index() 
added_df_Black_beans.iloc[:, 0] = added_df_Black_beans.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Black_beans.columns = ["metabolite", "flux"]
added_df_Black_beans = pd.concat([skeleton_Black_beans[["metabolite", "flux"]], added_df_Black_beans])
added_df_Cashew = added_Cashew.reset_index() 
added_df_Cashew.iloc[:, 0] = added_df_Cashew.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Cashew.columns = ["metabolite", "flux"]
added_df_Cashew = pd.concat([skeleton_Cashew[["metabolite", "flux"]], added_df_Cashew])
added_df_Chia = added_Chia.reset_index() 
added_df_Chia.iloc[:, 0] = added_df_Chia.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Chia.columns = ["metabolite", "flux"]
added_df_Chia = pd.concat([skeleton_Chia[["metabolite", "flux"]], added_df_Chia])
added_df_Chickpea = added_Chickpea.reset_index() 
added_df_Chickpea.iloc[:, 0] = added_df_Chickpea.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Chickpea.columns = ["metabolite", "flux"]
added_df_Chickpea = pd.concat([skeleton_Chickpea[["metabolite", "flux"]], added_df_Chickpea])
added_df_Green_peas = added_Green_peas.reset_index() 
added_df_Green_peas.iloc[:, 0] = added_df_Green_peas.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Green_peas.columns = ["metabolite", "flux"]
added_df_Green_peas = pd.concat([skeleton_Green_peas[["metabolite", "flux"]], added_df_Green_peas])
added_df_Hazelnut = added_Hazelnut.reset_index() 
added_df_Hazelnut.iloc[:, 0] = added_df_Hazelnut.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Hazelnut.columns = ["metabolite", "flux"]
added_df_Hazelnut = pd.concat([skeleton_Hazelnut[["metabolite", "flux"]], added_df_Hazelnut])
added_df_Lentils = added_Lentils.reset_index() 
added_df_Lentils.iloc[:, 0] = added_df_Lentils.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Lentils.columns = ["metabolite", "flux"]
added_df_Lentils = pd.concat([skeleton_Lentils[["metabolite", "flux"]], added_df_Lentils])
added_df_Peanut = added_Peanut.reset_index() 
added_df_Peanut.iloc[:, 0] = added_df_Peanut.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Peanut.columns = ["metabolite", "flux"]
added_df_Peanut = pd.concat([skeleton_Peanut[["metabolite", "flux"]], added_df_Peanut])
added_df_Pecans = added_Pecans.reset_index() 
added_df_Pecans.iloc[:, 0] = added_df_Pecans.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Pecans.columns = ["metabolite", "flux"]
added_df_Pecans = pd.concat([skeleton_Pecans[["metabolite", "flux"]], added_df_Pecans])
added_df_Pumpkin_seed = added_Pumpkin_seed.reset_index() 
added_df_Pumpkin_seed.iloc[:, 0] = added_df_Pumpkin_seed.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Pumpkin_seed.columns = ["metabolite", "flux"]
added_df_Pumpkin_seed = pd.concat([skeleton_Pumpkin_seed[["metabolite", "flux"]], added_df_Pumpkin_seed])
added_df_Red_beans = added_Red_beans.reset_index() 
added_df_Red_beans.iloc[:, 0] = added_df_Red_beans.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Red_beans.columns = ["metabolite", "flux"]
added_df_Red_beans = pd.concat([skeleton_Red_beans[["metabolite", "flux"]], added_df_Red_beans])
added_df_Soybean = added_Soybean.reset_index() 
added_df_Soybean.iloc[:, 0] = added_df_Soybean.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Soybean.columns = ["metabolite", "flux"]
added_df_Soybean = pd.concat([skeleton_Soybean[["metabolite", "flux"]], added_df_Soybean])
added_df_Split_peas = added_Split_peas.reset_index() 
added_df_Split_peas.iloc[:, 0] = added_df_Split_peas.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Split_peas.columns = ["metabolite", "flux"]
added_df_Split_peas = pd.concat([skeleton_Split_peas[["metabolite", "flux"]], added_df_Split_peas])
added_df_Sunflower_seed = added_Sunflower_seed.reset_index() 
added_df_Sunflower_seed.iloc[:, 0] = added_df_Sunflower_seed.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Sunflower_seed.columns = ["metabolite", "flux"]
added_df_Sunflower_seed = pd.concat([skeleton_Sunflower_seed[["metabolite", "flux"]], added_df_Sunflower_seed])
added_df_White_beans = added_White_beans.reset_index() 
added_df_White_beans.iloc[:, 0] = added_df_White_beans.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_White_beans.columns = ["metabolite", "flux"]
added_df_White_beans = pd.concat([skeleton_White_beans[["metabolite", "flux"]], added_df_White_beans])
added_df_Breastmilk = added_Breastmilk.reset_index() 
added_df_Breastmilk.iloc[:, 0] = added_df_Breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Breastmilk.columns = ["metabolite", "flux"]
added_df_Breastmilk = pd.concat([skeleton_Breastmilk[["metabolite", "flux"]], added_df_Breastmilk])
added_df_Infant_formula = added_Infant_formula.reset_index() 
added_df_Infant_formula.iloc[:, 0] = added_df_Infant_formula.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Infant_formula.columns = ["metabolite", "flux"]
added_df_Infant_formula = pd.concat([skeleton_Infant_formula[["metabolite", "flux"]], added_df_Infant_formula])

completed_Broccoli = pd.merge(added_df_Broccoli, annotations, on="metabolite", how="left")
completed_Broccoli["reaction"] = "EX_" + completed_Broccoli.metabolite + "_m"
completed_Broccoli["global_id"] = "EX_" + completed_Broccoli.metabolite + "(e)"
completed_Brussel = pd.merge(added_df_Brussel, annotations, on="metabolite", how="left")
completed_Brussel["reaction"] = "EX_" + completed_Brussel.metabolite + "_m"
completed_Brussel["global_id"] = "EX_" + completed_Brussel.metabolite + "(e)"
completed_Cabbage = pd.merge(added_df_Cabbage, annotations, on="metabolite", how="left")
completed_Cabbage["reaction"] = "EX_" + completed_Cabbage.metabolite + "_m"
completed_Cabbage["global_id"] = "EX_" + completed_Cabbage.metabolite + "(e)"
completed_Carrot = pd.merge(added_df_Carrot, annotations, on="metabolite", how="left")
completed_Carrot["reaction"] = "EX_" + completed_Carrot.metabolite + "_m"
completed_Carrot["global_id"] = "EX_" + completed_Carrot.metabolite + "(e)"
completed_Cauliflower = pd.merge(added_df_Cauliflower, annotations, on="metabolite", how="left")
completed_Cauliflower["reaction"] = "EX_" + completed_Cauliflower.metabolite + "_m"
completed_Cauliflower["global_id"] = "EX_" + completed_Cauliflower.metabolite + "(e)"
completed_Celery = pd.merge(added_df_Celery, annotations, on="metabolite", how="left")
completed_Celery["reaction"] = "EX_" + completed_Celery.metabolite + "_m"
completed_Celery["global_id"] = "EX_" + completed_Celery.metabolite + "(e)"
completed_Cucumber = pd.merge(added_df_Cucumber, annotations, on="metabolite", how="left")
completed_Cucumber["reaction"] = "EX_" + completed_Cucumber.metabolite + "_m"
completed_Cucumber["global_id"] = "EX_" + completed_Cucumber.metabolite + "(e)"
completed_Eggplant = pd.merge(added_df_Eggplant, annotations, on="metabolite", how="left")
completed_Eggplant["reaction"] = "EX_" + completed_Eggplant.metabolite + "_m"
completed_Eggplant["global_id"] = "EX_" + completed_Eggplant.metabolite + "(e)"
completed_Green_beans = pd.merge(added_df_Green_beans, annotations, on="metabolite", how="left")
completed_Green_beans["reaction"] = "EX_" + completed_Green_beans.metabolite + "_m"
completed_Green_beans["global_id"] = "EX_" + completed_Green_beans.metabolite + "(e)"
completed_Green_capsicum = pd.merge(added_df_Green_capsicum, annotations, on="metabolite", how="left")
completed_Green_capsicum["reaction"] = "EX_" + completed_Green_capsicum.metabolite + "_m"
completed_Green_capsicum["global_id"] = "EX_" + completed_Green_capsicum.metabolite + "(e)"
completed_Lettuce = pd.merge(added_df_Lettuce, annotations, on="metabolite", how="left")
completed_Lettuce["reaction"] = "EX_" + completed_Lettuce.metabolite + "_m"
completed_Lettuce["global_id"] = "EX_" + completed_Lettuce.metabolite + "(e)"
completed_Mushroom = pd.merge(added_df_Mushroom, annotations, on="metabolite", how="left")
completed_Mushroom["reaction"] = "EX_" + completed_Mushroom.metabolite + "_m"
completed_Mushroom["global_id"] = "EX_" + completed_Mushroom.metabolite + "(e)"
completed_Onion = pd.merge(added_df_Onion, annotations, on="metabolite", how="left")
completed_Onion["reaction"] = "EX_" + completed_Onion.metabolite + "_m"
completed_Onion["global_id"] = "EX_" + completed_Onion.metabolite + "(e)"
completed_Pak_choi = pd.merge(added_df_Pak_choi, annotations, on="metabolite", how="left")
completed_Pak_choi["reaction"] = "EX_" + completed_Pak_choi.metabolite + "_m"
completed_Pak_choi["global_id"] = "EX_" + completed_Pak_choi.metabolite + "(e)"
completed_Potato = pd.merge(added_df_Potato, annotations, on="metabolite", how="left")
completed_Potato["reaction"] = "EX_" + completed_Potato.metabolite + "_m"
completed_Potato["global_id"] = "EX_" + completed_Potato.metabolite + "(e)"
completed_Pumpkin = pd.merge(added_df_Pumpkin, annotations, on="metabolite", how="left")
completed_Pumpkin["reaction"] = "EX_" + completed_Pumpkin.metabolite + "_m"
completed_Pumpkin["global_id"] = "EX_" + completed_Pumpkin.metabolite + "(e)"
completed_Sweetcorn = pd.merge(added_df_Sweetcorn, annotations, on="metabolite", how="left")
completed_Sweetcorn["reaction"] = "EX_" + completed_Sweetcorn.metabolite + "_m"
completed_Sweetcorn["global_id"] = "EX_" + completed_Sweetcorn.metabolite + "(e)"
completed_Spinach = pd.merge(added_df_Spinach, annotations, on="metabolite", how="left")
completed_Spinach["reaction"] = "EX_" + completed_Spinach.metabolite + "_m"
completed_Spinach["global_id"] = "EX_" + completed_Spinach.metabolite + "(e)"
completed_Squash = pd.merge(added_df_Squash, annotations, on="metabolite", how="left")
completed_Squash["reaction"] = "EX_" + completed_Squash.metabolite + "_m"
completed_Squash["global_id"] = "EX_" + completed_Squash.metabolite + "(e)"
completed_Sweet_potato = pd.merge(added_df_Sweet_potato, annotations, on="metabolite", how="left")
completed_Sweet_potato["reaction"] = "EX_" + completed_Sweet_potato.metabolite + "_m"
completed_Sweet_potato["global_id"] = "EX_" + completed_Sweet_potato.metabolite + "(e)"
completed_Tomato = pd.merge(added_df_Tomato, annotations, on="metabolite", how="left")
completed_Tomato["reaction"] = "EX_" + completed_Tomato.metabolite + "_m"
completed_Tomato["global_id"] = "EX_" + completed_Tomato.metabolite + "(e)"
completed_Yam = pd.merge(added_df_Yam, annotations, on="metabolite", how="left")
completed_Yam["reaction"] = "EX_" + completed_Yam.metabolite + "_m"
completed_Yam["global_id"] = "EX_" + completed_Yam.metabolite + "(e)"
completed_Zucchini = pd.merge(added_df_Zucchini, annotations, on="metabolite", how="left")
completed_Zucchini["reaction"] = "EX_" + completed_Zucchini.metabolite + "_m"
completed_Zucchini["global_id"] = "EX_" + completed_Zucchini.metabolite + "(e)"
completed_Apple = pd.merge(added_df_Apple, annotations, on="metabolite", how="left")
completed_Apple["reaction"] = "EX_" + completed_Apple.metabolite + "_m"
completed_Apple["global_id"] = "EX_" + completed_Apple.metabolite + "(e)"
completed_Banana = pd.merge(added_df_Banana, annotations, on="metabolite", how="left")
completed_Banana["reaction"] = "EX_" + completed_Banana.metabolite + "_m"
completed_Banana["global_id"] = "EX_" + completed_Banana.metabolite + "(e)"
completed_Blackcurrant = pd.merge(added_df_Blackcurrant, annotations, on="metabolite", how="left")
completed_Blackcurrant["reaction"] = "EX_" + completed_Blackcurrant.metabolite + "_m"
completed_Blackcurrant["global_id"] = "EX_" + completed_Blackcurrant.metabolite + "(e)"
completed_Blueberries = pd.merge(added_df_Blueberries, annotations, on="metabolite", how="left")
completed_Blueberries["reaction"] = "EX_" + completed_Blueberries.metabolite + "_m"
completed_Blueberries["global_id"] = "EX_" + completed_Blueberries.metabolite + "(e)"
completed_Cherry = pd.merge(added_df_Cherry, annotations, on="metabolite", how="left")
completed_Cherry["reaction"] = "EX_" + completed_Cherry.metabolite + "_m"
completed_Cherry["global_id"] = "EX_" + completed_Cherry.metabolite + "(e)"
completed_Feijoa = pd.merge(added_df_Feijoa, annotations, on="metabolite", how="left")
completed_Feijoa["reaction"] = "EX_" + completed_Feijoa.metabolite + "_m"
completed_Feijoa["global_id"] = "EX_" + completed_Feijoa.metabolite + "(e)"
completed_Gold_kiwifruit = pd.merge(added_df_Gold_kiwifruit, annotations, on="metabolite", how="left")
completed_Gold_kiwifruit["reaction"] = "EX_" + completed_Gold_kiwifruit.metabolite + "_m"
completed_Gold_kiwifruit["global_id"] = "EX_" + completed_Gold_kiwifruit.metabolite + "(e)"
completed_Grape = pd.merge(added_df_Grape, annotations, on="metabolite", how="left")
completed_Grape["reaction"] = "EX_" + completed_Grape.metabolite + "_m"
completed_Grape["global_id"] = "EX_" + completed_Grape.metabolite + "(e)"
completed_Grapefruit = pd.merge(added_df_Grapefruit, annotations, on="metabolite", how="left")
completed_Grapefruit["reaction"] = "EX_" + completed_Grapefruit.metabolite + "_m"
completed_Grapefruit["global_id"] = "EX_" + completed_Grapefruit.metabolite + "(e)"
completed_Green_kiwifruit = pd.merge(added_df_Green_kiwifruit, annotations, on="metabolite", how="left")
completed_Green_kiwifruit["reaction"] = "EX_" + completed_Green_kiwifruit.metabolite + "_m"
completed_Green_kiwifruit["global_id"] = "EX_" + completed_Green_kiwifruit.metabolite + "(e)"
completed_Mandarin = pd.merge(added_df_Mandarin, annotations, on="metabolite", how="left")
completed_Mandarin["reaction"] = "EX_" + completed_Mandarin.metabolite + "_m"
completed_Mandarin["global_id"] = "EX_" + completed_Mandarin.metabolite + "(e)"
completed_Mango = pd.merge(added_df_Mango, annotations, on="metabolite", how="left")
completed_Mango["reaction"] = "EX_" + completed_Mango.metabolite + "_m"
completed_Mango["global_id"] = "EX_" + completed_Mango.metabolite + "(e)"
completed_Melon = pd.merge(added_df_Melon, annotations, on="metabolite", how="left")
completed_Melon["reaction"] = "EX_" + completed_Melon.metabolite + "_m"
completed_Melon["global_id"] = "EX_" + completed_Melon.metabolite + "(e)"
completed_Nectarine = pd.merge(added_df_Nectarine, annotations, on="metabolite", how="left")
completed_Nectarine["reaction"] = "EX_" + completed_Nectarine.metabolite + "_m"
completed_Nectarine["global_id"] = "EX_" + completed_Nectarine.metabolite + "(e)"
completed_Orange = pd.merge(added_df_Orange, annotations, on="metabolite", how="left")
completed_Orange["reaction"] = "EX_" + completed_Orange.metabolite + "_m"
completed_Orange["global_id"] = "EX_" + completed_Orange.metabolite + "(e)"
completed_Peache = pd.merge(added_df_Peache, annotations, on="metabolite", how="left")
completed_Peache["reaction"] = "EX_" + completed_Peache.metabolite + "_m"
completed_Peache["global_id"] = "EX_" + completed_Peache.metabolite + "(e)"
completed_Pear = pd.merge(added_df_Pear, annotations, on="metabolite", how="left")
completed_Pear["reaction"] = "EX_" + completed_Pear.metabolite + "_m"
completed_Pear["global_id"] = "EX_" + completed_Pear.metabolite + "(e)"
completed_Pineapple = pd.merge(added_df_Pineapple, annotations, on="metabolite", how="left")
completed_Pineapple["reaction"] = "EX_" + completed_Pineapple.metabolite + "_m"
completed_Pineapple["global_id"] = "EX_" + completed_Pineapple.metabolite + "(e)"
completed_Plum = pd.merge(added_df_Plum, annotations, on="metabolite", how="left")
completed_Plum["reaction"] = "EX_" + completed_Plum.metabolite + "_m"
completed_Plum["global_id"] = "EX_" + completed_Plum.metabolite + "(e)"
completed_Raspberries = pd.merge(added_df_Raspberries, annotations, on="metabolite", how="left")
completed_Raspberries["reaction"] = "EX_" + completed_Raspberries.metabolite + "_m"
completed_Raspberries["global_id"] = "EX_" + completed_Raspberries.metabolite + "(e)"
completed_Strawberries = pd.merge(added_df_Strawberries, annotations, on="metabolite", how="left")
completed_Strawberries["reaction"] = "EX_" + completed_Strawberries.metabolite + "_m"
completed_Strawberries["global_id"] = "EX_" + completed_Strawberries.metabolite + "(e)"
completed_Barley = pd.merge(added_df_Barley, annotations, on="metabolite", how="left")
completed_Barley["reaction"] = "EX_" + completed_Barley.metabolite + "_m"
completed_Barley["global_id"] = "EX_" + completed_Barley.metabolite + "(e)"
completed_Barley_cereal = pd.merge(added_df_Barley_cereal, annotations, on="metabolite", how="left")
completed_Barley_cereal["reaction"] = "EX_" + completed_Barley_cereal.metabolite + "_m"
completed_Barley_cereal["global_id"] = "EX_" + completed_Barley_cereal.metabolite + "(e)"
completed_Couscous = pd.merge(added_df_Couscous, annotations, on="metabolite", how="left")
completed_Couscous["reaction"] = "EX_" + completed_Couscous.metabolite + "_m"
completed_Couscous["global_id"] = "EX_" + completed_Couscous.metabolite + "(e)"
completed_Noodles = pd.merge(added_df_Noodles, annotations, on="metabolite", how="left")
completed_Noodles["reaction"] = "EX_" + completed_Noodles.metabolite + "_m"
completed_Noodles["global_id"] = "EX_" + completed_Noodles.metabolite + "(e)"
completed_Oat_cereal = pd.merge(added_df_Oat_cereal, annotations, on="metabolite", how="left")
completed_Oat_cereal["reaction"] = "EX_" + completed_Oat_cereal.metabolite + "_m"
completed_Oat_cereal["global_id"] = "EX_" + completed_Oat_cereal.metabolite + "(e)"
completed_Pasta = pd.merge(added_df_Pasta, annotations, on="metabolite", how="left")
completed_Pasta["reaction"] = "EX_" + completed_Pasta.metabolite + "_m"
completed_Pasta["global_id"] = "EX_" + completed_Pasta.metabolite + "(e)"
completed_Rice = pd.merge(added_df_Rice, annotations, on="metabolite", how="left")
completed_Rice["reaction"] = "EX_" + completed_Rice.metabolite + "_m"
completed_Rice["global_id"] = "EX_" + completed_Rice.metabolite + "(e)"
completed_Rice_cereal = pd.merge(added_df_Rice_cereal, annotations, on="metabolite", how="left")
completed_Rice_cereal["reaction"] = "EX_" + completed_Rice_cereal.metabolite + "_m"
completed_Rice_cereal["global_id"] = "EX_" + completed_Rice_cereal.metabolite + "(e)"
completed_Tapioca_pudding = pd.merge(added_df_Tapioca_pudding, annotations, on="metabolite", how="left")
completed_Tapioca_pudding["reaction"] = "EX_" + completed_Tapioca_pudding.metabolite + "_m"
completed_Tapioca_pudding["global_id"] = "EX_" + completed_Tapioca_pudding.metabolite + "(e)"
completed_White_bread = pd.merge(added_df_White_bread, annotations, on="metabolite", how="left")
completed_White_bread["reaction"] = "EX_" + completed_White_bread.metabolite + "_m"
completed_White_bread["global_id"] = "EX_" + completed_White_bread.metabolite + "(e)"
completed_Wholegrain_bread = pd.merge(added_df_Wholegrain_bread, annotations, on="metabolite", how="left")
completed_Wholegrain_bread["reaction"] = "EX_" + completed_Wholegrain_bread.metabolite + "_m"
completed_Wholegrain_bread["global_id"] = "EX_" + completed_Wholegrain_bread.metabolite + "(e)"
completed_Cottage_cheese = pd.merge(added_df_Cottage_cheese, annotations, on="metabolite", how="left")
completed_Cottage_cheese["reaction"] = "EX_" + completed_Cottage_cheese.metabolite + "_m"
completed_Cottage_cheese["global_id"] = "EX_" + completed_Cottage_cheese.metabolite + "(e)"
completed_Eggs = pd.merge(added_df_Eggs, annotations, on="metabolite", how="left")
completed_Eggs["reaction"] = "EX_" + completed_Eggs.metabolite + "_m"
completed_Eggs["global_id"] = "EX_" + completed_Eggs.metabolite + "(e)"
completed_Mozzarella_cheese = pd.merge(added_df_Mozzarella_cheese, annotations, on="metabolite", how="left")
completed_Mozzarella_cheese["reaction"] = "EX_" + completed_Mozzarella_cheese.metabolite + "_m"
completed_Mozzarella_cheese["global_id"] = "EX_" + completed_Mozzarella_cheese.metabolite + "(e)"
completed_Soymilk = pd.merge(added_df_Soymilk, annotations, on="metabolite", how="left")
completed_Soymilk["reaction"] = "EX_" + completed_Soymilk.metabolite + "_m"
completed_Soymilk["global_id"] = "EX_" + completed_Soymilk.metabolite + "(e)"
completed_Tofu = pd.merge(added_df_Tofu, annotations, on="metabolite", how="left")
completed_Tofu["reaction"] = "EX_" + completed_Tofu.metabolite + "_m"
completed_Tofu["global_id"] = "EX_" + completed_Tofu.metabolite + "(e)"
completed_Whole_milk = pd.merge(added_df_Whole_milk, annotations, on="metabolite", how="left")
completed_Whole_milk["reaction"] = "EX_" + completed_Whole_milk.metabolite + "_m"
completed_Whole_milk["global_id"] = "EX_" + completed_Whole_milk.metabolite + "(e)"
completed_Yoghurt = pd.merge(added_df_Yoghurt, annotations, on="metabolite", how="left")
completed_Yoghurt["reaction"] = "EX_" + completed_Yoghurt.metabolite + "_m"
completed_Yoghurt["global_id"] = "EX_" + completed_Yoghurt.metabolite + "(e)"
completed_Beef = pd.merge(added_df_Beef, annotations, on="metabolite", how="left")
completed_Beef["reaction"] = "EX_" + completed_Beef.metabolite + "_m"
completed_Beef["global_id"] = "EX_" + completed_Beef.metabolite + "(e)"
completed_Chicken = pd.merge(added_df_Chicken, annotations, on="metabolite", how="left")
completed_Chicken["reaction"] = "EX_" + completed_Chicken.metabolite + "_m"
completed_Chicken["global_id"] = "EX_" + completed_Chicken.metabolite + "(e)"
completed_Codfish = pd.merge(added_df_Codfish, annotations, on="metabolite", how="left")
completed_Codfish["reaction"] = "EX_" + completed_Codfish.metabolite + "_m"
completed_Codfish["global_id"] = "EX_" + completed_Codfish.metabolite + "(e)"
completed_Lamb = pd.merge(added_df_Lamb, annotations, on="metabolite", how="left")
completed_Lamb["reaction"] = "EX_" + completed_Lamb.metabolite + "_m"
completed_Lamb["global_id"] = "EX_" + completed_Lamb.metabolite + "(e)"
completed_Mackerel = pd.merge(added_df_Mackerel, annotations, on="metabolite", how="left")
completed_Mackerel["reaction"] = "EX_" + completed_Mackerel.metabolite + "_m"
completed_Mackerel["global_id"] = "EX_" + completed_Mackerel.metabolite + "(e)"
completed_Mussels = pd.merge(added_df_Mussels, annotations, on="metabolite", how="left")
completed_Mussels["reaction"] = "EX_" + completed_Mussels.metabolite + "_m"
completed_Mussels["global_id"] = "EX_" + completed_Mussels.metabolite + "(e)"
completed_Pork = pd.merge(added_df_Pork, annotations, on="metabolite", how="left")
completed_Pork["reaction"] = "EX_" + completed_Pork.metabolite + "_m"
completed_Pork["global_id"] = "EX_" + completed_Pork.metabolite + "(e)"
completed_Salmon = pd.merge(added_df_Salmon, annotations, on="metabolite", how="left")
completed_Salmon["reaction"] = "EX_" + completed_Salmon.metabolite + "_m"
completed_Salmon["global_id"] = "EX_" + completed_Salmon.metabolite + "(e)"
completed_Shrimp = pd.merge(added_df_Shrimp, annotations, on="metabolite", how="left")
completed_Shrimp["reaction"] = "EX_" + completed_Shrimp.metabolite + "_m"
completed_Shrimp["global_id"] = "EX_" + completed_Shrimp.metabolite + "(e)"
completed_Tuna = pd.merge(added_df_Tuna, annotations, on="metabolite", how="left")
completed_Tuna["reaction"] = "EX_" + completed_Tuna.metabolite + "_m"
completed_Tuna["global_id"] = "EX_" + completed_Tuna.metabolite + "(e)"
completed_Turkey = pd.merge(added_df_Turkey, annotations, on="metabolite", how="left")
completed_Turkey["reaction"] = "EX_" + completed_Turkey.metabolite + "_m"
completed_Turkey["global_id"] = "EX_" + completed_Turkey.metabolite + "(e)"
completed_Almond = pd.merge(added_df_Almond, annotations, on="metabolite", how="left")
completed_Almond["reaction"] = "EX_" + completed_Almond.metabolite + "_m"
completed_Almond["global_id"] = "EX_" + completed_Almond.metabolite + "(e)"
completed_Black_beans = pd.merge(added_df_Black_beans, annotations, on="metabolite", how="left")
completed_Black_beans["reaction"] = "EX_" + completed_Black_beans.metabolite + "_m"
completed_Black_beans["global_id"] = "EX_" + completed_Black_beans.metabolite + "(e)"
completed_Cashew = pd.merge(added_df_Cashew, annotations, on="metabolite", how="left")
completed_Cashew["reaction"] = "EX_" + completed_Cashew.metabolite + "_m"
completed_Cashew["global_id"] = "EX_" + completed_Cashew.metabolite + "(e)"
completed_Chia = pd.merge(added_df_Chia, annotations, on="metabolite", how="left")
completed_Chia["reaction"] = "EX_" + completed_Chia.metabolite + "_m"
completed_Chia["global_id"] = "EX_" + completed_Chia.metabolite + "(e)"
completed_Chickpea = pd.merge(added_df_Chickpea, annotations, on="metabolite", how="left")
completed_Chickpea["reaction"] = "EX_" + completed_Chickpea.metabolite + "_m"
completed_Chickpea["global_id"] = "EX_" + completed_Chickpea.metabolite + "(e)"
completed_Green_peas = pd.merge(added_df_Green_peas, annotations, on="metabolite", how="left")
completed_Green_peas["reaction"] = "EX_" + completed_Green_peas.metabolite + "_m"
completed_Green_peas["global_id"] = "EX_" + completed_Green_peas.metabolite + "(e)"
completed_Hazelnut = pd.merge(added_df_Hazelnut, annotations, on="metabolite", how="left")
completed_Hazelnut["reaction"] = "EX_" + completed_Hazelnut.metabolite + "_m"
completed_Hazelnut["global_id"] = "EX_" + completed_Hazelnut.metabolite + "(e)"
completed_Lentils = pd.merge(added_df_Lentils, annotations, on="metabolite", how="left")
completed_Lentils["reaction"] = "EX_" + completed_Lentils.metabolite + "_m"
completed_Lentils["global_id"] = "EX_" + completed_Lentils.metabolite + "(e)"
completed_Peanut = pd.merge(added_df_Peanut, annotations, on="metabolite", how="left")
completed_Peanut["reaction"] = "EX_" + completed_Peanut.metabolite + "_m"
completed_Peanut["global_id"] = "EX_" + completed_Peanut.metabolite + "(e)"
completed_Pecans = pd.merge(added_df_Pecans, annotations, on="metabolite", how="left")
completed_Pecans["reaction"] = "EX_" + completed_Pecans.metabolite + "_m"
completed_Pecans["global_id"] = "EX_" + completed_Pecans.metabolite + "(e)"
completed_Pumpkin_seed = pd.merge(added_df_Pumpkin_seed, annotations, on="metabolite", how="left")
completed_Pumpkin_seed["reaction"] = "EX_" + completed_Pumpkin_seed.metabolite + "_m"
completed_Pumpkin_seed["global_id"] = "EX_" + completed_Pumpkin_seed.metabolite + "(e)"
completed_Red_beans = pd.merge(added_df_Red_beans, annotations, on="metabolite", how="left")
completed_Red_beans["reaction"] = "EX_" + completed_Red_beans.metabolite + "_m"
completed_Red_beans["global_id"] = "EX_" + completed_Red_beans.metabolite + "(e)"
completed_Soybean = pd.merge(added_df_Soybean, annotations, on="metabolite", how="left")
completed_Soybean["reaction"] = "EX_" + completed_Soybean.metabolite + "_m"
completed_Soybean["global_id"] = "EX_" + completed_Soybean.metabolite + "(e)"
completed_Split_peas = pd.merge(added_df_Split_peas, annotations, on="metabolite", how="left")
completed_Split_peas["reaction"] = "EX_" + completed_Split_peas.metabolite + "_m"
completed_Split_peas["global_id"] = "EX_" + completed_Split_peas.metabolite + "(e)"
completed_Sunflower_seed = pd.merge(added_df_Sunflower_seed, annotations, on="metabolite", how="left")
completed_Sunflower_seed["reaction"] = "EX_" + completed_Sunflower_seed.metabolite + "_m"
completed_Sunflower_seed["global_id"] = "EX_" + completed_Sunflower_seed.metabolite + "(e)"
completed_White_beans = pd.merge(added_df_White_beans, annotations, on="metabolite", how="left")
completed_White_beans["reaction"] = "EX_" + completed_White_beans.metabolite + "_m"
completed_White_beans["global_id"] = "EX_" + completed_White_beans.metabolite + "(e)"
completed_Breastmilk = pd.merge(added_df_Breastmilk, annotations, on="metabolite", how="left")
completed_Breastmilk["reaction"] = "EX_" + completed_Breastmilk.metabolite + "_m"
completed_Breastmilk["global_id"] = "EX_" + completed_Breastmilk.metabolite + "(e)"
completed_Infant_formula = pd.merge(added_df_Infant_formula, annotations, on="metabolite", how="left")
completed_Infant_formula["reaction"] = "EX_" + completed_Infant_formula.metabolite + "_m"
completed_Infant_formula["global_id"] = "EX_" + completed_Infant_formula.metabolite + "(e)"

#Saving the medium
completed_Broccoli.to_csv("media/Broccoli.csv") 
completed_Brussel.to_csv("media/Brussel.csv") 
completed_Cabbage.to_csv("media/Cabbage.csv") 
completed_Carrot.to_csv("media/Carrot.csv") 
completed_Cauliflower.to_csv("media/Cauliflower.csv") 
completed_Celery.to_csv("media/Celery.csv") 
completed_Cucumber.to_csv("media/Cucumber.csv") 
completed_Eggplant.to_csv("media/Eggplant.csv") 
completed_Green_beans.to_csv("media/Green_beans.csv") 
completed_Green_capsicum.to_csv("media/Green_capsicum.csv") 
completed_Lettuce.to_csv("media/Lettuce.csv") 
completed_Mushroom.to_csv("media/Mushroom.csv") 
completed_Onion.to_csv("media/Onion.csv") 
completed_Pak_choi.to_csv("media/Pak_choi.csv") 
completed_Potato.to_csv("media/Potato.csv") 
completed_Pumpkin.to_csv("media/Pumpkin.csv") 
completed_Sweetcorn.to_csv("media/Sweetcorn.csv") 
completed_Spinach.to_csv("media/Spinach.csv") 
completed_Squash.to_csv("media/Squash.csv") 
completed_Sweet_potato.to_csv("media/Sweet_potato.csv") 
completed_Tomato.to_csv("media/Tomato.csv") 
completed_Yam.to_csv("media/Yam.csv") 
completed_Zucchini.to_csv("media/Zucchini.csv") 
completed_Apple.to_csv("media/Apple.csv") 
completed_Banana.to_csv("media/Banana.csv") 
completed_Blackcurrant.to_csv("media/Blackcurrant.csv") 
completed_Blueberries.to_csv("media/Blueberries.csv") 
completed_Cherry.to_csv("media/Cherry.csv") 
completed_Feijoa.to_csv("media/Feijoa.csv") 
completed_Gold_kiwifruit.to_csv("media/Gold_kiwifruit.csv") 
completed_Grape.to_csv("media/Grape.csv") 
completed_Grapefruit.to_csv("media/Grapefruit.csv") 
completed_Green_kiwifruit.to_csv("media/Green_kiwifruit.csv") 
completed_Mandarin.to_csv("media/Mandarin.csv") 
completed_Mango.to_csv("media/Mango.csv") 
completed_Melon.to_csv("media/Melon.csv") 
completed_Nectarine.to_csv("media/Nectarine.csv") 
completed_Orange.to_csv("media/Orange.csv") 
completed_Peache.to_csv("media/Peache.csv") 
completed_Pear.to_csv("media/Pear.csv") 
completed_Pineapple.to_csv("media/Pineapple.csv") 
completed_Plum.to_csv("media/Plum.csv") 
completed_Raspberries.to_csv("media/Raspberries.csv") 
completed_Strawberries.to_csv("media/Strawberries.csv") 
completed_Barley.to_csv("media/Barley.csv") 
completed_Barley_cereal.to_csv("media/Barley_cereal.csv") 
completed_Couscous.to_csv("media/Couscous.csv") 
completed_Noodles.to_csv("media/Noodles.csv") 
completed_Oat_cereal.to_csv("media/Oat_cereal.csv") 
completed_Pasta.to_csv("media/Pasta.csv") 
completed_Rice.to_csv("media/Rice.csv") 
completed_Rice_cereal.to_csv("media/Rice_cereal.csv") 
completed_Tapioca_pudding.to_csv("media/Tapioca_pudding.csv") 
completed_White_bread.to_csv("media/White_bread.csv") 
completed_Wholegrain_bread.to_csv("media/Wholegrain_bread.csv") 
completed_Cottage_cheese.to_csv("media/Cottage_cheese.csv") 
completed_Eggs.to_csv("media/Eggs.csv") 
completed_Mozzarella_cheese.to_csv("media/Mozzarella_cheese.csv") 
completed_Soymilk.to_csv("media/Soymilk.csv") 
completed_Tofu.to_csv("media/Tofu.csv")
completed_Whole_milk.to_csv("media/Whole_milk.csv") 
completed_Yoghurt.to_csv("media/Yoghurt.csv") 
completed_Beef.to_csv("media/Beef.csv") 
completed_Chicken.to_csv("media/Chicken.csv") 
completed_Codfish.to_csv("media/Codfish.csv") 
completed_Lamb.to_csv("media/Lamb.csv") 
completed_Mackerel.to_csv("media/Mackerel.csv") 
completed_Mussels.to_csv("media/Mussels.csv") 
completed_Pork.to_csv("media/Pork.csv") 
completed_Salmon.to_csv("media/Salmon.csv") 
completed_Shrimp.to_csv("media/Shrimp.csv") 
completed_Tuna.to_csv("media/Tuna.csv") 
completed_Turkey.to_csv("media/Turkey.csv") 
completed_Almond.to_csv("media/Almond.csv") 
completed_Black_beans.to_csv("media/Black_beans.csv") 
completed_Cashew.to_csv("media/Cashew.csv") 
completed_Chia.to_csv("media/Chia.csv") 
completed_Chickpea.to_csv("media/Chickpea.csv") 
completed_Green_peas.to_csv("media/Green_peas.csv") 
completed_Hazelnut.to_csv("media/Hazelnut.csv")  
completed_Lentils.to_csv("media/Lentils.csv") 
completed_Peanut.to_csv("media/Peanut.csv") 
completed_Pecans.to_csv("media/Pecans.csv") 
completed_Pumpkin_seed.to_csv("media/Pumpkin_seed.csv") 
completed_Red_beans.to_csv("media/Red_beans.csv") 
completed_Soybean.to_csv("media/Soybean.csv") 
completed_Split_peas.to_csv("media/Split_peas.csv") 
completed_Sunflower_seed.to_csv("media/Sunflower_seed.csv") 
completed_White_beans.to_csv("media/White_beans.csv") 
completed_Breastmilk.to_csv("media/Breastmilk.csv") 
completed_Infant_formula.to_csv("media/Infant_formula.csv") 

#importing medium
import pandas as pd

completed_Broccoli = pd.read_csv("media/Broccoli.csv") 
completed_Brussel = pd.read_csv("media/Brussel.csv") 
completed_Cabbage = pd.read_csv("media/Cabbage.csv") 
completed_Carrot = pd.read_csv("media/Carrot.csv") 
completed_Cauliflower = pd.read_csv("media/Cauliflower.csv") 
completed_Celery = pd.read_csv("media/Celery.csv") 
completed_Cucumber = pd.read_csv("media/Cucumber.csv") 
completed_Eggplant = pd.read_csv("media/Eggplant.csv") 
completed_Green_beans = pd.read_csv("media/Green_beans.csv") 
completed_Green_capsicum = pd.read_csv("media/Green_capsicum.csv") 
completed_Lettuce = pd.read_csv("media/Lettuce.csv") 
completed_Mushroom = pd.read_csv("media/Mushroom.csv") 
completed_Onion = pd.read_csv("media/Onion.csv") 
completed_Pak_choi = pd.read_csv("media/Pak_choi.csv") 
completed_Potato = pd.read_csv("media/Potato.csv") 
completed_Pumpkin = pd.read_csv("media/Pumpkin.csv") 
completed_Sweetcorn = pd.read_csv("media/Sweetcorn.csv") 
completed_Spinach = pd.read_csv("media/Spinach.csv") 
completed_Squash = pd.read_csv("media/Squash.csv") 
completed_Sweet_potato = pd.read_csv("media/Sweet_potato.csv") 
completed_Tomato = pd.read_csv("media/Tomato.csv") 
completed_Yam = pd.read_csv("media/Yam.csv") 
completed_Zucchini = pd.read_csv("media/Zucchini.csv") 
completed_Apple = pd.read_csv("media/Apple.csv") 
completed_Banana = pd.read_csv("media/Banana.csv") 
completed_Blackcurrant = pd.read_csv("media/Blackcurrant.csv") 
completed_Blueberries = pd.read_csv("media/Blueberries.csv") 
completed_Cherry = pd.read_csv("media/Cherry.csv") 
completed_Feijoa = pd.read_csv("media/Feijoa.csv") 
completed_Gold_kiwifruit = pd.read_csv("media/Gold_kiwifruit.csv") 
completed_Grape = pd.read_csv("media/Grape.csv") 
completed_Grapefruit = pd.read_csv("media/Grapefruit.csv") 
completed_Green_kiwifruit = pd.read_csv("media/Green_kiwifruit.csv") 
completed_Mandarin = pd.read_csv("media/Mandarin.csv") 
completed_Mango = pd.read_csv("media/Mango.csv") 
completed_Melon = pd.read_csv("media/Melon.csv") 
completed_Nectarine = pd.read_csv("media/Nectarine.csv") 
completed_Orange = pd.read_csv("media/Orange.csv") 
completed_Peache = pd.read_csv("media/Peache.csv") 
completed_Pear = pd.read_csv("media/Pear.csv") 
completed_Pineapple = pd.read_csv("media/Pineapple.csv") 
completed_Plum = pd.read_csv("media/Plum.csv") 
completed_Raspberries = pd.read_csv("media/Raspberries.csv") 
completed_Strawberries = pd.read_csv("media/Strawberries.csv") 
completed_Barley = pd.read_csv("media/Barley.csv") 
completed_Barley_cereal = pd.read_csv("media/Barley_cereal.csv") 
completed_Couscous = pd.read_csv("media/Couscous.csv") 
completed_Noodles = pd.read_csv("media/Noodles.csv") 
completed_Oat_cereal = pd.read_csv("media/Oat_cereal.csv") 
completed_Pasta = pd.read_csv("media/Pasta.csv") 
completed_Rice = pd.read_csv("media/Rice.csv") 
completed_Rice_cereal = pd.read_csv("media/Rice_cereal.csv") 
completed_Tapioca_pudding = pd.read_csv("media/Tapioca_pudding.csv") 
completed_White_bread = pd.read_csv("media/White_bread.csv") 
completed_Wholegrain_bread = pd.read_csv("media/Wholegrain_bread.csv") 
completed_Cottage_cheese = pd.read_csv("media/Cottage_cheese.csv") 
completed_Eggs = pd.read_csv("media/Eggs.csv") 
completed_Mozzarella_cheese = pd.read_csv("media/Mozzarella_cheese.csv") 
completed_Soymilk = pd.read_csv("media/Soymilk.csv") 
completed_Tofu = pd.read_csv("media/Tofu.csv")
completed_Whole_milk = pd.read_csv("media/Whole_milk.csv") 
completed_Yoghurt = pd.read_csv("media/Yoghurt.csv") 
completed_Beef = pd.read_csv("media/Beef.csv") 
completed_Chicken = pd.read_csv("media/Chicken.csv") 
completed_Codfish = pd.read_csv("media/Codfish.csv") 
completed_Lamb = pd.read_csv("media/Lamb.csv") 
completed_Mackerel = pd.read_csv("media/Mackerel.csv") 
completed_Mussels = pd.read_csv("media/Mussels.csv") 
completed_Pork = pd.read_csv("media/Pork.csv") 
completed_Salmon = pd.read_csv("media/Salmon.csv") 
completed_Shrimp = pd.read_csv("media/Shrimp.csv") 
completed_Tuna = pd.read_csv("media/Tuna.csv") 
completed_Turkey = pd.read_csv("media/Turkey.csv") 
completed_Almond = pd.read_csv("media/Almond.csv") 
completed_Black_beans = pd.read_csv("media/Black_beans.csv") 
completed_Cashew = pd.read_csv("media/Cashew.csv") 
completed_Chia = pd.read_csv("media/Chia.csv") 
completed_Chickpea = pd.read_csv("media/Chickpea.csv") 
completed_Green_peas = pd.read_csv("media/Green_peas.csv") 
completed_Hazelnut = pd.read_csv("media/Hazelnut.csv")  
completed_Lentils = pd.read_csv("media/Lentils.csv") 
completed_Peanut = pd.read_csv("media/Peanut.csv") 
completed_Pecans = pd.read_csv("media/Pecans.csv") 
completed_Pumpkin_seed = pd.read_csv("media/Pumpkin_seed.csv") 
completed_Red_beans = pd.read_csv("media/Red_beans.csv") 
completed_Soybean = pd.read_csv("media/Soybean.csv") 
completed_Split_peas = pd.read_csv("media/Split_peas.csv") 
completed_Sunflower_seed = pd.read_csv("media/Sunflower_seed.csv") 
completed_White_beans = pd.read_csv("media/White_beans.csv") 
completed_Breastmilk = pd.read_csv("media/Breastmilk.csv") 
completed_Infant_formula = pd.read_csv("media/Infant_formula.csv") 

#Checking the medium
from micom.workflows.db_media import check_db_medium

check_Broccoli = check_db_medium("data/agora201__species.qza", medium=completed_Broccoli, threads=14)
check_Brussel = check_db_medium("data/agora201__species.qza", medium=completed_Brussel, threads=14)
check_Cabbage = check_db_medium("data/agora201__species.qza", medium=completed_Cabbage, threads=14)
check_Carrot = check_db_medium("data/agora201__species.qza", medium=completed_Carrot, threads=14)
check_Cauliflower = check_db_medium("data/agora201__species.qza", medium=completed_Cauliflower, threads=14)
check_Celery = check_db_medium("data/agora201__species.qza", medium=completed_Celery, threads=14)
check_Cucumber = check_db_medium("data/agora201__species.qza", medium=completed_Cucumber, threads=14)
check_Eggplant = check_db_medium("data/agora201__species.qza", medium=completed_Eggplant, threads=14)
check_Green_beans = check_db_medium("data/agora201__species.qza", medium=completed_Green_beans, threads=14)
check_Green_capsicum = check_db_medium("data/agora201__species.qza", medium=completed_Green_capsicum, threads=14)
check_Lettuce = check_db_medium("data/agora201__species.qza", medium=completed_Lettuce, threads=14)
check_Mushroom = check_db_medium("data/agora201__species.qza", medium=completed_Mushroom, threads=14)
check_Onion = check_db_medium("data/agora201__species.qza", medium=completed_Onion, threads=14)
check_Pak_choi = check_db_medium("data/agora201__species.qza", medium=completed_Pak_choi, threads=14)
check_Potato = check_db_medium("data/agora201__species.qza", medium=completed_Potato, threads=14)
check_Pumpkin = check_db_medium("data/agora201__species.qza", medium=completed_Pumpkin, threads=14)
check_Sweetcorn = check_db_medium("data/agora201__species.qza", medium=completed_Sweetcorn, threads=14)
check_Spinach = check_db_medium("data/agora201__species.qza", medium=completed_Spinach, threads=14)
check_Squash = check_db_medium("data/agora201__species.qza", medium=completed_Squash, threads=14)
check_Sweet_potato = check_db_medium("data/agora201__species.qza", medium=completed_Sweet_potato, threads=14)
check_Tomato = check_db_medium("data/agora201__species.qza", medium=completed_Tomato, threads=14)
check_Yam = check_db_medium("data/agora201__species.qza", medium=completed_Yam, threads=14)
check_Zucchini = check_db_medium("data/agora201__species.qza", medium=completed_Zucchini, threads=14)
check_Apple = check_db_medium("data/agora201__species.qza", medium=completed_Apple, threads=14)
check_Banana = check_db_medium("data/agora201__species.qza", medium=completed_Banana, threads=14)
check_Blackcurrant = check_db_medium("data/agora201__species.qza", medium=completed_Blackcurrant, threads=14)
check_Blueberries = check_db_medium("data/agora201__species.qza", medium=completed_Blueberries, threads=14)
check_Cherry = check_db_medium("data/agora201__species.qza", medium=completed_Cherry, threads=14)
check_Feijoa = check_db_medium("data/agora201__species.qza", medium=completed_Feijoa, threads=14)
check_Gold_kiwifruit = check_db_medium("data/agora201__species.qza", medium=completed_Gold_kiwifruit, threads=14)
check_Grape = check_db_medium("data/agora201__species.qza", medium=completed_Grape, threads=14)
check_Grapefruit = check_db_medium("data/agora201__species.qza", medium=completed_Grapefruit, threads=14)
check_Green_kiwifruit = check_db_medium("data/agora201__species.qza", medium=completed_Green_kiwifruit, threads=14)
check_Mandarin = check_db_medium("data/agora201__species.qza", medium=completed_Mandarin, threads=14)
check_Mango = check_db_medium("data/agora201__species.qza", medium=completed_Mango, threads=14)
check_Melon = check_db_medium("data/agora201__species.qza", medium=completed_Melon, threads=14)
check_Nectarine = check_db_medium("data/agora201__species.qza", medium=completed_Nectarine, threads=14)
check_Orange = check_db_medium("data/agora201__species.qza", medium=completed_Orange, threads=14)
check_Peache = check_db_medium("data/agora201__species.qza", medium=completed_Peache, threads=14)
check_Pear = check_db_medium("data/agora201__species.qza", medium=completed_Pear, threads=14)
check_Pineapple = check_db_medium("data/agora201__species.qza", medium=completed_Pineapple, threads=14)
check_Plum = check_db_medium("data/agora201__species.qza", medium=completed_Plum, threads=14)
check_Raspberries = check_db_medium("data/agora201__species.qza", medium=completed_Raspberries, threads=14)
check_Strawberries = check_db_medium("data/agora201__species.qza", medium=completed_Strawberries, threads=14)
check_Barley = check_db_medium("data/agora201__species.qza", medium=completed_Barley, threads=14)
check_Barley_cereal = check_db_medium("data/agora201__species.qza", medium=completed_Barley_cereal, threads=14)
check_Couscous = check_db_medium("data/agora201__species.qza", medium=completed_Couscous, threads=14)
check_Noodles = check_db_medium("data/agora201__species.qza", medium=completed_Noodles, threads=14)
check_Oat_cereal = check_db_medium("data/agora201__species.qza", medium=completed_Oat_cereal, threads=14)
check_Pasta = check_db_medium("data/agora201__species.qza", medium=completed_Pasta, threads=14)
check_Rice = check_db_medium("data/agora201__species.qza", medium=completed_Rice, threads=14)
check_Rice_cereal = check_db_medium("data/agora201__species.qza", medium=completed_Rice_cereal, threads=14)
check_Tapioca_pudding = check_db_medium("data/agora201__species.qza", medium=completed_Tapioca_pudding, threads=14)
check_White_bread = check_db_medium("data/agora201__species.qza", medium=completed_White_bread, threads=14)
check_Wholegrain_bread = check_db_medium("data/agora201__species.qza", medium=completed_Wholegrain_bread, threads=14)
check_Cottage_cheese = check_db_medium("data/agora201__species.qza", medium=completed_Cottage_cheese, threads=14)
check_Eggs = check_db_medium("data/agora201__species.qza", medium=completed_Eggs, threads=14)
check_Mozzarella_cheese = check_db_medium("data/agora201__species.qza", medium=completed_Mozzarella_cheese, threads=14)
check_Soymilk = check_db_medium("data/agora201__species.qza", medium=completed_Soymilk, threads=14)
check_Tofu = check_db_medium("data/agora201__species.qza", medium=completed_Tofu, threads=14)
check_Whole_milk = check_db_medium("data/agora201__species.qza", medium=completed_Whole_milk, threads=14)
check_Yoghurt = check_db_medium("data/agora201__species.qza", medium=completed_Yoghurt, threads=14)
check_Beef = check_db_medium("data/agora201__species.qza", medium=completed_Beef, threads=14)
check_Chicken = check_db_medium("data/agora201__species.qza", medium=completed_Chicken, threads=14)
check_Codfish = check_db_medium("data/agora201__species.qza", medium=completed_Codfish, threads=14)
check_Lamb = check_db_medium("data/agora201__species.qza", medium=completed_Lamb, threads=14)
check_Mackerel = check_db_medium("data/agora201__species.qza", medium=completed_Mackerel, threads=14)
check_Mussels = check_db_medium("data/agora201__species.qza", medium=completed_Mussels, threads=14)
check_Pork = check_db_medium("data/agora201__species.qza", medium=completed_Pork, threads=14)
check_Salmon = check_db_medium("data/agora201__species.qza", medium=completed_Salmon, threads=14)
check_Shrimp = check_db_medium("data/agora201__species.qza", medium=completed_Shrimp, threads=14)
check_Tuna = check_db_medium("data/agora201__species.qza", medium=completed_Tuna, threads=14)
check_Turkey = check_db_medium("data/agora201__species.qza", medium=completed_Turkey, threads=14)
check_Almond = check_db_medium("data/agora201__species.qza", medium=completed_Almond, threads=14)
check_Black_beans = check_db_medium("data/agora201__species.qza", medium=completed_Black_beans, threads=14)
check_Cashew = check_db_medium("data/agora201__species.qza", medium=completed_Cashew, threads=14)
check_Chia = check_db_medium("data/agora201__species.qza", medium=completed_Chia, threads=14)
check_Chickpea = check_db_medium("data/agora201__species.qza", medium=completed_Chickpea, threads=14)
check_Green_peas = check_db_medium("data/agora201__species.qza", medium=completed_Green_peas, threads=14)
check_Hazelnut = check_db_medium("data/agora201__species.qza", medium=completed_Hazelnut, threads=14)
check_Lentils = check_db_medium("data/agora201__species.qza", medium=completed_Lentils, threads=14)
check_Peanut = check_db_medium("data/agora201__species.qza", medium=completed_Peanut, threads=14)
check_Pecans = check_db_medium("data/agora201__species.qza", medium=completed_Pecans, threads=14)
check_Pumpkin_seed = check_db_medium("data/agora201__species.qza", medium=completed_Pumpkin_seed, threads=14)
check_Red_beans = check_db_medium("data/agora201__species.qza", medium=completed_Red_beans, threads=14)
check_Soybean = check_db_medium("data/agora201__species.qza", medium=completed_Soybean, threads=14)
check_Split_peas = check_db_medium("data/agora201__species.qza", medium=completed_Split_peas, threads=14)
check_Sunflower_seed = check_db_medium("data/agora201__species.qza", medium=completed_Sunflower_seed, threads=14)
check_White_beans = check_db_medium("data/agora201__species.qza", medium=completed_White_beans, threads=14)
check_Breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Breastmilk, threads=14)
check_Infant_formula = check_db_medium("data/agora201__species.qza", medium=completed_Infant_formula, threads=14)

check_Broccoli.growth_rate.describe()
check_Brussel.growth_rate.describe()
check_Cabbage.growth_rate.describe()
check_Carrot.growth_rate.describe()
check_Cauliflower.growth_rate.describe()
check_Celery.growth_rate.describe()
check_Cucumber.growth_rate.describe()
check_Eggplant.growth_rate.describe()
check_Green_beans.growth_rate.describe()
check_Green_capsicum.growth_rate.describe()
check_Lettuce.growth_rate.describe()
check_Mushroom.growth_rate.describe()
check_Onion.growth_rate.describe()
check_Pak_choi.growth_rate.describe()
check_Potato.growth_rate.describe()
check_Pumpkin.growth_rate.describe()
check_Sweetcorn.growth_rate.describe()
check_Spinach.growth_rate.describe()
check_Squash.growth_rate.describe()
check_Sweet_potato.growth_rate.describe()
check_Tomato.growth_rate.describe()
check_Yam.growth_rate.describe()
check_Zucchini.growth_rate.describe()
check_Apple.growth_rate.describe()
check_Banana.growth_rate.describe()
check_Blackcurrant.growth_rate.describe()
check_Blueberries.growth_rate.describe()
check_Cherry.growth_rate.describe()
check_Feijoa.growth_rate.describe()
check_Gold_kiwifruit.growth_rate.describe()
check_Grape.growth_rate.describe()
check_Grapefruit.growth_rate.describe()
check_Green_kiwifruit.growth_rate.describe()
check_Mandarin.growth_rate.describe()
check_Mango.growth_rate.describe()
check_Melon.growth_rate.describe()
check_Nectarine.growth_rate.describe()
check_Orange.growth_rate.describe()
check_Peache.growth_rate.describe()
check_Pear.growth_rate.describe()
check_Pineapple.growth_rate.describe()
check_Plum.growth_rate.describe()
check_Raspberries.growth_rate.describe()
check_Strawberries.growth_rate.describe()
check_Barley.growth_rate.describe()
check_Barley_cereal.growth_rate.describe()
check_Couscous.growth_rate.describe()
check_Noodles.growth_rate.describe()
check_Oat_cereal.growth_rate.describe()
check_Pasta.growth_rate.describe()
check_Rice.growth_rate.describe()
check_Rice_cereal.growth_rate.describe()
check_Tapioca_pudding.growth_rate.describe()
check_White_bread.growth_rate.describe()
check_Wholegrain_bread.growth_rate.describe()
check_Cottage_cheese.growth_rate.describe()
check_Eggs.growth_rate.describe()
check_Mozzarella_cheese.growth_rate.describe()
check_Soymilk.growth_rate.describe()
check_Tofu.growth_rate.describe()
check_Whole_milk.growth_rate.describe()
check_Yoghurt.growth_rate.describe()
check_Beef.growth_rate.describe()
check_Chicken.growth_rate.describe()
check_Codfish.growth_rate.describe()
check_Lamb.growth_rate.describe()
check_Mackerel.growth_rate.describe()
check_Mussels.growth_rate.describe()
check_Pork.growth_rate.describe()
check_Salmon.growth_rate.describe()
check_Shrimp.growth_rate.describe()
check_Tuna.growth_rate.describe()
check_Turkey.growth_rate.describe()
check_Almond.growth_rate.describe()
check_Black_beans.growth_rate.describe()
check_Cashew.growth_rate.describe()
check_Chia.growth_rate.describe()
check_Chickpea.growth_rate.describe()
check_Green_peas.growth_rate.describe()
check_Hazelnut.growth_rate.describe()
check_Lentils.growth_rate.describe()
check_Peanut.growth_rate.describe()
check_Pecans.growth_rate.describe()
check_Pumpkin_seed.growth_rate.describe()
check_Red_beans.growth_rate.describe()
check_Soybean.growth_rate.describe()
check_Split_peas.growth_rate.describe()
check_Sunflower_seed.growth_rate.describe()
check_White_beans.growth_rate.describe()
check_Breastmilk.growth_rate.describe()
check_Infant_formula.growth_rate.describe()