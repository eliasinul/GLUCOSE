# Log changes, 2022
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


# Log changes, 2024
## Adding Hydrogen and Methanol production
### Hydrogen production [C1ELHGP00]
Adding one technology [C1ELHGP00] and one fuel - secondary hydrogen [C1_S_HDG].
- Efficiency, CapitalCost and OperationalLife data coming from IEA (2023) "Global Hydrogen Review 2023: Assumptions Annex <https://www.iea.org/reports/global-hydrogen-review-2023#downloads>
- EmissionActivityRatio for WATER, derived from:
    - Office of Energy Efficiency & Renewable Energy, U.S. Dept. of Energy (n.a.) "Hydrogen Storage" <https://www.energy.gov/eere/fuelcells/hydrogen-storage#:~:text=On%20a%20mass%20basis%2C%20hydrogen,44%20MJ%2Fkg%20for%20gasoline.>
    - Rocky Mountain Institute (2023) "Hydrogen Reality Check: Distilling Green Hydrogen’s Water Consumption" <https://rmi.org/hydrogen-reality-check-distilling-green-hydrogens-water-consumption/#:~:text=Per%20chemistry%20fundamentals%2C%209%20liters,20%20L%2Fkg%20is%20needed.>
    - TotalAnnualMax/MixCapacity constraint defined based on IEA (n.a.) "Electrolysers" <https://www.iea.org/energy-system/low-emission-fuels/electrolysers>

### Methanol production [C1ELMHP00]
Adding one technology [C1ELMHP00] and one fuel - secondary methanol [C1_S_MOH].
- Data for EmissionActivityRatio (for WATER and CO2EQ), InputActivityRatio, VariableCost, coming from IRENA (2021) "Innovation Outlook: Renewable Methanol" <https://www.irena.org/publications/2021/Jan/Innovation-Outlook-Renewable-Methanol>

## Adding Maritime transport using Methanol [C1MHMRF00]
Adding one technology [C1MHMRF00] using Methanol [C1_S_MOH] as fuel,
- Data sources:
    - IRENA (2021) "Innovation Outlook: Renewable Methanol" <https://www.irena.org/publications/2021/Jan/Innovation-Outlook-Renewable-Methanol>
    - Lundgren and Wachsmann (2014) "The potential of methanol as a competiitve marine fuel" <https://odr.chalmers.se/items/25e40178-c48e-441e-ade5-f66f81dd5fd1>

## Adding Steel industry using hydrogen [STEHGPLANT]
Adding one technology [STEHGPLANT] using hydrogen [C1_S_HDG] as fuel input to produce steel.
- Data sources:
    - Shahabuddin et al. (2023) "Decarbonisation and hydrogen integration of steel industries: Recent development, challenges and technoeconomic analysis" <https://www.sciencedirect.com/science/article/pii/S0959652623005498#bib5>
    - HYBRIT project:
        - Pei et al. (2023) "Toward a Fossil Free Future with HYBRIT: Development of Iron and Steelmaking Technology in Sweden and Finland" <https://www.mdpi.com/2075-4701/10/7/972>
        - Åhman et al. (2018) "Hydrogen steelmaking for a low-carbon economy: A joint LU-SEI working paper for the HYBRIT project" <https://www.sei.org/publications/hydrogen-steelmaking/>
        - HYBRIT (2017) "Summary of findings from HYBRIT Pre-Feasibility Study 2016–2017" <https://www.hybritdevelopment.se/en/media/hybrit-brochure-english/>

## Adding Aluminium recycling [ALURECYCLE] and Aluminium industry [ALURCPLANT] using recycled aluminium [RCALU]
Adding one technology [ALURECYCLE] to produce recycled aluminium [RCALU].
Adding one technology to represent sustainable aluminium industry [ALURCPLANT] using recycled aluminium [RCALU] as fuel input to produce aluminium.
- Data sources for ALURECYCLE:
    - International Aluminium Institute (2020) "Aluminium Recycling Factsheet" <https://international-aluminium.org/resource/aluminium-recycling-fact-sheet/>
    - IEA (2023) "Aluminium, Technology deployment" <https://www.iea.org/energy-system/industry/aluminium>
- Data sources for ALURCPLANT:
    - Cushman-Roisin and Cremonini (2021) "Data, Statistics, and Useful Numbers for Environmental Sustainability, Chapter 1 - Materials" <https://doi.org/10.1016/B978-0-12-822958-3.00012-1>
    - Deng et al. (2022) "Environmental-Techno-Economic analysis of decarbonization strategies for the Indian aluminum industry" <https://doi.org/10.1016/j.enconman.2022.116455>
    - International Aluminium Institute (2020) "Aluminium Recycling Factsheet" <https://international-aluminium.org/resource/aluminium-recycling-fact-sheet/>
    - IEA (2023) "Aluminium, Technology deployment" <https://www.iea.org/energy-system/industry/aluminium>
    - IEA ETSAP (2012) "Aluminium Production" <https://iea-etsap.org/E-TechDS/PDF/I10_AlProduction_ER_March2012_Final%20GSOK.pdf>

## Adding low-carbon Cement industry with CS [CEMPLANTCS]
Adding a low-carbon Cement industry option [CEMPLANTCS] using carbon capture and storage to lower industry-related CO2EQ emissions.
- Data sources:
    - Roussanaly et al. (2017) "Techno-economic Analysis of MEA CO2 Capture from a Cement Kiln – Impact of Steam Supply Scenario" <https://doi.org/10.1016/j.egypro.2017.03.1761>
    - IEA (2023) "Cement, Innovation" <https://www.iea.org/energy-system/industry/cement>

## Adding high temperature (industrial) heat pump [C1HPINF0I] generating heat for industry [C1_F_HEA_IHP]
Adding high temperature (industrial) heat pump technology option [tech: C1HPINF0I] producing heat for industrial use [fuel: C1_F_HEA_IHP].
- Data sources:
    - Danish Energy Agency (2022) "Technology Data for Industrial Process Heat" <https://ens.dk/en/our-services/technology-catalogues/technology-data-industrial-process-heat>
    - McKinsey & Company (2024) "Industrial heat pumps: Five considerations for future growth" <https://www.mckinsey.com/industries/industrials-and-electronics/our-insights/industrial-heat-pumps-five-considerations-for-future-growth>

## Adding Pulp&Paper industry process [PAPELPLANT] using electrified heat [C1_F_HEA_IHP] from industrial heat pump as input
Adding Pulp&Paper industry process [tech: PAPELPLANT] using electrified heat [fuel: C1_F_HEA_IHP] from industrial heat pump as input, providing a low-carbon alternative to traditional Pulp&Paper industry.
- Data sources:
    - IEA (2023) "Paper, Technology deployment" <https://www.iea.org/energy-system/industry/paper>
    - Zuberi et al (2023) "Techno-economic evaluation of industrial heat pump applications in US pulp and paper, textile, and automotive industries" <https://doi.org/10.1007/s12053-023-10089-6>

## Adding Petrochemical industry process [PETBELPLANT] using electrified heat [C1_F_HEA_IHP] from industrial heat pump as input
Adding Petrochemical industry process [tech: PETBELPLANT] using electrified heat [fuel: C1_F_HEA_IHP] from industrial heat pump to supply 80% of the heat input, allowing for using a higher share of renewable primary energy resources compared to traditional Petrochemical industry.
- Data sources:
    - IEA (2023) "Chemicals, Innovation" <https://www.iea.org/energy-system/industry/chemicals>
