
#TechGroups1 = GLUCOSE_techs.groupby(['InputFuel'])

    
    # if 'electricity, heat' in TechGroups.groupby(['OutputFuel']).groups.keys():
    #     eh = GLUCOSE_techs.groupby(['InputFuel', 'OutputFuel']).get_group(i, 'electricity, heat')
    #     cat[i]= [e.Technology.unique()]
    #     #c = TechGroups.get_group(i)
    #d=e.append(eh)
    #cat[i]= [e.Technology.unique()]

#%%
# FuelGroups = GLUCOSE_fuels.groupby('Level')
# level = {}
# for j in GLUCOSE_fuels.Level.unique():
#     f = FuelGroups.get_group(j)
#     level[j]= [f.Fuel.unique()]

#%%
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
#%% ProductionByTechnologyAnnual - PBTA
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
