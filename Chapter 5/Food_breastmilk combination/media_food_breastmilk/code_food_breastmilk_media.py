##Diets for NZ infants (6-12 months old)

#6 months = 15% food + 85% breatsmilk (608 kcal/d)
#AGORA2

#27/07/23

#Importing the dietary fluxes and converting then
import pandas as pd

diet_Broccoli_breastmilk = pd.read_csv("data/Broccoli, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Broccoli_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Brussel_breastmilk = pd.read_csv("data/Brussel, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Brussel_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Cabbage_breastmilk = pd.read_csv("data/Cabbage, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Cabbage_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Carrot_breastmilk = pd.read_csv("data/Carrot, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Carrot_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Cauliflower_breastmilk = pd.read_csv("data/Cauliflower, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Cauliflower_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Celery_breastmilk = pd.read_csv("data/Celery, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Celery_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Cucumber_breastmilk = pd.read_csv("data/Cucumber, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Cucumber_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Eggplant_breastmilk = pd.read_csv("data/Eggplant, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Eggplant_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Green_beans_breastmilk = pd.read_csv("data/Green_beans, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Green_beans_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Green_capsicum_breastmilk = pd.read_csv("data/Green_capsicum, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Green_capsicum_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Lettuce_breastmilk = pd.read_csv("data/Lettuce, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Lettuce_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Mushroom_breastmilk = pd.read_csv("data/Mushroom, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Mushroom_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Onion_breastmilk = pd.read_csv("data/Onion, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Onion_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Pak_choi_breastmilk = pd.read_csv("data/Pak_choi, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Pak_choi_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Potato_breastmilk = pd.read_csv("data/Potato, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Potato_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Pumpkin_breastmilk = pd.read_csv("data/Pumpkin, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Pumpkin_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Sweetcorn_breastmilk = pd.read_csv("data/Sweetcorn, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Sweetcorn_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Spinach_breastmilk = pd.read_csv("data/Spinach, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Spinach_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Squash_breastmilk = pd.read_csv("data/Squash, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Squash_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Sweet_potato_breastmilk = pd.read_csv("data/Sweet_potato, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Sweet_potato_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Tomato_breastmilk = pd.read_csv("data/Tomato, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Tomato_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Yam_breastmilk = pd.read_csv("data/Yam, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Yam_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Zucchini_breastmilk = pd.read_csv("data/Zucchini, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Zucchini_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Apple_breastmilk = pd.read_csv("data/Apple, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Apple_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Banana_breastmilk = pd.read_csv("data/Banana, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Banana_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Blackcurrant_breastmilk = pd.read_csv("data/Blackcurrant, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Blackcurrant_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Blueberries_breastmilk = pd.read_csv("data/Blueberries, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Blueberries_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Cherry_breastmilk = pd.read_csv("data/Cherry, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Cherry_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Feijoa_breastmilk = pd.read_csv("data/Feijoa, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Feijoa_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Gold_kiwifruit_breastmilk = pd.read_csv("data/Gold_kiwifruit, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Gold_kiwifruit_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Grape_breastmilk = pd.read_csv("data/Grape, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Grape_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Grapefruit_breastmilk = pd.read_csv("data/Grapefruit, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Grapefruit_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Green_kiwifruit_breastmilk = pd.read_csv("data/Green_kiwifruit, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Green_kiwifruit_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Mandarin_breastmilk = pd.read_csv("data/Mandarin, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Mandarin_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Mango_breastmilk = pd.read_csv("data/Mango, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Mango_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Melon_breastmilk = pd.read_csv("data/Melon, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Melon_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Nectarine_breastmilk = pd.read_csv("data/Nectarine, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Nectarine_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Orange_breastmilk = pd.read_csv("data/Orange, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Orange_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Peache_breastmilk = pd.read_csv("data/Peache, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Peache_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Pear_breastmilk = pd.read_csv("data/Pear, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Pear_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Pineapple_breastmilk = pd.read_csv("data/Pineapple, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Pineapple_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Plum_breastmilk = pd.read_csv("data/Plum, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Plum_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Raspberries_breastmilk = pd.read_csv("data/Raspberries, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Raspberries_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Strawberries_breastmilk = pd.read_csv("data/Strawberries, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Strawberries_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Barley_breastmilk = pd.read_csv("data/Barley, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Barley_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Barley_cereal_breastmilk = pd.read_csv("data/Barley_cereal, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Barley_cereal_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Couscous_breastmilk = pd.read_csv("data/Couscous, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Couscous_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Noodles_breastmilk = pd.read_csv("data/Noodles, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Noodles_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Oat_cereal_breastmilk = pd.read_csv("data/Oat_cereal, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Oat_cereal_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Pasta_breastmilk = pd.read_csv("data/Pasta, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Pasta_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Rice_breastmilk = pd.read_csv("data/Rice, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Rice_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Rice_cereal_breastmilk = pd.read_csv("data/Rice_cereal, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Rice_cereal_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Tapioca_pudding_breastmilk = pd.read_csv("data/Tapioca_pudding, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Tapioca_pudding_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_White_bread_breastmilk = pd.read_csv("data/White_bread, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_White_bread_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Wholegrain_bread_breastmilk = pd.read_csv("data/Wholegrain_bread, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Wholegrain_bread_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Cottage_cheese_breastmilk = pd.read_csv("data/Cottage_cheese, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Cottage_cheese_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Eggs_breastmilk = pd.read_csv("data/Eggs, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Eggs_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Mozzarella_cheese_breastmilk = pd.read_csv("data/Mozzarella_cheese, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Mozzarella_cheese_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Soymilk_breastmilk = pd.read_csv("data/Soymilk, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Soymilk_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Tofu_breastmilk = pd.read_csv("data/Tofu, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Tofu_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Whole_milk_breastmilk = pd.read_csv("data/Whole_milk, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Whole_milk_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Yoghurt_breastmilk = pd.read_csv("data/Yoghurt, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Yoghurt_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Beef_breastmilk = pd.read_csv("data/Beef, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Beef_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Chicken_breastmilk = pd.read_csv("data/Chicken, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Chicken_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Codfish_breastmilk = pd.read_csv("data/Codfish, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Codfish_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Lamb_breastmilk = pd.read_csv("data/Lamb, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Lamb_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Mackerel_breastmilk = pd.read_csv("data/Mackerel, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Mackerel_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Mussels_breastmilk = pd.read_csv("data/Mussels, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Mussels_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Pork_breastmilk = pd.read_csv("data/Pork, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Pork_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Salmon_breastmilk = pd.read_csv("data/Salmon, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Salmon_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Shrimp_breastmilk = pd.read_csv("data/Shrimp, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Shrimp_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Tuna_breastmilk = pd.read_csv("data/Tuna, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Tuna_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Turkey_breastmilk = pd.read_csv("data/Turkey, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Turkey_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Almond_breastmilk = pd.read_csv("data/Almond, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Almond_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Black_beans_breastmilk = pd.read_csv("data/Black_beans, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Black_beans_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Cashew_breastmilk = pd.read_csv("data/Cashew, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Cashew_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Chia_breastmilk = pd.read_csv("data/Chia, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Chia_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Chickpea_breastmilk = pd.read_csv("data/Chickpea, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Chickpea_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Green_peas_breastmilk = pd.read_csv("data/Green_peas, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Green_peas_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Hazelnut_breastmilk = pd.read_csv("data/Hazelnut, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Hazelnut_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Lentils_breastmilk = pd.read_csv("data/Lentils, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Lentils_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Peanut_breastmilk = pd.read_csv("data/Peanut, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Peanut_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Pecans_breastmilk = pd.read_csv("data/Pecans, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Pecans_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Pumpkin_seed_breastmilk = pd.read_csv("data/Pumpkin_seed, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Pumpkin_seed_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Red_beans_breastmilk = pd.read_csv("data/Red_beans, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Red_beans_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Soybean_breastmilk = pd.read_csv("data/Soybean, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Soybean_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Split_peas_breastmilk = pd.read_csv("data/Split_peas, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Split_peas_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_Sunflower_seed_breastmilk = pd.read_csv("data/Sunflower_seed, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_Sunflower_seed_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns
diet_White_beans_breastmilk = pd.read_csv("data/White_beans, breastmilk.tsv", sep="\t", header=None) #importing fluxes
diet_White_beans_breastmilk.columns = ["reaction", "flux"] #changing the name of the columns

annotations = pd.read_csv("data/agora_metabolites.csv") #importing a table with the description of agora metabolites
 
diet_Broccoli_breastmilk = diet_Broccoli_breastmilk.rename(columns={diet_Broccoli_breastmilk.columns[0]: "reaction"})
diet_Broccoli_breastmilk["metabolite"] = diet_Broccoli_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Broccoli_breastmilk.loc[diet_Broccoli_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Broccoli_breastmilk.loc[diet_Broccoli_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Brussel_breastmilk = diet_Brussel_breastmilk.rename(columns={diet_Brussel_breastmilk.columns[0]: "reaction"})
diet_Brussel_breastmilk["metabolite"] = diet_Brussel_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Brussel_breastmilk.loc[diet_Brussel_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Brussel_breastmilk.loc[diet_Brussel_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Cabbage_breastmilk = diet_Cabbage_breastmilk.rename(columns={diet_Cabbage_breastmilk.columns[0]: "reaction"})
diet_Cabbage_breastmilk["metabolite"] = diet_Cabbage_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Cabbage_breastmilk.loc[diet_Cabbage_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Cabbage_breastmilk.loc[diet_Cabbage_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Carrot_breastmilk = diet_Carrot_breastmilk.rename(columns={diet_Carrot_breastmilk.columns[0]: "reaction"})
diet_Carrot_breastmilk["metabolite"] = diet_Carrot_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Carrot_breastmilk.loc[diet_Carrot_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Carrot_breastmilk.loc[diet_Carrot_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Cauliflower_breastmilk = diet_Cauliflower_breastmilk.rename(columns={diet_Cauliflower_breastmilk.columns[0]: "reaction"})
diet_Cauliflower_breastmilk["metabolite"] = diet_Cauliflower_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Cauliflower_breastmilk.loc[diet_Cauliflower_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Cauliflower_breastmilk.loc[diet_Cauliflower_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Celery_breastmilk = diet_Celery_breastmilk.rename(columns={diet_Celery_breastmilk.columns[0]: "reaction"})
diet_Celery_breastmilk["metabolite"] = diet_Celery_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Celery_breastmilk.loc[diet_Celery_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Celery_breastmilk.loc[diet_Celery_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Cucumber_breastmilk = diet_Cucumber_breastmilk.rename(columns={diet_Cucumber_breastmilk.columns[0]: "reaction"})
diet_Cucumber_breastmilk["metabolite"] = diet_Cucumber_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Cucumber_breastmilk.loc[diet_Cucumber_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Cucumber_breastmilk.loc[diet_Cucumber_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Eggplant_breastmilk = diet_Eggplant_breastmilk.rename(columns={diet_Eggplant_breastmilk.columns[0]: "reaction"})
diet_Eggplant_breastmilk["metabolite"] = diet_Eggplant_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Eggplant_breastmilk.loc[diet_Eggplant_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Eggplant_breastmilk.loc[diet_Eggplant_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Green_beans_breastmilk = diet_Green_beans_breastmilk.rename(columns={diet_Green_beans_breastmilk.columns[0]: "reaction"})
diet_Green_beans_breastmilk["metabolite"] = diet_Green_beans_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Green_beans_breastmilk.loc[diet_Green_beans_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Green_beans_breastmilk.loc[diet_Green_beans_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Green_capsicum_breastmilk = diet_Green_capsicum_breastmilk.rename(columns={diet_Green_capsicum_breastmilk.columns[0]: "reaction"})
diet_Green_capsicum_breastmilk["metabolite"] = diet_Green_capsicum_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Green_capsicum_breastmilk.loc[diet_Green_capsicum_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Green_capsicum_breastmilk.loc[diet_Green_capsicum_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Lettuce_breastmilk = diet_Lettuce_breastmilk.rename(columns={diet_Lettuce_breastmilk.columns[0]: "reaction"})
diet_Lettuce_breastmilk["metabolite"] = diet_Lettuce_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Lettuce_breastmilk.loc[diet_Lettuce_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Lettuce_breastmilk.loc[diet_Lettuce_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Mushroom_breastmilk = diet_Mushroom_breastmilk.rename(columns={diet_Mushroom_breastmilk.columns[0]: "reaction"})
diet_Mushroom_breastmilk["metabolite"] = diet_Mushroom_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Mushroom_breastmilk.loc[diet_Mushroom_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Mushroom_breastmilk.loc[diet_Mushroom_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Onion_breastmilk = diet_Onion_breastmilk.rename(columns={diet_Onion_breastmilk.columns[0]: "reaction"})
diet_Onion_breastmilk["metabolite"] = diet_Onion_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Onion_breastmilk.loc[diet_Onion_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Onion_breastmilk.loc[diet_Onion_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Pak_choi_breastmilk = diet_Pak_choi_breastmilk.rename(columns={diet_Pak_choi_breastmilk.columns[0]: "reaction"})
diet_Pak_choi_breastmilk["metabolite"] = diet_Pak_choi_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Pak_choi_breastmilk.loc[diet_Pak_choi_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Pak_choi_breastmilk.loc[diet_Pak_choi_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Potato_breastmilk = diet_Potato_breastmilk.rename(columns={diet_Potato_breastmilk.columns[0]: "reaction"})
diet_Potato_breastmilk["metabolite"] = diet_Potato_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Potato_breastmilk.loc[diet_Potato_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Potato_breastmilk.loc[diet_Potato_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Pumpkin_breastmilk = diet_Pumpkin_breastmilk.rename(columns={diet_Pumpkin_breastmilk.columns[0]: "reaction"})
diet_Pumpkin_breastmilk["metabolite"] = diet_Pumpkin_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Pumpkin_breastmilk.loc[diet_Pumpkin_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Pumpkin_breastmilk.loc[diet_Pumpkin_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Sweetcorn_breastmilk = diet_Sweetcorn_breastmilk.rename(columns={diet_Sweetcorn_breastmilk.columns[0]: "reaction"})
diet_Sweetcorn_breastmilk["metabolite"] = diet_Sweetcorn_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Sweetcorn_breastmilk.loc[diet_Sweetcorn_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Sweetcorn_breastmilk.loc[diet_Sweetcorn_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Spinach_breastmilk = diet_Spinach_breastmilk.rename(columns={diet_Spinach_breastmilk.columns[0]: "reaction"})
diet_Spinach_breastmilk["metabolite"] = diet_Spinach_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Spinach_breastmilk.loc[diet_Spinach_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Spinach_breastmilk.loc[diet_Spinach_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Squash_breastmilk = diet_Squash_breastmilk.rename(columns={diet_Squash_breastmilk.columns[0]: "reaction"})
diet_Squash_breastmilk["metabolite"] = diet_Squash_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Squash_breastmilk.loc[diet_Squash_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Squash_breastmilk.loc[diet_Squash_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Sweet_potato_breastmilk = diet_Sweet_potato_breastmilk.rename(columns={diet_Sweet_potato_breastmilk.columns[0]: "reaction"})
diet_Sweet_potato_breastmilk["metabolite"] = diet_Sweet_potato_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Sweet_potato_breastmilk.loc[diet_Sweet_potato_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Sweet_potato_breastmilk.loc[diet_Sweet_potato_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Tomato_breastmilk = diet_Tomato_breastmilk.rename(columns={diet_Tomato_breastmilk.columns[0]: "reaction"})
diet_Tomato_breastmilk["metabolite"] = diet_Tomato_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Tomato_breastmilk.loc[diet_Tomato_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Tomato_breastmilk.loc[diet_Tomato_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Yam_breastmilk = diet_Yam_breastmilk.rename(columns={diet_Yam_breastmilk.columns[0]: "reaction"})
diet_Yam_breastmilk["metabolite"] = diet_Yam_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Yam_breastmilk.loc[diet_Yam_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Yam_breastmilk.loc[diet_Yam_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Zucchini_breastmilk = diet_Zucchini_breastmilk.rename(columns={diet_Zucchini_breastmilk.columns[0]: "reaction"})
diet_Zucchini_breastmilk["metabolite"] = diet_Zucchini_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Zucchini_breastmilk.loc[diet_Zucchini_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Zucchini_breastmilk.loc[diet_Zucchini_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Apple_breastmilk = diet_Apple_breastmilk.rename(columns={diet_Apple_breastmilk.columns[0]: "reaction"})
diet_Apple_breastmilk["metabolite"] = diet_Apple_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Apple_breastmilk.loc[diet_Apple_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Apple_breastmilk.loc[diet_Apple_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Banana_breastmilk = diet_Banana_breastmilk.rename(columns={diet_Banana_breastmilk.columns[0]: "reaction"})
diet_Banana_breastmilk["metabolite"] = diet_Banana_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Banana_breastmilk.loc[diet_Banana_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Banana_breastmilk.loc[diet_Banana_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Blackcurrant_breastmilk = diet_Blackcurrant_breastmilk.rename(columns={diet_Blackcurrant_breastmilk.columns[0]: "reaction"})
diet_Blackcurrant_breastmilk["metabolite"] = diet_Blackcurrant_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Blackcurrant_breastmilk.loc[diet_Blackcurrant_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Blackcurrant_breastmilk.loc[diet_Blackcurrant_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Blueberries_breastmilk = diet_Blueberries_breastmilk.rename(columns={diet_Blueberries_breastmilk.columns[0]: "reaction"})
diet_Blueberries_breastmilk["metabolite"] = diet_Blueberries_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Blueberries_breastmilk.loc[diet_Blueberries_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Blueberries_breastmilk.loc[diet_Blueberries_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Cherry_breastmilk = diet_Cherry_breastmilk.rename(columns={diet_Cherry_breastmilk.columns[0]: "reaction"})
diet_Cherry_breastmilk["metabolite"] = diet_Cherry_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Cherry_breastmilk.loc[diet_Cherry_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Cherry_breastmilk.loc[diet_Cherry_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Feijoa_breastmilk = diet_Feijoa_breastmilk.rename(columns={diet_Feijoa_breastmilk.columns[0]: "reaction"})
diet_Feijoa_breastmilk["metabolite"] = diet_Feijoa_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Feijoa_breastmilk.loc[diet_Feijoa_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Feijoa_breastmilk.loc[diet_Feijoa_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Gold_kiwifruit_breastmilk = diet_Gold_kiwifruit_breastmilk.rename(columns={diet_Gold_kiwifruit_breastmilk.columns[0]: "reaction"})
diet_Gold_kiwifruit_breastmilk["metabolite"] = diet_Gold_kiwifruit_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Gold_kiwifruit_breastmilk.loc[diet_Gold_kiwifruit_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Gold_kiwifruit_breastmilk.loc[diet_Gold_kiwifruit_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Grape_breastmilk = diet_Grape_breastmilk.rename(columns={diet_Grape_breastmilk.columns[0]: "reaction"})
diet_Grape_breastmilk["metabolite"] = diet_Grape_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Grape_breastmilk.loc[diet_Grape_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Grape_breastmilk.loc[diet_Grape_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Grapefruit_breastmilk = diet_Grapefruit_breastmilk.rename(columns={diet_Grapefruit_breastmilk.columns[0]: "reaction"})
diet_Grapefruit_breastmilk["metabolite"] = diet_Grapefruit_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Grapefruit_breastmilk.loc[diet_Grapefruit_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Grapefruit_breastmilk.loc[diet_Grapefruit_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Green_kiwifruit_breastmilk = diet_Green_kiwifruit_breastmilk.rename(columns={diet_Green_kiwifruit_breastmilk.columns[0]: "reaction"})
diet_Green_kiwifruit_breastmilk["metabolite"] = diet_Green_kiwifruit_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Green_kiwifruit_breastmilk.loc[diet_Green_kiwifruit_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Green_kiwifruit_breastmilk.loc[diet_Green_kiwifruit_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Mandarin_breastmilk = diet_Mandarin_breastmilk.rename(columns={diet_Mandarin_breastmilk.columns[0]: "reaction"})
diet_Mandarin_breastmilk["metabolite"] = diet_Mandarin_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Mandarin_breastmilk.loc[diet_Mandarin_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Mandarin_breastmilk.loc[diet_Mandarin_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Mango_breastmilk = diet_Mango_breastmilk.rename(columns={diet_Mango_breastmilk.columns[0]: "reaction"})
diet_Mango_breastmilk["metabolite"] = diet_Mango_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Mango_breastmilk.loc[diet_Mango_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Mango_breastmilk.loc[diet_Mango_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Melon_breastmilk = diet_Melon_breastmilk.rename(columns={diet_Melon_breastmilk.columns[0]: "reaction"})
diet_Melon_breastmilk["metabolite"] = diet_Melon_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Melon_breastmilk.loc[diet_Melon_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Melon_breastmilk.loc[diet_Melon_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Nectarine_breastmilk = diet_Nectarine_breastmilk.rename(columns={diet_Nectarine_breastmilk.columns[0]: "reaction"})
diet_Nectarine_breastmilk["metabolite"] = diet_Nectarine_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Nectarine_breastmilk.loc[diet_Nectarine_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Nectarine_breastmilk.loc[diet_Nectarine_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Orange_breastmilk = diet_Orange_breastmilk.rename(columns={diet_Orange_breastmilk.columns[0]: "reaction"})
diet_Orange_breastmilk["metabolite"] = diet_Orange_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Orange_breastmilk.loc[diet_Orange_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Orange_breastmilk.loc[diet_Orange_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Peache_breastmilk = diet_Peache_breastmilk.rename(columns={diet_Peache_breastmilk.columns[0]: "reaction"})
diet_Peache_breastmilk["metabolite"] = diet_Peache_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Peache_breastmilk.loc[diet_Peache_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Peache_breastmilk.loc[diet_Peache_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Pear_breastmilk = diet_Pear_breastmilk.rename(columns={diet_Pear_breastmilk.columns[0]: "reaction"})
diet_Pear_breastmilk["metabolite"] = diet_Pear_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Pear_breastmilk.loc[diet_Pear_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Pear_breastmilk.loc[diet_Pear_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Pineapple_breastmilk = diet_Pineapple_breastmilk.rename(columns={diet_Pineapple_breastmilk.columns[0]: "reaction"})
diet_Pineapple_breastmilk["metabolite"] = diet_Pineapple_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Pineapple_breastmilk.loc[diet_Pineapple_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Pineapple_breastmilk.loc[diet_Pineapple_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Plum_breastmilk = diet_Plum_breastmilk.rename(columns={diet_Plum_breastmilk.columns[0]: "reaction"})
diet_Plum_breastmilk["metabolite"] = diet_Plum_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Plum_breastmilk.loc[diet_Plum_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Plum_breastmilk.loc[diet_Plum_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Raspberries_breastmilk = diet_Raspberries_breastmilk.rename(columns={diet_Raspberries_breastmilk.columns[0]: "reaction"})
diet_Raspberries_breastmilk["metabolite"] = diet_Raspberries_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Raspberries_breastmilk.loc[diet_Raspberries_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Raspberries_breastmilk.loc[diet_Raspberries_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Strawberries_breastmilk = diet_Strawberries_breastmilk.rename(columns={diet_Strawberries_breastmilk.columns[0]: "reaction"})
diet_Strawberries_breastmilk["metabolite"] = diet_Strawberries_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Strawberries_breastmilk.loc[diet_Strawberries_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Strawberries_breastmilk.loc[diet_Strawberries_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Barley_breastmilk = diet_Barley_breastmilk.rename(columns={diet_Barley_breastmilk.columns[0]: "reaction"})
diet_Barley_breastmilk["metabolite"] = diet_Barley_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Barley_breastmilk.loc[diet_Barley_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Barley_breastmilk.loc[diet_Barley_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Barley_cereal_breastmilk = diet_Barley_cereal_breastmilk.rename(columns={diet_Barley_cereal_breastmilk.columns[0]: "reaction"})
diet_Barley_cereal_breastmilk["metabolite"] = diet_Barley_cereal_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Barley_cereal_breastmilk.loc[diet_Barley_cereal_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Barley_cereal_breastmilk.loc[diet_Barley_cereal_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Couscous_breastmilk = diet_Couscous_breastmilk.rename(columns={diet_Couscous_breastmilk.columns[0]: "reaction"})
diet_Couscous_breastmilk["metabolite"] = diet_Couscous_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Couscous_breastmilk.loc[diet_Couscous_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Couscous_breastmilk.loc[diet_Couscous_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Noodles_breastmilk = diet_Noodles_breastmilk.rename(columns={diet_Noodles_breastmilk.columns[0]: "reaction"})
diet_Noodles_breastmilk["metabolite"] = diet_Noodles_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Noodles_breastmilk.loc[diet_Noodles_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Noodles_breastmilk.loc[diet_Noodles_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Oat_cereal_breastmilk = diet_Oat_cereal_breastmilk.rename(columns={diet_Oat_cereal_breastmilk.columns[0]: "reaction"})
diet_Oat_cereal_breastmilk["metabolite"] = diet_Oat_cereal_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Oat_cereal_breastmilk.loc[diet_Oat_cereal_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Oat_cereal_breastmilk.loc[diet_Oat_cereal_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Pasta_breastmilk = diet_Pasta_breastmilk.rename(columns={diet_Pasta_breastmilk.columns[0]: "reaction"})
diet_Pasta_breastmilk["metabolite"] = diet_Pasta_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Pasta_breastmilk.loc[diet_Pasta_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Pasta_breastmilk.loc[diet_Pasta_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Rice_breastmilk = diet_Rice_breastmilk.rename(columns={diet_Rice_breastmilk.columns[0]: "reaction"})
diet_Rice_breastmilk["metabolite"] = diet_Rice_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Rice_breastmilk.loc[diet_Rice_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Rice_breastmilk.loc[diet_Rice_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Rice_cereal_breastmilk = diet_Rice_cereal_breastmilk.rename(columns={diet_Rice_cereal_breastmilk.columns[0]: "reaction"})
diet_Rice_cereal_breastmilk["metabolite"] = diet_Rice_cereal_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Rice_cereal_breastmilk.loc[diet_Rice_cereal_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Rice_cereal_breastmilk.loc[diet_Rice_cereal_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Tapioca_pudding_breastmilk = diet_Tapioca_pudding_breastmilk.rename(columns={diet_Tapioca_pudding_breastmilk.columns[0]: "reaction"})
diet_Tapioca_pudding_breastmilk["metabolite"] = diet_Tapioca_pudding_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Tapioca_pudding_breastmilk.loc[diet_Tapioca_pudding_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Tapioca_pudding_breastmilk.loc[diet_Tapioca_pudding_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_White_bread_breastmilk = diet_White_bread_breastmilk.rename(columns={diet_White_bread_breastmilk.columns[0]: "reaction"})
diet_White_bread_breastmilk["metabolite"] = diet_White_bread_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_White_bread_breastmilk.loc[diet_White_bread_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_White_bread_breastmilk.loc[diet_White_bread_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Wholegrain_bread_breastmilk = diet_Wholegrain_bread_breastmilk.rename(columns={diet_Wholegrain_bread_breastmilk.columns[0]: "reaction"})
diet_Wholegrain_bread_breastmilk["metabolite"] = diet_Wholegrain_bread_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Wholegrain_bread_breastmilk.loc[diet_Wholegrain_bread_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Wholegrain_bread_breastmilk.loc[diet_Wholegrain_bread_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Cottage_cheese_breastmilk = diet_Cottage_cheese_breastmilk.rename(columns={diet_Cottage_cheese_breastmilk.columns[0]: "reaction"})
diet_Cottage_cheese_breastmilk["metabolite"] = diet_Cottage_cheese_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Cottage_cheese_breastmilk.loc[diet_Cottage_cheese_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Cottage_cheese_breastmilk.loc[diet_Cottage_cheese_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Eggs_breastmilk = diet_Eggs_breastmilk.rename(columns={diet_Eggs_breastmilk.columns[0]: "reaction"})
diet_Eggs_breastmilk["metabolite"] = diet_Eggs_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Eggs_breastmilk.loc[diet_Eggs_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Eggs_breastmilk.loc[diet_Eggs_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Mozzarella_cheese_breastmilk = diet_Mozzarella_cheese_breastmilk.rename(columns={diet_Mozzarella_cheese_breastmilk.columns[0]: "reaction"})
diet_Mozzarella_cheese_breastmilk["metabolite"] = diet_Mozzarella_cheese_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Mozzarella_cheese_breastmilk.loc[diet_Mozzarella_cheese_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Mozzarella_cheese_breastmilk.loc[diet_Mozzarella_cheese_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Soymilk_breastmilk = diet_Soymilk_breastmilk.rename(columns={diet_Soymilk_breastmilk.columns[0]: "reaction"})
diet_Soymilk_breastmilk["metabolite"] = diet_Soymilk_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Soymilk_breastmilk.loc[diet_Soymilk_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Soymilk_breastmilk.loc[diet_Soymilk_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Tofu_breastmilk = diet_Tofu_breastmilk.rename(columns={diet_Tofu_breastmilk.columns[0]: "reaction"})
diet_Tofu_breastmilk["metabolite"] = diet_Tofu_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Tofu_breastmilk.loc[diet_Tofu_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Tofu_breastmilk.loc[diet_Tofu_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Whole_milk_breastmilk = diet_Whole_milk_breastmilk.rename(columns={diet_Whole_milk_breastmilk.columns[0]: "reaction"})
diet_Whole_milk_breastmilk["metabolite"] = diet_Whole_milk_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Whole_milk_breastmilk.loc[diet_Whole_milk_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Whole_milk_breastmilk.loc[diet_Whole_milk_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Yoghurt_breastmilk = diet_Yoghurt_breastmilk.rename(columns={diet_Yoghurt_breastmilk.columns[0]: "reaction"})
diet_Yoghurt_breastmilk["metabolite"] = diet_Yoghurt_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Yoghurt_breastmilk.loc[diet_Yoghurt_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Yoghurt_breastmilk.loc[diet_Yoghurt_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Beef_breastmilk = diet_Beef_breastmilk.rename(columns={diet_Beef_breastmilk.columns[0]: "reaction"})
diet_Beef_breastmilk["metabolite"] = diet_Beef_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Beef_breastmilk.loc[diet_Beef_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Beef_breastmilk.loc[diet_Beef_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Chicken_breastmilk = diet_Chicken_breastmilk.rename(columns={diet_Chicken_breastmilk.columns[0]: "reaction"})
diet_Chicken_breastmilk["metabolite"] = diet_Chicken_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Chicken_breastmilk.loc[diet_Chicken_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Chicken_breastmilk.loc[diet_Chicken_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Codfish_breastmilk = diet_Codfish_breastmilk.rename(columns={diet_Codfish_breastmilk.columns[0]: "reaction"})
diet_Codfish_breastmilk["metabolite"] = diet_Codfish_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Codfish_breastmilk.loc[diet_Codfish_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Codfish_breastmilk.loc[diet_Codfish_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Lamb_breastmilk = diet_Lamb_breastmilk.rename(columns={diet_Lamb_breastmilk.columns[0]: "reaction"})
diet_Lamb_breastmilk["metabolite"] = diet_Lamb_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Lamb_breastmilk.loc[diet_Lamb_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Lamb_breastmilk.loc[diet_Lamb_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Mackerel_breastmilk = diet_Mackerel_breastmilk.rename(columns={diet_Mackerel_breastmilk.columns[0]: "reaction"})
diet_Mackerel_breastmilk["metabolite"] = diet_Mackerel_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Mackerel_breastmilk.loc[diet_Mackerel_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Mackerel_breastmilk.loc[diet_Mackerel_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Mussels_breastmilk = diet_Mussels_breastmilk.rename(columns={diet_Mussels_breastmilk.columns[0]: "reaction"})
diet_Mussels_breastmilk["metabolite"] = diet_Mussels_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Mussels_breastmilk.loc[diet_Mussels_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Mussels_breastmilk.loc[diet_Mussels_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Pork_breastmilk = diet_Pork_breastmilk.rename(columns={diet_Pork_breastmilk.columns[0]: "reaction"})
diet_Pork_breastmilk["metabolite"] = diet_Pork_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Pork_breastmilk.loc[diet_Pork_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Pork_breastmilk.loc[diet_Pork_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Salmon_breastmilk = diet_Salmon_breastmilk.rename(columns={diet_Salmon_breastmilk.columns[0]: "reaction"})
diet_Salmon_breastmilk["metabolite"] = diet_Salmon_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Salmon_breastmilk.loc[diet_Salmon_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Salmon_breastmilk.loc[diet_Salmon_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Shrimp_breastmilk = diet_Shrimp_breastmilk.rename(columns={diet_Shrimp_breastmilk.columns[0]: "reaction"})
diet_Shrimp_breastmilk["metabolite"] = diet_Shrimp_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Shrimp_breastmilk.loc[diet_Shrimp_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Shrimp_breastmilk.loc[diet_Shrimp_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Tuna_breastmilk = diet_Tuna_breastmilk.rename(columns={diet_Tuna_breastmilk.columns[0]: "reaction"})
diet_Tuna_breastmilk["metabolite"] = diet_Tuna_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Tuna_breastmilk.loc[diet_Tuna_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Tuna_breastmilk.loc[diet_Tuna_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Turkey_breastmilk = diet_Turkey_breastmilk.rename(columns={diet_Turkey_breastmilk.columns[0]: "reaction"})
diet_Turkey_breastmilk["metabolite"] = diet_Turkey_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Turkey_breastmilk.loc[diet_Turkey_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Turkey_breastmilk.loc[diet_Turkey_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Almond_breastmilk = diet_Almond_breastmilk.rename(columns={diet_Almond_breastmilk.columns[0]: "reaction"})
diet_Almond_breastmilk["metabolite"] = diet_Almond_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Almond_breastmilk.loc[diet_Almond_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Almond_breastmilk.loc[diet_Almond_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Black_beans_breastmilk = diet_Black_beans_breastmilk.rename(columns={diet_Black_beans_breastmilk.columns[0]: "reaction"})
diet_Black_beans_breastmilk["metabolite"] = diet_Black_beans_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Black_beans_breastmilk.loc[diet_Black_beans_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Black_beans_breastmilk.loc[diet_Black_beans_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Cashew_breastmilk = diet_Cashew_breastmilk.rename(columns={diet_Cashew_breastmilk.columns[0]: "reaction"})
diet_Cashew_breastmilk["metabolite"] = diet_Cashew_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Cashew_breastmilk.loc[diet_Cashew_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Cashew_breastmilk.loc[diet_Cashew_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Chia_breastmilk = diet_Chia_breastmilk.rename(columns={diet_Chia_breastmilk.columns[0]: "reaction"})
diet_Chia_breastmilk["metabolite"] = diet_Chia_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Chia_breastmilk.loc[diet_Chia_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Chia_breastmilk.loc[diet_Chia_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Chickpea_breastmilk = diet_Chickpea_breastmilk.rename(columns={diet_Chickpea_breastmilk.columns[0]: "reaction"})
diet_Chickpea_breastmilk["metabolite"] = diet_Chickpea_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Chickpea_breastmilk.loc[diet_Chickpea_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Chickpea_breastmilk.loc[diet_Chickpea_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Green_peas_breastmilk = diet_Green_peas_breastmilk.rename(columns={diet_Green_peas_breastmilk.columns[0]: "reaction"})
diet_Green_peas_breastmilk["metabolite"] = diet_Green_peas_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Green_peas_breastmilk.loc[diet_Green_peas_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Green_peas_breastmilk.loc[diet_Green_peas_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Hazelnut_breastmilk = diet_Hazelnut_breastmilk.rename(columns={diet_Hazelnut_breastmilk.columns[0]: "reaction"})
diet_Hazelnut_breastmilk["metabolite"] = diet_Hazelnut_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Hazelnut_breastmilk.loc[diet_Hazelnut_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Hazelnut_breastmilk.loc[diet_Hazelnut_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Lentils_breastmilk = diet_Lentils_breastmilk.rename(columns={diet_Lentils_breastmilk.columns[0]: "reaction"})
diet_Lentils_breastmilk["metabolite"] = diet_Lentils_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Lentils_breastmilk.loc[diet_Lentils_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Lentils_breastmilk.loc[diet_Lentils_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Peanut_breastmilk = diet_Peanut_breastmilk.rename(columns={diet_Peanut_breastmilk.columns[0]: "reaction"})
diet_Peanut_breastmilk["metabolite"] = diet_Peanut_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Peanut_breastmilk.loc[diet_Peanut_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Peanut_breastmilk.loc[diet_Peanut_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Pecans_breastmilk = diet_Pecans_breastmilk.rename(columns={diet_Pecans_breastmilk.columns[0]: "reaction"})
diet_Pecans_breastmilk["metabolite"] = diet_Pecans_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Pecans_breastmilk.loc[diet_Pecans_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Pecans_breastmilk.loc[diet_Pecans_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Pumpkin_seed_breastmilk = diet_Pumpkin_seed_breastmilk.rename(columns={diet_Pumpkin_seed_breastmilk.columns[0]: "reaction"})
diet_Pumpkin_seed_breastmilk["metabolite"] = diet_Pumpkin_seed_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Pumpkin_seed_breastmilk.loc[diet_Pumpkin_seed_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Pumpkin_seed_breastmilk.loc[diet_Pumpkin_seed_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Red_beans_breastmilk = diet_Red_beans_breastmilk.rename(columns={diet_Red_beans_breastmilk.columns[0]: "reaction"})
diet_Red_beans_breastmilk["metabolite"] = diet_Red_beans_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Red_beans_breastmilk.loc[diet_Red_beans_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Red_beans_breastmilk.loc[diet_Red_beans_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Soybean_breastmilk = diet_Soybean_breastmilk.rename(columns={diet_Soybean_breastmilk.columns[0]: "reaction"})
diet_Soybean_breastmilk["metabolite"] = diet_Soybean_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Soybean_breastmilk.loc[diet_Soybean_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Soybean_breastmilk.loc[diet_Soybean_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Split_peas_breastmilk = diet_Split_peas_breastmilk.rename(columns={diet_Split_peas_breastmilk.columns[0]: "reaction"})
diet_Split_peas_breastmilk["metabolite"] = diet_Split_peas_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Split_peas_breastmilk.loc[diet_Split_peas_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Split_peas_breastmilk.loc[diet_Split_peas_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_Sunflower_seed_breastmilk = diet_Sunflower_seed_breastmilk.rename(columns={diet_Sunflower_seed_breastmilk.columns[0]: "reaction"})
diet_Sunflower_seed_breastmilk["metabolite"] = diet_Sunflower_seed_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_Sunflower_seed_breastmilk.loc[diet_Sunflower_seed_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_Sunflower_seed_breastmilk.loc[diet_Sunflower_seed_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0
diet_White_beans_breastmilk = diet_White_beans_breastmilk.rename(columns={diet_White_beans_breastmilk.columns[0]: "reaction"})
diet_White_beans_breastmilk["metabolite"] = diet_White_beans_breastmilk.reaction.str.replace("^EX_", "", regex=True).str.replace("\\[e\\]|\\(e\\)", "", regex=True)
diet_White_beans_breastmilk.loc[diet_White_beans_breastmilk.metabolite == "4hpro", "metabolite"] = "4hpro_LT"  # fix name for hydroxyproline
diet_White_beans_breastmilk.loc[diet_White_beans_breastmilk.flux == 0, "flux"] = 1e-4  # bug in VMH designer where everything <1e-4 gets truncated to 0

from cobra.io import read_sbml_model
import pandas as pd

recon3 = read_sbml_model("data/Recon3D.xml.gz") #importing Recon3D model
exchanges = pd.Series([r.id for r in recon3.exchanges])
exchanges = exchanges.str.replace("__", "_").str.replace("_e$|EX_", "", regex=True) #list with the nutrients that are absrobed

diet_Broccoli_breastmilk["dilution"] = 1.0
diet_Broccoli_breastmilk.loc[diet_Broccoli_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Broccoli_breastmilk["flux"] = diet_Broccoli_breastmilk["flux"] * diet_Broccoli_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Broccoli_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Brussel_breastmilk["dilution"] = 1.0
diet_Brussel_breastmilk.loc[diet_Brussel_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Brussel_breastmilk["flux"] = diet_Brussel_breastmilk["flux"] * diet_Brussel_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Brussel_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Cabbage_breastmilk["dilution"] = 1.0
diet_Cabbage_breastmilk.loc[diet_Cabbage_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Cabbage_breastmilk["flux"] = diet_Cabbage_breastmilk["flux"] * diet_Cabbage_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Cabbage_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Carrot_breastmilk["dilution"] = 1.0
diet_Carrot_breastmilk.loc[diet_Carrot_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Carrot_breastmilk["flux"] = diet_Carrot_breastmilk["flux"] * diet_Carrot_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Carrot_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Cauliflower_breastmilk["dilution"] = 1.0
diet_Cauliflower_breastmilk.loc[diet_Cauliflower_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Cauliflower_breastmilk["flux"] = diet_Cauliflower_breastmilk["flux"] * diet_Cauliflower_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Cauliflower_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Celery_breastmilk["dilution"] = 1.0
diet_Celery_breastmilk.loc[diet_Celery_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Celery_breastmilk["flux"] = diet_Celery_breastmilk["flux"] * diet_Celery_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Celery_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Cucumber_breastmilk["dilution"] = 1.0
diet_Cucumber_breastmilk.loc[diet_Cucumber_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Cucumber_breastmilk["flux"] = diet_Cucumber_breastmilk["flux"] * diet_Cucumber_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Cucumber_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Eggplant_breastmilk["dilution"] = 1.0
diet_Eggplant_breastmilk.loc[diet_Eggplant_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Eggplant_breastmilk["flux"] = diet_Eggplant_breastmilk["flux"] * diet_Eggplant_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Eggplant_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Green_beans_breastmilk["dilution"] = 1.0
diet_Green_beans_breastmilk.loc[diet_Green_beans_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Green_beans_breastmilk["flux"] = diet_Green_beans_breastmilk["flux"] * diet_Green_beans_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Green_beans_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Green_capsicum_breastmilk["dilution"] = 1.0
diet_Green_capsicum_breastmilk.loc[diet_Green_capsicum_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Green_capsicum_breastmilk["flux"] = diet_Green_capsicum_breastmilk["flux"] * diet_Green_capsicum_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Green_capsicum_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Lettuce_breastmilk["dilution"] = 1.0
diet_Lettuce_breastmilk.loc[diet_Lettuce_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Lettuce_breastmilk["flux"] = diet_Lettuce_breastmilk["flux"] * diet_Lettuce_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Lettuce_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Mushroom_breastmilk["dilution"] = 1.0
diet_Mushroom_breastmilk.loc[diet_Mushroom_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Mushroom_breastmilk["flux"] = diet_Mushroom_breastmilk["flux"] * diet_Mushroom_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Mushroom_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Onion_breastmilk["dilution"] = 1.0
diet_Onion_breastmilk.loc[diet_Onion_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Onion_breastmilk["flux"] = diet_Onion_breastmilk["flux"] * diet_Onion_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Onion_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Pak_choi_breastmilk["dilution"] = 1.0
diet_Pak_choi_breastmilk.loc[diet_Pak_choi_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Pak_choi_breastmilk["flux"] = diet_Pak_choi_breastmilk["flux"] * diet_Pak_choi_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Pak_choi_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Potato_breastmilk["dilution"] = 1.0
diet_Potato_breastmilk.loc[diet_Potato_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Potato_breastmilk["flux"] = diet_Potato_breastmilk["flux"] * diet_Potato_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Potato_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Pumpkin_breastmilk["dilution"] = 1.0
diet_Pumpkin_breastmilk.loc[diet_Pumpkin_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Pumpkin_breastmilk["flux"] = diet_Pumpkin_breastmilk["flux"] * diet_Pumpkin_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Pumpkin_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Sweetcorn_breastmilk["dilution"] = 1.0
diet_Sweetcorn_breastmilk.loc[diet_Sweetcorn_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Sweetcorn_breastmilk["flux"] = diet_Sweetcorn_breastmilk["flux"] * diet_Sweetcorn_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Sweetcorn_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Spinach_breastmilk["dilution"] = 1.0
diet_Spinach_breastmilk.loc[diet_Spinach_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Spinach_breastmilk["flux"] = diet_Spinach_breastmilk["flux"] * diet_Spinach_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Spinach_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Squash_breastmilk["dilution"] = 1.0
diet_Squash_breastmilk.loc[diet_Squash_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Squash_breastmilk["flux"] = diet_Squash_breastmilk["flux"] * diet_Squash_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Squash_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Sweet_potato_breastmilk["dilution"] = 1.0
diet_Sweet_potato_breastmilk.loc[diet_Sweet_potato_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Sweet_potato_breastmilk["flux"] = diet_Sweet_potato_breastmilk["flux"] * diet_Sweet_potato_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Sweet_potato_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Tomato_breastmilk["dilution"] = 1.0
diet_Tomato_breastmilk.loc[diet_Tomato_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Tomato_breastmilk["flux"] = diet_Tomato_breastmilk["flux"] * diet_Tomato_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Tomato_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Yam_breastmilk["dilution"] = 1.0
diet_Yam_breastmilk.loc[diet_Yam_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Yam_breastmilk["flux"] = diet_Yam_breastmilk["flux"] * diet_Yam_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Yam_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Zucchini_breastmilk["dilution"] = 1.0
diet_Zucchini_breastmilk.loc[diet_Zucchini_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Zucchini_breastmilk["flux"] = diet_Zucchini_breastmilk["flux"] * diet_Zucchini_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Zucchini_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Apple_breastmilk["dilution"] = 1.0
diet_Apple_breastmilk.loc[diet_Apple_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Apple_breastmilk["flux"] = diet_Apple_breastmilk["flux"] * diet_Apple_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Apple_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Banana_breastmilk["dilution"] = 1.0
diet_Banana_breastmilk.loc[diet_Banana_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Banana_breastmilk["flux"] = diet_Banana_breastmilk["flux"] * diet_Banana_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Banana_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Blackcurrant_breastmilk["dilution"] = 1.0
diet_Blackcurrant_breastmilk.loc[diet_Blackcurrant_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Blackcurrant_breastmilk["flux"] = diet_Blackcurrant_breastmilk["flux"] * diet_Blackcurrant_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Blackcurrant_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Blueberries_breastmilk["dilution"] = 1.0
diet_Blueberries_breastmilk.loc[diet_Blueberries_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Blueberries_breastmilk["flux"] = diet_Blueberries_breastmilk["flux"] * diet_Blueberries_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Blueberries_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Cherry_breastmilk["dilution"] = 1.0
diet_Cherry_breastmilk.loc[diet_Cherry_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Cherry_breastmilk["flux"] = diet_Cherry_breastmilk["flux"] * diet_Cherry_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Cherry_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Feijoa_breastmilk["dilution"] = 1.0
diet_Feijoa_breastmilk.loc[diet_Feijoa_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Feijoa_breastmilk["flux"] = diet_Feijoa_breastmilk["flux"] * diet_Feijoa_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Feijoa_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Gold_kiwifruit_breastmilk["dilution"] = 1.0
diet_Gold_kiwifruit_breastmilk.loc[diet_Gold_kiwifruit_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Gold_kiwifruit_breastmilk["flux"] = diet_Gold_kiwifruit_breastmilk["flux"] * diet_Gold_kiwifruit_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Gold_kiwifruit_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Grape_breastmilk["dilution"] = 1.0
diet_Grape_breastmilk.loc[diet_Grape_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Grape_breastmilk["flux"] = diet_Grape_breastmilk["flux"] * diet_Grape_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Grape_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Grapefruit_breastmilk["dilution"] = 1.0
diet_Grapefruit_breastmilk.loc[diet_Grapefruit_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Grapefruit_breastmilk["flux"] = diet_Grapefruit_breastmilk["flux"] * diet_Grapefruit_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Grapefruit_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Green_kiwifruit_breastmilk["dilution"] = 1.0
diet_Green_kiwifruit_breastmilk.loc[diet_Green_kiwifruit_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Green_kiwifruit_breastmilk["flux"] = diet_Green_kiwifruit_breastmilk["flux"] * diet_Green_kiwifruit_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Green_kiwifruit_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Mandarin_breastmilk["dilution"] = 1.0
diet_Mandarin_breastmilk.loc[diet_Mandarin_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Mandarin_breastmilk["flux"] = diet_Mandarin_breastmilk["flux"] * diet_Mandarin_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Mandarin_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Mango_breastmilk["dilution"] = 1.0
diet_Mango_breastmilk.loc[diet_Mango_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Mango_breastmilk["flux"] = diet_Mango_breastmilk["flux"] * diet_Mango_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Mango_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Melon_breastmilk["dilution"] = 1.0
diet_Melon_breastmilk.loc[diet_Melon_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Melon_breastmilk["flux"] = diet_Melon_breastmilk["flux"] * diet_Melon_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Melon_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Nectarine_breastmilk["dilution"] = 1.0
diet_Nectarine_breastmilk.loc[diet_Nectarine_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Nectarine_breastmilk["flux"] = diet_Nectarine_breastmilk["flux"] * diet_Nectarine_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Nectarine_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Orange_breastmilk["dilution"] = 1.0
diet_Orange_breastmilk.loc[diet_Orange_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Orange_breastmilk["flux"] = diet_Orange_breastmilk["flux"] * diet_Orange_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Orange_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Peache_breastmilk["dilution"] = 1.0
diet_Peache_breastmilk.loc[diet_Peache_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Peache_breastmilk["flux"] = diet_Peache_breastmilk["flux"] * diet_Peache_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Peache_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Pear_breastmilk["dilution"] = 1.0
diet_Pear_breastmilk.loc[diet_Pear_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Pear_breastmilk["flux"] = diet_Pear_breastmilk["flux"] * diet_Pear_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Pear_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Pineapple_breastmilk["dilution"] = 1.0
diet_Pineapple_breastmilk.loc[diet_Pineapple_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Pineapple_breastmilk["flux"] = diet_Pineapple_breastmilk["flux"] * diet_Pineapple_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Pineapple_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Plum_breastmilk["dilution"] = 1.0
diet_Plum_breastmilk.loc[diet_Plum_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Plum_breastmilk["flux"] = diet_Plum_breastmilk["flux"] * diet_Plum_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Plum_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Raspberries_breastmilk["dilution"] = 1.0
diet_Raspberries_breastmilk.loc[diet_Raspberries_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Raspberries_breastmilk["flux"] = diet_Raspberries_breastmilk["flux"] * diet_Raspberries_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Raspberries_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Strawberries_breastmilk["dilution"] = 1.0
diet_Strawberries_breastmilk.loc[diet_Strawberries_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Strawberries_breastmilk["flux"] = diet_Strawberries_breastmilk["flux"] * diet_Strawberries_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Strawberries_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Barley_breastmilk["dilution"] = 1.0
diet_Barley_breastmilk.loc[diet_Barley_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Barley_breastmilk["flux"] = diet_Barley_breastmilk["flux"] * diet_Barley_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Barley_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Barley_cereal_breastmilk["dilution"] = 1.0
diet_Barley_cereal_breastmilk.loc[diet_Barley_cereal_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Barley_cereal_breastmilk["flux"] = diet_Barley_cereal_breastmilk["flux"] * diet_Barley_cereal_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Barley_cereal_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Couscous_breastmilk["dilution"] = 1.0
diet_Couscous_breastmilk.loc[diet_Couscous_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Couscous_breastmilk["flux"] = diet_Couscous_breastmilk["flux"] * diet_Couscous_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Couscous_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Noodles_breastmilk["dilution"] = 1.0
diet_Noodles_breastmilk.loc[diet_Noodles_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Noodles_breastmilk["flux"] = diet_Noodles_breastmilk["flux"] * diet_Noodles_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Noodles_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Oat_cereal_breastmilk["dilution"] = 1.0
diet_Oat_cereal_breastmilk.loc[diet_Oat_cereal_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Oat_cereal_breastmilk["flux"] = diet_Oat_cereal_breastmilk["flux"] * diet_Oat_cereal_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Oat_cereal_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Pasta_breastmilk["dilution"] = 1.0
diet_Pasta_breastmilk.loc[diet_Pasta_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Pasta_breastmilk["flux"] = diet_Pasta_breastmilk["flux"] * diet_Pasta_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Pasta_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Rice_breastmilk["dilution"] = 1.0
diet_Rice_breastmilk.loc[diet_Rice_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Rice_breastmilk["flux"] = diet_Rice_breastmilk["flux"] * diet_Rice_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Rice_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Rice_cereal_breastmilk["dilution"] = 1.0
diet_Rice_cereal_breastmilk.loc[diet_Rice_cereal_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Rice_cereal_breastmilk["flux"] = diet_Rice_cereal_breastmilk["flux"] * diet_Rice_cereal_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Rice_cereal_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Tapioca_pudding_breastmilk["dilution"] = 1.0
diet_Tapioca_pudding_breastmilk.loc[diet_Tapioca_pudding_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Tapioca_pudding_breastmilk["flux"] = diet_Tapioca_pudding_breastmilk["flux"] * diet_Tapioca_pudding_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Tapioca_pudding_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_White_bread_breastmilk["dilution"] = 1.0
diet_White_bread_breastmilk.loc[diet_White_bread_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_White_bread_breastmilk["flux"] = diet_White_bread_breastmilk["flux"] * diet_White_bread_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_White_bread_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Wholegrain_bread_breastmilk["dilution"] = 1.0
diet_Wholegrain_bread_breastmilk.loc[diet_Wholegrain_bread_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Wholegrain_bread_breastmilk["flux"] = diet_Wholegrain_bread_breastmilk["flux"] * diet_Wholegrain_bread_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Wholegrain_bread_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Cottage_cheese_breastmilk["dilution"] = 1.0
diet_Cottage_cheese_breastmilk.loc[diet_Cottage_cheese_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Cottage_cheese_breastmilk["flux"] = diet_Cottage_cheese_breastmilk["flux"] * diet_Cottage_cheese_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Cottage_cheese_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Eggs_breastmilk["dilution"] = 1.0
diet_Eggs_breastmilk.loc[diet_Eggs_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Eggs_breastmilk["flux"] = diet_Eggs_breastmilk["flux"] * diet_Eggs_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Eggs_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Mozzarella_cheese_breastmilk["dilution"] = 1.0
diet_Mozzarella_cheese_breastmilk.loc[diet_Mozzarella_cheese_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Mozzarella_cheese_breastmilk["flux"] = diet_Mozzarella_cheese_breastmilk["flux"] * diet_Mozzarella_cheese_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Mozzarella_cheese_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Soymilk_breastmilk["dilution"] = 1.0
diet_Soymilk_breastmilk.loc[diet_Soymilk_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Soymilk_breastmilk["flux"] = diet_Soymilk_breastmilk["flux"] * diet_Soymilk_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Soymilk_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Tofu_breastmilk["dilution"] = 1.0
diet_Tofu_breastmilk.loc[diet_Tofu_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Tofu_breastmilk["flux"] = diet_Tofu_breastmilk["flux"] * diet_Tofu_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Tofu_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Whole_milk_breastmilk["dilution"] = 1.0
diet_Whole_milk_breastmilk.loc[diet_Whole_milk_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Whole_milk_breastmilk["flux"] = diet_Whole_milk_breastmilk["flux"] * diet_Whole_milk_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Whole_milk_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Yoghurt_breastmilk["dilution"] = 1.0
diet_Yoghurt_breastmilk.loc[diet_Yoghurt_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Yoghurt_breastmilk["flux"] = diet_Yoghurt_breastmilk["flux"] * diet_Yoghurt_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Yoghurt_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Beef_breastmilk["dilution"] = 1.0
diet_Beef_breastmilk.loc[diet_Beef_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Beef_breastmilk["flux"] = diet_Beef_breastmilk["flux"] * diet_Beef_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Beef_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Chicken_breastmilk["dilution"] = 1.0
diet_Chicken_breastmilk.loc[diet_Chicken_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Chicken_breastmilk["flux"] = diet_Chicken_breastmilk["flux"] * diet_Chicken_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Chicken_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Codfish_breastmilk["dilution"] = 1.0
diet_Codfish_breastmilk.loc[diet_Codfish_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Codfish_breastmilk["flux"] = diet_Codfish_breastmilk["flux"] * diet_Codfish_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Codfish_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Lamb_breastmilk["dilution"] = 1.0
diet_Lamb_breastmilk.loc[diet_Lamb_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Lamb_breastmilk["flux"] = diet_Lamb_breastmilk["flux"] * diet_Lamb_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Lamb_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Mackerel_breastmilk["dilution"] = 1.0
diet_Mackerel_breastmilk.loc[diet_Mackerel_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Mackerel_breastmilk["flux"] = diet_Mackerel_breastmilk["flux"] * diet_Mackerel_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Mackerel_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Mussels_breastmilk["dilution"] = 1.0
diet_Mussels_breastmilk.loc[diet_Mussels_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Mussels_breastmilk["flux"] = diet_Mussels_breastmilk["flux"] * diet_Mussels_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Mussels_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Pork_breastmilk["dilution"] = 1.0
diet_Pork_breastmilk.loc[diet_Pork_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Pork_breastmilk["flux"] = diet_Pork_breastmilk["flux"] * diet_Pork_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Pork_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Salmon_breastmilk["dilution"] = 1.0
diet_Salmon_breastmilk.loc[diet_Salmon_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Salmon_breastmilk["flux"] = diet_Salmon_breastmilk["flux"] * diet_Salmon_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Salmon_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Shrimp_breastmilk["dilution"] = 1.0
diet_Shrimp_breastmilk.loc[diet_Shrimp_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Shrimp_breastmilk["flux"] = diet_Shrimp_breastmilk["flux"] * diet_Shrimp_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Shrimp_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Tuna_breastmilk["dilution"] = 1.0
diet_Tuna_breastmilk.loc[diet_Tuna_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Tuna_breastmilk["flux"] = diet_Tuna_breastmilk["flux"] * diet_Tuna_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Tuna_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Turkey_breastmilk["dilution"] = 1.0
diet_Turkey_breastmilk.loc[diet_Turkey_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Turkey_breastmilk["flux"] = diet_Turkey_breastmilk["flux"] * diet_Turkey_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Turkey_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Almond_breastmilk["dilution"] = 1.0
diet_Almond_breastmilk.loc[diet_Almond_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Almond_breastmilk["flux"] = diet_Almond_breastmilk["flux"] * diet_Almond_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Almond_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Black_beans_breastmilk["dilution"] = 1.0
diet_Black_beans_breastmilk.loc[diet_Black_beans_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Black_beans_breastmilk["flux"] = diet_Black_beans_breastmilk["flux"] * diet_Black_beans_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Black_beans_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Cashew_breastmilk["dilution"] = 1.0
diet_Cashew_breastmilk.loc[diet_Cashew_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Cashew_breastmilk["flux"] = diet_Cashew_breastmilk["flux"] * diet_Cashew_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Cashew_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Chia_breastmilk["dilution"] = 1.0
diet_Chia_breastmilk.loc[diet_Chia_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Chia_breastmilk["flux"] = diet_Chia_breastmilk["flux"] * diet_Chia_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Chia_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Chickpea_breastmilk["dilution"] = 1.0
diet_Chickpea_breastmilk.loc[diet_Chickpea_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Chickpea_breastmilk["flux"] = diet_Chickpea_breastmilk["flux"] * diet_Chickpea_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Chickpea_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Green_peas_breastmilk["dilution"] = 1.0
diet_Green_peas_breastmilk.loc[diet_Green_peas_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Green_peas_breastmilk["flux"] = diet_Green_peas_breastmilk["flux"] * diet_Green_peas_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Green_peas_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Hazelnut_breastmilk["dilution"] = 1.0
diet_Hazelnut_breastmilk.loc[diet_Hazelnut_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Hazelnut_breastmilk["flux"] = diet_Hazelnut_breastmilk["flux"] * diet_Hazelnut_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Hazelnut_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Lentils_breastmilk["dilution"] = 1.0
diet_Lentils_breastmilk.loc[diet_Lentils_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Lentils_breastmilk["flux"] = diet_Lentils_breastmilk["flux"] * diet_Lentils_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Lentils_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Peanut_breastmilk["dilution"] = 1.0
diet_Peanut_breastmilk.loc[diet_Peanut_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Peanut_breastmilk["flux"] = diet_Peanut_breastmilk["flux"] * diet_Peanut_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Peanut_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Pecans_breastmilk["dilution"] = 1.0
diet_Pecans_breastmilk.loc[diet_Pecans_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Pecans_breastmilk["flux"] = diet_Pecans_breastmilk["flux"] * diet_Pecans_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Pecans_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Pumpkin_seed_breastmilk["dilution"] = 1.0
diet_Pumpkin_seed_breastmilk.loc[diet_Pumpkin_seed_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Pumpkin_seed_breastmilk["flux"] = diet_Pumpkin_seed_breastmilk["flux"] * diet_Pumpkin_seed_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Pumpkin_seed_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Red_beans_breastmilk["dilution"] = 1.0
diet_Red_beans_breastmilk.loc[diet_Red_beans_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Red_beans_breastmilk["flux"] = diet_Red_beans_breastmilk["flux"] * diet_Red_beans_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Red_beans_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Soybean_breastmilk["dilution"] = 1.0
diet_Soybean_breastmilk.loc[diet_Soybean_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Soybean_breastmilk["flux"] = diet_Soybean_breastmilk["flux"] * diet_Soybean_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Soybean_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Split_peas_breastmilk["dilution"] = 1.0
diet_Split_peas_breastmilk.loc[diet_Split_peas_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Split_peas_breastmilk["flux"] = diet_Split_peas_breastmilk["flux"] * diet_Split_peas_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Split_peas_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_Sunflower_seed_breastmilk["dilution"] = 1.0
diet_Sunflower_seed_breastmilk.loc[diet_Sunflower_seed_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_Sunflower_seed_breastmilk["flux"] = diet_Sunflower_seed_breastmilk["flux"] * diet_Sunflower_seed_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_Sunflower_seed_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()
diet_White_beans_breastmilk["dilution"] = 1.0
diet_White_beans_breastmilk.loc[diet_White_beans_breastmilk.metabolite.isin(exchanges), "dilution"] = 0.2 #abosrbed nutrietns will be dilute
diet_White_beans_breastmilk["flux"] = diet_White_beans_breastmilk["flux"] * diet_White_beans_breastmilk["dilution"] #updaing the flux, considering the dilution
diet_White_beans_breastmilk[["metabolite", "dilution"]].drop_duplicates().dilution.value_counts()

#Adding host secreted substrates
#we consider the flux of these compounds as 1 mmol/h

diet_Broccoli_breastmilk.set_index("metabolite", inplace=True)
diet_Brussel_breastmilk.set_index("metabolite", inplace=True)
diet_Cabbage_breastmilk.set_index("metabolite", inplace=True)
diet_Carrot_breastmilk.set_index("metabolite", inplace=True)
diet_Cauliflower_breastmilk.set_index("metabolite", inplace=True)
diet_Celery_breastmilk.set_index("metabolite", inplace=True)
diet_Cucumber_breastmilk.set_index("metabolite", inplace=True)
diet_Eggplant_breastmilk.set_index("metabolite", inplace=True)
diet_Green_beans_breastmilk.set_index("metabolite", inplace=True)
diet_Green_capsicum_breastmilk.set_index("metabolite", inplace=True)
diet_Lettuce_breastmilk.set_index("metabolite", inplace=True)
diet_Mushroom_breastmilk.set_index("metabolite", inplace=True)
diet_Onion_breastmilk.set_index("metabolite", inplace=True)
diet_Pak_choi_breastmilk.set_index("metabolite", inplace=True)
diet_Potato_breastmilk.set_index("metabolite", inplace=True)
diet_Pumpkin_breastmilk.set_index("metabolite", inplace=True)
diet_Sweetcorn_breastmilk.set_index("metabolite", inplace=True)
diet_Spinach_breastmilk.set_index("metabolite", inplace=True)
diet_Squash_breastmilk.set_index("metabolite", inplace=True)
diet_Sweet_potato_breastmilk.set_index("metabolite", inplace=True)
diet_Tomato_breastmilk.set_index("metabolite", inplace=True)
diet_Yam_breastmilk.set_index("metabolite", inplace=True)
diet_Zucchini_breastmilk.set_index("metabolite", inplace=True)
diet_Apple_breastmilk.set_index("metabolite", inplace=True)
diet_Banana_breastmilk.set_index("metabolite", inplace=True)
diet_Blackcurrant_breastmilk.set_index("metabolite", inplace=True)
diet_Blueberries_breastmilk.set_index("metabolite", inplace=True)
diet_Cherry_breastmilk.set_index("metabolite", inplace=True)
diet_Feijoa_breastmilk.set_index("metabolite", inplace=True)
diet_Gold_kiwifruit_breastmilk.set_index("metabolite", inplace=True)
diet_Grape_breastmilk.set_index("metabolite", inplace=True)
diet_Grapefruit_breastmilk.set_index("metabolite", inplace=True)
diet_Green_kiwifruit_breastmilk.set_index("metabolite", inplace=True)
diet_Mandarin_breastmilk.set_index("metabolite", inplace=True)
diet_Mango_breastmilk.set_index("metabolite", inplace=True)
diet_Melon_breastmilk.set_index("metabolite", inplace=True)
diet_Nectarine_breastmilk.set_index("metabolite", inplace=True)
diet_Orange_breastmilk.set_index("metabolite", inplace=True)
diet_Peache_breastmilk.set_index("metabolite", inplace=True)
diet_Pear_breastmilk.set_index("metabolite", inplace=True)
diet_Pineapple_breastmilk.set_index("metabolite", inplace=True)
diet_Plum_breastmilk.set_index("metabolite", inplace=True)
diet_Raspberries_breastmilk.set_index("metabolite", inplace=True)
diet_Strawberries_breastmilk.set_index("metabolite", inplace=True)
diet_Barley_breastmilk.set_index("metabolite", inplace=True)
diet_Barley_cereal_breastmilk.set_index("metabolite", inplace=True)
diet_Couscous_breastmilk.set_index("metabolite", inplace=True)
diet_Noodles_breastmilk.set_index("metabolite", inplace=True)
diet_Oat_cereal_breastmilk.set_index("metabolite", inplace=True)
diet_Pasta_breastmilk.set_index("metabolite", inplace=True)
diet_Rice_breastmilk.set_index("metabolite", inplace=True)
diet_Rice_cereal_breastmilk.set_index("metabolite", inplace=True)
diet_Tapioca_pudding_breastmilk.set_index("metabolite", inplace=True)
diet_White_bread_breastmilk.set_index("metabolite", inplace=True)
diet_Wholegrain_bread_breastmilk.set_index("metabolite", inplace=True)
diet_Cottage_cheese_breastmilk.set_index("metabolite", inplace=True)
diet_Eggs_breastmilk.set_index("metabolite", inplace=True)
diet_Mozzarella_cheese_breastmilk.set_index("metabolite", inplace=True)
diet_Soymilk_breastmilk.set_index("metabolite", inplace=True)
diet_Tofu_breastmilk.set_index("metabolite", inplace=True)
diet_Whole_milk_breastmilk.set_index("metabolite", inplace=True)
diet_Yoghurt_breastmilk.set_index("metabolite", inplace=True)
diet_Beef_breastmilk.set_index("metabolite", inplace=True)
diet_Chicken_breastmilk.set_index("metabolite", inplace=True)
diet_Codfish_breastmilk.set_index("metabolite", inplace=True)
diet_Lamb_breastmilk.set_index("metabolite", inplace=True)
diet_Mackerel_breastmilk.set_index("metabolite", inplace=True)
diet_Mussels_breastmilk.set_index("metabolite", inplace=True)
diet_Pork_breastmilk.set_index("metabolite", inplace=True)
diet_Salmon_breastmilk.set_index("metabolite", inplace=True)
diet_Shrimp_breastmilk.set_index("metabolite", inplace=True)
diet_Tuna_breastmilk.set_index("metabolite", inplace=True)
diet_Turkey_breastmilk.set_index("metabolite", inplace=True)
diet_Almond_breastmilk.set_index("metabolite", inplace=True)
diet_Black_beans_breastmilk.set_index("metabolite", inplace=True)
diet_Cashew_breastmilk.set_index("metabolite", inplace=True)
diet_Chia_breastmilk.set_index("metabolite", inplace=True)
diet_Chickpea_breastmilk.set_index("metabolite", inplace=True)
diet_Green_peas_breastmilk.set_index("metabolite", inplace=True)
diet_Hazelnut_breastmilk.set_index("metabolite", inplace=True)
diet_Lentils_breastmilk.set_index("metabolite", inplace=True)
diet_Peanut_breastmilk.set_index("metabolite", inplace=True)
diet_Pecans_breastmilk.set_index("metabolite", inplace=True)
diet_Pumpkin_seed_breastmilk.set_index("metabolite", inplace=True)
diet_Red_beans_breastmilk.set_index("metabolite", inplace=True)
diet_Soybean_breastmilk.set_index("metabolite", inplace=True)
diet_Split_peas_breastmilk.set_index("metabolite", inplace=True)
diet_Sunflower_seed_breastmilk.set_index("metabolite", inplace=True)
diet_White_beans_breastmilk.set_index("metabolite", inplace=True)

for met in annotations.loc[annotations.metabolite.str.contains("core"), "metabolite"]: # mucins
    diet_Broccoli_breastmilk.loc[met, "flux"] = 1
    diet_Brussel_breastmilk.loc[met, "flux"] = 1
    diet_Cabbage_breastmilk.loc[met, "flux"] = 1
    diet_Carrot_breastmilk.loc[met, "flux"] = 1
    diet_Cauliflower_breastmilk.loc[met, "flux"] = 1
    diet_Celery_breastmilk.loc[met, "flux"] = 1
    diet_Cucumber_breastmilk.loc[met, "flux"] = 1
    diet_Eggplant_breastmilk.loc[met, "flux"] = 1
    diet_Green_beans_breastmilk.loc[met, "flux"] = 1
    diet_Green_capsicum_breastmilk.loc[met, "flux"] = 1
    diet_Lettuce_breastmilk.loc[met, "flux"] = 1
    diet_Mushroom_breastmilk.loc[met, "flux"] = 1
    diet_Onion_breastmilk.loc[met, "flux"] = 1
    diet_Pak_choi_breastmilk.loc[met, "flux"] = 1
    diet_Potato_breastmilk.loc[met, "flux"] = 1
    diet_Pumpkin_breastmilk.loc[met, "flux"] = 1
    diet_Sweetcorn_breastmilk.loc[met, "flux"] = 1
    diet_Spinach_breastmilk.loc[met, "flux"] = 1
    diet_Squash_breastmilk.loc[met, "flux"] = 1
    diet_Sweet_potato_breastmilk.loc[met, "flux"] = 1
    diet_Tomato_breastmilk.loc[met, "flux"] = 1
    diet_Yam_breastmilk.loc[met, "flux"] = 1
    diet_Zucchini_breastmilk.loc[met, "flux"] = 1
    diet_Apple_breastmilk.loc[met, "flux"] = 1
    diet_Banana_breastmilk.loc[met, "flux"] = 1
    diet_Blackcurrant_breastmilk.loc[met, "flux"] = 1
    diet_Blueberries_breastmilk.loc[met, "flux"] = 1
    diet_Cherry_breastmilk.loc[met, "flux"] = 1
    diet_Feijoa_breastmilk.loc[met, "flux"] = 1
    diet_Gold_kiwifruit_breastmilk.loc[met, "flux"] = 1
    diet_Grape_breastmilk.loc[met, "flux"] = 1
    diet_Grapefruit_breastmilk.loc[met, "flux"] = 1
    diet_Green_kiwifruit_breastmilk.loc[met, "flux"] = 1
    diet_Mandarin_breastmilk.loc[met, "flux"] = 1
    diet_Mango_breastmilk.loc[met, "flux"] = 1
    diet_Melon_breastmilk.loc[met, "flux"] = 1
    diet_Nectarine_breastmilk.loc[met, "flux"] = 1
    diet_Orange_breastmilk.loc[met, "flux"] = 1
    diet_Peache_breastmilk.loc[met, "flux"] = 1
    diet_Pear_breastmilk.loc[met, "flux"] = 1
    diet_Pineapple_breastmilk.loc[met, "flux"] = 1
    diet_Plum_breastmilk.loc[met, "flux"] = 1
    diet_Raspberries_breastmilk.loc[met, "flux"] = 1
    diet_Strawberries_breastmilk.loc[met, "flux"] = 1
    diet_Barley_breastmilk.loc[met, "flux"] = 1
    diet_Barley_cereal_breastmilk.loc[met, "flux"] = 1
    diet_Couscous_breastmilk.loc[met, "flux"] = 1
    diet_Noodles_breastmilk.loc[met, "flux"] = 1
    diet_Oat_cereal_breastmilk.loc[met, "flux"] = 1
    diet_Pasta_breastmilk.loc[met, "flux"] = 1
    diet_Rice_breastmilk.loc[met, "flux"] = 1
    diet_Rice_cereal_breastmilk.loc[met, "flux"] = 1
    diet_Tapioca_pudding_breastmilk.loc[met, "flux"] = 1
    diet_White_bread_breastmilk.loc[met, "flux"] = 1
    diet_Wholegrain_bread_breastmilk.loc[met, "flux"] = 1
    diet_Cottage_cheese_breastmilk.loc[met, "flux"] = 1
    diet_Eggs_breastmilk.loc[met, "flux"] = 1
    diet_Mozzarella_cheese_breastmilk.loc[met, "flux"] = 1
    diet_Soymilk_breastmilk.loc[met, "flux"] = 1
    diet_Tofu_breastmilk.loc[met, "flux"] = 1
    diet_Whole_milk_breastmilk.loc[met, "flux"] = 1
    diet_Yoghurt_breastmilk.loc[met, "flux"] = 1
    diet_Beef_breastmilk.loc[met, "flux"] = 1
    diet_Chicken_breastmilk.loc[met, "flux"] = 1
    diet_Codfish_breastmilk.loc[met, "flux"] = 1
    diet_Lamb_breastmilk.loc[met, "flux"] = 1
    diet_Mackerel_breastmilk.loc[met, "flux"] = 1
    diet_Mussels_breastmilk.loc[met, "flux"] = 1
    diet_Pork_breastmilk.loc[met, "flux"] = 1
    diet_Salmon_breastmilk.loc[met, "flux"] = 1
    diet_Shrimp_breastmilk.loc[met, "flux"] = 1
    diet_Tuna_breastmilk.loc[met, "flux"] = 1
    diet_Turkey_breastmilk.loc[met, "flux"] = 1
    diet_Almond_breastmilk.loc[met, "flux"] = 1
    diet_Black_beans_breastmilk.loc[met, "flux"] = 1
    diet_Cashew_breastmilk.loc[met, "flux"] = 1
    diet_Chia_breastmilk.loc[met, "flux"] = 1
    diet_Chickpea_breastmilk.loc[met, "flux"] = 1
    diet_Green_peas_breastmilk.loc[met, "flux"] = 1
    diet_Hazelnut_breastmilk.loc[met, "flux"] = 1
    diet_Lentils_breastmilk.loc[met, "flux"] = 1
    diet_Peanut_breastmilk.loc[met, "flux"] = 1
    diet_Pecans_breastmilk.loc[met, "flux"] = 1
    diet_Pumpkin_seed_breastmilk.loc[met, "flux"] = 1
    diet_Red_beans_breastmilk.loc[met, "flux"] = 1
    diet_Soybean_breastmilk.loc[met, "flux"] = 1
    diet_Split_peas_breastmilk.loc[met, "flux"] = 1
    diet_Sunflower_seed_breastmilk.loc[met, "flux"] = 1
    diet_White_beans_breastmilk.loc[met, "flux"] = 1

for met in ["gchola", "tchola"]: # primary BAs
    diet_Broccoli_breastmilk.loc[met, "flux"] = 1
    diet_Brussel_breastmilk.loc[met, "flux"] = 1
    diet_Cabbage_breastmilk.loc[met, "flux"] = 1
    diet_Carrot_breastmilk.loc[met, "flux"] = 1
    diet_Cauliflower_breastmilk.loc[met, "flux"] = 1
    diet_Celery_breastmilk.loc[met, "flux"] = 1
    diet_Cucumber_breastmilk.loc[met, "flux"] = 1
    diet_Eggplant_breastmilk.loc[met, "flux"] = 1
    diet_Green_beans_breastmilk.loc[met, "flux"] = 1
    diet_Green_capsicum_breastmilk.loc[met, "flux"] = 1
    diet_Lettuce_breastmilk.loc[met, "flux"] = 1
    diet_Mushroom_breastmilk.loc[met, "flux"] = 1
    diet_Onion_breastmilk.loc[met, "flux"] = 1
    diet_Pak_choi_breastmilk.loc[met, "flux"] = 1
    diet_Potato_breastmilk.loc[met, "flux"] = 1
    diet_Pumpkin_breastmilk.loc[met, "flux"] = 1
    diet_Sweetcorn_breastmilk.loc[met, "flux"] = 1
    diet_Spinach_breastmilk.loc[met, "flux"] = 1
    diet_Squash_breastmilk.loc[met, "flux"] = 1
    diet_Sweet_potato_breastmilk.loc[met, "flux"] = 1
    diet_Tomato_breastmilk.loc[met, "flux"] = 1
    diet_Yam_breastmilk.loc[met, "flux"] = 1
    diet_Zucchini_breastmilk.loc[met, "flux"] = 1
    diet_Apple_breastmilk.loc[met, "flux"] = 1
    diet_Banana_breastmilk.loc[met, "flux"] = 1
    diet_Blackcurrant_breastmilk.loc[met, "flux"] = 1
    diet_Blueberries_breastmilk.loc[met, "flux"] = 1
    diet_Cherry_breastmilk.loc[met, "flux"] = 1
    diet_Feijoa_breastmilk.loc[met, "flux"] = 1
    diet_Gold_kiwifruit_breastmilk.loc[met, "flux"] = 1
    diet_Grape_breastmilk.loc[met, "flux"] = 1
    diet_Grapefruit_breastmilk.loc[met, "flux"] = 1
    diet_Green_kiwifruit_breastmilk.loc[met, "flux"] = 1
    diet_Mandarin_breastmilk.loc[met, "flux"] = 1
    diet_Mango_breastmilk.loc[met, "flux"] = 1
    diet_Melon_breastmilk.loc[met, "flux"] = 1
    diet_Nectarine_breastmilk.loc[met, "flux"] = 1
    diet_Orange_breastmilk.loc[met, "flux"] = 1
    diet_Peache_breastmilk.loc[met, "flux"] = 1
    diet_Pear_breastmilk.loc[met, "flux"] = 1
    diet_Pineapple_breastmilk.loc[met, "flux"] = 1
    diet_Plum_breastmilk.loc[met, "flux"] = 1
    diet_Raspberries_breastmilk.loc[met, "flux"] = 1
    diet_Strawberries_breastmilk.loc[met, "flux"] = 1
    diet_Barley_breastmilk.loc[met, "flux"] = 1
    diet_Barley_cereal_breastmilk.loc[met, "flux"] = 1
    diet_Couscous_breastmilk.loc[met, "flux"] = 1
    diet_Noodles_breastmilk.loc[met, "flux"] = 1
    diet_Oat_cereal_breastmilk.loc[met, "flux"] = 1
    diet_Pasta_breastmilk.loc[met, "flux"] = 1
    diet_Rice_breastmilk.loc[met, "flux"] = 1
    diet_Rice_cereal_breastmilk.loc[met, "flux"] = 1
    diet_Tapioca_pudding_breastmilk.loc[met, "flux"] = 1
    diet_White_bread_breastmilk.loc[met, "flux"] = 1
    diet_Wholegrain_bread_breastmilk.loc[met, "flux"] = 1
    diet_Cottage_cheese_breastmilk.loc[met, "flux"] = 1
    diet_Eggs_breastmilk.loc[met, "flux"] = 1
    diet_Mozzarella_cheese_breastmilk.loc[met, "flux"] = 1
    diet_Soymilk_breastmilk.loc[met, "flux"] = 1
    diet_Tofu_breastmilk.loc[met, "flux"] = 1
    diet_Whole_milk_breastmilk.loc[met, "flux"] = 1
    diet_Yoghurt_breastmilk.loc[met, "flux"] = 1
    diet_Beef_breastmilk.loc[met, "flux"] = 1
    diet_Chicken_breastmilk.loc[met, "flux"] = 1
    diet_Codfish_breastmilk.loc[met, "flux"] = 1
    diet_Lamb_breastmilk.loc[met, "flux"] = 1
    diet_Mackerel_breastmilk.loc[met, "flux"] = 1
    diet_Mussels_breastmilk.loc[met, "flux"] = 1
    diet_Pork_breastmilk.loc[met, "flux"] = 1
    diet_Salmon_breastmilk.loc[met, "flux"] = 1
    diet_Shrimp_breastmilk.loc[met, "flux"] = 1
    diet_Tuna_breastmilk.loc[met, "flux"] = 1
    diet_Turkey_breastmilk.loc[met, "flux"] = 1
    diet_Almond_breastmilk.loc[met, "flux"] = 1
    diet_Black_beans_breastmilk.loc[met, "flux"] = 1
    diet_Cashew_breastmilk.loc[met, "flux"] = 1
    diet_Chia_breastmilk.loc[met, "flux"] = 1
    diet_Chickpea_breastmilk.loc[met, "flux"] = 1
    diet_Green_peas_breastmilk.loc[met, "flux"] = 1
    diet_Hazelnut_breastmilk.loc[met, "flux"] = 1
    diet_Lentils_breastmilk.loc[met, "flux"] = 1
    diet_Peanut_breastmilk.loc[met, "flux"] = 1
    diet_Pecans_breastmilk.loc[met, "flux"] = 1
    diet_Pumpkin_seed_breastmilk.loc[met, "flux"] = 1
    diet_Red_beans_breastmilk.loc[met, "flux"] = 1
    diet_Soybean_breastmilk.loc[met, "flux"] = 1
    diet_Split_peas_breastmilk.loc[met, "flux"] = 1
    diet_Sunflower_seed_breastmilk.loc[met, "flux"] = 1
    diet_White_beans_breastmilk.loc[met, "flux"] = 1

diet_Broccoli_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Brussel_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Cabbage_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Carrot_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Cauliflower_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Celery_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Cucumber_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Eggplant_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Green_beans_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Green_capsicum_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Lettuce_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Mushroom_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Onion_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Pak_choi_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Potato_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Pumpkin_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Sweetcorn_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Spinach_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Squash_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Sweet_potato_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Tomato_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Yam_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Zucchini_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Apple_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Banana_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Blackcurrant_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Blueberries_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Cherry_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Feijoa_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Gold_kiwifruit_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Grape_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Grapefruit_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Green_kiwifruit_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Mandarin_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Mango_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Melon_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Nectarine_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Orange_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Peache_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Pear_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Pineapple_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Plum_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Raspberries_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Strawberries_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Barley_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Barley_cereal_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Couscous_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Noodles_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Oat_cereal_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Pasta_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Rice_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Rice_cereal_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Tapioca_pudding_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_White_bread_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Wholegrain_bread_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Cottage_cheese_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Eggs_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Mozzarella_cheese_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Soymilk_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Tofu_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Whole_milk_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Yoghurt_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Beef_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Chicken_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Codfish_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Lamb_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Mackerel_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Mussels_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Pork_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Salmon_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Shrimp_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Tuna_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Turkey_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Almond_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Black_beans_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Cashew_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Chia_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Chickpea_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Green_peas_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Hazelnut_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Lentils_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Peanut_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Pecans_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Pumpkin_seed_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Red_beans_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Soybean_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Split_peas_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_Sunflower_seed_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment
diet_White_beans_breastmilk.loc["o2", "flux"] = 0.001 # anaerobic environment

diet_Broccoli_breastmilk.reset_index(inplace=True)
diet_Broccoli_breastmilk["reaction"] = "EX_" + diet_Broccoli_breastmilk.metabolite + "(e)"
diet_Brussel_breastmilk.reset_index(inplace=True)
diet_Brussel_breastmilk["reaction"] = "EX_" + diet_Brussel_breastmilk.metabolite + "(e)"
diet_Cabbage_breastmilk.reset_index(inplace=True)
diet_Cabbage_breastmilk["reaction"] = "EX_" + diet_Cabbage_breastmilk.metabolite + "(e)"
diet_Carrot_breastmilk.reset_index(inplace=True)
diet_Carrot_breastmilk["reaction"] = "EX_" + diet_Carrot_breastmilk.metabolite + "(e)"
diet_Cauliflower_breastmilk.reset_index(inplace=True)
diet_Cauliflower_breastmilk["reaction"] = "EX_" + diet_Cauliflower_breastmilk.metabolite + "(e)"
diet_Celery_breastmilk.reset_index(inplace=True)
diet_Celery_breastmilk["reaction"] = "EX_" + diet_Celery_breastmilk.metabolite + "(e)"
diet_Cucumber_breastmilk.reset_index(inplace=True)
diet_Cucumber_breastmilk["reaction"] = "EX_" + diet_Cucumber_breastmilk.metabolite + "(e)"
diet_Eggplant_breastmilk.reset_index(inplace=True)
diet_Eggplant_breastmilk["reaction"] = "EX_" + diet_Eggplant_breastmilk.metabolite + "(e)"
diet_Green_beans_breastmilk.reset_index(inplace=True)
diet_Green_beans_breastmilk["reaction"] = "EX_" + diet_Green_beans_breastmilk.metabolite + "(e)"
diet_Green_capsicum_breastmilk.reset_index(inplace=True)
diet_Green_capsicum_breastmilk["reaction"] = "EX_" + diet_Green_capsicum_breastmilk.metabolite + "(e)"
diet_Lettuce_breastmilk.reset_index(inplace=True)
diet_Lettuce_breastmilk["reaction"] = "EX_" + diet_Lettuce_breastmilk.metabolite + "(e)"
diet_Mushroom_breastmilk.reset_index(inplace=True)
diet_Mushroom_breastmilk["reaction"] = "EX_" + diet_Mushroom_breastmilk.metabolite + "(e)"
diet_Onion_breastmilk.reset_index(inplace=True)
diet_Onion_breastmilk["reaction"] = "EX_" + diet_Onion_breastmilk.metabolite + "(e)"
diet_Pak_choi_breastmilk.reset_index(inplace=True)
diet_Pak_choi_breastmilk["reaction"] = "EX_" + diet_Pak_choi_breastmilk.metabolite + "(e)"
diet_Potato_breastmilk.reset_index(inplace=True)
diet_Potato_breastmilk["reaction"] = "EX_" + diet_Potato_breastmilk.metabolite + "(e)"
diet_Pumpkin_breastmilk.reset_index(inplace=True)
diet_Pumpkin_breastmilk["reaction"] = "EX_" + diet_Pumpkin_breastmilk.metabolite + "(e)"
diet_Sweetcorn_breastmilk.reset_index(inplace=True)
diet_Sweetcorn_breastmilk["reaction"] = "EX_" + diet_Sweetcorn_breastmilk.metabolite + "(e)"
diet_Spinach_breastmilk.reset_index(inplace=True)
diet_Spinach_breastmilk["reaction"] = "EX_" + diet_Spinach_breastmilk.metabolite + "(e)"
diet_Squash_breastmilk.reset_index(inplace=True)
diet_Squash_breastmilk["reaction"] = "EX_" + diet_Squash_breastmilk.metabolite + "(e)"
diet_Sweet_potato_breastmilk.reset_index(inplace=True)
diet_Sweet_potato_breastmilk["reaction"] = "EX_" + diet_Sweet_potato_breastmilk.metabolite + "(e)"
diet_Tomato_breastmilk.reset_index(inplace=True)
diet_Tomato_breastmilk["reaction"] = "EX_" + diet_Tomato_breastmilk.metabolite + "(e)"
diet_Yam_breastmilk.reset_index(inplace=True)
diet_Yam_breastmilk["reaction"] = "EX_" + diet_Yam_breastmilk.metabolite + "(e)"
diet_Zucchini_breastmilk.reset_index(inplace=True)
diet_Zucchini_breastmilk["reaction"] = "EX_" + diet_Zucchini_breastmilk.metabolite + "(e)"
diet_Apple_breastmilk.reset_index(inplace=True)
diet_Apple_breastmilk["reaction"] = "EX_" + diet_Apple_breastmilk.metabolite + "(e)"
diet_Banana_breastmilk.reset_index(inplace=True)
diet_Banana_breastmilk["reaction"] = "EX_" + diet_Banana_breastmilk.metabolite + "(e)"
diet_Blackcurrant_breastmilk.reset_index(inplace=True)
diet_Blackcurrant_breastmilk["reaction"] = "EX_" + diet_Blackcurrant_breastmilk.metabolite + "(e)"
diet_Blueberries_breastmilk.reset_index(inplace=True)
diet_Blueberries_breastmilk["reaction"] = "EX_" + diet_Blueberries_breastmilk.metabolite + "(e)"
diet_Cherry_breastmilk.reset_index(inplace=True)
diet_Cherry_breastmilk["reaction"] = "EX_" + diet_Cherry_breastmilk.metabolite + "(e)"
diet_Feijoa_breastmilk.reset_index(inplace=True)
diet_Feijoa_breastmilk["reaction"] = "EX_" + diet_Feijoa_breastmilk.metabolite + "(e)"
diet_Gold_kiwifruit_breastmilk.reset_index(inplace=True)
diet_Gold_kiwifruit_breastmilk["reaction"] = "EX_" + diet_Gold_kiwifruit_breastmilk.metabolite + "(e)"
diet_Grape_breastmilk.reset_index(inplace=True)
diet_Grape_breastmilk["reaction"] = "EX_" + diet_Grape_breastmilk.metabolite + "(e)"
diet_Grapefruit_breastmilk.reset_index(inplace=True)
diet_Grapefruit_breastmilk["reaction"] = "EX_" + diet_Grapefruit_breastmilk.metabolite + "(e)"
diet_Green_kiwifruit_breastmilk.reset_index(inplace=True)
diet_Green_kiwifruit_breastmilk["reaction"] = "EX_" + diet_Green_kiwifruit_breastmilk.metabolite + "(e)"
diet_Mandarin_breastmilk.reset_index(inplace=True)
diet_Mandarin_breastmilk["reaction"] = "EX_" + diet_Mandarin_breastmilk.metabolite + "(e)"
diet_Mango_breastmilk.reset_index(inplace=True)
diet_Mango_breastmilk["reaction"] = "EX_" + diet_Mango_breastmilk.metabolite + "(e)"
diet_Melon_breastmilk.reset_index(inplace=True)
diet_Melon_breastmilk["reaction"] = "EX_" + diet_Melon_breastmilk.metabolite + "(e)"
diet_Nectarine_breastmilk.reset_index(inplace=True)
diet_Nectarine_breastmilk["reaction"] = "EX_" + diet_Nectarine_breastmilk.metabolite + "(e)"
diet_Orange_breastmilk.reset_index(inplace=True)
diet_Orange_breastmilk["reaction"] = "EX_" + diet_Orange_breastmilk.metabolite + "(e)"
diet_Peache_breastmilk.reset_index(inplace=True)
diet_Peache_breastmilk["reaction"] = "EX_" + diet_Peache_breastmilk.metabolite + "(e)"
diet_Pear_breastmilk.reset_index(inplace=True)
diet_Pear_breastmilk["reaction"] = "EX_" + diet_Pear_breastmilk.metabolite + "(e)"
diet_Pineapple_breastmilk.reset_index(inplace=True)
diet_Pineapple_breastmilk["reaction"] = "EX_" + diet_Pineapple_breastmilk.metabolite + "(e)"
diet_Plum_breastmilk.reset_index(inplace=True)
diet_Plum_breastmilk["reaction"] = "EX_" + diet_Plum_breastmilk.metabolite + "(e)"
diet_Raspberries_breastmilk.reset_index(inplace=True)
diet_Raspberries_breastmilk["reaction"] = "EX_" + diet_Raspberries_breastmilk.metabolite + "(e)"
diet_Strawberries_breastmilk.reset_index(inplace=True)
diet_Strawberries_breastmilk["reaction"] = "EX_" + diet_Strawberries_breastmilk.metabolite + "(e)"
diet_Barley_breastmilk.reset_index(inplace=True)
diet_Barley_breastmilk["reaction"] = "EX_" + diet_Barley_breastmilk.metabolite + "(e)"
diet_Barley_cereal_breastmilk.reset_index(inplace=True)
diet_Barley_cereal_breastmilk["reaction"] = "EX_" + diet_Barley_cereal_breastmilk.metabolite + "(e)"
diet_Couscous_breastmilk.reset_index(inplace=True)
diet_Couscous_breastmilk["reaction"] = "EX_" + diet_Couscous_breastmilk.metabolite + "(e)"
diet_Noodles_breastmilk.reset_index(inplace=True)
diet_Noodles_breastmilk["reaction"] = "EX_" + diet_Noodles_breastmilk.metabolite + "(e)"
diet_Oat_cereal_breastmilk.reset_index(inplace=True)
diet_Oat_cereal_breastmilk["reaction"] = "EX_" + diet_Oat_cereal_breastmilk.metabolite + "(e)"
diet_Pasta_breastmilk.reset_index(inplace=True)
diet_Pasta_breastmilk["reaction"] = "EX_" + diet_Pasta_breastmilk.metabolite + "(e)"
diet_Rice_breastmilk.reset_index(inplace=True)
diet_Rice_breastmilk["reaction"] = "EX_" + diet_Rice_breastmilk.metabolite + "(e)"
diet_Rice_cereal_breastmilk.reset_index(inplace=True)
diet_Rice_cereal_breastmilk["reaction"] = "EX_" + diet_Rice_cereal_breastmilk.metabolite + "(e)"
diet_Tapioca_pudding_breastmilk.reset_index(inplace=True)
diet_Tapioca_pudding_breastmilk["reaction"] = "EX_" + diet_Tapioca_pudding_breastmilk.metabolite + "(e)"
diet_White_bread_breastmilk.reset_index(inplace=True)
diet_White_bread_breastmilk["reaction"] = "EX_" + diet_White_bread_breastmilk.metabolite + "(e)"
diet_Wholegrain_bread_breastmilk.reset_index(inplace=True)
diet_Wholegrain_bread_breastmilk["reaction"] = "EX_" + diet_Wholegrain_bread_breastmilk.metabolite + "(e)"
diet_Cottage_cheese_breastmilk.reset_index(inplace=True)
diet_Cottage_cheese_breastmilk["reaction"] = "EX_" + diet_Cottage_cheese_breastmilk.metabolite + "(e)"
diet_Eggs_breastmilk.reset_index(inplace=True)
diet_Eggs_breastmilk["reaction"] = "EX_" + diet_Eggs_breastmilk.metabolite + "(e)"
diet_Mozzarella_cheese_breastmilk.reset_index(inplace=True)
diet_Mozzarella_cheese_breastmilk["reaction"] = "EX_" + diet_Mozzarella_cheese_breastmilk.metabolite + "(e)"
diet_Soymilk_breastmilk.reset_index(inplace=True)
diet_Soymilk_breastmilk["reaction"] = "EX_" + diet_Soymilk_breastmilk.metabolite + "(e)"
diet_Tofu_breastmilk.reset_index(inplace=True)
diet_Tofu_breastmilk["reaction"] = "EX_" + diet_Tofu_breastmilk.metabolite + "(e)"
diet_Whole_milk_breastmilk.reset_index(inplace=True)
diet_Whole_milk_breastmilk["reaction"] = "EX_" + diet_Whole_milk_breastmilk.metabolite + "(e)"
diet_Yoghurt_breastmilk.reset_index(inplace=True)
diet_Yoghurt_breastmilk["reaction"] = "EX_" + diet_Yoghurt_breastmilk.metabolite + "(e)"
diet_Beef_breastmilk.reset_index(inplace=True)
diet_Beef_breastmilk["reaction"] = "EX_" + diet_Beef_breastmilk.metabolite + "(e)"
diet_Chicken_breastmilk.reset_index(inplace=True)
diet_Chicken_breastmilk["reaction"] = "EX_" + diet_Chicken_breastmilk.metabolite + "(e)"
diet_Codfish_breastmilk.reset_index(inplace=True)
diet_Codfish_breastmilk["reaction"] = "EX_" + diet_Codfish_breastmilk.metabolite + "(e)"
diet_Lamb_breastmilk.reset_index(inplace=True)
diet_Lamb_breastmilk["reaction"] = "EX_" + diet_Lamb_breastmilk.metabolite + "(e)"
diet_Mackerel_breastmilk.reset_index(inplace=True)
diet_Mackerel_breastmilk["reaction"] = "EX_" + diet_Mackerel_breastmilk.metabolite + "(e)"
diet_Mussels_breastmilk.reset_index(inplace=True)
diet_Mussels_breastmilk["reaction"] = "EX_" + diet_Mussels_breastmilk.metabolite + "(e)"
diet_Pork_breastmilk.reset_index(inplace=True)
diet_Pork_breastmilk["reaction"] = "EX_" + diet_Pork_breastmilk.metabolite + "(e)"
diet_Salmon_breastmilk.reset_index(inplace=True)
diet_Salmon_breastmilk["reaction"] = "EX_" + diet_Salmon_breastmilk.metabolite + "(e)"
diet_Shrimp_breastmilk.reset_index(inplace=True)
diet_Shrimp_breastmilk["reaction"] = "EX_" + diet_Shrimp_breastmilk.metabolite + "(e)"
diet_Tuna_breastmilk.reset_index(inplace=True)
diet_Tuna_breastmilk["reaction"] = "EX_" + diet_Tuna_breastmilk.metabolite + "(e)"
diet_Turkey_breastmilk.reset_index(inplace=True)
diet_Turkey_breastmilk["reaction"] = "EX_" + diet_Turkey_breastmilk.metabolite + "(e)"
diet_Almond_breastmilk.reset_index(inplace=True)
diet_Almond_breastmilk["reaction"] = "EX_" + diet_Almond_breastmilk.metabolite + "(e)"
diet_Black_beans_breastmilk.reset_index(inplace=True)
diet_Black_beans_breastmilk["reaction"] = "EX_" + diet_Black_beans_breastmilk.metabolite + "(e)"
diet_Cashew_breastmilk.reset_index(inplace=True)
diet_Cashew_breastmilk["reaction"] = "EX_" + diet_Cashew_breastmilk.metabolite + "(e)"
diet_Chia_breastmilk.reset_index(inplace=True)
diet_Chia_breastmilk["reaction"] = "EX_" + diet_Chia_breastmilk.metabolite + "(e)"
diet_Chickpea_breastmilk.reset_index(inplace=True)
diet_Chickpea_breastmilk["reaction"] = "EX_" + diet_Chickpea_breastmilk.metabolite + "(e)"
diet_Green_peas_breastmilk.reset_index(inplace=True)
diet_Green_peas_breastmilk["reaction"] = "EX_" + diet_Green_peas_breastmilk.metabolite + "(e)"
diet_Hazelnut_breastmilk.reset_index(inplace=True)
diet_Hazelnut_breastmilk["reaction"] = "EX_" + diet_Hazelnut_breastmilk.metabolite + "(e)"
diet_Lentils_breastmilk.reset_index(inplace=True)
diet_Lentils_breastmilk["reaction"] = "EX_" + diet_Lentils_breastmilk.metabolite + "(e)"
diet_Peanut_breastmilk.reset_index(inplace=True)
diet_Peanut_breastmilk["reaction"] = "EX_" + diet_Peanut_breastmilk.metabolite + "(e)"
diet_Pecans_breastmilk.reset_index(inplace=True)
diet_Pecans_breastmilk["reaction"] = "EX_" + diet_Pecans_breastmilk.metabolite + "(e)"
diet_Pumpkin_seed_breastmilk.reset_index(inplace=True)
diet_Pumpkin_seed_breastmilk["reaction"] = "EX_" + diet_Pumpkin_seed_breastmilk.metabolite + "(e)"
diet_Red_beans_breastmilk.reset_index(inplace=True)
diet_Red_beans_breastmilk["reaction"] = "EX_" + diet_Red_beans_breastmilk.metabolite + "(e)"
diet_Soybean_breastmilk.reset_index(inplace=True)
diet_Soybean_breastmilk["reaction"] = "EX_" + diet_Soybean_breastmilk.metabolite + "(e)"
diet_Split_peas_breastmilk.reset_index(inplace=True)
diet_Split_peas_breastmilk["reaction"] = "EX_" + diet_Split_peas_breastmilk.metabolite + "(e)"
diet_Sunflower_seed_breastmilk.reset_index(inplace=True)
diet_Sunflower_seed_breastmilk["reaction"] = "EX_" + diet_Sunflower_seed_breastmilk.metabolite + "(e)"
diet_White_beans_breastmilk.reset_index(inplace=True)
diet_White_beans_breastmilk["reaction"] = "EX_" + diet_White_beans_breastmilk.metabolite + "(e)"

#Adding information in our diet table
skeleton_Broccoli_breastmilk = pd.merge(diet_Broccoli_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Broccoli_breastmilk["global_id"] = skeleton_Broccoli_breastmilk.reaction
skeleton_Broccoli_breastmilk["reaction"] = "EX_" + skeleton_Broccoli_breastmilk.metabolite + "_m"
skeleton_Brussel_breastmilk = pd.merge(diet_Brussel_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Brussel_breastmilk["global_id"] = skeleton_Brussel_breastmilk.reaction
skeleton_Brussel_breastmilk["reaction"] = "EX_" + skeleton_Brussel_breastmilk.metabolite + "_m"
skeleton_Cabbage_breastmilk = pd.merge(diet_Cabbage_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Cabbage_breastmilk["global_id"] = skeleton_Cabbage_breastmilk.reaction
skeleton_Cabbage_breastmilk["reaction"] = "EX_" + skeleton_Cabbage_breastmilk.metabolite + "_m"
skeleton_Carrot_breastmilk = pd.merge(diet_Carrot_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Carrot_breastmilk["global_id"] = skeleton_Carrot_breastmilk.reaction
skeleton_Carrot_breastmilk["reaction"] = "EX_" + skeleton_Carrot_breastmilk.metabolite + "_m"
skeleton_Cauliflower_breastmilk = pd.merge(diet_Cauliflower_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Cauliflower_breastmilk["global_id"] = skeleton_Cauliflower_breastmilk.reaction
skeleton_Cauliflower_breastmilk["reaction"] = "EX_" + skeleton_Cauliflower_breastmilk.metabolite + "_m"
skeleton_Celery_breastmilk = pd.merge(diet_Celery_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Celery_breastmilk["global_id"] = skeleton_Celery_breastmilk.reaction
skeleton_Celery_breastmilk["reaction"] = "EX_" + skeleton_Celery_breastmilk.metabolite + "_m"
skeleton_Cucumber_breastmilk = pd.merge(diet_Cucumber_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Cucumber_breastmilk["global_id"] = skeleton_Cucumber_breastmilk.reaction
skeleton_Cucumber_breastmilk["reaction"] = "EX_" + skeleton_Cucumber_breastmilk.metabolite + "_m"
skeleton_Eggplant_breastmilk = pd.merge(diet_Eggplant_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Eggplant_breastmilk["global_id"] = skeleton_Eggplant_breastmilk.reaction
skeleton_Eggplant_breastmilk["reaction"] = "EX_" + skeleton_Eggplant_breastmilk.metabolite + "_m"
skeleton_Green_beans_breastmilk = pd.merge(diet_Green_beans_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Green_beans_breastmilk["global_id"] = skeleton_Green_beans_breastmilk.reaction
skeleton_Green_beans_breastmilk["reaction"] = "EX_" + skeleton_Green_beans_breastmilk.metabolite + "_m"
skeleton_Green_capsicum_breastmilk = pd.merge(diet_Green_capsicum_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Green_capsicum_breastmilk["global_id"] = skeleton_Green_capsicum_breastmilk.reaction
skeleton_Green_capsicum_breastmilk["reaction"] = "EX_" + skeleton_Green_capsicum_breastmilk.metabolite + "_m"
skeleton_Lettuce_breastmilk = pd.merge(diet_Lettuce_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Lettuce_breastmilk["global_id"] = skeleton_Lettuce_breastmilk.reaction
skeleton_Lettuce_breastmilk["reaction"] = "EX_" + skeleton_Lettuce_breastmilk.metabolite + "_m"
skeleton_Mushroom_breastmilk = pd.merge(diet_Mushroom_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Mushroom_breastmilk["global_id"] = skeleton_Mushroom_breastmilk.reaction
skeleton_Mushroom_breastmilk["reaction"] = "EX_" + skeleton_Mushroom_breastmilk.metabolite + "_m"
skeleton_Onion_breastmilk = pd.merge(diet_Onion_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Onion_breastmilk["global_id"] = skeleton_Onion_breastmilk.reaction
skeleton_Onion_breastmilk["reaction"] = "EX_" + skeleton_Onion_breastmilk.metabolite + "_m"
skeleton_Pak_choi_breastmilk = pd.merge(diet_Pak_choi_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Pak_choi_breastmilk["global_id"] = skeleton_Pak_choi_breastmilk.reaction
skeleton_Pak_choi_breastmilk["reaction"] = "EX_" + skeleton_Pak_choi_breastmilk.metabolite + "_m"
skeleton_Potato_breastmilk = pd.merge(diet_Potato_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Potato_breastmilk["global_id"] = skeleton_Potato_breastmilk.reaction
skeleton_Potato_breastmilk["reaction"] = "EX_" + skeleton_Potato_breastmilk.metabolite + "_m"
skeleton_Pumpkin_breastmilk = pd.merge(diet_Pumpkin_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Pumpkin_breastmilk["global_id"] = skeleton_Pumpkin_breastmilk.reaction
skeleton_Pumpkin_breastmilk["reaction"] = "EX_" + skeleton_Pumpkin_breastmilk.metabolite + "_m"
skeleton_Sweetcorn_breastmilk = pd.merge(diet_Sweetcorn_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Sweetcorn_breastmilk["global_id"] = skeleton_Sweetcorn_breastmilk.reaction
skeleton_Sweetcorn_breastmilk["reaction"] = "EX_" + skeleton_Sweetcorn_breastmilk.metabolite + "_m"
skeleton_Spinach_breastmilk = pd.merge(diet_Spinach_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Spinach_breastmilk["global_id"] = skeleton_Spinach_breastmilk.reaction
skeleton_Spinach_breastmilk["reaction"] = "EX_" + skeleton_Spinach_breastmilk.metabolite + "_m"
skeleton_Squash_breastmilk = pd.merge(diet_Squash_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Squash_breastmilk["global_id"] = skeleton_Squash_breastmilk.reaction
skeleton_Squash_breastmilk["reaction"] = "EX_" + skeleton_Squash_breastmilk.metabolite + "_m"
skeleton_Sweet_potato_breastmilk = pd.merge(diet_Sweet_potato_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Sweet_potato_breastmilk["global_id"] = skeleton_Sweet_potato_breastmilk.reaction
skeleton_Sweet_potato_breastmilk["reaction"] = "EX_" + skeleton_Sweet_potato_breastmilk.metabolite + "_m"
skeleton_Tomato_breastmilk = pd.merge(diet_Tomato_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Tomato_breastmilk["global_id"] = skeleton_Tomato_breastmilk.reaction
skeleton_Tomato_breastmilk["reaction"] = "EX_" + skeleton_Tomato_breastmilk.metabolite + "_m"
skeleton_Yam_breastmilk = pd.merge(diet_Yam_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Yam_breastmilk["global_id"] = skeleton_Yam_breastmilk.reaction
skeleton_Yam_breastmilk["reaction"] = "EX_" + skeleton_Yam_breastmilk.metabolite + "_m"
skeleton_Zucchini_breastmilk = pd.merge(diet_Zucchini_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Zucchini_breastmilk["global_id"] = skeleton_Zucchini_breastmilk.reaction
skeleton_Zucchini_breastmilk["reaction"] = "EX_" + skeleton_Zucchini_breastmilk.metabolite + "_m"
skeleton_Apple_breastmilk = pd.merge(diet_Apple_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Apple_breastmilk["global_id"] = skeleton_Apple_breastmilk.reaction
skeleton_Apple_breastmilk["reaction"] = "EX_" + skeleton_Apple_breastmilk.metabolite + "_m"
skeleton_Banana_breastmilk = pd.merge(diet_Banana_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Banana_breastmilk["global_id"] = skeleton_Banana_breastmilk.reaction
skeleton_Banana_breastmilk["reaction"] = "EX_" + skeleton_Banana_breastmilk.metabolite + "_m"
skeleton_Blackcurrant_breastmilk = pd.merge(diet_Blackcurrant_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Blackcurrant_breastmilk["global_id"] = skeleton_Blackcurrant_breastmilk.reaction
skeleton_Blackcurrant_breastmilk["reaction"] = "EX_" + skeleton_Blackcurrant_breastmilk.metabolite + "_m"
skeleton_Blueberries_breastmilk = pd.merge(diet_Blueberries_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Blueberries_breastmilk["global_id"] = skeleton_Blueberries_breastmilk.reaction
skeleton_Blueberries_breastmilk["reaction"] = "EX_" + skeleton_Blueberries_breastmilk.metabolite + "_m"
skeleton_Cherry_breastmilk = pd.merge(diet_Cherry_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Cherry_breastmilk["global_id"] = skeleton_Cherry_breastmilk.reaction
skeleton_Cherry_breastmilk["reaction"] = "EX_" + skeleton_Cherry_breastmilk.metabolite + "_m"
skeleton_Feijoa_breastmilk = pd.merge(diet_Feijoa_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Feijoa_breastmilk["global_id"] = skeleton_Feijoa_breastmilk.reaction
skeleton_Feijoa_breastmilk["reaction"] = "EX_" + skeleton_Feijoa_breastmilk.metabolite + "_m"
skeleton_Gold_kiwifruit_breastmilk = pd.merge(diet_Gold_kiwifruit_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Gold_kiwifruit_breastmilk["global_id"] = skeleton_Gold_kiwifruit_breastmilk.reaction
skeleton_Gold_kiwifruit_breastmilk["reaction"] = "EX_" + skeleton_Gold_kiwifruit_breastmilk.metabolite + "_m"
skeleton_Grape_breastmilk = pd.merge(diet_Grape_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Grape_breastmilk["global_id"] = skeleton_Grape_breastmilk.reaction
skeleton_Grape_breastmilk["reaction"] = "EX_" + skeleton_Grape_breastmilk.metabolite + "_m"
skeleton_Grapefruit_breastmilk = pd.merge(diet_Grapefruit_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Grapefruit_breastmilk["global_id"] = skeleton_Grapefruit_breastmilk.reaction
skeleton_Grapefruit_breastmilk["reaction"] = "EX_" + skeleton_Grapefruit_breastmilk.metabolite + "_m"
skeleton_Green_kiwifruit_breastmilk = pd.merge(diet_Green_kiwifruit_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Green_kiwifruit_breastmilk["global_id"] = skeleton_Green_kiwifruit_breastmilk.reaction
skeleton_Green_kiwifruit_breastmilk["reaction"] = "EX_" + skeleton_Green_kiwifruit_breastmilk.metabolite + "_m"
skeleton_Mandarin_breastmilk = pd.merge(diet_Mandarin_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Mandarin_breastmilk["global_id"] = skeleton_Mandarin_breastmilk.reaction
skeleton_Mandarin_breastmilk["reaction"] = "EX_" + skeleton_Mandarin_breastmilk.metabolite + "_m"
skeleton_Mango_breastmilk = pd.merge(diet_Mango_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Mango_breastmilk["global_id"] = skeleton_Mango_breastmilk.reaction
skeleton_Mango_breastmilk["reaction"] = "EX_" + skeleton_Mango_breastmilk.metabolite + "_m"
skeleton_Melon_breastmilk = pd.merge(diet_Melon_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Melon_breastmilk["global_id"] = skeleton_Melon_breastmilk.reaction
skeleton_Melon_breastmilk["reaction"] = "EX_" + skeleton_Melon_breastmilk.metabolite + "_m"
skeleton_Nectarine_breastmilk = pd.merge(diet_Nectarine_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Nectarine_breastmilk["global_id"] = skeleton_Nectarine_breastmilk.reaction
skeleton_Nectarine_breastmilk["reaction"] = "EX_" + skeleton_Nectarine_breastmilk.metabolite + "_m"
skeleton_Orange_breastmilk = pd.merge(diet_Orange_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Orange_breastmilk["global_id"] = skeleton_Orange_breastmilk.reaction
skeleton_Orange_breastmilk["reaction"] = "EX_" + skeleton_Orange_breastmilk.metabolite + "_m"
skeleton_Peache_breastmilk = pd.merge(diet_Peache_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Peache_breastmilk["global_id"] = skeleton_Peache_breastmilk.reaction
skeleton_Peache_breastmilk["reaction"] = "EX_" + skeleton_Peache_breastmilk.metabolite + "_m"
skeleton_Pear_breastmilk = pd.merge(diet_Pear_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Pear_breastmilk["global_id"] = skeleton_Pear_breastmilk.reaction
skeleton_Pear_breastmilk["reaction"] = "EX_" + skeleton_Pear_breastmilk.metabolite + "_m"
skeleton_Pineapple_breastmilk = pd.merge(diet_Pineapple_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Pineapple_breastmilk["global_id"] = skeleton_Pineapple_breastmilk.reaction
skeleton_Pineapple_breastmilk["reaction"] = "EX_" + skeleton_Pineapple_breastmilk.metabolite + "_m"
skeleton_Plum_breastmilk = pd.merge(diet_Plum_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Plum_breastmilk["global_id"] = skeleton_Plum_breastmilk.reaction
skeleton_Plum_breastmilk["reaction"] = "EX_" + skeleton_Plum_breastmilk.metabolite + "_m"
skeleton_Raspberries_breastmilk = pd.merge(diet_Raspberries_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Raspberries_breastmilk["global_id"] = skeleton_Raspberries_breastmilk.reaction
skeleton_Raspberries_breastmilk["reaction"] = "EX_" + skeleton_Raspberries_breastmilk.metabolite + "_m"
skeleton_Strawberries_breastmilk = pd.merge(diet_Strawberries_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Strawberries_breastmilk["global_id"] = skeleton_Strawberries_breastmilk.reaction
skeleton_Strawberries_breastmilk["reaction"] = "EX_" + skeleton_Strawberries_breastmilk.metabolite + "_m"
skeleton_Barley_breastmilk = pd.merge(diet_Barley_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Barley_breastmilk["global_id"] = skeleton_Barley_breastmilk.reaction
skeleton_Barley_breastmilk["reaction"] = "EX_" + skeleton_Barley_breastmilk.metabolite + "_m"
skeleton_Barley_cereal_breastmilk = pd.merge(diet_Barley_cereal_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Barley_cereal_breastmilk["global_id"] = skeleton_Barley_cereal_breastmilk.reaction
skeleton_Barley_cereal_breastmilk["reaction"] = "EX_" + skeleton_Barley_cereal_breastmilk.metabolite + "_m"
skeleton_Couscous_breastmilk = pd.merge(diet_Couscous_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Couscous_breastmilk["global_id"] = skeleton_Couscous_breastmilk.reaction
skeleton_Couscous_breastmilk["reaction"] = "EX_" + skeleton_Couscous_breastmilk.metabolite + "_m"
skeleton_Noodles_breastmilk = pd.merge(diet_Noodles_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Noodles_breastmilk["global_id"] = skeleton_Noodles_breastmilk.reaction
skeleton_Noodles_breastmilk["reaction"] = "EX_" + skeleton_Noodles_breastmilk.metabolite + "_m"
skeleton_Oat_cereal_breastmilk = pd.merge(diet_Oat_cereal_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Oat_cereal_breastmilk["global_id"] = skeleton_Oat_cereal_breastmilk.reaction
skeleton_Oat_cereal_breastmilk["reaction"] = "EX_" + skeleton_Oat_cereal_breastmilk.metabolite + "_m"
skeleton_Pasta_breastmilk = pd.merge(diet_Pasta_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Pasta_breastmilk["global_id"] = skeleton_Pasta_breastmilk.reaction
skeleton_Pasta_breastmilk["reaction"] = "EX_" + skeleton_Pasta_breastmilk.metabolite + "_m"
skeleton_Rice_breastmilk = pd.merge(diet_Rice_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Rice_breastmilk["global_id"] = skeleton_Rice_breastmilk.reaction
skeleton_Rice_breastmilk["reaction"] = "EX_" + skeleton_Rice_breastmilk.metabolite + "_m"
skeleton_Rice_cereal_breastmilk = pd.merge(diet_Rice_cereal_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Rice_cereal_breastmilk["global_id"] = skeleton_Rice_cereal_breastmilk.reaction
skeleton_Rice_cereal_breastmilk["reaction"] = "EX_" + skeleton_Rice_cereal_breastmilk.metabolite + "_m"
skeleton_Tapioca_pudding_breastmilk = pd.merge(diet_Tapioca_pudding_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Tapioca_pudding_breastmilk["global_id"] = skeleton_Tapioca_pudding_breastmilk.reaction
skeleton_Tapioca_pudding_breastmilk["reaction"] = "EX_" + skeleton_Tapioca_pudding_breastmilk.metabolite + "_m"
skeleton_White_bread_breastmilk = pd.merge(diet_White_bread_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_White_bread_breastmilk["global_id"] = skeleton_White_bread_breastmilk.reaction
skeleton_White_bread_breastmilk["reaction"] = "EX_" + skeleton_White_bread_breastmilk.metabolite + "_m"
skeleton_Wholegrain_bread_breastmilk = pd.merge(diet_Wholegrain_bread_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Wholegrain_bread_breastmilk["global_id"] = skeleton_Wholegrain_bread_breastmilk.reaction
skeleton_Wholegrain_bread_breastmilk["reaction"] = "EX_" + skeleton_Wholegrain_bread_breastmilk.metabolite + "_m"
skeleton_Cottage_cheese_breastmilk = pd.merge(diet_Cottage_cheese_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Cottage_cheese_breastmilk["global_id"] = skeleton_Cottage_cheese_breastmilk.reaction
skeleton_Cottage_cheese_breastmilk["reaction"] = "EX_" + skeleton_Cottage_cheese_breastmilk.metabolite + "_m"
skeleton_Eggs_breastmilk = pd.merge(diet_Eggs_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Eggs_breastmilk["global_id"] = skeleton_Eggs_breastmilk.reaction
skeleton_Eggs_breastmilk["reaction"] = "EX_" + skeleton_Eggs_breastmilk.metabolite + "_m"
skeleton_Mozzarella_cheese_breastmilk = pd.merge(diet_Mozzarella_cheese_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Mozzarella_cheese_breastmilk["global_id"] = skeleton_Mozzarella_cheese_breastmilk.reaction
skeleton_Mozzarella_cheese_breastmilk["reaction"] = "EX_" + skeleton_Mozzarella_cheese_breastmilk.metabolite + "_m"
skeleton_Soymilk_breastmilk = pd.merge(diet_Soymilk_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Soymilk_breastmilk["global_id"] = skeleton_Soymilk_breastmilk.reaction
skeleton_Soymilk_breastmilk["reaction"] = "EX_" + skeleton_Soymilk_breastmilk.metabolite + "_m"
skeleton_Tofu_breastmilk = pd.merge(diet_Tofu_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Tofu_breastmilk["global_id"] = skeleton_Tofu_breastmilk.reaction
skeleton_Tofu_breastmilk["reaction"] = "EX_" + skeleton_Tofu_breastmilk.metabolite + "_m"
skeleton_Whole_milk_breastmilk = pd.merge(diet_Whole_milk_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Whole_milk_breastmilk["global_id"] = skeleton_Whole_milk_breastmilk.reaction
skeleton_Whole_milk_breastmilk["reaction"] = "EX_" + skeleton_Whole_milk_breastmilk.metabolite + "_m"
skeleton_Yoghurt_breastmilk = pd.merge(diet_Yoghurt_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Yoghurt_breastmilk["global_id"] = skeleton_Yoghurt_breastmilk.reaction
skeleton_Yoghurt_breastmilk["reaction"] = "EX_" + skeleton_Yoghurt_breastmilk.metabolite + "_m"
skeleton_Beef_breastmilk = pd.merge(diet_Beef_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Beef_breastmilk["global_id"] = skeleton_Beef_breastmilk.reaction
skeleton_Beef_breastmilk["reaction"] = "EX_" + skeleton_Beef_breastmilk.metabolite + "_m"
skeleton_Chicken_breastmilk = pd.merge(diet_Chicken_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Chicken_breastmilk["global_id"] = skeleton_Chicken_breastmilk.reaction
skeleton_Chicken_breastmilk["reaction"] = "EX_" + skeleton_Chicken_breastmilk.metabolite + "_m"
skeleton_Codfish_breastmilk = pd.merge(diet_Codfish_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Codfish_breastmilk["global_id"] = skeleton_Codfish_breastmilk.reaction
skeleton_Codfish_breastmilk["reaction"] = "EX_" + skeleton_Codfish_breastmilk.metabolite + "_m"
skeleton_Lamb_breastmilk = pd.merge(diet_Lamb_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Lamb_breastmilk["global_id"] = skeleton_Lamb_breastmilk.reaction
skeleton_Lamb_breastmilk["reaction"] = "EX_" + skeleton_Lamb_breastmilk.metabolite + "_m"
skeleton_Mackerel_breastmilk = pd.merge(diet_Mackerel_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Mackerel_breastmilk["global_id"] = skeleton_Mackerel_breastmilk.reaction
skeleton_Mackerel_breastmilk["reaction"] = "EX_" + skeleton_Mackerel_breastmilk.metabolite + "_m"
skeleton_Mussels_breastmilk = pd.merge(diet_Mussels_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Mussels_breastmilk["global_id"] = skeleton_Mussels_breastmilk.reaction
skeleton_Mussels_breastmilk["reaction"] = "EX_" + skeleton_Mussels_breastmilk.metabolite + "_m"
skeleton_Pork_breastmilk = pd.merge(diet_Pork_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Pork_breastmilk["global_id"] = skeleton_Pork_breastmilk.reaction
skeleton_Pork_breastmilk["reaction"] = "EX_" + skeleton_Pork_breastmilk.metabolite + "_m"
skeleton_Salmon_breastmilk = pd.merge(diet_Salmon_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Salmon_breastmilk["global_id"] = skeleton_Salmon_breastmilk.reaction
skeleton_Salmon_breastmilk["reaction"] = "EX_" + skeleton_Salmon_breastmilk.metabolite + "_m"
skeleton_Shrimp_breastmilk = pd.merge(diet_Shrimp_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Shrimp_breastmilk["global_id"] = skeleton_Shrimp_breastmilk.reaction
skeleton_Shrimp_breastmilk["reaction"] = "EX_" + skeleton_Shrimp_breastmilk.metabolite + "_m"
skeleton_Tuna_breastmilk = pd.merge(diet_Tuna_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Tuna_breastmilk["global_id"] = skeleton_Tuna_breastmilk.reaction
skeleton_Tuna_breastmilk["reaction"] = "EX_" + skeleton_Tuna_breastmilk.metabolite + "_m"
skeleton_Turkey_breastmilk = pd.merge(diet_Turkey_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Turkey_breastmilk["global_id"] = skeleton_Turkey_breastmilk.reaction
skeleton_Turkey_breastmilk["reaction"] = "EX_" + skeleton_Turkey_breastmilk.metabolite + "_m"
skeleton_Almond_breastmilk = pd.merge(diet_Almond_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Almond_breastmilk["global_id"] = skeleton_Almond_breastmilk.reaction
skeleton_Almond_breastmilk["reaction"] = "EX_" + skeleton_Almond_breastmilk.metabolite + "_m"
skeleton_Black_beans_breastmilk = pd.merge(diet_Black_beans_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Black_beans_breastmilk["global_id"] = skeleton_Black_beans_breastmilk.reaction
skeleton_Black_beans_breastmilk["reaction"] = "EX_" + skeleton_Black_beans_breastmilk.metabolite + "_m"
skeleton_Cashew_breastmilk = pd.merge(diet_Cashew_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Cashew_breastmilk["global_id"] = skeleton_Cashew_breastmilk.reaction
skeleton_Cashew_breastmilk["reaction"] = "EX_" + skeleton_Cashew_breastmilk.metabolite + "_m"
skeleton_Chia_breastmilk = pd.merge(diet_Chia_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Chia_breastmilk["global_id"] = skeleton_Chia_breastmilk.reaction
skeleton_Chia_breastmilk["reaction"] = "EX_" + skeleton_Chia_breastmilk.metabolite + "_m"
skeleton_Chickpea_breastmilk = pd.merge(diet_Chickpea_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Chickpea_breastmilk["global_id"] = skeleton_Chickpea_breastmilk.reaction
skeleton_Chickpea_breastmilk["reaction"] = "EX_" + skeleton_Chickpea_breastmilk.metabolite + "_m"
skeleton_Green_peas_breastmilk = pd.merge(diet_Green_peas_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Green_peas_breastmilk["global_id"] = skeleton_Green_peas_breastmilk.reaction
skeleton_Green_peas_breastmilk["reaction"] = "EX_" + skeleton_Green_peas_breastmilk.metabolite + "_m"
skeleton_Hazelnut_breastmilk = pd.merge(diet_Hazelnut_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Hazelnut_breastmilk["global_id"] = skeleton_Hazelnut_breastmilk.reaction
skeleton_Hazelnut_breastmilk["reaction"] = "EX_" + skeleton_Hazelnut_breastmilk.metabolite + "_m"
skeleton_Lentils_breastmilk = pd.merge(diet_Lentils_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Lentils_breastmilk["global_id"] = skeleton_Lentils_breastmilk.reaction
skeleton_Lentils_breastmilk["reaction"] = "EX_" + skeleton_Lentils_breastmilk.metabolite + "_m"
skeleton_Peanut_breastmilk = pd.merge(diet_Peanut_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Peanut_breastmilk["global_id"] = skeleton_Peanut_breastmilk.reaction
skeleton_Peanut_breastmilk["reaction"] = "EX_" + skeleton_Peanut_breastmilk.metabolite + "_m"
skeleton_Pecans_breastmilk = pd.merge(diet_Pecans_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Pecans_breastmilk["global_id"] = skeleton_Pecans_breastmilk.reaction
skeleton_Pecans_breastmilk["reaction"] = "EX_" + skeleton_Pecans_breastmilk.metabolite + "_m"
skeleton_Pumpkin_seed_breastmilk = pd.merge(diet_Pumpkin_seed_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Pumpkin_seed_breastmilk["global_id"] = skeleton_Pumpkin_seed_breastmilk.reaction
skeleton_Pumpkin_seed_breastmilk["reaction"] = "EX_" + skeleton_Pumpkin_seed_breastmilk.metabolite + "_m"
skeleton_Red_beans_breastmilk = pd.merge(diet_Red_beans_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Red_beans_breastmilk["global_id"] = skeleton_Red_beans_breastmilk.reaction
skeleton_Red_beans_breastmilk["reaction"] = "EX_" + skeleton_Red_beans_breastmilk.metabolite + "_m"
skeleton_Soybean_breastmilk = pd.merge(diet_Soybean_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Soybean_breastmilk["global_id"] = skeleton_Soybean_breastmilk.reaction
skeleton_Soybean_breastmilk["reaction"] = "EX_" + skeleton_Soybean_breastmilk.metabolite + "_m"
skeleton_Split_peas_breastmilk = pd.merge(diet_Split_peas_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Split_peas_breastmilk["global_id"] = skeleton_Split_peas_breastmilk.reaction
skeleton_Split_peas_breastmilk["reaction"] = "EX_" + skeleton_Split_peas_breastmilk.metabolite + "_m"
skeleton_Sunflower_seed_breastmilk = pd.merge(diet_Sunflower_seed_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_Sunflower_seed_breastmilk["global_id"] = skeleton_Sunflower_seed_breastmilk.reaction
skeleton_Sunflower_seed_breastmilk["reaction"] = "EX_" + skeleton_Sunflower_seed_breastmilk.metabolite + "_m"
skeleton_White_beans_breastmilk = pd.merge(diet_White_beans_breastmilk, annotations, on="metabolite") #new data frame with diet and annotations
skeleton_White_beans_breastmilk["global_id"] = skeleton_White_beans_breastmilk.reaction
skeleton_White_beans_breastmilk["reaction"] = "EX_" + skeleton_White_beans_breastmilk.metabolite + "_m"

#Supplementing the medium with essential nutrietns for microbial growth
from micom.workflows.db_media import complete_db_medium

manifest_Broccoli_breastmilk, imports_Broccoli_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Broccoli_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Brussel_breastmilk, imports_Brussel_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Brussel_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Cabbage_breastmilk, imports_Cabbage_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Cabbage_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Carrot_breastmilk, imports_Carrot_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Carrot_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Cauliflower_breastmilk, imports_Cauliflower_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Cauliflower_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Celery_breastmilk, imports_Celery_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Celery_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Cucumber_breastmilk, imports_Cucumber_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Cucumber_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Eggplant_breastmilk, imports_Eggplant_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Eggplant_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Green_beans_breastmilk, imports_Green_beans_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Green_beans_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Green_capsicum_breastmilk, imports_Green_capsicum_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Green_capsicum_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Lettuce_breastmilk, imports_Lettuce_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Lettuce_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Mushroom_breastmilk, imports_Mushroom_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Mushroom_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Onion_breastmilk, imports_Onion_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Onion_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Pak_choi_breastmilk, imports_Pak_choi_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Pak_choi_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Potato_breastmilk, imports_Potato_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Potato_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Pumpkin_breastmilk, importsPumpkin_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Pumpkin_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Sweetcorn_breastmilk, imports_Sweetcorn_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Sweetcorn_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Spinach_breastmilk, imports_Spinach_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Spinach_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Squash_breastmilk, imports_Squash_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Squash_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Sweet_potato_breastmilk, imports_Sweet_potato_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Sweet_potato_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Tomato_breastmilk, imports_Tomato_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Tomato_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Yam_breastmilk, imports_Yam_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Yam_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Zucchini_breastmilk, imports_Zucchini_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Zucchini_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Apple_breastmilk, imports_Apple_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Apple_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Banana_breastmilk, imports_Banana_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Banana_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Blackcurrant_breastmilk, imports_Blackcurrant_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Blackcurrant_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Blueberries_breastmilk, imports_Blueberries_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Blueberries_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Cherry_breastmilk, imports_Cherry_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Cherry_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Feijoa_breastmilk, imports_Feijoa_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Feijoa_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Gold_kiwifruit_breastmilk, imports_Gold_kiwifruit_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Gold_kiwifruit_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Grape_breastmilk, imports_Grape_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Grape_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Grapefruit_breastmilk, imports_Grapefruit_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Grapefruit_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Green_kiwifruit_breastmilk, imports_Green_kiwifruit_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Green_kiwifruit_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Mandarin_breastmilk, imports_Mandarin_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Mandarin_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Mango_breastmilk, imports_Mango_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Mango_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Melon_breastmilk, imports_Melon_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Melon_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Nectarine_breastmilk, imports_Nectarine_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Nectarine_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Orange_breastmilk, imports_Orange_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Orange_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Peache_breastmilk, imports_Peache_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Peache_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Pear_breastmilk, imports_Pear_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Pear_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Pineapple_breastmilk, imports_Pineapple_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Pineapple_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Plum_breastmilk, imports_Plum_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Plum_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Raspberries_breastmilk, imports_Raspberries_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Raspberries_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Strawberries_breastmilk, imports_Strawberries_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Strawberries_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Barley_breastmilk, imports_Barley_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Barley_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Barley_cereal_breastmilk, imports_Barley_cereal_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Barley_cereal_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Couscous_breastmilk, imports_Couscous_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Couscous_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Noodles_breastmilk, imports_Noodles_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Noodles_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Oat_cereal_breastmilk, imports_Oat_cereal_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Oat_cereal_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Pasta_breastmilk, imports_Pasta_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Pasta_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Rice_breastmilk, imports_Rice_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Rice_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Rice_cereal_breastmilk, imports_Rice_cereal_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Rice_cereal_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Tapioca_pudding_breastmilk, imports_Tapioca_pudding_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Tapioca_pudding_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_White_bread_breastmilk, imports_White_bread_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_White_bread_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Wholegrain_bread_breastmilk, imports_Wholegrain_bread_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Wholegrain_bread_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Cottage_cheese_breastmilk, imports_Cottage_cheese_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Cottage_cheese_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Eggs_breastmilk, imports_Eggs_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Eggs_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Mozzarella_cheese_breastmilk, imports_Mozzarella_cheese_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Mozzarella_cheese_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Soymilk_breastmilk, imports_Soymilk_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Soymilk_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Tofu_breastmilk, imports_Tofu_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Tofu_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Whole_milk_breastmilk, imports_Whole_milk_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Whole_milk_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Yoghurt_breastmilk, imports_Yoghurt_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Yoghurt_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Beef_breastmilk, imports_Beef_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Beef_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Chicken_breastmilk, imports_Chicken_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Chicken_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Codfish_breastmilk, imports_Codfish_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Codfish_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Lamb_breastmilk, imports_Lamb_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Lamb_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Mackerel_breastmilk, imports_Mackerel_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Mackerel_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Mussels_breastmilk, imports_Mussels_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Mussels_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Pork_breastmilk, imports_Pork_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Pork_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Salmon_breastmilk, imports_Salmon_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Salmon_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Shrimp_breastmilk, imports_Shrimp_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Shrimp_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Tuna_breastmilk, imports_Tuna_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Tuna_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Turkey_breastmilk, imports_Turkey_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Turkey_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Almond_breastmilk, imports_Almond_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Almond_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Black_beans_breastmilk, imports_Black_beans_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Black_beans_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Cashew_breastmilk, imports_Cashew_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Cashew_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Chia_breastmilk, imports_Chia_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Chia_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Chickpea_breastmilk, imports_Chickpea_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Chickpea_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Green_peas_breastmilk, imports_Green_peas_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Green_peas_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Hazelnut_breastmilk, imports_Hazelnut_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Hazelnut_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Lentils_breastmilk, imports_Lentils_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Lentils_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Peanut_breastmilk, imports_Peanut_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Peanut_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Pecans_breastmilk, imports_Pecans_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Pecans_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Pumpkin_seed_breastmilk, imports_Pumpkin_seed_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Pumpkin_seed_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Red_beans_breastmilk, imports_Red_beans_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Red_beans_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Soybean_breastmilk, imports_Soybean_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Soybean_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Split_peas_breastmilk, imports_Split_peas_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Split_peas_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_Sunflower_seed_breastmilk, imports_Sunflower_seed_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_Sunflower_seed_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)
manifest_White_beans_breastmilk, imports_White_beans_breastmilk = complete_db_medium("data/agora201__species.qza", skeleton_White_beans_breastmilk, growth=0.01, threads=14, max_added_import=10, minimize_components=True)

manifest_Broccoli_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Broccoli_breastmilk = imports_Broccoli_breastmilk.max()
added_Broccoli_breastmilk = filled_Broccoli_breastmilk[~filled_Broccoli_breastmilk.index.isin(skeleton_Broccoli_breastmilk.reaction)] #fluxes that were added
manifest_Brussel_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Brussel_breastmilk = imports_Brussel_breastmilk.max()
added_Brussel_breastmilk = filled_Brussel_breastmilk[~filled_Brussel_breastmilk.index.isin(skeleton_Brussel_breastmilk.reaction)] #fluxes that were added
manifest_Cabbage_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Cabbage_breastmilk = imports_Cabbage_breastmilk.max()
added_Cabbage_breastmilk = filled_Cabbage_breastmilk[~filled_Cabbage_breastmilk.index.isin(skeleton_Cabbage_breastmilk.reaction)] #fluxes that were added
manifest_Carrot_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Carrot_breastmilk = imports_Carrot_breastmilk.max()
added_Carrot_breastmilk = filled_Carrot_breastmilk[~filled_Carrot_breastmilk.index.isin(skeleton_Carrot_breastmilk.reaction)] #fluxes that were added
manifest_Cauliflower_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Cauliflower_breastmilk = imports_Cauliflower_breastmilk.max()
added_Cauliflower_breastmilk = filled_Cauliflower_breastmilk[~filled_Cauliflower_breastmilk.index.isin(skeleton_Cauliflower_breastmilk.reaction)] #fluxes that were added
manifest_Celery_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Celery_breastmilk = imports_Celery_breastmilk.max()
added_Celery_breastmilk = filled_Celery_breastmilk[~filled_Celery_breastmilk.index.isin(skeleton_Celery_breastmilk.reaction)] #fluxes that were added
manifest_Cucumber_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Cucumber_breastmilk = imports_Cucumber_breastmilk.max()
added_Cucumber_breastmilk = filled_Cucumber_breastmilk[~filled_Cucumber_breastmilk.index.isin(skeleton_Cucumber_breastmilk.reaction)] #fluxes that were added
manifest_Eggplant_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Eggplant_breastmilk = imports_Eggplant_breastmilk.max()
added_Eggplant_breastmilk = filled_Eggplant_breastmilk[~filled_Eggplant_breastmilk.index.isin(skeleton_Eggplant_breastmilk.reaction)] #fluxes that were added
manifest_Green_beans_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Green_beans_breastmilk = imports_Green_beans_breastmilk.max()
added_Green_beans_breastmilk = filled_Green_beans_breastmilk[~filled_Green_beans_breastmilk.index.isin(skeleton_Green_beans_breastmilk.reaction)] #fluxes that were added
manifest_Green_capsicum_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Green_capsicum_breastmilk = imports_Green_capsicum_breastmilk.max()
added_Green_capsicum_breastmilk = filled_Green_capsicum_breastmilk[~filled_Green_capsicum_breastmilk.index.isin(skeleton_Green_capsicum_breastmilk.reaction)] #fluxes that were added
manifest_Lettuce_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Lettuce_breastmilk = imports_Lettuce_breastmilk.max()
added_Lettuce_breastmilk = filled_Lettuce_breastmilk[~filled_Lettuce_breastmilk.index.isin(skeleton_Lettuce_breastmilk.reaction)] #fluxes that were added
manifest_Mushroom_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Mushroom_breastmilk = imports_Mushroom_breastmilk.max()
added_Mushroom_breastmilk = filled_Mushroom_breastmilk[~filled_Mushroom_breastmilk.index.isin(skeleton_Mushroom_breastmilk.reaction)] #fluxes that were added
manifest_Onion_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Onion_breastmilk = imports_Onion_breastmilk.max()
added_Onion_breastmilk = filled_Onion_breastmilk[~filled_Onion_breastmilk.index.isin(skeleton_Onion_breastmilk.reaction)] #fluxes that were added
manifest_Pak_choi_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Pak_choi_breastmilk = imports_Pak_choi_breastmilk.max()
added_Pak_choi_breastmilk = filled_Pak_choi_breastmilk[~filled_Pak_choi_breastmilk.index.isin(skeleton_Pak_choi_breastmilk.reaction)] #fluxes that were added
manifest_Potato_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Potato_breastmilk = imports_Potato_breastmilk.max()
added_Potato_breastmilk = filled_Potato_breastmilk[~filled_Potato_breastmilk.index.isin(skeleton_Potato_breastmilk.reaction)] #fluxes that were added
manifest_Pumpkin_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Pumpkin_breastmilk = importsPumpkin_breastmilk.max()
addedPumpkin_breastmilk = filled_Pumpkin_breastmilk[~filled_Pumpkin_breastmilk.index.isin(skeleton_Pumpkin_breastmilk.reaction)] #fluxes that were added
manifest_Sweetcorn_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Sweetcorn_breastmilk = imports_Sweetcorn_breastmilk.max()
added_Sweetcorn_breastmilk = filled_Sweetcorn_breastmilk[~filled_Sweetcorn_breastmilk.index.isin(skeleton_Sweetcorn_breastmilk.reaction)] #fluxes that were added
manifest_Spinach_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Spinach_breastmilk = imports_Spinach_breastmilk.max()
added_Spinach_breastmilk = filled_Spinach_breastmilk[~filled_Spinach_breastmilk.index.isin(skeleton_Spinach_breastmilk.reaction)] #fluxes that were added
manifest_Squash_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Squash_breastmilk = imports_Squash_breastmilk.max()
added_Squash_breastmilk = filled_Squash_breastmilk[~filled_Squash_breastmilk.index.isin(skeleton_Squash_breastmilk.reaction)] #fluxes that were added
manifest_Sweet_potato_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Sweet_potato_breastmilk = imports_Sweet_potato_breastmilk.max()
added_Sweet_potato_breastmilk = filled_Sweet_potato_breastmilk[~filled_Sweet_potato_breastmilk.index.isin(skeleton_Sweet_potato_breastmilk.reaction)] #fluxes that were added
manifest_Tomato_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Tomato_breastmilk = imports_Tomato_breastmilk.max()
added_Tomato_breastmilk = filled_Tomato_breastmilk[~filled_Tomato_breastmilk.index.isin(skeleton_Tomato_breastmilk.reaction)] #fluxes that were added
manifest_Yam_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Yam_breastmilk = imports_Yam_breastmilk.max()
added_Yam_breastmilk = filled_Yam_breastmilk[~filled_Yam_breastmilk.index.isin(skeleton_Yam_breastmilk.reaction)] #fluxes that were added
manifest_Zucchini_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Zucchini_breastmilk = imports_Zucchini_breastmilk.max()
added_Zucchini_breastmilk = filled_Zucchini_breastmilk[~filled_Zucchini_breastmilk.index.isin(skeleton_Zucchini_breastmilk.reaction)] #fluxes that were added
manifest_Apple_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Apple_breastmilk = imports_Apple_breastmilk.max()
added_Apple_breastmilk = filled_Apple_breastmilk[~filled_Apple_breastmilk.index.isin(skeleton_Apple_breastmilk.reaction)] #fluxes that were added
manifest_Banana_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Banana_breastmilk = imports_Banana_breastmilk.max()
added_Banana_breastmilk = filled_Banana_breastmilk[~filled_Banana_breastmilk.index.isin(skeleton_Banana_breastmilk.reaction)] #fluxes that were added
manifest_Blackcurrant_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Blackcurrant_breastmilk = imports_Blackcurrant_breastmilk.max()
added_Blackcurrant_breastmilk = filled_Blackcurrant_breastmilk[~filled_Blackcurrant_breastmilk.index.isin(skeleton_Blackcurrant_breastmilk.reaction)] #fluxes that were added
manifest_Blueberries_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Blueberries_breastmilk = imports_Blueberries_breastmilk.max()
added_Blueberries_breastmilk = filled_Blueberries_breastmilk[~filled_Blueberries_breastmilk.index.isin(skeleton_Blueberries_breastmilk.reaction)] #fluxes that were added
manifest_Cherry_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Cherry_breastmilk = imports_Cherry_breastmilk.max()
added_Cherry_breastmilk = filled_Cherry_breastmilk[~filled_Cherry_breastmilk.index.isin(skeleton_Cherry_breastmilk.reaction)] #fluxes that were added
manifest_Feijoa_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Feijoa_breastmilk = imports_Feijoa_breastmilk.max()
added_Feijoa_breastmilk = filled_Feijoa_breastmilk[~filled_Feijoa_breastmilk.index.isin(skeleton_Feijoa_breastmilk.reaction)] #fluxes that were added
manifest_Gold_kiwifruit_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Gold_kiwifruit_breastmilk = imports_Gold_kiwifruit_breastmilk.max()
added_Gold_kiwifruit_breastmilk = filled_Gold_kiwifruit_breastmilk[~filled_Gold_kiwifruit_breastmilk.index.isin(skeleton_Gold_kiwifruit_breastmilk.reaction)] #fluxes that were added
manifest_Grape_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Grape_breastmilk = imports_Grape_breastmilk.max()
added_Grape_breastmilk = filled_Grape_breastmilk[~filled_Grape_breastmilk.index.isin(skeleton_Grape_breastmilk.reaction)] #fluxes that were added
manifest_Grapefruit_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Grapefruit_breastmilk = imports_Grapefruit_breastmilk.max()
added_Grapefruit_breastmilk = filled_Grapefruit_breastmilk[~filled_Grapefruit_breastmilk.index.isin(skeleton_Grapefruit_breastmilk.reaction)] #fluxes that were added
manifest_Green_kiwifruit_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Green_kiwifruit_breastmilk = imports_Green_kiwifruit_breastmilk.max()
added_Green_kiwifruit_breastmilk = filled_Green_kiwifruit_breastmilk[~filled_Green_kiwifruit_breastmilk.index.isin(skeleton_Green_kiwifruit_breastmilk.reaction)] #fluxes that were added
manifest_Mandarin_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Mandarin_breastmilk = imports_Mandarin_breastmilk.max()
added_Mandarin_breastmilk = filled_Mandarin_breastmilk[~filled_Mandarin_breastmilk.index.isin(skeleton_Mandarin_breastmilk.reaction)] #fluxes that were added
manifest_Mango_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Mango_breastmilk = imports_Mango_breastmilk.max()
added_Mango_breastmilk = filled_Mango_breastmilk[~filled_Mango_breastmilk.index.isin(skeleton_Mango_breastmilk.reaction)] #fluxes that were added
manifest_Melon_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Melon_breastmilk = imports_Melon_breastmilk.max()
added_Melon_breastmilk = filled_Melon_breastmilk[~filled_Melon_breastmilk.index.isin(skeleton_Melon_breastmilk.reaction)] #fluxes that were added
manifest_Nectarine_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Nectarine_breastmilk = imports_Nectarine_breastmilk.max()
added_Nectarine_breastmilk = filled_Nectarine_breastmilk[~filled_Nectarine_breastmilk.index.isin(skeleton_Nectarine_breastmilk.reaction)] #fluxes that were added
manifest_Orange_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Orange_breastmilk = imports_Orange_breastmilk.max()
added_Orange_breastmilk = filled_Orange_breastmilk[~filled_Orange_breastmilk.index.isin(skeleton_Orange_breastmilk.reaction)] #fluxes that were added
manifest_Peache_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Peache_breastmilk = imports_Peache_breastmilk.max()
added_Peache_breastmilk = filled_Peache_breastmilk[~filled_Peache_breastmilk.index.isin(skeleton_Peache_breastmilk.reaction)] #fluxes that were added
manifest_Pear_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Pear_breastmilk = imports_Pear_breastmilk.max()
added_Pear_breastmilk = filled_Pear_breastmilk[~filled_Pear_breastmilk.index.isin(skeleton_Pear_breastmilk.reaction)] #fluxes that were added
manifest_Pineapple_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Pineapple_breastmilk = imports_Pineapple_breastmilk.max()
added_Pineapple_breastmilk = filled_Pineapple_breastmilk[~filled_Pineapple_breastmilk.index.isin(skeleton_Pineapple_breastmilk.reaction)] #fluxes that were added
manifest_Plum_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Plum_breastmilk = imports_Plum_breastmilk.max()
added_Plum_breastmilk = filled_Plum_breastmilk[~filled_Plum_breastmilk.index.isin(skeleton_Plum_breastmilk.reaction)] #fluxes that were added
manifest_Raspberries_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Raspberries_breastmilk = imports_Raspberries_breastmilk.max()
added_Raspberries_breastmilk = filled_Raspberries_breastmilk[~filled_Raspberries_breastmilk.index.isin(skeleton_Raspberries_breastmilk.reaction)] #fluxes that were added
manifest_Strawberries_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Strawberries_breastmilk = imports_Strawberries_breastmilk.max()
added_Strawberries_breastmilk = filled_Strawberries_breastmilk[~filled_Strawberries_breastmilk.index.isin(skeleton_Strawberries_breastmilk.reaction)] #fluxes that were added
manifest_Barley_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Barley_breastmilk = imports_Barley_breastmilk.max()
added_Barley_breastmilk = filled_Barley_breastmilk[~filled_Barley_breastmilk.index.isin(skeleton_Barley_breastmilk.reaction)] #fluxes that were added
manifest_Barley_cereal_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Barley_cereal_breastmilk = imports_Barley_cereal_breastmilk.max()
added_Barley_cereal_breastmilk = filled_Barley_cereal_breastmilk[~filled_Barley_cereal_breastmilk.index.isin(skeleton_Barley_cereal_breastmilk.reaction)] #fluxes that were added
manifest_Couscous_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Couscous_breastmilk = imports_Couscous_breastmilk.max()
added_Couscous_breastmilk = filled_Couscous_breastmilk[~filled_Couscous_breastmilk.index.isin(skeleton_Couscous_breastmilk.reaction)] #fluxes that were added
manifest_Noodles_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Noodles_breastmilk = imports_Noodles_breastmilk.max()
added_Noodles_breastmilk = filled_Noodles_breastmilk[~filled_Noodles_breastmilk.index.isin(skeleton_Noodles_breastmilk.reaction)] #fluxes that were added
manifest_Oat_cereal_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Oat_cereal_breastmilk = imports_Oat_cereal_breastmilk.max()
added_Oat_cereal_breastmilk = filled_Oat_cereal_breastmilk[~filled_Oat_cereal_breastmilk.index.isin(skeleton_Oat_cereal_breastmilk.reaction)] #fluxes that were added
manifest_Pasta_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Pasta_breastmilk = imports_Pasta_breastmilk.max()
added_Pasta_breastmilk = filled_Pasta_breastmilk[~filled_Pasta_breastmilk.index.isin(skeleton_Pasta_breastmilk.reaction)] #fluxes that were added
manifest_Rice_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Rice_breastmilk = imports_Rice_breastmilk.max()
added_Rice_breastmilk = filled_Rice_breastmilk[~filled_Rice_breastmilk.index.isin(skeleton_Rice_breastmilk.reaction)] #fluxes that were added
manifest_Rice_cereal_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Rice_cereal_breastmilk = imports_Rice_cereal_breastmilk.max()
added_Rice_cereal_breastmilk = filled_Rice_cereal_breastmilk[~filled_Rice_cereal_breastmilk.index.isin(skeleton_Rice_cereal_breastmilk.reaction)] #fluxes that were added
manifest_Tapioca_pudding_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Tapioca_pudding_breastmilk = imports_Tapioca_pudding_breastmilk.max()
added_Tapioca_pudding_breastmilk = filled_Tapioca_pudding_breastmilk[~filled_Tapioca_pudding_breastmilk.index.isin(skeleton_Tapioca_pudding_breastmilk.reaction)] #fluxes that were added
manifest_White_bread_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_White_bread_breastmilk = imports_White_bread_breastmilk.max()
added_White_bread_breastmilk = filled_White_bread_breastmilk[~filled_White_bread_breastmilk.index.isin(skeleton_White_bread_breastmilk.reaction)] #fluxes that were added
manifest_Wholegrain_bread_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Wholegrain_bread_breastmilk = imports_Wholegrain_bread_breastmilk.max()
added_Wholegrain_bread_breastmilk = filled_Wholegrain_bread_breastmilk[~filled_Wholegrain_bread_breastmilk.index.isin(skeleton_Wholegrain_bread_breastmilk.reaction)] #fluxes that were added
manifest_Cottage_cheese_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Cottage_cheese_breastmilk = imports_Cottage_cheese_breastmilk.max()
added_Cottage_cheese_breastmilk = filled_Cottage_cheese_breastmilk[~filled_Cottage_cheese_breastmilk.index.isin(skeleton_Cottage_cheese_breastmilk.reaction)] #fluxes that were added
manifest_Eggs_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Eggs_breastmilk = imports_Eggs_breastmilk.max()
added_Eggs_breastmilk = filled_Eggs_breastmilk[~filled_Eggs_breastmilk.index.isin(skeleton_Eggs_breastmilk.reaction)] #fluxes that were added
manifest_Mozzarella_cheese_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Mozzarella_cheese_breastmilk = imports_Mozzarella_cheese_breastmilk.max()
added_Mozzarella_cheese_breastmilk = filled_Mozzarella_cheese_breastmilk[~filled_Mozzarella_cheese_breastmilk.index.isin(skeleton_Mozzarella_cheese_breastmilk.reaction)] #fluxes that were added
manifest_Soymilk_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Soymilk_breastmilk = imports_Soymilk_breastmilk.max()
added_Soymilk_breastmilk = filled_Soymilk_breastmilk[~filled_Soymilk_breastmilk.index.isin(skeleton_Soymilk_breastmilk.reaction)] #fluxes that were added
manifest_Tofu_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Tofu_breastmilk = imports_Tofu_breastmilk.max()
added_Tofu_breastmilk = filled_Tofu_breastmilk[~filled_Tofu_breastmilk.index.isin(skeleton_Tofu_breastmilk.reaction)] #fluxes that were added
manifest_Whole_milk_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Whole_milk_breastmilk = imports_Whole_milk_breastmilk.max()
added_Whole_milk_breastmilk = filled_Whole_milk_breastmilk[~filled_Whole_milk_breastmilk.index.isin(skeleton_Whole_milk_breastmilk.reaction)] #fluxes that were added
manifest_Yoghurt_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Yoghurt_breastmilk = imports_Yoghurt_breastmilk.max()
added_Yoghurt_breastmilk = filled_Yoghurt_breastmilk[~filled_Yoghurt_breastmilk.index.isin(skeleton_Yoghurt_breastmilk.reaction)] #fluxes that were added
manifest_Beef_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Beef_breastmilk = imports_Beef_breastmilk.max()
added_Beef_breastmilk = filled_Beef_breastmilk[~filled_Beef_breastmilk.index.isin(skeleton_Beef_breastmilk.reaction)] #fluxes that were added
manifest_Chicken_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Chicken_breastmilk = imports_Chicken_breastmilk.max()
added_Chicken_breastmilk = filled_Chicken_breastmilk[~filled_Chicken_breastmilk.index.isin(skeleton_Chicken_breastmilk.reaction)] #fluxes that were added
manifest_Codfish_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Codfish_breastmilk = imports_Codfish_breastmilk.max()
added_Codfish_breastmilk = filled_Codfish_breastmilk[~filled_Codfish_breastmilk.index.isin(skeleton_Codfish_breastmilk.reaction)] #fluxes that were added
manifest_Lamb_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Lamb_breastmilk = imports_Lamb_breastmilk.max()
added_Lamb_breastmilk = filled_Lamb_breastmilk[~filled_Lamb_breastmilk.index.isin(skeleton_Lamb_breastmilk.reaction)] #fluxes that were added
manifest_Mackerel_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Mackerel_breastmilk = imports_Mackerel_breastmilk.max()
added_Mackerel_breastmilk = filled_Mackerel_breastmilk[~filled_Mackerel_breastmilk.index.isin(skeleton_Mackerel_breastmilk.reaction)] #fluxes that were added
manifest_Mussels_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Mussels_breastmilk = imports_Mussels_breastmilk.max()
added_Mussels_breastmilk = filled_Mussels_breastmilk[~filled_Mussels_breastmilk.index.isin(skeleton_Mussels_breastmilk.reaction)] #fluxes that were added
manifest_Pork_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Pork_breastmilk = imports_Pork_breastmilk.max()
added_Pork_breastmilk = filled_Pork_breastmilk[~filled_Pork_breastmilk.index.isin(skeleton_Pork_breastmilk.reaction)] #fluxes that were added
manifest_Salmon_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Salmon_breastmilk = imports_Salmon_breastmilk.max()
added_Salmon_breastmilk = filled_Salmon_breastmilk[~filled_Salmon_breastmilk.index.isin(skeleton_Salmon_breastmilk.reaction)] #fluxes that were added
manifest_Shrimp_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Shrimp_breastmilk = imports_Shrimp_breastmilk.max()
added_Shrimp_breastmilk = filled_Shrimp_breastmilk[~filled_Shrimp_breastmilk.index.isin(skeleton_Shrimp_breastmilk.reaction)] #fluxes that were added
manifest_Tuna_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Tuna_breastmilk = imports_Tuna_breastmilk.max()
added_Tuna_breastmilk = filled_Tuna_breastmilk[~filled_Tuna_breastmilk.index.isin(skeleton_Tuna_breastmilk.reaction)] #fluxes that were added
manifest_Turkey_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Turkey_breastmilk = imports_Turkey_breastmilk.max()
added_Turkey_breastmilk = filled_Turkey_breastmilk[~filled_Turkey_breastmilk.index.isin(skeleton_Turkey_breastmilk.reaction)] #fluxes that were added
manifest_Almond_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Almond_breastmilk = imports_Almond_breastmilk.max()
added_Almond_breastmilk = filled_Almond_breastmilk[~filled_Almond_breastmilk.index.isin(skeleton_Almond_breastmilk.reaction)] #fluxes that were added
manifest_Black_beans_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Black_beans_breastmilk = imports_Black_beans_breastmilk.max()
added_Black_beans_breastmilk = filled_Black_beans_breastmilk[~filled_Black_beans_breastmilk.index.isin(skeleton_Black_beans_breastmilk.reaction)] #fluxes that were added
manifest_Cashew_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Cashew_breastmilk = imports_Cashew_breastmilk.max()
added_Cashew_breastmilk = filled_Cashew_breastmilk[~filled_Cashew_breastmilk.index.isin(skeleton_Cashew_breastmilk.reaction)] #fluxes that were added
manifest_Chia_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Chia_breastmilk = imports_Chia_breastmilk.max()
added_Chia_breastmilk = filled_Chia_breastmilk[~filled_Chia_breastmilk.index.isin(skeleton_Chia_breastmilk.reaction)] #fluxes that were added
manifest_Chickpea_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Chickpea_breastmilk = imports_Chickpea_breastmilk.max()
added_Chickpea_breastmilk = filled_Chickpea_breastmilk[~filled_Chickpea_breastmilk.index.isin(skeleton_Chickpea_breastmilk.reaction)] #fluxes that were added
manifest_Green_peas_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Green_peas_breastmilk = imports_Green_peas_breastmilk.max()
added_Green_peas_breastmilk = filled_Green_peas_breastmilk[~filled_Green_peas_breastmilk.index.isin(skeleton_Green_peas_breastmilk.reaction)] #fluxes that were added
manifest_Hazelnut_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Hazelnut_breastmilk = imports_Hazelnut_breastmilk.max()
added_Hazelnut_breastmilk = filled_Hazelnut_breastmilk[~filled_Hazelnut_breastmilk.index.isin(skeleton_Hazelnut_breastmilk.reaction)] #fluxes that were added
manifest_Lentils_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Lentils_breastmilk = imports_Lentils_breastmilk.max()
added_Lentils_breastmilk = filled_Lentils_breastmilk[~filled_Lentils_breastmilk.index.isin(skeleton_Lentils_breastmilk.reaction)] #fluxes that were added
manifest_Peanut_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Peanut_breastmilk = imports_Peanut_breastmilk.max()
added_Peanut_breastmilk = filled_Peanut_breastmilk[~filled_Peanut_breastmilk.index.isin(skeleton_Peanut_breastmilk.reaction)] #fluxes that were added
manifest_Pecans_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Pecans_breastmilk = imports_Pecans_breastmilk.max()
added_Pecans_breastmilk = filled_Pecans_breastmilk[~filled_Pecans_breastmilk.index.isin(skeleton_Pecans_breastmilk.reaction)] #fluxes that were added
manifest_Pumpkin_seed_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Pumpkin_seed_breastmilk = imports_Pumpkin_seed_breastmilk.max()
added_Pumpkin_seed_breastmilk = filled_Pumpkin_seed_breastmilk[~filled_Pumpkin_seed_breastmilk.index.isin(skeleton_Pumpkin_seed_breastmilk.reaction)] #fluxes that were added
manifest_Red_beans_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Red_beans_breastmilk = imports_Red_beans_breastmilk.max()
added_Red_beans_breastmilk = filled_Red_beans_breastmilk[~filled_Red_beans_breastmilk.index.isin(skeleton_Red_beans_breastmilk.reaction)] #fluxes that were added
manifest_Soybean_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Soybean_breastmilk = imports_Soybean_breastmilk.max()
added_Soybean_breastmilk = filled_Soybean_breastmilk[~filled_Soybean_breastmilk.index.isin(skeleton_Soybean_breastmilk.reaction)] #fluxes that were added
manifest_Split_peas_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Split_peas_breastmilk = imports_Split_peas_breastmilk.max()
added_Split_peas_breastmilk = filled_Split_peas_breastmilk[~filled_Split_peas_breastmilk.index.isin(skeleton_Split_peas_breastmilk.reaction)] #fluxes that were added
manifest_Sunflower_seed_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_Sunflower_seed_breastmilk = imports_Sunflower_seed_breastmilk.max()
added_Sunflower_seed_breastmilk = filled_Sunflower_seed_breastmilk[~filled_Sunflower_seed_breastmilk.index.isin(skeleton_Sunflower_seed_breastmilk.reaction)] #fluxes that were added
manifest_White_beans_breastmilk.can_grow.value_counts() #checking the microbial growth
filled_White_beans_breastmilk = imports_White_beans_breastmilk.max()
added_White_beans_breastmilk = filled_White_beans_breastmilk[~filled_White_beans_breastmilk.index.isin(skeleton_White_beans_breastmilk.reaction)] #fluxes that were added

#Assembling the final medium

added_df_Broccoli_breastmilk = added_Broccoli_breastmilk.reset_index() 
added_df_Broccoli_breastmilk.iloc[:, 0] = added_df_Broccoli_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Broccoli_breastmilk.columns = ["metabolite", "flux"]
added_df_Broccoli_breastmilk = pd.concat([skeleton_Broccoli_breastmilk[["metabolite", "flux"]], added_df_Broccoli_breastmilk])
added_df_Brussel_breastmilk = added_Brussel_breastmilk.reset_index() 
added_df_Brussel_breastmilk.iloc[:, 0] = added_df_Brussel_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Brussel_breastmilk.columns = ["metabolite", "flux"]
added_df_Brussel_breastmilk = pd.concat([skeleton_Brussel_breastmilk[["metabolite", "flux"]], added_df_Brussel_breastmilk])
added_df_Cabbage_breastmilk = added_Cabbage_breastmilk.reset_index() 
added_df_Cabbage_breastmilk.iloc[:, 0] = added_df_Cabbage_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Cabbage_breastmilk.columns = ["metabolite", "flux"]
added_df_Cabbage_breastmilk = pd.concat([skeleton_Cabbage_breastmilk[["metabolite", "flux"]], added_df_Cabbage_breastmilk])
added_df_Carrot_breastmilk = added_Carrot_breastmilk.reset_index() 
added_df_Carrot_breastmilk.iloc[:, 0] = added_df_Carrot_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Carrot_breastmilk.columns = ["metabolite", "flux"]
added_df_Carrot_breastmilk = pd.concat([skeleton_Carrot_breastmilk[["metabolite", "flux"]], added_df_Carrot_breastmilk])
added_df_Cauliflower_breastmilk = added_Cauliflower_breastmilk.reset_index() 
added_df_Cauliflower_breastmilk.iloc[:, 0] = added_df_Cauliflower_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Cauliflower_breastmilk.columns = ["metabolite", "flux"]
added_df_Cauliflower_breastmilk = pd.concat([skeleton_Cauliflower_breastmilk[["metabolite", "flux"]], added_df_Cauliflower_breastmilk])
added_df_Celery_breastmilk = added_Celery_breastmilk.reset_index() 
added_df_Celery_breastmilk.iloc[:, 0] = added_df_Celery_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Celery_breastmilk.columns = ["metabolite", "flux"]
added_df_Celery_breastmilk = pd.concat([skeleton_Celery_breastmilk[["metabolite", "flux"]], added_df_Celery_breastmilk])
added_df_Cucumber_breastmilk = added_Cucumber_breastmilk.reset_index() 
added_df_Cucumber_breastmilk.iloc[:, 0] = added_df_Cucumber_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Cucumber_breastmilk.columns = ["metabolite", "flux"]
added_df_Cucumber_breastmilk = pd.concat([skeleton_Cucumber_breastmilk[["metabolite", "flux"]], added_df_Cucumber_breastmilk])
added_df_Eggplant_breastmilk = added_Eggplant_breastmilk.reset_index() 
added_df_Eggplant_breastmilk.iloc[:, 0] = added_df_Eggplant_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Eggplant_breastmilk.columns = ["metabolite", "flux"]
added_df_Eggplant_breastmilk = pd.concat([skeleton_Eggplant_breastmilk[["metabolite", "flux"]], added_df_Eggplant_breastmilk])
added_df_Green_beans_breastmilk = added_Green_beans_breastmilk.reset_index() 
added_df_Green_beans_breastmilk.iloc[:, 0] = added_df_Green_beans_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Green_beans_breastmilk.columns = ["metabolite", "flux"]
added_df_Green_beans_breastmilk = pd.concat([skeleton_Green_beans_breastmilk[["metabolite", "flux"]], added_df_Green_beans_breastmilk])
added_df_Green_capsicum_breastmilk = added_Green_capsicum_breastmilk.reset_index() 
added_df_Green_capsicum_breastmilk.iloc[:, 0] = added_df_Green_capsicum_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Green_capsicum_breastmilk.columns = ["metabolite", "flux"]
added_df_Green_capsicum_breastmilk = pd.concat([skeleton_Green_capsicum_breastmilk[["metabolite", "flux"]], added_df_Green_capsicum_breastmilk])
added_df_Lettuce_breastmilk = added_Lettuce_breastmilk.reset_index() 
added_df_Lettuce_breastmilk.iloc[:, 0] = added_df_Lettuce_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Lettuce_breastmilk.columns = ["metabolite", "flux"]
added_df_Lettuce_breastmilk = pd.concat([skeleton_Lettuce_breastmilk[["metabolite", "flux"]], added_df_Lettuce_breastmilk])
added_df_Mushroom_breastmilk = added_Mushroom_breastmilk.reset_index() 
added_df_Mushroom_breastmilk.iloc[:, 0] = added_df_Mushroom_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Mushroom_breastmilk.columns = ["metabolite", "flux"]
added_df_Mushroom_breastmilk = pd.concat([skeleton_Mushroom_breastmilk[["metabolite", "flux"]], added_df_Mushroom_breastmilk])
added_df_Onion_breastmilk = added_Onion_breastmilk.reset_index() 
added_df_Onion_breastmilk.iloc[:, 0] = added_df_Onion_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Onion_breastmilk.columns = ["metabolite", "flux"]
added_df_Onion_breastmilk = pd.concat([skeleton_Onion_breastmilk[["metabolite", "flux"]], added_df_Onion_breastmilk])
added_df_Pak_choi_breastmilk = added_Pak_choi_breastmilk.reset_index() 
added_df_Pak_choi_breastmilk.iloc[:, 0] = added_df_Pak_choi_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Pak_choi_breastmilk.columns = ["metabolite", "flux"]
added_df_Pak_choi_breastmilk = pd.concat([skeleton_Pak_choi_breastmilk[["metabolite", "flux"]], added_df_Pak_choi_breastmilk])
added_df_Potato_breastmilk = added_Potato_breastmilk.reset_index() 
added_df_Potato_breastmilk.iloc[:, 0] = added_df_Potato_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Potato_breastmilk.columns = ["metabolite", "flux"]
added_df_Potato_breastmilk = pd.concat([skeleton_Potato_breastmilk[["metabolite", "flux"]], added_df_Potato_breastmilk])
added_df_Pumpkin_breastmilk = addedPumpkin_breastmilk.reset_index() 
added_df_Pumpkin_breastmilk.iloc[:, 0] = added_df_Pumpkin_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Pumpkin_breastmilk.columns = ["metabolite", "flux"]
added_df_Pumpkin_breastmilk = pd.concat([skeleton_Pumpkin_breastmilk[["metabolite", "flux"]], added_df_Pumpkin_breastmilk])
added_df_Sweetcorn_breastmilk = added_Sweetcorn_breastmilk.reset_index() 
added_df_Sweetcorn_breastmilk.iloc[:, 0] = added_df_Sweetcorn_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Sweetcorn_breastmilk.columns = ["metabolite", "flux"]
added_df_Sweetcorn_breastmilk = pd.concat([skeleton_Sweetcorn_breastmilk[["metabolite", "flux"]], added_df_Sweetcorn_breastmilk])
added_df_Spinach_breastmilk = added_Spinach_breastmilk.reset_index() 
added_df_Spinach_breastmilk.iloc[:, 0] = added_df_Spinach_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Spinach_breastmilk.columns = ["metabolite", "flux"]
added_df_Spinach_breastmilk = pd.concat([skeleton_Spinach_breastmilk[["metabolite", "flux"]], added_df_Spinach_breastmilk])
added_df_Squash_breastmilk = added_Squash_breastmilk.reset_index() 
added_df_Squash_breastmilk.iloc[:, 0] = added_df_Squash_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Squash_breastmilk.columns = ["metabolite", "flux"]
added_df_Squash_breastmilk = pd.concat([skeleton_Squash_breastmilk[["metabolite", "flux"]], added_df_Squash_breastmilk])
added_df_Sweet_potato_breastmilk = added_Sweet_potato_breastmilk.reset_index() 
added_df_Sweet_potato_breastmilk.iloc[:, 0] = added_df_Sweet_potato_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Sweet_potato_breastmilk.columns = ["metabolite", "flux"]
added_df_Sweet_potato_breastmilk = pd.concat([skeleton_Sweet_potato_breastmilk[["metabolite", "flux"]], added_df_Sweet_potato_breastmilk])
added_df_Tomato_breastmilk = added_Tomato_breastmilk.reset_index() 
added_df_Tomato_breastmilk.iloc[:, 0] = added_df_Tomato_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Tomato_breastmilk.columns = ["metabolite", "flux"]
added_df_Tomato_breastmilk = pd.concat([skeleton_Tomato_breastmilk[["metabolite", "flux"]], added_df_Tomato_breastmilk])
added_df_Yam_breastmilk = added_Yam_breastmilk.reset_index() 
added_df_Yam_breastmilk.iloc[:, 0] = added_df_Yam_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Yam_breastmilk.columns = ["metabolite", "flux"]
added_df_Yam_breastmilk = pd.concat([skeleton_Yam_breastmilk[["metabolite", "flux"]], added_df_Yam_breastmilk])
added_df_Zucchini_breastmilk = added_Zucchini_breastmilk.reset_index() 
added_df_Zucchini_breastmilk.iloc[:, 0] = added_df_Zucchini_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Zucchini_breastmilk.columns = ["metabolite", "flux"]
added_df_Zucchini_breastmilk = pd.concat([skeleton_Zucchini_breastmilk[["metabolite", "flux"]], added_df_Zucchini_breastmilk])
added_df_Apple_breastmilk = added_Apple_breastmilk.reset_index() 
added_df_Apple_breastmilk.iloc[:, 0] = added_df_Apple_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Apple_breastmilk.columns = ["metabolite", "flux"]
added_df_Apple_breastmilk = pd.concat([skeleton_Apple_breastmilk[["metabolite", "flux"]], added_df_Apple_breastmilk])
added_df_Banana_breastmilk = added_Banana_breastmilk.reset_index() 
added_df_Banana_breastmilk.iloc[:, 0] = added_df_Banana_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Banana_breastmilk.columns = ["metabolite", "flux"]
added_df_Banana_breastmilk = pd.concat([skeleton_Banana_breastmilk[["metabolite", "flux"]], added_df_Banana_breastmilk])
added_df_Blackcurrant_breastmilk = added_Blackcurrant_breastmilk.reset_index() 
added_df_Blackcurrant_breastmilk.iloc[:, 0] = added_df_Blackcurrant_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Blackcurrant_breastmilk.columns = ["metabolite", "flux"]
added_df_Blackcurrant_breastmilk = pd.concat([skeleton_Blackcurrant_breastmilk[["metabolite", "flux"]], added_df_Blackcurrant_breastmilk])
added_df_Blueberries_breastmilk = added_Blueberries_breastmilk.reset_index() 
added_df_Blueberries_breastmilk.iloc[:, 0] = added_df_Blueberries_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Blueberries_breastmilk.columns = ["metabolite", "flux"]
added_df_Blueberries_breastmilk = pd.concat([skeleton_Blueberries_breastmilk[["metabolite", "flux"]], added_df_Blueberries_breastmilk])
added_df_Cherry_breastmilk = added_Cherry_breastmilk.reset_index() 
added_df_Cherry_breastmilk.iloc[:, 0] = added_df_Cherry_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Cherry_breastmilk.columns = ["metabolite", "flux"]
added_df_Cherry_breastmilk = pd.concat([skeleton_Cherry_breastmilk[["metabolite", "flux"]], added_df_Cherry_breastmilk])
added_df_Feijoa_breastmilk = added_Feijoa_breastmilk.reset_index() 
added_df_Feijoa_breastmilk.iloc[:, 0] = added_df_Feijoa_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Feijoa_breastmilk.columns = ["metabolite", "flux"]
added_df_Feijoa_breastmilk = pd.concat([skeleton_Feijoa_breastmilk[["metabolite", "flux"]], added_df_Feijoa_breastmilk])
added_df_Gold_kiwifruit_breastmilk = added_Gold_kiwifruit_breastmilk.reset_index() 
added_df_Gold_kiwifruit_breastmilk.iloc[:, 0] = added_df_Gold_kiwifruit_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Gold_kiwifruit_breastmilk.columns = ["metabolite", "flux"]
added_df_Gold_kiwifruit_breastmilk = pd.concat([skeleton_Gold_kiwifruit_breastmilk[["metabolite", "flux"]], added_df_Gold_kiwifruit_breastmilk])
added_df_Grape_breastmilk = added_Grape_breastmilk.reset_index() 
added_df_Grape_breastmilk.iloc[:, 0] = added_df_Grape_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Grape_breastmilk.columns = ["metabolite", "flux"]
added_df_Grape_breastmilk = pd.concat([skeleton_Grape_breastmilk[["metabolite", "flux"]], added_df_Grape_breastmilk])
added_df_Grapefruit_breastmilk = added_Grapefruit_breastmilk.reset_index() 
added_df_Grapefruit_breastmilk.iloc[:, 0] = added_df_Grapefruit_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Grapefruit_breastmilk.columns = ["metabolite", "flux"]
added_df_Grapefruit_breastmilk = pd.concat([skeleton_Grapefruit_breastmilk[["metabolite", "flux"]], added_df_Grapefruit_breastmilk])
added_df_Green_kiwifruit_breastmilk = added_Green_kiwifruit_breastmilk.reset_index() 
added_df_Green_kiwifruit_breastmilk.iloc[:, 0] = added_df_Green_kiwifruit_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Green_kiwifruit_breastmilk.columns = ["metabolite", "flux"]
added_df_Green_kiwifruit_breastmilk = pd.concat([skeleton_Green_kiwifruit_breastmilk[["metabolite", "flux"]], added_df_Green_kiwifruit_breastmilk])
added_df_Mandarin_breastmilk = added_Mandarin_breastmilk.reset_index() 
added_df_Mandarin_breastmilk.iloc[:, 0] = added_df_Mandarin_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Mandarin_breastmilk.columns = ["metabolite", "flux"]
added_df_Mandarin_breastmilk = pd.concat([skeleton_Mandarin_breastmilk[["metabolite", "flux"]], added_df_Mandarin_breastmilk])
added_df_Mango_breastmilk = added_Mango_breastmilk.reset_index() 
added_df_Mango_breastmilk.iloc[:, 0] = added_df_Mango_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Mango_breastmilk.columns = ["metabolite", "flux"]
added_df_Mango_breastmilk = pd.concat([skeleton_Mango_breastmilk[["metabolite", "flux"]], added_df_Mango_breastmilk])
added_df_Melon_breastmilk = added_Melon_breastmilk.reset_index() 
added_df_Melon_breastmilk.iloc[:, 0] = added_df_Melon_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Melon_breastmilk.columns = ["metabolite", "flux"]
added_df_Melon_breastmilk = pd.concat([skeleton_Melon_breastmilk[["metabolite", "flux"]], added_df_Melon_breastmilk])
added_df_Nectarine_breastmilk = added_Nectarine_breastmilk.reset_index() 
added_df_Nectarine_breastmilk.iloc[:, 0] = added_df_Nectarine_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Nectarine_breastmilk.columns = ["metabolite", "flux"]
added_df_Nectarine_breastmilk = pd.concat([skeleton_Nectarine_breastmilk[["metabolite", "flux"]], added_df_Nectarine_breastmilk])
added_df_Orange_breastmilk = added_Orange_breastmilk.reset_index() 
added_df_Orange_breastmilk.iloc[:, 0] = added_df_Orange_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Orange_breastmilk.columns = ["metabolite", "flux"]
added_df_Orange_breastmilk = pd.concat([skeleton_Orange_breastmilk[["metabolite", "flux"]], added_df_Orange_breastmilk])
added_df_Peache_breastmilk = added_Peache_breastmilk.reset_index() 
added_df_Peache_breastmilk.iloc[:, 0] = added_df_Peache_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Peache_breastmilk.columns = ["metabolite", "flux"]
added_df_Peache_breastmilk = pd.concat([skeleton_Peache_breastmilk[["metabolite", "flux"]], added_df_Peache_breastmilk])
added_df_Pear_breastmilk = added_Pear_breastmilk.reset_index() 
added_df_Pear_breastmilk.iloc[:, 0] = added_df_Pear_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Pear_breastmilk.columns = ["metabolite", "flux"]
added_df_Pear_breastmilk = pd.concat([skeleton_Pear_breastmilk[["metabolite", "flux"]], added_df_Pear_breastmilk])
added_df_Pineapple_breastmilk = added_Pineapple_breastmilk.reset_index() 
added_df_Pineapple_breastmilk.iloc[:, 0] = added_df_Pineapple_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Pineapple_breastmilk.columns = ["metabolite", "flux"]
added_df_Pineapple_breastmilk = pd.concat([skeleton_Pineapple_breastmilk[["metabolite", "flux"]], added_df_Pineapple_breastmilk])
added_df_Plum_breastmilk = added_Plum_breastmilk.reset_index() 
added_df_Plum_breastmilk.iloc[:, 0] = added_df_Plum_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Plum_breastmilk.columns = ["metabolite", "flux"]
added_df_Plum_breastmilk = pd.concat([skeleton_Plum_breastmilk[["metabolite", "flux"]], added_df_Plum_breastmilk])
added_df_Raspberries_breastmilk = added_Raspberries_breastmilk.reset_index() 
added_df_Raspberries_breastmilk.iloc[:, 0] = added_df_Raspberries_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Raspberries_breastmilk.columns = ["metabolite", "flux"]
added_df_Raspberries_breastmilk = pd.concat([skeleton_Raspberries_breastmilk[["metabolite", "flux"]], added_df_Raspberries_breastmilk])
added_df_Strawberries_breastmilk = added_Strawberries_breastmilk.reset_index() 
added_df_Strawberries_breastmilk.iloc[:, 0] = added_df_Strawberries_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Strawberries_breastmilk.columns = ["metabolite", "flux"]
added_df_Strawberries_breastmilk = pd.concat([skeleton_Strawberries_breastmilk[["metabolite", "flux"]], added_df_Strawberries_breastmilk])
added_df_Barley_breastmilk = added_Barley_breastmilk.reset_index() 
added_df_Barley_breastmilk.iloc[:, 0] = added_df_Barley_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Barley_breastmilk.columns = ["metabolite", "flux"]
added_df_Barley_breastmilk = pd.concat([skeleton_Barley_breastmilk[["metabolite", "flux"]], added_df_Barley_breastmilk])
added_df_Barley_cereal_breastmilk = added_Barley_cereal_breastmilk.reset_index() 
added_df_Barley_cereal_breastmilk.iloc[:, 0] = added_df_Barley_cereal_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Barley_cereal_breastmilk.columns = ["metabolite", "flux"]
added_df_Barley_cereal_breastmilk = pd.concat([skeleton_Barley_cereal_breastmilk[["metabolite", "flux"]], added_df_Barley_cereal_breastmilk])
added_df_Couscous_breastmilk = added_Couscous_breastmilk.reset_index() 
added_df_Couscous_breastmilk.iloc[:, 0] = added_df_Couscous_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Couscous_breastmilk.columns = ["metabolite", "flux"]
added_df_Couscous_breastmilk = pd.concat([skeleton_Couscous_breastmilk[["metabolite", "flux"]], added_df_Couscous_breastmilk])
added_df_Noodles_breastmilk = added_Noodles_breastmilk.reset_index() 
added_df_Noodles_breastmilk.iloc[:, 0] = added_df_Noodles_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Noodles_breastmilk.columns = ["metabolite", "flux"]
added_df_Noodles_breastmilk = pd.concat([skeleton_Noodles_breastmilk[["metabolite", "flux"]], added_df_Noodles_breastmilk])
added_df_Oat_cereal_breastmilk = added_Oat_cereal_breastmilk.reset_index() 
added_df_Oat_cereal_breastmilk.iloc[:, 0] = added_df_Oat_cereal_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Oat_cereal_breastmilk.columns = ["metabolite", "flux"]
added_df_Oat_cereal_breastmilk = pd.concat([skeleton_Oat_cereal_breastmilk[["metabolite", "flux"]], added_df_Oat_cereal_breastmilk])
added_df_Pasta_breastmilk = added_Pasta_breastmilk.reset_index() 
added_df_Pasta_breastmilk.iloc[:, 0] = added_df_Pasta_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Pasta_breastmilk.columns = ["metabolite", "flux"]
added_df_Pasta_breastmilk = pd.concat([skeleton_Pasta_breastmilk[["metabolite", "flux"]], added_df_Pasta_breastmilk])
added_df_Rice_breastmilk = added_Rice_breastmilk.reset_index() 
added_df_Rice_breastmilk.iloc[:, 0] = added_df_Rice_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Rice_breastmilk.columns = ["metabolite", "flux"]
added_df_Rice_breastmilk = pd.concat([skeleton_Rice_breastmilk[["metabolite", "flux"]], added_df_Rice_breastmilk])
added_df_Rice_cereal_breastmilk = added_Rice_cereal_breastmilk.reset_index() 
added_df_Rice_cereal_breastmilk.iloc[:, 0] = added_df_Rice_cereal_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Rice_cereal_breastmilk.columns = ["metabolite", "flux"]
added_df_Rice_cereal_breastmilk = pd.concat([skeleton_Rice_cereal_breastmilk[["metabolite", "flux"]], added_df_Rice_cereal_breastmilk])
added_df_Tapioca_pudding_breastmilk = added_Tapioca_pudding_breastmilk.reset_index() 
added_df_Tapioca_pudding_breastmilk.iloc[:, 0] = added_df_Tapioca_pudding_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Tapioca_pudding_breastmilk.columns = ["metabolite", "flux"]
added_df_Tapioca_pudding_breastmilk = pd.concat([skeleton_Tapioca_pudding_breastmilk[["metabolite", "flux"]], added_df_Tapioca_pudding_breastmilk])
added_df_White_bread_breastmilk = added_White_bread_breastmilk.reset_index() 
added_df_White_bread_breastmilk.iloc[:, 0] = added_df_White_bread_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_White_bread_breastmilk.columns = ["metabolite", "flux"]
added_df_White_bread_breastmilk = pd.concat([skeleton_White_bread_breastmilk[["metabolite", "flux"]], added_df_White_bread_breastmilk])
added_df_Wholegrain_bread_breastmilk = added_Wholegrain_bread_breastmilk.reset_index() 
added_df_Wholegrain_bread_breastmilk.iloc[:, 0] = added_df_Wholegrain_bread_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Wholegrain_bread_breastmilk.columns = ["metabolite", "flux"]
added_df_Wholegrain_bread_breastmilk = pd.concat([skeleton_Wholegrain_bread_breastmilk[["metabolite", "flux"]], added_df_Wholegrain_bread_breastmilk])
added_df_Cottage_cheese_breastmilk = added_Cottage_cheese_breastmilk.reset_index() 
added_df_Cottage_cheese_breastmilk.iloc[:, 0] = added_df_Cottage_cheese_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Cottage_cheese_breastmilk.columns = ["metabolite", "flux"]
added_df_Cottage_cheese_breastmilk = pd.concat([skeleton_Cottage_cheese_breastmilk[["metabolite", "flux"]], added_df_Cottage_cheese_breastmilk])
added_df_Eggs_breastmilk = added_Eggs_breastmilk.reset_index() 
added_df_Eggs_breastmilk.iloc[:, 0] = added_df_Eggs_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Eggs_breastmilk.columns = ["metabolite", "flux"]
added_df_Eggs_breastmilk = pd.concat([skeleton_Eggs_breastmilk[["metabolite", "flux"]], added_df_Eggs_breastmilk])
added_df_Mozzarella_cheese_breastmilk = added_Mozzarella_cheese_breastmilk.reset_index() 
added_df_Mozzarella_cheese_breastmilk.iloc[:, 0] = added_df_Mozzarella_cheese_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Mozzarella_cheese_breastmilk.columns = ["metabolite", "flux"]
added_df_Mozzarella_cheese_breastmilk = pd.concat([skeleton_Mozzarella_cheese_breastmilk[["metabolite", "flux"]], added_df_Mozzarella_cheese_breastmilk])
added_df_Soymilk_breastmilk = added_Soymilk_breastmilk.reset_index() 
added_df_Soymilk_breastmilk.iloc[:, 0] = added_df_Soymilk_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Soymilk_breastmilk.columns = ["metabolite", "flux"]
added_df_Soymilk_breastmilk = pd.concat([skeleton_Soymilk_breastmilk[["metabolite", "flux"]], added_df_Soymilk_breastmilk])
added_df_Tofu_breastmilk = added_Tofu_breastmilk.reset_index() 
added_df_Tofu_breastmilk.iloc[:, 0] = added_df_Tofu_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Tofu_breastmilk.columns = ["metabolite", "flux"]
added_df_Tofu_breastmilk = pd.concat([skeleton_Tofu_breastmilk[["metabolite", "flux"]], added_df_Tofu_breastmilk])
added_df_Whole_milk_breastmilk = added_Whole_milk_breastmilk.reset_index() 
added_df_Whole_milk_breastmilk.iloc[:, 0] = added_df_Whole_milk_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Whole_milk_breastmilk.columns = ["metabolite", "flux"]
added_df_Whole_milk_breastmilk = pd.concat([skeleton_Whole_milk_breastmilk[["metabolite", "flux"]], added_df_Whole_milk_breastmilk])
added_df_Yoghurt_breastmilk = added_Yoghurt_breastmilk.reset_index() 
added_df_Yoghurt_breastmilk.iloc[:, 0] = added_df_Yoghurt_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Yoghurt_breastmilk.columns = ["metabolite", "flux"]
added_df_Yoghurt_breastmilk = pd.concat([skeleton_Yoghurt_breastmilk[["metabolite", "flux"]], added_df_Yoghurt_breastmilk])
added_df_Beef_breastmilk = added_Beef_breastmilk.reset_index() 
added_df_Beef_breastmilk.iloc[:, 0] = added_df_Beef_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Beef_breastmilk.columns = ["metabolite", "flux"]
added_df_Beef_breastmilk = pd.concat([skeleton_Beef_breastmilk[["metabolite", "flux"]], added_df_Beef_breastmilk])
added_df_Chicken_breastmilk = added_Chicken_breastmilk.reset_index() 
added_df_Chicken_breastmilk.iloc[:, 0] = added_df_Chicken_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Chicken_breastmilk.columns = ["metabolite", "flux"]
added_df_Chicken_breastmilk = pd.concat([skeleton_Chicken_breastmilk[["metabolite", "flux"]], added_df_Chicken_breastmilk])
added_df_Codfish_breastmilk = added_Codfish_breastmilk.reset_index() 
added_df_Codfish_breastmilk.iloc[:, 0] = added_df_Codfish_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Codfish_breastmilk.columns = ["metabolite", "flux"]
added_df_Codfish_breastmilk = pd.concat([skeleton_Codfish_breastmilk[["metabolite", "flux"]], added_df_Codfish_breastmilk])
added_df_Lamb_breastmilk = added_Lamb_breastmilk.reset_index() 
added_df_Lamb_breastmilk.iloc[:, 0] = added_df_Lamb_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Lamb_breastmilk.columns = ["metabolite", "flux"]
added_df_Lamb_breastmilk = pd.concat([skeleton_Lamb_breastmilk[["metabolite", "flux"]], added_df_Lamb_breastmilk])
added_df_Mackerel_breastmilk = added_Mackerel_breastmilk.reset_index() 
added_df_Mackerel_breastmilk.iloc[:, 0] = added_df_Mackerel_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Mackerel_breastmilk.columns = ["metabolite", "flux"]
added_df_Mackerel_breastmilk = pd.concat([skeleton_Mackerel_breastmilk[["metabolite", "flux"]], added_df_Mackerel_breastmilk])
added_df_Mussels_breastmilk = added_Mussels_breastmilk.reset_index() 
added_df_Mussels_breastmilk.iloc[:, 0] = added_df_Mussels_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Mussels_breastmilk.columns = ["metabolite", "flux"]
added_df_Mussels_breastmilk = pd.concat([skeleton_Mussels_breastmilk[["metabolite", "flux"]], added_df_Mussels_breastmilk])
added_df_Pork_breastmilk = added_Pork_breastmilk.reset_index() 
added_df_Pork_breastmilk.iloc[:, 0] = added_df_Pork_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Pork_breastmilk.columns = ["metabolite", "flux"]
added_df_Pork_breastmilk = pd.concat([skeleton_Pork_breastmilk[["metabolite", "flux"]], added_df_Pork_breastmilk])
added_df_Salmon_breastmilk = added_Salmon_breastmilk.reset_index() 
added_df_Salmon_breastmilk.iloc[:, 0] = added_df_Salmon_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Salmon_breastmilk.columns = ["metabolite", "flux"]
added_df_Salmon_breastmilk = pd.concat([skeleton_Salmon_breastmilk[["metabolite", "flux"]], added_df_Salmon_breastmilk])
added_df_Shrimp_breastmilk = added_Shrimp_breastmilk.reset_index() 
added_df_Shrimp_breastmilk.iloc[:, 0] = added_df_Shrimp_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Shrimp_breastmilk.columns = ["metabolite", "flux"]
added_df_Shrimp_breastmilk = pd.concat([skeleton_Shrimp_breastmilk[["metabolite", "flux"]], added_df_Shrimp_breastmilk])
added_df_Tuna_breastmilk = added_Tuna_breastmilk.reset_index() 
added_df_Tuna_breastmilk.iloc[:, 0] = added_df_Tuna_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Tuna_breastmilk.columns = ["metabolite", "flux"]
added_df_Tuna_breastmilk = pd.concat([skeleton_Tuna_breastmilk[["metabolite", "flux"]], added_df_Tuna_breastmilk])
added_df_Turkey_breastmilk = added_Turkey_breastmilk.reset_index() 
added_df_Turkey_breastmilk.iloc[:, 0] = added_df_Turkey_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Turkey_breastmilk.columns = ["metabolite", "flux"]
added_df_Turkey_breastmilk = pd.concat([skeleton_Turkey_breastmilk[["metabolite", "flux"]], added_df_Turkey_breastmilk])
added_df_Almond_breastmilk = added_Almond_breastmilk.reset_index() 
added_df_Almond_breastmilk.iloc[:, 0] = added_df_Almond_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Almond_breastmilk.columns = ["metabolite", "flux"]
added_df_Almond_breastmilk = pd.concat([skeleton_Almond_breastmilk[["metabolite", "flux"]], added_df_Almond_breastmilk])
added_df_Black_beans_breastmilk = added_Black_beans_breastmilk.reset_index() 
added_df_Black_beans_breastmilk.iloc[:, 0] = added_df_Black_beans_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Black_beans_breastmilk.columns = ["metabolite", "flux"]
added_df_Black_beans_breastmilk = pd.concat([skeleton_Black_beans_breastmilk[["metabolite", "flux"]], added_df_Black_beans_breastmilk])
added_df_Cashew_breastmilk = added_Cashew_breastmilk.reset_index() 
added_df_Cashew_breastmilk.iloc[:, 0] = added_df_Cashew_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Cashew_breastmilk.columns = ["metabolite", "flux"]
added_df_Cashew_breastmilk = pd.concat([skeleton_Cashew_breastmilk[["metabolite", "flux"]], added_df_Cashew_breastmilk])
added_df_Chia_breastmilk = added_Chia_breastmilk.reset_index() 
added_df_Chia_breastmilk.iloc[:, 0] = added_df_Chia_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Chia_breastmilk.columns = ["metabolite", "flux"]
added_df_Chia_breastmilk = pd.concat([skeleton_Chia_breastmilk[["metabolite", "flux"]], added_df_Chia_breastmilk])
added_df_Chickpea_breastmilk = added_Chickpea_breastmilk.reset_index() 
added_df_Chickpea_breastmilk.iloc[:, 0] = added_df_Chickpea_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Chickpea_breastmilk.columns = ["metabolite", "flux"]
added_df_Chickpea_breastmilk = pd.concat([skeleton_Chickpea_breastmilk[["metabolite", "flux"]], added_df_Chickpea_breastmilk])
added_df_Green_peas_breastmilk = added_Green_peas_breastmilk.reset_index() 
added_df_Green_peas_breastmilk.iloc[:, 0] = added_df_Green_peas_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Green_peas_breastmilk.columns = ["metabolite", "flux"]
added_df_Green_peas_breastmilk = pd.concat([skeleton_Green_peas_breastmilk[["metabolite", "flux"]], added_df_Green_peas_breastmilk])
added_df_Hazelnut_breastmilk = added_Hazelnut_breastmilk.reset_index() 
added_df_Hazelnut_breastmilk.iloc[:, 0] = added_df_Hazelnut_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Hazelnut_breastmilk.columns = ["metabolite", "flux"]
added_df_Hazelnut_breastmilk = pd.concat([skeleton_Hazelnut_breastmilk[["metabolite", "flux"]], added_df_Hazelnut_breastmilk])
added_df_Lentils_breastmilk = added_Lentils_breastmilk.reset_index() 
added_df_Lentils_breastmilk.iloc[:, 0] = added_df_Lentils_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Lentils_breastmilk.columns = ["metabolite", "flux"]
added_df_Lentils_breastmilk = pd.concat([skeleton_Lentils_breastmilk[["metabolite", "flux"]], added_df_Lentils_breastmilk])
added_df_Peanut_breastmilk = added_Peanut_breastmilk.reset_index() 
added_df_Peanut_breastmilk.iloc[:, 0] = added_df_Peanut_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Peanut_breastmilk.columns = ["metabolite", "flux"]
added_df_Peanut_breastmilk = pd.concat([skeleton_Peanut_breastmilk[["metabolite", "flux"]], added_df_Peanut_breastmilk])
added_df_Pecans_breastmilk = added_Pecans_breastmilk.reset_index() 
added_df_Pecans_breastmilk.iloc[:, 0] = added_df_Pecans_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Pecans_breastmilk.columns = ["metabolite", "flux"]
added_df_Pecans_breastmilk = pd.concat([skeleton_Pecans_breastmilk[["metabolite", "flux"]], added_df_Pecans_breastmilk])
added_df_Pumpkin_seed_breastmilk = added_Pumpkin_seed_breastmilk.reset_index() 
added_df_Pumpkin_seed_breastmilk.iloc[:, 0] = added_df_Pumpkin_seed_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Pumpkin_seed_breastmilk.columns = ["metabolite", "flux"]
added_df_Pumpkin_seed_breastmilk = pd.concat([skeleton_Pumpkin_seed_breastmilk[["metabolite", "flux"]], added_df_Pumpkin_seed_breastmilk])
added_df_Red_beans_breastmilk = added_Red_beans_breastmilk.reset_index() 
added_df_Red_beans_breastmilk.iloc[:, 0] = added_df_Red_beans_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Red_beans_breastmilk.columns = ["metabolite", "flux"]
added_df_Red_beans_breastmilk = pd.concat([skeleton_Red_beans_breastmilk[["metabolite", "flux"]], added_df_Red_beans_breastmilk])
added_df_Soybean_breastmilk = added_Soybean_breastmilk.reset_index() 
added_df_Soybean_breastmilk.iloc[:, 0] = added_df_Soybean_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Soybean_breastmilk.columns = ["metabolite", "flux"]
added_df_Soybean_breastmilk = pd.concat([skeleton_Soybean_breastmilk[["metabolite", "flux"]], added_df_Soybean_breastmilk])
added_df_Split_peas_breastmilk = added_Split_peas_breastmilk.reset_index() 
added_df_Split_peas_breastmilk.iloc[:, 0] = added_df_Split_peas_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Split_peas_breastmilk.columns = ["metabolite", "flux"]
added_df_Split_peas_breastmilk = pd.concat([skeleton_Split_peas_breastmilk[["metabolite", "flux"]], added_df_Split_peas_breastmilk])
added_df_Sunflower_seed_breastmilk = added_Sunflower_seed_breastmilk.reset_index() 
added_df_Sunflower_seed_breastmilk.iloc[:, 0] = added_df_Sunflower_seed_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_Sunflower_seed_breastmilk.columns = ["metabolite", "flux"]
added_df_Sunflower_seed_breastmilk = pd.concat([skeleton_Sunflower_seed_breastmilk[["metabolite", "flux"]], added_df_Sunflower_seed_breastmilk])
added_df_White_beans_breastmilk = added_White_beans_breastmilk.reset_index() 
added_df_White_beans_breastmilk.iloc[:, 0] = added_df_White_beans_breastmilk.iloc[:, 0].str.replace("EX_|_m$", "", regex=True)
added_df_White_beans_breastmilk.columns = ["metabolite", "flux"]
added_df_White_beans_breastmilk = pd.concat([skeleton_White_beans_breastmilk[["metabolite", "flux"]], added_df_White_beans_breastmilk])

completed_Broccoli_breastmilk = pd.merge(added_df_Broccoli_breastmilk, annotations, on="metabolite", how="left")
completed_Broccoli_breastmilk["reaction"] = "EX_" + completed_Broccoli_breastmilk.metabolite + "_m"
completed_Broccoli_breastmilk["global_id"] = "EX_" + completed_Broccoli_breastmilk.metabolite + "(e)"
completed_Brussel_breastmilk = pd.merge(added_df_Brussel_breastmilk, annotations, on="metabolite", how="left")
completed_Brussel_breastmilk["reaction"] = "EX_" + completed_Brussel_breastmilk.metabolite + "_m"
completed_Brussel_breastmilk["global_id"] = "EX_" + completed_Brussel_breastmilk.metabolite + "(e)"
completed_Cabbage_breastmilk = pd.merge(added_df_Cabbage_breastmilk, annotations, on="metabolite", how="left")
completed_Cabbage_breastmilk["reaction"] = "EX_" + completed_Cabbage_breastmilk.metabolite + "_m"
completed_Cabbage_breastmilk["global_id"] = "EX_" + completed_Cabbage_breastmilk.metabolite + "(e)"
completed_Carrot_breastmilk = pd.merge(added_df_Carrot_breastmilk, annotations, on="metabolite", how="left")
completed_Carrot_breastmilk["reaction"] = "EX_" + completed_Carrot_breastmilk.metabolite + "_m"
completed_Carrot_breastmilk["global_id"] = "EX_" + completed_Carrot_breastmilk.metabolite + "(e)"
completed_Cauliflower_breastmilk = pd.merge(added_df_Cauliflower_breastmilk, annotations, on="metabolite", how="left")
completed_Cauliflower_breastmilk["reaction"] = "EX_" + completed_Cauliflower_breastmilk.metabolite + "_m"
completed_Cauliflower_breastmilk["global_id"] = "EX_" + completed_Cauliflower_breastmilk.metabolite + "(e)"
completed_Celery_breastmilk = pd.merge(added_df_Celery_breastmilk, annotations, on="metabolite", how="left")
completed_Celery_breastmilk["reaction"] = "EX_" + completed_Celery_breastmilk.metabolite + "_m"
completed_Celery_breastmilk["global_id"] = "EX_" + completed_Celery_breastmilk.metabolite + "(e)"
completed_Cucumber_breastmilk = pd.merge(added_df_Cucumber_breastmilk, annotations, on="metabolite", how="left")
completed_Cucumber_breastmilk["reaction"] = "EX_" + completed_Cucumber_breastmilk.metabolite + "_m"
completed_Cucumber_breastmilk["global_id"] = "EX_" + completed_Cucumber_breastmilk.metabolite + "(e)"
completed_Eggplant_breastmilk = pd.merge(added_df_Eggplant_breastmilk, annotations, on="metabolite", how="left")
completed_Eggplant_breastmilk["reaction"] = "EX_" + completed_Eggplant_breastmilk.metabolite + "_m"
completed_Eggplant_breastmilk["global_id"] = "EX_" + completed_Eggplant_breastmilk.metabolite + "(e)"
completed_Green_beans_breastmilk = pd.merge(added_df_Green_beans_breastmilk, annotations, on="metabolite", how="left")
completed_Green_beans_breastmilk["reaction"] = "EX_" + completed_Green_beans_breastmilk.metabolite + "_m"
completed_Green_beans_breastmilk["global_id"] = "EX_" + completed_Green_beans_breastmilk.metabolite + "(e)"
completed_Green_capsicum_breastmilk = pd.merge(added_df_Green_capsicum_breastmilk, annotations, on="metabolite", how="left")
completed_Green_capsicum_breastmilk["reaction"] = "EX_" + completed_Green_capsicum_breastmilk.metabolite + "_m"
completed_Green_capsicum_breastmilk["global_id"] = "EX_" + completed_Green_capsicum_breastmilk.metabolite + "(e)"
completed_Lettuce_breastmilk = pd.merge(added_df_Lettuce_breastmilk, annotations, on="metabolite", how="left")
completed_Lettuce_breastmilk["reaction"] = "EX_" + completed_Lettuce_breastmilk.metabolite + "_m"
completed_Lettuce_breastmilk["global_id"] = "EX_" + completed_Lettuce_breastmilk.metabolite + "(e)"
completed_Mushroom_breastmilk = pd.merge(added_df_Mushroom_breastmilk, annotations, on="metabolite", how="left")
completed_Mushroom_breastmilk["reaction"] = "EX_" + completed_Mushroom_breastmilk.metabolite + "_m"
completed_Mushroom_breastmilk["global_id"] = "EX_" + completed_Mushroom_breastmilk.metabolite + "(e)"
completed_Onion_breastmilk = pd.merge(added_df_Onion_breastmilk, annotations, on="metabolite", how="left")
completed_Onion_breastmilk["reaction"] = "EX_" + completed_Onion_breastmilk.metabolite + "_m"
completed_Onion_breastmilk["global_id"] = "EX_" + completed_Onion_breastmilk.metabolite + "(e)"
completed_Pak_choi_breastmilk = pd.merge(added_df_Pak_choi_breastmilk, annotations, on="metabolite", how="left")
completed_Pak_choi_breastmilk["reaction"] = "EX_" + completed_Pak_choi_breastmilk.metabolite + "_m"
completed_Pak_choi_breastmilk["global_id"] = "EX_" + completed_Pak_choi_breastmilk.metabolite + "(e)"
completed_Potato_breastmilk = pd.merge(added_df_Potato_breastmilk, annotations, on="metabolite", how="left")
completed_Potato_breastmilk["reaction"] = "EX_" + completed_Potato_breastmilk.metabolite + "_m"
completed_Potato_breastmilk["global_id"] = "EX_" + completed_Potato_breastmilk.metabolite + "(e)"
completed_Pumpkin_breastmilk = pd.merge(added_df_Pumpkin_breastmilk, annotations, on="metabolite", how="left")
completed_Pumpkin_breastmilk["reaction"] = "EX_" + completed_Pumpkin_breastmilk.metabolite + "_m"
completed_Pumpkin_breastmilk["global_id"] = "EX_" + completed_Pumpkin_breastmilk.metabolite + "(e)"
completed_Sweetcorn_breastmilk = pd.merge(added_df_Sweetcorn_breastmilk, annotations, on="metabolite", how="left")
completed_Sweetcorn_breastmilk["reaction"] = "EX_" + completed_Sweetcorn_breastmilk.metabolite + "_m"
completed_Sweetcorn_breastmilk["global_id"] = "EX_" + completed_Sweetcorn_breastmilk.metabolite + "(e)"
completed_Spinach_breastmilk = pd.merge(added_df_Spinach_breastmilk, annotations, on="metabolite", how="left")
completed_Spinach_breastmilk["reaction"] = "EX_" + completed_Spinach_breastmilk.metabolite + "_m"
completed_Spinach_breastmilk["global_id"] = "EX_" + completed_Spinach_breastmilk.metabolite + "(e)"
completed_Squash_breastmilk = pd.merge(added_df_Squash_breastmilk, annotations, on="metabolite", how="left")
completed_Squash_breastmilk["reaction"] = "EX_" + completed_Squash_breastmilk.metabolite + "_m"
completed_Squash_breastmilk["global_id"] = "EX_" + completed_Squash_breastmilk.metabolite + "(e)"
completed_Sweet_potato_breastmilk = pd.merge(added_df_Sweet_potato_breastmilk, annotations, on="metabolite", how="left")
completed_Sweet_potato_breastmilk["reaction"] = "EX_" + completed_Sweet_potato_breastmilk.metabolite + "_m"
completed_Sweet_potato_breastmilk["global_id"] = "EX_" + completed_Sweet_potato_breastmilk.metabolite + "(e)"
completed_Tomato_breastmilk = pd.merge(added_df_Tomato_breastmilk, annotations, on="metabolite", how="left")
completed_Tomato_breastmilk["reaction"] = "EX_" + completed_Tomato_breastmilk.metabolite + "_m"
completed_Tomato_breastmilk["global_id"] = "EX_" + completed_Tomato_breastmilk.metabolite + "(e)"
completed_Yam_breastmilk = pd.merge(added_df_Yam_breastmilk, annotations, on="metabolite", how="left")
completed_Yam_breastmilk["reaction"] = "EX_" + completed_Yam_breastmilk.metabolite + "_m"
completed_Yam_breastmilk["global_id"] = "EX_" + completed_Yam_breastmilk.metabolite + "(e)"
completed_Zucchini_breastmilk = pd.merge(added_df_Zucchini_breastmilk, annotations, on="metabolite", how="left")
completed_Zucchini_breastmilk["reaction"] = "EX_" + completed_Zucchini_breastmilk.metabolite + "_m"
completed_Zucchini_breastmilk["global_id"] = "EX_" + completed_Zucchini_breastmilk.metabolite + "(e)"
completed_Apple_breastmilk = pd.merge(added_df_Apple_breastmilk, annotations, on="metabolite", how="left")
completed_Apple_breastmilk["reaction"] = "EX_" + completed_Apple_breastmilk.metabolite + "_m"
completed_Apple_breastmilk["global_id"] = "EX_" + completed_Apple_breastmilk.metabolite + "(e)"
completed_Banana_breastmilk = pd.merge(added_df_Banana_breastmilk, annotations, on="metabolite", how="left")
completed_Banana_breastmilk["reaction"] = "EX_" + completed_Banana_breastmilk.metabolite + "_m"
completed_Banana_breastmilk["global_id"] = "EX_" + completed_Banana_breastmilk.metabolite + "(e)"
completed_Blackcurrant_breastmilk = pd.merge(added_df_Blackcurrant_breastmilk, annotations, on="metabolite", how="left")
completed_Blackcurrant_breastmilk["reaction"] = "EX_" + completed_Blackcurrant_breastmilk.metabolite + "_m"
completed_Blackcurrant_breastmilk["global_id"] = "EX_" + completed_Blackcurrant_breastmilk.metabolite + "(e)"
completed_Blueberries_breastmilk = pd.merge(added_df_Blueberries_breastmilk, annotations, on="metabolite", how="left")
completed_Blueberries_breastmilk["reaction"] = "EX_" + completed_Blueberries_breastmilk.metabolite + "_m"
completed_Blueberries_breastmilk["global_id"] = "EX_" + completed_Blueberries_breastmilk.metabolite + "(e)"
completed_Cherry_breastmilk = pd.merge(added_df_Cherry_breastmilk, annotations, on="metabolite", how="left")
completed_Cherry_breastmilk["reaction"] = "EX_" + completed_Cherry_breastmilk.metabolite + "_m"
completed_Cherry_breastmilk["global_id"] = "EX_" + completed_Cherry_breastmilk.metabolite + "(e)"
completed_Feijoa_breastmilk = pd.merge(added_df_Feijoa_breastmilk, annotations, on="metabolite", how="left")
completed_Feijoa_breastmilk["reaction"] = "EX_" + completed_Feijoa_breastmilk.metabolite + "_m"
completed_Feijoa_breastmilk["global_id"] = "EX_" + completed_Feijoa_breastmilk.metabolite + "(e)"
completed_Gold_kiwifruit_breastmilk = pd.merge(added_df_Gold_kiwifruit_breastmilk, annotations, on="metabolite", how="left")
completed_Gold_kiwifruit_breastmilk["reaction"] = "EX_" + completed_Gold_kiwifruit_breastmilk.metabolite + "_m"
completed_Gold_kiwifruit_breastmilk["global_id"] = "EX_" + completed_Gold_kiwifruit_breastmilk.metabolite + "(e)"
completed_Grape_breastmilk = pd.merge(added_df_Grape_breastmilk, annotations, on="metabolite", how="left")
completed_Grape_breastmilk["reaction"] = "EX_" + completed_Grape_breastmilk.metabolite + "_m"
completed_Grape_breastmilk["global_id"] = "EX_" + completed_Grape_breastmilk.metabolite + "(e)"
completed_Grapefruit_breastmilk = pd.merge(added_df_Grapefruit_breastmilk, annotations, on="metabolite", how="left")
completed_Grapefruit_breastmilk["reaction"] = "EX_" + completed_Grapefruit_breastmilk.metabolite + "_m"
completed_Grapefruit_breastmilk["global_id"] = "EX_" + completed_Grapefruit_breastmilk.metabolite + "(e)"
completed_Green_kiwifruit_breastmilk = pd.merge(added_df_Green_kiwifruit_breastmilk, annotations, on="metabolite", how="left")
completed_Green_kiwifruit_breastmilk["reaction"] = "EX_" + completed_Green_kiwifruit_breastmilk.metabolite + "_m"
completed_Green_kiwifruit_breastmilk["global_id"] = "EX_" + completed_Green_kiwifruit_breastmilk.metabolite + "(e)"
completed_Mandarin_breastmilk = pd.merge(added_df_Mandarin_breastmilk, annotations, on="metabolite", how="left")
completed_Mandarin_breastmilk["reaction"] = "EX_" + completed_Mandarin_breastmilk.metabolite + "_m"
completed_Mandarin_breastmilk["global_id"] = "EX_" + completed_Mandarin_breastmilk.metabolite + "(e)"
completed_Mango_breastmilk = pd.merge(added_df_Mango_breastmilk, annotations, on="metabolite", how="left")
completed_Mango_breastmilk["reaction"] = "EX_" + completed_Mango_breastmilk.metabolite + "_m"
completed_Mango_breastmilk["global_id"] = "EX_" + completed_Mango_breastmilk.metabolite + "(e)"
completed_Melon_breastmilk = pd.merge(added_df_Melon_breastmilk, annotations, on="metabolite", how="left")
completed_Melon_breastmilk["reaction"] = "EX_" + completed_Melon_breastmilk.metabolite + "_m"
completed_Melon_breastmilk["global_id"] = "EX_" + completed_Melon_breastmilk.metabolite + "(e)"
completed_Nectarine_breastmilk = pd.merge(added_df_Nectarine_breastmilk, annotations, on="metabolite", how="left")
completed_Nectarine_breastmilk["reaction"] = "EX_" + completed_Nectarine_breastmilk.metabolite + "_m"
completed_Nectarine_breastmilk["global_id"] = "EX_" + completed_Nectarine_breastmilk.metabolite + "(e)"
completed_Orange_breastmilk = pd.merge(added_df_Orange_breastmilk, annotations, on="metabolite", how="left")
completed_Orange_breastmilk["reaction"] = "EX_" + completed_Orange_breastmilk.metabolite + "_m"
completed_Orange_breastmilk["global_id"] = "EX_" + completed_Orange_breastmilk.metabolite + "(e)"
completed_Peache_breastmilk = pd.merge(added_df_Peache_breastmilk, annotations, on="metabolite", how="left")
completed_Peache_breastmilk["reaction"] = "EX_" + completed_Peache_breastmilk.metabolite + "_m"
completed_Peache_breastmilk["global_id"] = "EX_" + completed_Peache_breastmilk.metabolite + "(e)"
completed_Pear_breastmilk = pd.merge(added_df_Pear_breastmilk, annotations, on="metabolite", how="left")
completed_Pear_breastmilk["reaction"] = "EX_" + completed_Pear_breastmilk.metabolite + "_m"
completed_Pear_breastmilk["global_id"] = "EX_" + completed_Pear_breastmilk.metabolite + "(e)"
completed_Pineapple_breastmilk = pd.merge(added_df_Pineapple_breastmilk, annotations, on="metabolite", how="left")
completed_Pineapple_breastmilk["reaction"] = "EX_" + completed_Pineapple_breastmilk.metabolite + "_m"
completed_Pineapple_breastmilk["global_id"] = "EX_" + completed_Pineapple_breastmilk.metabolite + "(e)"
completed_Plum_breastmilk = pd.merge(added_df_Plum_breastmilk, annotations, on="metabolite", how="left")
completed_Plum_breastmilk["reaction"] = "EX_" + completed_Plum_breastmilk.metabolite + "_m"
completed_Plum_breastmilk["global_id"] = "EX_" + completed_Plum_breastmilk.metabolite + "(e)"
completed_Raspberries_breastmilk = pd.merge(added_df_Raspberries_breastmilk, annotations, on="metabolite", how="left")
completed_Raspberries_breastmilk["reaction"] = "EX_" + completed_Raspberries_breastmilk.metabolite + "_m"
completed_Raspberries_breastmilk["global_id"] = "EX_" + completed_Raspberries_breastmilk.metabolite + "(e)"
completed_Strawberries_breastmilk = pd.merge(added_df_Strawberries_breastmilk, annotations, on="metabolite", how="left")
completed_Strawberries_breastmilk["reaction"] = "EX_" + completed_Strawberries_breastmilk.metabolite + "_m"
completed_Strawberries_breastmilk["global_id"] = "EX_" + completed_Strawberries_breastmilk.metabolite + "(e)"
completed_Barley_breastmilk = pd.merge(added_df_Barley_breastmilk, annotations, on="metabolite", how="left")
completed_Barley_breastmilk["reaction"] = "EX_" + completed_Barley_breastmilk.metabolite + "_m"
completed_Barley_breastmilk["global_id"] = "EX_" + completed_Barley_breastmilk.metabolite + "(e)"
completed_Barley_cereal_breastmilk = pd.merge(added_df_Barley_cereal_breastmilk, annotations, on="metabolite", how="left")
completed_Barley_cereal_breastmilk["reaction"] = "EX_" + completed_Barley_cereal_breastmilk.metabolite + "_m"
completed_Barley_cereal_breastmilk["global_id"] = "EX_" + completed_Barley_cereal_breastmilk.metabolite + "(e)"
completed_Couscous_breastmilk = pd.merge(added_df_Couscous_breastmilk, annotations, on="metabolite", how="left")
completed_Couscous_breastmilk["reaction"] = "EX_" + completed_Couscous_breastmilk.metabolite + "_m"
completed_Couscous_breastmilk["global_id"] = "EX_" + completed_Couscous_breastmilk.metabolite + "(e)"
completed_Noodles_breastmilk = pd.merge(added_df_Noodles_breastmilk, annotations, on="metabolite", how="left")
completed_Noodles_breastmilk["reaction"] = "EX_" + completed_Noodles_breastmilk.metabolite + "_m"
completed_Noodles_breastmilk["global_id"] = "EX_" + completed_Noodles_breastmilk.metabolite + "(e)"
completed_Oat_cereal_breastmilk = pd.merge(added_df_Oat_cereal_breastmilk, annotations, on="metabolite", how="left")
completed_Oat_cereal_breastmilk["reaction"] = "EX_" + completed_Oat_cereal_breastmilk.metabolite + "_m"
completed_Oat_cereal_breastmilk["global_id"] = "EX_" + completed_Oat_cereal_breastmilk.metabolite + "(e)"
completed_Pasta_breastmilk = pd.merge(added_df_Pasta_breastmilk, annotations, on="metabolite", how="left")
completed_Pasta_breastmilk["reaction"] = "EX_" + completed_Pasta_breastmilk.metabolite + "_m"
completed_Pasta_breastmilk["global_id"] = "EX_" + completed_Pasta_breastmilk.metabolite + "(e)"
completed_Rice_breastmilk = pd.merge(added_df_Rice_breastmilk, annotations, on="metabolite", how="left")
completed_Rice_breastmilk["reaction"] = "EX_" + completed_Rice_breastmilk.metabolite + "_m"
completed_Rice_breastmilk["global_id"] = "EX_" + completed_Rice_breastmilk.metabolite + "(e)"
completed_Rice_cereal_breastmilk = pd.merge(added_df_Rice_cereal_breastmilk, annotations, on="metabolite", how="left")
completed_Rice_cereal_breastmilk["reaction"] = "EX_" + completed_Rice_cereal_breastmilk.metabolite + "_m"
completed_Rice_cereal_breastmilk["global_id"] = "EX_" + completed_Rice_cereal_breastmilk.metabolite + "(e)"
completed_Tapioca_pudding_breastmilk = pd.merge(added_df_Tapioca_pudding_breastmilk, annotations, on="metabolite", how="left")
completed_Tapioca_pudding_breastmilk["reaction"] = "EX_" + completed_Tapioca_pudding_breastmilk.metabolite + "_m"
completed_Tapioca_pudding_breastmilk["global_id"] = "EX_" + completed_Tapioca_pudding_breastmilk.metabolite + "(e)"
completed_White_bread_breastmilk = pd.merge(added_df_White_bread_breastmilk, annotations, on="metabolite", how="left")
completed_White_bread_breastmilk["reaction"] = "EX_" + completed_White_bread_breastmilk.metabolite + "_m"
completed_White_bread_breastmilk["global_id"] = "EX_" + completed_White_bread_breastmilk.metabolite + "(e)"
completed_Wholegrain_bread_breastmilk = pd.merge(added_df_Wholegrain_bread_breastmilk, annotations, on="metabolite", how="left")
completed_Wholegrain_bread_breastmilk["reaction"] = "EX_" + completed_Wholegrain_bread_breastmilk.metabolite + "_m"
completed_Wholegrain_bread_breastmilk["global_id"] = "EX_" + completed_Wholegrain_bread_breastmilk.metabolite + "(e)"
completed_Cottage_cheese_breastmilk = pd.merge(added_df_Cottage_cheese_breastmilk, annotations, on="metabolite", how="left")
completed_Cottage_cheese_breastmilk["reaction"] = "EX_" + completed_Cottage_cheese_breastmilk.metabolite + "_m"
completed_Cottage_cheese_breastmilk["global_id"] = "EX_" + completed_Cottage_cheese_breastmilk.metabolite + "(e)"
completed_Eggs_breastmilk = pd.merge(added_df_Eggs_breastmilk, annotations, on="metabolite", how="left")
completed_Eggs_breastmilk["reaction"] = "EX_" + completed_Eggs_breastmilk.metabolite + "_m"
completed_Eggs_breastmilk["global_id"] = "EX_" + completed_Eggs_breastmilk.metabolite + "(e)"
completed_Mozzarella_cheese_breastmilk = pd.merge(added_df_Mozzarella_cheese_breastmilk, annotations, on="metabolite", how="left")
completed_Mozzarella_cheese_breastmilk["reaction"] = "EX_" + completed_Mozzarella_cheese_breastmilk.metabolite + "_m"
completed_Mozzarella_cheese_breastmilk["global_id"] = "EX_" + completed_Mozzarella_cheese_breastmilk.metabolite + "(e)"
completed_Soymilk_breastmilk = pd.merge(added_df_Soymilk_breastmilk, annotations, on="metabolite", how="left")
completed_Soymilk_breastmilk["reaction"] = "EX_" + completed_Soymilk_breastmilk.metabolite + "_m"
completed_Soymilk_breastmilk["global_id"] = "EX_" + completed_Soymilk_breastmilk.metabolite + "(e)"
completed_Tofu_breastmilk = pd.merge(added_df_Tofu_breastmilk, annotations, on="metabolite", how="left")
completed_Tofu_breastmilk["reaction"] = "EX_" + completed_Tofu_breastmilk.metabolite + "_m"
completed_Tofu_breastmilk["global_id"] = "EX_" + completed_Tofu_breastmilk.metabolite + "(e)"
completed_Whole_milk_breastmilk = pd.merge(added_df_Whole_milk_breastmilk, annotations, on="metabolite", how="left")
completed_Whole_milk_breastmilk["reaction"] = "EX_" + completed_Whole_milk_breastmilk.metabolite + "_m"
completed_Whole_milk_breastmilk["global_id"] = "EX_" + completed_Whole_milk_breastmilk.metabolite + "(e)"
completed_Yoghurt_breastmilk = pd.merge(added_df_Yoghurt_breastmilk, annotations, on="metabolite", how="left")
completed_Yoghurt_breastmilk["reaction"] = "EX_" + completed_Yoghurt_breastmilk.metabolite + "_m"
completed_Yoghurt_breastmilk["global_id"] = "EX_" + completed_Yoghurt_breastmilk.metabolite + "(e)"
completed_Beef_breastmilk = pd.merge(added_df_Beef_breastmilk, annotations, on="metabolite", how="left")
completed_Beef_breastmilk["reaction"] = "EX_" + completed_Beef_breastmilk.metabolite + "_m"
completed_Beef_breastmilk["global_id"] = "EX_" + completed_Beef_breastmilk.metabolite + "(e)"
completed_Chicken_breastmilk = pd.merge(added_df_Chicken_breastmilk, annotations, on="metabolite", how="left")
completed_Chicken_breastmilk["reaction"] = "EX_" + completed_Chicken_breastmilk.metabolite + "_m"
completed_Chicken_breastmilk["global_id"] = "EX_" + completed_Chicken_breastmilk.metabolite + "(e)"
completed_Codfish_breastmilk = pd.merge(added_df_Codfish_breastmilk, annotations, on="metabolite", how="left")
completed_Codfish_breastmilk["reaction"] = "EX_" + completed_Codfish_breastmilk.metabolite + "_m"
completed_Codfish_breastmilk["global_id"] = "EX_" + completed_Codfish_breastmilk.metabolite + "(e)"
completed_Lamb_breastmilk = pd.merge(added_df_Lamb_breastmilk, annotations, on="metabolite", how="left")
completed_Lamb_breastmilk["reaction"] = "EX_" + completed_Lamb_breastmilk.metabolite + "_m"
completed_Lamb_breastmilk["global_id"] = "EX_" + completed_Lamb_breastmilk.metabolite + "(e)"
completed_Mackerel_breastmilk = pd.merge(added_df_Mackerel_breastmilk, annotations, on="metabolite", how="left")
completed_Mackerel_breastmilk["reaction"] = "EX_" + completed_Mackerel_breastmilk.metabolite + "_m"
completed_Mackerel_breastmilk["global_id"] = "EX_" + completed_Mackerel_breastmilk.metabolite + "(e)"
completed_Mussels_breastmilk = pd.merge(added_df_Mussels_breastmilk, annotations, on="metabolite", how="left")
completed_Mussels_breastmilk["reaction"] = "EX_" + completed_Mussels_breastmilk.metabolite + "_m"
completed_Mussels_breastmilk["global_id"] = "EX_" + completed_Mussels_breastmilk.metabolite + "(e)"
completed_Pork_breastmilk = pd.merge(added_df_Pork_breastmilk, annotations, on="metabolite", how="left")
completed_Pork_breastmilk["reaction"] = "EX_" + completed_Pork_breastmilk.metabolite + "_m"
completed_Pork_breastmilk["global_id"] = "EX_" + completed_Pork_breastmilk.metabolite + "(e)"
completed_Salmon_breastmilk = pd.merge(added_df_Salmon_breastmilk, annotations, on="metabolite", how="left")
completed_Salmon_breastmilk["reaction"] = "EX_" + completed_Salmon_breastmilk.metabolite + "_m"
completed_Salmon_breastmilk["global_id"] = "EX_" + completed_Salmon_breastmilk.metabolite + "(e)"
completed_Shrimp_breastmilk = pd.merge(added_df_Shrimp_breastmilk, annotations, on="metabolite", how="left")
completed_Shrimp_breastmilk["reaction"] = "EX_" + completed_Shrimp_breastmilk.metabolite + "_m"
completed_Shrimp_breastmilk["global_id"] = "EX_" + completed_Shrimp_breastmilk.metabolite + "(e)"
completed_Tuna_breastmilk = pd.merge(added_df_Tuna_breastmilk, annotations, on="metabolite", how="left")
completed_Tuna_breastmilk["reaction"] = "EX_" + completed_Tuna_breastmilk.metabolite + "_m"
completed_Tuna_breastmilk["global_id"] = "EX_" + completed_Tuna_breastmilk.metabolite + "(e)"
completed_Turkey_breastmilk = pd.merge(added_df_Turkey_breastmilk, annotations, on="metabolite", how="left")
completed_Turkey_breastmilk["reaction"] = "EX_" + completed_Turkey_breastmilk.metabolite + "_m"
completed_Turkey_breastmilk["global_id"] = "EX_" + completed_Turkey_breastmilk.metabolite + "(e)"
completed_Almond_breastmilk = pd.merge(added_df_Almond_breastmilk, annotations, on="metabolite", how="left")
completed_Almond_breastmilk["reaction"] = "EX_" + completed_Almond_breastmilk.metabolite + "_m"
completed_Almond_breastmilk["global_id"] = "EX_" + completed_Almond_breastmilk.metabolite + "(e)"
completed_Black_beans_breastmilk = pd.merge(added_df_Black_beans_breastmilk, annotations, on="metabolite", how="left")
completed_Black_beans_breastmilk["reaction"] = "EX_" + completed_Black_beans_breastmilk.metabolite + "_m"
completed_Black_beans_breastmilk["global_id"] = "EX_" + completed_Black_beans_breastmilk.metabolite + "(e)"
completed_Cashew_breastmilk = pd.merge(added_df_Cashew_breastmilk, annotations, on="metabolite", how="left")
completed_Cashew_breastmilk["reaction"] = "EX_" + completed_Cashew_breastmilk.metabolite + "_m"
completed_Cashew_breastmilk["global_id"] = "EX_" + completed_Cashew_breastmilk.metabolite + "(e)"
completed_Chia_breastmilk = pd.merge(added_df_Chia_breastmilk, annotations, on="metabolite", how="left")
completed_Chia_breastmilk["reaction"] = "EX_" + completed_Chia_breastmilk.metabolite + "_m"
completed_Chia_breastmilk["global_id"] = "EX_" + completed_Chia_breastmilk.metabolite + "(e)"
completed_Chickpea_breastmilk = pd.merge(added_df_Chickpea_breastmilk, annotations, on="metabolite", how="left")
completed_Chickpea_breastmilk["reaction"] = "EX_" + completed_Chickpea_breastmilk.metabolite + "_m"
completed_Chickpea_breastmilk["global_id"] = "EX_" + completed_Chickpea_breastmilk.metabolite + "(e)"
completed_Green_peas_breastmilk = pd.merge(added_df_Green_peas_breastmilk, annotations, on="metabolite", how="left")
completed_Green_peas_breastmilk["reaction"] = "EX_" + completed_Green_peas_breastmilk.metabolite + "_m"
completed_Green_peas_breastmilk["global_id"] = "EX_" + completed_Green_peas_breastmilk.metabolite + "(e)"
completed_Hazelnut_breastmilk = pd.merge(added_df_Hazelnut_breastmilk, annotations, on="metabolite", how="left")
completed_Hazelnut_breastmilk["reaction"] = "EX_" + completed_Hazelnut_breastmilk.metabolite + "_m"
completed_Hazelnut_breastmilk["global_id"] = "EX_" + completed_Hazelnut_breastmilk.metabolite + "(e)"
completed_Lentils_breastmilk = pd.merge(added_df_Lentils_breastmilk, annotations, on="metabolite", how="left")
completed_Lentils_breastmilk["reaction"] = "EX_" + completed_Lentils_breastmilk.metabolite + "_m"
completed_Lentils_breastmilk["global_id"] = "EX_" + completed_Lentils_breastmilk.metabolite + "(e)"
completed_Peanut_breastmilk = pd.merge(added_df_Peanut_breastmilk, annotations, on="metabolite", how="left")
completed_Peanut_breastmilk["reaction"] = "EX_" + completed_Peanut_breastmilk.metabolite + "_m"
completed_Peanut_breastmilk["global_id"] = "EX_" + completed_Peanut_breastmilk.metabolite + "(e)"
completed_Pecans_breastmilk = pd.merge(added_df_Pecans_breastmilk, annotations, on="metabolite", how="left")
completed_Pecans_breastmilk["reaction"] = "EX_" + completed_Pecans_breastmilk.metabolite + "_m"
completed_Pecans_breastmilk["global_id"] = "EX_" + completed_Pecans_breastmilk.metabolite + "(e)"
completed_Pumpkin_seed_breastmilk = pd.merge(added_df_Pumpkin_seed_breastmilk, annotations, on="metabolite", how="left")
completed_Pumpkin_seed_breastmilk["reaction"] = "EX_" + completed_Pumpkin_seed_breastmilk.metabolite + "_m"
completed_Pumpkin_seed_breastmilk["global_id"] = "EX_" + completed_Pumpkin_seed_breastmilk.metabolite + "(e)"
completed_Red_beans_breastmilk = pd.merge(added_df_Red_beans_breastmilk, annotations, on="metabolite", how="left")
completed_Red_beans_breastmilk["reaction"] = "EX_" + completed_Red_beans_breastmilk.metabolite + "_m"
completed_Red_beans_breastmilk["global_id"] = "EX_" + completed_Red_beans_breastmilk.metabolite + "(e)"
completed_Soybean_breastmilk = pd.merge(added_df_Soybean_breastmilk, annotations, on="metabolite", how="left")
completed_Soybean_breastmilk["reaction"] = "EX_" + completed_Soybean_breastmilk.metabolite + "_m"
completed_Soybean_breastmilk["global_id"] = "EX_" + completed_Soybean_breastmilk.metabolite + "(e)"
completed_Split_peas_breastmilk = pd.merge(added_df_Split_peas_breastmilk, annotations, on="metabolite", how="left")
completed_Split_peas_breastmilk["reaction"] = "EX_" + completed_Split_peas_breastmilk.metabolite + "_m"
completed_Split_peas_breastmilk["global_id"] = "EX_" + completed_Split_peas_breastmilk.metabolite + "(e)"
completed_Sunflower_seed_breastmilk = pd.merge(added_df_Sunflower_seed_breastmilk, annotations, on="metabolite", how="left")
completed_Sunflower_seed_breastmilk["reaction"] = "EX_" + completed_Sunflower_seed_breastmilk.metabolite + "_m"
completed_Sunflower_seed_breastmilk["global_id"] = "EX_" + completed_Sunflower_seed_breastmilk.metabolite + "(e)"
completed_White_beans_breastmilk = pd.merge(added_df_White_beans_breastmilk, annotations, on="metabolite", how="left")
completed_White_beans_breastmilk["reaction"] = "EX_" + completed_White_beans_breastmilk.metabolite + "_m"
completed_White_beans_breastmilk["global_id"] = "EX_" + completed_White_beans_breastmilk.metabolite + "(e)"

#Saving the medium
completed_Broccoli_breastmilk.to_csv("media/Broccoli_breastmilk.csv") 
completed_Brussel_breastmilk.to_csv("media/Brussel_breastmilk.csv") 
completed_Cabbage_breastmilk.to_csv("media/Cabbage_breastmilk.csv") 
completed_Carrot_breastmilk.to_csv("media/Carrot_breastmilk.csv") 
completed_Cauliflower_breastmilk.to_csv("media/Cauliflower_breastmilk.csv") 
completed_Celery_breastmilk.to_csv("media/Celery_breastmilk.csv") 
completed_Cucumber_breastmilk.to_csv("media/Cucumber_breastmilk.csv") 
completed_Eggplant_breastmilk.to_csv("media/Eggplant_breastmilk.csv") 
completed_Green_beans_breastmilk.to_csv("media/Green_beans_breastmilk.csv") 
completed_Green_capsicum_breastmilk.to_csv("media/Green_capsicum_breastmilk.csv") 
completed_Lettuce_breastmilk.to_csv("media/Lettuce_breastmilk.csv") 
completed_Mushroom_breastmilk.to_csv("media/Mushroom_breastmilk.csv") 
completed_Onion_breastmilk.to_csv("media/Onion_breastmilk.csv") 
completed_Pak_choi_breastmilk.to_csv("media/Pak_choi_breastmilk.csv") 
completed_Potato_breastmilk.to_csv("media/Potato_breastmilk.csv") 
completed_Pumpkin_breastmilk.to_csv("media/Pumpkin_breastmilk.csv") 
completed_Sweetcorn_breastmilk.to_csv("media/Sweetcorn_breastmilk.csv") 
completed_Spinach_breastmilk.to_csv("media/Spinach_breastmilk.csv") 
completed_Squash_breastmilk.to_csv("media/Squash_breastmilk.csv") 
completed_Sweet_potato_breastmilk.to_csv("media/Sweet_potato_breastmilk.csv") 
completed_Tomato_breastmilk.to_csv("media/Tomato_breastmilk.csv") 
completed_Yam_breastmilk.to_csv("media/Yam_breastmilk.csv") 
completed_Zucchini_breastmilk.to_csv("media/Zucchini_breastmilk.csv") 
completed_Apple_breastmilk.to_csv("media/Apple_breastmilk.csv") 
completed_Banana_breastmilk.to_csv("media/Banana_breastmilk.csv") 
completed_Blackcurrant_breastmilk.to_csv("media/Blackcurrant_breastmilk.csv") 
completed_Blueberries_breastmilk.to_csv("media/Blueberries_breastmilk.csv") 
completed_Cherry_breastmilk.to_csv("media/Cherry_breastmilk.csv") 
completed_Feijoa_breastmilk.to_csv("media/Feijoa_breastmilk.csv") 
completed_Gold_kiwifruit_breastmilk.to_csv("media/Gold_kiwifruit_breastmilk.csv") 
completed_Grape_breastmilk.to_csv("media/Grape_breastmilk.csv") 
completed_Grapefruit_breastmilk.to_csv("media/Grapefruit_breastmilk.csv") 
completed_Green_kiwifruit_breastmilk.to_csv("media/Green_kiwifruit_breastmilk.csv") 
completed_Mandarin_breastmilk.to_csv("media/Mandarin_breastmilk.csv") 
completed_Mango_breastmilk.to_csv("media/Mango_breastmilk.csv") 
completed_Melon_breastmilk.to_csv("media/Melon_breastmilk.csv") 
completed_Nectarine_breastmilk.to_csv("media/Nectarine_breastmilk.csv") 
completed_Orange_breastmilk.to_csv("media/Orange_breastmilk.csv") 
completed_Peache_breastmilk.to_csv("media/Peache_breastmilk.csv") 
completed_Pear_breastmilk.to_csv("media/Pear_breastmilk.csv") 
completed_Pineapple_breastmilk.to_csv("media/Pineapple_breastmilk.csv") 
completed_Plum_breastmilk.to_csv("media/Plum_breastmilk.csv") 
completed_Raspberries_breastmilk.to_csv("media/Raspberries_breastmilk.csv") 
completed_Strawberries_breastmilk.to_csv("media/Strawberries_breastmilk.csv") 
completed_Barley_breastmilk.to_csv("media/Barley_breastmilk.csv") 
completed_Barley_cereal_breastmilk.to_csv("media/Barley_cereal_breastmilk.csv") 
completed_Couscous_breastmilk.to_csv("media/Couscous_breastmilk.csv") 
completed_Noodles_breastmilk.to_csv("media/Noodles_breastmilk.csv") 
completed_Oat_cereal_breastmilk.to_csv("media/Oat_cereal_breastmilk.csv") 
completed_Pasta_breastmilk.to_csv("media/Pasta_breastmilk.csv") 
completed_Rice_breastmilk.to_csv("media/Rice_breastmilk.csv") 
completed_Rice_cereal_breastmilk.to_csv("media/Rice_cereal_breastmilk.csv") 
completed_Tapioca_pudding_breastmilk.to_csv("media/Tapioca_pudding_breastmilk.csv") 
completed_White_bread_breastmilk.to_csv("media/White_bread_breastmilk.csv") 
completed_Wholegrain_bread_breastmilk.to_csv("media/Wholegrain_bread_breastmilk.csv") 
completed_Cottage_cheese_breastmilk.to_csv("media/Cottage_cheese_breastmilk.csv") 
completed_Eggs_breastmilk.to_csv("media/Eggs_breastmilk.csv") 
completed_Mozzarella_cheese_breastmilk.to_csv("media/Mozzarella_cheese_breastmilk.csv") 
completed_Soymilk_breastmilk.to_csv("media/Soymilk_breastmilk.csv") 
completed_Tofu_breastmilk.to_csv("media/Tofu_breastmilk.csv")
completed_Whole_milk_breastmilk.to_csv("media/Whole_milk_breastmilk.csv") 
completed_Yoghurt_breastmilk.to_csv("media/Yoghurt_breastmilk.csv") 
completed_Beef_breastmilk.to_csv("media/Beef_breastmilk.csv") 
completed_Chicken_breastmilk.to_csv("media/Chicken_breastmilk.csv") 
completed_Codfish_breastmilk.to_csv("media/Codfish_breastmilk.csv") 
completed_Lamb_breastmilk.to_csv("media/Lamb_breastmilk.csv") 
completed_Mackerel_breastmilk.to_csv("media/Mackerel_breastmilk.csv") 
completed_Mussels_breastmilk.to_csv("media/Mussels_breastmilk.csv") 
completed_Pork_breastmilk.to_csv("media/Pork_breastmilk.csv") 
completed_Salmon_breastmilk.to_csv("media/Salmon_breastmilk.csv") 
completed_Shrimp_breastmilk.to_csv("media/Shrimp_breastmilk.csv") 
completed_Tuna_breastmilk.to_csv("media/Tuna_breastmilk.csv") 
completed_Turkey_breastmilk.to_csv("media/Turkey_breastmilk.csv") 
completed_Almond_breastmilk.to_csv("media/Almond_breastmilk.csv") 
completed_Black_beans_breastmilk.to_csv("media/Black_beans_breastmilk.csv") 
completed_Cashew_breastmilk.to_csv("media/Cashew_breastmilk.csv") 
completed_Chia_breastmilk.to_csv("media/Chia_breastmilk.csv") 
completed_Chickpea_breastmilk.to_csv("media/Chickpea_breastmilk.csv") 
completed_Green_peas_breastmilk.to_csv("media/Green_peas_breastmilk.csv") 
completed_Hazelnut_breastmilk.to_csv("media/Hazelnut_breastmilk.csv")  
completed_Lentils_breastmilk.to_csv("media/Lentils_breastmilk.csv") 
completed_Peanut_breastmilk.to_csv("media/Peanut_breastmilk.csv") 
completed_Pecans_breastmilk.to_csv("media/Pecans_breastmilk.csv") 
completed_Pumpkin_seed_breastmilk.to_csv("media/Pumpkin_seed_breastmilk.csv") 
completed_Red_beans_breastmilk.to_csv("media/Red_beans_breastmilk.csv") 
completed_Soybean_breastmilk.to_csv("media/Soybean_breastmilk.csv") 
completed_Split_peas_breastmilk.to_csv("media/Split_peas_breastmilk.csv") 
completed_Sunflower_seed_breastmilk.to_csv("media/Sunflower_seed_breastmilk.csv") 
completed_White_beans_breastmilk.to_csv("media/White_beans_breastmilk.csv") 

#importing medium
import pandas as pd

completed_Broccoli_breastmilk = pd.read_csv("media/Broccoli_breastmilk.csv") 
completed_Brussel_breastmilk = pd.read_csv("media/Brussel_breastmilk.csv") 
completed_Cabbage_breastmilk = pd.read_csv("media/Cabbage_breastmilk.csv") 
completed_Carrot_breastmilk = pd.read_csv("media/Carrot_breastmilk.csv") 
completed_Cauliflower_breastmilk = pd.read_csv("media/Cauliflower_breastmilk.csv") 
completed_Celery_breastmilk = pd.read_csv("media/Celery_breastmilk.csv") 
completed_Cucumber_breastmilk = pd.read_csv("media/Cucumber_breastmilk.csv") 
completed_Eggplant_breastmilk = pd.read_csv("media/Eggplant_breastmilk.csv") 
completed_Green_beans_breastmilk = pd.read_csv("media/Green_beans_breastmilk.csv") 
completed_Green_capsicum_breastmilk = pd.read_csv("media/Green_capsicum_breastmilk.csv") 
completed_Lettuce_breastmilk = pd.read_csv("media/Lettuce_breastmilk.csv") 
completed_Mushroom_breastmilk = pd.read_csv("media/Mushroom_breastmilk.csv") 
completed_Onion_breastmilk = pd.read_csv("media/Onion_breastmilk.csv") 
completed_Pak_choi_breastmilk = pd.read_csv("media/Pak_choi_breastmilk.csv") 
completed_Potato_breastmilk = pd.read_csv("media/Potato_breastmilk.csv") 
completed_Pumpkin_breastmilk = pd.read_csv("media/Pumpkin_breastmilk.csv") 
completed_Sweetcorn_breastmilk = pd.read_csv("media/Sweetcorn_breastmilk.csv") 
completed_Spinach_breastmilk = pd.read_csv("media/Spinach_breastmilk.csv") 
completed_Squash_breastmilk = pd.read_csv("media/Squash_breastmilk.csv") 
completed_Sweet_potato_breastmilk = pd.read_csv("media/Sweet_potato_breastmilk.csv") 
completed_Tomato_breastmilk = pd.read_csv("media/Tomato_breastmilk.csv") 
completed_Yam_breastmilk = pd.read_csv("media/Yam_breastmilk.csv") 
completed_Zucchini_breastmilk = pd.read_csv("media/Zucchini_breastmilk.csv") 
completed_Apple_breastmilk = pd.read_csv("media/Apple_breastmilk.csv") 
completed_Banana_breastmilk = pd.read_csv("media/Banana_breastmilk.csv") 
completed_Blackcurrant_breastmilk = pd.read_csv("media/Blackcurrant_breastmilk.csv") 
completed_Blueberries_breastmilk = pd.read_csv("media/Blueberries_breastmilk.csv") 
completed_Cherry_breastmilk = pd.read_csv("media/Cherry_breastmilk.csv") 
completed_Feijoa_breastmilk = pd.read_csv("media/Feijoa_breastmilk.csv") 
completed_Gold_kiwifruit_breastmilk = pd.read_csv("media/Gold_kiwifruit_breastmilk.csv") 
completed_Grape_breastmilk = pd.read_csv("media/Grape_breastmilk.csv") 
completed_Grapefruit_breastmilk = pd.read_csv("media/Grapefruit_breastmilk.csv") 
completed_Green_kiwifruit_breastmilk = pd.read_csv("media/Green_kiwifruit_breastmilk.csv") 
completed_Mandarin_breastmilk = pd.read_csv("media/Mandarin_breastmilk.csv") 
completed_Mango_breastmilk = pd.read_csv("media/Mango_breastmilk.csv") 
completed_Melon_breastmilk = pd.read_csv("media/Melon_breastmilk.csv") 
completed_Nectarine_breastmilk = pd.read_csv("media/Nectarine_breastmilk.csv") 
completed_Orange_breastmilk = pd.read_csv("media/Orange_breastmilk.csv") 
completed_Peache_breastmilk = pd.read_csv("media/Peache_breastmilk.csv") 
completed_Pear_breastmilk = pd.read_csv("media/Pear_breastmilk.csv") 
completed_Pineapple_breastmilk = pd.read_csv("media/Pineapple_breastmilk.csv") 
completed_Plum_breastmilk = pd.read_csv("media/Plum_breastmilk.csv") 
completed_Raspberries_breastmilk = pd.read_csv("media/Raspberries_breastmilk.csv") 
completed_Strawberries_breastmilk = pd.read_csv("media/Strawberries_breastmilk.csv") 
completed_Barley_breastmilk = pd.read_csv("media/Barley_breastmilk.csv") 
completed_Barley_cereal_breastmilk = pd.read_csv("media/Barley_cereal_breastmilk.csv") 
completed_Couscous_breastmilk = pd.read_csv("media/Couscous_breastmilk.csv") 
completed_Noodles_breastmilk = pd.read_csv("media/Noodles_breastmilk.csv") 
completed_Oat_cereal_breastmilk = pd.read_csv("media/Oat_cereal_breastmilk.csv") 
completed_Pasta_breastmilk = pd.read_csv("media/Pasta_breastmilk.csv") 
completed_Rice_breastmilk = pd.read_csv("media/Rice_breastmilk.csv") 
completed_Rice_cereal_breastmilk = pd.read_csv("media/Rice_cereal_breastmilk.csv") 
completed_Tapioca_pudding_breastmilk = pd.read_csv("media/Tapioca_pudding_breastmilk.csv") 
completed_White_bread_breastmilk = pd.read_csv("media/White_bread_breastmilk.csv") 
completed_Wholegrain_bread_breastmilk = pd.read_csv("media/Wholegrain_bread_breastmilk.csv") 
completed_Cottage_cheese_breastmilk = pd.read_csv("media/Cottage_cheese_breastmilk.csv") 
completed_Eggs_breastmilk = pd.read_csv("media/Eggs_breastmilk.csv") 
completed_Mozzarella_cheese_breastmilk = pd.read_csv("media/Mozzarella_cheese_breastmilk.csv") 
completed_Soymilk_breastmilk = pd.read_csv("media/Soymilk_breastmilk.csv") 
completed_Tofu_breastmilk = pd.read_csv("media/Tofu_breastmilk.csv")
completed_Whole_milk_breastmilk = pd.read_csv("media/Whole_milk_breastmilk.csv") 
completed_Yoghurt_breastmilk = pd.read_csv("media/Yoghurt_breastmilk.csv") 
completed_Beef_breastmilk = pd.read_csv("media/Beef_breastmilk.csv") 
completed_Chicken_breastmilk = pd.read_csv("media/Chicken_breastmilk.csv") 
completed_Codfish_breastmilk = pd.read_csv("media/Codfish_breastmilk.csv") 
completed_Lamb_breastmilk = pd.read_csv("media/Lamb_breastmilk.csv") 
completed_Mackerel_breastmilk = pd.read_csv("media/Mackerel_breastmilk.csv") 
completed_Mussels_breastmilk = pd.read_csv("media/Mussels_breastmilk.csv") 
completed_Pork_breastmilk = pd.read_csv("media/Pork_breastmilk.csv") 
completed_Salmon_breastmilk = pd.read_csv("media/Salmon_breastmilk.csv") 
completed_Shrimp_breastmilk = pd.read_csv("media/Shrimp_breastmilk.csv") 
completed_Tuna_breastmilk = pd.read_csv("media/Tuna_breastmilk.csv") 
completed_Turkey_breastmilk = pd.read_csv("media/Turkey_breastmilk.csv") 
completed_Almond_breastmilk = pd.read_csv("media/Almond_breastmilk.csv") 
completed_Black_beans_breastmilk = pd.read_csv("media/Black_beans_breastmilk.csv") 
completed_Cashew_breastmilk = pd.read_csv("media/Cashew_breastmilk.csv") 
completed_Chia_breastmilk = pd.read_csv("media/Chia_breastmilk.csv") 
completed_Chickpea_breastmilk = pd.read_csv("media/Chickpea_breastmilk.csv") 
completed_Green_peas_breastmilk = pd.read_csv("media/Green_peas_breastmilk.csv") 
completed_Hazelnut_breastmilk = pd.read_csv("media/Hazelnut_breastmilk.csv")  
completed_Lentils_breastmilk = pd.read_csv("media/Lentils_breastmilk.csv") 
completed_Peanut_breastmilk = pd.read_csv("media/Peanut_breastmilk.csv") 
completed_Pecans_breastmilk = pd.read_csv("media/Pecans_breastmilk.csv") 
completed_Pumpkin_seed_breastmilk = pd.read_csv("media/Pumpkin_seed_breastmilk.csv") 
completed_Red_beans_breastmilk = pd.read_csv("media/Red_beans_breastmilk.csv") 
completed_Soybean_breastmilk = pd.read_csv("media/Soybean_breastmilk.csv") 
completed_Split_peas_breastmilk = pd.read_csv("media/Split_peas_breastmilk.csv") 
completed_Sunflower_seed_breastmilk = pd.read_csv("media/Sunflower_seed_breastmilk.csv") 
completed_White_beans_breastmilk = pd.read_csv("media/White_beans_breastmilk.csv") 

#Checking the medium
from micom.workflows.db_media import check_db_medium

check_Broccoli_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Broccoli_breastmilk, threads=14)
check_Brussel_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Brussel_breastmilk, threads=14)
check_Cabbage_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Cabbage_breastmilk, threads=14)
check_Carrot_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Carrot_breastmilk, threads=14)
check_Cauliflower_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Cauliflower_breastmilk, threads=14)
check_Celery_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Celery_breastmilk, threads=14)
check_Cucumber_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Cucumber_breastmilk, threads=14)
check_Eggplant_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Eggplant_breastmilk, threads=14)
check_Green_beans_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Green_beans_breastmilk, threads=14)
check_Green_capsicum_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Green_capsicum_breastmilk, threads=14)
check_Lettuce_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Lettuce_breastmilk, threads=14)
check_Mushroom_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Mushroom_breastmilk, threads=14)
check_Onion_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Onion_breastmilk, threads=14)
check_Pak_choi_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Pak_choi_breastmilk, threads=14)
check_Potato_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Potato_breastmilk, threads=14)
check_Pumpkin_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Pumpkin_breastmilk, threads=14)
check_Sweetcorn_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Sweetcorn_breastmilk, threads=14)
check_Spinach_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Spinach_breastmilk, threads=14)
check_Squash_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Squash_breastmilk, threads=14)
check_Sweet_potato_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Sweet_potato_breastmilk, threads=14)
check_Tomato_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Tomato_breastmilk, threads=14)
check_Yam_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Yam_breastmilk, threads=14)
check_Zucchini_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Zucchini_breastmilk, threads=14)
check_Apple_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Apple_breastmilk, threads=14)
check_Banana_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Banana_breastmilk, threads=14)
check_Blackcurrant_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Blackcurrant_breastmilk, threads=14)
check_Blueberries_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Blueberries_breastmilk, threads=14)
check_Cherry_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Cherry_breastmilk, threads=14)
check_Feijoa_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Feijoa_breastmilk, threads=14)
check_Gold_kiwifruit_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Gold_kiwifruit_breastmilk, threads=14)
check_Grape_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Grape_breastmilk, threads=14)
check_Grapefruit_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Grapefruit_breastmilk, threads=14)
check_Green_kiwifruit_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Green_kiwifruit_breastmilk, threads=14)
check_Mandarin_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Mandarin_breastmilk, threads=14)
check_Mango_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Mango_breastmilk, threads=14)
check_Melon_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Melon_breastmilk, threads=14)
check_Nectarine_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Nectarine_breastmilk, threads=14)
check_Orange_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Orange_breastmilk, threads=14)
check_Peache_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Peache_breastmilk, threads=14)
check_Pear_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Pear_breastmilk, threads=14)
check_Pineapple_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Pineapple_breastmilk, threads=14)
check_Plum_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Plum_breastmilk, threads=14)
check_Raspberries_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Raspberries_breastmilk, threads=14)
check_Strawberries_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Strawberries_breastmilk, threads=14)
check_Barley_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Barley_breastmilk, threads=14)
check_Barley_cereal_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Barley_cereal_breastmilk, threads=14)
check_Couscous_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Couscous_breastmilk, threads=14)
check_Noodles_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Noodles_breastmilk, threads=14)
check_Oat_cereal_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Oat_cereal_breastmilk, threads=14)
check_Pasta_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Pasta_breastmilk, threads=14)
check_Rice_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Rice_breastmilk, threads=14)
check_Rice_cereal_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Rice_cereal_breastmilk, threads=14)
check_Tapioca_pudding_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Tapioca_pudding_breastmilk, threads=14)
check_White_bread_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_White_bread_breastmilk, threads=14)
check_Wholegrain_bread_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Wholegrain_bread_breastmilk, threads=14)
check_Cottage_cheese_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Cottage_cheese_breastmilk, threads=14)
check_Eggs_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Eggs_breastmilk, threads=14)
check_Mozzarella_cheese_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Mozzarella_cheese_breastmilk, threads=14)
check_Soymilk_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Soymilk_breastmilk, threads=14)
check_Tofu_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Tofu_breastmilk, threads=14)
check_Whole_milk_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Whole_milk_breastmilk, threads=14)
check_Yoghurt_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Yoghurt_breastmilk, threads=14)
check_Beef_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Beef_breastmilk, threads=14)
check_Chicken_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Chicken_breastmilk, threads=14)
check_Codfish_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Codfish_breastmilk, threads=14)
check_Lamb_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Lamb_breastmilk, threads=14)
check_Mackerel_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Mackerel_breastmilk, threads=14)
check_Mussels_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Mussels_breastmilk, threads=14)
check_Pork_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Pork_breastmilk, threads=14)
check_Salmon_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Salmon_breastmilk, threads=14)
check_Shrimp_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Shrimp_breastmilk, threads=14)
check_Tuna_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Tuna_breastmilk, threads=14)
check_Turkey_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Turkey_breastmilk, threads=14)
check_Almond_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Almond_breastmilk, threads=14)
check_Black_beans_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Black_beans_breastmilk, threads=14)
check_Cashew_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Cashew_breastmilk, threads=14)
check_Chia_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Chia_breastmilk, threads=14)
check_Chickpea_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Chickpea_breastmilk, threads=14)
check_Green_peas_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Green_peas_breastmilk, threads=14)
check_Hazelnut_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Hazelnut_breastmilk, threads=14)
check_Lentils_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Lentils_breastmilk, threads=14)
check_Peanut_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Peanut_breastmilk, threads=14)
check_Pecans_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Pecans_breastmilk, threads=14)
check_Pumpkin_seed_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Pumpkin_seed_breastmilk, threads=14)
check_Red_beans_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Red_beans_breastmilk, threads=14)
check_Soybean_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Soybean_breastmilk, threads=14)
check_Split_peas_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Split_peas_breastmilk, threads=14)
check_Sunflower_seed_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_Sunflower_seed_breastmilk, threads=14)
check_White_beans_breastmilk = check_db_medium("data/agora201__species.qza", medium=completed_White_beans_breastmilk, threads=14)

check_Broccoli_breastmilk.growth_rate.describe()
check_Brussel_breastmilk.growth_rate.describe()
check_Cabbage_breastmilk.growth_rate.describe()
check_Carrot_breastmilk.growth_rate.describe()
check_Cauliflower_breastmilk.growth_rate.describe()
check_Celery_breastmilk.growth_rate.describe()
check_Cucumber_breastmilk.growth_rate.describe()
check_Eggplant_breastmilk.growth_rate.describe()
check_Green_beans_breastmilk.growth_rate.describe()
check_Green_capsicum_breastmilk.growth_rate.describe()
check_Lettuce_breastmilk.growth_rate.describe()
check_Mushroom_breastmilk.growth_rate.describe()
check_Onion_breastmilk.growth_rate.describe()
check_Pak_choi_breastmilk.growth_rate.describe()
check_Potato_breastmilk.growth_rate.describe()
check_Pumpkin_breastmilk.growth_rate.describe()
check_Sweetcorn_breastmilk.growth_rate.describe()
check_Spinach_breastmilk.growth_rate.describe()
check_Squash_breastmilk.growth_rate.describe()
check_Sweet_potato_breastmilk.growth_rate.describe()
check_Tomato_breastmilk.growth_rate.describe()
check_Yam_breastmilk.growth_rate.describe()
check_Zucchini_breastmilk.growth_rate.describe()
check_Apple_breastmilk.growth_rate.describe()
check_Banana_breastmilk.growth_rate.describe()
check_Blackcurrant_breastmilk.growth_rate.describe()
check_Blueberries_breastmilk.growth_rate.describe()
check_Cherry_breastmilk.growth_rate.describe()
check_Feijoa_breastmilk.growth_rate.describe()
check_Gold_kiwifruit_breastmilk.growth_rate.describe()
check_Grape_breastmilk.growth_rate.describe()
check_Grapefruit_breastmilk.growth_rate.describe()
check_Green_kiwifruit_breastmilk.growth_rate.describe()
check_Mandarin_breastmilk.growth_rate.describe()
check_Mango_breastmilk.growth_rate.describe()
check_Melon_breastmilk.growth_rate.describe()
check_Nectarine_breastmilk.growth_rate.describe()
check_Orange_breastmilk.growth_rate.describe()
check_Peache_breastmilk.growth_rate.describe()
check_Pear_breastmilk.growth_rate.describe()
check_Pineapple_breastmilk.growth_rate.describe()
check_Plum_breastmilk.growth_rate.describe()
check_Raspberries_breastmilk.growth_rate.describe()
check_Strawberries_breastmilk.growth_rate.describe()
check_Barley_breastmilk.growth_rate.describe()
check_Barley_cereal_breastmilk.growth_rate.describe()
check_Couscous_breastmilk.growth_rate.describe()
check_Noodles_breastmilk.growth_rate.describe()
check_Oat_cereal_breastmilk.growth_rate.describe()
check_Pasta_breastmilk.growth_rate.describe()
check_Rice_breastmilk.growth_rate.describe()
check_Rice_cereal_breastmilk.growth_rate.describe()
check_Tapioca_pudding_breastmilk.growth_rate.describe()
check_White_bread_breastmilk.growth_rate.describe()
check_Wholegrain_bread_breastmilk.growth_rate.describe()
check_Cottage_cheese_breastmilk.growth_rate.describe()
check_Eggs_breastmilk.growth_rate.describe()
check_Mozzarella_cheese_breastmilk.growth_rate.describe()
check_Soymilk_breastmilk.growth_rate.describe()
check_Tofu_breastmilk.growth_rate.describe()
check_Whole_milk_breastmilk.growth_rate.describe()
check_Yoghurt_breastmilk.growth_rate.describe()
check_Beef_breastmilk.growth_rate.describe()
check_Chicken_breastmilk.growth_rate.describe()
check_Codfish_breastmilk.growth_rate.describe()
check_Lamb_breastmilk.growth_rate.describe()
check_Mackerel_breastmilk.growth_rate.describe()
check_Mussels_breastmilk.growth_rate.describe()
check_Pork_breastmilk.growth_rate.describe()
check_Salmon_breastmilk.growth_rate.describe()
check_Shrimp_breastmilk.growth_rate.describe()
check_Tuna_breastmilk.growth_rate.describe()
check_Turkey_breastmilk.growth_rate.describe()
check_Almond_breastmilk.growth_rate.describe()
check_Black_beans_breastmilk.growth_rate.describe()
check_Cashew_breastmilk.growth_rate.describe()
check_Chia_breastmilk.growth_rate.describe()
check_Chickpea_breastmilk.growth_rate.describe()
check_Green_peas_breastmilk.growth_rate.describe()
check_Hazelnut_breastmilk.growth_rate.describe()
check_Lentils_breastmilk.growth_rate.describe()
check_Peanut_breastmilk.growth_rate.describe()
check_Pecans_breastmilk.growth_rate.describe()
check_Pumpkin_seed_breastmilk.growth_rate.describe()
check_Red_beans_breastmilk.growth_rate.describe()
check_Soybean_breastmilk.growth_rate.describe()
check_Split_peas_breastmilk.growth_rate.describe()
check_Sunflower_seed_breastmilk.growth_rate.describe()
check_White_beans_breastmilk.growth_rate.describe()
