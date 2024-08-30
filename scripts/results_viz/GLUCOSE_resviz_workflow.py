import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly
import plotly.express as px
from pathlib import Path
import glob
import pickle

import os
import sys


# locate folder with data
def visualise_results(folder):
    # folder = 'results/GLUCOSE_noDA2CS_9/results_processed'
    folder = os.sep.join(folder.split('/')[:-1])

    myPath = Path(f'{folder}')
    tifCounter = len(glob.glob1(myPath,"*.ilp"))
    print('Infeasible scenarios:', tifCounter)

    myPath = Path(f'{folder}')
    n_replications = int(len(glob.glob1(myPath,"*.sol")))
    print("Number of replications/runs:", n_replications)
    replications = list(range(0,n_replications))

    #%% read output data (results)
    ## PrimaryEnergy
    output = 'GLUCOSE_PrimaryEnergy'
    myPath = Path(f'{folder}', 'results_processed', f'{output}'+'.p') 
    fp = open(myPath, 'rb')
    PrimaryEnergy = pickle.load(fp)

    ### PrimaryEnergy_RE considers BM, GO, HY, OC, SO, WN
    output = 'GLUCOSE_PrimaryEnergy_RE'
    myPath = Path(f'{folder}', 'results_processed', f'{output}'+'.p') 
    fp = open(myPath, 'rb')
    PrimaryEnergy_RE = pickle.load(fp)

    output = 'GLUCOSE_PrimaryEnergy_NU'
    myPath = Path(f'{folder}', 'results_processed', f'{output}'+'.p') 
    fp = open(myPath, 'rb')
    PrimaryEnergy_NU = pickle.load(fp)

    ## ElectricalCapacity
    output = 'GLUCOSE_ElectricalCapacity'
    myPath = Path(f'{folder}', 'results_processed', f'{output}'+'.p') 
    fp = open(myPath, 'rb')
    CapacityElc = pickle.load(fp)

    ### ElectricalCapacity RE
    output = 'GLUCOSE_ElectricalCapacity_RE'
    myPath = Path(f'{folder}', 'results_processed', f'{output}'+'.p')  
    fp = open(myPath, 'rb')
    RE_ElcCap = pickle.load(fp)

    output = 'GLUCOSE_ElectricalCapacity_RE_diff'
    myPath = Path(f'{folder}', 'results_processed', f'{output}'+'.p')  
    fp = open(myPath, 'rb')
    RE_ElcCap_diff = pickle.load(fp)

    ### ElectricalCapacity NU
    output = 'GLUCOSE_ElectricalCapacity_NU'
    myPath = Path(f'{folder}', 'results_processed', f'{output}'+'.p')  
    fp = open(myPath, 'rb')
    NU_ElcCap = pickle.load(fp)

    output = 'GLUCOSE_ElectricalCapacity_NU_diff'
    myPath = Path(f'{folder}', 'results_processed', f'{output}'+'.p')  
    fp = open(myPath, 'rb')
    NU_ElcCap_diff = pickle.load(fp)

    ### ElectricalCapacity CCS
    output = 'GLUCOSE_ElectricalCapacity_CCS'
    myPath = Path(f'{folder}', 'results_processed', f'{output}'+'.p') 
    fp = open(myPath, 'rb')
    CCS_ElcCap = pickle.load(fp)

    ## LandUse
    output = 'GLUCOSE_LandUse'
    myPath = Path(f'{folder}', 'results_processed', f'{output}'+'.p') 
    fp = open(myPath, 'rb')
    LandUse = pickle.load(fp)

    output = 'GLUCOSE_LandUse_LF'
    myPath = Path(f'{folder}', 'results_processed', f'{output}'+'.p') 
    fp = open(myPath, 'rb')
    LandUse_LF = pickle.load(fp)

    ## IndustryProduction
    output = 'GLUCOSE_IndustryProduction'
    myPath = Path(f'{folder}', 'results_processed', f'{output}'+'.p') 
    fp = open(myPath, 'rb')
    IndustryProd = pickle.load(fp)

    ## AnnualEmissions, total
    output = 'GLUCOSE_Emissions'
    myPath = Path(f'{folder}', 'results_processed', f'{output}'+'.p') 
    fp = open(myPath, 'rb')
    Emissions = pickle.load(fp)
    Emissions_GHG = Emissions['CO2EQ']
    #Emissions_GHG = Emissions_GHG.iloc[:-10]
    Emissions_Water = Emissions['WATER']
    #Emissions_Water = Emissions_Water.iloc[:-10]

    ### Emissions, total 2020-2050
    #Emissions_GHG['Total, 2020-2050'] = Emissions_GHG.loc[:,2020:2050].sum(axis=1)

    ### DirectAirCapture emissions
    output = 'GLUCOSE_Emissions_DAC'
    myPath = Path(f'{folder}', 'results_processed', f'{output}'+'.p') 
    fp = open(myPath, 'rb')
    Emissions_DAC = pickle.load(fp)
    #Emissions_DAC = Emissions_DAC.iloc[:,:-10]

    #%% set run
    run = 0

    #%% ProductionByTechnologyAnnual - Primary Energy
    ### option 1
    #PrimaryEnergy[0].plot.area()

    ### option 2
    PrimaryEnergy=PrimaryEnergy.iloc[:-10,:]

    PrimaryEnergy.rename(columns = {'C1CO00I00':'Coal', 'C1NG00I00':'NaturalGas', 'C1NU00I00':'Nuclear', 'C1OI00I00':'Oil', 'BM':'Biomass', 'GO':'Geothermal', 'HY':'Hydro', 'OC':'Ocean', 'SO':'Solar', 'WD':'Wind'}, inplace = True)
    PrimaryEnergy=PrimaryEnergy.loc[:, ['Coal','Oil','NaturalGas','Nuclear','Hydro','Solar','Wind','Biomass','Geothermal','Ocean']]
    fig1 = px.bar(PrimaryEnergy, x=PrimaryEnergy.index, y=PrimaryEnergy.columns, color_discrete_sequence=[px.colors.qualitative.Dark24[5],px.colors.qualitative.Light24[0],px.colors.qualitative.Dark24[15],px.colors.qualitative.Dark24[4],
                                                                                                        px.colors.qualitative.Dark24[9],px.colors.qualitative.Light24[7],px.colors.qualitative.Dark24[17],px.colors.qualitative.Light24[8],px.colors.qualitative.Dark24[13],px.colors.qualitative.Dark24[0]], height=700, width=1400)
    fig1.update_layout(
        title="Primary Energy",
        xaxis_title="Years",
        yaxis_title="Primary Energy [EJ]",
        legend_title="Legend")
    fig1.update_traces(hovertemplate='Year: %{x} <br>Primary Energy: %{y}')
    # fig1.show()

    #%% TotalCapacityAnnual - Electrical Capacity
    ### option 1
    #CapacityElc[0].plot.area()

    ### option 2
    CapacityElc=CapacityElc.iloc[:-10,:]

    CapacityElc.rename(columns = {'OC':'Ocean', 'GO':'Geothermal', 'BM':'Biomass', 'BMCS':'Biomass+CCS', 'WD':'Wind', 'SO':'Solar', 'HY':'Hydro', 'NU':'Nuclear', 'NG':'NaturalGas','NGCS':'NaturalGas+CCS', 'HF':'Oil|HeavyFuel', 'LF':'Oil|LightFuel', 'OI':'Oil', 'CO':'Coal', 'COCS':'Coal+CCS'}, inplace = True)
    CapacityElc=CapacityElc.loc[:,['Coal','Coal+CCS','Oil|HeavyFuel','Oil|LightFuel','Oil','NaturalGas','NaturalGas+CCS','Nuclear','Hydro','Solar','Wind','Biomass','Biomass+CCS','Geothermal','Ocean']]
    fig2 = px.bar(CapacityElc, x=CapacityElc.index, y=CapacityElc.columns, color_discrete_sequence=[px.colors.qualitative.Dark24[5],px.colors.qualitative.Dark2[7],px.colors.qualitative.Light24[0],px.colors.qualitative.Light24[0],px.colors.qualitative.Light24[0],px.colors.qualitative.Dark24[15],
                                                                                                    px.colors.qualitative.Light24[12],px.colors.qualitative.Dark24[4],px.colors.qualitative.Dark24[9],px.colors.qualitative.Light24[7],px.colors.qualitative.Dark24[17],px.colors.qualitative.Light24[8],
                                                                                                    px.colors.qualitative.Light24[19],px.colors.qualitative.Dark24[13],px.colors.qualitative.Dark24[0]], height=700, width=1400)
    fig2.update_layout(
        title="Electrical Capacity",
        xaxis_title="Years",
        yaxis_title="Electrical Capacity [TW]",
        legend_title="Legend")
    fig2.update_traces(hovertemplate='Year: %{x} <br>Capacity|Electricity: %{y}')
    # fig2.show()

    #%% read in GLUCOSE results: LandUse - Forest
    ForestLand = pd.DataFrame(columns=LandUse.index).fillna(0)

    forest = LandUse.loc[:, LandUse.columns.str.startswith('Forest|')]
    ForestLand = forest.sum(axis=1)

    #%% TotalAnnualTechnologyActivityByMode - Land Use
    ### option 1
    #LandUse[0].plot.area()

    ### option 2
    LandUse=LandUse.iloc[:-10,:]

    LandUse.rename(columns = {'LA1':'Cropland|Rainfed', 'LA1_i':'Cropland|Irrigated', 'LA2':'Pasture', 'LF1':'Forest|Primary', 'LF2':'Forest|Other', 'LO':'Other Land'}, inplace = True)
    fig3 = px.bar(LandUse, x=LandUse.index, y=LandUse.columns, 
                color_discrete_sequence=[px.colors.qualitative.Dark24[0], px.colors.qualitative.Dark24[9], px.colors.qualitative.Set1[6], px.colors.qualitative.Prism[3], px.colors.qualitative.Prism[4], px.colors.qualitative.Prism[10]], height=700, width=1400)
    fig3.update_layout(
        title="Land Use",
        xaxis_title="Years",
        yaxis_title="Land Area [mio ha]",
        legend_title="Legend")
    fig3.update_yaxes(rangemode='tozero', matches=None) #, showticklabels=True)
    fig3.update_traces(hovertemplate='Year: %{x} <br>Land Area: %{y}')
    # fig3.show()

    fig_forest = px.line(ForestLand, x=ForestLand.index, y=ForestLand, height=600, width=1200)
    fig_forest.update_layout(
        title="LandUse|Forest",
        xaxis_title="Years",
        yaxis_title="Land area [mio ha]", showlegend=False)
    fig_forest.update_yaxes(rangemode='tozero', matches=None, showticklabels=True)
    fig_forest.update_traces(hovertemplate='Year: %{x} <br>Primary Energy: %{y}')
    # fig_forest.show()

    #%% ProductionByTechnologyAnnual - Industry Production
    ### option 1
    #LandUse[0].plot.area()

    ### option 2
    #IndustryProd=LandUse.iloc[:-10,:]

    #IndustryProd.rename(columns = {'LA1':'Cropland|Rainfed', 'LA1_i':'Cropland|Irrigated', 'LA2':'Pasture', 'LF1':'Forest|Primary', 'LF2':'Forest|Other', 'LO':'Other Land'}, inplace = True)
    fig4 = px.bar(IndustryProd, x=IndustryProd.index, y=IndustryProd.columns, 
                color_discrete_sequence=[px.colors.qualitative.Pastel[10], px.colors.qualitative.Pastel2[7], px.colors.qualitative.G10[9], 
                                        px.colors.qualitative.Dark24[22], px.colors.qualitative.Plotly[7], px.colors.qualitative.T10[8], px.colors.qualitative.Set1[6], px.colors.qualitative.G10[4], px.colors.qualitative.D3[4],
                                        px.colors.qualitative.Set1[3], px.colors.qualitative.Dark2[1], px.colors.qualitative.Set2[1]], height=700, width=1400)
    fig4.update_layout(
        title="Industry Production",
        xaxis_title="Years",
        yaxis_title="Materials production [Mt]",
        legend_title="Legend")
    fig4.update_yaxes(rangemode='tozero', matches=None, showticklabels=True)
    fig4.update_traces(hovertemplate='Year: %{x} <br>Material Production: %{y}')
    # fig4.show()

    #%% Primary Energy, Renewables - penetration
    RES=PrimaryEnergy_RE.T
    #RES=RES.iloc[:-10]

    fig5 = px.line(RES, x=RES.index, y=RES, height=700, width=1400)
    fig5.update_layout(
        title="Primary Energy|Renewables",
        xaxis_title="Years",
        yaxis_title="Primary Energy [EJ]", showlegend=False)
    fig5.update_yaxes(rangemode='tozero', matches=None, showticklabels=True)
    fig5.update_traces(hovertemplate='Year: %{x} <br>Primary Energy: %{y}')
    # fig5.show()


    #%% Primary Energy, Nuclear - penetration
    # NU = PrimaryEnergy_NU.transpose()
    # #NU=NU.iloc[:,:-10]

    # fig6 = px.line(NU, x=NU.index, y=NU)
    # fig6.update_layout(
    #     title="Primary Energy|Nuclear",
    #     xaxis_title="Years",
    #     yaxis_title="Primary Energy [EJ]", showlegend=False)
    # fig6.update_yaxes(rangemode='tozero', matches=None, showticklabels=True)
    # fig6.update_traces(hovertemplate='Year: %{x} <br>Primary Energy: %{y}')
    # fig6.show()

    # # run_selection = NU.iloc[:, run:(run+1)]
    # # #print(run_selection)
    # # fig5r = px.line(run_selection, x=run_selection.index, y=run_selection.columns)
    # # fig5r.update_layout(
    # #     title="Primary Energy|Nuclear",
    # #     xaxis_title="Years",
    # #     yaxis_title="Primary Energy [EJ]", showlegend=False)
    # # fig5r.update_traces(hovertemplate='Year: %{x} <br>Emissions: %{y}')
    # # fig5r.show()

    #%% DAC technology - penetration
    DAC=Emissions_DAC.transpose()
    fig7 = px.line(DAC, x=DAC.index, y=DAC, height=700, width=1400)
    fig7.update_layout(
        title="Emissions|CO2EQ|DirectAirCapture",
        xaxis_title="Years",
        yaxis_title="Emissions [Gt CO2EQ]", showlegend=False)
    fig7.update_yaxes(rangemode='tozero', matches=None, showticklabels=True)
    fig7.update_traces(hovertemplate='Year: %{x} <br>Emissions: %{y}')
    # fig7.show()

    #%% CCS technologies - penetration
    #CCS = CCS_ElcCap
    #print(CCS_ElcCap)
    fig8 = px.line(CCS_ElcCap, x=CCS_ElcCap.index, y=CCS_ElcCap, height=700, width=1400)
    fig8.update_layout(
        title="ElectricalCapacity|CCS",
        xaxis_title="Years",
        yaxis_title="Capacity [TW]", showlegend=False)
    fig8.update_traces(hovertemplate='Year: %{x} <br>Emissions: %{y}')
    # fig8.show()

    #%% CO2EQ emissions trajectories
    CO2EQ = Emissions_GHG.T
    fig9 = px.line(CO2EQ, x=CO2EQ.index, y=CO2EQ, height=700, width=1400)
    fig9.update_layout(
        title="Emissions|CO2EQ|Total",
        xaxis_title="Years",
        yaxis_title="Emissions [Gt CO2EQ]", showlegend=False)
    fig9.update_yaxes(rangemode='tozero', matches=None, showticklabels=True)
    fig9.update_traces(hovertemplate='Year: %{x} <br>Emissions: %{y}')
    # fig9.show()

    #%% WATER consumption, trajectories
    WATER=Emissions_Water.T
    fig = px.line(WATER, x=WATER.index, y=WATER, height=700, width=1400)
    fig.update_yaxes(rangemode='tozero', matches=None, showticklabels=True)
    # fig.show()

    #%% # RE_ElcCap_diff['mean_value']= RE_ElcCap_diff.mean(axis=1)
    # data = {'RE capacity, yearly increase':RE_ElcCap_diff['mean_value'].to_list(), 'DAC penetration, 2050':Emissions_DAC[2050].to_list(), 'Runs':replications}
    # solution_space = pd.DataFrame(data=data)

    # RE_max = (1+0.05)*solution_space['RE capacity, yearly increase'].min()

    # RE_min = solution_space['RE capacity, yearly increase'].min()
    # DAC_max = solution_space['DAC penetration, 2050'].max()
    # DAC_min = (1+0.05)*solution_space['DAC penetration, 2050'].max()
    # print(RE_max, RE_min, DAC_max, DAC_min)

    # fig_scatter = px.scatter(solution_space, x='DAC penetration, 2050', y= 'RE capacity, yearly increase', color="Runs", width=800, height=600, labels={ # replaces default labels by column name
    #                 "DAC penetration, 2050": "Direct Air Capture technology penetration, 2050 [Gt CO2eq.]",  "RE capacity, yearly increase": "Renewable Energy capacity, yearly increase [TW]"}, template="plotly_white")
    # fig_scatter.add_shape( # add a horizontal "target" line
    #     type="line", line_color="red", line_width=4, opacity=1,
    #     x0=DAC_min, x1=DAC_min, y0=RE_max, y1=(RE_min-0.005)
    # )
    # fig_scatter.add_shape( # add a horizontal "target" line
    #     type="line", line_color="red", line_width=4, opacity=1,
    #     x0=(DAC_min), x1=(DAC_max+0.2), y0=RE_max, y1=RE_max
    # )
    # # fig.add_vrect(x0=DAC_min, x1=DAC_max, y0=RE_min, y1=RE_max)
    # fig_scatter.show()


    #%% Save images


    folder_path = Path(f'{folder}', 'img')#, 'GLUCOSE_viz.html')
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # folder_path = folder_out
    # folder_path = Path('..', '..', f'{folder}', 'img')#, 'GLUCOSE_viz.html')
    # if not os.path.exists(folder_out):
    #     os.makedirs(folder_out)

    myPath_html = Path(f'{folder_path}', 'GLUCOSE_viz.html')
    with open(myPath_html, 'a') as f:
        f.write(fig1.to_html(full_html=False, include_plotlyjs='cdn'))
        f.write(fig2.to_html(full_html=False, include_plotlyjs='cdn'))
        f.write(fig3.to_html(full_html=False, include_plotlyjs='cdn'))
        f.write(fig4.to_html(full_html=False, include_plotlyjs='cdn'))
        f.write(fig5.to_html(full_html=False, include_plotlyjs='cdn'))
        # f.write(fig6.to_html(full_html=False, include_plotlyjs='cdn'))
        f.write(fig7.to_html(full_html=False, include_plotlyjs='cdn'))
        f.write(fig8.to_html(full_html=False, include_plotlyjs='cdn'))
        f.write(fig9.to_html(full_html=False, include_plotlyjs='cdn'))
        f.write(fig_forest.to_html(full_html=False, include_plotlyjs='cdn'))
        #f.write(fig_scatter.to_html(full_html=False, include_plotlyjs='cdn'))

    return

#%%
if __name__ == "__main__":

    # args = sys.argv[1:]

    # if len(args) != 1:
    #     print("Usage: python GLUCOSE_resviz_workflow.py <folder_in> ")
    #     exit(1)

    # folder_in = args[0]
    # visualise_results(folder_in)
    # folder_out = args[1]

    # scenario = snakemake.wildcards[0] #.params.sc
    folder_in = snakemake.input[0]
    # log_path = snakemake.log[0]

    visualise_results(folder_in)
