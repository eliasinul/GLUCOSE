# Log changes
## Solar and Wind resource constraints
Increased estimates for solar and wind renewable capacity potential
- Changing TotalAnnualCapacity and TotatlAnnualMaxCapacityInvestment for solar PV technologies (C1SOV1P00, C1SOV2P00), based on SolarPower Europe (2022) "Global Market Outlook for Solar Power 2022-2026" <https://www.solarpowereurope.org/insights/market-outlooks/global-market-outlook-for-solar-power-2022>
- Changing TotalAnnualCapacity and TotatlAnnualMaxCapacityInvestment for wind on- and off-shore technologies (C1WDONP00, C1WDOFP00), based on Global Wind Energy Council (2022) "Global Wind Report 2022" <https://gwec.net/global-wind-report-2022/>

## Maritime and Aviation transport efficiency
Increased efficiency of Maritime and Aviation transport technologies, based on IEA (2020) "Energy Technology Perspectives 2020" <https://www.iea.org/reports/energy-technology-perspectives-2020>:
- Changing InputActivityRatio of C1_P_HFO into Maritime transport technology (C1HFMRF00)
- Changing InputActivityRatio of C1_P_LFO into Aviation transport technology (C1LFAVF00)

## Direct Air Capture technology
Adding Direct Air Capture (DAC) as backstop technologies, to allow for model flexibility and negative emissions:
- C1ENDA1CS, using secondary electricity (C1_S_ELC) and heat coming from natural gas (C1_S_HEAT)
- C1ENDA2CS, using secondary electricity (C1_S_ELC) and heat coming from waste heat recovery from industry (C1_F_HEA_Ir)
    - adding new fuel C1_F_HEA_Ir and related OutPutActivityRatio from all materials industry technolgies

Sources:
- IEA (2022) "CCUS around the world in 2021, DAC1" <https://www.iea.org/reports/ccus-around-the-world-in-2021/dac-1>
- IEA (2021) "Direct Air Capture" <https://www.iea.org/reports/direct-air-capture>
- Realmonte et al. (2019) "An inter-model assessment of the role of direct air capture in deep mitigation pathways" <https://doi.org/10.1038/s41467-019-10842-5>

## GHG Emissions constraint (CO2EQ)
- AnnualEmissionLimit: equal the GLUCOSE Baseline trajectory (high-value, increasing over modelling period) for the period 2010-2020 
- ModelPeriodEmissionLimit: added based on IPCC AR6 WG1 (2021) on "Climate Change 2021: The Physical Science Basis report", Summary Volume <https://www.ipcc.ch/report/ar6/wg1/downloads/report/IPCC_AR6_WGI_SummaryVolume.pdf>
    - Page 29, Table SPM.2 - Estimated remaining carbon budgets from the beginning of 2020 (GtCO2) [with Likelyhood of limiting global warming to temperature limit of 83%].

