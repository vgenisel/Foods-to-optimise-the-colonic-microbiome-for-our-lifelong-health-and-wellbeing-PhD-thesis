#Loading the packages
library(BacArena)

#Loading the default conditions of diet and microbial community - they are found as supplementary material in the article
diet = read.csv("TableS1.csv",header=T) #loading diet information - table S1 is found in the article as supp material
load("FileS2.RData") #loading metabolic models as R list "sihumi" with models - found in the article as supp material

#Running the simulation using default conditions
arena <- Arena(100, 100, stir=F, Lx=0.025, Ly=0.025, tstep=1) #defining the arena as default conditions - conditions found in the article
for(i in 1:length(sihumi)){ #adding bacterial species to the arena
  model = sihumi[[i]]
  bac = Bac(model=model, growtype="exponential", speed=10)
  arena = addOrg(arena, bac, amount=200)
}

diet = diet[which(diet$Exchange %in% arena@mediac),] #ensure that all diet components can be used by the models
muc = as.character(diet$Exchange[which(diet$category=="mucin")]) #create a vector with only mucus glycans
arena = addSubs(arena, smax=diet$concentration.im.mM,difspeed=diet$diffconstant,unit="mM",
                mediac=as.character(diet$Exchange)) #add metabolites to environment
arena = createGradient(arena,smax=1e-03,mediac=muc,position='left',steep=0.5,add=T,unit="mM") #add a mucus gradient

sim_default <- simEnv(arena, time=10) #simulate for 10h

#Plotting the results for default condition
plotCurves2(sim_default, legendpos = "topleft", subs = list("EX_ac(e)", "EX_ppa(e)", "EX_but(e)")) #growth and resources over time
plotAbundance(sim_default) #changes in microbial abundance over time
plotGrowthCurve(sim_default, use_biomass = T) #only growth

#Adding new microbial species using the AGORA reconstructions
#Loading the reconstructions
mod1 <- readMATmod("Akkermansia_muciniphila_ATCC_BAA_835.mat")
mod2 <- readMATmod("Eubacterium_rectale_M104_1.mat")
mod3 <- readMATmod("Methanobrevibacter_smithii_ATCC_35061.mat")
mod4 <- readMATmod("Prevotella_copri_CB7_DSM_18205.mat")
mod5 <- readMATmod("Ruminococcus_bromii_L2_63.mat")
#Adding them to the arena
arena <- addOrg(arena, Bac(model=mod1,growtype="exponential", speed=10), amount=200)
arena <- addOrg(arena, Bac(model=mod2,growtype="exponential", speed=10), amount=200)
arena <- addOrg(arena, Bac(model=mod3,growtype="exponential", speed=10), amount=200)
arena <- addOrg(arena, Bac(model=mod4,growtype="exponential", speed=10), amount=200)
arena <- addOrg(arena, Bac(model=mod5,growtype="exponential", speed=10), amount=200)

#Runing the new simulation
sim_microbes <- simEnv(arena, time=10)

#Plotting the results for the new simulation
plotCurves2(sim_microbes, legendpos = "topleft", subs = list("EX_ac(e)", "EX_ppa(e)", "EX_but(e)")) #growth and resources over time
plotAbundance(sim_microbes) #changes in microbial abundance over time
plotGrowthCurve(sim_microbes, use_biomass = T) #only growth

#Comparing results between the simulations
#Default conditions
getVarSubs(sim_default) #look at substances having higher variations
getSubHist(sim_default, "EX_but(e)") #looking at the SCFA
getSubHist(sim_default, "EX_ppa(e)") #looking at the SCFA
getSubHist(sim_default, "EX_ac(e)") #looking at the SCFA
#New microbial community
getVarSubs(sim_microbes) #look at substances having higher variations
getSubHist(sim_microbes, "EX_but(e)") #looking at the SCFA
getSubHist(sim_microbes, "EX_ppa(e)") #looking at the SCFA
getSubHist(sim_microbes, "EX_ac(e)") #looking at the SCFA
