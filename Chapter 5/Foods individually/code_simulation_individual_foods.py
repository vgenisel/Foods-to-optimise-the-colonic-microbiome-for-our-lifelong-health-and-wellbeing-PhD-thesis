##Simulating NZ foods on the microbiome of weaning infants
#Foods designed for infants at 6 months (608 kcal/day)
#Daily fluxes, CPLEX 22.1, AGORA2, genus
#89 NZ single food combinations + 2 controls (only breastmilk and only infant formula)

#07/08/23

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

Broccoli = pd.read_csv('data/Broccoli.csv')
Brussel = pd.read_csv('data/Brussel.csv')
Cabbage = pd.read_csv('data/Cabbage.csv')
Carrot = pd.read_csv('data/Carrot.csv')
Cauliflower = pd.read_csv('data/Cauliflower.csv')
Celery = pd.read_csv('data/Celery.csv')
Eggplant = pd.read_csv('data/Eggplant.csv')
Green_beans = pd.read_csv('data/Green_beans.csv')
Green_capsicum = pd.read_csv('data/Green_capsicum.csv')
Lettuce = pd.read_csv('data/Lettuce.csv')
Mushroom = pd.read_csv('data/Mushroom.csv')
Onion = pd.read_csv('data/Onion.csv')
Pak_choi = pd.read_csv('data/Pak_choi.csv')
Potato = pd.read_csv('data/Potato.csv')
Sweetcorn = pd.read_csv('data/Sweetcorn.csv')
Spinach = pd.read_csv('data/Spinach.csv')
Squash = pd.read_csv('data/Squash.csv')
Sweet_potato = pd.read_csv('data/Sweet_potato.csv')
Tomato = pd.read_csv('data/Tomato.csv')
Yam = pd.read_csv('data/Yam.csv')
Apple = pd.read_csv('data/Apple.csv')
Banana = pd.read_csv('data/Banana.csv')
Blackcurrant = pd.read_csv('data/Blackcurrant.csv')
Blueberries = pd.read_csv('data/Blueberries.csv')
Cherry = pd.read_csv('data/Cherry.csv')
Feijoa = pd.read_csv('data/Feijoa.csv')
Gold_kiwifruit = pd.read_csv('data/Gold_kiwifruit.csv')
Grapefruit = pd.read_csv('data/Grapefruit.csv')
Green_kiwifruit = pd.read_csv('data/Green_kiwifruit.csv')
Mandarin = pd.read_csv('data/Mandarin.csv')
Mango = pd.read_csv('data/Mango.csv')
Melon = pd.read_csv('data/Melon.csv')
Nectarine = pd.read_csv('data/Nectarine.csv')
Orange = pd.read_csv('data/Orange.csv')
Pear = pd.read_csv('data/Pear.csv')
Pineapple = pd.read_csv('data/Pineapple.csv')
Plum = pd.read_csv('data/Plum.csv')
Raspberries = pd.read_csv('data/Raspberries.csv')
Strawberries = pd.read_csv('data/Strawberries.csv')
Barley_cereal = pd.read_csv('data/Barley_cereal.csv')
Couscous = pd.read_csv('data/Couscous.csv')
Noodles = pd.read_csv('data/Noodles.csv')
Oat_cereal = pd.read_csv('data/Oat_cereal.csv')
Pasta = pd.read_csv('data/Pasta.csv')
Rice_cereal = pd.read_csv('data/Rice_cereal.csv')
Tapioca_pudding = pd.read_csv('data/Tapioca_pudding.csv')
White_bread = pd.read_csv('data/White_bread.csv')
Wholegrain_bread = pd.read_csv('data/Wholegrain_bread.csv')
Cottage_cheese = pd.read_csv('data/Cottage_cheese.csv')
Eggs = pd.read_csv('data/Eggs.csv')
Mozzarella_cheese = pd.read_csv('data/Mozzarella_cheese.csv')
Soymilk = pd.read_csv('data/Soymilk.csv')
Tofu = pd.read_csv('data/Tofu.csv')
Whole_milk = pd.read_csv('data/Whole_milk.csv')
Yoghurt = pd.read_csv('data/Yoghurt.csv')
Beef = pd.read_csv('data/Beef.csv')
Chicken = pd.read_csv('data/Chicken.csv')
Lamb = pd.read_csv('data/Lamb.csv')
Mackerel = pd.read_csv('data/Mackerel.csv')
Mussels = pd.read_csv('data/Mussels.csv')
Pork = pd.read_csv('data/Pork.csv')
Salmon = pd.read_csv('data/Salmon.csv')
Shrimp = pd.read_csv('data/Shrimp.csv')
Turkey = pd.read_csv('data/Turkey.csv')
Almond = pd.read_csv('data/Almond.csv')
Black_beans = pd.read_csv('data/Black_beans.csv')
Chia = pd.read_csv('data/Chia.csv')
Chickpea = pd.read_csv('data/Chickpea.csv')
Green_peas = pd.read_csv('data/Green_peas.csv')
Hazelnut = pd.read_csv('data/Hazelnut.csv')
Lentils = pd.read_csv('data/Lentils.csv')
Peanut = pd.read_csv('data/Peanut.csv')
Pecans = pd.read_csv('data/Pecans.csv')
Pumpkin_seed = pd.read_csv('data/Pumpkin_seed.csv')
Red_beans = pd.read_csv('data/Red_beans.csv')
Soybean = pd.read_csv('data/Soybean.csv')
Split_peas = pd.read_csv('data/Split_peas.csv')
Sunflower_seed = pd.read_csv('data/Sunflower_seed.csv')
White_beans = pd.read_csv('data/White_beans.csv')
Zucchini = pd.read_csv('data/Zucchini.csv')
Peache = pd.read_csv('data/Peache.csv')
Cashew = pd.read_csv('data/Cashew.csv')
Codfish = pd.read_csv('data/Codfish.csv')
Tuna = pd.read_csv('data/Tuna.csv')
Cucumber = pd.read_csv('data/Cucumber.csv')
Pumpkin = pd.read_csv('data/Pumpkin.csv')
Grape = pd.read_csv('data/Grape.csv')
Barley = pd.read_csv('data/Barley.csv')
Rice = pd.read_csv('data/Rice.csv')
Control_Breastmilk = pd.read_csv('data/Breastmilk.csv') #control
Control_Infant_formula = pd.read_csv('data/Infant_formula.csv') #control

#Choosing the tradeoff
#normally 0.3-0.6 works good
#largest tradeoff that allows the majority of the bacteria to grow 
#compromise between individual and cooperative growth
from micom.workflows import tradeoff
from micom.viz import plot_tradeoff

tradeoff_Broccoli = tradeoff(manifest, model_folder="models_cplex", medium=Broccoli, threads=14) 
plot_tradeoff(tradeoff_Broccoli, filename="results/tradeoff_Broccoli.html")
tradeoff_Brussel = tradeoff(manifest, model_folder="models_cplex", medium=Brussel, threads=14) 
plot_tradeoff(tradeoff_Brussel, filename="results/tradeoff_Brussel.html")
tradeoff_Cabbage = tradeoff(manifest, model_folder="models_cplex", medium=Cabbage, threads=14) 
plot_tradeoff(tradeoff_Cabbage, filename="results/tradeoff_Cabbage.html")
tradeoff_Carrot = tradeoff(manifest, model_folder="models_cplex", medium=Carrot, threads=14) 
plot_tradeoff(tradeoff_Carrot, filename="results/tradeoff_Carrot.html")
tradeoff_Cauliflower = tradeoff(manifest, model_folder="models_cplex", medium=Cauliflower, threads=14) 
plot_tradeoff(tradeoff_Cauliflower, filename="results/tradeoff_Cauliflower.html")
tradeoff_Celery = tradeoff(manifest, model_folder="models_cplex", medium=Celery, threads=14) 
plot_tradeoff(tradeoff_Celery, filename="results/tradeoff_Celery.html")
tradeoff_Eggplant = tradeoff(manifest, model_folder="models_cplex", medium=Eggplant, threads=14) 
plot_tradeoff(tradeoff_Eggplant, filename="results/tradeoff_Eggplant.html")
tradeoff_Green_beans = tradeoff(manifest, model_folder="models_cplex", medium=Green_beans, threads=14) 
plot_tradeoff(tradeoff_Green_beans, filename="results/tradeoff_Green_beans.html")
tradeoff_Green_capsicum = tradeoff(manifest, model_folder="models_cplex", medium=Green_capsicum, threads=14) 
plot_tradeoff(tradeoff_Green_capsicum, filename="results/tradeoff_Green_capsicum.html")
tradeoff_Lettuce = tradeoff(manifest, model_folder="models_cplex", medium=Lettuce, threads=14) 
plot_tradeoff(tradeoff_Lettuce, filename="results/tradeoff_Lettuce.html")
tradeoff_Mushroom = tradeoff(manifest, model_folder="models_cplex", medium=Mushroom, threads=14) 
plot_tradeoff(tradeoff_Mushroom, filename="results/tradeoff_Mushroom.html")
tradeoff_Onion = tradeoff(manifest, model_folder="models_cplex", medium=Onion, threads=14) 
plot_tradeoff(tradeoff_Onion, filename="results/tradeoff_Onion.html")
tradeoff_Pak_choi = tradeoff(manifest, model_folder="models_cplex", medium=Pak_choi, threads=14) 
plot_tradeoff(tradeoff_Pak_choi, filename="results/tradeoff_Pak_choi.html")
tradeoff_Potato = tradeoff(manifest, model_folder="models_cplex", medium=Potato, threads=14) 
plot_tradeoff(tradeoff_Potato, filename="results/tradeoff_Potato.html")
tradeoff_Sweetcorn = tradeoff(manifest, model_folder="models_cplex", medium=Sweetcorn, threads=14) 
plot_tradeoff(tradeoff_Sweetcorn, filename="results/tradeoff_Sweetcorn.html")
tradeoff_Spinach = tradeoff(manifest, model_folder="models_cplex", medium=Spinach, threads=14) 
plot_tradeoff(tradeoff_Spinach, filename="results/tradeoff_Spinach.html")
tradeoff_Squash = tradeoff(manifest, model_folder="models_cplex", medium=Squash, threads=14) 
plot_tradeoff(tradeoff_Squash, filename="results/tradeoff_Squash.html")
tradeoff_Sweet_potato = tradeoff(manifest, model_folder="models_cplex", medium=Sweet_potato, threads=14) 
plot_tradeoff(tradeoff_Sweet_potato, filename="results/tradeoff_Sweet_potato.html")
tradeoff_Tomato = tradeoff(manifest, model_folder="models_cplex", medium=Tomato, threads=14) 
plot_tradeoff(tradeoff_Tomato, filename="results/tradeoff_Tomato.html")
tradeoff_Yam = tradeoff(manifest, model_folder="models_cplex", medium=Yam, threads=14) 
plot_tradeoff(tradeoff_Yam, filename="results/tradeoff_Yam.html")
tradeoff_Apple = tradeoff(manifest, model_folder="models_cplex", medium=Apple, threads=14) 
plot_tradeoff(tradeoff_Apple, filename="results/tradeoff_Apple.html")
tradeoff_Banana = tradeoff(manifest, model_folder="models_cplex", medium=Banana, threads=14) 
plot_tradeoff(tradeoff_Banana, filename="results/tradeoff_Banana.html")
tradeoff_Blackcurrant = tradeoff(manifest, model_folder="models_cplex", medium=Blackcurrant, threads=14) 
plot_tradeoff(tradeoff_Blackcurrant, filename="results/tradeoff_Blackcurrant.html")
tradeoff_Blueberries = tradeoff(manifest, model_folder="models_cplex", medium=Blueberries, threads=14) 
plot_tradeoff(tradeoff_Blueberries, filename="results/tradeoff_Blueberries.html")
tradeoff_Cherry = tradeoff(manifest, model_folder="models_cplex", medium=Cherry, threads=14) 
plot_tradeoff(tradeoff_Cherry, filename="results/tradeoff_Cherry.html")
tradeoff_Feijoa = tradeoff(manifest, model_folder="models_cplex", medium=Feijoa, threads=14) 
plot_tradeoff(tradeoff_Feijoa, filename="results/tradeoff_Feijoa.html")
tradeoff_Gold_kiwifruit = tradeoff(manifest, model_folder="models_cplex", medium=Gold_kiwifruit, threads=14) 
plot_tradeoff(tradeoff_Gold_kiwifruit, filename="results/tradeoff_Gold_kiwifruit.html")
tradeoff_Grapefruit = tradeoff(manifest, model_folder="models_cplex", medium=Grapefruit, threads=14) 
plot_tradeoff(tradeoff_Grapefruit, filename="results/tradeoff_Grapefruit.html")
tradeoff_Green_kiwifruit = tradeoff(manifest, model_folder="models_cplex", medium=Green_kiwifruit, threads=14) 
plot_tradeoff(tradeoff_Green_kiwifruit, filename="results/tradeoff_Green_kiwifruit.html")
tradeoff_Mandarin = tradeoff(manifest, model_folder="models_cplex", medium=Mandarin, threads=14) 
plot_tradeoff(tradeoff_Mandarin, filename="results/tradeoff_Mandarin.html")
tradeoff_Mango = tradeoff(manifest, model_folder="models_cplex", medium=Mango, threads=14) 
plot_tradeoff(tradeoff_Mango, filename="results/tradeoff_Mango.html")
tradeoff_Melon = tradeoff(manifest, model_folder="models_cplex", medium=Melon, threads=14) 
plot_tradeoff(tradeoff_Melon, filename="results/tradeoff_Melon.html")
tradeoff_Nectarine = tradeoff(manifest, model_folder="models_cplex", medium=Nectarine, threads=14) 
plot_tradeoff(tradeoff_Nectarine, filename="results/tradeoff_Nectarine.html")
tradeoff_Orange = tradeoff(manifest, model_folder="models_cplex", medium=Orange, threads=14) 
plot_tradeoff(tradeoff_Orange, filename="results/tradeoff_Orange.html")
tradeoff_Pear = tradeoff(manifest, model_folder="models_cplex", medium=Pear, threads=14) 
plot_tradeoff(tradeoff_Pear, filename="results/tradeoff_Pear.html")
tradeoff_Pineapple = tradeoff(manifest, model_folder="models_cplex", medium=Pineapple, threads=14) 
plot_tradeoff(tradeoff_Pineapple, filename="results/tradeoff_Pineapple.html")
tradeoff_Plum = tradeoff(manifest, model_folder="models_cplex", medium=Plum, threads=14) 
plot_tradeoff(tradeoff_Plum, filename="results/tradeoff_Plum.html")
tradeoff_Raspberries = tradeoff(manifest, model_folder="models_cplex", medium=Raspberries, threads=14) 
plot_tradeoff(tradeoff_Raspberries, filename="results/tradeoff_Raspberries.html")
tradeoff_Strawberries = tradeoff(manifest, model_folder="models_cplex", medium=Strawberries, threads=14) 
plot_tradeoff(tradeoff_Strawberries, filename="results/tradeoff_Strawberries.html")
tradeoff_Barley_cereal = tradeoff(manifest, model_folder="models_cplex", medium=Barley_cereal, threads=14) 
plot_tradeoff(tradeoff_Barley_cereal, filename="results/tradeoff_Barley_cereal.html")
tradeoff_Couscous = tradeoff(manifest, model_folder="models_cplex", medium=Couscous, threads=14) 
plot_tradeoff(tradeoff_Couscous, filename="results/tradeoff_Couscous.html")
tradeoff_Noodles = tradeoff(manifest, model_folder="models_cplex", medium=Noodles, threads=14) 
plot_tradeoff(tradeoff_Noodles, filename="results/tradeoff_Noodles.html")
tradeoff_Oat_cereal = tradeoff(manifest, model_folder="models_cplex", medium=Oat_cereal, threads=14) 
plot_tradeoff(tradeoff_Oat_cereal, filename="results/tradeoff_Oat_cereal.html")
tradeoff_Pasta = tradeoff(manifest, model_folder="models_cplex", medium=Pasta, threads=14) 
plot_tradeoff(tradeoff_Pasta, filename="results/tradeoff_Pasta.html")
tradeoff_Rice_cereal = tradeoff(manifest, model_folder="models_cplex", medium=Rice_cereal, threads=14) 
plot_tradeoff(tradeoff_Rice_cereal, filename="results/tradeoff_Rice_cereal.html")
tradeoff_Tapioca_pudding = tradeoff(manifest, model_folder="models_cplex", medium=Tapioca_pudding, threads=14) 
plot_tradeoff(tradeoff_Tapioca_pudding, filename="results/tradeoff_Tapioca_pudding.html")
tradeoff_White_bread = tradeoff(manifest, model_folder="models_cplex", medium=White_bread, threads=14) 
plot_tradeoff(tradeoff_White_bread, filename="results/tradeoff_White_bread.html")
tradeoff_Wholegrain_bread = tradeoff(manifest, model_folder="models_cplex", medium=Wholegrain_bread, threads=14) 
plot_tradeoff(tradeoff_Wholegrain_bread, filename="results/tradeoff_Wholegrain_bread.html")
tradeoff_Cottage_cheese = tradeoff(manifest, model_folder="models_cplex", medium=Cottage_cheese, threads=14) 
plot_tradeoff(tradeoff_Cottage_cheese, filename="results/tradeoff_Cottage_cheese.html")
tradeoff_Eggs = tradeoff(manifest, model_folder="models_cplex", medium=Eggs, threads=14) 
plot_tradeoff(tradeoff_Eggs, filename="results/tradeoff_Eggs.html")
tradeoff_Mozzarella_cheese = tradeoff(manifest, model_folder="models_cplex", medium=Mozzarella_cheese, threads=14) 
plot_tradeoff(tradeoff_Mozzarella_cheese, filename="results/tradeoff_Mozzarella_cheese.html")
tradeoff_Soymilk = tradeoff(manifest, model_folder="models_cplex", medium=Soymilk, threads=14) 
plot_tradeoff(tradeoff_Soymilk, filename="results/tradeoff_Soymilk.html")
tradeoff_Tofu = tradeoff(manifest, model_folder="models_cplex", medium=Tofu, threads=14) 
plot_tradeoff(tradeoff_Tofu, filename="results/tradeoff_Tofu.html")
tradeoff_Whole_milk = tradeoff(manifest, model_folder="models_cplex", medium=Whole_milk, threads=14) 
plot_tradeoff(tradeoff_Whole_milk, filename="results/tradeoff_Whole_milk.html")
tradeoff_Yoghurt = tradeoff(manifest, model_folder="models_cplex", medium=Yoghurt, threads=14) 
plot_tradeoff(tradeoff_Yoghurt, filename="results/tradeoff_Yoghurt.html")
tradeoff_Beef = tradeoff(manifest, model_folder="models_cplex", medium=Beef, threads=14) 
plot_tradeoff(tradeoff_Beef, filename="results/tradeoff_Beef.html")
tradeoff_Chicken = tradeoff(manifest, model_folder="models_cplex", medium=Chicken, threads=14) 
plot_tradeoff(tradeoff_Chicken, filename="results/tradeoff_Chicken.html")
tradeoff_Lamb = tradeoff(manifest, model_folder="models_cplex", medium=Lamb, threads=14) 
plot_tradeoff(tradeoff_Lamb, filename="results/tradeoff_Lamb.html")
tradeoff_Mackerel = tradeoff(manifest, model_folder="models_cplex", medium=Mackerel, threads=14) 
plot_tradeoff(tradeoff_Mackerel, filename="results/tradeoff_Mackerel.html")
tradeoff_Mussels = tradeoff(manifest, model_folder="models_cplex", medium=Mussels, threads=14) 
plot_tradeoff(tradeoff_Mussels, filename="results/tradeoff_Mussels.html")
tradeoff_Pork = tradeoff(manifest, model_folder="models_cplex", medium=Pork, threads=14) 
plot_tradeoff(tradeoff_Pork, filename="results/tradeoff_Pork.html")
tradeoff_Salmon = tradeoff(manifest, model_folder="models_cplex", medium=Salmon, threads=14) 
plot_tradeoff(tradeoff_Salmon, filename="results/tradeoff_Salmon.html")
tradeoff_Shrimp = tradeoff(manifest, model_folder="models_cplex", medium=Shrimp, threads=14) 
plot_tradeoff(tradeoff_Shrimp, filename="results/tradeoff_Shrimp.html")
tradeoff_Turkey = tradeoff(manifest, model_folder="models_cplex", medium=Turkey, threads=14) 
plot_tradeoff(tradeoff_Turkey, filename="results/tradeoff_Turkey.html")
tradeoff_Almond = tradeoff(manifest, model_folder="models_cplex", medium=Almond, threads=14) 
plot_tradeoff(tradeoff_Almond, filename="results/tradeoff_Almond.html")
tradeoff_Black_beans = tradeoff(manifest, model_folder="models_cplex", medium=Black_beans, threads=14) 
plot_tradeoff(tradeoff_Black_beans, filename="results/tradeoff_Black_beans.html")
tradeoff_Chia = tradeoff(manifest, model_folder="models_cplex", medium=Chia, threads=14) 
plot_tradeoff(tradeoff_Chia, filename="results/tradeoff_Chia.html")
tradeoff_Chickpea = tradeoff(manifest, model_folder="models_cplex", medium=Chickpea, threads=14) 
plot_tradeoff(tradeoff_Chickpea, filename="results/tradeoff_Chickpea.html")
tradeoff_Green_peas = tradeoff(manifest, model_folder="models_cplex", medium=Green_peas, threads=14) 
plot_tradeoff(tradeoff_Green_peas, filename="results/tradeoff_Green_peas.html")
tradeoff_Hazelnut = tradeoff(manifest, model_folder="models_cplex", medium=Hazelnut, threads=14) 
plot_tradeoff(tradeoff_Hazelnut, filename="results/tradeoff_Hazelnut.html")
tradeoff_Lentils = tradeoff(manifest, model_folder="models_cplex", medium=Lentils, threads=14) 
plot_tradeoff(tradeoff_Lentils, filename="results/tradeoff_Lentils.html")
tradeoff_Peanut = tradeoff(manifest, model_folder="models_cplex", medium=Peanut, threads=14) 
plot_tradeoff(tradeoff_Peanut, filename="results/tradeoff_Peanut.html")
tradeoff_Pecans = tradeoff(manifest, model_folder="models_cplex", medium=Pecans, threads=14) 
plot_tradeoff(tradeoff_Pecans, filename="results/tradeoff_Pecans.html")
tradeoff_Pumpkin_seed = tradeoff(manifest, model_folder="models_cplex", medium=Pumpkin_seed, threads=14) 
plot_tradeoff(tradeoff_Pumpkin_seed, filename="results/tradeoff_Pumpkin_seed.html")
tradeoff_Red_beans = tradeoff(manifest, model_folder="models_cplex", medium=Red_beans, threads=14) 
plot_tradeoff(tradeoff_Red_beans, filename="results/tradeoff_Red_beans.html")
tradeoff_Soybean = tradeoff(manifest, model_folder="models_cplex", medium=Soybean, threads=14) 
plot_tradeoff(tradeoff_Soybean, filename="results/tradeoff_Soybean.html")
tradeoff_Split_peas = tradeoff(manifest, model_folder="models_cplex", medium=Split_peas, threads=14) 
plot_tradeoff(tradeoff_Split_peas, filename="results/tradeoff_Split_peas.html")
tradeoff_Sunflower_seed = tradeoff(manifest, model_folder="models_cplex", medium=Sunflower_seed, threads=14) 
plot_tradeoff(tradeoff_Sunflower_seed, filename="results/tradeoff_Sunflower_seed.html")
tradeoff_White_beans = tradeoff(manifest, model_folder="models_cplex", medium=White_beans, threads=14) 
plot_tradeoff(tradeoff_White_beans, filename="results/tradeoff_White_beans.html")
tradeoff_Zucchini = tradeoff(manifest, model_folder="models_cplex", medium=Zucchini, threads=14) 
plot_tradeoff(tradeoff_Zucchini, filename="results/tradeoff_Zucchini.html")
tradeoff_Peache = tradeoff(manifest, model_folder="models_cplex", medium=Peache, threads=14) 
plot_tradeoff(tradeoff_Peache, filename="results/tradeoff_Peache.html")
tradeoff_Cashew = tradeoff(manifest, model_folder="models_cplex", medium=Cashew, threads=14) 
plot_tradeoff(tradeoff_Cashew, filename="results/tradeoff_Cashew.html")
tradeoff_Codfish = tradeoff(manifest, model_folder="models_cplex", medium=Codfish, threads=14) 
plot_tradeoff(tradeoff_Codfish, filename="results/tradeoff_Codfish.html")
tradeoff_Tuna = tradeoff(manifest, model_folder="models_cplex", medium=Tuna, threads=14) 
plot_tradeoff(tradeoff_Tuna, filename="results/tradeoff_Tuna.html")
tradeoff_Cucumber = tradeoff(manifest, model_folder="models_cplex", medium=Cucumber, threads=14) 
plot_tradeoff(tradeoff_Cucumber, filename="results/tradeoff_Cucumber.html")
tradeoff_Pumpkin = tradeoff(manifest, model_folder="models_cplex", medium=Pumpkin, threads=14) 
plot_tradeoff(tradeoff_Pumpkin, filename="results/tradeoff_Pumpkin.html")
tradeoff_Grape = tradeoff(manifest, model_folder="models_cplex", medium=Grape, threads=14) 
plot_tradeoff(tradeoff_Grape, filename="results/tradeoff_Grape.html")
tradeoff_Barley = tradeoff(manifest, model_folder="models_cplex", medium=Barley, threads=14) 
plot_tradeoff(tradeoff_Barley, filename="results/tradeoff_Barley.html")
tradeoff_Rice = tradeoff(manifest, model_folder="models_cplex", medium=Rice, threads=14) 
plot_tradeoff(tradeoff_Rice, filename="results/tradeoff_Rice.html")
tradeoff_Control_Breastmilk = tradeoff(manifest, model_folder="models_cplex", medium=Control_Breastmilk, threads=14) 
plot_tradeoff(tradeoff_Control_Breastmilk, filename="results/tradeoff_Control_Breastmilk.html")
tradeoff_Control_Infant_formula = tradeoff(manifest, model_folder="models_cplex", medium=Control_Infant_formula, threads=14) 
plot_tradeoff(tradeoff_Control_Infant_formula, filename="results/tradeoff_infant_control_formula.html")

##Growing the models
from micom.workflows import grow, save_results

res_Broccoli = grow(manifest, model_folder="models_cplex", medium=Broccoli, tradeoff=0.8, threads=14) 
save_results(res_Broccoli, "results/Broccoli.zip") 
res_Brussel = grow(manifest, model_folder="models_cplex", medium=Brussel, tradeoff=0.8, threads=14) 
save_results(res_Brussel, "results/Brussel.zip")
res_Cabbage = grow(manifest, model_folder="models_cplex", medium=Cabbage, tradeoff=0.8, threads=14) 
save_results(res_Cabbage, "results/Cabbage.zip") 
res_Carrot = grow(manifest, model_folder="models_cplex", medium=Carrot, tradeoff=0.8, threads=14) 
save_results(res_Carrot, "results/Carrot.zip")  
res_Cauliflower = grow(manifest, model_folder="models_cplex", medium=Cauliflower, tradeoff=0.7, threads=14) 
save_results(res_Cauliflower, "results/Cauliflower.zip") 
res_Celery = grow(manifest, model_folder="models_cplex", medium=Celery, tradeoff=0.8, threads=14) 
save_results(res_Celery, "results/Celery.zip") 
res_Eggplant = grow(manifest, model_folder="models_cplex", medium=Eggplant, tradeoff=0.9, threads=14) 
save_results(res_Eggplant, "results/Eggplant.zip")
res_Green_beans = grow(manifest, model_folder="models_cplex", medium=Green_beans, tradeoff=0.8, threads=14) 
save_results(res_Green_beans, "results/Green_beans.zip") 
res_Green_capsicum = grow(manifest, model_folder="models_cplex", medium=Green_capsicum, tradeoff=0.8, threads=14) 
save_results(res_Green_capsicum, "results/Green_capsicum.zip")  
res_Lettuce = grow(manifest, model_folder="models_cplex", medium=Lettuce, tradeoff=0.8, threads=14) 
save_results(res_Lettuce, "results/Lettuce.zip") 
res_Mushroom = grow(manifest, model_folder="models_cplex", medium=Mushroom, tradeoff=0.9, threads=14) 
save_results(res_Mushroom, "results/Mushroom.zip") 
res_Onion = grow(manifest, model_folder="models_cplex", medium=Onion, tradeoff=0.8, threads=14) 
save_results(res_Onion, "results/Onion.zip")
res_Pak_choi = grow(manifest, model_folder="models_cplex", medium=Pak_choi, tradeoff=0.9, threads=14) 
save_results(res_Pak_choi, "results/Pak_choi.zip") 
res_Potato = grow(manifest, model_folder="models_cplex", medium=Potato, tradeoff=0.8, threads=14) 
save_results(res_Potato, "results/Potato.zip")  
res_Sweetcorn = grow(manifest, model_folder="models_cplex", medium=Sweetcorn, tradeoff=0.8, threads=14) 
save_results(res_Sweetcorn, "results/Sweetcorn.zip") 
res_Spinach = grow(manifest, model_folder="models_cplex", medium=Spinach, tradeoff=0.8, threads=14) 
save_results(res_Spinach, "results/Spinach.zip") 
res_Squash = grow(manifest, model_folder="models_cplex", medium=Squash, tradeoff=0.8, threads=14) 
save_results(res_Squash, "results/Squash.zip")
res_Sweet_potato = grow(manifest, model_folder="models_cplex", medium=Sweet_potato, tradeoff=0.9, threads=14) 
save_results(res_Sweet_potato, "results/Sweet_potato.zip") 
res_Tomato = grow(manifest, model_folder="models_cplex", medium=Tomato, tradeoff=0.8, threads=14) 
save_results(res_Tomato, "results/Tomato.zip")  
res_Yam = grow(manifest, model_folder="models_cplex", medium=Yam, tradeoff=0.7, threads=14) 
save_results(res_Yam, "results/Yam.zip") 
res_Apple = grow(manifest, model_folder="models_cplex", medium=Apple, tradeoff=0.8, threads=14) 
save_results(res_Apple, "results/Apple.zip") 
res_Banana = grow(manifest, model_folder="models_cplex", medium=Banana, tradeoff=0.8, threads=14) 
save_results(res_Banana, "results/Banana.zip")
res_Blackcurrant = grow(manifest, model_folder="models_cplex", medium=Blackcurrant, tradeoff=0.9, threads=14) 
save_results(res_Blackcurrant, "results/Blackcurrant.zip") 
res_Blueberries = grow(manifest, model_folder="models_cplex", medium=Blueberries, tradeoff=0.9, threads=14) 
save_results(res_Blueberries, "results/Blueberries.zip")  
res_Cherry = grow(manifest, model_folder="models_cplex", medium=Cherry, tradeoff=0.9, threads=14) 
save_results(res_Cherry, "results/Cherry.zip") 
res_Feijoa = grow(manifest, model_folder="models_cplex", medium=Feijoa, tradeoff=0.9, threads=14) 
save_results(res_Feijoa, "results/Feijoa.zip") 
res_Gold_kiwifruit = grow(manifest, model_folder="models_cplex", medium=Gold_kiwifruit, tradeoff=0.9, threads=14) 
save_results(res_Gold_kiwifruit, "results/Gold_kiwifruit.zip")
res_Grapefruit = grow(manifest, model_folder="models_cplex", medium=Grapefruit, tradeoff=0.8, threads=14) 
save_results(res_Grapefruit, "results/Grapefruit.zip") 
res_Green_kiwifruit = grow(manifest, model_folder="models_cplex", medium=Green_kiwifruit, tradeoff=0.8, threads=14) 
save_results(res_Green_kiwifruit, "results/Green_kiwifruit.zip")  
res_Mandarin = grow(manifest, model_folder="models_cplex", medium=Mandarin, tradeoff=0.8, threads=14) 
save_results(res_Mandarin, "results/Mandarin.zip") 
res_Mango = grow(manifest, model_folder="models_cplex", medium=Mango, tradeoff=0.9, threads=14) 
save_results(res_Mango, "results/Mango.zip") 
res_Melon = grow(manifest, model_folder="models_cplex", medium=Melon, tradeoff=0.8, threads=14) 
save_results(res_Melon, "results/Melon.zip")
res_Nectarine = grow(manifest, model_folder="models_cplex", medium=Nectarine, tradeoff=0.9, threads=14) 
save_results(res_Nectarine, "results/Nectarine.zip") 
res_Orange = grow(manifest, model_folder="models_cplex", medium=Orange, tradeoff=0.8, threads=14) 
save_results(res_Orange, "results/Orange.zip")  
res_Pear = grow(manifest, model_folder="models_cplex", medium=Pear, tradeoff=0.8, threads=14) 
save_results(res_Pear, "results/Pear.zip") 
res_Pineapple = grow(manifest, model_folder="models_cplex", medium=Pineapple, tradeoff=0.9, threads=14) 
save_results(res_Pineapple, "results/Pineapple.zip") 
res_Plum = grow(manifest, model_folder="models_cplex", medium=Plum, tradeoff=0.8, threads=14) 
save_results(res_Plum, "results/Plum.zip")
res_Raspberries = grow(manifest, model_folder="models_cplex", medium=Raspberries, tradeoff=0.9, threads=14) 
save_results(res_Raspberries, "results/Raspberries.zip") 
res_Strawberries = grow(manifest, model_folder="models_cplex", medium=Strawberries, tradeoff=0.8, threads=14) 
save_results(res_Strawberries, "results/Strawberries.zip")  
res_Barley_cereal = grow(manifest, model_folder="models_cplex", medium=Barley_cereal, tradeoff=0.8, threads=14) 
save_results(res_Barley_cereal, "results/Barley_cereal.zip") 
res_Couscous = grow(manifest, model_folder="models_cplex", medium=Couscous, tradeoff=0.8, threads=14) 
save_results(res_Couscous, "results/Couscous.zip") 
res_Noodles = grow(manifest, model_folder="models_cplex", medium=Noodles, tradeoff=0.8, threads=14) 
save_results(res_Noodles, "results/Noodles.zip")
res_Oat_cereal = grow(manifest, model_folder="models_cplex", medium=Oat_cereal, tradeoff=0.8, threads=14) 
save_results(res_Oat_cereal, "results/Oat_cereal.zip") 
res_Pasta = grow(manifest, model_folder="models_cplex", medium=Pasta, tradeoff=0.9, threads=14) 
save_results(res_Pasta, "results/Pasta.zip")  
res_Rice_cereal = grow(manifest, model_folder="models_cplex", medium=Rice_cereal, tradeoff=0.7, threads=14) 
save_results(res_Rice_cereal, "results/Rice_cereal.zip") 
res_Tapioca_pudding = grow(manifest, model_folder="models_cplex", medium=Tapioca_pudding, tradeoff=0.9, threads=14) 
save_results(res_Tapioca_pudding, "results/Tapioca_pudding.zip") 
res_White_bread = grow(manifest, model_folder="models_cplex", medium=White_bread, tradeoff=0.9, threads=14) 
save_results(res_White_bread, "results/White_bread.zip")
res_Wholegrain_bread = grow(manifest, model_folder="models_cplex", medium=Wholegrain_bread, tradeoff=0.9, threads=14) 
save_results(res_Wholegrain_bread, "results/Wholegrain_bread.zip") 
res_Cottage_cheese = grow(manifest, model_folder="models_cplex", medium=Cottage_cheese, tradeoff=0.6, threads=14) 
save_results(res_Cottage_cheese, "results/Cottage_cheese.zip")  
res_Eggs = grow(manifest, model_folder="models_cplex", medium=Eggs, tradeoff=0.9, threads=14) 
save_results(res_Eggs, "results/Eggs.zip") 
res_Mozzarella_cheese = grow(manifest, model_folder="models_cplex", medium=Mozzarella_cheese, tradeoff=0.7, threads=14) 
save_results(res_Mozzarella_cheese, "results/Mozzarella_cheese.zip") 
res_Soymilk = grow(manifest, model_folder="models_cplex", medium=Soymilk, tradeoff=0.8, threads=14) 
save_results(res_Soymilk, "results/Soymilk.zip")
res_Tofu = grow(manifest, model_folder="models_cplex", medium=Tofu, tradeoff=0.8, threads=14) 
save_results(res_Tofu, "results/Tofu.zip") 
res_Whole_milk = grow(manifest, model_folder="models_cplex", medium=Whole_milk, tradeoff=0.8, threads=14) 
save_results(res_Whole_milk, "results/Whole_milk.zip")  
res_Yoghurt = grow(manifest, model_folder="models_cplex", medium=Yoghurt, tradeoff=0.8, threads=14) 
save_results(res_Yoghurt, "results/Yoghurt.zip") 
res_Beef = grow(manifest, model_folder="models_cplex", medium=Beef, tradeoff=0.5, threads=14) 
save_results(res_Beef, "results/Beef.zip") 
res_Chicken = grow(manifest, model_folder="models_cplex", medium=Chicken, tradeoff=0.4, threads=14) 
save_results(res_Chicken, "results/Chicken.zip")
res_Lamb = grow(manifest, model_folder="models_cplex", medium=Lamb, tradeoff=0.9, threads=14) 
save_results(res_Lamb, "results/Lamb.zip") 
res_Mackerel = grow(manifest, model_folder="models_cplex", medium=Mackerel, tradeoff=0.8, threads=14) 
save_results(res_Mackerel, "results/Mackerel.zip")  
res_Mussels = grow(manifest, model_folder="models_cplex", medium=Mussels, tradeoff=0.8, threads=14) 
save_results(res_Mussels, "results/Mussels.zip") 
res_Pork = grow(manifest, model_folder="models_cplex", medium=Pork, tradeoff=0.8, threads=14) 
save_results(res_Pork, "results/Pork.zip") 
res_Salmon = grow(manifest, model_folder="models_cplex", medium=Salmon, tradeoff=0.9, threads=14) 
save_results(res_Salmon, "results/Salmon.zip")
res_Shrimp = grow(manifest, model_folder="models_cplex", medium=Shrimp, tradeoff=0.8, threads=14) 
save_results(res_Shrimp, "results/Shrimp.zip") 
res_Turkey = grow(manifest, model_folder="models_cplex", medium=Turkey, tradeoff=0.6, threads=14) 
save_results(res_Turkey, "results/Turkey.zip")  
res_Almond = grow(manifest, model_folder="models_cplex", medium=Almond, tradeoff=0.8, threads=14) 
save_results(res_Almond, "results/Almond.zip") 
res_Black_beans = grow(manifest, model_folder="models_cplex", medium=Black_beans, tradeoff=0.8, threads=14) 
save_results(res_Black_beans, "results/Black_beans.zip") 
res_Chia = grow(manifest, model_folder="models_cplex", medium=Chia, tradeoff=0.8, threads=14) 
save_results(res_Chia, "results/Chia.zip")
res_Chickpea = grow(manifest, model_folder="models_cplex", medium=Chickpea, tradeoff=0.8, threads=14) 
save_results(res_Chickpea, "results/Chickpea.zip") 
res_Green_peas = grow(manifest, model_folder="models_cplex", medium=Green_peas, tradeoff=0.8, threads=14) 
save_results(res_Green_peas, "results/Green_peas.zip")  
res_Hazelnut = grow(manifest, model_folder="models_cplex", medium=Hazelnut, tradeoff=0.8, threads=14) 
save_results(res_Hazelnut, "results/Hazelnut.zip") 
res_Lentils = grow(manifest, model_folder="models_cplex", medium=Lentils, tradeoff=0.8, threads=14) 
save_results(res_Lentils, "results/Lentils.zip") 
res_Peanut = grow(manifest, model_folder="models_cplex", medium=Peanut, tradeoff=0.8, threads=14) 
save_results(res_Peanut, "results/Peanut.zip")
res_Pecans = grow(manifest, model_folder="models_cplex", medium=Pecans, tradeoff=0.8, threads=14) 
save_results(res_Pecans, "results/Pecans.zip") 
res_Pumpkin_seed = grow(manifest, model_folder="models_cplex", medium=Pumpkin_seed, tradeoff=0.8, threads=14) 
save_results(res_Pumpkin_seed, "results/Pumpkin_seed.zip")  
res_Red_beans = grow(manifest, model_folder="models_cplex", medium=Red_beans, tradeoff=0.8, threads=14) 
save_results(res_Red_beans, "results/Red_beans.zip")
res_Soybean = grow(manifest, model_folder="models_cplex", medium=Soybean, tradeoff=0.8, threads=14) 
save_results(res_Soybean, "results/Soybean.zip") 
res_Split_peas = grow(manifest, model_folder="models_cplex", medium=Split_peas, tradeoff=0.8, threads=14) 
save_results(res_Split_peas, "results/Split_peas.zip")
res_Sunflower_seed = grow(manifest, model_folder="models_cplex", medium=Sunflower_seed, tradeoff=0.8, threads=14) 
save_results(res_Sunflower_seed, "results/Sunflower_seed.zip") 
res_White_beans = grow(manifest, model_folder="models_cplex", medium=White_beans, tradeoff=0.5, threads=14) 
save_results(res_White_beans, "results/White_beans.zip")  
res_Zucchini = grow(manifest, model_folder="models_cplex", medium=Zucchini, tradeoff=0.8, threads=14) 
save_results(res_Zucchini, "results/Zucchini.zip") 
res_Peache = grow(manifest, model_folder="models_cplex", medium=Peache, tradeoff=0.8, threads=14) 
save_results(res_Peache, "results/Peache.zip") 
res_Cashew = grow(manifest, model_folder="models_cplex", medium=Cashew, tradeoff=0.8, threads=14) 
save_results(res_Cashew, "results/Cashew.zip")
res_Codfish = grow(manifest, model_folder="models_cplex", medium=Codfish, tradeoff=0.8, threads=14) 
save_results(res_Codfish, "results/Codfish.zip") 
res_Tuna = grow(manifest, model_folder="models_cplex", medium=Tuna, tradeoff=0.7, threads=14) 
save_results(res_Tuna, "results/Tuna.zip")  
res_Cucumber = grow(manifest, model_folder="models_cplex", medium=Cucumber, tradeoff=0.8, threads=14) 
save_results(res_Cucumber, "results/Cucumber.zip") 
res_Pumpkin = grow(manifest, model_folder="models_cplex", medium=Pumpkin, tradeoff=0.8, threads=14) 
save_results(res_Pumpkin, "results/Pumpkin.zip") 
res_Grape = grow(manifest, model_folder="models_cplex", medium=Grape, tradeoff=0.8, threads=14) 
save_results(res_Grape, "results/Grape.zip")
res_Barley = grow(manifest, model_folder="models_cplex", medium=Barley, tradeoff=0.9, threads=14) 
save_results(res_Barley, "results/Barley.zip") 
res_Rice = grow(manifest, model_folder="models_cplex", medium=Rice, tradeoff=0.7, threads=14) 
save_results(res_Rice, "results/Rice.zip")  
res_Control_Breastmilk = grow(manifest, model_folder="models_cplex", medium=Control_Breastmilk, tradeoff=0.9, threads=14) 
save_results(res_Control_Breastmilk, "results/Control_Breastmilk.zip") 
res_Control_Infant_formula = grow(manifest, model_folder="models_cplex", medium=Control_Infant_formula, tradeoff=0.8, threads=14) 
save_results(res_Control_Infant_formula, "results/Control_Infant_formula.zip")

#Visualisations
from micom.viz import plot_growth
#Growth rates

plot_growth(res_Broccoli, filename="results/growth_rates_Broccoli.html")  
plot_growth(res_Brussel, filename="results/growth_rates_Brussel.html") 
plot_growth(res_Cabbage, filename="results/growth_rates_Cabbage.html")  
plot_growth(res_Carrot, filename="results/growth_rates_Carrot.html") 
plot_growth(res_Cauliflower, filename="results/growth_rates_Cauliflower.html") 
plot_growth(res_Celery, filename="results/growth_rates_Celery.html")  
plot_growth(res_Eggplant, filename="results/growth_rates_Eggplant.html") 
plot_growth(res_Green_beans, filename="results/growth_rates_Green_beans.html")  
plot_growth(res_Green_capsicum, filename="results/growth_rates_Green_capsicum.html") 
plot_growth(res_Lettuce, filename="results/growth_rates_Lettuce.html")
plot_growth(res_Mushroom, filename="results/growth_rates_Mushroom.html")  
plot_growth(res_Onion, filename="results/growth_rates_Onion.html") 
plot_growth(res_Pak_choi, filename="results/growth_rates_Pak_choi.html")  
plot_growth(res_Potato, filename="results/growth_rates_Potato.html") 
plot_growth(res_Sweetcorn, filename="results/growth_rates_Sweetcorn.html") 
plot_growth(res_Spinach, filename="results/growth_rates_Spinach.html")  
plot_growth(res_Squash, filename="results/growth_rates_Squash.html") 
plot_growth(res_Sweet_potato, filename="results/growth_rates_Sweet_potato.html")  
plot_growth(res_Tomato, filename="results/growth_rates_Tomato.html") 
plot_growth(res_Yam, filename="results/growth_rates_Yam.html") 
plot_growth(res_Apple, filename="results/growth_rates_Apple.html")  
plot_growth(res_Banana, filename="results/growth_rates_Banana.html") 
plot_growth(res_Blackcurrant, filename="results/growth_rates_Blackcurrant.html")  
plot_growth(res_Blueberries, filename="results/growth_rates_Blueberries.html") 
plot_growth(res_Cherry, filename="results/growth_rates_Cherry.html")
plot_growth(res_Feijoa, filename="results/growth_rates_Feijoa.html")  
plot_growth(res_Gold_kiwifruit, filename="results/growth_rates_Gold_kiwifruit.html") 
plot_growth(res_Grapefruit, filename="results/growth_rates_Grapefruit.html")  
plot_growth(res_Green_kiwifruit, filename="results/growth_rates_Green_kiwifruit.html") 
plot_growth(res_Mandarin, filename="results/growth_rates_Mandarin.html") 
plot_growth(res_Mango, filename="results/growth_rates_Mango.html")  
plot_growth(res_Melon, filename="results/growth_rates_Melon.html") 
plot_growth(res_Nectarine, filename="results/growth_rates_Nectarine.html")  
plot_growth(res_Orange, filename="results/growth_rates_Orange.html") 
plot_growth(res_Pear, filename="results/growth_rates_Pear.html") 
plot_growth(res_Pineapple, filename="results/growth_rates_Pineapple.html")  
plot_growth(res_Plum, filename="results/growth_rates_Plum.html") 
plot_growth(res_Raspberries, filename="results/growth_rates_Raspberries.html")  
plot_growth(res_Strawberries, filename="results/growth_rates_Strawberries.html") 
plot_growth(res_Barley_cereal, filename="results/growth_rates_Barley_cereal.html")
plot_growth(res_Couscous, filename="results/growth_rates_Couscous.html")  
plot_growth(res_Noodles, filename="results/growth_rates_Noodles.html") 
plot_growth(res_Oat_cereal, filename="results/growth_rates_Oat_cereal.html")  
plot_growth(res_Pasta, filename="results/growth_rates_Pasta.html") 
plot_growth(res_Rice_cereal, filename="results/growth_rates_Rice_cereal.html") 
plot_growth(res_Tapioca_pudding, filename="results/growth_rates_Tapioca_pudding.html")  
plot_growth(res_White_bread, filename="results/growth_rates_White_bread.html") 
plot_growth(res_Wholegrain_bread, filename="results/growth_rates_Wholegrain_bread.html")  
plot_growth(res_Cottage_cheese, filename="results/growth_rates_Cottage_cheese.html") 
plot_growth(res_Eggs, filename="results/growth_rates_Eggs.html") 
plot_growth(res_Mozzarella_cheese, filename="results/growth_rates_Mozzarella_cheese.html")  
plot_growth(res_Soymilk, filename="results/growth_rates_Soymilk.html") 
plot_growth(res_Tofu, filename="results/growth_rates_Tofu.html")  
plot_growth(res_Whole_milk, filename="results/growth_rates_Whole_milk.html") 
plot_growth(res_Yoghurt, filename="results/growth_rates_Yoghurt.html")
plot_growth(res_Beef, filename="results/growth_rates_Beef.html")  
plot_growth(res_Chicken, filename="results/growth_rates_Chicken.html") 
plot_growth(res_Lamb, filename="results/growth_rates_Lamb.html")  
plot_growth(res_Mackerel, filename="results/growth_rates_Mackerel.html") 
plot_growth(res_Mussels, filename="results/growth_rates_Mussels.html")
plot_growth(res_Pork, filename="results/growth_rates_Pork.html")  
plot_growth(res_Salmon, filename="results/growth_rates_Salmon.html") 
plot_growth(res_Shrimp, filename="results/growth_rates_Shrimp.html")  
plot_growth(res_Turkey, filename="results/growth_rates_Turkey.html") 
plot_growth(res_Almond, filename="results/growth_rates_Almond.html") 
plot_growth(res_Black_beans, filename="results/growth_rates_Black_beans.html")  
plot_growth(res_Chia, filename="results/growth_rates_Chia.html") 
plot_growth(res_Chickpea, filename="results/growth_rates_Chickpea.html")  
plot_growth(res_Green_peas, filename="results/growth_rates_Green_peas.html") 
plot_growth(res_Hazelnut, filename="results/growth_rates_Hazelnut.html")
plot_growth(res_Lentils, filename="results/growth_rates_Lentils.html")  
plot_growth(res_Peanut, filename="results/growth_rates_Peanut.html") 
plot_growth(res_Pecans, filename="results/growth_rates_Pecans.html")  
plot_growth(res_Pumpkin_seed, filename="results/growth_rates_Pumpkin_seed.html") 
plot_growth(res_Red_beans, filename="results/growth_rates_Red_beans.html") 
plot_growth(res_Soybean, filename="results/growth_rates_Soybean.html")  
plot_growth(res_Split_peas, filename="results/growth_rates_Split_peas.html") 
plot_growth(res_Sunflower_seed, filename="results/growth_rates_Sunflower_seed.html")  
plot_growth(res_White_beans, filename="results/growth_rates_White_beans.html") 
plot_growth(res_Zucchini, filename="results/growth_rates_Zucchini.html") 
plot_growth(res_Peache, filename="results/growth_rates_Peache.html")  
plot_growth(res_Cashew, filename="results/growth_rates_Cashew.html") 
plot_growth(res_Codfish, filename="results/growth_rates_Codfish.html")  
plot_growth(res_Tuna, filename="results/growth_rates_Tuna.html") 
plot_growth(res_Cucumber, filename="results/growth_rates_Cucumber.html")
plot_growth(res_Pumpkin, filename="results/growth_rates_Pumpkin.html")  
plot_growth(res_Grape, filename="results/growth_rates_Grape.html") 
plot_growth(res_Barley, filename="results/growth_rates_Barley.html")  
plot_growth(res_Rice, filename="results/growth_rates_Rice.html")  
plot_growth(res_Control_Breastmilk, filename="results/growth_rates_Control_Breastmilk.html")  
plot_growth(res_Control_Infant_formula, filename="results/growth_rates_Control_Infant_formula.html") 

#Production rate
from micom.measures import production_rates
import pandas as pd

prod_Broccoli = production_rates(res_Broccoli)
prod_Brussel = production_rates(res_Brussel)
prod_Cabbage = production_rates(res_Cabbage)
prod_Carrot = production_rates(res_Carrot)
prod_Cauliflower = production_rates(res_Cauliflower)
prod_Celery = production_rates(res_Celery)
prod_Eggplant = production_rates(res_Eggplant)
prod_Green_beans = production_rates(res_Green_beans)
prod_Green_capsicum = production_rates(res_Green_capsicum)
prod_Lettuce = production_rates(res_Lettuce)
prod_Mushroom = production_rates(res_Mushroom)
prod_Onion = production_rates(res_Onion)
prod_Pak_choi = production_rates(res_Pak_choi)
prod_Potato = production_rates(res_Potato)
prod_Sweetcorn = production_rates(res_Sweetcorn)
prod_Spinach = production_rates(res_Spinach)
prod_Squash = production_rates(res_Squash)
prod_Sweet_potato = production_rates(res_Sweet_potato)
prod_Tomato = production_rates(res_Tomato)
prod_Yam = production_rates(res_Yam)
prod_Apple = production_rates(res_Apple)
prod_Banana = production_rates(res_Banana)
prod_Blackcurrant = production_rates(res_Blackcurrant)
prod_Blueberries = production_rates(res_Blueberries)
prod_Cherry = production_rates(res_Cherry)
prod_Feijoa = production_rates(res_Feijoa)
prod_Gold_kiwifruit = production_rates(res_Gold_kiwifruit)
prod_Grapefruit = production_rates(res_Grapefruit)
prod_Green_kiwifruit = production_rates(res_Green_kiwifruit)
prod_Mandarin = production_rates(res_Mandarin)
prod_Mango = production_rates(res_Mango)
prod_Melon = production_rates(res_Melon)
prod_Nectarine = production_rates(res_Nectarine)
prod_Orange = production_rates(res_Orange)
prod_Pear = production_rates(res_Pear)
prod_Pineapple = production_rates(res_Pineapple)
prod_Plum = production_rates(res_Plum)
prod_Raspberries = production_rates(res_Raspberries)
prod_Strawberries = production_rates(res_Strawberries)
prod_Barley_cereal = production_rates(res_Barley_cereal)
prod_Couscous = production_rates(res_Couscous)
prod_Noodles = production_rates(res_Noodles)
prod_Oat_cereal = production_rates(res_Oat_cereal)
prod_Pasta = production_rates(res_Pasta)
prod_Rice_cereal = production_rates(res_Rice_cereal)
prod_Tapioca_pudding = production_rates(res_Tapioca_pudding)
prod_White_bread = production_rates(res_White_bread)
prod_Wholegrain_bread = production_rates(res_Wholegrain_bread)
prod_Cottage_cheese = production_rates(res_Cottage_cheese)
prod_Eggs = production_rates(res_Eggs)
prod_Mozzarella_cheese = production_rates(res_Mozzarella_cheese)
prod_Soymilk = production_rates(res_Soymilk)
prod_Tofu = production_rates(res_Tofu)
prod_Whole_milk = production_rates(res_Whole_milk)
prod_Yoghurt = production_rates(res_Yoghurt)
prod_Beef = production_rates(res_Beef)
prod_Chicken = production_rates(res_Chicken)
prod_Lamb = production_rates(res_Lamb)
prod_Mackerel = production_rates(res_Mackerel)
prod_Mussels = production_rates(res_Mussels)
prod_Pork = production_rates(res_Pork)
prod_Salmon = production_rates(res_Salmon)
prod_Shrimp = production_rates(res_Shrimp)
prod_Turkey = production_rates(res_Turkey)
prod_Almond = production_rates(res_Almond)
prod_Black_beans = production_rates(res_Black_beans)
prod_Chia = production_rates(res_Chia)
prod_Chickpea = production_rates(res_Chickpea)
prod_Green_peas = production_rates(res_Green_peas)
prod_Hazelnut = production_rates(res_Hazelnut)
prod_Lentils = production_rates(res_Lentils)
prod_Peanut = production_rates(res_Peanut)
prod_Pecans = production_rates(res_Pecans)
prod_Pumpkin_seed = production_rates(res_Pumpkin_seed)
prod_Red_beans = production_rates(res_Red_beans)
prod_Soybean = production_rates(res_Soybean)
prod_Split_peas = production_rates(res_Split_peas)
prod_Sunflower_seed = production_rates(res_Sunflower_seed)
prod_White_beans = production_rates(res_White_beans)
prod_Zucchini = production_rates(res_Zucchini)
prod_Peache = production_rates(res_Peache)
prod_Cashew = production_rates(res_Cashew)
prod_Codfish = production_rates(res_Codfish)
prod_Tuna = production_rates(res_Tuna)
prod_Cucumber = production_rates(res_Cucumber)
prod_Pumpkin = production_rates(res_Pumpkin)
prod_Grape = production_rates(res_Grape)
prod_Barley = production_rates(res_Barley)
prod_Rice = production_rates(res_Rice)
prod_Control_Breastmilk = production_rates(res_Control_Breastmilk)
prod_Control_Infant_formula = production_rates(res_Control_Infant_formula)

prod_Broccoli['diet'] = 'Broccoli' #create new colum
prod_Brussel['diet'] = 'Brussel' #create new colum
prod_Cabbage['diet'] = 'Cabbage' #create new colum
prod_Carrot['diet'] = 'Carrot' #create new colum
prod_Cauliflower['diet'] = 'Cauliflower' #create new colum
prod_Celery['diet'] = 'Celery' #create new colum
prod_Eggplant['diet'] = 'Eggplant' #create new colum
prod_Green_beans['diet'] = 'Green_beans' #create new colum
prod_Green_capsicum['diet'] = 'Green_capsicum' #create new colum
prod_Lettuce['diet'] = 'Lettuce' #create new colum
prod_Mushroom['diet'] = 'Mushroom' #create new colum
prod_Onion['diet'] = 'Onion' #create new colum
prod_Pak_choi['diet'] = 'Pak_choi' #create new colum
prod_Potato['diet'] = 'Potato' #create new colum
prod_Sweetcorn['diet'] = 'Sweetcorn' #create new colum
prod_Spinach['diet'] = 'Spinach' #create new colum
prod_Squash['diet'] = 'Squash' #create new colum
prod_Sweet_potato['diet'] = 'Sweet_potato' #create new colum
prod_Tomato['diet'] = 'Tomato' #create new colum
prod_Yam['diet'] = 'Yam' #create new colum
prod_Apple['diet'] = 'Apple' #create new colum
prod_Banana['diet'] = 'Banana' #create new colum
prod_Blackcurrant['diet'] = 'Blackcurrant' #create new colum
prod_Blueberries['diet'] = 'Blueberries' #create new colum
prod_Cherry['diet'] = 'Cherry' #create new colum
prod_Feijoa['diet'] = 'Feijoa' #create new colum
prod_Gold_kiwifruit['diet'] = 'Gold_kiwifruit' #create new colum
prod_Grapefruit['diet'] = 'Grapefruit' #create new colum
prod_Green_kiwifruit['diet'] = 'Green_kiwifruit' #create new colum
prod_Mandarin['diet'] = 'Mandarin' #create new colum
prod_Mango['diet'] = 'Mango' #create new colum
prod_Melon['diet'] = 'Melon' #create new colum
prod_Nectarine['diet'] = 'Nectarine' #create new colum
prod_Orange['diet'] = 'Orange' #create new colum
prod_Pear['diet'] = 'Pear' #create new colum
prod_Pineapple['diet'] = 'Pineapple' #create new colum
prod_Plum['diet'] = 'Plum' #create new colum
prod_Raspberries['diet'] = 'Raspberries' #create new colum
prod_Strawberries['diet'] = 'Strawberries' #create new colum
prod_Barley_cereal['diet'] = 'Barley_cereal' #create new colum
prod_Couscous['diet'] = 'Couscous' #create new colum
prod_Noodles['diet'] = 'Noodles' #create new colum
prod_Oat_cereal['diet'] = 'Oat_cereal' #create new colum
prod_Pasta['diet'] = 'Pasta' #create new colum
prod_Rice_cereal['diet'] = 'Rice_cereal' #create new colum
prod_Tapioca_pudding['diet'] = 'Tapioca_pudding' #create new colum
prod_White_bread['diet'] = 'White_bread' #create new colum
prod_Wholegrain_bread['diet'] = 'Wholegrain_bread' #create new colum
prod_Cottage_cheese['diet'] = 'Cottage_cheese' #create new colum
prod_Eggs['diet'] = 'Eggs' #create new colum
prod_Mozzarella_cheese['diet'] = 'Mozzarella_cheese' #create new colum
prod_Soymilk['diet'] = 'Soymilk' #create new colum
prod_Tofu['diet'] = 'Tofu' #create new colum
prod_Whole_milk['diet'] = 'Whole_milk' #create new colum
prod_Yoghurt['diet'] = 'Yoghurt' #create new colum
prod_Beef['diet'] = 'Beef' #create new colum
prod_Chicken['diet'] = 'Chicken' #create new colum
prod_Lamb['diet'] = 'Lamb' #create new colum
prod_Mackerel['diet'] = 'Mackerel' #create new colum
prod_Mussels['diet'] = 'Mussels' #create new colum
prod_Pork['diet'] = 'Pork' #create new colum
prod_Salmon['diet'] = 'Salmon' #create new colum
prod_Shrimp['diet'] = 'Shrimp' #create new colum
prod_Turkey['diet'] = 'Turkey' #create new colum
prod_Almond['diet'] = 'Almond' #create new colum
prod_Black_beans['diet'] = 'Black_beans' #create new colum
prod_Chia['diet'] = 'Chia' #create new colum
prod_Chickpea['diet'] = 'Chickpea' #create new colum
prod_Green_peas['diet'] = 'Green_peas' #create new colum
prod_Hazelnut['diet'] = 'Hazelnut' #create new colum
prod_Lentils['diet'] = 'Lentils' #create new colum
prod_Peanut['diet'] = 'Peanut' #create new colum
prod_Pecans['diet'] = 'Pecans' #create new colum
prod_Pumpkin_seed['diet'] = 'Pumpkin_seed' #create new colum
prod_Red_beans['diet'] = 'Red_beans' #create new colum
prod_Soybean['diet'] = 'Soybean' #create new colum
prod_Split_peas['diet'] = 'Split_peas' #create new colum
prod_Sunflower_seed['diet'] = 'Sunflower_seed' #create new colum
prod_White_beans['diet'] = 'White_beans' #create new colum
prod_Zucchini['diet'] = 'Zucchini' #create new colum
prod_Peache['diet'] = 'Peache' #create new colum
prod_Cashew['diet'] = 'Cashew' #create new colum
prod_Codfish['diet'] = 'Codfish' #create new colum
prod_Tuna['diet'] = 'Tuna' #create new colum
prod_Cucumber['diet'] = 'Cucumber' #create new colum
prod_Pumpkin['diet'] = 'Pumpkin' #create new colum
prod_Grape['diet'] = 'Grape' #create new colum
prod_Barley['diet'] = 'Barley' #create new colum
prod_Rice['diet'] = 'Rice' #create new colum
prod_Control_Breastmilk['diet'] = 'Control_Breastmilk' #create new colum
prod_Control_Infant_formula['diet'] = 'Control_Infant_formula' #create new colum

exchanges = pd.concat([prod_Broccoli,prod_Brussel,prod_Cabbage,prod_Carrot,prod_Cauliflower,
                       prod_Celery,prod_Eggplant,prod_Green_beans,prod_Green_capsicum,prod_Lettuce,
                       prod_Mushroom,prod_Onion,prod_Pak_choi,prod_Potato,prod_Sweetcorn,
                       prod_Spinach,prod_Squash,prod_Sweet_potato,prod_Tomato,prod_Yam,
                       prod_Apple,prod_Banana,prod_Blackcurrant,prod_Blueberries,prod_Cherry,
                       prod_Feijoa,prod_Gold_kiwifruit,prod_Grapefruit,prod_Green_kiwifruit,prod_Mandarin,
                       prod_Mango,prod_Melon,prod_Nectarine,prod_Orange,prod_Pear,
                       prod_Pineapple,prod_Plum,prod_Raspberries,prod_Strawberries,prod_Barley_cereal,
                       prod_Couscous,prod_Noodles,prod_Oat_cereal,prod_Pasta,prod_Rice_cereal,
                       prod_Tapioca_pudding,prod_White_bread,prod_Wholegrain_bread,prod_Cottage_cheese,prod_Eggs,
                       prod_Mozzarella_cheese,prod_Soymilk,prod_Tofu,prod_Whole_milk,prod_Yoghurt,
                       prod_Beef,prod_Chicken,prod_Lamb,prod_Mackerel,prod_Mussels,
                       prod_Pork,prod_Salmon,prod_Shrimp,prod_Turkey,prod_Almond,
                       prod_Black_beans,prod_Chia,prod_Chickpea,prod_Green_peas,prod_Hazelnut,
                       prod_Lentils,prod_Peanut,prod_Pecans,prod_Pumpkin_seed,prod_Red_beans,
                       prod_Soybean,prod_Split_peas,prod_Sunflower_seed,prod_White_beans,prod_Zucchini,
                       prod_Peache,prod_Cashew,prod_Codfish,prod_Tuna,prod_Cucumber,
                       prod_Pumpkin,prod_Grape,prod_Barley,prod_Rice,
                       prod_Control_Breastmilk,prod_Control_Infant_formula])  # merge the production rates

exchanges = pd.pivot_table(exchanges, index = ['diet'], columns = 'name', values = 'flux') #converting into matrix
exchanges.to_csv("results/exchanges.csv")
exchanges_reduced = exchanges[["Acetate", "Propionate", "Butyrate","Isobutyrate, 2-Methylpropanoate", "Isovalerate, 3-Methylbutanoate"]] #selecting the metabolites of interest
exchanges_reduced.to_csv("results/exchanges_reduced.csv")

#Plotting growth rates
import pandas as pd
import seaborn as sns

growth_Broccoli = pd.read_csv('results/growth_rates_Broccoli.csv')
growth_Brussel = pd.read_csv('results/growth_rates_Brussel.csv')
growth_Cabbage = pd.read_csv('results/growth_rates_Cabbage.csv')
growth_Carrot = pd.read_csv('results/growth_rates_Carrot.csv')
growth_Cauliflower = pd.read_csv('results/growth_rates_Cauliflower.csv')
growth_Celery = pd.read_csv('results/growth_rates_Celery.csv')
growth_Eggplant = pd.read_csv('results/growth_rates_Eggplant.csv')
growth_Green_beans = pd.read_csv('results/growth_rates_Green_beans.csv')
growth_Green_capsicum = pd.read_csv('results/growth_rates_Green_capsicum.csv')
growth_Lettuce = pd.read_csv('results/growth_rates_Lettuce.csv')
growth_Mushroom = pd.read_csv('results/growth_rates_Mushroom.csv')
growth_Onion = pd.read_csv('results/growth_rates_Onion.csv')
growth_Pak_choi = pd.read_csv('results/growth_rates_Pak_choi.csv')
growth_Potato = pd.read_csv('results/growth_rates_Potato.csv')
growth_Sweetcorn = pd.read_csv('results/growth_rates_Sweetcorn.csv')
growth_Spinach = pd.read_csv('results/growth_rates_Spinach.csv')
growth_Squash = pd.read_csv('results/growth_rates_Squash.csv')
growth_Sweet_potato = pd.read_csv('results/growth_rates_Sweet_potato.csv')
growth_Tomato = pd.read_csv('results/growth_rates_Tomato.csv')
growth_Yam = pd.read_csv('results/growth_rates_Yam.csv')
growth_Apple = pd.read_csv('results/growth_rates_Apple.csv')
growth_Banana = pd.read_csv('results/growth_rates_Banana.csv')
growth_Blackcurrant = pd.read_csv('results/growth_rates_Blackcurrant.csv')
growth_Blueberries = pd.read_csv('results/growth_rates_Blueberries.csv')
growth_Cherry = pd.read_csv('results/growth_rates_Cherry.csv')
growth_Feijoa = pd.read_csv('results/growth_rates_Feijoa.csv')
growth_Gold_kiwifruit = pd.read_csv('results/growth_rates_Gold_kiwifruit.csv')
growth_Grapefruit = pd.read_csv('results/growth_rates_Grapefruit.csv')
growth_Green_kiwifruit = pd.read_csv('results/growth_rates_Green_kiwifruit.csv')
growth_Mandarin = pd.read_csv('results/growth_rates_Mandarin.csv')
growth_Mango = pd.read_csv('results/growth_rates_Mango.csv')
growth_Melon = pd.read_csv('results/growth_rates_Melon.csv')
growth_Nectarine = pd.read_csv('results/growth_rates_Nectarine.csv')
growth_Orange = pd.read_csv('results/growth_rates_Orange.csv')
growth_Pear = pd.read_csv('results/growth_rates_Pear.csv')
growth_Pineapple = pd.read_csv('results/growth_rates_Pineapple.csv')
growth_Plum = pd.read_csv('results/growth_rates_Plum.csv')
growth_Raspberries = pd.read_csv('results/growth_rates_Raspberries.csv')
growth_Strawberries = pd.read_csv('results/growth_rates_Strawberries.csv')
growth_Barley_cereal = pd.read_csv('results/growth_rates_Barley_cereal.csv')
growth_Couscous = pd.read_csv('results/growth_rates_Couscous.csv')
growth_Noodles = pd.read_csv('results/growth_rates_Noodles.csv')
growth_Oat_cereal = pd.read_csv('results/growth_rates_Oat_cereal.csv')
growth_Pasta = pd.read_csv('results/growth_rates_Pasta.csv')
growth_Rice_cereal = pd.read_csv('results/growth_rates_Rice_cereal.csv')
growth_Tapioca_pudding = pd.read_csv('results/growth_rates_Tapioca_pudding.csv')
growth_White_bread = pd.read_csv('results/growth_rates_White_bread.csv')
growth_Wholegrain_bread = pd.read_csv('results/growth_rates_Wholegrain_bread.csv')
growth_Cottage_cheese = pd.read_csv('results/growth_rates_Cottage_cheese.csv')
growth_Eggs = pd.read_csv('results/growth_rates_Eggs.csv')
growth_Mozzarella_cheese = pd.read_csv('results/growth_rates_Mozzarella_cheese.csv')
growth_Soymilk = pd.read_csv('results/growth_rates_Soymilk.csv')
growth_Tofu = pd.read_csv('results/growth_rates_Tofu.csv')
growth_Whole_milk = pd.read_csv('results/growth_rates_Whole_milk.csv')
growth_Yoghurt = pd.read_csv('results/growth_rates_Yoghurt.csv')
growth_Beef = pd.read_csv('results/growth_rates_Beef.csv')
growth_Chicken = pd.read_csv('results/growth_rates_Chicken.csv')
growth_Lamb = pd.read_csv('results/growth_rates_Lamb.csv')
growth_Mackerel = pd.read_csv('results/growth_rates_Mackerel.csv')
growth_Mussels = pd.read_csv('results/growth_rates_Mussels.csv')
growth_Pork = pd.read_csv('results/growth_rates_Pork.csv')
growth_Salmon = pd.read_csv('results/growth_rates_Salmon.csv')
growth_Shrimp = pd.read_csv('results/growth_rates_Shrimp.csv')
growth_Turkey = pd.read_csv('results/growth_rates_Turkey.csv')
growth_Almond = pd.read_csv('results/growth_rates_Almond.csv')
growth_Black_beans = pd.read_csv('results/growth_rates_Black_beans.csv')
growth_Chia = pd.read_csv('results/growth_rates_Chia.csv')
growth_Chickpea = pd.read_csv('results/growth_rates_Chickpea.csv')
growth_Green_peas = pd.read_csv('results/growth_rates_Green_peas.csv')
growth_Hazelnut = pd.read_csv('results/growth_rates_Hazelnut.csv')
growth_Lentils = pd.read_csv('results/growth_rates_Lentils.csv')
growth_Peanut = pd.read_csv('results/growth_rates_Peanut.csv')
growth_Pecans = pd.read_csv('results/growth_rates_Pecans.csv')
growth_Pumpkin_seed = pd.read_csv('results/growth_rates_Pumpkin_seed.csv')
growth_Red_beans = pd.read_csv('results/growth_rates_Red_beans.csv')
growth_Soybean = pd.read_csv('results/growth_rates_Soybean.csv')
growth_Split_peas = pd.read_csv('results/growth_rates_Split_peas.csv')
growth_Sunflower_seed = pd.read_csv('results/growth_rates_Sunflower_seed.csv')
growth_White_beans = pd.read_csv('results/growth_rates_White_beans.csv')
growth_Zucchini = pd.read_csv('results/growth_rates_Zucchini.csv')
growth_Peache = pd.read_csv('results/growth_rates_Peache.csv')
growth_Cashew = pd.read_csv('results/growth_rates_Cashew.csv')
growth_Codfish = pd.read_csv('results/growth_rates_Codfish.csv')
growth_Tuna = pd.read_csv('results/growth_rates_Tuna.csv')
growth_Cucumber = pd.read_csv('results/growth_rates_Cucumber.csv')
growth_Pumpkin = pd.read_csv('results/growth_rates_Pumpkin.csv')
growth_Grape = pd.read_csv('results/growth_rates_Grape.csv')
growth_Barley = pd.read_csv('results/growth_rates_Barley.csv')
growth_Rice = pd.read_csv('results/growth_rates_Rice.csv')
growth_Control_Breastmilk = pd.read_csv('results/growth_rates_Control_Breastmilk.csv')
growth_Control_Infant_formula = pd.read_csv('results/growth_rates_Control_Infant_formula.csv')

growth_Broccoli['diet'] = 'Broccoli' 
growth_Brussel['diet'] = 'Brussel' 
growth_Cabbage['diet'] = 'Cabbage' 
growth_Carrot['diet'] = 'Carrot' 
growth_Cauliflower['diet'] = 'Cauliflower' 
growth_Celery['diet'] = 'Celery' 
growth_Eggplant['diet'] = 'Eggplant' 
growth_Green_beans['diet'] = 'Green_beans' 
growth_Green_capsicum['diet'] = 'Green_capsicum' 
growth_Lettuce['diet'] = 'Lettuce' 
growth_Mushroom['diet'] = 'Mushroom' 
growth_Onion['diet'] = 'Onion' 
growth_Pak_choi['diet'] = 'Pak_choi' 
growth_Potato['diet'] = 'Potato' 
growth_Sweetcorn['diet'] = 'Sweetcorn' 
growth_Spinach['diet'] = 'Spinach' 
growth_Squash['diet'] = 'Squash' 
growth_Sweet_potato['diet'] = 'Sweet_potato' 
growth_Tomato['diet'] = 'Tomato' 
growth_Yam['diet'] = 'Yam' 
growth_Apple['diet'] = 'Apple' 
growth_Banana['diet'] = 'Banana' 
growth_Blackcurrant['diet'] = 'Blackcurrant' 
growth_Blueberries['diet'] = 'Blueberries' 
growth_Cherry['diet'] = 'Cherry' 
growth_Feijoa['diet'] = 'Feijoa' 
growth_Gold_kiwifruit['diet'] = 'Gold_kiwifruit' 
growth_Grapefruit['diet'] = 'Grapefruit' 
growth_Green_kiwifruit['diet'] = 'Green_kiwifruit' 
growth_Mandarin['diet'] = 'Mandarin' 
growth_Mango['diet'] = 'Mango' 
growth_Melon['diet'] = 'Melon' 
growth_Nectarine['diet'] = 'Nectarine' 
growth_Orange['diet'] = 'Orange' 
growth_Pear['diet'] = 'Pear' 
growth_Pineapple['diet'] = 'Pineapple' 
growth_Plum['diet'] = 'Plum' 
growth_Raspberries['diet'] = 'Raspberries' 
growth_Strawberries['diet'] = 'Strawberries' 
growth_Barley_cereal['diet'] = 'Barley_cereal' 
growth_Couscous['diet'] = 'Couscous' 
growth_Noodles['diet'] = 'Noodles' 
growth_Oat_cereal['diet'] = 'Oat_cereal' 
growth_Pasta['diet'] = 'Pasta' 
growth_Rice_cereal['diet'] = 'Rice_cereal' 
growth_Tapioca_pudding['diet'] = 'Tapioca_pudding' 
growth_White_bread['diet'] = 'White_bread' 
growth_Wholegrain_bread['diet'] = 'Wholegrain_bread' 
growth_Cottage_cheese['diet'] = 'Cottage_cheese' 
growth_Eggs['diet'] = 'Eggs' 
growth_Mozzarella_cheese['diet'] = 'Mozzarella_cheese' 
growth_Soymilk['diet'] = 'Soymilk' 
growth_Tofu['diet'] = 'Tofu' 
growth_Whole_milk['diet'] = 'Whole_milk' 
growth_Yoghurt['diet'] = 'Yoghurt' 
growth_Beef['diet'] = 'Beef' 
growth_Chicken['diet'] = 'Chicken' 
growth_Lamb['diet'] = 'Lamb' 
growth_Mackerel['diet'] = 'Mackerel' 
growth_Mussels['diet'] = 'Mussels' 
growth_Pork['diet'] = 'Pork' 
growth_Salmon['diet'] = 'Salmon' 
growth_Shrimp['diet'] = 'Shrimp' 
growth_Turkey['diet'] = 'Turkey' 
growth_Almond['diet'] = 'Almond' 
growth_Black_beans['diet'] = 'Black_beans' 
growth_Chia['diet'] = 'Chia' 
growth_Chickpea['diet'] = 'Chickpea' 
growth_Green_peas['diet'] = 'Green_peas' 
growth_Hazelnut['diet'] = 'Hazelnut' 
growth_Lentils['diet'] = 'Lentils' 
growth_Peanut['diet'] = 'Peanut' 
growth_Pecans['diet'] = 'Pecans' 
growth_Pumpkin_seed['diet'] = 'Pumpkin_seed' 
growth_Red_beans['diet'] = 'Red_beans' 
growth_Soybean['diet'] = 'Soybean' 
growth_Split_peas['diet'] = 'Split_peas' 
growth_Sunflower_seed['diet'] = 'Sunflower_seed' 
growth_White_beans['diet'] = 'White_beans' 
growth_Zucchini['diet'] = 'Zucchini' 
growth_Peache['diet'] = 'Peache' 
growth_Cashew['diet'] = 'Cashew' 
growth_Codfish['diet'] = 'Codfish' 
growth_Tuna['diet'] = 'Tuna' 
growth_Cucumber['diet'] = 'Cucumber' 
growth_Pumpkin['diet'] = 'Pumpkin' 
growth_Grape['diet'] = 'Grape' 
growth_Barley['diet'] = 'Barley' 
growth_Rice['diet'] = 'Rice' 
growth_Control_Breastmilk['diet'] = 'Control_Breastmilk' 
growth_Control_Infant_formula['diet'] = 'Control_Infant_formula' 

growth_rates = pd.concat([growth_Broccoli,growth_Brussel,growth_Cabbage,growth_Carrot,growth_Cauliflower,
                          growth_Celery,growth_Eggplant,growth_Green_beans,growth_Green_capsicum,growth_Lettuce,
                          growth_Mushroom,growth_Onion,growth_Pak_choi,growth_Potato,growth_Sweetcorn,
                          growth_Spinach,growth_Squash,growth_Sweet_potato,growth_Tomato,growth_Yam,
                          growth_Apple,growth_Banana,growth_Blackcurrant,growth_Blueberries,growth_Cherry,
                          growth_Feijoa,growth_Gold_kiwifruit,growth_Grapefruit,growth_Green_kiwifruit,growth_Mandarin,
                          growth_Mango,growth_Melon,growth_Nectarine,growth_Orange,growth_Pear,
                          growth_Pineapple,growth_Plum,growth_Raspberries,growth_Strawberries,growth_Barley_cereal,
                          growth_Couscous,growth_Noodles,growth_Oat_cereal,growth_Pasta,growth_Rice_cereal,
                          growth_Tapioca_pudding,growth_White_bread,growth_Wholegrain_bread,growth_Cottage_cheese,growth_Eggs,
                          growth_Mozzarella_cheese,growth_Soymilk,growth_Tofu,growth_Whole_milk,growth_Yoghurt,
                          growth_Beef,growth_Chicken,growth_Lamb,growth_Mackerel,growth_Mussels,
                          growth_Pork,growth_Salmon,growth_Shrimp,growth_Turkey,growth_Almond,
                          growth_Black_beans,growth_Chia,growth_Chickpea,growth_Green_peas,growth_Hazelnut,
                          growth_Lentils,growth_Peanut,growth_Pecans,growth_Pumpkin_seed,growth_Red_beans,
                          growth_Soybean,growth_Split_peas,growth_Sunflower_seed,growth_White_beans,growth_Zucchini,
                          growth_Peache,growth_Cashew,growth_Codfish,growth_Tuna,growth_Cucumber,
                          growth_Pumpkin,growth_Grape,growth_Barley,growth_Rice,
                          growth_Control_Breastmilk,growth_Control_Infant_formula])  # merging the growth rates
growth_rates = pd.pivot_table(growth_rates, index = ["diet"], columns = "taxon", values = "growth_rate") #pivoting the table
growth_rates.to_csv("results/growth_rates.csv")