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
- Danish Energy Agency (2024) "Technology Data for Carbon Capture, Transport and Storage" <https://ens.dk/en/our-services/technology-catalogues/technology-data-carbon-capture-transport-and-storage>

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
### Aluminium Recycling [ALURECYCLE] producing recycled aluminium [RCALU]
Adding one technology [ALURECYCLE] to produce recycled aluminium [RCALU].
- Data sources:
    - International Aluminium Institute (2020) "Aluminium Recycling Factsheet" <https://international-aluminium.org/resource/aluminium-recycling-fact-sheet/>
    - IEA (2023) "Aluminium, Technology deployment" <https://www.iea.org/energy-system/industry/aluminium>
### Aluminium industry [ALURCPLANT] using recycled aluminium
Adding one technology to represent sustainable aluminium industry [ALURCPLANT] using recycled aluminium [RCALU] as fuel input to produce aluminium.
- Data sources for ALURCPLANT:
    - Cushman-Roisin and Cremonini (2021) "Data, Statistics, and Useful Numbers for Environmental Sustainability, Chapter 1 - Materials" <https://doi.org/10.1016/B978-0-12-822958-3.00012-1>
    - Deng et al. (2022) "Environmental-Techno-Economic analysis of decarbonization strategies for the Indian aluminum industry" <https://doi.org/10.1016/j.enconman.2022.116455>
    - International Aluminium Institute (2020) "Aluminium Recycling Factsheet" <https://international-aluminium.org/resource/aluminium-recycling-fact-sheet/>
    - IEA (2023) "Aluminium, Technology deployment" <https://www.iea.org/energy-system/industry/aluminium>
    - IEA ETSAP (2012) "Aluminium Production" <https://iea-etsap.org/E-TechDS/PDF/I10_AlProduction_ER_March2012_Final%20GSOK.pdf>

## Adding low-carbon Cement industry with CS [CEMCSPLANT]
Adding a low-carbon Cement industry option [CEMCSPLANT] using carbon capture and storage to lower industry-related CO2EQ emissions.
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


# Model Testing, August 2024
## GLUCOSE_noDA2CS
Action: 
- Removing technology `C1ENDA2CS`.
- Removing TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00` from 2020 onwards.
Effects: no significant difference, more accentuated *bump* in results for 2020-2025, indicating a disruptive change in model behaviour.

# Potential issues with Constraints
## CapacityOfOneTechnologyUnit[r,t,y]
No defined constraint in GLUCOSE.

## TotalAnnualMaxCapacity[r,t,y]
- Constraint defined for hydrogen, methanol, DAC: constrained to 0 till 2020, then slowly allowed to come in.

Potential issues:
- Constraint defined for renewable technologies.

## TotalAnnualMinCapacity[r,t,y]
- Constraint defined for biomass technologies.
- Constrained defined for hydrogen technologies to reflect IEA historical and estimated data.

## TotalAnnualMaxCapacityInvestment[r,t,y]
Potential issues:
- Constraint defined for renewables [techs: C1SOC1P00, C1SOTHF00, C1SOV1P00, C1SOV2P00, C1WDOFP00, C1WDONP00] seem lower than for other fossil fuel techs, and not reflecting potential learing curve, at least till 2025-2028.
- Constraint for biomass, coal, and gass-to-liquid techs seems particularly high.
- Constraint for coal, gass, and oil primary energy import are high - probably because of different capacity units.
- Constaint for DAC tech is also significantly high

## TotalAnnualMinCapacityInvestment[r,t,y]
No defined constraint in GLUCOSE.

## TotalTechnologyAnnualActivityLowerLimit[r,t,y]
Potential issues:
- Constraint defined for for coal, gass, and oil primary energy import [techs: C1CO00I00, C1NG00I00, C1OI00I00] till 2020

## TotalTechnologyAnnualActivityUpperLimit[r,t,y]
Constraint defined for CS technologies [techs: C1BMIGPCS, C1COSCPCS, C1NGCCPCS]

Potential issues:
- Constraint defined for fossil free steel production via hydrogen [tech: STEHGPLANT]
- Constraint defined for recycling aluminium [tech: ALURECYCLE]
- Constraint defined for heat pump technologies [techs: C1HPASF01, C1HPINF0I]
- Constraint defined for solar and wind [techs: C1SOC1P00, C1SOTHF00, C1SOV1P00, C1SOV2P00, C1WDOFP00, C1WDONP00], ocean [tech: C1OCCVP00] and geothermal [techs: C1GOCVP00, C1GOHTF0] technologies: data might be old and need double chec

## TotalTechnologyModelPeriodActivityUpperLimit[r,t]
Constraint defined only for import of primary energy or materials [techs: C1CO00I00, C1NG00I00, C1OI00I00, XALUMINE, XCEMMINE, XPHOMINE, XPOTMINE, XSTEMINE].

## TotalTechnologyModelPeriodActivityLowerLimit[r,t]
No defined constraint in GLUCOSE.

## AnnualEmissionLimit[r,e,y]
Constraint defined for `CO2EQ` emissions, till 2020.

## ModelPeriodEmissionLimit[r,e]
Constraint defined for `CO2EQ` emissions.

# Potential issues with other input Parameters
## ResidualCapacity[r,t,y]
- Lots of residual capacity for industry technologies [techs: ALUPLANT, CEMPLANT, FERTPLANT, PAPPLANT, PETAPLANT, PETBPLANT, STEPLANT] till up to 2040.
- Lots of residual capacity for fossil fuel power technologies [techs: C1COCHP00, C1COIGP00, C1COSCP00, C1HFGCP00, C1NGCCP00, C1NGCCPCH, C1NGGCP00, C1NGGCPCH, C1OIRFP00].

## CapitalCost[r,t,y]
- Costs of CO, NG and BM technologies with or without CCS [techs: C1BMCHP00, C1BMIGPCS, C1COSCP00, C1COSCPCS, C1NGCCP00, C1NGCCPCS] are in the same order of magnitude, with at times CCS technologies being cheaper than non-CCS ones.
- Possibly, Direct Air Capture technology [techs: C1ENDA1CS] is too low.

# Model Testing, August 2024
## GLUCOSE_noDA2CS
Action: 
- Removing technology `C1ENDA2CS` and fuel `C1_F_HEA_Ir`.
- Removing TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00` from 2020 onwards.
- Removing TotalTechnologyAnnualActivityUpperLimit for `STEHGPLANT` from 2020 onwards.
Effects: no significant difference, more accentuated *bump* in results for 2020-2025, indicating a disruptive change in model behaviour.

## GLUCOSE_noDA2CS_2
Action: 
- Removing technology `C1ENDA2CS` and fuel `C1_F_HEA_Ir`.
- Removing TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00` from 2020 onwards.
- Removing TotalTechnologyAnnualActivityUpperLimit for `STEHGPLANT` from 2020 onwards.
- **Removing TotalTechnologyAnnualActivityUpperLimit for `C1HPINF0I` from 2025 onwards.**

Effects: no significant difference.

## GLUCOSE_noDA2CS_3
Action: 
- Removing technology `C1ENDA2CS` and fuel `C1_F_HEA_Ir`.
- Removing TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00` from 2020 onwards.
- Removing TotalTechnologyAnnualActivityUpperLimit for `STEHGPLANT` from 2020 onwards.
- Removing TotalTechnologyAnnualActivityUpperLimit for `C1HPINF0I` from 2025 onwards.
- **Removing TotalTechnologyAnnualActivityUpperLimit for `ALURECYCLE` from 2025 onwards.**

Effects: no significant difference.

## GLUCOSE_noDA2CS_4
Action: 
- Removing technology `C1ENDA2CS` and fuel `C1_F_HEA_Ir`.
- Removing TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00` from 2020 onwards.
- Removing TotalTechnologyAnnualActivityUpperLimit for `STEHGPLANT` from 2020 onwards.
- Removing TotalTechnologyAnnualActivityUpperLimit for `C1HPINF0I` from 2025 onwards.
- Removing TotalTechnologyAnnualActivityUpperLimit for `ALURECYCLE` from 2025 onwards.
- **Reducing ResidualCapacity for `ALUPLANT`, `CEMPLANT`, `FERTPLANT`, `PAPPLANT`, `PETAPLANT`, `PETBPLANT`, `STEPLANT` from 2025 onwards, by reducing the capacity by 30% each year till 2030 and then going to zero.**
- **Reducing ResidualCapacity for `C1COCHP00`, `C1COIGP00`, `C1COSCP00`, `C1HFGCP00`, `C1NGCCP00`, `C1NGCCPCH`, `C1NGGCP00`, `C1NGGCPCH`, `C1OIRFP00` from 2025 onwards, by reducing the capacity by 30% each year till 2030 and then going to zero.**

Effects: no significant difference.

## GLUCOSE_noDA2CS_5
Action: 
- Removing technology `C1ENDA2CS` and fuel `C1_F_HEA_Ir`.
- Removing TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00` from 2020 onwards.
- Removing TotalTechnologyAnnualActivityUpperLimit for `STEHGPLANT` from 2020 onwards.
- Removing TotalTechnologyAnnualActivityUpperLimit for `C1HPINF0I` from 2025 onwards.
- Removing TotalTechnologyAnnualActivityUpperLimit for `ALURECYCLE` from 2025 onwards.
- Reducing ResidualCapacity for `ALUPLANT`, `CEMPLANT`, `FERTPLANT`, `PAPPLANT`, `PETAPLANT`, `PETBPLANT`, `STEPLANT` from 2025 onwards, by reducing the capacity by 30% each year till 2030 and then going to zero.
- Reducing ResidualCapacity for `C1COCHP00`, `C1COIGP00`, `C1COSCP00`, `C1HFGCP00`, `C1NGCCP00`, `C1NGCCPCH`, `C1NGGCP00`, `C1NGGCPCH`, `C1OIRFP00` from 2025 onwards, by reducing the capacity by 30% each year till 2030 and then going to zero.
- **Remove completely TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00`.**

Effects: DAC technology coming in later (from 2030), but overall historical trends in years 2010-2020 are off.

## GLUCOSE_noDA2CS_6
Action: 
- Removing technology `C1ENDA2CS` and fuel `C1_F_HEA_Ir`.
- Removing TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00` from 2020 onwards.
- Removing TotalTechnologyAnnualActivityUpperLimit for `STEHGPLANT` from 2020 onwards.
- Removing TotalTechnologyAnnualActivityUpperLimit for `C1HPINF0I` from 2025 onwards.
- Removing TotalTechnologyAnnualActivityUpperLimit for `ALURECYCLE` from 2025 onwards.
- Reducing ResidualCapacity for `ALUPLANT`, `CEMPLANT`, `FERTPLANT`, `PAPPLANT`, `PETAPLANT`, `PETBPLANT`, `STEPLANT` from 2025 onwards, by reducing the capacity by 30% each year till 2030 and then going to zero.
- Reducing ResidualCapacity for `C1COCHP00`, `C1COIGP00`, `C1COSCP00`, `C1HFGCP00`, `C1NGCCP00`, `C1NGCCPCH`, `C1NGGCP00`, `C1NGGCPCH`, `C1OIRFP00` from 2025 onwards, by reducing the capacity by 30% each year till 2030 and then going to zero.
- Remove completely TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00`.
- **Increase CapitalCost for `C1BMCHP00`, `C1BMIGPCS`, `C1COSCP00`, `C1COSCPCS`, `C1NGCCP00`, `C1NGCCPCS` by 1000 compared to non-CCS alternatives.**
- **Increase CapitalCost for `C1ENDA1CS` by 500.**

Effects: DAC technologies delayed till 2034, coal almost entirely disappearing from the power sector (but overall historical trends in years 2010-2020 are off), CCS still coming in massively in 2020, no ALURCPLANT or STEHGPLANT used.

## GLUCOSE_noDA2CS_7
Action: 
- Removing technology `C1ENDA2CS` and fuel `C1_F_HEA_Ir`.
- Removing TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00` from 2020 onwards.
- Removing TotalTechnologyAnnualActivityUpperLimit for `STEHGPLANT` from 2020 onwards.
- Removing TotalTechnologyAnnualActivityUpperLimit for `C1HPINF0I` from 2025 onwards.
- Removing TotalTechnologyAnnualActivityUpperLimit for `ALURECYCLE` from 2025 onwards.
- Reducing ResidualCapacity for `ALUPLANT`, `CEMPLANT`, `FERTPLANT`, `PAPPLANT`, `PETAPLANT`, `PETBPLANT`, `STEPLANT` from 2025 onwards, by reducing the capacity by 30% each year till 2030 and then going to zero.
- Reducing ResidualCapacity for `C1COCHP00`, `C1COIGP00`, `C1COSCP00`, `C1HFGCP00`, `C1NGCCP00`, `C1NGCCPCH`, `C1NGGCP00`, `C1NGGCPCH`, `C1OIRFP00` from 2025 onwards, by reducing the capacity by 30% each year till 2030 and then going to zero.
- Remove completely TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00`.
- Increase CapitalCost for `C1BMCHP00`, `C1BMIGPCS`, `C1COSCP00`, `C1COSCPCS`, `C1NGCCP00`, `C1NGCCPCS` by 1000 compared to non-CCS alternatives.
- Increase CapitalCost for `C1ENDA1CS` by 500.
- **Mistake found in unit conversion for InputActivityRatio of energy for `ALURCPLANT` - values need to be divided by 1000.**

Effects: (finallly!) ALURCPLANT works and as expected comes in fully, as soon as ALUPLANT does not have ResidualCapacity/other constraint forcing it in.

## GLUCOSE_noDA2CS_8
Action: 
- Removing technology `C1ENDA2CS` and fuel `C1_F_HEA_Ir`.
- Removing TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00` from 2020 onwards.
- Removing TotalTechnologyAnnualActivityUpperLimit for `STEHGPLANT` from 2020 onwards.
- Removing TotalTechnologyAnnualActivityUpperLimit for `C1HPINF0I` from 2025 onwards.
- Removing TotalTechnologyAnnualActivityUpperLimit for `ALURECYCLE` from 2025 onwards.
- Reducing ResidualCapacity for `ALUPLANT`, `CEMPLANT`, `FERTPLANT`, `PAPPLANT`, `PETAPLANT`, `PETBPLANT`, `STEPLANT` from 2025 onwards, by reducing the capacity by 30% each year till 2030 and then going to zero.
- Reducing ResidualCapacity for `C1COCHP00`, `C1COIGP00`, `C1COSCP00`, `C1HFGCP00`, `C1NGCCP00`, `C1NGCCPCH`, `C1NGGCP00`, `C1NGGCPCH`, `C1OIRFP00` from 2025 onwards, by reducing the capacity by 30% each year till 2030 and then going to zero.
- Remove completely TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00`.
- Increase CapitalCost for `C1BMCHP00`, `C1BMIGPCS`, `C1COSCP00`, `C1COSCPCS`, `C1NGCCP00`, `C1NGCCPCS` by 1000 compared to non-CCS alternatives.
- Increase CapitalCost for `C1ENDA1CS` by 500.
- Mistake found in unit conversion for InputActivityRatio of energy for `ALURECYCLE` - values need to be divided by 1000.
- **Issue found with FixedCost for `STEHGPLANT`, as thye are way higher than for `STEPLANT` (might be because in the HYBRIT project the hydrogen production is part of the steel making process, while in GLUCOSE it is modelled as separate technology) - removing FixedCost for `STEHGPLANT` to see how the model reacts.**

Effects: (finally!) also STEHGPLANT is now coming into the system from 2031, albeit not massively. As a result, also the DAC technology comes in later - only from 2036 onwards. 

# To Try
- Check costs and Input/Output units for ALURCPLANT vs ALUPLANT, and STEHGPLANT vs STEPLANT?
- Remove further the ResidualCapacity for industries?
- Increase further costs for DAC technology [tech: C1ENDA1CS]?