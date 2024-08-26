# GLUCOSE
The Global Least-cost User-friendly CLEWs Open Source Exploratory model

## Instructions

- Input data files in .txt and .csv formats are stored in the `input_data` folder
    - One folder is available per each modelled scenario: namely, BASELINE, 2DEGREE, FOOD, MATERIALS, TOTAL. 
- The OSeMOSYS model file needed to run the GLUCOSE model is retrievable from the [OSeMOSYS GitHub repository](https://github.com/OSeMOSYS/OSeMOSYS_GNU_MathProg/releases)

- To run GLUCOSE on your device, the following software needs to be installed:
    - [GNU Linear Programming Kit (GLPK)](https://sourceforge.net/projects/winglpk/): instructions for installing **GLPK** are available [here](https://sourceforge.net/projects/winglpk/)

- To generate results for GLUCOSE, the following steps are needed:
    1. On your device, type the following command in the terminal to generate the linear programming file needed to solve the model:
        > glpsol -m model_file.txt -d data_file.txt --wlp results_file.lp --check
    2. Once the `results_file.lp`is generated, the model can be optimized using a solver of your choice. 
        In order for the GLUCOSE model to be completely open from source to solver, we recommend using the open-source mixed integer linear programming solver [**Cbc**](https://github.com/coin-or/Cbc):
        > cbc results_file.lp solve -solu results_file.txt

To enhance the transparency and accessibility of the model data and results, both the `input_data.txt` files and the related `results_file.txt` files can be converted into different file formats usign the [**otoole** Python package](https://otoole.readthedocs.io/en/latest/), which provides a command-line interface for users of OSeMOSYS.

## Using the snakemake workflow to run OSeMOSYS models
This workflow allows to run one or multiple scenarios for a model built in OSeMOSYS, using the Python package otoole and the solver GUROBI. 
1. Starting from an OSeMOSYS datapackage, the workflow uses otoole to generate an OSeMOSYS input data file in .txt
2. Each scenario is then solved using the Gurobi solver.
    a. if of interest, the workflow can extract dual values for multiple constraints in the model.
3. The solution file generated in Gurobi (.sol) is then converted using otoole to a set of .csv result files.

### Installation
Create a new environment called `snakemake`, where to install snakemake using conda, using this commands:

```bash
conda install -c conda-forge mamba
mamba create -c bioconda -c conda-forge -n snakemake snakemake-minimal
```

### Adding new scenarios
Place datapackage(s) in the folder `input_data`. Each datapackage should be placed in a specific folder named after the scenario, e.g. `Baseline`.

### Running the workflow
1. ***Optional***: To retrieve dual values from your model you need to edit the following:
    - edit the list of `constraints` in the file `scripts/workflow/run.py`, by unhashing lines 77, 85-86
    - edit the file `snakefile`, by unshashing line 63
2. Open terminal or command prompt and change to the directory of the snakefile.
3. Activate the conda environment `snakemake`.
    ```bash
    conda activate snakemake
    ```
5. ***Optional***: Perform a dry run to test snakemake with the command: 
    ```bash
    snakemake -n
    ```
5. Start the scenario runs via the workflow, using the following command:
    ```bash
    snakemake --cores <number of cores to be used> --use-conda
    ```

## Licensing

- The GLUCOSE data is released under the terms of a [CC-BY 4.0 License Agreement](https://creativecommons.org/licenses/by/4.0/legalcode).
