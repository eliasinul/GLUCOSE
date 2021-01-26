# GLUCOSE results visualization
Scripts for visualizing the results of the GLUCOSE model

## How to use them
...

## GLUCOSE Naming Convention

### Energy module - Technology names
| Region |       | Resource ID |           | Technology ID |              | Level ID |         | Attributes |                     |
|:------:|-------|:-----------:|-----------|:-------------:|--------------|:--------:|---------|:----------:|---------------------|
| C1     | World | BF          | Biofuel   | RD            | Road         | F        | Final   | 00         |                     |
|        |       | BM          | Biomass   | BR            | Boiler       | F        | Final   | H1         | Historical capacity, Small |
|        |       |             |           | BR            | Boiler       | F        | Final   | N1       | New capacity, Small   |
|        |       |             |           | CH            | Combined Heat | P       | Primary | 00       |                     |
|        |       |             |           | HT            | Heat         | F        | Final   | 03       | Large               | 
|        |       |             |           | IG            | Internal Gasification | P        | Primary | CS        | Carbon-capture and Storage |
|        |       |             |           | LP            | Liquid Biofuel Prod. | 0        |         | 00       |                     |
|        |       |             |           | SC            | Steam Cycle  | P        | Primary | 00       |                     |
|        |       | CO          | Coal      | 00            |              | I        | Import  | 00       |                     |
|        |       |             |           | BR            | Boiler       | F        | Final   | H1       | Historical capacity, Small |
|        |       |             |           | CH            | Combined Heat | P        | Primary | 00       |                    |
|        |       |             |           | HT            | Heat         | F        | Final   | 03       | Large               |
|        |       |             |           | IG            | Internal Gasification | P        | Primary | 00       |                     |
|        |       |             |           | LP            | Coal to Liquid prod. | 0        |         | 00       |                     |
|        |       |             |           | SC            | Steam Cycle  | P        | Primary | 00       |                     |
|        |       |             |           |               |              |          |         | CS       | Carbon-capture and Storage |
|        |       |             |           | SF            | Synfuel      | 0        |         | 00       |                     |
|        |       | EL          | Electricity | EF            | Electric Efficiency switch | F        | Final   | 00   |         |
|        |       |             |           | RD            | Road         | F        | Final   | 00       |                     |
|        |       |             |           | RL            | Road         | F        | Final   | 00       |                     |
|        |       | GO          | Geothermal | CV           | Conventional | P        | Primary | 00       |                     |
|        |       |             |           | HT            | Heat         | F        | Final   | 03       | Large               |
|        |       | HF          | Heavy Fuel Oil | GC       | Gas Turbine  | P        | Primary | 00       |                     |
|        |       |             |           |               |              | P        | Primary | CH       | Combined Heat and Power |
|        |       |             |           | MR            | Maritime     | F        | Fuel    | 00       |                     |
|        |       | HY          | Hydro     | DM            | Dam          | P        | Primary | 00       |                     |
|        |       |             |           | MI            | Mini         | P        | Primary | 00       |                     |
|        |       | LF          | Light Fuel Oil | AV       | Aviation     | F        | Final   | 00       |                     |
|        |       |             |           | BR            | Boiler       | F        | Final   | H1       | Historical capacity, Small |
|        |       |             |           |               |              |          | Final   | N1       | New capacity, Small |
|        |       |             |           | CC            | Combined Cycle | P        | Primary | 00     |                     |
|        |       |             |           | RD            | Road         | F        | Final   | 00       |                     |
|        |       |             |           | RF            | Rail         | F        | Final   | 00       |                     |
|        |       | NG        | Natural Gas | 00            |              | I        | Import  | 00       |                     |
|        |       |             |           | BR            | Boiler       | F        | Final   | H1       | Historical Capacity, Small |
|        |       |             |           |               |              |          |         | N1       | New Capacity, Small |
|        |       |             |           | CC            | Combined Cycle | P        | Primary | 00       |                     |
|        |       |             |           |               |              |          |         | CH       | Combined Heat and Power |
|        |       |             |           |               |              |          |         | CS       | Carbon-capture and Storage |
|        |       |             |           | GC            | Gas Turbine  | P        | Primary | 00       |                     | 
|        |       |             |           |               |              |          |         | CH       | Combined Heat and Power |
|        |       |             |           | HT            | Heat         | F        | Final   | 03       | Large |
|        |       |             |           | LP            | Gas to Liquid prod. | 0        |         | 00       |                     |
|        |       | NU          | Nuclear   | 00            |              | I        | Import  | 00       |                     |
|        |       |             |           | LW            | Light Water  | P        | Primary | 00       |                     |
|        |       | OC          | Ocean     | CV            | Conventional | P        | Primary | 00       |                     |
|        |       | OI          | Crude Oil | 00            |              | I        | Import  | 00       |                     |
|        |       |             |           | HT            | Heat         | F        | Final   | 03       | Large               |
|        |       |             |           | RF            | Refinery     | P        | Primary | 00       |                     |
|        |       | SO          | Solar     | C1            | Concentrated, solar thermal | P        | Primary |          |                     |
|        |       |             |           | TH            | Thermal      |          | F       | Final   | 00                  |
|        |       |             |           | V1            | Photovoltaic, rooftop | P        | Primary | 00       |                     |
|        |       |             |           | V2            | Photovoltaic, rooftop | P        | Primary | 00       |                     |
|        |       | WD          | Wind      | ON            | Onshore      | P        | Primary | 00       |                     |
|        |       |             |           | OF            | Offshore     | P        | Primary | 00       |                     |
|        |       |             |           |               |              |          |         |          |                     |

*Transmission and Distribution*
| Region |       | Resource ID |           | Technology ID |              | Function |         | Attributes |                     |
|:------:|-------|:-----------:|-----------|:-------------:|--------------|:--------:|---------|:----------:|---------------------|
| C1     | World | HT          | Heat      | OO            | Distribution | T        | Transmission | FI    | Final, Industry     |
|        |       |             |           |               |              |          |         | FR         | Final, Residential  |

### Energy module - Resource vector names
| Region |       | Resource Level |           | Resource ID |                      | Sector ID |             |
|:------:|-------|:--------------:|-----------|:-----------:|----------------------|:---------:|-------------|
| C1     | World | R              | Resource  | OIL         | Crude Oil            |           |             |
|        |       | P              | Primary   | BIOW        | Biomass for energy   |           |             |
|        |       |                |           | BIOW2       | Biomass for industry |           |             |
|        |       |                |           | GAS         | Natural Gas          |           |             |
|        |       |                |           | HCO         | Coal                 |           |             |
|        |       |                |           | HFO         | Heavy Fuel Oil       |           |             |
|        |       |                |           | LFO         | Light Fuel Oil       |           |             |
|        |       |                |           | NUC         | Nuclear              |           |             |
|        |       | S              | Secondary | BIOL        | Biofuel              |           |             |
|        |       |                |           | ELC         | Electricity          |           |             |
|        |       |                |           | HEAT        | Heat                 |           |             |
|        |       | F              | Final     | CLS         | Electricity          |           |             |
|        |       |                |           | HEA         | Heat                 | I         | Industry    |
|        |       |                |           |             |                      | R         | Residential |
|        |       |                |           | MOT         | Motion and Aviation  |           |             |
|        |       |                |           | RD          | Road                 |           |             |
|        |       |                |           | RL          | Rail                 |           |             |


### Materials module - Technology names
| Resource ID |                                  | Technology ID |              |
|:-----------:|----------------------------------|:-------------:|--------------|
| XALU        | Primary resource, Aluminium      | MINE          | Extraction   |
| XCEM        | Primary resource, Cement         | MINE          | Extraction   |
| XPHO        | Primary resource, Phosphorus     | MINE          | Extraction   |
| XPOT        | Primary resource, Potassium      | MINE          | Extraction   |
| XSTE        | Primary resource, Steel and Iron | MINE          | Extraction   |
| ALU         | Aluminium                        | PLANT         | Production   |
| CEM         | Cement                           | PLANT         | Production   |
| FERT        | Fertiliser                       | PLANT         | Production   |
| PAP         | Pulp and Paper                   | PLANT         | Production   |
| PETA        | Ammonia                          | PLANT         | Production   |
| PETB        | Petrochemicals                   | PLANT         | Production   |
| STE         | Steel and Iron                   | PLANT         | Production   |

### Materials module - Resource vector names
| Resource Level |                       | Resource ID |                      |
|:--------------:|-----------------------|:-----------:|----------------------|
| X              | Resource (extraction) | ALU         | Aluminium            |
|                |                       | CEM         | Cement               |
|                |                       | PHO         | Phosphorus           |
|                |                       | POT         | Potassium            |
|                |                       | STE         | Steel and Iron       |
| F              | Final                 | ALU         | Aluminium            |
|                |                       | AMM         | Ammonia              |
|                |                       | CEM         | Cement               |
|                |                       | FERT        | Fertiliser           |
|                |                       | PAP         | Pulp and Paper       |
|                |                       | PET         | Petrochemicals       |
|                |                       | STE         | Steel and Iron       |


### Land and Food module - Technology names
| Resource ID |                           | Resource type |                     | Level ID |              |
|:-----------:|---------------------------|:-------------:|---------------------|:--------:|--------------|
| L0          | Land                      | 00            | Total               | RES      | Resource     |
| LA          | Agriculture Land          | 00            | Total               | RES      | Resource     |
|             |                           | Cr            | Cropland, rainfed   | RES      | Resource     |
|             |                           |               |                     | PRD      | Production   |
|             |                           | Ci            | Cropland, Irrigated | RES      | Resource     |
|             |                           |               |                     | PRD      | Production   |
|             |                           | PS            | Pasture land        | RES      | Resource     |
|             |                           |               |                     | PRD      | Production   |
| LF          | Forest land               | 00            | Total               | RES      | Resource     |
|             |                           | PR            | Primary forest land | RES      | Resource     |
|             |                           | OT            | Other forest land   | RES      | Resource     |
|             |                           |               |                     | PRD      | Production   |
| LO          | Other Land                | 00            | Total               | RES      | Resource     |

### Land and Food module - Resource vector names
#### Land - Resource vector names
| Resource ID |                      | Land Level |                     | Sector ID |                            |
|:-----------:|----------------------|:----------:|---------------------|:---------:|----------------------------|
| LAND        | Land, total          |            |                     |           |                            |
| L           | Land                 | AGR        | Agriculture         |           |                            |
|             |                      |            |                     | MFOO      | Livestock production       |
|             |                      |            |                     | VFOO      | Crops production           |
|             |                      |            |                     | VFOOi     | Irrigated Crops production |
|             |                      | FRST       | Forest              |           |                            |
|             |                      |            |                     | BIOW      | Biomass production         |
|             |                      | OTHER      | Other              |           |                            |

#### Food - Resource vector names
| Resource ID |                      | Resource Level |                     | Origin |                           |
|:-----------:|----------------------|:--------------:|---------------------|:------:|---------------------------|
| MFOO        | Livestock, food      |                |                     |        |                           |
|             |                      | P              | Primary             | LAPS   | Agriculture land, Pasture |
| VFOO        | Crops, food          |                |                     |        |                           |
|             |                      | P              | Primary             | LAC    | Agriculture land, Crops   |