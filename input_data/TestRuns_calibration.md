# Model Calibration, August 2024
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

## GLUCOSE_noDA2CS_9
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
- Issue found with FixedCost for `STEHGPLANT`, as thye are way higher than for `STEPLANT` (might be because in the HYBRIT project the hydrogen production is part of the steel making process, while in GLUCOSE it is modelled as separate technology) - removing FixedCost for `STEHGPLANT` to see how the model reacts.
- **Implementing backstop CapitalCosts for `C1ENDA1CS` - to test if alternative low-carbon technologies come more strongly into the system.**

Effects: strong increase of nuclear power in the system, descrease in use of DAC (which comes in only in 2046, to a max of 10 GtCO2EQ) and slower penetration of CCS technologies. Also noticeable, the forest land seems to be increased in some critical years e.g. 2022-2023. Strangely, STEHGPLANT is not used, as well as other industry technologies.

## GLUCOSE_noDA2CS_10
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
- Issue found with FixedCost for `STEHGPLANT`, as thye are way higher than for `STEPLANT` (might be because in the HYBRIT project the hydrogen production is part of the steel making process, while in GLUCOSE it is modelled as separate technology) - removing FixedCost for `STEHGPLANT` to see how the model reacts.
- Implementing backstop CapitalCosts of 99999 for `C1ENDA1CS` - to test if alternative low-carbon technologies come more strongly into the system.
- **Reintroduce TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00`, to calibrate historical data.**

Effects: DAC coming in from 2035 onwards, again. STEHGPLANT coming in more massively from 2043 onwards. CO2EQ emission trajectory looks quite *bumpy*. 

## GLUCOSE_noDA2CS_11
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
- Issue found with FixedCost for `STEHGPLANT`, as thye are way higher than for `STEPLANT` (might be because in the HYBRIT project the hydrogen production is part of the steel making process, while in GLUCOSE it is modelled as separate technology) - removing FixedCost for `STEHGPLANT` to see how the model reacts.
- Implementing backstop CapitalCosts of 99999 for `C1ENDA1CS` - to test if alternative low-carbon technologies come more strongly into the system.
- Reintroduce TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00`, to calibrate historical data.
- **Implementing historical capacities for renewable as TotalAnnualMinCapacity, years 2014-2021.**
    - **Source: [IRENA, 2024. Renewable Energy Statistics 2024](https://www.irena.org/Publications/2024/Jul/Renewable-energy-statistics-2024)**
- **Adjusting TotalAnnualMaxCapacity and TotalAnnualMaxCapacityInvestment as to avoid conflicts with the new constraint.**

Effects: it is noticeable that the TotalAnnualMinCapacity constraint comes in only in 2014, hence the first 4 years of the modelling period are a bit *bumpy*; in addition, there is a strong change in primary energy mix in the switch between 2020 and 2021.

## GLUCOSE_noDA2CS_12
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
- Issue found with FixedCost for `STEHGPLANT`, as thye are way higher than for `STEPLANT` (might be because in the HYBRIT project the hydrogen production is part of the steel making process, while in GLUCOSE it is modelled as separate technology) - removing FixedCost for `STEHGPLANT` to see how the model reacts.
- Implementing backstop CapitalCosts of 99999 for `C1ENDA1CS` - to test if alternative low-carbon technologies come more strongly into the system.
- Reintroduce TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00`, to calibrate historical data.
- Implementing historical capacities for renewable as TotalAnnualMinCapacity, years 2014-2021.
    - Source: [IRENA, 2024. Renewable Energy Statistics 2024](https://www.irena.org/Publications/2024/Jul/Renewable-energy-statistics-2024)
- Adjusting TotalAnnualMaxCapacity and TotalAnnualMaxCapacityInvestment as to avoid conflicts with the new constraint.
- **Reintroducing TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00` years 2010-2021, plus reducing the TotalTechnologyAnnualActivityLowerLimit by 20% each year between 2022-2035.**

Effects: sudden shift in energy mix is distributing over 2020-2025, but there are still issues with e.g. NG penetration till 2025.

## GLUCOSE_noDA2CS_13
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
- Issue found with FixedCost for `STEHGPLANT`, as thye are way higher than for `STEPLANT` (might be because in the HYBRIT project the hydrogen production is part of the steel making process, while in GLUCOSE it is modelled as separate technology) - removing FixedCost for `STEHGPLANT` to see how the model reacts.
- Implementing backstop CapitalCosts of 99999 for `C1ENDA1CS` - to test if alternative low-carbon technologies come more strongly into the system.
- Reintroduce TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00`, to calibrate historical data.
- Implementing historical capacities for renewable as TotalAnnualMinCapacity, years 2014-2021.
    - Source: [IRENA, 2024. Renewable Energy Statistics 2024](https://www.irena.org/Publications/2024/Jul/Renewable-energy-statistics-2024)
- Adjusting TotalAnnualMaxCapacity and TotalAnnualMaxCapacityInvestment as to avoid conflicts with the new constraint.
- Reintroducing TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00` years 2010-2021, plus reducing the TotalTechnologyAnnualActivityLowerLimit by 20% each year between 2022-2035.
- **Implementing historical capacities for natural gas between 2015-2021: updating TotalTechnologyAnnualActivityLowerLimit for `C1NG00I00` between 2010-2035.**
    - **Source: [Our World In Data, 2024. Gas consumption by region](https://ourworldindata.org/grapher/natural-gas-consumption-by-region#sources-and-processing)**

Effects: now natural gas in primary energy looks much better (!!) but installed capacity is still low. Also, coal is again in the system till 2050.

## GLUCOSE_noDA2CS_14
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
- Issue found with FixedCost for `STEHGPLANT`, as thye are way higher than for `STEPLANT` (might be because in the HYBRIT project the hydrogen production is part of the steel making process, while in GLUCOSE it is modelled as separate technology) - removing FixedCost for `STEHGPLANT` to see how the model reacts.
- Implementing backstop CapitalCosts of 99999 for `C1ENDA1CS` - to test if alternative low-carbon technologies come more strongly into the system.
- Reintroduce TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00`, to calibrate historical data.
- Implementing historical capacities for renewable as TotalAnnualMinCapacity, years 2014-2021.
    - Source: [IRENA, 2024. Renewable Energy Statistics 2024.](https://www.irena.org/Publications/2024/Jul/Renewable-energy-statistics-2024)
- Adjusting TotalAnnualMaxCapacity and TotalAnnualMaxCapacityInvestment as to avoid conflicts with the new constraint.
- Reintroducing TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00` years 2010-2021, plus reducing the TotalTechnologyAnnualActivityLowerLimit by 20% each year between 2022-2035.
- Implementing historical capacities for natural gas between 2015-2021: updating TotalTechnologyAnnualActivityLowerLimit for `C1NG00I00` between 2010-2035.
    - Source: [Our World In Data, 2024. Gas consumption by region.](https://ourworldindata.org/grapher/natural-gas-consumption-by-region#sources-and-processing)
- **Reducing the TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00` by 30% each year between 2022-2030, then removing it from 2030-2050.**
- **Adding TotalAnnualMaxCapacity for `C1NULWP00` for years 2011-2021 based on historical installed capacity data, to prevent the model from overinvesting in nuclear in the historical period; removing TotalAnnualMaxCapacityInvestment for `C1NULWP00` for years 2010-2021 to avoid overconstraining the model.**
    - **Source: [EMBER, 2024. Yearly electricity data.](https://ember-climate.org/data-catalogue/yearly-electricity-data/)**
- **Remove AnnualEmissionLimit for CO2EQ, to relax emissions constraint in years 2010-2021.**

Effects: Infeasible. It seems the model has some big issues to handle years 2015-2020. 

## GLUCOSE_noDA2CS_15
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
- Issue found with FixedCost for `STEHGPLANT`, as thye are way higher than for `STEPLANT` (might be because in the HYBRIT project the hydrogen production is part of the steel making process, while in GLUCOSE it is modelled as separate technology) - removing FixedCost for `STEHGPLANT` to see how the model reacts.
- Implementing backstop CapitalCosts of 99999 for `C1ENDA1CS` - to test if alternative low-carbon technologies come more strongly into the system.
- Reintroduce TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00`, to calibrate historical data.
- Implementing historical capacities for renewable as TotalAnnualMinCapacity, years 2014-2021.
    - Source: [IRENA, 2024. Renewable Energy Statistics 2024.](https://www.irena.org/Publications/2024/Jul/Renewable-energy-statistics-2024)
- Adjusting TotalAnnualMaxCapacity and TotalAnnualMaxCapacityInvestment as to avoid conflicts with the new constraint.
- Reintroducing TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00` years 2010-2021, plus reducing the TotalTechnologyAnnualActivityLowerLimit by 20% each year between 2022-2035.
- Implementing historical capacities for natural gas between 2015-2021: updating TotalTechnologyAnnualActivityLowerLimit for `C1NG00I00` between 2010-2035.
    - Source: [Our World In Data, 2024. Gas consumption by region.](https://ourworldindata.org/grapher/natural-gas-consumption-by-region#sources-and-processing)
- Reducing the TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00` by 30% each year between 2022-2030, then removing it from 2030-2050.
- Adding TotalAnnualMaxCapacity for `C1NULWP00` for years 2011-2021 based on historical installed capacity data, to prevent the model from overinvesting in nuclear in the historical period; removing TotalAnnualMaxCapacityInvestment for `C1NULWP00` for years 2010-2021 to avoid overconstraining the model.
    - Source: [EMBER, 2024. Yearly electricity data.](https://ember-climate.org/data-catalogue/yearly-electricity-data/)
- Remove AnnualEmissionLimit for CO2EQ, to relax emissions constraint in years 2010-2021.
- **Increase TotalAnnualMaxCapacityInvestment between 2010-2021 from 0.1 to 0.15, for techs: `C1COCHP00`, `C1COSCP00`, `C1NGCCP00`, `C1NGCCPCH`, `C1NGGCP00`, `C1NGGCPCH`.**

Effects: Infeasible. It seems the model has some big issues to handle years 2015-2020. 

## GLUCOSE_noDA2CS_16
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
- Issue found with FixedCost for `STEHGPLANT`, as thye are way higher than for `STEPLANT` (might be because in the HYBRIT project the hydrogen production is part of the steel making process, while in GLUCOSE it is modelled as separate technology) - removing FixedCost for `STEHGPLANT` to see how the model reacts.
- Implementing backstop CapitalCosts of 99999 for `C1ENDA1CS` - to test if alternative low-carbon technologies come more strongly into the system.
- Reintroduce TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00`, to calibrate historical data.
- Implementing historical capacities for renewable as TotalAnnualMinCapacity, years 2014-2021.
    - Source: [IRENA, 2024. Renewable Energy Statistics 2024.](https://www.irena.org/Publications/2024/Jul/Renewable-energy-statistics-2024)
- Adjusting TotalAnnualMaxCapacity and TotalAnnualMaxCapacityInvestment as to avoid conflicts with the new constraint.
- Reintroducing TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00` years 2010-2021, plus reducing the TotalTechnologyAnnualActivityLowerLimit by 20% each year between 2022-2035.
- Implementing historical capacities for natural gas between 2015-2021: updating TotalTechnologyAnnualActivityLowerLimit for `C1NG00I00` between 2010-2035.
    - Source: [Our World In Data, 2024. Gas consumption by region.](https://ourworldindata.org/grapher/natural-gas-consumption-by-region#sources-and-processing)
- Reducing the TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00` by 30% each year between 2022-2030, then removing it from 2030-2050.
- Adding TotalAnnualMaxCapacity for `C1NULWP00` for years 2011-2021 based on historical installed capacity data, to prevent the model from overinvesting in nuclear in the historical period; removing TotalAnnualMaxCapacityInvestment for `C1NULWP00` for years 2010-2021 to avoid overconstraining the model.
    - Source: [EMBER, 2024. Yearly electricity data.](https://ember-climate.org/data-catalogue/yearly-electricity-data/)
- Remove AnnualEmissionLimit for CO2EQ, to relax emissions constraint in years 2010-2021.
- Increase TotalAnnualMaxCapacityInvestment between 2010-2021 from 0.1 to 0.15, for techs: `C1COCHP00`, `C1COSCP00`, `C1NGCCP00`, `C1NGCCPCH`, `C1NGGCP00`, `C1NGGCPCH`.
- **Increase ModelPeriodEmissionLimit based on higher historical emissions between 2010-2020 - I do not consider lower emissions, due to GLUCOSE not fully representing the energy demand globally.**

Effects: the model is solving, but fossil fuels are still low in years 2010-2020, compared to historical data.

## GLUCOSE_noDA2CS_17
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
- Issue found with FixedCost for `STEHGPLANT`, as thye are way higher than for `STEPLANT` (might be because in the HYBRIT project the hydrogen production is part of the steel making process, while in GLUCOSE it is modelled as separate technology) - removing FixedCost for `STEHGPLANT` to see how the model reacts.
- Implementing backstop CapitalCosts of 99999 for `C1ENDA1CS` - to test if alternative low-carbon technologies come more strongly into the system.
- Reintroduce TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00`, to calibrate historical data.
- Implementing historical capacities for renewable as TotalAnnualMinCapacity, years 2014-2021.
    - Source: [IRENA, 2024. Renewable Energy Statistics 2024.](https://www.irena.org/Publications/2024/Jul/Renewable-energy-statistics-2024)
- Adjusting TotalAnnualMaxCapacity and TotalAnnualMaxCapacityInvestment as to avoid conflicts with the new constraint.
- Reintroducing TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00` years 2010-2021, plus reducing the TotalTechnologyAnnualActivityLowerLimit by 20% each year between 2022-2035.
- Implementing historical capacities for natural gas between 2015-2021: updating TotalTechnologyAnnualActivityLowerLimit for `C1NG00I00` between 2010-2035.
    - Source: [Our World In Data, 2024. Gas consumption by region.](https://ourworldindata.org/grapher/natural-gas-consumption-by-region#sources-and-processing)
- Reducing the TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00` by 30% each year between 2022-2030, then removing it from 2030-2050.
- Adding TotalAnnualMaxCapacity for `C1NULWP00` for years 2011-2021 based on historical installed capacity data, to prevent the model from overinvesting in nuclear in the historical period; removing TotalAnnualMaxCapacityInvestment for `C1NULWP00` for years 2010-2021 to avoid overconstraining the model.
    - Source: [EMBER, 2024. Yearly electricity data.](https://ember-climate.org/data-catalogue/yearly-electricity-data/)
- Remove AnnualEmissionLimit for CO2EQ, to relax emissions constraint in years 2010-2021.
- Increase TotalAnnualMaxCapacityInvestment between 2010-2021 from 0.1 to 0.15, for techs: `C1COCHP00`, `C1COSCP00`, `C1NGCCP00`, `C1NGCCPCH`, `C1NGGCP00`, `C1NGGCPCH`.
- Increase ModelPeriodEmissionLimit based on higher historical emissions between 2010-2020 - I do not consider lower emissions, due to GLUCOSE not fully representing the energy demand globally.
- **Increase TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00` for years 2010-2020, to force in more coal capacity.**

Effects: still not enough. 

## GLUCOSE_noDA2CS_18
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
- Issue found with FixedCost for `STEHGPLANT`, as thye are way higher than for `STEPLANT` (might be because in the HYBRIT project the hydrogen production is part of the steel making process, while in GLUCOSE it is modelled as separate technology) - removing FixedCost for `STEHGPLANT` to see how the model reacts.
- Implementing backstop CapitalCosts of 99999 for `C1ENDA1CS` - to test if alternative low-carbon technologies come more strongly into the system.
- Reintroduce TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00`, to calibrate historical data.
- Implementing historical capacities for renewable as TotalAnnualMinCapacity, years 2014-2021.
    - Source: [IRENA, 2024. Renewable Energy Statistics 2024.](https://www.irena.org/Publications/2024/Jul/Renewable-energy-statistics-2024)
- Adjusting TotalAnnualMaxCapacity and TotalAnnualMaxCapacityInvestment as to avoid conflicts with the new constraint.
- Reintroducing TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00` years 2010-2021, plus reducing the TotalTechnologyAnnualActivityLowerLimit by 20% each year between 2022-2035.
- Implementing historical capacities for natural gas between 2015-2021: updating TotalTechnologyAnnualActivityLowerLimit for `C1NG00I00` between 2010-2035.
    - Source: [Our World In Data, 2024. Gas consumption by region.](https://ourworldindata.org/grapher/natural-gas-consumption-by-region#sources-and-processing)
- Reducing the TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00` by 30% each year between 2022-2030, then removing it from 2030-2050.
- Adding TotalAnnualMaxCapacity for `C1NULWP00` for years 2011-2021 based on historical installed capacity data, to prevent the model from overinvesting in nuclear in the historical period; removing TotalAnnualMaxCapacityInvestment for `C1NULWP00` for years 2010-2021 to avoid overconstraining the model.
    - Source: [EMBER, 2024. Yearly electricity data.](https://ember-climate.org/data-catalogue/yearly-electricity-data/)
- Remove AnnualEmissionLimit for CO2EQ, to relax emissions constraint in years 2010-2021.
- Increase TotalAnnualMaxCapacityInvestment between 2010-2021 from 0.1 to 0.15, for techs: `C1COCHP00`, `C1COSCP00`, `C1NGCCP00`, `C1NGCCPCH`, `C1NGGCP00`, `C1NGGCPCH`.
- Increase ModelPeriodEmissionLimit based on higher historical emissions between 2010-2020 - I do not consider lower emissions, due to GLUCOSE not fully representing the energy demand globally.
- Increase TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00` for years 2010-2020, to force in more coal capacity.
- **Increase ResidualCapacity for coal, NG, oil, Nuclear technologies between 2010-2020, to force in more fossil fuels as per historical data.**

Effects: 

## GLUCOSE_noDA2CS_14_1
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
- Issue found with FixedCost for `STEHGPLANT`, as thye are way higher than for `STEPLANT` (might be because in the HYBRIT project the hydrogen production is part of the steel making process, while in GLUCOSE it is modelled as separate technology) - removing FixedCost for `STEHGPLANT` to see how the model reacts.
- Implementing backstop CapitalCosts of 99999 for `C1ENDA1CS` - to test if alternative low-carbon technologies come more strongly into the system.
- Reintroduce TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00`, to calibrate historical data.
- Implementing historical capacities for renewable as TotalAnnualMinCapacity, years 2014-2021.
    - Source: [IRENA, 2024. Renewable Energy Statistics 2024.](https://www.irena.org/Publications/2024/Jul/Renewable-energy-statistics-2024)
- Adjusting TotalAnnualMaxCapacity and TotalAnnualMaxCapacityInvestment as to avoid conflicts with the new constraint.
- Reintroducing TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00` years 2010-2021, plus reducing the TotalTechnologyAnnualActivityLowerLimit by 20% each year between 2022-2035.
- Implementing historical capacities for natural gas between 2015-2021: updating TotalTechnologyAnnualActivityLowerLimit for `C1NG00I00` between 2010-2035.
    - Source: [Our World In Data, 2024. Gas consumption by region.](https://ourworldindata.org/grapher/natural-gas-consumption-by-region#sources-and-processing)
- Reducing the TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00` by 30% each year between 2022-2030, then removing it from 2030-2050.
- Adding TotalAnnualMaxCapacity for `C1NULWP00` for years 2011-2021 based on historical installed capacity data, to prevent the model from overinvesting in nuclear in the historical period; removing TotalAnnualMaxCapacityInvestment for `C1NULWP00` for years 2010-2021 to avoid overconstraining the model.
    - Source: [EMBER, 2024. Yearly electricity data.](https://ember-climate.org/data-catalogue/yearly-electricity-data/)
- Remove AnnualEmissionLimit for CO2EQ, to relax emissions constraint in years 2010-2021.
- **Increase ModelPeriodEmissionLimit based on higher historical emissions between 2010-2020 - I do consider 20% lower emissions, due to GLUCOSE not fully representing all the sector demands globally.**

Effects: 

## GLUCOSE_noDA2CS_14_2
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
- Issue found with FixedCost for `STEHGPLANT`, as thye are way higher than for `STEPLANT` (might be because in the HYBRIT project the hydrogen production is part of the steel making process, while in GLUCOSE it is modelled as separate technology) - removing FixedCost for `STEHGPLANT` to see how the model reacts.
- Implementing backstop CapitalCosts of 99999 for `C1ENDA1CS` - to test if alternative low-carbon technologies come more strongly into the system.
- Reintroduce TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00`, to calibrate historical data.
- Implementing historical capacities for renewable as TotalAnnualMinCapacity, years 2014-2021.
    - Source: [IRENA, 2024. Renewable Energy Statistics 2024.](https://www.irena.org/Publications/2024/Jul/Renewable-energy-statistics-2024)
- Adjusting TotalAnnualMaxCapacity and TotalAnnualMaxCapacityInvestment as to avoid conflicts with the new constraint.
- Reintroducing TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00` years 2010-2021, plus reducing the TotalTechnologyAnnualActivityLowerLimit by 20% each year between 2022-2035.
- Implementing historical capacities for natural gas between 2015-2021: updating TotalTechnologyAnnualActivityLowerLimit for `C1NG00I00` between 2010-2035.
    - Source: [Our World In Data, 2024. Gas consumption by region.](https://ourworldindata.org/grapher/natural-gas-consumption-by-region#sources-and-processing)
- Reducing the TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00` by 30% each year between 2022-2030, then removing it from 2030-2050.
- Adding TotalAnnualMaxCapacity for `C1NULWP00` for years 2011-2021 based on historical installed capacity data, to prevent the model from overinvesting in nuclear in the historical period; removing TotalAnnualMaxCapacityInvestment for `C1NULWP00` for years 2010-2021 to avoid overconstraining the model.
    - Source: [EMBER, 2024. Yearly electricity data.](https://ember-climate.org/data-catalogue/yearly-electricity-data/)
- Remove AnnualEmissionLimit for CO2EQ, to relax emissions constraint in years 2010-2021.
- Increase ModelPeriodEmissionLimit based on higher historical emissions between 2010-2020 - I do consider 20% lower emissions, due to GLUCOSE not fully representing all the sector demands globally.
- **For Aviation (C1LFAVF00) remove TotalTechnolgyAnnualActivitUpperLimit and implement the same values of the TotalTechnolgyAnnualActivitUpperLimit (minus 5%) as TotalTechnolgyAnnualActivitLowerLimit, to ensure that in the production of the final C1_F_MOT fuel it is correctly represented the share of maritime and aviation demand.**

Effects:

## GLUCOSE_noDA2CS_14_3
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
- Issue found with FixedCost for `STEHGPLANT`, as thye are way higher than for `STEPLANT` (might be because in the HYBRIT project the hydrogen production is part of the steel making process, while in GLUCOSE it is modelled as separate technology) - removing FixedCost for `STEHGPLANT` to see how the model reacts.
- Implementing backstop CapitalCosts of 99999 for `C1ENDA1CS` - to test if alternative low-carbon technologies come more strongly into the system.
- Reintroduce TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00`, to calibrate historical data.
- Implementing historical capacities for renewable as TotalAnnualMinCapacity, years 2014-2021.
    - Source: [IRENA, 2024. Renewable Energy Statistics 2024.](https://www.irena.org/Publications/2024/Jul/Renewable-energy-statistics-2024)
- Adjusting TotalAnnualMaxCapacity and TotalAnnualMaxCapacityInvestment as to avoid conflicts with the new constraint.
- Reintroducing TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00` years 2010-2021, plus reducing the TotalTechnologyAnnualActivityLowerLimit by 20% each year between 2022-2035.
- Implementing historical capacities for natural gas between 2015-2021: updating TotalTechnologyAnnualActivityLowerLimit for `C1NG00I00` between 2010-2035.
    - Source: [Our World In Data, 2024. Gas consumption by region.](https://ourworldindata.org/grapher/natural-gas-consumption-by-region#sources-and-processing)
- Reducing the TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00` by 30% each year between 2022-2030, then removing it from 2030-2050.
- Adding TotalAnnualMaxCapacity for `C1NULWP00` for years 2011-2021 based on historical installed capacity data, to prevent the model from overinvesting in nuclear in the historical period; removing TotalAnnualMaxCapacityInvestment for `C1NULWP00` for years 2010-2021 to avoid overconstraining the model.
    - Source: [EMBER, 2024. Yearly electricity data.](https://ember-climate.org/data-catalogue/yearly-electricity-data/)
- Remove AnnualEmissionLimit for CO2EQ, to relax emissions constraint in years 2010-2021.
- Increase ModelPeriodEmissionLimit based on higher historical emissions between 2010-2020 - I do consider 20% lower emissions, due to GLUCOSE not fully representing all the sector demands globally.
- For Aviation (C1LFAVF00) remove TotalTechnolgyAnnualActivitUpperLimit and implement the same values of the TotalTechnolgyAnnualActivitUpperLimit (minus 5%) as TotalTechnolgyAnnualActivitLowerLimit, to ensure that in the production of the final C1_F_MOT fuel it is correctly represented the share of maritime and aviation demand.
- **Implementing new InputActivityRatio for `C1LFAVF00, C1_P_LFO`, `C1LFRLF00, C1_P_LFO`, and `C1HFMRF00, C1_P_HFO`, backcalculated from historical data on total final energy consuption for transport.**
    - **Source: IEA (2024), "Extended world energy balances", IEA World Energy Statistics and Balances (database). <https://doi.org/10.1787/data-00513-en> (accessed on 04 September 2024)**

Effects: UseByTechnology for rail, maritime and aviation transport is now matching statistics for 2010, but gets off again later on. Also TPES and ElcCap in 2010 are not yet aligned.

## GLUCOSE_noDA2CS_14_4
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
- Issue found with FixedCost for `STEHGPLANT`, as thye are way higher than for `STEPLANT` (might be because in the HYBRIT project the hydrogen production is part of the steel making process, while in GLUCOSE it is modelled as separate technology) - removing FixedCost for `STEHGPLANT` to see how the model reacts.
- Implementing backstop CapitalCosts of 99999 for `C1ENDA1CS` - to test if alternative low-carbon technologies come more strongly into the system.
- Reintroduce TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00`, to calibrate historical data.
- Implementing historical capacities for renewable as TotalAnnualMinCapacity, years 2014-2021.
    - Source: [IRENA, 2024. Renewable Energy Statistics 2024.](https://www.irena.org/Publications/2024/Jul/Renewable-energy-statistics-2024)
- Adjusting TotalAnnualMaxCapacity and TotalAnnualMaxCapacityInvestment as to avoid conflicts with the new constraint.
- Reintroducing TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00` years 2010-2021, plus reducing the TotalTechnologyAnnualActivityLowerLimit by 20% each year between 2022-2035.
- Implementing historical capacities for natural gas between 2015-2021: updating TotalTechnologyAnnualActivityLowerLimit for `C1NG00I00` between 2010-2035.
    - Source: [Our World In Data, 2024. Gas consumption by region.](https://ourworldindata.org/grapher/natural-gas-consumption-by-region#sources-and-processing)
- Reducing the TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00` by 30% each year between 2022-2030, then removing it from 2030-2050.
- Adding TotalAnnualMaxCapacity for `C1NULWP00` for years 2011-2021 based on historical installed capacity data, to prevent the model from overinvesting in nuclear in the historical period; removing TotalAnnualMaxCapacityInvestment for `C1NULWP00` for years 2010-2021 to avoid overconstraining the model.
    - Source: [EMBER, 2024. Yearly electricity data.](https://ember-climate.org/data-catalogue/yearly-electricity-data/)
- Remove AnnualEmissionLimit for CO2EQ, to relax emissions constraint in years 2010-2021.
- Increase ModelPeriodEmissionLimit based on higher historical emissions between 2010-2020 - I do consider 20% lower emissions, due to GLUCOSE not fully representing all the sector demands globally.
- For Aviation (C1LFAVF00) remove TotalTechnolgyAnnualActivitUpperLimit and implement the same values of the TotalTechnolgyAnnualActivitUpperLimit (minus 5%) as TotalTechnolgyAnnualActivitLowerLimit, to ensure that in the production of the final C1_F_MOT fuel it is correctly represented the share of maritime and aviation demand.
- **Implementing new InputActivityRatio for `C1LFAVF00, C1_P_LFO`, `C1LFRLF00, C1_P_LFO`, `C1HFMRF00, C1_P_HFO`, `C1BFRLF00, C1_P_LFO`, and `C1LFRDF00, C1_P_LFO` between 2010-2020, backcalculated from historical data on total final energy consuption for transport; then slowing phasing in original InputActivityRatio between 2020-2025.**
    - **Source: IEA (2024), "Extended world energy balances", IEA World Energy Statistics and Balances (database). <https://doi.org/10.1787/data-00513-en> (accessed on 04 September 2024)**
- **Increasing ModelPeriodEmissionsLimit to 923.23 Gt  CO2EQ, to match historical data between 2010-2020. Cause I am now accounting for higher transport fuel demands.**

Effects: transport final energy consumption is now more in line with hostorical data, which drives up also fossil fuels TPES and a bit ElcCap.

## GLUCOSE_noDA2CS_14_5
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
- Issue found with FixedCost for `STEHGPLANT`, as thye are way higher than for `STEPLANT` (might be because in the HYBRIT project the hydrogen production is part of the steel making process, while in GLUCOSE it is modelled as separate technology) - removing FixedCost for `STEHGPLANT` to see how the model reacts.
- Implementing backstop CapitalCosts of 99999 for `C1ENDA1CS` - to test if alternative low-carbon technologies come more strongly into the system.
- Reintroduce TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00`, to calibrate historical data.
- Implementing historical capacities for renewable as TotalAnnualMinCapacity, years 2014-2021.
    - Source: [IRENA, 2024. Renewable Energy Statistics 2024.](https://www.irena.org/Publications/2024/Jul/Renewable-energy-statistics-2024)
- Adjusting TotalAnnualMaxCapacity and TotalAnnualMaxCapacityInvestment as to avoid conflicts with the new constraint.
- Reintroducing TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00` years 2010-2021, plus reducing the TotalTechnologyAnnualActivityLowerLimit by 20% each year between 2022-2035.
- Implementing historical capacities for natural gas between 2015-2021: updating TotalTechnologyAnnualActivityLowerLimit for `C1NG00I00` between 2010-2035.
    - Source: [Our World In Data, 2024. Gas consumption by region.](https://ourworldindata.org/grapher/natural-gas-consumption-by-region#sources-and-processing)
- Reducing the TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00` by 30% each year between 2022-2030, then removing it from 2030-2050.
- Adding TotalAnnualMaxCapacity for `C1NULWP00` for years 2011-2021 based on historical installed capacity data, to prevent the model from overinvesting in nuclear in the historical period; removing TotalAnnualMaxCapacityInvestment for `C1NULWP00` for years 2010-2021 to avoid overconstraining the model.
    - Source: [EMBER, 2024. Yearly electricity data.](https://ember-climate.org/data-catalogue/yearly-electricity-data/)
- Remove AnnualEmissionLimit for CO2EQ, to relax emissions constraint in years 2010-2021.
- Increase ModelPeriodEmissionLimit based on higher historical emissions between 2010-2020 - I do consider 20% lower emissions, due to GLUCOSE not fully representing all the sector demands globally.
- For Aviation (C1LFAVF00) remove TotalTechnolgyAnnualActivitUpperLimit and implement the same values of the TotalTechnolgyAnnualActivitUpperLimit (minus 5%) as TotalTechnolgyAnnualActivitLowerLimit, to ensure that in the production of the final C1_F_MOT fuel it is correctly represented the share of maritime and aviation demand.
- Implementing new InputActivityRatio for `C1LFAVF00, C1_P_LFO`, `C1LFRLF00, C1_P_LFO`, `C1HFMRF00, C1_P_HFO`, `C1BFRLF00, C1_P_LFO`, and `C1LFRDF00, C1_P_LFO` between 2010-2020, backcalculated from historical data on total final energy consuption for transport; then slowing phasing in original InputActivityRatio between 2020-2025.
    - Source: IEA (2024), "Extended world energy balances", IEA World Energy Statistics and Balances (database). <https://doi.org/10.1787/data-00513-en> (accessed on 04 September 2024)
- Increasing ModelPeriodEmissionsLimit to 923.23 Gt  CO2EQ, to match historical data between 2010-2020. Cause I am now accounting for higher transport fuel demands.
- **Remove all the TotalAnnualMinCapacity for Renewables, move them to ResidualCapacity and lower them by 10% betwee 2014-2021. Then lower ResidiualCapacity by 25% per year till 2025, then go to zero. Data as from IRENA historical data.**
- **Lower TotalTechnologyAnnualActivityLowerLimit by 10% each year for primary fossil fuels imports between 2010-2030.**

Effects: still struggling to see impact on results and correct dynamics in TPES and ElcCap.

## GLUCOSE_noDA2CS_14_6
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
- Issue found with FixedCost for `STEHGPLANT`, as thye are way higher than for `STEPLANT` (might be because in the HYBRIT project the hydrogen production is part of the steel making process, while in GLUCOSE it is modelled as separate technology) - removing FixedCost for `STEHGPLANT` to see how the model reacts.
- Implementing backstop CapitalCosts of 99999 for `C1ENDA1CS` - to test if alternative low-carbon technologies come more strongly into the system.
- Reintroduce TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00`, to calibrate historical data.
- Implementing historical capacities for renewable as TotalAnnualMinCapacity, years 2014-2021.
    - Source: [IRENA, 2024. Renewable Energy Statistics 2024.](https://www.irena.org/Publications/2024/Jul/Renewable-energy-statistics-2024)
- Adjusting TotalAnnualMaxCapacity and TotalAnnualMaxCapacityInvestment as to avoid conflicts with the new constraint.
- Reintroducing TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00` years 2010-2021, plus reducing the TotalTechnologyAnnualActivityLowerLimit by 20% each year between 2022-2035.
- Implementing historical capacities for natural gas between 2015-2021: updating TotalTechnologyAnnualActivityLowerLimit for `C1NG00I00` between 2010-2035.
    - Source: [Our World In Data, 2024. Gas consumption by region.](https://ourworldindata.org/grapher/natural-gas-consumption-by-region#sources-and-processing)
- Reducing the TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00` by 30% each year between 2022-2030, then removing it from 2030-2050.
- Adding TotalAnnualMaxCapacity for `C1NULWP00` for years 2011-2021 based on historical installed capacity data, to prevent the model from overinvesting in nuclear in the historical period; removing TotalAnnualMaxCapacityInvestment for `C1NULWP00` for years 2010-2021 to avoid overconstraining the model.
    - Source: [EMBER, 2024. Yearly electricity data.](https://ember-climate.org/data-catalogue/yearly-electricity-data/)
- Remove AnnualEmissionLimit for CO2EQ, to relax emissions constraint in years 2010-2021.
- Increase ModelPeriodEmissionLimit based on higher historical emissions between 2010-2020 - I do consider 20% lower emissions, due to GLUCOSE not fully representing all the sector demands globally.
- For Aviation (C1LFAVF00) remove TotalTechnolgyAnnualActivitUpperLimit and implement the same values of the TotalTechnolgyAnnualActivitUpperLimit (minus 5%) as TotalTechnolgyAnnualActivitLowerLimit, to ensure that in the production of the final C1_F_MOT fuel it is correctly represented the share of maritime and aviation demand.
- Implementing new InputActivityRatio for `C1LFAVF00, C1_P_LFO`, `C1LFRLF00, C1_P_LFO`, `C1HFMRF00, C1_P_HFO`, `C1BFRLF00, C1_P_LFO`, and `C1LFRDF00, C1_P_LFO` between 2010-2020, backcalculated from historical data on total final energy consuption for transport; then slowing phasing in original InputActivityRatio between 2020-2025.
    - Source: IEA (2024), "Extended world energy balances", IEA World Energy Statistics and Balances (database). <https://doi.org/10.1787/data-00513-en> (accessed on 04 September 2024)
- Increasing ModelPeriodEmissionsLimit to 923.23 Gt  CO2EQ, to match historical data between 2010-2020. Cause I am now accounting for higher transport fuel demands.
- Remove all the TotalAnnualMinCapacity for Renewables, move them to ResidualCapacity and lower them by 10% betwee 2014-2021. Then lower ResidiualCapacity by 25% per year till 2025, then go to zero. Data as from IRENA historical data.
- Lower TotalTechnologyAnnualActivityLowerLimit by 10% each year for primary fossil fuels imports between 2010-2030.
- **Remove TotalTechnologyAnnualActivityLowerLimit for primary fossil fuels imports.**

Effects: TPES and ElcCap are not crazy off for fossil fuels, but Geothermal heat production takes over coal. Need to limit geothermal capacity/activity.

## GLUCOSE_noDA2CS_14_7
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
- Issue found with FixedCost for `STEHGPLANT`, as thye are way higher than for `STEPLANT` (might be because in the HYBRIT project the hydrogen production is part of the steel making process, while in GLUCOSE it is modelled as separate technology) - removing FixedCost for `STEHGPLANT` to see how the model reacts.
- Implementing backstop CapitalCosts of 99999 for `C1ENDA1CS` - to test if alternative low-carbon technologies come more strongly into the system.
- Reintroduce TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00`, to calibrate historical data.
- Implementing historical capacities for renewable as TotalAnnualMinCapacity, years 2014-2021.
    - Source: [IRENA, 2024. Renewable Energy Statistics 2024.](https://www.irena.org/Publications/2024/Jul/Renewable-energy-statistics-2024)
- Adjusting TotalAnnualMaxCapacity and TotalAnnualMaxCapacityInvestment as to avoid conflicts with the new constraint.
- Reintroducing TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00` years 2010-2021, plus reducing the TotalTechnologyAnnualActivityLowerLimit by 20% each year between 2022-2035.
- Implementing historical capacities for natural gas between 2015-2021: updating TotalTechnologyAnnualActivityLowerLimit for `C1NG00I00` between 2010-2035.
    - Source: [Our World In Data, 2024. Gas consumption by region.](https://ourworldindata.org/grapher/natural-gas-consumption-by-region#sources-and-processing)
- Reducing the TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00` by 30% each year between 2022-2030, then removing it from 2030-2050.
- Adding TotalAnnualMaxCapacity for `C1NULWP00` for years 2011-2021 based on historical installed capacity data, to prevent the model from overinvesting in nuclear in the historical period; removing TotalAnnualMaxCapacityInvestment for `C1NULWP00` for years 2010-2021 to avoid overconstraining the model.
    - Source: [EMBER, 2024. Yearly electricity data.](https://ember-climate.org/data-catalogue/yearly-electricity-data/)
- Remove AnnualEmissionLimit for CO2EQ, to relax emissions constraint in years 2010-2021.
- Increase ModelPeriodEmissionLimit based on higher historical emissions between 2010-2020 - I do consider 20% lower emissions, due to GLUCOSE not fully representing all the sector demands globally.
- For Aviation (C1LFAVF00) remove TotalTechnolgyAnnualActivitUpperLimit and implement the same values of the TotalTechnolgyAnnualActivitUpperLimit (minus 5%) as TotalTechnolgyAnnualActivitLowerLimit, to ensure that in the production of the final C1_F_MOT fuel it is correctly represented the share of maritime and aviation demand.
- Implementing new InputActivityRatio for `C1LFAVF00, C1_P_LFO`, `C1LFRLF00, C1_P_LFO`, `C1HFMRF00, C1_P_HFO`, `C1BFRLF00, C1_P_LFO`, and `C1LFRDF00, C1_P_LFO` between 2010-2020, backcalculated from historical data on total final energy consuption for transport; then slowing phasing in original InputActivityRatio between 2020-2025.
    - Source: IEA (2024), "Extended world energy balances", IEA World Energy Statistics and Balances (database). <https://doi.org/10.1787/data-00513-en> (accessed on 04 September 2024)
- Increasing ModelPeriodEmissionsLimit to 923.23 Gt  CO2EQ, to match historical data between 2010-2020. Cause I am now accounting for higher transport fuel demands.
- Remove all the TotalAnnualMinCapacity for Renewables, move them to ResidualCapacity and lower them by 10% betwee 2014-2021. Then lower ResidiualCapacity by 25% per year till 2025, then go to zero. Data as from IRENA historical data.
- Lower TotalTechnologyAnnualActivityLowerLimit by 10% each year for primary fossil fuels imports between 2010-2030.
- Remove TotalTechnologyAnnualActivityLowerLimit for primary fossil fuels imports.
- **Introduce ResidualCapacity and TotalAnnualMaxCapacity for Geothermal elc (`C1GOCVP00`), and ResidualCapacity, TotalAnnualMaxCapacity, and TotalTechnology AnnualActivityUpperLimit for Geothermal heat (`C1GOHTF03`) to match IRENA historical installed capacity and IEA historical TPES between 2014-2021**. 

Effects: all looks better, but coal is off - ElcCap comes in but TPES goes to zero in 2015-2020.


## GLUCOSE_noDA2CS_14_8
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
- Issue found with FixedCost for `STEHGPLANT`, as thye are way higher than for `STEPLANT` (might be because in the HYBRIT project the hydrogen production is part of the steel making process, while in GLUCOSE it is modelled as separate technology) - removing FixedCost for `STEHGPLANT` to see how the model reacts.
- Implementing backstop CapitalCosts of 99999 for `C1ENDA1CS` - to test if alternative low-carbon technologies come more strongly into the system.
- Reintroduce TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00`, to calibrate historical data.
- Implementing historical capacities for renewable as TotalAnnualMinCapacity, years 2014-2021.
    - Source: [IRENA, 2024. Renewable Energy Statistics 2024.](https://www.irena.org/Publications/2024/Jul/Renewable-energy-statistics-2024)
- Adjusting TotalAnnualMaxCapacity and TotalAnnualMaxCapacityInvestment as to avoid conflicts with the new constraint.
- Reintroducing TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00` years 2010-2021, plus reducing the TotalTechnologyAnnualActivityLowerLimit by 20% each year between 2022-2035.
- Implementing historical capacities for natural gas between 2015-2021: updating TotalTechnologyAnnualActivityLowerLimit for `C1NG00I00` between 2010-2035.
    - Source: [Our World In Data, 2024. Gas consumption by region.](https://ourworldindata.org/grapher/natural-gas-consumption-by-region#sources-and-processing)
- Reducing the TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00` by 30% each year between 2022-2030, then removing it from 2030-2050.
- Adding TotalAnnualMaxCapacity for `C1NULWP00` for years 2011-2021 based on historical installed capacity data, to prevent the model from overinvesting in nuclear in the historical period; removing TotalAnnualMaxCapacityInvestment for `C1NULWP00` for years 2010-2021 to avoid overconstraining the model.
    - Source: [EMBER, 2024. Yearly electricity data.](https://ember-climate.org/data-catalogue/yearly-electricity-data/)
- Remove AnnualEmissionLimit for CO2EQ, to relax emissions constraint in years 2010-2021.
- Increase ModelPeriodEmissionLimit based on higher historical emissions between 2010-2020 - I do consider 20% lower emissions, due to GLUCOSE not fully representing all the sector demands globally.
- For Aviation (C1LFAVF00) remove TotalTechnolgyAnnualActivitUpperLimit and implement the same values of the TotalTechnolgyAnnualActivitUpperLimit (minus 5%) as TotalTechnolgyAnnualActivitLowerLimit, to ensure that in the production of the final C1_F_MOT fuel it is correctly represented the share of maritime and aviation demand.
- Implementing new InputActivityRatio for `C1LFAVF00, C1_P_LFO`, `C1LFRLF00, C1_P_LFO`, `C1HFMRF00, C1_P_HFO`, `C1BFRLF00, C1_P_LFO`, and `C1LFRDF00, C1_P_LFO` between 2010-2020, backcalculated from historical data on total final energy consuption for transport; then slowing phasing in original InputActivityRatio between 2020-2025.
    - Source: IEA (2024), "Extended world energy balances", IEA World Energy Statistics and Balances (database). <https://doi.org/10.1787/data-00513-en> (accessed on 04 September 2024)
- Increasing ModelPeriodEmissionsLimit to 923.23 Gt  CO2EQ, to match historical data between 2010-2020. Cause I am now accounting for higher transport fuel demands.
- Remove all the TotalAnnualMinCapacity for Renewables, move them to ResidualCapacity and lower them by 10% betwee 2014-2021. Then lower ResidiualCapacity by 25% per year till 2025, then go to zero. Data as from IRENA historical data.
- Lower TotalTechnologyAnnualActivityLowerLimit by 10% each year for primary fossil fuels imports between 2010-2030.
- Remove TotalTechnologyAnnualActivityLowerLimit for primary fossil fuels imports.
- Introduce ResidualCapacity and TotalAnnualMaxCapacity for Geothermal elc (`C1GOCVP00`), and ResidualCapacity, TotalAnnualMaxCapacity, and TotalTechnology AnnualActivityUpperLimit for Geothermal heat (`C1GOHTF03`) to match IRENA historical installed capacity and IEA historical TPES (minus 10%) between 2014-2021. 
- **Introduce TotalTechnology AnnualActivityUpperLimit for primary gas and oil import, to match IEA TPES (minus 10%) between 2010-2020.**
- **Adjust TotalMaxCapacity for hydro, to avoid over production of TPES from it in historical years (2010-2020).**

Effects: slightly better, but still too little coal and significant NG and oil. Also, too low TPES total.

## *GLUCOSE_noDA2CS_14_9*
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
- Issue found with FixedCost for `STEHGPLANT`, as thye are way higher than for `STEPLANT` (might be because in the HYBRIT project the hydrogen production is part of the steel making process, while in GLUCOSE it is modelled as separate technology) - removing FixedCost for `STEHGPLANT` to see how the model reacts.
- Implementing backstop CapitalCosts of 99999 for `C1ENDA1CS` - to test if alternative low-carbon technologies come more strongly into the system.
- Reintroduce TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00`, to calibrate historical data.
- Implementing historical capacities for renewable as TotalAnnualMinCapacity, years 2014-2021.
    - Source: [IRENA, 2024. Renewable Energy Statistics 2024.](https://www.irena.org/Publications/2024/Jul/Renewable-energy-statistics-2024)
- Adjusting TotalAnnualMaxCapacity and TotalAnnualMaxCapacityInvestment as to avoid conflicts with the new constraint.
- Reintroducing TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00` years 2010-2021, plus reducing the TotalTechnologyAnnualActivityLowerLimit by 20% each year between 2022-2035.
- Implementing historical capacities for natural gas between 2015-2021: updating TotalTechnologyAnnualActivityLowerLimit for `C1NG00I00` between 2010-2035.
    - Source: [Our World In Data, 2024. Gas consumption by region.](https://ourworldindata.org/grapher/natural-gas-consumption-by-region#sources-and-processing)
- Reducing the TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00` by 30% each year between 2022-2030, then removing it from 2030-2050.
- Adding TotalAnnualMaxCapacity for `C1NULWP00` for years 2011-2021 based on historical installed capacity data, to prevent the model from overinvesting in nuclear in the historical period; removing TotalAnnualMaxCapacityInvestment for `C1NULWP00` for years 2010-2021 to avoid overconstraining the model.
    - Source: [EMBER, 2024. Yearly electricity data.](https://ember-climate.org/data-catalogue/yearly-electricity-data/)
- Remove AnnualEmissionLimit for CO2EQ, to relax emissions constraint in years 2010-2021.
- Increase ModelPeriodEmissionLimit based on higher historical emissions between 2010-2020 - I do consider 20% lower emissions, due to GLUCOSE not fully representing all the sector demands globally.
- For Aviation (C1LFAVF00) remove TotalTechnolgyAnnualActivitUpperLimit and implement the same values of the TotalTechnolgyAnnualActivitUpperLimit (minus 5%) as TotalTechnolgyAnnualActivitLowerLimit, to ensure that in the production of the final C1_F_MOT fuel it is correctly represented the share of maritime and aviation demand.
- Implementing new InputActivityRatio for `C1LFAVF00, C1_P_LFO`, `C1LFRLF00, C1_P_LFO`, `C1HFMRF00, C1_P_HFO`, `C1BFRLF00, C1_P_LFO`, and `C1LFRDF00, C1_P_LFO` between 2010-2020, backcalculated from historical data on total final energy consuption for transport; then slowing phasing in original InputActivityRatio between 2020-2025.
    - Source: IEA (2024), "Extended world energy balances", IEA World Energy Statistics and Balances (database). <https://doi.org/10.1787/data-00513-en> (accessed on 04 September 2024)
- Increasing ModelPeriodEmissionsLimit to 923.23 Gt  CO2EQ, to match historical data between 2010-2020. Cause I am now accounting for higher transport fuel demands.
- Remove all the TotalAnnualMinCapacity for Renewables, move them to ResidualCapacity and lower them by 10% betwee 2014-2021. Then lower ResidiualCapacity by 25% per year till 2025, then go to zero. Data as from IRENA historical data.
- Lower TotalTechnologyAnnualActivityLowerLimit by 10% each year for primary fossil fuels imports between 2010-2030.
- Remove TotalTechnologyAnnualActivityLowerLimit for primary fossil fuels imports.
- Introduce ResidualCapacity and TotalAnnualMaxCapacity for Geothermal elc (`C1GOCVP00`), and ResidualCapacity, TotalAnnualMaxCapacity, and TotalTechnology AnnualActivityUpperLimit for Geothermal heat (`C1GOHTF03`) to match IRENA historical installed capacity and IEA historical TPES (minus 10%) between 2014-2021. 
- Introduce TotalTechnology AnnualActivityUpperLimit for primary gas and oil import, to match IEA TPES (minus 10%) between 2010-2020.
- Adjust TotalMaxCapacity for hydro, to avoid over production of TPES from it in historical years (2010-2020).
- **Adding back TotalTechnology AnnualActivityLowerLimit for primary coal, to to match IEA TPES (minus 15%) in years 2010-2020 with values reducing to zero in years 2021-2025.**

Effects: results look better, coal TPES is more in line with historical data. 
### *Final test: sent to Will for approval.*

## GLUCOSE_noDA2CS_14_10
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
- Issue found with FixedCost for `STEHGPLANT`, as thye are way higher than for `STEPLANT` (might be because in the HYBRIT project the hydrogen production is part of the steel making process, while in GLUCOSE it is modelled as separate technology) - removing FixedCost for `STEHGPLANT` to see how the model reacts.
- Implementing backstop CapitalCosts of 99999 for `C1ENDA1CS` - to test if alternative low-carbon technologies come more strongly into the system.
- Reintroduce TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00`, to calibrate historical data.
- Implementing historical capacities for renewable as TotalAnnualMinCapacity, years 2014-2021.
    - Source: [IRENA, 2024. Renewable Energy Statistics 2024.](https://www.irena.org/Publications/2024/Jul/Renewable-energy-statistics-2024)
- Adjusting TotalAnnualMaxCapacity and TotalAnnualMaxCapacityInvestment as to avoid conflicts with the new constraint.
- Reintroducing TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00` years 2010-2021, plus reducing the TotalTechnologyAnnualActivityLowerLimit by 20% each year between 2022-2035.
- Implementing historical capacities for natural gas between 2015-2021: updating TotalTechnologyAnnualActivityLowerLimit for `C1NG00I00` between 2010-2035.
    - Source: [Our World In Data, 2024. Gas consumption by region.](https://ourworldindata.org/grapher/natural-gas-consumption-by-region#sources-and-processing)
- Reducing the TotalTechnologyAnnualActivityLowerLimit for `C1CO00I00`, `C1NG00I00`, `C1OI00I00` by 30% each year between 2022-2030, then removing it from 2030-2050.
- Adding TotalAnnualMaxCapacity for `C1NULWP00` for years 2011-2021 based on historical installed capacity data, to prevent the model from overinvesting in nuclear in the historical period; removing TotalAnnualMaxCapacityInvestment for `C1NULWP00` for years 2010-2021 to avoid overconstraining the model.
    - Source: [EMBER, 2024. Yearly electricity data.](https://ember-climate.org/data-catalogue/yearly-electricity-data/)
- Remove AnnualEmissionLimit for CO2EQ, to relax emissions constraint in years 2010-2021.
- Increase ModelPeriodEmissionLimit based on higher historical emissions between 2010-2020 - I do consider 20% lower emissions, due to GLUCOSE not fully representing all the sector demands globally.
- For Aviation (C1LFAVF00) remove TotalTechnolgyAnnualActivitUpperLimit and implement the same values of the TotalTechnolgyAnnualActivitUpperLimit (minus 5%) as TotalTechnolgyAnnualActivitLowerLimit, to ensure that in the production of the final C1_F_MOT fuel it is correctly represented the share of maritime and aviation demand.
- Implementing new InputActivityRatio for `C1LFAVF00, C1_P_LFO`, `C1LFRLF00, C1_P_LFO`, `C1HFMRF00, C1_P_HFO`, `C1BFRLF00, C1_P_LFO`, and `C1LFRDF00, C1_P_LFO` between 2010-2020, backcalculated from historical data on total final energy consuption for transport; then slowing phasing in original InputActivityRatio between 2020-2025.
    - Source: IEA (2024), "Extended world energy balances", IEA World Energy Statistics and Balances (database). <https://doi.org/10.1787/data-00513-en> (accessed on 04 September 2024)
- Increasing ModelPeriodEmissionsLimit to 923.23 Gt  CO2EQ, to match historical data between 2010-2020. Cause I am now accounting for higher transport fuel demands.
- Remove all the TotalAnnualMinCapacity for Renewables, move them to ResidualCapacity and lower them by 10% betwee 2014-2021. Then lower ResidiualCapacity by 25% per year till 2025, then go to zero. Data as from IRENA historical data.
- Lower TotalTechnologyAnnualActivityLowerLimit by 10% each year for primary fossil fuels imports between 2010-2030.
- Remove TotalTechnologyAnnualActivityLowerLimit for primary fossil fuels imports.
- Introduce ResidualCapacity and TotalAnnualMaxCapacity for Geothermal elc (`C1GOCVP00`), and ResidualCapacity, TotalAnnualMaxCapacity, and TotalTechnologyAnnualActivityUpperLimit for Geothermal heat (`C1GOHTF03`) to match IRENA historical installed capacity and IEA historical TPES (minus 10%) between 2014-2021. 
- Introduce TotalTechnologyAnnualActivityUpperLimit for primary gas and oil import, to match IEA TPES (minus 10%) between 2010-2020.
- Adjust TotalMaxCapacity for hydro, to avoid over production of TPES from it in historical years (2010-2020).
- Adding back TotalTechnologyAnnualActivityLowerLimit for primary coal, to to match IEA TPES (minus 15%) in years 2010-2020 with values reducing to zero in years 2021-2025.
- **Adding lower constraints to fix the model historical period - so that the RDM run won't affect years 2010-2020.**
    - adding TotalTechnologyAnnualActivityLowerLimit for `C1NG00I00` and `C1OI00I00`
    - modifying ResidualCapacity and TotalAnnualMaxCapacity for hydro technologies - to avoid the model to over-invest on hydro
    - adding TotalAnnualMinCapacity for all renewables and for a selection of coal, oil, and gas power plant technologies (`C1COCHP00`, `C1COHTF03`, `C1COSCP00`, `C1HFGCP00`, `C1LFBRFH1`, `C1NGCCP00`, `C1NGGCP00`) - to push the model to use fossil fuels in the historical period.






-------
# To Try
- Check costs and Input/Output units for ALURCPLANT vs ALUPLANT, and STEHGPLANT vs STEPLANT?
- Remove further the ResidualCapacity for industries?
- Increase further costs for DAC technology [tech: C1ENDA1CS]?

## meeting with Will
- try to delay ccs and see how the model reacts
- try also with very high ccs costs?
- ccs behaviour - check if fuels are forced in
- check dual values for ccs techs and biomass resource
check constraints on biomass resources?


- add dual values for constraint on lower limit of activity
- try testing a very high cost for DAC (as for backstop) and check dual values then and see how it reacts
- recive investment max cap constraints for renewables
- work on historic trends - need to match results till 2022
- once historic data are in, check if the dual values shows constraints in remewable investments
- release constraints in heat pumps for residential


### NB
- for SD - relax as many constraint as possible, and then use constraints as uncertainty parameters
- explore wide range of scenarios - then constraint the solution space based on the data uncertainty that I have from the literature (learning curve, growth constraints)

- check what input fuel takes hydrogen production - check what the emission intensity is based on the input fuel to generate hydrogen