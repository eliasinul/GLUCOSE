import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

from pathlib import Path

import sys
import os

import glob

import pickle

# #read in the path to the folder of interest


folder_in = 'input_data/GLUCOSE_noDA2CS_14_2'
folder_out = 'results/GLUCOSE_noDA2CS_14_2'

myPath = Path('..','..',f'{folder_out}', 'results_csv')
tifCounter = len(glob.glob1(myPath,"*.ilp"))
print('Infeasible scenarios:', tifCounter)

#data processing from GLUCOSE scenarios runs
#creating a database with yearly data inputs
#configfile: "config/config.yaml"

myPath = Path(f'{folder_out}','results_csv')
n_replications = int(len(glob.glob1(myPath,"*.sol")))
print("Number of replications/runs:", n_replications)
replications = list(range(0,n_replications))
print(replications)

#%% create folder to save processed results

folder_path = Path('..', '..', f'{folder_out}', 'results_processed') 
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

#%% read in model parameter data

FUEL = pd.read_csv(Path('..','..',f'{folder_in}', 'data_csv', 'FUEL.csv'))
TECH = pd.read_csv(Path('..','..',f'{folder_in}', 'data_csv', 'TECHNOLOGY.csv'))

## energy fuels
energy_fuel = FUEL.loc[(FUEL.VALUE.str[0:2] == 'C1')]
PrimEN_fuel = (energy_fuel.loc[(energy_fuel.VALUE.str[3:4] == 'P')|(energy_fuel.VALUE.str[3:4] == 'R')]).VALUE.unique()
SecEN_fuel = (energy_fuel.loc[(energy_fuel.VALUE.str[3:4] == 'S')]).VALUE.unique()
#print(SecEN_fuel)
FinalEN_fuel = (energy_fuel.loc[(energy_fuel.VALUE.str[3:4] == 'F')]).VALUE.unique()
#print(FinalEN_fuel)
## energy techs
energy_tech = TECH.loc[(TECH.VALUE.str[0:2] == 'C1')]
ResEN_tech = (energy_tech.loc[(energy_tech.VALUE.str[6:7] == 'I')]).VALUE.unique()
RE_tech = (energy_tech.loc[(energy_tech.VALUE.str[2:4] == 'SO')|(energy_tech.VALUE.str[2:4] == 'WD')|(energy_tech.VALUE.str[2:4] == 'HY')|(energy_tech.VALUE.str[2:4] == 'GO')|(energy_tech.VALUE.str[2:4] == 'OC')]).VALUE.unique()
PrimEN_tech = (energy_tech.loc[(energy_tech.VALUE.str[6:7] == 'P')|(energy_tech.VALUE.str[6:7] == '0')]).VALUE.unique()
SecEN_tech = (energy_tech.loc[(energy_tech.VALUE.str[6:7] == 'T')]).VALUE.unique()
FinalEN_tech = (energy_tech.loc[(energy_tech.VALUE.str[6:7] == 'F')]).VALUE.unique()
Transport_tech = (energy_tech.loc[(energy_tech.VALUE.str[4:6] == 'RD')|(energy_tech.VALUE.str[4:6] == 'RL')|(energy_tech.VALUE.str[4:6] == 'AV')|(energy_tech.VALUE.str[4:6] == 'MR')]).VALUE.unique()

## land and food fuels
land_fuel = (FUEL.loc[(FUEL.VALUE.str[0:1] == 'L')]).VALUE.unique()
food_fuel = (FUEL.loc[(FUEL.VALUE.str[0:1] == 'M')|(FUEL.VALUE.str[0:1] == 'V')]).VALUE.unique()
## land and food techs
land_tech = (TECH.loc[(TECH.VALUE.str[0:1] == 'L')]).VALUE.unique()
food_tech = (TECH.loc[(TECH.VALUE.str[0:1] == 'M')|(TECH.VALUE.str[0:1] == 'V')]).VALUE.unique()

## materials fuels
material_fuel = (FUEL.loc[(FUEL.VALUE.str.len() == 3)|(FUEL.VALUE.str.len() == 4)]).VALUE.unique()
## materials techs
industry_tech = (TECH.loc[(TECH.VALUE.str[-5:] == 'PLANT')]).VALUE.unique()
material_tech = (TECH.loc[(TECH.VALUE.str[-4:] == 'MINE')|(TECH.VALUE.str[-7:] == 'RECYCLE')]).VALUE.unique()

## emissions
EMISSION = pd.read_csv(Path('..','..',f'{folder_in}','data_csv', 'EMISSION.csv'))
emissions = (EMISSION.loc[(EMISSION.VALUE.str.len() == 5)]).VALUE.unique()

## timeframe / modelling period
YEAR = pd.read_csv(Path('..','..',f'{folder_in}','data_csv', 'YEAR.csv'))
YEAR = YEAR.iloc[:-10]

# parameter_file = glob.glob1(folder_in, '*parameters*')
# parameters_GLUCOSE = pd.read_csv(Path('..','..',f'{folder_in}',f'{parameter_file}'))
# col = parameters_GLUCOSE['indexes']


#%% define function for calculating yearly technology penetration (incremental share of electrical capacity)
def percentage_change(col1,col2):
    return ((col2 - col1) / col1) * 100

#%% Processing results
# initialise pd.Series
CO2EQ_GLUCOSE = pd.Series(index=YEAR.VALUE, dtype='float64') 
ccs_em = pd.Series(index=YEAR.VALUE, dtype='float64')  
WATER_GLUCOSE = pd.Series(index=YEAR.VALUE, dtype='float64')  
LAi_GLUC = pd.Series(index=YEAR.VALUE, dtype='float64')  
LF_GLUCOSE = pd.Series(index=YEAR.VALUE, dtype='float64')  
NU_prod = pd.Series(index=YEAR.VALUE, dtype='float64')  
NU_cap = pd.Series(index=YEAR.VALUE, dtype='float64')  
BM_use = pd.Series(index=YEAR.VALUE, dtype='float64')  

# read in selected results for year 2050
results_file1 = Path('..', '..', f'{folder_out}', 'results_csv', 'TotalAnnualTechnologyActivityByMode.csv')
results_file2 = Path('..', '..', f'{folder_out}', 'results_csv', 'AnnualEmissions.csv')
results_file3 = Path('..', '..', f'{folder_out}', 'results_csv', 'AnnualTechnologyEmission.csv')
results_file4 = Path('..', '..', f'{folder_out}', 'results_csv', 'ProductionByTechnologyAnnual.csv')
results_file5 = Path('..', '..', f'{folder_out}', 'results_csv', 'TotalCapacityAnnual.csv')
results_file6 = Path('..', '..', f'{folder_out}', 'results_csv', 'UseByTechnology.csv')

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
                LF_GLUCOSE.loc[year] = land_temp['VALUE'].sum()
            if tech == 'LA1_i':
                land_temp = TotalAnnualTechnologyActivityByMode[(TotalAnnualTechnologyActivityByMode['TECHNOLOGY'] == tech)&(TotalAnnualTechnologyActivityByMode['YEAR'] == year)&(TotalAnnualTechnologyActivityByMode['MODE_OF_OPERATION'] == 1)]
                LAi_GLUC.loc[year] = land_temp['VALUE'].sum()
            for tech in PrimEN_tech:
                if tech[2:4]=='NU':
                    production = ProductionByTechnologyAnnual[(ProductionByTechnologyAnnual['TECHNOLOGY']==tech)&(ProductionByTechnologyAnnual['YEAR']== year)]
                    capacity = TotalCapacityAnnual[(TotalCapacityAnnual['TECHNOLOGY']==tech)&(TotalCapacityAnnual['YEAR']== year)]
                    NU_prod.loc[year] = production['VALUE'].sum()
                    NU_cap.loc[year] = capacity['VALUE'].sum()
        use = UseByTechnology.loc[(UseByTechnology['TECHNOLOGY'].str[2:4]=='BM')&(UseByTechnology['FUEL']=='C1_P_BIOW')&(UseByTechnology['YEAR']==year)]
        #UseByTechnology[(UseByTechnology['FUEL']==fuel)&(UseByTechnology['TECHNOLOGY']==tech)&(UseByTechnology['YEAR']==year)]
        BM_use.loc[year] = use['VALUE'].sum()
        for ems in emissions:
            if ems == 'CO2EQ':
                em = AnnualEmissions[(AnnualEmissions['EMISSION'] == ems)&(AnnualEmissions['YEAR'] == year)]
                AnnualTechnologyEmission_ccs = AnnualTechnologyEmission.loc[(AnnualTechnologyEmission['TECHNOLOGY'].str[-2:] == 'CS')|(AnnualTechnologyEmission['TECHNOLOGY'].str[-7:-5] == 'CS')]
                AnnualTechnologyEmission_ccs_em = AnnualTechnologyEmission_ccs[(AnnualTechnologyEmission_ccs['EMISSION'] == ems)&(AnnualTechnologyEmission_ccs['YEAR'] == year)]
                CO2EQ_GLUCOSE.loc[year] = em.VALUE.sum()# em['VALUE'].values
                if not AnnualTechnologyEmission_ccs_em.empty:
                    AnnualTechnologyEmission_ccs = (AnnualTechnologyEmission.loc[(AnnualTechnologyEmission['TECHNOLOGY'].str[-2:] == 'CS')|(AnnualTechnologyEmission['TECHNOLOGY'].str[-7:-5] == 'CS')])[(AnnualTechnologyEmission['EMISSION'] == ems)&(AnnualTechnologyEmission['YEAR'] == year)]
                    ccs_em.loc[year] = AnnualTechnologyEmission_ccs_em.VALUE.sum()
            if ems == 'WATER':
                em = AnnualEmissions[(AnnualEmissions['EMISSION'] == ems)&(AnnualEmissions['YEAR'] == year)]
                WATER_GLUCOSE.loc[year] = em.VALUE.sum()


#%% read in GLUCOSE results: ProductionByTechnologyAnnual - Primary Energy
PrimEn = {}
RE_tech = pd.Series(RE_tech).str[2:4].unique()
#ResEN_tech = pd.Series(ResEN_tech).str[2:4].unique()
ResEN_tech = np.append(ResEN_tech, 'BM')


PrimEn = pd.DataFrame(index=YEAR.VALUE, columns=(list(ResEN_tech)+list(RE_tech))).fillna(0)
results_file1 = Path('..', '..', f'{folder_out}', 'results_csv', 'ProductionByTechnologyAnnual.csv')
results_file2 = Path('..', '..', f'{folder_out}', 'results_csv', 'UseByTechnology.csv')
if not os.path.exists(results_file1):
    pass
else:
    ProductionByTechnologyAnnual=pd.read_csv(results_file1)
    UseByTechnology=pd.read_csv(results_file2)
    for year in YEAR.VALUE:
        for tech in ResEN_tech:
            PrimEn_temp = ProductionByTechnologyAnnual[(ProductionByTechnologyAnnual['TECHNOLOGY'] == tech)&(ProductionByTechnologyAnnual['YEAR'] == year)]
            PrimEn.loc[year,tech] = PrimEn_temp['VALUE'].sum()
        Use_temp = UseByTechnology.loc[(UseByTechnology['TECHNOLOGY'].str[2:4]=='BM')&(UseByTechnology['FUEL']=='C1_P_BIOW')&(UseByTechnology['YEAR']==year)]
        PrimEn.loc[year, 'BM']+= Use_temp['VALUE'].sum()
        for tech in RE_tech:
            PrimREn_temp = ProductionByTechnologyAnnual.loc[(ProductionByTechnologyAnnual['TECHNOLOGY'].str[2:4] == tech)&(ProductionByTechnologyAnnual['YEAR'] == year)]
            PrimEn.loc[year, tech] = PrimREn_temp['VALUE'].sum()

# save results ProductionByTechnologyAnnual - Primary Energy into file
output = 'GLUCOSE_PrimaryEnergy'

#fp = open(f'{output}'+'.p', 'wb')
my_path = Path('..', '..', f'{folder_out}', 'results_processed', f'{output}'+'.p') 
with my_path.open('wb') as fp:
    pickle.dump(PrimEn, fp)

# save to csv file
my_path_csv = Path('..', '..', f'{folder_out}', 'results_processed', f'{output}'+'.csv') 
PrimEn.to_csv(my_path_csv, index=False)

#%% read in GLUCOSE results: TotalCapacityAnnual - Electrical Capacity
Capacity_elc = {}
#RE_tech = pd.Series(RE_tech).str[2:4].unique()
PrimEN_tech_abb = (pd.Series(PrimEN_tech).str[2:4].unique())
PrimEN_tech = np.append(PrimEN_tech, 'BM')

Capacity_elc = pd.DataFrame(index=YEAR.VALUE, columns=(list(PrimEN_tech_abb))).fillna(0)
results_file1 = Path('..', '..', f'{folder_out}', 'results_csv', 'TotalCapacityAnnual.csv')
results_file2 = Path('..', '..', f'{folder_in}', 'data_csv', 'OutputActivityRatio.csv')
if not os.path.exists(results_file1)|os.path.exists(results_file2):
    pass
else:
    TotalCapacityAnnual=pd.read_csv(results_file1)
    OutputActivityRatio=pd.read_csv(results_file2)
    for tech in PrimEN_tech:
        if tech[-2:] != 'CS':
            for year in YEAR.VALUE:
                #for tech in PrimEN_tech:
                OAR = (OutputActivityRatio[(OutputActivityRatio['TECHNOLOGY'] == tech)&(OutputActivityRatio['YEAR'] == year)&(OutputActivityRatio['MODE_OF_OPERATION'] == 1)]).FUEL
                for oar in OAR:
                    if oar == 'C1_S_ELC':
                        Capacity_elc_temp = TotalCapacityAnnual[(TotalCapacityAnnual['TECHNOLOGY'] == tech)&(TotalCapacityAnnual['YEAR'] == year)]
                        tech_abb = tech[2:4]
                        Capacity_elc.loc[year,tech_abb] += Capacity_elc_temp['VALUE'].sum()
        else:
            ccs_abb = tech[2:4]+tech[-2:]
            Capacity_elc[ccs_abb]=0
            for year in YEAR.VALUE:
                #for tech in PrimEN_tech:
                OAR = (OutputActivityRatio[(OutputActivityRatio['TECHNOLOGY'] == tech)&(OutputActivityRatio['YEAR'] == year)&(OutputActivityRatio['MODE_OF_OPERATION'] == 1)]).FUEL
                for oar in OAR:
                    if oar == 'C1_S_ELC':
                        Capacity_elc_temp = TotalCapacityAnnual[(TotalCapacityAnnual['TECHNOLOGY'] == tech)&(TotalCapacityAnnual['YEAR'] == year)]
                        Capacity_elc.loc[year,ccs_abb] += Capacity_elc_temp['VALUE'].sum()

        # Use_temp = UseByTechnology.loc[(UseByTechnology['TECHNOLOGY'].str[2:4]=='BM')&(UseByTechnology['FUEL']=='C1_P_BIOW')&(UseByTechnology['YEAR']==year)]
        # PrimEn[run].loc[year, 'BM']+= Use_temp['VALUE'].sum()
        # for tech in RE_tech:
        #     TPES_temp = ProductionByTechnologyAnnual.loc[(ProductionByTechnologyAnnual['TECHNOLOGY'].str[2:4] == tech)&(ProductionByTechnologyAnnual['YEAR'] == year)]
        #     TPES[run].loc[year, tech] = TPES_temp['VALUE'].sum()

# save results TotalCapacityAnnual - Electrical Capacity into file
output = 'GLUCOSE_ElectricalCapacity'

#fp = open(f'{output}'+'.p', 'wb')
my_path = Path('..', '..', f'{folder_out}', 'results_processed', f'{output}'+'.p') 
with my_path.open('wb') as fp:
    pickle.dump(Capacity_elc, fp)

# save to csv file
my_path_csv = Path('..', '..', f'{folder_out}', 'results_processed', f'{output}'+'.csv') 
Capacity_elc.to_csv(my_path_csv, index=False)

#%% read in GLUCOSE results: TotalAnnualTechnologyActivityByMode - Land Use
LandResources = {}
land_tech = ['LA1', 'LA1_i', 'LA2', 'LF1', 'LF2', 'LO']
# for tech in land_tech:
#     LandResources[run]=pd.DataFrame(index=YEAR.VALUE, columns=land_tech).fillna(0)


LandResources=pd.DataFrame(index=YEAR.VALUE, columns=(list(land_tech))).fillna(0)
results_file1 = Path('..', '..', f'{folder_out}', 'results_csv', 'TotalAnnualTechnologyActivityByMode.csv')
if not os.path.exists(results_file1):
    pass
else:
    TotalAnnualTechnologyActivityByMode=pd.read_csv(results_file1)
    for year in YEAR.VALUE:
        for tech in land_tech:
            Land_temp = TotalAnnualTechnologyActivityByMode[(TotalAnnualTechnologyActivityByMode['TECHNOLOGY'] == tech)&(TotalAnnualTechnologyActivityByMode['YEAR'] == year)&(TotalAnnualTechnologyActivityByMode['MODE_OF_OPERATION'] == 1)]
            LandResources.loc[year, tech] = Land_temp['VALUE'].sum()

# save results TotalAnnualTechnologyActivityByMode - Land Use into file
output = 'GLUCOSE_LandUse'

#fp = open(f'{output}'+'.p', 'wb')
my_path = Path('..', '..', f'{folder_out}', 'results_processed', f'{output}'+'.p') 
with my_path.open('wb') as fp:
    pickle.dump(LandResources, fp)

#%% read in GLUCOSE results: ProductionByTechnologyAnnual - Industry
IndustryProd = {}

IndustryProd=pd.DataFrame(index=YEAR.VALUE, columns=(list(industry_tech))).fillna(0)
results_file1 = Path('..', '..', f'{folder_out}', 'results_csv', 'ProductionByTechnologyAnnual.csv')
if not os.path.exists(results_file1):
    pass
else:
    ProductionByTechnologyAnnual=pd.read_csv(results_file1)
    for year in YEAR.VALUE:
        for tech in industry_tech:
            for fuel in material_fuel:
                Industry_temp = ProductionByTechnologyAnnual[(ProductionByTechnologyAnnual['TECHNOLOGY'] == tech)&(ProductionByTechnologyAnnual['YEAR'] == year)&(ProductionByTechnologyAnnual['FUEL'] == fuel)]
                IndustryProd.loc[year, tech] += Industry_temp['VALUE'].sum()

# save results ProductionByTechnologyAnnual - Industry into file
output = 'GLUCOSE_IndustryProduction'

#fp = open(f'{output}'+'.p', 'wb')
my_path = Path('..', '..', f'{folder_out}', 'results_processed', f'{output}'+'.p') 
with my_path.open('wb') as fp:
    pickle.dump(IndustryProd, fp)

#%% read in GLUCOSE results: ProductionByTechnologyAnnual - Primary Energy, RENEWABLES
# RE penetration 
RE_prod = pd.DataFrame(columns=YEAR.VALUE).fillna(0)

PrimEn_RE = PrimEn.iloc[: , -6:].sum(axis=1)
RE_prod = PrimEn_RE.transpose()

# save GLUCOSE results: ProductionByTechnologyAnnual - Primary Energy, RENEWABLES into file
output = 'GLUCOSE_PrimaryEnergy_RE'

#fp = open(f'{output}'+'.p', 'wb')
my_path = Path('..', '..', f'{folder_out}', 'results_processed', f'{output}'+'.p') 
with my_path.open('wb') as fp:
    pickle.dump(RE_prod, fp)

#%% read in GLUCOSE results: TotalCapacityAnnual - Electrical Capacity, RENEWABLES
# RE penetration 

#RES = pd.Series(pd.Series(RE_tech).str[2:4].unique())
RES = np.append(RE_tech, 'BM')
RE_cap = pd.DataFrame(columns=YEAR.VALUE).fillna(0)

ElcCap_RE = pd.Series(index=YEAR.VALUE, dtype=float).fillna(0)
for t in RES:
    ElcCap_RE += Capacity_elc[t]
RE_cap = ElcCap_RE.transpose()

# save GLUCOSE results: TotalCapacityAnnual - Electrical Capacity, RENEWABLES into file
output = 'GLUCOSE_ElectricalCapacity_RE'

#fp = open(f'{output}'+'.p', 'wb')
my_path = Path('..', '..', f'{folder_out}', 'results_processed', f'{output}'+'.p') 
with my_path.open('wb') as fp:
    pickle.dump(RE_cap, fp)

#%% calculate technology penetration rate: TotalCapacityAnnual - Electrical Capacity, RENEWABLES 
RE_cap_diff = pd.Series(index=range(2020,2051))
for c in RE_cap_diff.index:
    RE_cap_diff[c]= RE_cap[c] - RE_cap[c-1]

#save technology penetration rate: TotalCapacityAnnual - Electrical Capacity, RENEWABLE
output = 'GLUCOSE_ElectricalCapacity_RE_diff'

#fp = open(f'{output}'+'.p', 'wb')
my_path = Path('..', '..', f'{folder_out}', 'results_processed', f'{output}'+'.p') 
with my_path.open('wb') as fp:
    pickle.dump(RE_cap_diff, fp)

#%% read in GLUCOSE results: ProductionByTechnologyAnnual - Primary Energy, NUCLEAR
# nuclear penetration
NU_prod = pd.Series(index=YEAR.VALUE, dtype='float64') #.fillna(0)

PrimEn_techs = pd.Series(PrimEn.columns) 
NU_tech = PrimEn_techs[PrimEn_techs.str[2:4]=='NU']
PrimEn_NU = PrimEn[NU_tech]
NU_prod = PrimEn_NU

# save GLUCOSE results: ProductionByTechnologyAnnual - Primary Energy, NUCLEAR into file
output = 'GLUCOSE_PrimaryEnergy_NU'

#fp = open(f'{output}'+'.p', 'wb')
my_path = Path('..', '..', f'{folder_out}', 'results_processed', f'{output}'+'.p') 
with my_path.open('wb') as fp:
    pickle.dump(NU_prod, fp)

#%% read in GLUCOSE results: TotalCapacityAnnual - Electrical Capacity, NUCLEAR
# nuclear penetration
NU_cap = pd.Series(index=YEAR.VALUE, dtype='float64')#.fillna(0)

NU_tech = PrimEn_techs[PrimEn_techs.str[2:4]=='NU']
#CapElc_NU = Capacity_elc[run][NU_tech.str[2:4]]
NU_cap = Capacity_elc[NU_tech.str[2:4]].transpose()

# save GLUCOSE results: TotalCapacityAnnual - Electrical Capacity, NUCLEAR
output = 'GLUCOSE_ElectricalCapacity_NU'

#fp = open(f'{output}'+'.p', 'wb')
my_path = Path('..', '..', f'{folder_out}', 'results_processed', f'{output}'+'.p') 
with my_path.open('wb') as fp:
    pickle.dump(NU_cap, fp)

#%% calculate technology penetration rate: TotalCapacityAnnual - Electrical Capacity, NUCLEAR 
NU_cap_diff = pd.Series(index=range(2020,2051), dtype='float64')
for c in NU_cap_diff.index:
    NU_cap_diff[c]=NU_cap[c]-NU_cap[c-1]

NU_cap_diff = NU_cap_diff.T

# save technology penetration rate: TotalCapacityAnnual - Electrical Capacity, NUCLEAR 
output = 'GLUCOSE_ElectricalCapacity_NU_diff'

#fp = open(f'{output}'+'.p', 'wb')
my_path = Path('..', '..', f'{folder_out}', 'results_processed', f'{output}'+'.p') 
with my_path.open('wb') as fp:
    pickle.dump(NU_cap_diff, fp)

#%% read in GLUCOSE results: TotalCapacityAnnual - Electrical Capacity, CCS
# CCS penetration
CCS_ElcCap = pd.Series(index=YEAR.VALUE, dtype='float64')

Capacity_elc_techs = pd.Series(Capacity_elc.columns) 
CCS_tech = Capacity_elc_techs[Capacity_elc_techs.str[-2:]=='CS']
Cap_CCS = Capacity_elc[CCS_tech].sum(axis=1)
CCS_ElcCap = Cap_CCS.T

# save GLUCOSE results: TotalCapacityAnnual - Electrical Capacity, CCS into file
output = 'GLUCOSE_ElectricalCapacity_CCS'

#fp = open(f'{output}'+'.p', 'wb')
my_path = Path('..', '..', f'{folder_out}', 'results_processed', f'{output}'+'.p') 
with my_path.open('wb') as fp:
    pickle.dump(CCS_ElcCap, fp)

#%% calculate technology penetration rate: TotalCapacityAnnual - Electrical Capacity, CCS
CCS_ElcCap_diff = pd.Series(index=range(2020,2051))
for c in CCS_ElcCap_diff.index:
    CCS_ElcCap_diff[c]=CCS_ElcCap[c]-CCS_ElcCap[c-1]

# save GLUCOSE results: TotalCapacityAnnual - Electrical Capacity, CCS into file
output = 'GLUCOSE_ElectricalCapacity_CCS_diff'

#fp = open(f'{output}'+'.p', 'wb')
my_path = Path('..', '..', f'{folder_out}', 'results_processed', f'{output}'+'.p') 
with my_path.open('wb') as fp:
    pickle.dump(CCS_ElcCap_diff, fp)

#%% read in GLUCOSE data: AccumulatedAnnualDemand - Food - Crops, Livestock
# food consumption
Demand_MFOO = pd.DataFrame(columns=YEAR.VALUE).fillna(0)
Demand_VFOO = pd.DataFrame(columns=YEAR.VALUE).fillna(0)

variable = 'AccumulatedAnnualDemand'
csv_file = Path('..', '..', f'{folder_in}', 'data_csv', f'{variable}.csv')
AccumulatedAnnualDemand = pd.read_csv(csv_file)
MFOO = AccumulatedAnnualDemand.loc[(AccumulatedAnnualDemand["FUEL"]=='MFOO')]
VFOO = AccumulatedAnnualDemand.loc[(AccumulatedAnnualDemand["FUEL"]=='VFOO')]
for year in YEAR.VALUE:
    MFOO_temp = MFOO[(MFOO['YEAR'] == year)]
    VFOO_temp = VFOO[(VFOO['YEAR'] == year)]
    Demand_MFOO.loc[0, year] = MFOO_temp['VALUE'].sum()
    Demand_VFOO.loc[0, year] = VFOO_temp['VALUE'].sum()

# save GLUCOSE data: AccumulatedAnnualDemand - Food - Crops, Livestock into file
output1 = 'GLUCOSE_FoodDemand_VFOO'
output2 = 'GLUCOSE_FoodDemand_MFOO'

#fp = open(f'{output1}'+'.p', 'wb')
my_path = Path('..', '..', f'{folder_out}', 'results_processed', f'{output}'+'.p') 
with my_path.open('wb') as fp:
    pickle.dump(Demand_VFOO, fp)

#fp = open(f'{output2}'+'.p', 'wb')
my_path = Path('..', '..', f'{folder_out}', 'results_processed', f'{output}'+'.p') 
with my_path.open('wb') as fp:
    pickle.dump(Demand_MFOO, fp)

#%% read in GLUCOSE results: TotalAnnualTechnologyActivityByMode - Land Use, Forest land
# total forest land (LF1+LF2)
Forest_tot = pd.Series(index=YEAR.VALUE).fillna(0)

LF_tot = LandResources['LF1']+LandResources['LF2']
Forest_tot = LF_tot.T

# save GLUCOSE results: TotalAnnualTechnologyActivityByMode - Land Use, Forest land into file
output = 'GLUCOSE_LandUse_LF'

#fp = open(f'{output}'+'.p', 'wb')
my_path = Path('..', '..', f'{folder_out}', 'results_processed', f'{output}'+'.p') 
with my_path.open('wb') as fp:
    pickle.dump(Forest_tot, fp)

#%% read in GLUCOSE results: AnnualEmissions
# Total Emissions - CO2EQ and WATER
Emissions = {}

for e in emissions:
    Emissions[e] = pd.Series(index=YEAR.VALUE)
    csv_file = Path('..', '..', f'{folder_out}', 'results_csv', 'AnnualEmissions.csv')
    if not os.path.exists(csv_file):
        pass
    else:
        AnnualEmissions = pd.read_csv(csv_file)
        for year in YEAR.VALUE:
            em_temp = AnnualEmissions[(AnnualEmissions['EMISSION'] == e)&(AnnualEmissions['YEAR'] == year)]
            Emissions[e].loc[year] = em_temp['VALUE'].sum()

e_co2eq = Emissions['CO2EQ']
e_water = Emissions['WATER']

# save GLUCOSE results: AnnualEmissions into file
output = 'GLUCOSE_Emissions'

#fp = open(f'{output}'+'.p', 'wb')
my_path = Path('..', '..', f'{folder_out}', 'results_processed', f'{output}'+'.p') 
with my_path.open('wb') as fp:
    pickle.dump(Emissions, fp)

# save to csv file
for e in Emissions:
    my_path_csv = Path('..', '..', f'{folder_out}', 'results_processed', f'{e}'+'.csv')
    Emissions[e].to_csv(my_path_csv, index=False)

#%% read in GLUCOSE results: AnnualTechnologyEmission - CO2EQ, Direct Air Capture technologies
# DAC penetration (C1ENDA1CS + C1ENDA2CS)
DAC_emission = pd.Series(index=YEAR.VALUE).fillna(0)

csv_file = Path('..', '..', f'{folder_out}', 'results_csv', 'AnnualTechnologyEmission.csv')
if not os.path.exists(csv_file):
    pass
else:
    AnnualTechnologyEmission = pd.read_csv(csv_file)
    for year in YEAR.VALUE:
        DAC_CO2EQ = AnnualTechnologyEmission[((AnnualTechnologyEmission['TECHNOLOGY'] == 'C1ENDA1CS')|(AnnualTechnologyEmission['TECHNOLOGY'] == 'C1ENDA2CS'))&(AnnualTechnologyEmission['EMISSION'] == 'CO2EQ')&(AnnualTechnologyEmission['YEAR'] == year)]
        DAC_emission.loc[year] = DAC_CO2EQ['VALUE'].sum()

# save GLUCOSE results: AnnualTechnologyEmission - CO2EQ, Direct Air Capture technologies
output = 'GLUCOSE_Emissions_DAC'

#fp = open(f'{output}'+'.p', 'wb')
my_path = Path('..', '..', f'{folder_out}', 'results_processed', f'{output}'+'.p') 
with my_path.open('wb') as fp:
    pickle.dump(DAC_emission, fp)

#%% calculate technology penetration rate: AnnualTechnologyEmission - CO2EQ, Direct Air Capture technologies
DAC_emission_diff = pd.Series(index=range(2020,2051))
for c in DAC_emission_diff.index:
    DAC_emission_diff[c]=DAC_emission[c]-DAC_emission[c-1]

# save GLUCOSE results: AnnualTechnologyEmission - CO2EQ, Direct Air Capture technologies penetration rate into file
output = 'GLUCOSE_Emissions_DAC_diff'

#fp = open('..', '..', f'{folder_out}', 'results_processed', f'{output}'+'.p', 'wb')
my_path = Path('..', '..', f'{folder_out}', 'results_processed', f'{output}'+'.p') 
with my_path.open('wb') as fp:
    pickle.dump(DAC_emission_diff, fp)

#%% calculate Transport energy demand: UseByTechnology for transport technologies
Transport_EnUse = pd.DataFrame(index=YEAR.VALUE, columns=(list(Transport_tech))).fillna(0)

results_file = Path('..', '..', f'{folder_out}', 'results_csv', 'UseByTechnology.csv')

if not os.path.exists(results_file):
    pass
else:
    UseByTechnology = pd.read_csv(results_file)        
    for year in YEAR.VALUE:
        for tech in Transport_tech:
            transp_temp = UseByTechnology[(UseByTechnology['TECHNOLOGY'] == tech)&(UseByTechnology['YEAR'] == year)]
            print(transp_temp)
            Transport_EnUse.loc[year,tech] = transp_temp['VALUE'].sum()


# save GLUCOSE results: Transport_EnergyDemand
output = 'GLUCOSE_Transport_EnergyDemand'

#fp = open('..', '..', f'{folder_out}', 'results_processed', f'{output}'+'.p', 'wb')
my_path = Path('..', '..', f'{folder_out}', 'results_processed', f'{output}'+'.p') 
with my_path.open('wb') as fp:
    pickle.dump(Transport_EnUse, fp)

#%%
# if __name__ == "__main__":

#     args = sys.argv[1:]

#     if len(args) != 2:
#         print("Usage: python GLUCOSE_DataProcessing.py <in_folder_in> <out_folder> <>")
#         exit(1)
    
#     # env = gp.Env(log_path)
#     env = gp.Env(DataProcessing.log)

#     in_folder = args[0]
#     out_folder = args[1]

#     # #scenario = snakemake.wildcards[0] #.params.sc
#     # in_folder = snakemake.input[0]
#     # out_folder = snakemake.output[0]
#     # log_path = snakemake.log[0]

#     create_folder(out_folder)
#     read_in_data(in_folder)
#     process_results(out_folder)
    
