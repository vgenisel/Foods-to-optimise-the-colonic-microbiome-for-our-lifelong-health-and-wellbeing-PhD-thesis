#Loading the library
library(microPopGut)

#defining the microbial functional groups as default

microbeNames = c('Bacteroides','ButyrateProducers1','ButyrateProducers2','ButyrateProducers3', #loading the 10 microbial
                 'LactateProducers','PropionateProducers','Methanogens','NoButyFibreDeg',      #functional groups
                 'NoButyStarchDeg','Acetogens')

microbeNames.short = c('Bacteroides'= 'Bacteroides','ButyrateProducers1'='Butryate1',
                       'ButyrateProducers2'='Butyrate2','ButyrateProducers3'='Butyrate3',
                       'LactateProducers'='Lactate','PropionateProducers'='Propionate',
                       'Methanogens'='Methanogens','NoButyFibreDeg'='FibreDeg',
                       'NoButyStarchDeg'='StarchDeg','Acetogens'='Acetogens')

#Change pH tolerance & Gmax(RS) for lactate producers
#as proposed in the tutorial
LactateProducers['pHcorners',2:5]=c(4.5,5.25,7.2,7.95)
LactateProducers['maxGrowthRate','RS']=7


#Running the model in the default conditions
#Here the inflow of carbohydrates is 50 g/d and the RS fraction is 0.78. The inflow of proteins is 10 g/d

m.out_default=microPopGut(
  numDays=1,
  time.step=1/24/60,
  transitTime=1.25,
  microbeNames=microbeNames,
  microbeNames.short=microbeNames.short,
  #initial mass in each compartment - default conditions
  init=list(  #define the initial conditions
    C=2, #carbohydrate (g)
    P=0, #protein (g)
    B=10, #biomass (g)
    Acetate=0.3606, #g
    Propionate=0.1482, #g
    Butyrate=0.1762, #g
    W=100), #water (g)
  
  #inflow from diet - default conditions
  inflow=list(  #define the nutrients brought by diet
    C=50, #carbohydrate (g/d)
    P=10, #protein (g/d)
    W=1100, #water (g/d)
    RS.frac=0.78), #fraction of carbohydrates that are resistant starch (the rest is non-starch polysaccharides)
  
  plotOptions= list(microbeLegendPosition="")
  )

#viewing results
time=m.out_default$solution[[1]][,'time']
verification(m.out_default,start.av=0.999*max(time),fin.av=max(time))
dev.new()
plotMPG(m.out_default)

##Running a high-protein-low-fibre diet
#The inflow of carbohydrates is changed to 30 g/d and the RS fraction to 0.3. The inflow of proteins is increased to 30 g/d

m.out_protein=microPopGut(
  numDays=1,
  time.step=1/24/60,
  transitTime=1.25,
  microbeNames=microbeNames,
  microbeNames.short=microbeNames.short,
  #initial mass in each compartment
  init=list(  #define the initial conditions - same to the default 
    C=2, #carbohydrate (g)
    P=0, #protein (g)
    B=10, #biomass (g)
    Acetate=0.3606, #g
    Propionate=0.1482, #g
    Butyrate=0.1762, #g
    W=100), #water (g)
  
  #inflow from diet
  inflow=list(  #define the nutrients brought by diet
    C=30, #carbohydrate (g/d)
    P=30, #protein (g/d)
    W=1100, #water (g/d)
    RS.frac=0.3) #fraction of C that is resistant starch (rest is NSP)
)


#viewing results
time=m.out_protein$solution[[1]][,'time']
verification(m.out_protein,start.av=0.999*max(time),fin.av=max(time))
dev.new()
plotMPG(m.out_protein)

##Running a high-fibre diet
#The inflow of carbohydrates is increased to 55 g/d and the RS fraction to 0.9. The inflow of proteins is decreased to 5 g/d

m.out_fibre=microPopGut(
  numDays=1,
  time.step=1/24/60,
  transitTime=1.25,
  microbeNames=microbeNames,
  microbeNames.short=microbeNames.short,
  #initial mass in each compartment
  init=list(  #define the initial conditions - same to the default
    C=2, #carbohydrate (g)
    P=0, #protein (g)
    B=10, #biomass (g)
    Acetate=0.3606, #g
    Propionate=0.1482, #g
    Butyrate=0.1762, #g
    W=100), #water (g)
  
  #inflow from diet
  inflow=list(  #define the nutrients brought by diet
    C=55, #carbohydrate (g/d)
    P=5, #protein (g/d)
    W=1100, #water (g/d)
    RS.frac=0.9) #fraction of C that is resistant starch (rest is NSP)
)

#viewing results
time=m.out_fibre$solution[[1]][,'time']
verification(m.out_fibre,start.av=0.999*max(time),fin.av=max(time))
dev.new()
plotMPG(m.out_fibre)


##Comparing the results of microbial biomass

#High-protein-low-fibre diet
m.out_protein[["solution"]][[3]][nrow(m.out_protein[["solution"]][[3]]),c('Bacteroides','NoButyStarchDeg','NoButyFibreDeg','LactateProducers', 
                                                                          'ButyrateProducers1','ButyrateProducers2','ButyrateProducers3',
                                                                          'PropionateProducers','Acetogens','Methanogens')]     #Bacteroides

#High-fibre diet
m.out_fibre[["solution"]][[3]][nrow(m.out_fibre[["solution"]][[3]]),c('Bacteroides','NoButyStarchDeg','NoButyFibreDeg','LactateProducers', 
                                                                      'ButyrateProducers1','ButyrateProducers2','ButyrateProducers3',
                                                                      'PropionateProducers','Acetogens','Methanogens')]

#Default conditions
m.out_default[["solution"]][[3]][nrow(m.out_default[["solution"]][[3]]),c('Bacteroides','NoButyStarchDeg','NoButyFibreDeg','LactateProducers', 
                                                                           'ButyrateProducers1','ButyrateProducers2','ButyrateProducers3',
                                                                           'PropionateProducers','Acetogens','Methanogens')]

m.out_default[["solution"]][[3]][nrow(m.out_default[["solution"]][[3]]),c('Acetate','Propionate', 'Butyrate')]     #high-fibre diet