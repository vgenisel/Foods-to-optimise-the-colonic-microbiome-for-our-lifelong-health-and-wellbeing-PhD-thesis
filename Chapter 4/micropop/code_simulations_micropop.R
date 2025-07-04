##Simulating the default conditions for the colonic microbiota in microPop

#load the necessary library
library(microPop)

#Running the model in the default conditions
  #we run the model using the 10 proposed microbial functional groups
  #and using the standard conditions of resources and microbes in the colon (these are found as excel sheets in the model files)

out_default=microPopModel( #calling the model
  microbeNames=c('Bacteroides','NoButyStarchDeg','NoButyFibreDeg','LactateProducers', #we use the 10 microbial function groups
                 'ButyrateProducers1','ButyrateProducers2','ButyrateProducers3',
                 'PropionateProducers','Acetogens','Methanogens'),
  times=seq(0,24,1/24), #running the simulation for 24 hours
  resourceSysInfo=resourceSysInfoHuman, #we use the standard resources in the colon
  microbeSysInfo=microbeSysInfoHuman, #we use the standard microbial composition in the colon
  plotOptions = list(plotFig=TRUE, sumOverStrains=FALSE, resourceLegendPosition="topright",
                     microbeLegendPosition="topright", saveFig=FALSE, figType='eps',
                     figName='microPopFig', yLabel='Concentration (g/L)', xLabel='Time')
)

##Increasing the initial concentration and inflow of protein in the colon and decreasing the RS (high protein low fibre diet)

  #we can view the standard conditions, clone into a new variable and further modify it
resourceSysInfoHuman #protein start value = 5.9 g/l and inflow = 5.9 g/l/d, RS is 5.6 g/l and g/l/d respectively
resourceSysInfo_protein <- resourceSysInfoHuman #cloning
resourceSysInfo_protein["startValue", "Protein"] <- 8.9 #making a start value of 8.9 g/l of protein
resourceSysInfo_protein["inflowRate", "Protein"] <- 8.9 #making a inflowRate of 8.9 g/l/d of protein
resourceSysInfo_protein["startValue", "RS"] <- 3.0 #making a start value of 2.6 g/l of RS
resourceSysInfo_protein["inflowRate", "RS"] <- 3.0 #making a inflowRate of 2.6 g/l/d of RS
resourceSysInfo_protein["startValue", "NSP"] <- 1.22 #making a start value of 2.6 g/l of NSP
resourceSysInfo_protein["inflowRate", "NSP"] <- 1.22 #making a inflowRate of 2.6 g/l/d of NSP

  #now we run the model
out_protein=microPopModel( #calling the model with the new conditions
  microbeNames=c('Bacteroides','NoButyStarchDeg','NoButyFibreDeg','LactateProducers', #we use the 10 microbial function groups
                 'ButyrateProducers1','ButyrateProducers2','ButyrateProducers3',
                 'PropionateProducers','Acetogens','Methanogens'),
  times=seq(0,24,1/24), #running the simulation for 4 hours
  resourceSysInfo=resourceSysInfo_protein, #we use the new amount of protein in the colon
  microbeSysInfo=microbeSysInfoHuman, #we use the standard microbial composition in the colon
  plotOptions = list(plotFig=TRUE, sumOverStrains=FALSE, resourceLegendPosition="topright",
                     microbeLegendPosition="topright", saveFig=FALSE, figType='eps',
                     figName='microPopFig', yLabel='Concentration (g/L)', xLabel='Time')
)

##Increasing the initial concentration and inflow of RS in the colon and decreasing the protein (high fibre diet)

  #we can view the standard conditions, clone into a new variable and further modify it
resourceSysInfoHuman #protein start value = 5.9 g/l and inflow = 5.9 g/l/d, RS is 5.6 g/l and g/l/d respectively
resourceSysInfo_fibre <- resourceSysInfoHuman #cloning
resourceSysInfo_fibre["startValue", "Protein"] <- 2.9 #making a start value of 10 g/l of protein
resourceSysInfo_fibre["inflowRate", "Protein"] <- 2.9 #making a inflowRate of 10 g/l/d of protein
resourceSysInfo_fibre["startValue", "RS"] <- 8.2 #making a start value of 10 g/l of protein
resourceSysInfo_fibre["inflowRate", "RS"] <- 8.2 #making a inflowRate of 10 g/l/d of protein
resourceSysInfo_fibre["startValue", "NSP"] <- 2.02 #making a start value of 2.6 g/l of NSP
resourceSysInfo_fibre["inflowRate", "NSP"] <- 2.02 #making a inflowRate of 2.6 g/l/d of NSP

  #now we run the model
out_fibre=microPopModel( #calling the model with the new conditions
  microbeNames=c('Bacteroides','NoButyStarchDeg','NoButyFibreDeg','LactateProducers', #we use the 10 microbial function groups
                 'ButyrateProducers1','ButyrateProducers2','ButyrateProducers3',
                 'PropionateProducers','Acetogens','Methanogens'),
  times=seq(0,24,1/24), #running the simulation for 4 hours
  resourceSysInfo=resourceSysInfo_fibre, #we use the new amount of fibre in the colon
  microbeSysInfo=microbeSysInfoHuman, #we use the standard microbial composition in the colon
  plotOptions = list(plotFig=TRUE, sumOverStrains=FALSE, resourceLegendPosition="topright",
                     microbeLegendPosition="topright", saveFig=FALSE, figType='eps',
                     figName='microPopFig', yLabel='Concentration (g/L)', xLabel='Time')
)

##Comparing the results
#SCFA
out_default$solution[nrow(out_default$solution),c('Acetate','Propionate', 'Butyrate')] #default
out_protein$solution[nrow(out_protein$solution),c('Acetate','Propionate', 'Butyrate')] #high-protein-low-fibre diet
out_fibre$solution[nrow(out_fibre$solution),c('Acetate','Propionate', 'Butyrate')]     #high-fibre diet

#microbial functional groups
out_default$solution[nrow(out_default$solution),c('Bacteroides','NoButyStarchDeg','NoButyFibreDeg','LactateProducers', 
                                                  'ButyrateProducers1','ButyrateProducers2','ButyrateProducers3',
                                                  'PropionateProducers','Acetogens','Methanogens')] #default
out_protein$solution[nrow(out_protein$solution),c('Bacteroides','NoButyStarchDeg','NoButyFibreDeg','LactateProducers', 
                                                  'ButyrateProducers1','ButyrateProducers2','ButyrateProducers3',
                                                  'PropionateProducers','Acetogens','Methanogens')] #high-protein-low-fibre diet
out_fibre$solution[nrow(out_fibre$solution),c('Bacteroides','NoButyStarchDeg','NoButyFibreDeg','LactateProducers', 
                                              'ButyrateProducers1','ButyrateProducers2','ButyrateProducers3',
                                              'PropionateProducers','Acetogens','Methanogens')]     #high-fibre diet




