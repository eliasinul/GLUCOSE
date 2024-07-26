#%%
# from itertools import tee
# from math import prod
# from unittest import skip

import prim
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from pathlib import Path

import os

import glob

import pickle

folder = 'GLUCOSE_withAEL_220809'

myPath = Path(f'{folder}', 'results', '0')
tifCounter = len(glob.glob1(myPath,"*.ilp"))
print('Infeasible scenarios:', tifCounter)

#data processing from GLUCOSE scenarios runs
#creating a database with yearly data inputs
#configfile: "config/config.yaml"

myPath = Path(f'{folder}','results', '0')
n_replications = int(len(glob.glob1(myPath,"*.sol")))
print("Number of replications/runs:", n_replications)
replications = list(range(0,n_replications))

#%% read in parameter data

FUEL = pd.read_csv(Path(f'{folder}', 'results', '0', f'model_0', 'data', 'FUEL.csv'))
TECH = pd.read_csv(Path(f'{folder}', 'results', '0', f'model_0', 'data', 'TECHNOLOGY.csv'))

#energy fuels
energy_fuel = FUEL.loc[(FUEL.VALUE.str[0:2] == 'C1')]
PrimEN_fuel = (energy_fuel.loc[(energy_fuel.VALUE.str[3:4] == 'P')|(energy_fuel.VALUE.str[3:4] == 'R')]).VALUE.unique()
SecEN_fuel = (energy_fuel.loc[(energy_fuel.VALUE.str[3:4] == 'S')]).VALUE.unique()
FinalEN_fuel = (energy_fuel.loc[(energy_fuel.VALUE.str[3:4] == 'F')]).VALUE.unique()
#energy techs
energy_tech = TECH.loc[(TECH.VALUE.str[0:2] == 'C1')]
ResEN_tech = (energy_tech.loc[(energy_tech.VALUE.str[6:7] == 'I')]).VALUE.unique()
RE_tech = (energy_tech.loc[(energy_tech.VALUE.str[2:4] == 'SO')|(energy_tech.VALUE.str[2:4] == 'WD')|(energy_tech.VALUE.str[2:4] == 'HY')|(energy_tech.VALUE.str[2:4] == 'GO')|(energy_tech.VALUE.str[2:4] == 'OC')]).VALUE.unique()
PrimEN_tech = (energy_tech.loc[(energy_tech.VALUE.str[6:7] == 'P')|(energy_tech.VALUE.str[6:7] == '0')]).VALUE.unique()
SecEN_tech = (energy_tech.loc[(energy_tech.VALUE.str[6:7] == 'T')]).VALUE.unique()
FinalEN_tech = (energy_tech.loc[(energy_tech.VALUE.str[6:7] == 'F')]).VALUE.unique()

#land and food fuels
land_fuel = (FUEL.loc[(FUEL.VALUE.str[0:1] == 'L')]).VALUE.unique()
food_fuel = (FUEL.loc[(FUEL.VALUE.str[0:1] == 'M')|(FUEL.VALUE.str[0:1] == 'V')]).VALUE.unique()
#land and food techs
land_tech = (TECH.loc[(TECH.VALUE.str[0:1] == 'L')]).VALUE.unique()
food_tech = (TECH.loc[(TECH.VALUE.str[0:1] == 'M')|(TECH.VALUE.str[0:1] == 'V')]).VALUE.unique()

#materials fuels
material_fuel = (FUEL.loc[(FUEL.VALUE.str.len() == 3)]).VALUE.unique()
#materials techs
industry_tech = (TECH.loc[(TECH.VALUE.str[3:] == 'PLANT')|(TECH.VALUE.str[4:] == 'PLANT')]).VALUE.unique()
material_tech = (TECH.loc[(TECH.VALUE.str[4:] == 'MINE')]).VALUE.unique()

#emissions
EMISSION = pd.read_csv(Path(f'{folder}','results', '0', f'model_0', 'data', 'EMISSION.csv'))
emissions = (EMISSION.loc[(EMISSION.VALUE.str.len() == 5)]).VALUE.unique()

#timeframe / modelling period
YEAR = pd.read_csv(Path(f'{folder}','results', '0', f'model_0', 'data', 'YEAR.csv'))
YEAR.iloc[:-10]

parameter_file = glob.glob1(folder, '*parameters*')
parameters_GLUCOSE = pd.read_csv(Path(f'{folder}',f'{parameter_file[0]}'))
col = parameters_GLUCOSE['indexes']

#%% read in value of uncertainty inputs in 2050 - see parameters.csv file under config/ folder

inputs_GLUCOSE = pd.DataFrame(index=replications)
yr = 2050

for run in replications:
    for variable in (parameters_GLUCOSE['name']):
    #path = 'results/0/model_{run}/data/AccumulatedAnnualDemand.csv'
        csv_file_data = Path(f'{folder}','results', '0', f'model_{run}', 'data', f'{variable}.csv')
        #csv_file_data2 = Path('results', '0', f'model_{run}', 'data', 'SpecifiedAnnualDemand.csv')
        if not os.path.exists(csv_file_data):
            pass
        else:
            data=pd.read_csv(csv_file_data)
            parameters = parameters_GLUCOSE.loc[parameters_GLUCOSE['name']==variable]
            for param in parameters['indexes']:
                if variable[-6:] == 'Demand':
                    fuel = param[6:]
                    selection = data.loc[(data["FUEL"]==fuel)&(data["YEAR"]==yr)]
                    inputs_GLUCOSE.loc[run,(''.join(c for c in variable if c.isupper())+','+fuel)]=selection.VALUE.sum() 
                if (variable == 'InputActivityRatio')|(variable == 'OutputActivityRatio'):
                    technology = param.split(",")[1].strip()
                    fuel = param.split(",")[2].strip()
                    ModOp = param.split(",")[3].strip()
                    selection = data.loc[(data["TECHNOLOGY"]==technology)&(data["FUEL"]==fuel)&(data["MODE_OF_OPERATION"]==ModOp)&(data["YEAR"]==yr)]
                    inputs_GLUCOSE.loc[run,(''.join(c for c in variable if c.isupper())+','+technology+','+fuel)]=selection.VALUE.sum() 
                if (variable == 'TotalAnnualMaxCapacityInvestment')|(variable == 'TotalTechnologyAnnualActivityUpperLimit'):
                    technology = param.split(",")[1].strip()
                    selection = data.loc[(data["TECHNOLOGY"]==technology)&(data["YEAR"]==yr)]
                    inputs_GLUCOSE.loc[run,(''.join(c for c in variable if c.isupper())+','+technology)]=selection.VALUE.sum() 
                if variable == 'AnnualEmissionLimit':
                    emission = param.split(",")[1].strip()
                    selection = data.loc[(data["EMISSION"]==emission)&(data["YEAR"]==yr)]
                    inputs_GLUCOSE.loc[run,(''.join(c for c in variable if c.isupper())+','+emission)]=selection.VALUE.sum() 
                if variable == 'EmissionActivityRatio':
                    technology = param.split(",")[1].strip()
                    emission = param.split(",")[2].strip()
                    selection = data.loc[(data["TECHNOLOGY"]==technology)&(data["EMISSION"]==emission)&(data["YEAR"]==yr)]
                    inputs_GLUCOSE.loc[run,(''.join(c for c in variable if c.isupper())+','+technology+','+emission)]=selection.VALUE.sum() 

#inputs_GLUCOSE = inputs_GLUCOSE.astype(float)

output = 'GLUCOSE_DataInputs'

fp = open(f'{output}'+'.p', 'wb')
my_path = Path(f'{folder}', 'GLUCOSE_DataProcessing', f'{output}'+'.p') 
with my_path.open('wb') as fp:
    pickle.dump(inputs_GLUCOSE, fp)


#%% processing results - read in selected results for year 2050

CO2EQ_GLUCOSE = pd.DataFrame(index=replications, columns=YEAR.VALUE).fillna(0)
ccs_em = pd.DataFrame(index=replications, columns=YEAR.VALUE).fillna(0)
WATER_GLUCOSE = pd.DataFrame(index=replications, columns=YEAR.VALUE).fillna(0)
LAi_GLUC = pd.DataFrame(index=replications, columns=YEAR.VALUE).fillna(0)
LF_GLUCOSE = pd.DataFrame(index=replications, columns=YEAR.VALUE).fillna(0)
NU_prod = pd.DataFrame(index=replications, columns=YEAR.VALUE).fillna(0)
NU_cap = pd.DataFrame(index=replications, columns=YEAR.VALUE).fillna(0)
BM_use = pd.DataFrame(index=replications, columns=YEAR.VALUE).fillna(0)

for run in replications:
    results_file1 = Path(f'{folder}', 'results', '0', f'{run}', 'TotalAnnualTechnologyActivityByMode.csv')
    results_file2 = Path(f'{folder}', 'results', '0', f'{run}', 'AnnualEmissions.csv')
    results_file3 = Path(f'{folder}', 'results', '0', f'{run}', 'AnnualTechnologyEmission.csv')
    results_file4 = Path(f'{folder}', 'results', '0', f'{run}', 'ProductionByTechnologyAnnual.csv')
    results_file5 = Path(f'{folder}', 'results', '0', f'{run}', 'TotalCapacityAnnual.csv')
    results_file6 = Path(f'{folder}', 'results', '0', f'{run}', 'UseByTechnology.csv')
    if not os.path.exists(results_file1):
        pass
    else:
        TotalAnnualTechnologyActivityByMode=pd.read_csv(results_file1)
        AnnualEmissions = pd.read_csv(results_file2)
        AnnualTechnologyEmission = pd.read_csv(results_file3)
        ProductionByTechnologyAnnual = pd.read_csv(results_file4)
        TotalCapacityAnnual = pd.read_csv(results_file5)
        UseByTechnology = pd.read_csv(results_file6)        
        for year in YEAR.VALUE:
            for tech in land_tech:
                if tech == 'LF':
                    land_temp = TotalAnnualTechnologyActivityByMode[(TotalAnnualTechnologyActivityByMode['TECHNOLOGY'] == tech)&(TotalAnnualTechnologyActivityByMode['YEAR'] == year)&(TotalAnnualTechnologyActivityByMode['MODE_OF_OPERATION'] == 1)]
                    LF_GLUCOSE.loc[run, year] = land_temp['VALUE'].sum()
                if tech == 'LA1_i':
                    land_temp = TotalAnnualTechnologyActivityByMode[(TotalAnnualTechnologyActivityByMode['TECHNOLOGY'] == tech)&(TotalAnnualTechnologyActivityByMode['YEAR'] == year)&(TotalAnnualTechnologyActivityByMode['MODE_OF_OPERATION'] == 1)]
                    LAi_GLUC.loc[run, year] = land_temp['VALUE'].sum()
                for tech in PrimEN_tech:
                    if tech[2:4]=='NU':
                        production = ProductionByTechnologyAnnual[(ProductionByTechnologyAnnual['TECHNOLOGY']==tech)&(ProductionByTechnologyAnnual['YEAR']== year)]
                        capacity = TotalCapacityAnnual[(TotalCapacityAnnual['TECHNOLOGY']==tech)&(TotalCapacityAnnual['YEAR']== year)]
                        NU_prod.loc[run, year] = production['VALUE'].sum()
                        NU_cap.loc[run, year] = capacity['VALUE'].sum()
            use = UseByTechnology.loc[(UseByTechnology['TECHNOLOGY'].str[2:4]=='BM')&(UseByTechnology['FUEL']=='C1_P_BIOW')&(UseByTechnology['YEAR']==year)]
            #UseByTechnology[(UseByTechnology['FUEL']==fuel)&(UseByTechnology['TECHNOLOGY']==tech)&(UseByTechnology['YEAR']==year)]
            BM_use.loc[run, year]+= use['VALUE'].sum()
            for ems in emissions:
                if ems == 'CO2EQ':
                    em = AnnualEmissions[(AnnualEmissions['EMISSION'] == ems)&(AnnualEmissions['YEAR'] == year)]
                    AnnualTechnologyEmission_ccs = AnnualTechnologyEmission.loc[(AnnualTechnologyEmission['TECHNOLOGY'].str[-2:] == 'CS')]
                    AnnualTechnologyEmission_ccs_em = AnnualTechnologyEmission_ccs[(AnnualTechnologyEmission_ccs['EMISSION'] == ems)&(AnnualTechnologyEmission_ccs['YEAR'] == year)]
                    CO2EQ_GLUCOSE.loc[run, year] = em.VALUE.sum()# em['VALUE'].values
                    if not AnnualTechnologyEmission_ccs_em.empty:
                        #AnnualTechnologyEmission_ccs = (AnnualTechnologyEmission.loc[(AnnualTechnologyEmission['TECHNOLOGY'].str[-2:] == 'CS')])[(AnnualTechnologyEmission['EMISSION'] == ems)&(AnnualTechnologyEmission['YEAR'] == year)]
                        ccs_em.loc[run, year] = AnnualTechnologyEmission_ccs_em.VALUE.sum()
                if ems == 'WATER':
                    em = AnnualEmissions[(AnnualEmissions['EMISSION'] == ems)&(AnnualEmissions['YEAR'] == year)]
                    WATER_GLUCOSE.loc[run, year] = em.VALUE.sum()

#%% read in GLUCOSE results: ProductionByTechnologyAnnual - Primary Energy
PrimEn = {}
RE_tech = pd.Series(RE_tech).str[2:4].unique()
#ResEN_tech = pd.Series(ResEN_tech).str[2:4].unique()
ResEN_tech = np.append(ResEN_tech, 'BM')

for run in replications:
    PrimEn[run] = pd.DataFrame(index=YEAR.VALUE, columns=(list(ResEN_tech)+list(RE_tech))).fillna(0)
    results_file1 = Path(f'{folder}', 'results', '0', f'{run}', 'ProductionByTechnologyAnnual.csv')
    results_file2 = Path(f'{folder}', 'results', '0', f'{run}', 'UseByTechnology.csv')
    if not os.path.exists(results_file1):
        pass
    else:
        ProductionByTechnologyAnnual=pd.read_csv(results_file1)
        UseByTechnology=pd.read_csv(results_file2)
        for year in YEAR.VALUE:
            for tech in ResEN_tech:
                PrimEn_temp = ProductionByTechnologyAnnual[(ProductionByTechnologyAnnual['TECHNOLOGY'] == tech)&(ProductionByTechnologyAnnual['YEAR'] == year)]
                PrimEn[run].loc[year,tech] = PrimEn_temp['VALUE'].sum()
            Use_temp = UseByTechnology.loc[(UseByTechnology['TECHNOLOGY'].str[2:4]=='BM')&(UseByTechnology['FUEL']=='C1_P_BIOW')&(UseByTechnology['YEAR']==year)]
            PrimEn[run].loc[year, 'BM']+= Use_temp['VALUE'].sum()
            for tech in RE_tech:
                PrimREn_temp = ProductionByTechnologyAnnual.loc[(ProductionByTechnologyAnnual['TECHNOLOGY'].str[2:4] == tech)&(ProductionByTechnologyAnnual['YEAR'] == year)]
                PrimEn[run].loc[year, tech] = PrimREn_temp['VALUE'].sum()

output = 'GLUCOSE_PrimaryEnergy'

fp = open(f'{output}'+'.p', 'wb')
my_path = Path(f'{folder}', 'GLUCOSE_DataProcessing', f'{output}'+'.p') 
with my_path.open('wb') as fp:
    pickle.dump(PrimEn, fp)

#%% plotting GLUCOSE results: ProductionByTechnologyAnnual - Primary Energy
PrimEn[1].plot.area()
PrimEn[50].plot.area()
PrimEn[99].plot.area()

#%% read in GLUCOSE results: TotalCapacityAnnual - Electrical Capacity
Capacity_elc = {}
#RE_tech = pd.Series(RE_tech).str[2:4].unique()
PrimEN_tech_abb = (pd.Series(PrimEN_tech).str[2:4].unique())
#PrimEN_tech = np.append(PrimEN_tech, 'BM')

for run in replications:
    Capacity_elc[run] = pd.DataFrame(index=YEAR.VALUE, columns=(list(PrimEN_tech_abb))).fillna(0)
    results_file1 = Path(f'{folder}', 'results', '0', f'{run}', 'TotalCapacityAnnual.csv')
    results_file2 = Path(f'{folder}', 'results', '0', f'model_{run}', 'data', 'OutputActivityRatio.csv')
    if not os.path.exists(results_file1)|os.path.exists(results_file2):
        pass
    else:
        TotalCapacityAnnual=pd.read_csv(results_file1)
        OutputActivityRatio=pd.read_csv(results_file2)
        for year in YEAR.VALUE:
            for tech in PrimEN_tech:
                OAR = (OutputActivityRatio[(OutputActivityRatio['TECHNOLOGY'] == tech)&(OutputActivityRatio['YEAR'] == year)&(OutputActivityRatio['MODE_OF_OPERATION'] == 1)]).FUEL
                for oar in OAR:
                    if oar == 'C1_S_ELC':
                        Capacity_elc_temp = TotalCapacityAnnual[(TotalCapacityAnnual['TECHNOLOGY'] == tech)&(TotalCapacityAnnual['YEAR'] == year)]
                        tech_abb = tech[2:4]
                        Capacity_elc[run].loc[year,tech_abb] += Capacity_elc_temp['VALUE'].sum()
            # Use_temp = UseByTechnology.loc[(UseByTechnology['TECHNOLOGY'].str[2:4]=='BM')&(UseByTechnology['FUEL']=='C1_P_BIOW')&(UseByTechnology['YEAR']==year)]
            # PrimEn[run].loc[year, 'BM']+= Use_temp['VALUE'].sum()
            # for tech in RE_tech:
            #     TPES_temp = ProductionByTechnologyAnnual.loc[(ProductionByTechnologyAnnual['TECHNOLOGY'].str[2:4] == tech)&(ProductionByTechnologyAnnual['YEAR'] == year)]
            #     TPES[run].loc[year, tech] = TPES_temp['VALUE'].sum()

output = 'GLUCOSE_ElectricalCapacity'

fp = open(f'{output}'+'.p', 'wb')
my_path = Path(f'{folder}', 'GLUCOSE_DataProcessing', f'{output}'+'.p') 
with my_path.open('wb') as fp:
    pickle.dump(Capacity_elc, fp)


#%% plotting GLUCOSE results: TotalCapacityAnnual - Electrical Capacity
Capacity_elc[1].plot.area()
Capacity_elc[50].plot.area()
Capacity_elc[99].plot.area()

#%% read in GLUCOSE results: TotalAnnualTechnologyActivityByMode - Land Use
# land = {}
# for tech in land_tech:
#     land[tech]=pd.DataFrame(index=YEAR.VALUE, columns=(list(land_tech))).fillna(0)

# for run in replications:
#     results_file1 = Path(f'{folder}', 'results', '0', f'{run}', 'TotalAnnualTechnologyActivityByMode.csv')
#     if not os.path.exists(results_file1):
#         pass
#     else:
#         TotalAnnualTechnologyActivityByMode=pd.read_csv(results_file1)
#         for year in YEAR.VALUE:
#             for tech in land_tech:
#                 land_temp = TotalAnnualTechnologyActivityByMode[(TotalAnnualTechnologyActivityByMode['TECHNOLOGY'] == tech)&(TotalAnnualTechnologyActivityByMode['YEAR'] == year)&(TotalAnnualTechnologyActivityByMode['MODE_OF_OPERATION'] == 1)]
#                 land[tech].loc[run, year] = land_temp['VALUE'].sum()
#%% read in GLUCOSE results: TotalAnnualTechnologyActivityByMode - Land Use
LandResources = {}
land_tech = ['LA1', 'LA1_i', 'LA2', 'LF1', 'LF2', 'LO']
# for tech in land_tech:
#     LandResources[run]=pd.DataFrame(index=YEAR.VALUE, columns=land_tech).fillna(0)

for run in replications:
    LandResources[run]=pd.DataFrame(index=YEAR.VALUE, columns=(list(land_tech))).fillna(0)
    results_file1 = Path(f'{folder}', 'results', '0', f'{run}', 'TotalAnnualTechnologyActivityByMode.csv')
    if not os.path.exists(results_file1):
        pass
    else:
        TotalAnnualTechnologyActivityByMode=pd.read_csv(results_file1)
        for year in YEAR.VALUE:
            for tech in land_tech:
                Land_temp = TotalAnnualTechnologyActivityByMode[(TotalAnnualTechnologyActivityByMode['TECHNOLOGY'] == tech)&(TotalAnnualTechnologyActivityByMode['YEAR'] == year)&(TotalAnnualTechnologyActivityByMode['MODE_OF_OPERATION'] == 1)]
                LandResources[run].loc[year, tech] = Land_temp['VALUE'].sum()

output = 'GLUCOSE_LandUse'

fp = open(f'{output}'+'.p', 'wb')
my_path = Path(f'{folder}', 'GLUCOSE_DataProcessing', f'{output}'+'.p') 
with my_path.open('wb') as fp:
    pickle.dump(LandResources, fp)

#%% plotting GLUCOSE results: TotalAnnualTechnologyActivityByMode - Land Use
LandResources[1].plot.area()
LandResources[50].plot.area()
LandResources[99].plot.area()

#%%
# forest1 = land['LF1'].T
# ax = forest1.plot()
# forest2 = land['LF2'].T
# bx = forest2.plot()
# forest_tot = land['LF'].T
# abx = forest_tot.plot()

# rainfed = land['LA1'].T
# cx = rainfed.plot(legend=False)
# irrigated = land['LA1_i'].T
# dx = irrigated.plot(legend=False)
# LA_tot = land['LA']
# cdx = LA_tot.plot(legend=False)

# pasture = land['LA2'].T
# ex = pasture.plot()

# land_tot = land['LandRes'].T
# fx = land_tot.plot()

# other_land = land['LO'].T
# gx = other_land.plot()

#%% applying the PRIM algorithm - linking results with input data
# define solution space of interest (restricted dimensions for the PRIM algorithm to function)

# forest = LF_GLUCOSE[2050]>= LF_GLUCOSE[2020]
# forest_ofinterest = (forest>4000)

# irrigated = LAi_GLUC[2035] 
# i = LAi_GLUC.T
# ix = i.plot(legend=False)
# irrigated_ofinterest = (irrigated<1000)

# ccs = ccs_em[2035]

# water = WATER_GLUCOSE[2050] #<= WATER_GLUCOSE[2020]
# w = WATER_GLUCOSE.T
# wx=w.plot(legend=False)
# WATER_ofinterest = (water<50)

# nuclear_cap = NU_cap[2050]  #NU_cap[2020]

#%%
# GHG emissions by 2050
co2eq = CO2EQ_GLUCOSE[2050]
CO2EQ_ofinterest = (co2eq<5)

#%% read in GLUCOSE results: ProductionByTechnologyAnnual - Primary Energy, RENEWABLES
# RE penetration 
RE_prod = pd.DataFrame(index=replications, columns=YEAR.VALUE).fillna(0)
for run in replications:
    PrimEn_RE = PrimEn[run].iloc[: , -6:].sum(axis=1)
    RE_prod.iloc[run] = PrimEn_RE.transpose()

output = 'GLUCOSE_PrimaryEnergy_RE'

fp = open(f'{output}'+'.p', 'wb')
my_path = Path(f'{folder}', 'GLUCOSE_DataProcessing', f'{output}'+'.p') 
with my_path.open('wb') as fp:
    pickle.dump(RE_prod, fp)

#%% read in GLUCOSE results: ProductionByTechnologyAnnual - Primary Energy, NUCLEAR
# nuclear penetration
NU_prod = pd.DataFrame(index=replications, columns=YEAR.VALUE).fillna(0)
for run in replications:
    PrimEn_techs = pd.Series(PrimEn[run].columns) 
    NU_tech = PrimEn_techs[PrimEn_techs.str[2:4]=='NU']
    PrimEn_NU = PrimEn[run][NU_tech]
    NU_prod.iloc[run] = PrimEn_NU.transpose()

output = 'GLUCOSE_PrimaryEnergy_NU'

fp = open(f'{output}'+'.p', 'wb')
my_path = Path(f'{folder}', 'GLUCOSE_DataProcessing', f'{output}'+'.p') 
with my_path.open('wb') as fp:
    pickle.dump(NU_prod, fp)

#%% read in GLUCOSE data: AccumulatedAnnualDemand - Food - Crops, Livestock
# food consumption
Demand_MFOO = pd.DataFrame(index=replications, columns=YEAR.VALUE).fillna(0)
Demand_VFOO = pd.DataFrame(index=replications, columns=YEAR.VALUE).fillna(0)
for run in replications:
    variable = 'AccumulatedAnnualDemand'
    csv_file = Path(f'{folder}','results', '0', f'model_{run}', 'data', f'{variable}.csv')
    AccumulatedAnnualDemand = pd.read_csv(csv_file)
    MFOO = AccumulatedAnnualDemand.loc[(AccumulatedAnnualDemand["FUEL"]=='MFOO')]
    VFOO = AccumulatedAnnualDemand.loc[(AccumulatedAnnualDemand["FUEL"]=='VFOO')]
    for year in YEAR.VALUE:
        MFOO_temp = MFOO[(MFOO['YEAR'] == year)]
        VFOO_temp = VFOO[(VFOO['YEAR'] == year)]
        Demand_MFOO.loc[run, year] = MFOO_temp['VALUE'].sum()
        Demand_VFOO.loc[run, year] = VFOO_temp['VALUE'].sum()

output1 = 'GLUCOSE_FoodDemand_VFOO'
output2 = 'GLUCOSE_FoodDemand_MFOO'

fp = open(f'{output1}'+'.p', 'wb')
my_path = Path(f'{folder}', 'GLUCOSE_DataProcessing', f'{output1}'+'.p') 
with my_path.open('wb') as fp:
    pickle.dump(Demand_VFOO, fp)

fp = open(f'{output2}'+'.p', 'wb')
my_path = Path(f'{folder}', 'GLUCOSE_DataProcessing', f'{output2}'+'.p') 
with my_path.open('wb') as fp:
    pickle.dump(Demand_MFOO, fp)

#%% read in GLUCOSE results: TotalAnnualTechnologyActivityByMode - Land Use, Forest land
# total forest land (LF1+LF2)
Forest_tot = pd.DataFrame(index=replications, columns=YEAR.VALUE).fillna(0)
for run in replications:
    LF_tot = LandResources[run]['LF1']+LandResources[run]['LF2']
    Forest_tot.iloc[run] = LF_tot.transpose() 

output = 'GLUCOSE_LandUse_LF'

fp = open(f'{output}'+'.p', 'wb')
my_path = Path(f'{folder}', 'GLUCOSE_DataProcessing', f'{output}'+'.p') 
with my_path.open('wb') as fp:
    pickle.dump(Forest_tot, fp)

#%% read in GLUCOSE results: AnnualEmissions
# Total Emissions - CO2EQ and WATER
Emissions = {}

for e in emissions:
    Emissions[e] = pd.DataFrame(index=replications,columns=YEAR.VALUE)
    for run in replications:
        csv_file = Path(f'{folder}', 'results', '0', f'{run}', 'AnnualEmissions.csv')
        if not os.path.exists(csv_file):
            pass
        else:
            AnnualEmissions = pd.read_csv(csv_file)
            for year in YEAR.VALUE:
                em_temp = AnnualEmissions[(AnnualEmissions['EMISSION'] == e)&(AnnualEmissions['YEAR'] == year)]
                Emissions[e].loc[run, year] = em_temp['VALUE'].sum()

output = 'GLUCOSE_Emissions'

fp = open(f'{output}'+'.p', 'wb')
my_path = Path(f'{folder}', 'GLUCOSE_DataProcessing', f'{output}'+'.p') 
with my_path.open('wb') as fp:
    pickle.dump(Emissions, fp)

#%% read in GLUCOSE results: AnnualTechnologyEmission - CO2EQ, Direct Air Capture technologies
# DAC penetration (C1ENDA1CS + C1ENDA2CS)
DAC_emission = pd.DataFrame(index=replications, columns=YEAR.VALUE).fillna(0)
for run in replications:
    csv_file = Path(f'{folder}', 'results', '0', f'{run}', 'AnnualTechnologyEmission.csv')
    if not os.path.exists(csv_file):
        pass
    else:
        AnnualTechnologyEmission = pd.read_csv(csv_file)
        for year in YEAR.VALUE:
            DAC_CO2EQ = AnnualTechnologyEmission[((AnnualTechnologyEmission['TECHNOLOGY'] == 'C1ENDA1CS')|(AnnualTechnologyEmission['TECHNOLOGY'] == 'C1ENDA2CS'))&(AnnualTechnologyEmission['EMISSION'] == 'CO2EQ')&(AnnualTechnologyEmission['YEAR'] == year)]
            DAC_emission.loc[run,year] = DAC_CO2EQ['VALUE'].sum()

output = 'GLUCOSE_Emissions_DAC'

fp = open(f'{output}'+'.p', 'wb')
my_path = Path(f'{folder}', 'GLUCOSE_DataProcessing', f'{output}'+'.p') 
with my_path.open('wb') as fp:
    pickle.dump(DAC_emission, fp)

#%% preliminary results as of 22.08.15
# ofinterest = (co2eq<5)+(water<=(2*WATER_GLUCOSE[2025]))
# p = prim.Prim(inputs_GLUCOSE, ofinterest, threshold=0.8, threshold_type=">")  
# box = p.find_box()
# box.show_tradeoff()
# plt.title('co2eq + 2*WATER_GLUCOSE[2025]')
# plt.show()


ofinterest = (co2eq<5) #(PrimEn_RE[2050]>=250)+ (PrimEn_NU[2050]<=PrimEn_NU[2025])
p = prim.Prim(inputs_GLUCOSE, ofinterest, threshold=0.8, threshold_type=">")  
box = p.find_box()
box.show_tradeoff()

plt.title('emissions')
plt.show()
# %%
