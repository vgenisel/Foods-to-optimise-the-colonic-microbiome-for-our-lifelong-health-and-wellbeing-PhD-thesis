##Simulating NZ food-breastmilk combinations on the microbiome of weaning infants
#Food-breastlmik ratio (15/85%) designed for infants at 6 months (608 kcal/day)
#Daily fluxes, CPLEX 22.1, AGORA2, genus
#89 NZ single food combinations + 2 controls (only breastmilk and only infant formula)

#27/07/23

#Importing taxnomic data
import pandas as pd
tax = pd.read_csv('data/Taxa_genus_parkar_greegenes2.csv') 

#Building models using AGORA2 reconstructions
from micom.workflows import build
import pandas as pd
manifest = build(tax, model_db="data/agora201_genus_1.qza", out_folder="models_cplex", solver="cplex", cutoff=0.01, threads=14) #keeping taxa with at least 1% relative abundance
manifest #to check the fraction of the taxa that matches the AGORA2 database

##Defining the diets
import pandas as pd

Broccoli_breastmilk = pd.read_csv('data/Broccoli_breastmilk.csv')
Brussel_breastmilk = pd.read_csv('data/Brussel_breastmilk.csv')
Cabbage_breastmilk = pd.read_csv('data/Cabbage_breastmilk.csv')
Carrot_breastmilk = pd.read_csv('data/Carrot_breastmilk.csv')
Cauliflower_breastmilk = pd.read_csv('data/Cauliflower_breastmilk.csv')
Celery_breastmilk = pd.read_csv('data/Celery_breastmilk.csv')
Eggplant_breastmilk = pd.read_csv('data/Eggplant_breastmilk.csv')
Green_beans_breastmilk = pd.read_csv('data/Green_beans_breastmilk.csv')
Green_capsicum_breastmilk = pd.read_csv('data/Green_capsicum_breastmilk.csv')
Lettuce_breastmilk = pd.read_csv('data/Lettuce_breastmilk.csv')
Mushroom_breastmilk = pd.read_csv('data/Mushroom_breastmilk.csv')
Onion_breastmilk = pd.read_csv('data/Onion_breastmilk.csv')
Pak_choi_breastmilk = pd.read_csv('data/Pak_choi_breastmilk.csv')
Potato_breastmilk = pd.read_csv('data/Potato_breastmilk.csv')
Sweetcorn_breastmilk = pd.read_csv('data/Sweetcorn_breastmilk.csv')
Spinach_breastmilk = pd.read_csv('data/Spinach_breastmilk.csv')
Squash_breastmilk = pd.read_csv('data/Squash_breastmilk.csv')
Sweet_potato_breastmilk = pd.read_csv('data/Sweet_potato_breastmilk.csv')
Tomato_breastmilk = pd.read_csv('data/Tomato_breastmilk.csv')
Yam_breastmilk = pd.read_csv('data/Yam_breastmilk.csv')
Apple_breastmilk = pd.read_csv('data/Apple_breastmilk.csv')
Banana_breastmilk = pd.read_csv('data/Banana_breastmilk.csv')
Blackcurrant_breastmilk = pd.read_csv('data/Blackcurrant_breastmilk.csv')
Blueberries_breastmilk = pd.read_csv('data/Blueberries_breastmilk.csv')
Cherry_breastmilk = pd.read_csv('data/Cherry_breastmilk.csv')
Feijoa_breastmilk = pd.read_csv('data/Feijoa_breastmilk.csv')
Gold_kiwifruit_breastmilk = pd.read_csv('data/Gold_kiwifruit_breastmilk.csv')
Grapefruit_breastmilk = pd.read_csv('data/Grapefruit_breastmilk.csv')
Green_kiwifruit_breastmilk = pd.read_csv('data/Green_kiwifruit_breastmilk.csv')
Mandarin_breastmilk = pd.read_csv('data/Mandarin_breastmilk.csv')
Mango_breastmilk = pd.read_csv('data/Mango_breastmilk.csv')
Melon_breastmilk = pd.read_csv('data/Melon_breastmilk.csv')
Nectarine_breastmilk = pd.read_csv('data/Nectarine_breastmilk.csv')
Orange_breastmilk = pd.read_csv('data/Orange_breastmilk.csv')
Pear_breastmilk = pd.read_csv('data/Pear_breastmilk.csv')
Pineapple_breastmilk = pd.read_csv('data/Pineapple_breastmilk.csv')
Plum_breastmilk = pd.read_csv('data/Plum_breastmilk.csv')
Raspberries_breastmilk = pd.read_csv('data/Raspberries_breastmilk.csv')
Strawberries_breastmilk = pd.read_csv('data/Strawberries_breastmilk.csv')
Barley_cereal_breastmilk = pd.read_csv('data/Barley_cereal_breastmilk.csv')
Couscous_breastmilk = pd.read_csv('data/Couscous_breastmilk.csv')
Noodles_breastmilk = pd.read_csv('data/Noodles_breastmilk.csv')
Oat_cereal_breastmilk = pd.read_csv('data/Oat_cereal_breastmilk.csv')
Pasta_breastmilk = pd.read_csv('data/Pasta_breastmilk.csv')
Rice_cereal_breastmilk = pd.read_csv('data/Rice_cereal_breastmilk.csv')
Tapioca_pudding_breastmilk = pd.read_csv('data/Tapioca_pudding_breastmilk.csv')
White_bread_breastmilk = pd.read_csv('data/White_bread_breastmilk.csv')
Wholegrain_bread_breastmilk = pd.read_csv('data/Wholegrain_bread_breastmilk.csv')
Cottage_cheese_breastmilk = pd.read_csv('data/Cottage_cheese_breastmilk.csv')
Eggs_breastmilk = pd.read_csv('data/Eggs_breastmilk.csv')
Mozzarella_cheese_breastmilk = pd.read_csv('data/Mozzarella_cheese_breastmilk.csv')
Soymilk_breastmilk = pd.read_csv('data/Soymilk_breastmilk.csv')
Tofu_breastmilk = pd.read_csv('data/Tofu_breastmilk.csv')
Whole_milk_breastmilk = pd.read_csv('data/Whole_milk_breastmilk.csv')
Yoghurt_breastmilk = pd.read_csv('data/Yoghurt_breastmilk.csv')
Beef_breastmilk = pd.read_csv('data/Beef_breastmilk.csv')
Chicken_breastmilk = pd.read_csv('data/Chicken_breastmilk.csv')
Lamb_breastmilk = pd.read_csv('data/Lamb_breastmilk.csv')
Mackerel_breastmilk = pd.read_csv('data/Mackerel_breastmilk.csv')
Mussels_breastmilk = pd.read_csv('data/Mussels_breastmilk.csv')
Pork_breastmilk = pd.read_csv('data/Pork_breastmilk.csv')
Salmon_breastmilk = pd.read_csv('data/Salmon_breastmilk.csv')
Shrimp_breastmilk = pd.read_csv('data/Shrimp_breastmilk.csv')
Turkey_breastmilk = pd.read_csv('data/Turkey_breastmilk.csv')
Almond_breastmilk = pd.read_csv('data/Almond_breastmilk.csv')
Black_beans_breastmilk = pd.read_csv('data/Black_beans_breastmilk.csv')
Chia_breastmilk = pd.read_csv('data/Chia_breastmilk.csv')
Chickpea_breastmilk = pd.read_csv('data/Chickpea_breastmilk.csv')
Green_peas_breastmilk = pd.read_csv('data/Green_peas_breastmilk.csv')
Hazelnut_breastmilk = pd.read_csv('data/Hazelnut_breastmilk.csv')
Lentils_breastmilk = pd.read_csv('data/Lentils_breastmilk.csv')
Peanut_breastmilk = pd.read_csv('data/Peanut_breastmilk.csv')
Pecans_breastmilk = pd.read_csv('data/Pecans_breastmilk.csv')
Pumpkin_seed_breastmilk = pd.read_csv('data/Pumpkin_seed_breastmilk.csv')
Red_beans_breastmilk = pd.read_csv('data/Red_beans_breastmilk.csv')
Soybean_breastmilk = pd.read_csv('data/Soybean_breastmilk.csv')
Split_peas_breastmilk = pd.read_csv('data/Split_peas_breastmilk.csv')
Sunflower_seed_breastmilk = pd.read_csv('data/Sunflower_seed_breastmilk.csv')
White_beans_breastmilk = pd.read_csv('data/White_beans_breastmilk.csv')
Zucchini_breastmilk = pd.read_csv('data/Zucchini_breastmilk.csv')
Peache_breastmilk = pd.read_csv('data/Peache_breastmilk.csv')
Cashew_breastmilk = pd.read_csv('data/Cashew_breastmilk.csv')
Codfish_breastmilk = pd.read_csv('data/Codfish_breastmilk.csv')
Tuna_breastmilk = pd.read_csv('data/Tuna_breastmilk.csv')
Cucumber_breastmilk = pd.read_csv('data/Cucumber_breastmilk.csv')
Pumpkin_breastmilk = pd.read_csv('data/Pumpkin_breastmilk.csv')
Grape_breastmilk = pd.read_csv('data/Grape_breastmilk.csv')
Barley_breastmilk = pd.read_csv('data/Barley_breastmilk.csv')
Rice_breastmilk = pd.read_csv('data/Rice_breastmilk.csv')
Control_Breastmilk = pd.read_csv('data/Breastmilk.csv') #control
Control_Infant_formula = pd.read_csv('data/Infant_formula.csv') #control

#Choosing the tradeoff
#normally 0.3-0.6 works good
#largest tradeoff that allows the majority of the bacteria to grow 
#compromise between individual and cooperative growth
from micom.workflows import tradeoff
from micom.viz import plot_tradeoff

tradeoff_Broccoli_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Broccoli_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Broccoli_breastmilk, filename="results/tradeoff_Broccoli_breastmilk.html")
tradeoff_Brussel_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Brussel_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Brussel_breastmilk, filename="results/tradeoff_Brussel_breastmilk.html")
tradeoff_Cabbage_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Cabbage_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Cabbage_breastmilk, filename="results/tradeoff_Cabbage_breastmilk.html")
tradeoff_Carrot_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Carrot_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Carrot_breastmilk, filename="results/tradeoff_Carrot_breastmilk.html")
tradeoff_Cauliflower_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Cauliflower_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Cauliflower_breastmilk, filename="results/tradeoff_Cauliflower_breastmilk.html")
tradeoff_Celery_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Celery_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Celery_breastmilk, filename="results/tradeoff_Celery_breastmilk.html")
tradeoff_Eggplant_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Eggplant_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Eggplant_breastmilk, filename="results/tradeoff_Eggplant_breastmilk.html")
tradeoff_Green_beans_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Green_beans_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Green_beans_breastmilk, filename="results/tradeoff_Green_beans_breastmilk.html")
tradeoff_Green_capsicum_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Green_capsicum_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Green_capsicum_breastmilk, filename="results/tradeoff_Green_capsicum_breastmilk.html")
tradeoff_Lettuce_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Lettuce_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Lettuce_breastmilk, filename="results/tradeoff_Lettuce_breastmilk.html")
tradeoff_Mushroom_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Mushroom_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Mushroom_breastmilk, filename="results/tradeoff_Mushroom_breastmilk.html")
tradeoff_Onion_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Onion_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Onion_breastmilk, filename="results/tradeoff_Onion_breastmilk.html")
tradeoff_Pak_choi_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Pak_choi_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Pak_choi_breastmilk, filename="results/tradeoff_Pak_choi_breastmilk.html")
tradeoff_Potato_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Potato_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Potato_breastmilk, filename="results/tradeoff_Potato_breastmilk.html")
tradeoff_Sweetcorn_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Sweetcorn_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Sweetcorn_breastmilk, filename="results/tradeoff_Sweetcorn_breastmilk.html")
tradeoff_Spinach_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Spinach_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Spinach_breastmilk, filename="results/tradeoff_Spinach_breastmilk.html")
tradeoff_Squash_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Squash_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Squash_breastmilk, filename="results/tradeoff_Squash_breastmilk.html")
tradeoff_Sweet_potato_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Sweet_potato_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Sweet_potato_breastmilk, filename="results/tradeoff_Sweet_potato_breastmilk.html")
tradeoff_Tomato_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Tomato_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Tomato_breastmilk, filename="results/tradeoff_Tomato_breastmilk.html")
tradeoff_Yam_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Yam_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Yam_breastmilk, filename="results/tradeoff_Yam_breastmilk.html")
tradeoff_Apple_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Apple_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Apple_breastmilk, filename="results/tradeoff_Apple_breastmilk.html")
tradeoff_Banana_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Banana_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Banana_breastmilk, filename="results/tradeoff_Banana_breastmilk.html")
tradeoff_Blackcurrant_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Blackcurrant_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Blackcurrant_breastmilk, filename="results/tradeoff_Blackcurrant_breastmilk.html")
tradeoff_Blueberries_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Blueberries_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Blueberries_breastmilk, filename="results/tradeoff_Blueberries_breastmilk.html")
tradeoff_Cherry_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Cherry_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Cherry_breastmilk, filename="results/tradeoff_Cherry_breastmilk.html")
tradeoff_Feijoa_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Feijoa_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Feijoa_breastmilk, filename="results/tradeoff_Feijoa_breastmilk.html")
tradeoff_Gold_kiwifruit_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Gold_kiwifruit_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Gold_kiwifruit_breastmilk, filename="results/tradeoff_Gold_kiwifruit_breastmilk.html")
tradeoff_Grapefruit_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Grapefruit_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Grapefruit_breastmilk, filename="results/tradeoff_Grapefruit_breastmilk.html")
tradeoff_Green_kiwifruit_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Green_kiwifruit_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Green_kiwifruit_breastmilk, filename="results/tradeoff_Green_kiwifruit_breastmilk.html")
tradeoff_Mandarin_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Mandarin_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Mandarin_breastmilk, filename="results/tradeoff_Mandarin_breastmilk.html")
tradeoff_Mango_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Mango_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Mango_breastmilk, filename="results/tradeoff_Mango_breastmilk.html")
tradeoff_Melon_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Melon_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Melon_breastmilk, filename="results/tradeoff_Melon_breastmilk.html")
tradeoff_Nectarine_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Nectarine_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Nectarine_breastmilk, filename="results/tradeoff_Nectarine_breastmilk.html")
tradeoff_Orange_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Orange_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Orange_breastmilk, filename="results/tradeoff_Orange_breastmilk.html")
tradeoff_Pear_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Pear_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Pear_breastmilk, filename="results/tradeoff_Pear_breastmilk.html")
tradeoff_Pineapple_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Pineapple_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Pineapple_breastmilk, filename="results/tradeoff_Pineapple_breastmilk.html")
tradeoff_Plum_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Plum_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Plum_breastmilk, filename="results/tradeoff_Plum_breastmilk.html")
tradeoff_Raspberries_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Raspberries_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Raspberries_breastmilk, filename="results/tradeoff_Raspberries_breastmilk.html")
tradeoff_Strawberries_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Strawberries_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Strawberries_breastmilk, filename="results/tradeoff_Strawberries_breastmilk.html")
tradeoff_Barley_cereal_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Barley_cereal_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Barley_cereal_breastmilk, filename="results/tradeoff_Barley_cereal_breastmilk.html")
tradeoff_Couscous_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Couscous_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Couscous_breastmilk, filename="results/tradeoff_Couscous_breastmilk.html")
tradeoff_Noodles_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Noodles_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Noodles_breastmilk, filename="results/tradeoff_Noodles_breastmilk.html")
tradeoff_Oat_cereal_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Oat_cereal_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Oat_cereal_breastmilk, filename="results/tradeoff_Oat_cereal_breastmilk.html")
tradeoff_Pasta_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Pasta_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Pasta_breastmilk, filename="results/tradeoff_Pasta_breastmilk.html")
tradeoff_Rice_cereal_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Rice_cereal_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Rice_cereal_breastmilk, filename="results/tradeoff_Rice_cereal_breastmilk.html")
tradeoff_Tapioca_pudding_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Tapioca_pudding_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Tapioca_pudding_breastmilk, filename="results/tradeoff_Tapioca_pudding_breastmilk.html")
tradeoff_White_bread_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=White_bread_breastmilk, threads=14) 
plot_tradeoff(tradeoff_White_bread_breastmilk, filename="results/tradeoff_White_bread_breastmilk.html")
tradeoff_Wholegrain_bread_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Wholegrain_bread_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Wholegrain_bread_breastmilk, filename="results/tradeoff_Wholegrain_bread_breastmilk.html")
tradeoff_Cottage_cheese_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Cottage_cheese_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Cottage_cheese_breastmilk, filename="results/tradeoff_Cottage_cheese_breastmilk.html")
tradeoff_Eggs_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Eggs_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Eggs_breastmilk, filename="results/tradeoff_Eggs_breastmilk.html")
tradeoff_Mozzarella_cheese_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Mozzarella_cheese_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Mozzarella_cheese_breastmilk, filename="results/tradeoff_Mozzarella_cheese_breastmilk.html")
tradeoff_Soymilk_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Soymilk_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Soymilk_breastmilk, filename="results/tradeoff_Soymilk_breastmilk.html")
tradeoff_Tofu_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Tofu_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Tofu_breastmilk, filename="results/tradeoff_Tofu_breastmilk.html")
tradeoff_Whole_milk_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Whole_milk_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Whole_milk_breastmilk, filename="results/tradeoff_Whole_milk_breastmilk.html")
tradeoff_Yoghurt_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Yoghurt_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Yoghurt_breastmilk, filename="results/tradeoff_Yoghurt_breastmilk.html")
tradeoff_Beef_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Beef_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Beef_breastmilk, filename="results/tradeoff_Beef_breastmilk.html")
tradeoff_Chicken_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Chicken_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Chicken_breastmilk, filename="results/tradeoff_Chicken_breastmilk.html")
tradeoff_Lamb_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Lamb_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Lamb_breastmilk, filename="results/tradeoff_Lamb_breastmilk.html")
tradeoff_Mackerel_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Mackerel_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Mackerel_breastmilk, filename="results/tradeoff_Mackerel_breastmilk.html")
tradeoff_Mussels_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Mussels_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Mussels_breastmilk, filename="results/tradeoff_Mussels_breastmilk.html")
tradeoff_Pork_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Pork_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Pork_breastmilk, filename="results/tradeoff_Pork_breastmilk.html")
tradeoff_Salmon_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Salmon_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Salmon_breastmilk, filename="results/tradeoff_Salmon_breastmilk.html")
tradeoff_Shrimp_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Shrimp_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Shrimp_breastmilk, filename="results/tradeoff_Shrimp_breastmilk.html")
tradeoff_Turkey_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Turkey_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Turkey_breastmilk, filename="results/tradeoff_Turkey_breastmilk.html")
tradeoff_Almond_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Almond_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Almond_breastmilk, filename="results/tradeoff_Almond_breastmilk.html")
tradeoff_Black_beans_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Black_beans_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Black_beans_breastmilk, filename="results/tradeoff_Black_beans_breastmilk.html")
tradeoff_Chia_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Chia_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Chia_breastmilk, filename="results/tradeoff_Chia_breastmilk.html")
tradeoff_Chickpea_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Chickpea_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Chickpea_breastmilk, filename="results/tradeoff_Chickpea_breastmilk.html")
tradeoff_Green_peas_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Green_peas_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Green_peas_breastmilk, filename="results/tradeoff_Green_peas_breastmilk.html")
tradeoff_Hazelnut_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Hazelnut_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Hazelnut_breastmilk, filename="results/tradeoff_Hazelnut_breastmilk.html")
tradeoff_Lentils_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Lentils_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Lentils_breastmilk, filename="results/tradeoff_Lentils_breastmilk.html")
tradeoff_Peanut_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Peanut_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Peanut_breastmilk, filename="results/tradeoff_Peanut_breastmilk.html")
tradeoff_Pecans_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Pecans_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Pecans_breastmilk, filename="results/tradeoff_Pecans_breastmilk.html")
tradeoff_Pumpkin_seed_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Pumpkin_seed_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Pumpkin_seed_breastmilk, filename="results/tradeoff_Pumpkin_seed_breastmilk.html")
tradeoff_Red_beans_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Red_beans_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Red_beans_breastmilk, filename="results/tradeoff_Red_beans_breastmilk.html")
tradeoff_Soybean_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Soybean_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Soybean_breastmilk, filename="results/tradeoff_Soybean_breastmilk.html")
tradeoff_Split_peas_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Split_peas_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Split_peas_breastmilk, filename="results/tradeoff_Split_peas_breastmilk.html")
tradeoff_Sunflower_seed_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Sunflower_seed_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Sunflower_seed_breastmilk, filename="results/tradeoff_Sunflower_seed_breastmilk.html")
tradeoff_White_beans_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=White_beans_breastmilk, threads=14) 
plot_tradeoff(tradeoff_White_beans_breastmilk, filename="results/tradeoff_White_beans_breastmilk.html")
tradeoff_Zucchini_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Zucchini_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Zucchini_breastmilk, filename="results/tradeoff_Zucchini_breastmilk.html")
tradeoff_Peache_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Peache_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Peache_breastmilk, filename="results/tradeoff_Peache_breastmilk.html")
tradeoff_Cashew_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Cashew_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Cashew_breastmilk, filename="results/tradeoff_Cashew_breastmilk.html")
tradeoff_Codfish_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Codfish_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Codfish_breastmilk, filename="results/tradeoff_Codfish_breastmilk.html")
tradeoff_Tuna_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Tuna_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Tuna_breastmilk, filename="results/tradeoff_Tuna_breastmilk.html")
tradeoff_Cucumber_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Cucumber_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Cucumber_breastmilk, filename="results/tradeoff_Cucumber_breastmilk.html")
tradeoff_Pumpkin_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Pumpkin_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Pumpkin_breastmilk, filename="results/tradeoff_Pumpkin_breastmilk.html")
tradeoff_Grape_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Grape_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Grape_breastmilk, filename="results/tradeoff_Grape_breastmilk.html")
tradeoff_Barley_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Barley_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Barley_breastmilk, filename="results/tradeoff_Barley_breastmilk.html")
tradeoff_Rice_breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Rice_breastmilk, threads=14) 
plot_tradeoff(tradeoff_Rice_breastmilk, filename="results/tradeoff_Rice_breastmilk.html")
tradeoff_Control_Breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Control_Breastmilk, threads=14) 
plot_tradeoff(tradeoff_Control_Breastmilk, filename="results/tradeoff_Control_Breastmilk.html")
tradeoff_Control_Infant_formula = tradeoff(manifest, model_folder="models_cplex", medium=Control_Infant_formula, threads=14) 
plot_tradeoff(tradeoff_Control_Infant_formula, filename="results/tradeoff_infant_control_formula.html")

##Growing the models
from micom.workflows import grow, save_results

res_Broccoli_breastmilk = grow(manifest, model_folder="models_cplex", medium=Broccoli_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Broccoli_breastmilk, "results/Broccoli_breastmilk.zip") 
res_Brussel_breastmilk = grow(manifest, model_folder="models_cplex", medium=Brussel_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Brussel_breastmilk, "results/Brussel_breastmilk.zip")
res_Cabbage_breastmilk = grow(manifest, model_folder="models_cplex", medium=Cabbage_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Cabbage_breastmilk, "results/Cabbage_breastmilk.zip") 
res_Carrot_breastmilk = grow(manifest, model_folder="models_cplex", medium=Carrot_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Carrot_breastmilk, "results/Carrot_breastmilk.zip")  
res_Cauliflower_breastmilk = grow(manifest, model_folder="models_cplex", medium=Cauliflower_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Cauliflower_breastmilk, "results/Cauliflower_breastmilk.zip") 
res_Celery_breastmilk = grow(manifest, model_folder="models_cplex", medium=Celery_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Celery_breastmilk, "results/Celery_breastmilk.zip") 
res_Eggplant_breastmilk = grow(manifest, model_folder="models_cplex", medium=Eggplant_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Eggplant_breastmilk, "results/Eggplant_breastmilk.zip")
res_Green_beans_breastmilk = grow(manifest, model_folder="models_cplex", medium=Green_beans_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Green_beans_breastmilk, "results/Green_beans_breastmilk.zip") 
res_Green_capsicum_breastmilk = grow(manifest, model_folder="models_cplex", medium=Green_capsicum_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Green_capsicum_breastmilk, "results/Green_capsicum_breastmilk.zip")  
res_Lettuce_breastmilk = grow(manifest, model_folder="models_cplex", medium=Lettuce_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Lettuce_breastmilk, "results/Lettuce_breastmilk.zip") 
res_Mushroom_breastmilk = grow(manifest, model_folder="models_cplex", medium=Mushroom_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Mushroom_breastmilk, "results/Mushroom_breastmilk.zip") 
res_Onion_breastmilk = grow(manifest, model_folder="models_cplex", medium=Onion_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Onion_breastmilk, "results/Onion_breastmilk.zip")
res_Pak_choi_breastmilk = grow(manifest, model_folder="models_cplex", medium=Pak_choi_breastmilk, tradeoff=0.9, threads=14) 
save_results(res_Pak_choi_breastmilk, "results/Pak_choi_breastmilk.zip") 
res_Potato_breastmilk = grow(manifest, model_folder="models_cplex", medium=Potato_breastmilk, tradeoff=0.9, threads=14) 
save_results(res_Potato_breastmilk, "results/Potato_breastmilk.zip")  
res_Sweetcorn_breastmilk = grow(manifest, model_folder="models_cplex", medium=Sweetcorn_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Sweetcorn_breastmilk, "results/Sweetcorn_breastmilk.zip") 
res_Spinach_breastmilk = grow(manifest, model_folder="models_cplex", medium=Spinach_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Spinach_breastmilk, "results/Spinach_breastmilk.zip") 
res_Squash_breastmilk = grow(manifest, model_folder="models_cplex", medium=Squash_breastmilk, tradeoff=0.9, threads=14) 
save_results(res_Squash_breastmilk, "results/Squash_breastmilk.zip")
res_Sweet_potato_breastmilk = grow(manifest, model_folder="models_cplex", medium=Sweet_potato_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Sweet_potato_breastmilk, "results/Sweet_potato_breastmilk.zip") 
res_Tomato_breastmilk = grow(manifest, model_folder="models_cplex", medium=Tomato_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Tomato_breastmilk, "results/Tomato_breastmilk.zip")  
res_Yam_breastmilk = grow(manifest, model_folder="models_cplex", medium=Yam_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Yam_breastmilk, "results/Yam_breastmilk.zip") 
res_Apple_breastmilk = grow(manifest, model_folder="models_cplex", medium=Apple_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Apple_breastmilk, "results/Apple_breastmilk.zip") 
res_Banana_breastmilk = grow(manifest, model_folder="models_cplex", medium=Banana_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Banana_breastmilk, "results/Banana_breastmilk.zip")
res_Blackcurrant_breastmilk = grow(manifest, model_folder="models_cplex", medium=Blackcurrant_breastmilk, tradeoff=0.9, threads=14) 
save_results(res_Blackcurrant_breastmilk, "results/Blackcurrant_breastmilk.zip") 
res_Blueberries_breastmilk = grow(manifest, model_folder="models_cplex", medium=Blueberries_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Blueberries_breastmilk, "results/Blueberries_breastmilk.zip")  
res_Cherry_breastmilk = grow(manifest, model_folder="models_cplex", medium=Cherry_breastmilk, tradeoff=0.9, threads=14) 
save_results(res_Cherry_breastmilk, "results/Cherry_breastmilk.zip") 
res_Feijoa_breastmilk = grow(manifest, model_folder="models_cplex", medium=Feijoa_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Feijoa_breastmilk, "results/Feijoa_breastmilk.zip") 
res_Gold_kiwifruit_breastmilk = grow(manifest, model_folder="models_cplex", medium=Gold_kiwifruit_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Gold_kiwifruit_breastmilk, "results/Gold_kiwifruit_breastmilk.zip")
res_Grapefruit_breastmilk = grow(manifest, model_folder="models_cplex", medium=Grapefruit_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Grapefruit_breastmilk, "results/Grapefruit_breastmilk.zip") 
res_Green_kiwifruit_breastmilk = grow(manifest, model_folder="models_cplex", medium=Green_kiwifruit_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Green_kiwifruit_breastmilk, "results/Green_kiwifruit_breastmilk.zip")  
res_Mandarin_breastmilk = grow(manifest, model_folder="models_cplex", medium=Mandarin_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Mandarin_breastmilk, "results/Mandarin_breastmilk.zip") 
res_Mango_breastmilk = grow(manifest, model_folder="models_cplex", medium=Mango_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Mango_breastmilk, "results/Mango_breastmilk.zip") 
res_Melon_breastmilk = grow(manifest, model_folder="models_cplex", medium=Melon_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Melon_breastmilk, "results/Melon_breastmilk.zip")
res_Nectarine_breastmilk = grow(manifest, model_folder="models_cplex", medium=Nectarine_breastmilk, tradeoff=0.9, threads=14) 
save_results(res_Nectarine_breastmilk, "results/Nectarine_breastmilk.zip") 
res_Orange_breastmilk = grow(manifest, model_folder="models_cplex", medium=Orange_breastmilk, tradeoff=0.9, threads=14) 
save_results(res_Orange_breastmilk, "results/Orange_breastmilk.zip")  
res_Pear_breastmilk = grow(manifest, model_folder="models_cplex", medium=Pear_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Pear_breastmilk, "results/Pear_breastmilk.zip") 
res_Pineapple_breastmilk = grow(manifest, model_folder="models_cplex", medium=Pineapple_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Pineapple_breastmilk, "results/Pineapple_breastmilk.zip") 
res_Plum_breastmilk = grow(manifest, model_folder="models_cplex", medium=Plum_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Plum_breastmilk, "results/Plum_breastmilk.zip")
res_Raspberries_breastmilk = grow(manifest, model_folder="models_cplex", medium=Raspberries_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Raspberries_breastmilk, "results/Raspberries_breastmilk.zip") 
res_Strawberries_breastmilk = grow(manifest, model_folder="models_cplex", medium=Strawberries_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Strawberries_breastmilk, "results/Strawberries_breastmilk.zip")  
res_Barley_cereal_breastmilk = grow(manifest, model_folder="models_cplex", medium=Barley_cereal_breastmilk, tradeoff=0.9, threads=14) 
save_results(res_Barley_cereal_breastmilk, "results/Barley_cereal_breastmilk.zip") 
res_Couscous_breastmilk = grow(manifest, model_folder="models_cplex", medium=Couscous_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Couscous_breastmilk, "results/Couscous_breastmilk.zip") 
res_Noodles_breastmilk = grow(manifest, model_folder="models_cplex", medium=Noodles_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Noodles_breastmilk, "results/Noodles_breastmilk.zip")
res_Oat_cereal_breastmilk = grow(manifest, model_folder="models_cplex", medium=Oat_cereal_breastmilk, tradeoff=0.7, threads=14) 
save_results(res_Oat_cereal_breastmilk, "results/Oat_cereal_breastmilk.zip") 
res_Pasta_breastmilk = grow(manifest, model_folder="models_cplex", medium=Pasta_breastmilk, tradeoff=0.9, threads=14) 
save_results(res_Pasta_breastmilk, "results/Pasta_breastmilk.zip")  
res_Rice_cereal_breastmilk = grow(manifest, model_folder="models_cplex", medium=Rice_cereal_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Rice_cereal_breastmilk, "results/Rice_cereal_breastmilk.zip") 
res_Tapioca_pudding_breastmilk = grow(manifest, model_folder="models_cplex", medium=Tapioca_pudding_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Tapioca_pudding_breastmilk, "results/Tapioca_pudding_breastmilk.zip") 
res_White_bread_breastmilk = grow(manifest, model_folder="models_cplex", medium=White_bread_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_White_bread_breastmilk, "results/White_bread_breastmilk.zip")
res_Wholegrain_bread_breastmilk = grow(manifest, model_folder="models_cplex", medium=Wholegrain_bread_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Wholegrain_bread_breastmilk, "results/Wholegrain_bread_breastmilk.zip") 
res_Cottage_cheese_breastmilk = grow(manifest, model_folder="models_cplex", medium=Cottage_cheese_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Cottage_cheese_breastmilk, "results/Cottage_cheese_breastmilk.zip")  
res_Eggs_breastmilk = grow(manifest, model_folder="models_cplex", medium=Eggs_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Eggs_breastmilk, "results/Eggs_breastmilk.zip") 
res_Mozzarella_cheese_breastmilk = grow(manifest, model_folder="models_cplex", medium=Mozzarella_cheese_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Mozzarella_cheese_breastmilk, "results/Mozzarella_cheese_breastmilk.zip") 
res_Soymilk_breastmilk = grow(manifest, model_folder="models_cplex", medium=Soymilk_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Soymilk_breastmilk, "results/Soymilk_breastmilk.zip")
res_Tofu_breastmilk = grow(manifest, model_folder="models_cplex", medium=Tofu_breastmilk, tradeoff=0.7, threads=14) 
save_results(res_Tofu_breastmilk, "results/Tofu_breastmilk.zip") 
res_Whole_milk_breastmilk = grow(manifest, model_folder="models_cplex", medium=Whole_milk_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Whole_milk_breastmilk, "results/Whole_milk_breastmilk.zip")  
res_Yoghurt_breastmilk = grow(manifest, model_folder="models_cplex", medium=Yoghurt_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Yoghurt_breastmilk, "results/Yoghurt_breastmilk.zip") 
res_Beef_breastmilk = grow(manifest, model_folder="models_cplex", medium=Beef_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Beef_breastmilk, "results/Beef_breastmilk.zip") 
res_Chicken_breastmilk = grow(manifest, model_folder="models_cplex", medium=Chicken_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Chicken_breastmilk, "results/Chicken_breastmilk.zip")
res_Lamb_breastmilk = grow(manifest, model_folder="models_cplex", medium=Lamb_breastmilk, tradeoff=0.7, threads=14) 
save_results(res_Lamb_breastmilk, "results/Lamb_breastmilk.zip") 
res_Mackerel_breastmilk = grow(manifest, model_folder="models_cplex", medium=Mackerel_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Mackerel_breastmilk, "results/Mackerel_breastmilk.zip")  
res_Mussels_breastmilk = grow(manifest, model_folder="models_cplex", medium=Mussels_breastmilk, tradeoff=0.9, threads=14) 
save_results(res_Mussels_breastmilk, "results/Mussels_breastmilk.zip") 
res_Pork_breastmilk = grow(manifest, model_folder="models_cplex", medium=Pork_breastmilk, tradeoff=0.9, threads=14) 
save_results(res_Pork_breastmilk, "results/Pork_breastmilk.zip") 
res_Salmon_breastmilk = grow(manifest, model_folder="models_cplex", medium=Salmon_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Salmon_breastmilk, "results/Salmon_breastmilk.zip")
res_Shrimp_breastmilk = grow(manifest, model_folder="models_cplex", medium=Shrimp_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Shrimp_breastmilk, "results/Shrimp_breastmilk.zip") 
res_Turkey_breastmilk = grow(manifest, model_folder="models_cplex", medium=Turkey_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Turkey_breastmilk, "results/Turkey_breastmilk.zip")  
res_Almond_breastmilk = grow(manifest, model_folder="models_cplex", medium=Almond_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Almond_breastmilk, "results/Almond_breastmilk.zip") 
res_Black_beans_breastmilk = grow(manifest, model_folder="models_cplex", medium=Black_beans_breastmilk, tradeoff=0.9, threads=14) 
save_results(res_Black_beans_breastmilk, "results/Black_beans_breastmilk.zip") 
res_Chia_breastmilk = grow(manifest, model_folder="models_cplex", medium=Chia_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Chia_breastmilk, "results/Chia_breastmilk.zip")
res_Chickpea_breastmilk = grow(manifest, model_folder="models_cplex", medium=Chickpea_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Chickpea_breastmilk, "results/Chickpea_breastmilk.zip") 
res_Green_peas_breastmilk = grow(manifest, model_folder="models_cplex", medium=Green_peas_breastmilk, tradeoff=0.7, threads=14) 
save_results(res_Green_peas_breastmilk, "results/Green_peas_breastmilk.zip")  
res_Hazelnut_breastmilk = grow(manifest, model_folder="models_cplex", medium=Hazelnut_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Hazelnut_breastmilk, "results/Hazelnut_breastmilk.zip") 
res_Lentils_breastmilk = grow(manifest, model_folder="models_cplex", medium=Lentils_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Lentils_breastmilk, "results/Lentils_breastmilk.zip") 
res_Peanut_breastmilk = grow(manifest, model_folder="models_cplex", medium=Peanut_breastmilk, tradeoff=0.9, threads=14) 
save_results(res_Peanut_breastmilk, "results/Peanut_breastmilk.zip")
res_Pecans_breastmilk = grow(manifest, model_folder="models_cplex", medium=Pecans_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Pecans_breastmilk, "results/Pecans_breastmilk.zip") 
res_Pumpkin_seed_breastmilk = grow(manifest, model_folder="models_cplex", medium=Pumpkin_seed_breastmilk, tradeoff=0.9, threads=14) 
save_results(res_Pumpkin_seed_breastmilk, "results/Pumpkin_seed_breastmilk.zip")  
res_Red_beans_breastmilk = grow(manifest, model_folder="models_cplex", medium=Red_beans_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Red_beans_breastmilk, "results/Red_beans_breastmilk.zip")
res_Soybean_breastmilk = grow(manifest, model_folder="models_cplex", medium=Soybean_breastmilk, tradeoff=0.9, threads=14) 
save_results(res_Soybean_breastmilk, "results/Soybean_breastmilk.zip") 
res_Split_peas_breastmilk = grow(manifest, model_folder="models_cplex", medium=Split_peas_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Split_peas_breastmilk, "results/Split_peas_breastmilk.zip")
res_Sunflower_seed_breastmilk = grow(manifest, model_folder="models_cplex", medium=Sunflower_seed_breastmilk, tradeoff=0.5, threads=14) 
save_results(res_Sunflower_seed_breastmilk, "results/Sunflower_seed_breastmilk.zip") 
res_White_beans_breastmilk = grow(manifest, model_folder="models_cplex", medium=White_beans_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_White_beans_breastmilk, "results/White_beans_breastmilk.zip")  
res_Zucchini_breastmilk = grow(manifest, model_folder="models_cplex", medium=Zucchini_breastmilk, tradeoff=0.6, threads=14) 
save_results(res_Zucchini_breastmilk, "results/Zucchini_breastmilk.zip") 
res_Peache_breastmilk = grow(manifest, model_folder="models_cplex", medium=Peache_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Peache_breastmilk, "results/Peache_breastmilk.zip") 
res_Cashew_breastmilk = grow(manifest, model_folder="models_cplex", medium=Cashew_breastmilk, tradeoff=0.7, threads=14) 
save_results(res_Cashew_breastmilk, "results/Cashew_breastmilk.zip")
res_Codfish_breastmilk = grow(manifest, model_folder="models_cplex", medium=Codfish_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Codfish_breastmilk, "results/Codfish_breastmilk.zip") 
res_Tuna_breastmilk = grow(manifest, model_folder="models_cplex", medium=Tuna_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Tuna_breastmilk, "results/Tuna_breastmilk.zip")  
res_Cucumber_breastmilk = grow(manifest, model_folder="models_cplex", medium=Cucumber_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Cucumber_breastmilk, "results/Cucumber_breastmilk.zip") 
res_Pumpkin_breastmilk = grow(manifest, model_folder="models_cplex", medium=Pumpkin_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Pumpkin_breastmilk, "results/Pumpkin_breastmilk.zip") 
res_Grape_breastmilk = grow(manifest, model_folder="models_cplex", medium=Grape_breastmilk, tradeoff=0.9, threads=14) 
save_results(res_Grape_breastmilk, "results/Grape_breastmilk.zip")
res_Barley_breastmilk = grow(manifest, model_folder="models_cplex", medium=Barley_breastmilk, tradeoff=0.8, threads=14) 
save_results(res_Barley_breastmilk, "results/Barley_breastmilk.zip") 
res_Rice_breastmilk = grow(manifest, model_folder="models_cplex", medium=Rice_breastmilk, tradeoff=0.6, threads=14) 
save_results(res_Rice_breastmilk, "results/Rice_breastmilk.zip")  
res_Control_Breastmilk = grow(manifest, model_folder="models_cplex", medium=Control_Breastmilk, tradeoff=0.9, threads=14) 
save_results(res_Control_Breastmilk, "results/Control_Breastmilk.zip") 
res_Control_Infant_formula = grow(manifest, model_folder="models_cplex", medium=Control_Infant_formula, tradeoff=0.8, threads=14) 
save_results(res_Control_Infant_formula, "results/Control_Infant_formula.zip")

#Visualisations
from micom.viz import plot_growth
#Growth rates

plot_growth(res_Broccoli_breastmilk, filename="results/growth_rates_Broccoli_breastmilk.html")  
plot_growth(res_Brussel_breastmilk, filename="results/growth_rates_Brussel_breastmilk.html") 
plot_growth(res_Cabbage_breastmilk, filename="results/growth_rates_Cabbage_breastmilk.html")  
plot_growth(res_Carrot_breastmilk, filename="results/growth_rates_Carrot_breastmilk.html") 
plot_growth(res_Cauliflower_breastmilk, filename="results/growth_rates_Cauliflower_breastmilk.html") 
plot_growth(res_Celery_breastmilk, filename="results/growth_rates_Celery_breastmilk.html")  
plot_growth(res_Eggplant_breastmilk, filename="results/growth_rates_Eggplant_breastmilk.html") 
plot_growth(res_Green_beans_breastmilk, filename="results/growth_rates_Green_beans_breastmilk.html")  
plot_growth(res_Green_capsicum_breastmilk, filename="results/growth_rates_Green_capsicum_breastmilk.html") 
plot_growth(res_Lettuce_breastmilk, filename="results/growth_rates_Lettuce_breastmilk.html")
plot_growth(res_Mushroom_breastmilk, filename="results/growth_rates_Mushroom_breastmilk.html")  
plot_growth(res_Onion_breastmilk, filename="results/growth_rates_Onion_breastmilk.html") 
plot_growth(res_Pak_choi_breastmilk, filename="results/growth_rates_Pak_choi_breastmilk.html")  
plot_growth(res_Potato_breastmilk, filename="results/growth_rates_Potato_breastmilk.html") 
plot_growth(res_Sweetcorn_breastmilk, filename="results/growth_rates_Sweetcorn_breastmilk.html") 
plot_growth(res_Spinach_breastmilk, filename="results/growth_rates_Spinach_breastmilk.html")  
plot_growth(res_Squash_breastmilk, filename="results/growth_rates_Squash_breastmilk.html") 
plot_growth(res_Sweet_potato_breastmilk, filename="results/growth_rates_Sweet_potato_breastmilk.html")  
plot_growth(res_Tomato_breastmilk, filename="results/growth_rates_Tomato_breastmilk.html") 
plot_growth(res_Yam_breastmilk, filename="results/growth_rates_Yam_breastmilk.html") 
plot_growth(res_Apple_breastmilk, filename="results/growth_rates_Apple_breastmilk.html")  
plot_growth(res_Banana_breastmilk, filename="results/growth_rates_Banana_breastmilk.html") 
plot_growth(res_Blackcurrant_breastmilk, filename="results/growth_rates_Blackcurrant_breastmilk.html")  
plot_growth(res_Blueberries_breastmilk, filename="results/growth_rates_Blueberries_breastmilk.html") 
plot_growth(res_Cherry_breastmilk, filename="results/growth_rates_Cherry_breastmilk.html")
plot_growth(res_Feijoa_breastmilk, filename="results/growth_rates_Feijoa_breastmilk.html")  
plot_growth(res_Gold_kiwifruit_breastmilk, filename="results/growth_rates_Gold_kiwifruit_breastmilk.html") 
plot_growth(res_Grapefruit_breastmilk, filename="results/growth_rates_Grapefruit_breastmilk.html")  
plot_growth(res_Green_kiwifruit_breastmilk, filename="results/growth_rates_Green_kiwifruit_breastmilk.html") 
plot_growth(res_Mandarin_breastmilk, filename="results/growth_rates_Mandarin_breastmilk.html") 
plot_growth(res_Mango_breastmilk, filename="results/growth_rates_Mango_breastmilk.html")  
plot_growth(res_Melon_breastmilk, filename="results/growth_rates_Melon_breastmilk.html") 
plot_growth(res_Nectarine_breastmilk, filename="results/growth_rates_Nectarine_breastmilk.html")  
plot_growth(res_Orange_breastmilk, filename="results/growth_rates_Orange_breastmilk.html") 
plot_growth(res_Pear_breastmilk, filename="results/growth_rates_Pear_breastmilk.html") 
plot_growth(res_Pineapple_breastmilk, filename="results/growth_rates_Pineapple_breastmilk.html")  
plot_growth(res_Plum_breastmilk, filename="results/growth_rates_Plum_breastmilk.html") 
plot_growth(res_Raspberries_breastmilk, filename="results/growth_rates_Raspberries_breastmilk.html")  
plot_growth(res_Strawberries_breastmilk, filename="results/growth_rates_Strawberries_breastmilk.html") 
plot_growth(res_Barley_cereal_breastmilk, filename="results/growth_rates_Barley_cereal_breastmilk.html")
plot_growth(res_Couscous_breastmilk, filename="results/growth_rates_Couscous_breastmilk.html")  
plot_growth(res_Noodles_breastmilk, filename="results/growth_rates_Noodles_breastmilk.html") 
plot_growth(res_Oat_cereal_breastmilk, filename="results/growth_rates_Oat_cereal_breastmilk.html")  
plot_growth(res_Pasta_breastmilk, filename="results/growth_rates_Pasta_breastmilk.html") 
plot_growth(res_Rice_cereal_breastmilk, filename="results/growth_rates_Rice_cereal_breastmilk.html") 
plot_growth(res_Tapioca_pudding_breastmilk, filename="results/growth_rates_Tapioca_pudding_breastmilk.html")  
plot_growth(res_White_bread_breastmilk, filename="results/growth_rates_White_bread_breastmilk.html") 
plot_growth(res_Wholegrain_bread_breastmilk, filename="results/growth_rates_Wholegrain_bread_breastmilk.html")  
plot_growth(res_Cottage_cheese_breastmilk, filename="results/growth_rates_Cottage_cheese_breastmilk.html") 
plot_growth(res_Eggs_breastmilk, filename="results/growth_rates_Eggs_breastmilk.html") 
plot_growth(res_Mozzarella_cheese_breastmilk, filename="results/growth_rates_Mozzarella_cheese_breastmilk.html")  
plot_growth(res_Soymilk_breastmilk, filename="results/growth_rates_Soymilk_breastmilk.html") 
plot_growth(res_Tofu_breastmilk, filename="results/growth_rates_Tofu_breastmilk.html")  
plot_growth(res_Whole_milk_breastmilk, filename="results/growth_rates_Whole_milk_breastmilk.html") 
plot_growth(res_Yoghurt_breastmilk, filename="results/growth_rates_Yoghurt_breastmilk.html")
plot_growth(res_Beef_breastmilk, filename="results/growth_rates_Beef_breastmilk.html")  
plot_growth(res_Chicken_breastmilk, filename="results/growth_rates_Chicken_breastmilk.html") 
plot_growth(res_Lamb_breastmilk, filename="results/growth_rates_Lamb_breastmilk.html")  
plot_growth(res_Mackerel_breastmilk, filename="results/growth_rates_Mackerel_breastmilk.html") 
plot_growth(res_Mussels_breastmilk, filename="results/growth_rates_Mussels_breastmilk.html")
plot_growth(res_Pork_breastmilk, filename="results/growth_rates_Pork_breastmilk.html")  
plot_growth(res_Salmon_breastmilk, filename="results/growth_rates_Salmon_breastmilk.html") 
plot_growth(res_Shrimp_breastmilk, filename="results/growth_rates_Shrimp_breastmilk.html")  
plot_growth(res_Turkey_breastmilk, filename="results/growth_rates_Turkey_breastmilk.html") 
plot_growth(res_Almond_breastmilk, filename="results/growth_rates_Almond_breastmilk.html") 
plot_growth(res_Black_beans_breastmilk, filename="results/growth_rates_Black_beans_breastmilk.html")  
plot_growth(res_Chia_breastmilk, filename="results/growth_rates_Chia_breastmilk.html") 
plot_growth(res_Chickpea_breastmilk, filename="results/growth_rates_Chickpea_breastmilk.html")  
plot_growth(res_Green_peas_breastmilk, filename="results/growth_rates_Green_peas_breastmilk.html") 
plot_growth(res_Hazelnut_breastmilk, filename="results/growth_rates_Hazelnut_breastmilk.html")
plot_growth(res_Lentils_breastmilk, filename="results/growth_rates_Lentils_breastmilk.html")  
plot_growth(res_Peanut_breastmilk, filename="results/growth_rates_Peanut_breastmilk.html") 
plot_growth(res_Pecans_breastmilk, filename="results/growth_rates_Pecans_breastmilk.html")  
plot_growth(res_Pumpkin_seed_breastmilk, filename="results/growth_rates_Pumpkin_seed_breastmilk.html") 
plot_growth(res_Red_beans_breastmilk, filename="results/growth_rates_Red_beans_breastmilk.html") 
plot_growth(res_Soybean_breastmilk, filename="results/growth_rates_Soybean_breastmilk.html")  
plot_growth(res_Split_peas_breastmilk, filename="results/growth_rates_Split_peas_breastmilk.html") 
plot_growth(res_Sunflower_seed_breastmilk, filename="results/growth_rates_Sunflower_seed_breastmilk.html")  
plot_growth(res_White_beans_breastmilk, filename="results/growth_rates_White_beans_breastmilk.html") 
plot_growth(res_Zucchini_breastmilk, filename="results/growth_rates_Zucchini_breastmilk.html") 
plot_growth(res_Peache_breastmilk, filename="results/growth_rates_Peache_breastmilk.html")  
plot_growth(res_Cashew_breastmilk, filename="results/growth_rates_Cashew_breastmilk.html") 
plot_growth(res_Codfish_breastmilk, filename="results/growth_rates_Codfish_breastmilk.html")  
plot_growth(res_Tuna_breastmilk, filename="results/growth_rates_Tuna_breastmilk.html") 
plot_growth(res_Cucumber_breastmilk, filename="results/growth_rates_Cucumber_breastmilk.html")
plot_growth(res_Pumpkin_breastmilk, filename="results/growth_rates_Pumpkin_breastmilk.html")  
plot_growth(res_Grape_breastmilk, filename="results/growth_rates_Grape_breastmilk.html") 
plot_growth(res_Barley_breastmilk, filename="results/growth_rates_Barley_breastmilk.html")  
plot_growth(res_Rice_breastmilk, filename="results/growth_rates_Rice_breastmilk.html")  
plot_growth(res_Control_Breastmilk, filename="results/growth_rates_Control_Breastmilk.html")  
plot_growth(res_Control_Infant_formula, filename="results/growth_rates_Control_Infant_formula.html") 

#Production rate
from micom.measures import production_rates
import pandas as pd

prod_Broccoli_breastmilk = production_rates(res_Broccoli_breastmilk)
prod_Brussel_breastmilk = production_rates(res_Brussel_breastmilk)
prod_Cabbage_breastmilk = production_rates(res_Cabbage_breastmilk)
prod_Carrot_breastmilk = production_rates(res_Carrot_breastmilk)
prod_Cauliflower_breastmilk = production_rates(res_Cauliflower_breastmilk)
prod_Celery_breastmilk = production_rates(res_Celery_breastmilk)
prod_Eggplant_breastmilk = production_rates(res_Eggplant_breastmilk)
prod_Green_beans_breastmilk = production_rates(res_Green_beans_breastmilk)
prod_Green_capsicum_breastmilk = production_rates(res_Green_capsicum_breastmilk)
prod_Lettuce_breastmilk = production_rates(res_Lettuce_breastmilk)
prod_Mushroom_breastmilk = production_rates(res_Mushroom_breastmilk)
prod_Onion_breastmilk = production_rates(res_Onion_breastmilk)
prod_Pak_choi_breastmilk = production_rates(res_Pak_choi_breastmilk)
prod_Potato_breastmilk = production_rates(res_Potato_breastmilk)
prod_Sweetcorn_breastmilk = production_rates(res_Sweetcorn_breastmilk)
prod_Spinach_breastmilk = production_rates(res_Spinach_breastmilk)
prod_Squash_breastmilk = production_rates(res_Squash_breastmilk)
prod_Sweet_potato_breastmilk = production_rates(res_Sweet_potato_breastmilk)
prod_Tomato_breastmilk = production_rates(res_Tomato_breastmilk)
prod_Yam_breastmilk = production_rates(res_Yam_breastmilk)
prod_Apple_breastmilk = production_rates(res_Apple_breastmilk)
prod_Banana_breastmilk = production_rates(res_Banana_breastmilk)
prod_Blackcurrant_breastmilk = production_rates(res_Blackcurrant_breastmilk)
prod_Blueberries_breastmilk = production_rates(res_Blueberries_breastmilk)
prod_Cherry_breastmilk = production_rates(res_Cherry_breastmilk)
prod_Feijoa_breastmilk = production_rates(res_Feijoa_breastmilk)
prod_Gold_kiwifruit_breastmilk = production_rates(res_Gold_kiwifruit_breastmilk)
prod_Grapefruit_breastmilk = production_rates(res_Grapefruit_breastmilk)
prod_Green_kiwifruit_breastmilk = production_rates(res_Green_kiwifruit_breastmilk)
prod_Mandarin_breastmilk = production_rates(res_Mandarin_breastmilk)
prod_Mango_breastmilk = production_rates(res_Mango_breastmilk)
prod_Melon_breastmilk = production_rates(res_Melon_breastmilk)
prod_Nectarine_breastmilk = production_rates(res_Nectarine_breastmilk)
prod_Orange_breastmilk = production_rates(res_Orange_breastmilk)
prod_Pear_breastmilk = production_rates(res_Pear_breastmilk)
prod_Pineapple_breastmilk = production_rates(res_Pineapple_breastmilk)
prod_Plum_breastmilk = production_rates(res_Plum_breastmilk)
prod_Raspberries_breastmilk = production_rates(res_Raspberries_breastmilk)
prod_Strawberries_breastmilk = production_rates(res_Strawberries_breastmilk)
prod_Barley_cereal_breastmilk = production_rates(res_Barley_cereal_breastmilk)
prod_Couscous_breastmilk = production_rates(res_Couscous_breastmilk)
prod_Noodles_breastmilk = production_rates(res_Noodles_breastmilk)
prod_Oat_cereal_breastmilk = production_rates(res_Oat_cereal_breastmilk)
prod_Pasta_breastmilk = production_rates(res_Pasta_breastmilk)
prod_Rice_cereal_breastmilk = production_rates(res_Rice_cereal_breastmilk)
prod_Tapioca_pudding_breastmilk = production_rates(res_Tapioca_pudding_breastmilk)
prod_White_bread_breastmilk = production_rates(res_White_bread_breastmilk)
prod_Wholegrain_bread_breastmilk = production_rates(res_Wholegrain_bread_breastmilk)
prod_Cottage_cheese_breastmilk = production_rates(res_Cottage_cheese_breastmilk)
prod_Eggs_breastmilk = production_rates(res_Eggs_breastmilk)
prod_Mozzarella_cheese_breastmilk = production_rates(res_Mozzarella_cheese_breastmilk)
prod_Soymilk_breastmilk = production_rates(res_Soymilk_breastmilk)
prod_Tofu_breastmilk = production_rates(res_Tofu_breastmilk)
prod_Whole_milk_breastmilk = production_rates(res_Whole_milk_breastmilk)
prod_Yoghurt_breastmilk = production_rates(res_Yoghurt_breastmilk)
prod_Beef_breastmilk = production_rates(res_Beef_breastmilk)
prod_Chicken_breastmilk = production_rates(res_Chicken_breastmilk)
prod_Lamb_breastmilk = production_rates(res_Lamb_breastmilk)
prod_Mackerel_breastmilk = production_rates(res_Mackerel_breastmilk)
prod_Mussels_breastmilk = production_rates(res_Mussels_breastmilk)
prod_Pork_breastmilk = production_rates(res_Pork_breastmilk)
prod_Salmon_breastmilk = production_rates(res_Salmon_breastmilk)
prod_Shrimp_breastmilk = production_rates(res_Shrimp_breastmilk)
prod_Turkey_breastmilk = production_rates(res_Turkey_breastmilk)
prod_Almond_breastmilk = production_rates(res_Almond_breastmilk)
prod_Black_beans_breastmilk = production_rates(res_Black_beans_breastmilk)
prod_Chia_breastmilk = production_rates(res_Chia_breastmilk)
prod_Chickpea_breastmilk = production_rates(res_Chickpea_breastmilk)
prod_Green_peas_breastmilk = production_rates(res_Green_peas_breastmilk)
prod_Hazelnut_breastmilk = production_rates(res_Hazelnut_breastmilk)
prod_Lentils_breastmilk = production_rates(res_Lentils_breastmilk)
prod_Peanut_breastmilk = production_rates(res_Peanut_breastmilk)
prod_Pecans_breastmilk = production_rates(res_Pecans_breastmilk)
prod_Pumpkin_seed_breastmilk = production_rates(res_Pumpkin_seed_breastmilk)
prod_Red_beans_breastmilk = production_rates(res_Red_beans_breastmilk)
prod_Soybean_breastmilk = production_rates(res_Soybean_breastmilk)
prod_Split_peas_breastmilk = production_rates(res_Split_peas_breastmilk)
prod_Sunflower_seed_breastmilk = production_rates(res_Sunflower_seed_breastmilk)
prod_White_beans_breastmilk = production_rates(res_White_beans_breastmilk)
prod_Zucchini_breastmilk = production_rates(res_Zucchini_breastmilk)
prod_Peache_breastmilk = production_rates(res_Peache_breastmilk)
prod_Cashew_breastmilk = production_rates(res_Cashew_breastmilk)
prod_Codfish_breastmilk = production_rates(res_Codfish_breastmilk)
prod_Tuna_breastmilk = production_rates(res_Tuna_breastmilk)
prod_Cucumber_breastmilk = production_rates(res_Cucumber_breastmilk)
prod_Pumpkin_breastmilk = production_rates(res_Pumpkin_breastmilk)
prod_Grape_breastmilk = production_rates(res_Grape_breastmilk)
prod_Barley_breastmilk = production_rates(res_Barley_breastmilk)
prod_Rice_breastmilk = production_rates(res_Rice_breastmilk)
prod_Control_Breastmilk = production_rates(res_Control_Breastmilk)
prod_Control_Infant_formula = production_rates(res_Control_Infant_formula)

prod_Broccoli_breastmilk['diet'] = 'Broccoli_breastmilk' #create new colum
prod_Brussel_breastmilk['diet'] = 'Brussel_breastmilk' #create new colum
prod_Cabbage_breastmilk['diet'] = 'Cabbage_breastmilk' #create new colum
prod_Carrot_breastmilk['diet'] = 'Carrot_breastmilk' #create new colum
prod_Cauliflower_breastmilk['diet'] = 'Cauliflower_breastmilk' #create new colum
prod_Celery_breastmilk['diet'] = 'Celery_breastmilk' #create new colum
prod_Eggplant_breastmilk['diet'] = 'Eggplant_breastmilk' #create new colum
prod_Green_beans_breastmilk['diet'] = 'Green_beans_breastmilk' #create new colum
prod_Green_capsicum_breastmilk['diet'] = 'Green_capsicum_breastmilk' #create new colum
prod_Lettuce_breastmilk['diet'] = 'Lettuce_breastmilk' #create new colum
prod_Mushroom_breastmilk['diet'] = 'Mushroom_breastmilk' #create new colum
prod_Onion_breastmilk['diet'] = 'Onion_breastmilk' #create new colum
prod_Pak_choi_breastmilk['diet'] = 'Pak_choi_breastmilk' #create new colum
prod_Potato_breastmilk['diet'] = 'Potato_breastmilk' #create new colum
prod_Sweetcorn_breastmilk['diet'] = 'Sweetcorn_breastmilk' #create new colum
prod_Spinach_breastmilk['diet'] = 'Spinach_breastmilk' #create new colum
prod_Squash_breastmilk['diet'] = 'Squash_breastmilk' #create new colum
prod_Sweet_potato_breastmilk['diet'] = 'Sweet_potato_breastmilk' #create new colum
prod_Tomato_breastmilk['diet'] = 'Tomato_breastmilk' #create new colum
prod_Yam_breastmilk['diet'] = 'Yam_breastmilk' #create new colum
prod_Apple_breastmilk['diet'] = 'Apple_breastmilk' #create new colum
prod_Banana_breastmilk['diet'] = 'Banana_breastmilk' #create new colum
prod_Blackcurrant_breastmilk['diet'] = 'Blackcurrant_breastmilk' #create new colum
prod_Blueberries_breastmilk['diet'] = 'Blueberries_breastmilk' #create new colum
prod_Cherry_breastmilk['diet'] = 'Cherry_breastmilk' #create new colum
prod_Feijoa_breastmilk['diet'] = 'Feijoa_breastmilk' #create new colum
prod_Gold_kiwifruit_breastmilk['diet'] = 'Gold_kiwifruit_breastmilk' #create new colum
prod_Grapefruit_breastmilk['diet'] = 'Grapefruit_breastmilk' #create new colum
prod_Green_kiwifruit_breastmilk['diet'] = 'Green_kiwifruit_breastmilk' #create new colum
prod_Mandarin_breastmilk['diet'] = 'Mandarin_breastmilk' #create new colum
prod_Mango_breastmilk['diet'] = 'Mango_breastmilk' #create new colum
prod_Melon_breastmilk['diet'] = 'Melon_breastmilk' #create new colum
prod_Nectarine_breastmilk['diet'] = 'Nectarine_breastmilk' #create new colum
prod_Orange_breastmilk['diet'] = 'Orange_breastmilk' #create new colum
prod_Pear_breastmilk['diet'] = 'Pear_breastmilk' #create new colum
prod_Pineapple_breastmilk['diet'] = 'Pineapple_breastmilk' #create new colum
prod_Plum_breastmilk['diet'] = 'Plum_breastmilk' #create new colum
prod_Raspberries_breastmilk['diet'] = 'Raspberries_breastmilk' #create new colum
prod_Strawberries_breastmilk['diet'] = 'Strawberries_breastmilk' #create new colum
prod_Barley_cereal_breastmilk['diet'] = 'Barley_cereal_breastmilk' #create new colum
prod_Couscous_breastmilk['diet'] = 'Couscous_breastmilk' #create new colum
prod_Noodles_breastmilk['diet'] = 'Noodles_breastmilk' #create new colum
prod_Oat_cereal_breastmilk['diet'] = 'Oat_cereal_breastmilk' #create new colum
prod_Pasta_breastmilk['diet'] = 'Pasta_breastmilk' #create new colum
prod_Rice_cereal_breastmilk['diet'] = 'Rice_cereal_breastmilk' #create new colum
prod_Tapioca_pudding_breastmilk['diet'] = 'Tapioca_pudding_breastmilk' #create new colum
prod_White_bread_breastmilk['diet'] = 'White_bread_breastmilk' #create new colum
prod_Wholegrain_bread_breastmilk['diet'] = 'Wholegrain_bread_breastmilk' #create new colum
prod_Cottage_cheese_breastmilk['diet'] = 'Cottage_cheese_breastmilk' #create new colum
prod_Eggs_breastmilk['diet'] = 'Eggs_breastmilk' #create new colum
prod_Mozzarella_cheese_breastmilk['diet'] = 'Mozzarella_cheese_breastmilk' #create new colum
prod_Soymilk_breastmilk['diet'] = 'Soymilk_breastmilk' #create new colum
prod_Tofu_breastmilk['diet'] = 'Tofu_breastmilk' #create new colum
prod_Whole_milk_breastmilk['diet'] = 'Whole_milk_breastmilk' #create new colum
prod_Yoghurt_breastmilk['diet'] = 'Yoghurt_breastmilk' #create new colum
prod_Beef_breastmilk['diet'] = 'Beef_breastmilk' #create new colum
prod_Chicken_breastmilk['diet'] = 'Chicken_breastmilk' #create new colum
prod_Lamb_breastmilk['diet'] = 'Lamb_breastmilk' #create new colum
prod_Mackerel_breastmilk['diet'] = 'Mackerel_breastmilk' #create new colum
prod_Mussels_breastmilk['diet'] = 'Mussels_breastmilk' #create new colum
prod_Pork_breastmilk['diet'] = 'Pork_breastmilk' #create new colum
prod_Salmon_breastmilk['diet'] = 'Salmon_breastmilk' #create new colum
prod_Shrimp_breastmilk['diet'] = 'Shrimp_breastmilk' #create new colum
prod_Turkey_breastmilk['diet'] = 'Turkey_breastmilk' #create new colum
prod_Almond_breastmilk['diet'] = 'Almond_breastmilk' #create new colum
prod_Black_beans_breastmilk['diet'] = 'Black_beans_breastmilk' #create new colum
prod_Chia_breastmilk['diet'] = 'Chia_breastmilk' #create new colum
prod_Chickpea_breastmilk['diet'] = 'Chickpea_breastmilk' #create new colum
prod_Green_peas_breastmilk['diet'] = 'Green_peas_breastmilk' #create new colum
prod_Hazelnut_breastmilk['diet'] = 'Hazelnut_breastmilk' #create new colum
prod_Lentils_breastmilk['diet'] = 'Lentils_breastmilk' #create new colum
prod_Peanut_breastmilk['diet'] = 'Peanut_breastmilk' #create new colum
prod_Pecans_breastmilk['diet'] = 'Pecans_breastmilk' #create new colum
prod_Pumpkin_seed_breastmilk['diet'] = 'Pumpkin_seed_breastmilk' #create new colum
prod_Red_beans_breastmilk['diet'] = 'Red_beans_breastmilk' #create new colum
prod_Soybean_breastmilk['diet'] = 'Soybean_breastmilk' #create new colum
prod_Split_peas_breastmilk['diet'] = 'Split_peas_breastmilk' #create new colum
prod_Sunflower_seed_breastmilk['diet'] = 'Sunflower_seed_breastmilk' #create new colum
prod_White_beans_breastmilk['diet'] = 'White_beans_breastmilk' #create new colum
prod_Zucchini_breastmilk['diet'] = 'Zucchini_breastmilk' #create new colum
prod_Peache_breastmilk['diet'] = 'Peache_breastmilk' #create new colum
prod_Cashew_breastmilk['diet'] = 'Cashew_breastmilk' #create new colum
prod_Codfish_breastmilk['diet'] = 'Codfish_breastmilk' #create new colum
prod_Tuna_breastmilk['diet'] = 'Tuna_breastmilk' #create new colum
prod_Cucumber_breastmilk['diet'] = 'Cucumber_breastmilk' #create new colum
prod_Pumpkin_breastmilk['diet'] = 'Pumpkin_breastmilk' #create new colum
prod_Grape_breastmilk['diet'] = 'Grape_breastmilk' #create new colum
prod_Barley_breastmilk['diet'] = 'Barley_breastmilk' #create new colum
prod_Rice_breastmilk['diet'] = 'Rice_breastmilk' #create new colum
prod_Control_Breastmilk['diet'] = 'Control_Breastmilk' #create new colum
prod_Control_Infant_formula['diet'] = 'Control_Infant_formula' #create new colum

exchanges = pd.concat([prod_Broccoli_breastmilk,prod_Brussel_breastmilk,prod_Cabbage_breastmilk,prod_Carrot_breastmilk,prod_Cauliflower_breastmilk,
                       prod_Celery_breastmilk,prod_Eggplant_breastmilk,prod_Green_beans_breastmilk,prod_Green_capsicum_breastmilk,prod_Lettuce_breastmilk,
                       prod_Mushroom_breastmilk,prod_Onion_breastmilk,prod_Pak_choi_breastmilk,prod_Potato_breastmilk,prod_Sweetcorn_breastmilk,
                       prod_Spinach_breastmilk,prod_Squash_breastmilk,prod_Sweet_potato_breastmilk,prod_Tomato_breastmilk,prod_Yam_breastmilk,
                       prod_Apple_breastmilk,prod_Banana_breastmilk,prod_Blackcurrant_breastmilk,prod_Blueberries_breastmilk,prod_Cherry_breastmilk,
                       prod_Feijoa_breastmilk,prod_Gold_kiwifruit_breastmilk,prod_Grapefruit_breastmilk,prod_Green_kiwifruit_breastmilk,prod_Mandarin_breastmilk,
                       prod_Mango_breastmilk,prod_Melon_breastmilk,prod_Nectarine_breastmilk,prod_Orange_breastmilk,prod_Pear_breastmilk,
                       prod_Pineapple_breastmilk,prod_Plum_breastmilk,prod_Raspberries_breastmilk,prod_Strawberries_breastmilk,prod_Barley_cereal_breastmilk,
                       prod_Couscous_breastmilk,prod_Noodles_breastmilk,prod_Oat_cereal_breastmilk,prod_Pasta_breastmilk,prod_Rice_cereal_breastmilk,
                       prod_Tapioca_pudding_breastmilk,prod_White_bread_breastmilk,prod_Wholegrain_bread_breastmilk,prod_Cottage_cheese_breastmilk,prod_Eggs_breastmilk,
                       prod_Mozzarella_cheese_breastmilk,prod_Soymilk_breastmilk,prod_Tofu_breastmilk,prod_Whole_milk_breastmilk,prod_Yoghurt_breastmilk,
                       prod_Beef_breastmilk,prod_Chicken_breastmilk,prod_Lamb_breastmilk,prod_Mackerel_breastmilk,prod_Mussels_breastmilk,
                       prod_Pork_breastmilk,prod_Salmon_breastmilk,prod_Shrimp_breastmilk,prod_Turkey_breastmilk,prod_Almond_breastmilk,
                       prod_Black_beans_breastmilk,prod_Chia_breastmilk,prod_Chickpea_breastmilk,prod_Green_peas_breastmilk,prod_Hazelnut_breastmilk,
                       prod_Lentils_breastmilk,prod_Peanut_breastmilk,prod_Pecans_breastmilk,prod_Pumpkin_seed_breastmilk,prod_Red_beans_breastmilk,
                       prod_Soybean_breastmilk,prod_Split_peas_breastmilk,prod_Sunflower_seed_breastmilk,prod_White_beans_breastmilk,prod_Zucchini_breastmilk,
                       prod_Peache_breastmilk,prod_Cashew_breastmilk,prod_Codfish_breastmilk,prod_Tuna_breastmilk,prod_Cucumber_breastmilk,
                       prod_Pumpkin_breastmilk,prod_Grape_breastmilk,prod_Barley_breastmilk,prod_Rice_breastmilk,
                       prod_Control_Breastmilk,prod_Control_Infant_formula])  # merge the production rates

exchanges = pd.pivot_table(exchanges, index = ['diet'], columns = 'name', values = 'flux') #converting into matrix
exchanges.to_csv("results/exchanges.csv")
exchanges_reduced = exchanges[["Acetate", "Propionate", "Butyrate","Isobutyrate, 2-Methylpropanoate", "Isovalerate, 3-Methylbutanoate"]] #selecting the metabolites of interest
exchanges_reduced.to_csv("results/exchanges_reduced.csv")


#Plotting growth rates
import pandas as pd
import seaborn as sns

growth_Broccoli_breastmilk = pd.read_csv('results/growth_rates_Broccoli_breastmilk.csv')
growth_Brussel_breastmilk = pd.read_csv('results/growth_rates_Brussel_breastmilk.csv')
growth_Cabbage_breastmilk = pd.read_csv('results/growth_rates_Cabbage_breastmilk.csv')
growth_Carrot_breastmilk = pd.read_csv('results/growth_rates_Carrot_breastmilk.csv')
growth_Cauliflower_breastmilk = pd.read_csv('results/growth_rates_Cauliflower_breastmilk.csv')
growth_Celery_breastmilk = pd.read_csv('results/growth_rates_Celery_breastmilk.csv')
growth_Eggplant_breastmilk = pd.read_csv('results/growth_rates_Eggplant_breastmilk.csv')
growth_Green_beans_breastmilk = pd.read_csv('results/growth_rates_Green_beans_breastmilk.csv')
growth_Green_capsicum_breastmilk = pd.read_csv('results/growth_rates_Green_capsicum_breastmilk.csv')
growth_Lettuce_breastmilk = pd.read_csv('results/growth_rates_Lettuce_breastmilk.csv')
growth_Mushroom_breastmilk = pd.read_csv('results/growth_rates_Mushroom_breastmilk.csv')
growth_Onion_breastmilk = pd.read_csv('results/growth_rates_Onion_breastmilk.csv')
growth_Pak_choi_breastmilk = pd.read_csv('results/growth_rates_Pak_choi_breastmilk.csv')
growth_Potato_breastmilk = pd.read_csv('results/growth_rates_Potato_breastmilk.csv')
growth_Sweetcorn_breastmilk = pd.read_csv('results/growth_rates_Sweetcorn_breastmilk.csv')
growth_Spinach_breastmilk = pd.read_csv('results/growth_rates_Spinach_breastmilk.csv')
growth_Squash_breastmilk = pd.read_csv('results/growth_rates_Squash_breastmilk.csv')
growth_Sweet_potato_breastmilk = pd.read_csv('results/growth_rates_Sweet_potato_breastmilk.csv')
growth_Tomato_breastmilk = pd.read_csv('results/growth_rates_Tomato_breastmilk.csv')
growth_Yam_breastmilk = pd.read_csv('results/growth_rates_Yam_breastmilk.csv')
growth_Apple_breastmilk = pd.read_csv('results/growth_rates_Apple_breastmilk.csv')
growth_Banana_breastmilk = pd.read_csv('results/growth_rates_Banana_breastmilk.csv')
growth_Blackcurrant_breastmilk = pd.read_csv('results/growth_rates_Blackcurrant_breastmilk.csv')
growth_Blueberries_breastmilk = pd.read_csv('results/growth_rates_Blueberries_breastmilk.csv')
growth_Cherry_breastmilk = pd.read_csv('results/growth_rates_Cherry_breastmilk.csv')
growth_Feijoa_breastmilk = pd.read_csv('results/growth_rates_Feijoa_breastmilk.csv')
growth_Gold_kiwifruit_breastmilk = pd.read_csv('results/growth_rates_Gold_kiwifruit_breastmilk.csv')
growth_Grapefruit_breastmilk = pd.read_csv('results/growth_rates_Grapefruit_breastmilk.csv')
growth_Green_kiwifruit_breastmilk = pd.read_csv('results/growth_rates_Green_kiwifruit_breastmilk.csv')
growth_Mandarin_breastmilk = pd.read_csv('results/growth_rates_Mandarin_breastmilk.csv')
growth_Mango_breastmilk = pd.read_csv('results/growth_rates_Mango_breastmilk.csv')
growth_Melon_breastmilk = pd.read_csv('results/growth_rates_Melon_breastmilk.csv')
growth_Nectarine_breastmilk = pd.read_csv('results/growth_rates_Nectarine_breastmilk.csv')
growth_Orange_breastmilk = pd.read_csv('results/growth_rates_Orange_breastmilk.csv')
growth_Pear_breastmilk = pd.read_csv('results/growth_rates_Pear_breastmilk.csv')
growth_Pineapple_breastmilk = pd.read_csv('results/growth_rates_Pineapple_breastmilk.csv')
growth_Plum_breastmilk = pd.read_csv('results/growth_rates_Plum_breastmilk.csv')
growth_Raspberries_breastmilk = pd.read_csv('results/growth_rates_Raspberries_breastmilk.csv')
growth_Strawberries_breastmilk = pd.read_csv('results/growth_rates_Strawberries_breastmilk.csv')
growth_Barley_cereal_breastmilk = pd.read_csv('results/growth_rates_Barley_cereal_breastmilk.csv')
growth_Couscous_breastmilk = pd.read_csv('results/growth_rates_Couscous_breastmilk.csv')
growth_Noodles_breastmilk = pd.read_csv('results/growth_rates_Noodles_breastmilk.csv')
growth_Oat_cereal_breastmilk = pd.read_csv('results/growth_rates_Oat_cereal_breastmilk.csv')
growth_Pasta_breastmilk = pd.read_csv('results/growth_rates_Pasta_breastmilk.csv')
growth_Rice_cereal_breastmilk = pd.read_csv('results/growth_rates_Rice_cereal_breastmilk.csv')
growth_Tapioca_pudding_breastmilk = pd.read_csv('results/growth_rates_Tapioca_pudding_breastmilk.csv')
growth_White_bread_breastmilk = pd.read_csv('results/growth_rates_White_bread_breastmilk.csv')
growth_Wholegrain_bread_breastmilk = pd.read_csv('results/growth_rates_Wholegrain_bread_breastmilk.csv')
growth_Cottage_cheese_breastmilk = pd.read_csv('results/growth_rates_Cottage_cheese_breastmilk.csv')
growth_Eggs_breastmilk = pd.read_csv('results/growth_rates_Eggs_breastmilk.csv')
growth_Mozzarella_cheese_breastmilk = pd.read_csv('results/growth_rates_Mozzarella_cheese_breastmilk.csv')
growth_Soymilk_breastmilk = pd.read_csv('results/growth_rates_Soymilk_breastmilk.csv')
growth_Tofu_breastmilk = pd.read_csv('results/growth_rates_Tofu_breastmilk.csv')
growth_Whole_milk_breastmilk = pd.read_csv('results/growth_rates_Whole_milk_breastmilk.csv')
growth_Yoghurt_breastmilk = pd.read_csv('results/growth_rates_Yoghurt_breastmilk.csv')
growth_Beef_breastmilk = pd.read_csv('results/growth_rates_Beef_breastmilk.csv')
growth_Chicken_breastmilk = pd.read_csv('results/growth_rates_Chicken_breastmilk.csv')
growth_Lamb_breastmilk = pd.read_csv('results/growth_rates_Lamb_breastmilk.csv')
growth_Mackerel_breastmilk = pd.read_csv('results/growth_rates_Mackerel_breastmilk.csv')
growth_Mussels_breastmilk = pd.read_csv('results/growth_rates_Mussels_breastmilk.csv')
growth_Pork_breastmilk = pd.read_csv('results/growth_rates_Pork_breastmilk.csv')
growth_Salmon_breastmilk = pd.read_csv('results/growth_rates_Salmon_breastmilk.csv')
growth_Shrimp_breastmilk = pd.read_csv('results/growth_rates_Shrimp_breastmilk.csv')
growth_Turkey_breastmilk = pd.read_csv('results/growth_rates_Turkey_breastmilk.csv')
growth_Almond_breastmilk = pd.read_csv('results/growth_rates_Almond_breastmilk.csv')
growth_Black_beans_breastmilk = pd.read_csv('results/growth_rates_Black_beans_breastmilk.csv')
growth_Chia_breastmilk = pd.read_csv('results/growth_rates_Chia_breastmilk.csv')
growth_Chickpea_breastmilk = pd.read_csv('results/growth_rates_Chickpea_breastmilk.csv')
growth_Green_peas_breastmilk = pd.read_csv('results/growth_rates_Green_peas_breastmilk.csv')
growth_Hazelnut_breastmilk = pd.read_csv('results/growth_rates_Hazelnut_breastmilk.csv')
growth_Lentils_breastmilk = pd.read_csv('results/growth_rates_Lentils_breastmilk.csv')
growth_Peanut_breastmilk = pd.read_csv('results/growth_rates_Peanut_breastmilk.csv')
growth_Pecans_breastmilk = pd.read_csv('results/growth_rates_Pecans_breastmilk.csv')
growth_Pumpkin_seed_breastmilk = pd.read_csv('results/growth_rates_Pumpkin_seed_breastmilk.csv')
growth_Red_beans_breastmilk = pd.read_csv('results/growth_rates_Red_beans_breastmilk.csv')
growth_Soybean_breastmilk = pd.read_csv('results/growth_rates_Soybean_breastmilk.csv')
growth_Split_peas_breastmilk = pd.read_csv('results/growth_rates_Split_peas_breastmilk.csv')
growth_Sunflower_seed_breastmilk = pd.read_csv('results/growth_rates_Sunflower_seed_breastmilk.csv')
growth_White_beans_breastmilk = pd.read_csv('results/growth_rates_White_beans_breastmilk.csv')
growth_Zucchini_breastmilk = pd.read_csv('results/growth_rates_Zucchini_breastmilk.csv')
growth_Peache_breastmilk = pd.read_csv('results/growth_rates_Peache_breastmilk.csv')
growth_Cashew_breastmilk = pd.read_csv('results/growth_rates_Cashew_breastmilk.csv')
growth_Codfish_breastmilk = pd.read_csv('results/growth_rates_Codfish_breastmilk.csv')
growth_Tuna_breastmilk = pd.read_csv('results/growth_rates_Tuna_breastmilk.csv')
growth_Cucumber_breastmilk = pd.read_csv('results/growth_rates_Cucumber_breastmilk.csv')
growth_Pumpkin_breastmilk = pd.read_csv('results/growth_rates_Pumpkin_breastmilk.csv')
growth_Grape_breastmilk = pd.read_csv('results/growth_rates_Grape_breastmilk.csv')
growth_Barley_breastmilk = pd.read_csv('results/growth_rates_Barley_breastmilk.csv')
growth_Rice_breastmilk = pd.read_csv('results/growth_rates_Rice_breastmilk.csv')
growth_Control_Breastmilk = pd.read_csv('results/growth_rates_Control_Breastmilk.csv')
growth_Control_Infant_formula = pd.read_csv('results/growth_rates_Control_Infant_formula.csv')

growth_Broccoli_breastmilk['diet'] = 'Broccoli_breastmilk' 
growth_Brussel_breastmilk['diet'] = 'Brussel_breastmilk' 
growth_Cabbage_breastmilk['diet'] = 'Cabbage_breastmilk' 
growth_Carrot_breastmilk['diet'] = 'Carrot_breastmilk' 
growth_Cauliflower_breastmilk['diet'] = 'Cauliflower_breastmilk' 
growth_Celery_breastmilk['diet'] = 'Celery_breastmilk' 
growth_Eggplant_breastmilk['diet'] = 'Eggplant_breastmilk' 
growth_Green_beans_breastmilk['diet'] = 'Green_beans_breastmilk' 
growth_Green_capsicum_breastmilk['diet'] = 'Green_capsicum_breastmilk' 
growth_Lettuce_breastmilk['diet'] = 'Lettuce_breastmilk' 
growth_Mushroom_breastmilk['diet'] = 'Mushroom_breastmilk' 
growth_Onion_breastmilk['diet'] = 'Onion_breastmilk' 
growth_Pak_choi_breastmilk['diet'] = 'Pak_choi_breastmilk' 
growth_Potato_breastmilk['diet'] = 'Potato_breastmilk' 
growth_Sweetcorn_breastmilk['diet'] = 'Sweetcorn_breastmilk' 
growth_Spinach_breastmilk['diet'] = 'Spinach_breastmilk' 
growth_Squash_breastmilk['diet'] = 'Squash_breastmilk' 
growth_Sweet_potato_breastmilk['diet'] = 'Sweet_potato_breastmilk' 
growth_Tomato_breastmilk['diet'] = 'Tomato_breastmilk' 
growth_Yam_breastmilk['diet'] = 'Yam_breastmilk' 
growth_Apple_breastmilk['diet'] = 'Apple_breastmilk' 
growth_Banana_breastmilk['diet'] = 'Banana_breastmilk' 
growth_Blackcurrant_breastmilk['diet'] = 'Blackcurrant_breastmilk' 
growth_Blueberries_breastmilk['diet'] = 'Blueberries_breastmilk' 
growth_Cherry_breastmilk['diet'] = 'Cherry_breastmilk' 
growth_Feijoa_breastmilk['diet'] = 'Feijoa_breastmilk' 
growth_Gold_kiwifruit_breastmilk['diet'] = 'Gold_kiwifruit_breastmilk' 
growth_Grapefruit_breastmilk['diet'] = 'Grapefruit_breastmilk' 
growth_Green_kiwifruit_breastmilk['diet'] = 'Green_kiwifruit_breastmilk' 
growth_Mandarin_breastmilk['diet'] = 'Mandarin_breastmilk' 
growth_Mango_breastmilk['diet'] = 'Mango_breastmilk' 
growth_Melon_breastmilk['diet'] = 'Melon_breastmilk' 
growth_Nectarine_breastmilk['diet'] = 'Nectarine_breastmilk' 
growth_Orange_breastmilk['diet'] = 'Orange_breastmilk' 
growth_Pear_breastmilk['diet'] = 'Pear_breastmilk' 
growth_Pineapple_breastmilk['diet'] = 'Pineapple_breastmilk' 
growth_Plum_breastmilk['diet'] = 'Plum_breastmilk' 
growth_Raspberries_breastmilk['diet'] = 'Raspberries_breastmilk' 
growth_Strawberries_breastmilk['diet'] = 'Strawberries_breastmilk' 
growth_Barley_cereal_breastmilk['diet'] = 'Barley_cereal_breastmilk' 
growth_Couscous_breastmilk['diet'] = 'Couscous_breastmilk' 
growth_Noodles_breastmilk['diet'] = 'Noodles_breastmilk' 
growth_Oat_cereal_breastmilk['diet'] = 'Oat_cereal_breastmilk' 
growth_Pasta_breastmilk['diet'] = 'Pasta_breastmilk' 
growth_Rice_cereal_breastmilk['diet'] = 'Rice_cereal_breastmilk' 
growth_Tapioca_pudding_breastmilk['diet'] = 'Tapioca_pudding_breastmilk' 
growth_White_bread_breastmilk['diet'] = 'White_bread_breastmilk' 
growth_Wholegrain_bread_breastmilk['diet'] = 'Wholegrain_bread_breastmilk' 
growth_Cottage_cheese_breastmilk['diet'] = 'Cottage_cheese_breastmilk' 
growth_Eggs_breastmilk['diet'] = 'Eggs_breastmilk' 
growth_Mozzarella_cheese_breastmilk['diet'] = 'Mozzarella_cheese_breastmilk' 
growth_Soymilk_breastmilk['diet'] = 'Soymilk_breastmilk' 
growth_Tofu_breastmilk['diet'] = 'Tofu_breastmilk' 
growth_Whole_milk_breastmilk['diet'] = 'Whole_milk_breastmilk' 
growth_Yoghurt_breastmilk['diet'] = 'Yoghurt_breastmilk' 
growth_Beef_breastmilk['diet'] = 'Beef_breastmilk' 
growth_Chicken_breastmilk['diet'] = 'Chicken_breastmilk' 
growth_Lamb_breastmilk['diet'] = 'Lamb_breastmilk' 
growth_Mackerel_breastmilk['diet'] = 'Mackerel_breastmilk' 
growth_Mussels_breastmilk['diet'] = 'Mussels_breastmilk' 
growth_Pork_breastmilk['diet'] = 'Pork_breastmilk' 
growth_Salmon_breastmilk['diet'] = 'Salmon_breastmilk' 
growth_Shrimp_breastmilk['diet'] = 'Shrimp_breastmilk' 
growth_Turkey_breastmilk['diet'] = 'Turkey_breastmilk' 
growth_Almond_breastmilk['diet'] = 'Almond_breastmilk' 
growth_Black_beans_breastmilk['diet'] = 'Black_beans_breastmilk' 
growth_Chia_breastmilk['diet'] = 'Chia_breastmilk' 
growth_Chickpea_breastmilk['diet'] = 'Chickpea_breastmilk' 
growth_Green_peas_breastmilk['diet'] = 'Green_peas_breastmilk' 
growth_Hazelnut_breastmilk['diet'] = 'Hazelnut_breastmilk' 
growth_Lentils_breastmilk['diet'] = 'Lentils_breastmilk' 
growth_Peanut_breastmilk['diet'] = 'Peanut_breastmilk' 
growth_Pecans_breastmilk['diet'] = 'Pecans_breastmilk' 
growth_Pumpkin_seed_breastmilk['diet'] = 'Pumpkin_seed_breastmilk' 
growth_Red_beans_breastmilk['diet'] = 'Red_beans_breastmilk' 
growth_Soybean_breastmilk['diet'] = 'Soybean_breastmilk' 
growth_Split_peas_breastmilk['diet'] = 'Split_peas_breastmilk' 
growth_Sunflower_seed_breastmilk['diet'] = 'Sunflower_seed_breastmilk' 
growth_White_beans_breastmilk['diet'] = 'White_beans_breastmilk' 
growth_Zucchini_breastmilk['diet'] = 'Zucchini_breastmilk' 
growth_Peache_breastmilk['diet'] = 'Peache_breastmilk' 
growth_Cashew_breastmilk['diet'] = 'Cashew_breastmilk' 
growth_Codfish_breastmilk['diet'] = 'Codfish_breastmilk' 
growth_Tuna_breastmilk['diet'] = 'Tuna_breastmilk' 
growth_Cucumber_breastmilk['diet'] = 'Cucumber_breastmilk' 
growth_Pumpkin_breastmilk['diet'] = 'Pumpkin_breastmilk' 
growth_Grape_breastmilk['diet'] = 'Grape_breastmilk' 
growth_Barley_breastmilk['diet'] = 'Barley_breastmilk' 
growth_Rice_breastmilk['diet'] = 'Rice_breastmilk' 
growth_Control_Breastmilk['diet'] = 'Control_Breastmilk' 
growth_Control_Infant_formula['diet'] = 'Control_Infant_formula' 

growth_rates = pd.concat([growth_Broccoli_breastmilk,growth_Brussel_breastmilk,growth_Cabbage_breastmilk,growth_Carrot_breastmilk,growth_Cauliflower_breastmilk,
                          growth_Celery_breastmilk,growth_Eggplant_breastmilk,growth_Green_beans_breastmilk,growth_Green_capsicum_breastmilk,growth_Lettuce_breastmilk,
                          growth_Mushroom_breastmilk,growth_Onion_breastmilk,growth_Pak_choi_breastmilk,growth_Potato_breastmilk,growth_Sweetcorn_breastmilk,
                          growth_Spinach_breastmilk,growth_Squash_breastmilk,growth_Sweet_potato_breastmilk,growth_Tomato_breastmilk,growth_Yam_breastmilk,
                          growth_Apple_breastmilk,growth_Banana_breastmilk,growth_Blackcurrant_breastmilk,growth_Blueberries_breastmilk,growth_Cherry_breastmilk,
                          growth_Feijoa_breastmilk,growth_Gold_kiwifruit_breastmilk,growth_Grapefruit_breastmilk,growth_Green_kiwifruit_breastmilk,growth_Mandarin_breastmilk,
                          growth_Mango_breastmilk,growth_Melon_breastmilk,growth_Nectarine_breastmilk,growth_Orange_breastmilk,growth_Pear_breastmilk,
                          growth_Pineapple_breastmilk,growth_Plum_breastmilk,growth_Raspberries_breastmilk,growth_Strawberries_breastmilk,growth_Barley_cereal_breastmilk,
                          growth_Couscous_breastmilk,growth_Noodles_breastmilk,growth_Oat_cereal_breastmilk,growth_Pasta_breastmilk,growth_Rice_cereal_breastmilk,
                          growth_Tapioca_pudding_breastmilk,growth_White_bread_breastmilk,growth_Wholegrain_bread_breastmilk,growth_Cottage_cheese_breastmilk,growth_Eggs_breastmilk,
                          growth_Mozzarella_cheese_breastmilk,growth_Soymilk_breastmilk,growth_Tofu_breastmilk,growth_Whole_milk_breastmilk,growth_Yoghurt_breastmilk,
                          growth_Beef_breastmilk,growth_Chicken_breastmilk,growth_Lamb_breastmilk,growth_Mackerel_breastmilk,growth_Mussels_breastmilk,
                          growth_Pork_breastmilk,growth_Salmon_breastmilk,growth_Shrimp_breastmilk,growth_Turkey_breastmilk,growth_Almond_breastmilk,
                          growth_Black_beans_breastmilk,growth_Chia_breastmilk,growth_Chickpea_breastmilk,growth_Green_peas_breastmilk,growth_Hazelnut_breastmilk,
                          growth_Lentils_breastmilk,growth_Peanut_breastmilk,growth_Pecans_breastmilk,growth_Pumpkin_seed_breastmilk,growth_Red_beans_breastmilk,
                          growth_Soybean_breastmilk,growth_Split_peas_breastmilk,growth_Sunflower_seed_breastmilk,growth_White_beans_breastmilk,growth_Zucchini_breastmilk,
                          growth_Peache_breastmilk,growth_Cashew_breastmilk,growth_Codfish_breastmilk,growth_Tuna_breastmilk,growth_Cucumber_breastmilk,
                          growth_Pumpkin_breastmilk,growth_Grape_breastmilk,growth_Barley_breastmilk,growth_Rice_breastmilk,
                          growth_Control_Breastmilk,growth_Control_Infant_formula])  # merging the growth rates
growth_rates = pd.pivot_table(growth_rates, index = ["diet"], columns = "taxon", values = "growth_rate") #pivoting the table
growth_rates.to_csv("results/growth_rates.csv")






