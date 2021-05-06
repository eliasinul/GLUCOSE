# GLUCOSE
Global Least-cost User-friendly CLEWs Open Source Exploratory model

## Folder structure

- Input data files in .txt and .csv formats are stored in the `input_data` folder
    - One folder is available per each modelled scenario: namely, BASELINE, 2DEGREE, FOOD, MATERIALS, TOTAL. 
- The OSeMOSYS model file needed to run the GLUCOSE model is retrievable froom the [OSeMOSYS GitHub repository] (https://github.com/OSeMOSYS/OSeMOSYS_GNU_MathProg/releases)

- To run GLUCOSE on your device, the following software needs to be installed:
    - [GNU Linear Programming Kit (`GLPK`)] (https://sourceforge.net/projects/winglpk/): instructions for installing `GLPK` are available [here] (https://sourceforge.net/projects/winglpk/)

- To generate results for GLUCOSE, the following steps are needed:
    1. On your device, type the following command in the terminal to generate the linear programming file needed to solve the model:
        > glpsol -m model_file.txt -d data_file.txt --wlp results_file.lp
    2. Once the `results_file.lp`is generated, the model can be optimized using a solver of your choice. 
        In order for the GLUCOSE model to be completely open from source to solver, we recommend using the open-source mixed integer linear programming solver [`Cbc`](https://github.com/coin-or/Cbc).
        > cbc results_file.lp solve -solu results_file.txt

To enhance the transparency and accessibility of the model data and results, both the `input_data.txt` files and the related `results_file.txt` files can be converted into different file formats usign the [`otoole` Python package] (https://otoole.readthedocs.io/en/latest/), which provides a command-line interface for users of OSeMOSYS.

## Licensing

- Data is released under the terms of a CC-BY 4.0 License Agreement.
- A modified copy of OSeMOSYS is redistribruted in this repository under Apache 2.0 license agreement,
  a copy of which can be found in the `model` folder
