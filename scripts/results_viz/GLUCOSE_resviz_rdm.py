import pandas as pd
import matplotlib.pyplot as plt
import plotly
import plotly.express as px
from pathlib import Path
import glob
import pickle
import kaleido

import sys

#%%
folder = 'GLUCOSE_withCB_221104'

myPath = Path(f'{folder}', 'results', '0')
tifCounter = len(glob.glob1(myPath,"*.ilp"))
print('Infeasible scenarios:', tifCounter)

myPath = Path(f'{folder}','results', '0')
n_replications = int(len(glob.glob1(myPath,"*.sol")))
print("Number of replications/runs:", n_replications)
replications = list(range(0,n_replications))
#%%
# read output data (results)
## PrimaryEnergy
output = 'GLUCOSE_PrimaryEnergy'
myPath = Path(f'{folder}', 'GLUCOSE_DataProcessing', f'{output}'+'.p') 
fp = open(myPath, 'rb')
PrimaryEnergy = pickle.load(fp)

### PrimaryEnergy_RE considers BM, GO, HY, OC, SO, WN
output = 'GLUCOSE_PrimaryEnergy_RE'
myPath = Path(f'{folder}', 'GLUCOSE_DataProcessing', f'{output}'+'.p') 
fp = open(myPath, 'rb')
PrimaryEnergy_RE = pickle.load(fp)

output = 'GLUCOSE_PrimaryEnergy_NU'
myPath = Path(f'{folder}', 'GLUCOSE_DataProcessing', f'{output}'+'.p') 
fp = open(myPath, 'rb')
PrimaryEnergy_NU = pickle.load(fp)

## ElectricalCapacity
output = 'GLUCOSE_ElectricalCapacity'
myPath = Path(f'{folder}', 'GLUCOSE_DataProcessing', f'{output}'+'.p') 
fp = open(myPath, 'rb')
CapacityElc = pickle.load(fp)

### ElectricalCapacity RE
output = 'GLUCOSE_ElectricalCapacity_RE'
myPath = Path(f'{folder}', 'GLUCOSE_DataProcessing', f'{output}'+'.p') 
fp = open(myPath, 'rb')
RE_ElcCap = pickle.load(fp)

output = 'GLUCOSE_ElectricalCapacity_RE_diff'
myPath = Path(f'{folder}', 'GLUCOSE_DataProcessing', f'{output}'+'.p') 
fp = open(myPath, 'rb')
RE_ElcCap_diff = pickle.load(fp)

### ElectricalCapacity NU
output = 'GLUCOSE_ElectricalCapacity_NU'
myPath = Path(f'{folder}', 'GLUCOSE_DataProcessing', f'{output}'+'.p') 
fp = open(myPath, 'rb')
NU_ElcCap = pickle.load(fp)

output = 'GLUCOSE_ElectricalCapacity_NU_diff'
myPath = Path(f'{folder}', 'GLUCOSE_DataProcessing', f'{output}'+'.p') 
fp = open(myPath, 'rb')
NU_ElcCap_diff = pickle.load(fp)

### ElectricalCapacity CCS
output = 'GLUCOSE_ElectricalCapacity_CCS'
myPath = Path(f'{folder}', 'GLUCOSE_DataProcessing', f'{output}'+'.p') 
fp = open(myPath, 'rb')
CCS_ElcCap = pickle.load(fp)

## LandUse
output = 'GLUCOSE_LandUse'
myPath = Path(f'{folder}', 'GLUCOSE_DataProcessing', f'{output}'+'.p') 
fp = open(myPath, 'rb')
LandUse = pickle.load(fp)

output = 'GLUCOSE_LandUse_LF'
myPath = Path(f'{folder}', 'GLUCOSE_DataProcessing', f'{output}'+'.p') 
fp = open(myPath, 'rb')
LandUse_LF = pickle.load(fp)

## AnnualEmissions, total
output = 'GLUCOSE_Emissions'
myPath = Path(f'{folder}', 'GLUCOSE_DataProcessing', f'{output}'+'.p') 
fp = open(myPath, 'rb')
Emissions = pickle.load(fp)
Emissions_GHG = Emissions['CO2EQ']
Emissions_GHG = Emissions_GHG.iloc[:,:-10]
Emissions_Water = Emissions['WATER']
Emissions_Water = Emissions_Water.iloc[:,:-10]

### Emissions, total 2020-2050
#Emissions_GHG['Total, 2020-2050'] = Emissions_GHG.loc[:,2020:2050].sum(axis=1)

### DirectAirCapture emissions
output = 'GLUCOSE_Emissions_DAC'
myPath = Path(f'{folder}', 'GLUCOSE_DataProcessing', f'{output}'+'.p') 
fp = open(myPath, 'rb')
Emissions_DAC = pickle.load(fp)
Emissions_DAC = Emissions_DAC.iloc[:,:-10]
#%%
myPath = Path(f'{folder}', 'ofinterest1_runs.csv')
relevant_runs = pd.read_csv(myPath)
relevant_runs['0'] = relevant_runs['0'].astype(int)
for run in relevant_runs['0']:
    ## ProductionByTechnologyAnnual - Primary Energy
    PrimaryEnergy[run]=PrimaryEnergy[run].iloc[:-10,:]
    PrimaryEnergy[run].rename(columns = {'C1CO00I00':'Coal', 'C1NG00I00':'NaturalGas', 'C1NU00I00':'Nuclear', 'C1OI00I00':'Oil', 'BM':'Biomass', 'GO':'Geothermal', 'HY':'Hydro', 'OC':'Ocean', 'SO':'Solar', 'WD':'Wind'}, inplace = True)
    PrimaryEnergy[run]=PrimaryEnergy[run].loc[:, ['Coal','Oil','NaturalGas','Nuclear','Hydro','Solar','Wind','Biomass','Geothermal','Ocean']]
    fig1 = px.bar(PrimaryEnergy[run], x=PrimaryEnergy[run].index, y=PrimaryEnergy[run].columns, color_discrete_sequence=[px.colors.qualitative.Dark24[5],px.colors.qualitative.Light24[0],px.colors.qualitative.Dark24[15],px.colors.qualitative.Dark24[4],px.colors.qualitative.Dark24[9],px.colors.qualitative.Light24[7],px.colors.qualitative.Dark24[17],px.colors.qualitative.Light24[8],px.colors.qualitative.Dark24[13],px.colors.qualitative.Dark24[0]])
    fig1.update_layout(
        title="Primary Energy",
        xaxis_title="Years",
        yaxis_title="Primary Energy [EJ]",
        legend_title="Legend")
    fig1.update_traces(hovertemplate='Year: %{x} <br>Primary Energy: %{y}')
    ## TotalCapacityAnnual - Electrical Capacity
    CapacityElc[run]=CapacityElc[run].iloc[:-10,:]
    CapacityElc[run].rename(columns = {'OC':'Ocean', 'GO':'Geothermal', 'BM':'Biomass', 'BMCS':'Biomass+CCS', 'WD':'Wind', 'SO':'Solar', 'HY':'Hydro', 'NU':'Nuclear', 'NG':'NaturalGas','NGCS':'NaturalGas+CCS', 'HF':'Oil|HeavyFuel', 'LF':'Oil|LightFuel', 'OI':'Oil', 'CO':'Coal', 'COCS':'Coal+CCS'}, inplace = True)
    CapacityElc[run]=CapacityElc[run].loc[:,['Coal','Coal+CCS','Oil|HeavyFuel','Oil|LightFuel','Oil','NaturalGas','NaturalGas+CCS','Nuclear','Hydro','Solar','Wind','Biomass','Biomass+CCS','Geothermal','Ocean']]
    fig2 = px.bar(CapacityElc[run], x=CapacityElc[run].index, y=CapacityElc[run].columns, color_discrete_sequence=[px.colors.qualitative.Dark24[5],px.colors.qualitative.Dark2[7],px.colors.qualitative.Light24[0],px.colors.qualitative.Light24[0],px.colors.qualitative.Light24[0],px.colors.qualitative.Dark24[15],px.colors.qualitative.Light24[12],px.colors.qualitative.Dark24[4],px.colors.qualitative.Dark24[9],px.colors.qualitative.Light24[7],px.colors.qualitative.Dark24[17],px.colors.qualitative.Light24[8],px.colors.qualitative.Light24[19],px.colors.qualitative.Dark24[13],px.colors.qualitative.Dark24[0]])
    fig2.update_layout(
        title="Electrical Capacity",
        xaxis_title="Years",
        yaxis_title="Electrical Capacity [TW]",
        legend_title="Legend")
    fig2.update_traces(hovertemplate='Year: %{x} <br>Capacity|Electricity: %{y}')
    ## TotalAnnualTechnologyActivityByMode - Land Use
    LandUse[run]=LandUse[run].iloc[:-10,:]
    LandUse[run].rename(columns = {'LA1':'Cropland|Rainfed', 'LA1_i':'Cropland|Irrigated', 'LA2':'Pasture', 'LF1':'Forest|Primary', 'LF2':'Forest|Other', 'LO':'Other Land'}, inplace = True)
    fig3 = px.bar(LandUse[run], x=LandUse[run].index, y=LandUse[run].columns, 
                color_discrete_sequence=[px.colors.qualitative.Dark24[0], px.colors.qualitative.Dark24[9], px.colors.qualitative.Set1[6], px.colors.qualitative.Prism[3], px.colors.qualitative.Prism[4], px.colors.qualitative.Prism[10]])
    fig3.update_layout(
        title="Land Use",
        xaxis_title="Years",
        yaxis_title="Land Area [mio ha]",
        legend_title="Legend")
    fig3.update_traces(hovertemplate='Year: %{x} <br>Land Area: %{y}')
    ## Primary Energy, Renewables - penetration
    RES=PrimaryEnergy_RE.T
    RES=RES.iloc[:,:-10]
    # fig4 = px.line(RES, x=RES.index, y=RES.columns)
    # fig4.update_layout(
    #     title="Primary Energy|Renewables",
    #     xaxis_title="Years",
    #     yaxis_title="Primary Energy [EJ]", showlegend=False)
    # fig4.update_traces(hovertemplate='Year: %{x} <br>Primary Energy: %{y}')
    # fig4.show()
    run_selection = RES.iloc[:, run:(run+1)]
    fig4r = px.line(run_selection, x=run_selection.index, y=run_selection.columns)
    fig4r.update_layout(
        title="Primary Energy|Renewables",
        xaxis_title="Years",
        yaxis_title="Primary Energy [EJ]", showlegend=False)
    fig4r.update_traces(hovertemplate='Year: %{x} <br>Emissions: %{y}')
    ## Primary Energy, Nuclear - penetration
    NU = PrimaryEnergy_NU.T
    NU=NU.iloc[:,:-10]
    # fig5 = px.line(NU, x=NU.index, y=NU.columns)
    # fig5.update_layout(
    #     title="Primary Energy|Nuclear",
    #     xaxis_title="Years",
    #     yaxis_title="Primary Energy [EJ]", showlegend=False)
    # fig5.update_traces(hovertemplate='Year: %{x} <br>Primary Energy: %{y}')
    # fig5.show()
    run_selection = NU.iloc[:, run:(run+1)]
    #print(run_selection)
    fig5r = px.line(run_selection, x=run_selection.index, y=run_selection.columns)
    fig5r.update_layout(
        title="Primary Energy|Nuclear",
        xaxis_title="Years",
        yaxis_title="Primary Energy [EJ]", showlegend=False)
    fig5r.update_traces(hovertemplate='Year: %{x} <br>Emissions: %{y}')
    ## DAC technology - penetration
    DAC=Emissions_DAC.T
    # fig6 = px.line(DAC, x=DAC.index, y=DAC.columns)
    # fig6.update_layout(
    #     title="Emissions|CO2EQ|DirectAirCapture",
    #     xaxis_title="Years",
    #     yaxis_title="Emissions [Gt CO2EQ]", showlegend=False)
    # fig6.update_traces(hovertemplate='Year: %{x} <br>Emissions: %{y}')
    # fig6.show()
    run_selection = DAC.iloc[:, run:(run+1)]
    fig6r = px.line(run_selection, x=run_selection.index, y=run_selection.columns)
    fig6r.update_layout(
        title="Emissions|CO2EQ|DirectAirCapture",
        xaxis_title="Years",
        yaxis_title="Emissions [Gt CO2EQ]", showlegend=False)
    fig6r.update_traces(hovertemplate='Year: %{x} <br>Emissions: %{y}')
    ## CCS technologies - penetration
    CCS=CCS_ElcCap.T
    # fig = px.line(CCS, x=CCS.index, y=CCS.columns)
    # fig.show()
    run_selection = CCS.iloc[:, run:(run+1)]
    fig_r = px.line(run_selection, x=run_selection.index, y=run_selection.columns)
    fig_r.update_layout(
        title="ElectricapCapacity|CCS",
        xaxis_title="Years",
        yaxis_title="Capacity [TW]", showlegend=False)
    fig_r.update_traces(hovertemplate='Year: %{x} <br>Emissions: %{y}')
    ## CO2EQ emissions trajectories
    CO2EQ=Emissions_GHG.T
    # fig7 = px.line(CO2EQ, x=CO2EQ.index, y=CO2EQ.columns)
    # fig7.update_layout(
    #     title="Emissions|CO2EQ|Total",
    #     xaxis_title="Years",
    #     yaxis_title="Emissions [Gt CO2EQ]", showlegend=False)
    # fig7.update_traces(hovertemplate='Year: %{x} <br>Emissions: %{y}')
    # fig7.show()
    run_selection = CO2EQ.iloc[:, run:(run+1)]
    #print(run_selection)
    fig7r = px.line(run_selection, x=run_selection.index, y=run_selection.columns)
    fig7r.update_layout(
        title="Emissions|CO2EQ|Total",
        xaxis_title="Years",
        yaxis_title="Emissions [Gt CO2EQ]", showlegend=False)
    fig7r.update_traces(hovertemplate='Year: %{x} <br>Emissions: %{y}')
    myPath_html_run = Path(f'{folder}', 'img', 'GLUCOSE_viz_'+f'{run}'+'.html')
    with open(myPath_html_run, 'a') as f:
        f.write(fig1.to_html(full_html=False, include_plotlyjs='cdn'))
        f.write(fig2.to_html(full_html=False, include_plotlyjs='cdn'))
        f.write(fig3.to_html(full_html=False, include_plotlyjs='cdn'))
        f.write(fig4r.to_html(full_html=False, include_plotlyjs='cdn'))
        f.write(fig5r.to_html(full_html=False, include_plotlyjs='cdn'))
        f.write(fig_r.to_html(full_html=False, include_plotlyjs='cdn'))
        f.write(fig6r.to_html(full_html=False, include_plotlyjs='cdn'))
        f.write(fig7r.to_html(full_html=False, include_plotlyjs='cdn'))

#%%
## Primary Energy, Renewables - penetration
RES=PrimaryEnergy_RE.T
RES=RES.iloc[:,:-10]

fig4 = px.line(RES, x=RES.index, y=RES.columns)
fig4.update_layout(
    title="Primary Energy|Renewables",
    xaxis_title="Years",
    yaxis_title="Primary Energy [EJ]", showlegend=False)
fig4.update_traces(hovertemplate='Year: %{x} <br>Primary Energy: %{y}')

## Primary Energy, Nuclear - penetration
NU = PrimaryEnergy_NU.T
NU=NU.iloc[:,:-10]

fig5 = px.line(NU, x=NU.index, y=NU.columns)
fig5.update_layout(
    title="Primary Energy|Nuclear",
    xaxis_title="Years",
    yaxis_title="Primary Energy [EJ]", showlegend=False)
fig5.update_traces(hovertemplate='Year: %{x} <br>Primary Energy: %{y}')

## LandUse, Forest land
# ForestLand = pd.DataFrame(index=replications, columns=LandUse[0].index).fillna(0)
# for run in replications:
#     forest = LandUse[run].loc[:, LandUse[run].columns.str.startswith('Forest')]
#     forest = forest.sum(axis=1).transpose()
#     ForestLand.iloc[run] = forest.transpose()
# ForestLand = ForestLand.iloc[:,:-10]

# fig_forest = px.line(ForestLand.T, x=ForestLand.columns, y=ForestLand.index)
# fig_forest.update_layout(
#     title="LandUse|Forest",
#     xaxis_title="Years",
#     yaxis_title="Land area [mio ha]", showlegend=False)
# fig_forest.update_traces(hovertemplate='Year: %{x} <br>Primary Energy: %{y}')

## DAC technology - penetration
DAC=Emissions_DAC.T
fig6 = px.line(DAC, x=DAC.index, y=DAC.columns)
fig6.update_layout(
    title="Emissions|CO2EQ|DirectAirCapture",
    xaxis_title="Years",
    yaxis_title="Emissions [Gt CO2EQ]", showlegend=False)
fig6.update_traces(hovertemplate='Year: %{x} <br>Emissions: %{y}')

## CCS technologies - penetration
CCS=CCS_ElcCap.T
#print(CCS_ElcCap)
fig = px.line(CCS, x=CCS.index, y=CCS.columns)

## CO2EQ emissions trajectories
CO2EQ=Emissions_GHG.T
fig7 = px.line(CO2EQ, x=CO2EQ.index, y=CO2EQ.columns)
fig7.update_layout(
    title="Emissions|CO2EQ|Total",
    xaxis_title="Years",
    yaxis_title="Emissions [Gt CO2EQ]", showlegend=False)
fig7.update_traces(hovertemplate='Year: %{x} <br>Emissions: %{y}')

## scatter plot - runs
RE_ElcCap_diff['mean_value']= RE_ElcCap_diff.mean(axis=1)
data = {'RE capacity, yearly increase':RE_ElcCap_diff['mean_value'].to_list(), 'DAC penetration, 2050':Emissions_DAC[2050].to_list(), 'Runs':replications}
solution_space = pd.DataFrame(data=data)

RE_max = (1+0.05)*solution_space['RE capacity, yearly increase'].min()

RE_min = solution_space['RE capacity, yearly increase'].min()
DAC_max = solution_space['DAC penetration, 2050'].max()
DAC_min = (1+0.05)*solution_space['DAC penetration, 2050'].max()
print(RE_max, RE_min, DAC_max, DAC_min)

fig_scatter = px.scatter(solution_space, x='DAC penetration, 2050', y= 'RE capacity, yearly increase', color="Runs", width=800, height=600, labels={ # replaces default labels by column name
                "DAC penetration, 2050": "Direct Air Capture technology penetration, 2050 [Gt CO2eq.]",  "RE capacity, yearly increase": "Renewable Energy capacity, yearly increase [TW]"}, template="plotly_white")
fig_scatter.add_shape( # add a horizontal "target" line
    type="line", line_color="red", line_width=4, opacity=1,
    x0=DAC_min, x1=DAC_min, y0=RE_max, y1=(RE_min-0.005)
)
fig_scatter.add_shape( # add a horizontal "target" line
    type="line", line_color="red", line_width=4, opacity=1,
    x0=(DAC_min), x1=(DAC_max+0.2), y0=RE_max, y1=RE_max
)

#%% save figures
myPath_html = Path(f'{folder}', 'img', 'GLUCOSE_viz.html')
with open(myPath_html, 'a') as f:
    #f.write(fig1.to_html(full_html=False, include_plotlyjs='cdn'))
    #f.write(fig2.to_html(full_html=False, include_plotlyjs='cdn'))
    #f.write(fig3.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(fig4.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(fig5.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(fig6.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(fig7.to_html(full_html=False, include_plotlyjs='cdn'))
    # f.write(fig_forest.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(fig_scatter.to_html(full_html=False, include_plotlyjs='cdn'))
# %%
