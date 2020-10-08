"""
Trying to automate the results visualisation for GLUCOSE
"""
#%%
import pandas as pd
import numpy as np

import re
import matplotlib.pyplot as plt 
import seaborn as sns

GLUCOSE_techs = pd.read_excel('GLUCOSE_configuration.xlsx', sheet_name='Technologies')
EnergyTechs = GLUCOSE_techs.groupby(['Module']).get_group('energy')
#TechGroups1 = GLUCOSE_techs.groupby(['InputFuel'])

    
    # if 'electricity, heat' in TechGroups.groupby(['OutputFuel']).groups.keys():
    #     eh = GLUCOSE_techs.groupby(['InputFuel', 'OutputFuel']).get_group(i, 'electricity, heat')
    #     cat[i]= [e.Technology.unique()]
    #     #c = TechGroups.get_group(i)
    #d=e.append(eh)
    #cat[i]= [e.Technology.unique()]

#%%
GLUCOSE_fuels = pd.read_excel('GLUCOSE_configuration.xlsx', sheet_name='Fuels')
# FuelGroups = GLUCOSE_fuels.groupby('Level')
# level = {}
# for j in GLUCOSE_fuels.Level.unique():
#     f = FuelGroups.get_group(j)
#     level[j]= [f.Fuel.unique()]

GLUCOSE_years = pd.read_excel('GLUCOSE_configuration.xlsx', sheet_name='Years')
GLUCOSEdata_all = pd.read_csv('/Users/agnese/Documents/KTH-Work/KTH-dESA:GLUCOSE_GitHub/GLUCOSE/results/Baseline/results_otoole/ProductionByTechnologyAnnual.csv')
GLUCOSEdata_PBTA = GLUCOSEdata_all[GLUCOSEdata_all['YEAR']<2051]
GLUCOSEdata_all = pd.read_csv('/Users/agnese/Documents/KTH-Work/KTH-dESA:GLUCOSE_GitHub/GLUCOSE/results/Baseline/results_otoole/UseByTechnology.csv')
GLUCOSEdata_UBT = GLUCOSEdata_all[GLUCOSEdata_all['YEAR']<2051]

GLUCOSEdata_all = pd.read_csv('/Users/agnese/Documents/KTH-Work/KTH-dESA:GLUCOSE_GitHub/GLUCOSE/results/Baseline/results_otoole/TotalCapacityAnnual.csv')
GLUCOSEdata_TCA = GLUCOSEdata_all[GLUCOSEdata_all['YEAR']<2051]

#%%
def get_df_name(df):
    name =[x for x in globals() if globals()[x] is df][0]
    return name
#%%
def results_forPlotting(AllData, XY, TS):
    """
    function to summ all data by year for all technologies belonging to one category, and save the new data in a DataFrame to be used in the plot
    """
    Years= AllData.YEAR.unique()
    name = get_df_name(AllData)
    TechName = XY #name[:name.index("_" + XY)]
    
    RefinedData = pd.DataFrame(columns = AllData.columns)
    if TS == 'timeslice':
        for i in Years:
            RefinedData_intermediate = pd.DataFrame(columns = AllData.columns)
            for j in AllData.TIMESLICE.unique():
                data = AllData[(AllData.YEAR==i) & (AllData.TIMESLICE==j)]
                total1 = data.VALUE.sum()
                RefinedData_intermediate = RefinedData_intermediate.append({'REGION': data.REGION.unique(), 'TIMESLICE':j, 'TECHNOLOGY':TechName, 'FUEL': data.FUEL.unique(), 'YEAR': i, 'VALUE': total1}, ignore_index=True)
            total2 = RefinedData_intermediate.VALUE.sum()
            RefinedData = RefinedData.append({'REGION': data.REGION.unique(), 'TIMESLICE':'Sum', 'TECHNOLOGY':TechName, 'FUEL': data.FUEL.unique(), 'YEAR': i, 'VALUE': total2}, ignore_index=True)
    if TS == 'fuel':
        for i in Years:
            data = AllData[(AllData.YEAR==i)]
            total = data.VALUE.sum()
            RefinedData = RefinedData.append({'REGION': data.REGION.unique(), 'TECHNOLOGY':TechName, 'FUEL': data.FUEL.unique(), 'YEAR': i, 'VALUE': total}, ignore_index=True)
    else:
        for i in Years:
            data = AllData[(AllData.YEAR==i)]
            total = data.VALUE.sum()
            RefinedData = RefinedData.append({'REGION': data.REGION.unique(), 'TECHNOLOGY':TechName, 'YEAR': i, 'VALUE': total}, ignore_index=True)
    
    return (RefinedData) 
#%%
#Capacity, electrical:
#   coal = C1COCHP00, C1COIGP00, C1COSCP00
#   coal+CCS = C1COSCPCS
#   gas = C1NGCCP00, C1NGCCPCH, C1NGGCP00, C1NGGCPCH
#   gas+CCS = C1NGCCPCS
#   oil = C1HFGCP00, C1HFGCPCH, C1LFCCP00
#   nuclear = C1NULWP00
#   biomass = C1BMCHP00, C1BMSCP00
#   biomass+CCS = C1BMIGPCS
#   hydro = C1HYDMP00, C1HYMIP00
#   solar = C1SOV1P00, C1SOV2P00, C1SOC1P00
#   wind = C1WDOFP00, C1WDONP00
#   otherRE = C1GOCVP00, C1OCCVP00

TCA_cat = {}
for i in EnergyTechs.InputFuel.unique():
    TechGroups = EnergyTechs.groupby(['InputFuel']).get_group(i)
    if 'electricity' in TechGroups.groupby(['OutputFuel']).groups.keys():
        data = EnergyTechs.groupby(['InputFuel', 'OutputFuel']).get_group((i, 'electricity'))
        if 'electricity, heat' in TechGroups.groupby(['OutputFuel']).groups.keys():
            data = data.append(EnergyTechs.groupby(['InputFuel', 'OutputFuel']).get_group((i, 'electricity, heat')))
        TCA_cat[i]= [data.Technology.unique()]


TCA = {}
for i in TCA_cat:
    data = GLUCOSEdata_TCA[GLUCOSEdata_TCA['TECHNOLOGY'].isin(TCA_cat[i][0])]
    TCA[i] = results_forPlotting(data, i, 'no')

#%%
# PrimaryEnergy: 
#   coal = C1_P_HCO - C1CO00I00
#   gas = C1_P_GAS - C1NG00I00
#   oil = C1_R_OIL - C1OI00I00
#   hydro = C1_S_ELC - C1HYDMP00, C1HYMIP00
#   biomass = C1_P_BIOW - C1BMBRFH1, C1BMBRFN1, C1BMCHP00, C1BMHTF03, C1BMIGPCS, C1BMLP000, C1BMSCP00
#   nuclear = C1_P_NUC - C1NU00I00
#   solar = C1_S_ELC - C1SOC1P00, C1SOV1P00, C1SOV2P00, C1SOTHF00
#   wind = C1_S_ELC - C1WDOFP00, C1WDONP00
#   otherRE = C1_S_ELC - C1OCCVP00, C1GOCVP00, C1GOHTF03

PrimaryLevel = {}
fuel1=GLUCOSE_fuels.groupby(['Level']).get_group('primary')
for j in fuel1.EnergyFuel.unique():
    fuel2 = fuel1.groupby(['EnergyFuel']).get_group(j)
    PrimaryLevel[j]= [fuel2.Commodity.unique()]

SecondaryLevel = {}
fuel3=GLUCOSE_fuels.groupby(['Level']).get_group('secondary')
for k in fuel3.EnergyFuel.unique():
    fuel4 = fuel3.groupby(['EnergyFuel']).get_group(k)
    SecondaryLevel[k]= [fuel4.Commodity.unique()]

Renewables = {}
ren = EnergyTechs.groupby(['EnergyType']).get_group('renewable')
for x in ren.InputFuel.unique():
    ren2 = ren.groupby(['InputFuel']).get_group(x)
    Renewables[x]=[ren2.Technology.unique()]

#%%
biomassdata = GLUCOSEdata_UBT[GLUCOSEdata_UBT['FUEL'].isin(PrimaryLevel['biomass'][0])]
biomass_PBTA = results_forPlotting(biomassdata, 'biomass', 'timeslice')

RefinedData = pd.DataFrame(columns = biomassdata.columns)
TechName = 'biomass' #name[:name.index("_" + XY)]
Years= biomassdata.YEAR.unique()
for i in Years:
    RefinedData_intermediate = pd.DataFrame(columns = biomassdata.columns)
    for j in biomassdata.TIMESLICE.unique():
        data = biomassdata[(biomassdata.YEAR==i) & (biomassdata.TIMESLICE==j)]
        total1 = data.VALUE.sum()
        RefinedData_intermediate = RefinedData_intermediate.append({'REGION': data.REGION.unique(), 'TIMESLICE':j, 'TECHNOLOGY':TechName, 'FUEL': data.FUEL.unique(), 'YEAR': i, 'VALUE': total1}, ignore_index=True)
    total2 = RefinedData_intermediate.VALUE.sum()
    RefinedData = RefinedData.append({'REGION': data.REGION.unique(), 'TIMESLICE':'sum', 'TECHNOLOGY':TechName, 'FUEL': data.FUEL.unique(), 'YEAR': i, 'VALUE': total2}, ignore_index=True)

#%%
PBTA = {}
for i in PrimaryLevel:
    if i == 'biomass':
        data = GLUCOSEdata_UBT[GLUCOSEdata_UBT['FUEL'].isin(PrimaryLevel[i][0])]
        PBTA[i] = results_forPlotting(data, i, 'timeslice')
    if i != 'biomass':    
        data = GLUCOSEdata_PBTA[GLUCOSEdata_PBTA['FUEL'].isin(PrimaryLevel[i][0])]
        PBTA[i] = results_forPlotting(data, i, 'fuel')
for k in SecondaryLevel:
    if k == 'electricity':
        data = GLUCOSEdata_PBTA[GLUCOSEdata_PBTA['FUEL'].isin(SecondaryLevel[k][0])]    
        for j in Renewables:
            data1 = data[data['TECHNOLOGY'].isin(Renewables[j][0])] 
            PBTA[j] = results_forPlotting(data1, j, 'fuel')
        if k == 'heat':
            data2 = GLUCOSEdata_PBTA[GLUCOSEdata_PBTA['FUEL'].isin(SecondaryLevel[k][0])]    
            for j in Renewables:
                data3 = data2[data2['TECHNOLOGY'].isin(Renewables[j][0])] 
                PBTA[j] = results_forPlotting(data3, j, 'fuel')

b=PBTA['biomass']
s=PBTA['solar']
g=PBTA['geothermal']

#for Graph

x = GLUCOSE_years
y=[]
labels=[]
for i in PBTA:
    data = PBTA[i]
    y.append(data.VALUE)
    
    labels.append(i)


plt.stackplot(x,y, labels)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()


#%%
# PBTA_cat = {}
# EnergyTechs = GLUCOSE_techs.groupby(['Module']).get_group('energy')
# for i in EnergyTechs.InputFuel.unique():
#     TechGroups = EnergyTechs.groupby(['InputFuel']).get_group(i)
#     if 'import, production' in TechGroups.groupby(['OutputFuel']).groups.keys():
#         data = EnergyTechs.groupby(['InputFuel', 'OutputFuel']).get_group((i, 'import, production'))
#         PBTA_cat[i]= [data.Technology.unique()]
# Renewables = ['hydro', 'solar', 'wind', 'geothermal', 'ocean']
# for i in Renewables:
#     data = EnergyTechs.groupby(['InputFuel']).get_group(i)
#     PBTA_cat[i]= [data.Technology.unique()]
#%%
PBTA = {}
PrimaryFuels = [GLUCOSE_fuels.groupby(['Level']).get_group('primary')]
for j in PrimaryFuel:
    data = GLUCOSEdata_PBTA[GLUCOSEdata_PBTA['FUEL']==j]
    for 
    if 'primary' in FuelLevels.groupby(['Level']).groups.keys():
        data = GLUCOSEdata_PBTA[GLUCOSEdata_PBTA['FUEL'].isin(level[i][0])] 
        PTBA[i] = results_forPlotting(data, i, 'fuel')

#%%

coalPE = GLUCOSEdata_PBTA[(GLUCOSEdata_PBTA['TECHNOLOGY']=='C1CO00I00') & (GLUCOSEdata_PBTA['FUEL']=='C1_P_HCO')]
gasPE = GLUCOSEdata_PBTA[(GLUCOSEdata_PBTA['TECHNOLOGY']=='C1NG00I00') & (GLUCOSEdata_PBTA['FUEL']=='C1_P_GAS')]
oilPE = GLUCOSEdata_PBTA[(GLUCOSEdata_PBTA['TECHNOLOGY']=='C1OI00I00') & (GLUCOSEdata_PBTA['FUEL']=='C1_R_OIL')]
nuclearPE = GLUCOSEdata_PBTA[(GLUCOSEdata_PBTA['TECHNOLOGY']=='C1NU00I00') & (GLUCOSEdata_PBTA['FUEL']=='C1_P_NUC')]
biomass_PE_all = GLUCOSEdata_UBT[((GLUCOSEdata_UBT['TECHNOLOGY']=='C1BMBRFH1') | (GLUCOSEdata_UBT['TECHNOLOGY']=='C1BMBRFN1') | (GLUCOSEdata_UBT['TECHNOLOGY']=='C1BMCHP00') | (GLUCOSEdata_UBT['TECHNOLOGY']=='C1BMHTF03') | (GLUCOSEdata_UBT['TECHNOLOGY']=='C1BMIGPCS') | (GLUCOSEdata_UBT['TECHNOLOGY']=='C1BMLP000') | (GLUCOSEdata_UBT['TECHNOLOGY']=='C1BMSCP00')) & (GLUCOSEdata_UBT['FUEL']=='C1_P_BIOW')]
hydro_PE_all = GLUCOSEdata_PBTA[((GLUCOSEdata_PBTA['TECHNOLOGY']=='C1HYDMP00') | (GLUCOSEdata_PBTA['TECHNOLOGY']=='C1HYMIP00')) & (GLUCOSEdata_PBTA['FUEL']=='C1_S_ELC')]
solar_PE_all = GLUCOSEdata_PBTA[((GLUCOSEdata_PBTA['TECHNOLOGY']=='C1SOC1P00')|(GLUCOSEdata_PBTA['TECHNOLOGY']=='C1SOV1P00')|(GLUCOSEdata_PBTA['TECHNOLOGY']=='C1SOV2P00')|(GLUCOSEdata_PBTA['TECHNOLOGY']=='C1SOTHF00')) & (GLUCOSEdata_PBTA['FUEL']=='C1_S_ELC')]
wind_PE_all = GLUCOSEdata_PBTA[((GLUCOSEdata_PBTA['TECHNOLOGY']=='C1WDOFP00') | (GLUCOSEdata_PBTA['TECHNOLOGY']=='C1WDONP00')) & (GLUCOSEdata_PBTA['FUEL']=='C1_S_ELC')]
otherRE_PE_all = GLUCOSEdata_PBTA[((GLUCOSEdata_PBTA['TECHNOLOGY']=='C1OCCVP00') | (GLUCOSEdata_PBTA['TECHNOLOGY']=='C1GOCVP00') | (GLUCOSEdata_PBTA['TECHNOLOGY']=='C1GOHTF03')) & (GLUCOSEdata_PBTA['FUEL']=='C1_S_ELC')]

biomassPE = results_forPlotting(biomass_PE_all, 'PE', 'timeslice')
hydroPE = results_forPlotting(hydro_PE_all, 'PE', 'fuel')
solarPE = results_forPlotting(solar_PE_all, 'PE', 'fuel')
windPE = results_forPlotting(wind_PE_all, 'PE', 'fuel')
otherREPE = results_forPlotting(otherRE_PE_all, 'PE', 'fuel')

#Secondary Energy, ELECTRICITY:
#   coal =  C1_S_ELC - C1COCHP00, C1COIGP00, C1COSCP00
#   coal+CCS = C1_S_ELC - C1COSCPCS
#   gas = C1_S_ELC - C1NGCCP00, C1NGCCPCH, C1NGGCP00, C1NGGCPCH
#   gas+CCS = C1_S_ELC - C1NGCCPCS
#   oil = C1_S_ELC - C1HFGCP00, C1HFGCPCH, C1LFCCP00 
#   nuclear = C1_S_ELC - C1NULWP00
#   biomass = C1_S_ELC - C1BMCHP00, C1BMSCP00
#   biomass + CCS = C1_S_ELC - C1BMIGPCS
#   hydro = C1_S_ELC - C1HYDMP00, C1HYMIP00
#   solar = C1_S_ELC - C1SOV1P00, C1SOV2P00, C1SOC1P00
#   wind = C1_S_ELC - C1WDOFP00, C1WDONP00
#   otherRE = C1_S ELC - C1GOCVP00, C1OCCVP00

#Secondary Energy, HEAT:
#   coal = C1_S_HEAT - C1COCHP00, C1COIGP00, C1COSCP00, C1COSCPCS, C1COHTF03
#   gas = C1_S_HEAT - C1NGCCP00, C1NGCCPCH, C1NGCCPCS, C1NGGCP00, C1NGGCPCH, C1NGHTF03
#   oil = C1_S_HEAT - C1HFGCP00, C1HFGCPCH, C1LFCCP00, C1OIHTF03
#   nuclear = C1_S_HEAT - C1NULWP00
#   biomass = C1_S_HEAT - C1BMCHP00, C1BMIGPCS, C1BMSCP00, C1BMHTF03
#   hydro = C1_S_HEAT - C1HYDMP00, C1HYMIP00
#   solar = C1_S_HEAT - C1SOV1P00, C1SOV2P00, C1SOC1P00
#   wind = C1_S_HEAT - C1WDOFP00, C1WDONP00
#   otherRE = C1_S_HEAT - C1GOCVP00, C1GOHTF03, C1OCCVP00



#%%
# Graph data
x = GLUCOSE_years
y = [coalPE.VALUE, gasPE.VALUE, oilPE.VALUE, nuclearPE.VALUE, biomassPE.VALUE, hydroPE.VALUE, solarPE.VALUE, windPE.VALUE, otherREPE.VALUE]

# Plot
plt.stackplot(x,y, labels=['coal', 'gas', 'oil', 'nuclear', 'biomass', 'hydro', 'solar', 'wind', 'other RE'])
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

#z = [coal_TCA.VALUE, coalCCS_TCA.VALUE, gas_TCA.VALUE, gasCCS_TCA.VALUE, oil_TCA.VALUE, nuclear_TCA.VALUE, biomass_TCA.VALUE, biomassCCS_TCA.VALUE, hydro_TCA.VALUE, solar_TCA.VALUE, wind_TCA.VALUE, otherRE_TCA.VALUE]
# plt.stackplot(x,z, labels=['coal', 'coal+CCS', 'gas', 'gas+CCS', 'oil', 'nuclear', 'biomass', 'biomass+CCS', 'hydro', 'solar', 'wind', 'other RE'])
# plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
# plt.show()

# %%
