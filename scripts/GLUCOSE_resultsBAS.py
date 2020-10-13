"""
Trying to automate the results visualisation for GLUCOSE
"""
#%%
import pandas as pd
import numpy as np

import re
import matplotlib.pyplot as plt 
import seaborn as sns

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

GLUCOSE_techs = pd.read_excel('GLUCOSE_configuration.xlsx', sheet_name='Technologies')
EnergyTechs = GLUCOSE_techs.groupby(['Module']).get_group('energy')

#%%
GLUCOSE_fuels = pd.read_excel('GLUCOSE_configuration.xlsx', sheet_name='Fuels')
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
    else:    
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


#%%
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

#%% Dashboard colours

colours = dict(
    coal = 'rgb(0, 0, 0)',
    oil = 'rgb(121, 43, 41)',
    gas = 'rgb(86, 108, 140)',
    nuclear = 'rgb(186, 28, 175)',
    biomass = 'rgb(172, 199, 119)',
    biofuel = 'rgb(79, 98, 40)',
    hydro = 'rgb(0, 139, 188)',
    wind = 'rgb(143, 119, 173)',
    solar = 'rgb(230, 175, 0)',
    geothermal = 'rgb(192, 80, 77)',
    ocean ='rgb(22, 54, 92)',)

#%% dash app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='GLUCOSE results'),
    
    html.H2(children='Total Annual Capacity'),
    html.Div([
        html.Label('Installed power generation capacity'),
        dcc.Dropdown(
            id='tca',
            options = [{'label': i, 'value': TCA[i].VALUE} for i in TCA],
            value = 'biomass'
            ),
        dcc.Graph(
            id='tca-graph'
            )
        ], style={'width': '49%', 'display': 'inline-block'}),
    
    html.H2(children='Power generation'),
    html.Div([        
        html.Label('Electricity generation'),
        dcc.Dropdown(
            id='pbta',
            options = [{'label': i, 'value': PBTA[i].VALUE} for i in PBTA],
            value = 'biomass'
            ),
        dcc.Graph(
            id='Power-generation'
            )
        ], style={'width': '49%', 'display': 'inline-block'})
])

app.layout = html.Div(children=[
    html.H1(children='GLUCOSE results'),

    html.Div(children='''
        A dash board for comparing modelling results between GLUCOSE and SSP IAMs models.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                 {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                #{'x': z.YEAR, 'y': z.DATA, 'type': 'line', 'name': z.MODEL},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Capacity|Electricity'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

# %%
