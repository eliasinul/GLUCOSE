#!/bin/bash
# Load the glpk mode which includes glpsol, please check version this command is specific for Tegner
# Set the path to glpk (need to change) if not on Tegner
# module add glpk/4.65 only needed for kth cluster

cd .. || exit 
cd .. || exit 

## Provide the terminal command to install glpk
echo Install glpk via Homebrew - for Mac-users only
# brew install glpk || exit

## GLUCOSE Git repository URL 
# repo_url="https://github.com/AgnesBelt/GLUCOSE.git" 
 
# Directory to clone the repository into 
GLUCOSE_dir="KTH-dESA/GLUCOSE/" 

## Clone the Git repository 
# echo Clone GitHUb repository: AgnesBelt/GLUCOSE || exit
# git clone "$repo_url" 

## Navigate into the cloned repository directory 
echo Navigate to the folder: KTH-dESA/GLUCOSE/
cd "$GLUCOSE_dir" || exit 

## Install and create conda environment: snakemake
# echo Install and create conda environment : snakemake
# conda install -c conda-forge mamba || exit
# mamba create -c bioconda -c conda-forge -n snakemake snakemake-minimal pandas || exit

## Activate conda environment snakemake
echo Activate conda environment: snakemake
source /Users/agnesebeltramo/anaconda3/etc/profile.d/conda.sh || exit 
conda activate snakemake || exit 

## Execute the snakemake workflow for GLUCOSE:
    # 1. read input_data in .csv
    # 2. generate .lp, run the model with GUROBI
    # 3. generate solution .sol file
    # 4. convert .sol file into .csv results files
    # 5. process results and generate results visualisation

# git branch GLUCOSE_rdm || exit

echo Execute workflow to run and process GLUCOSE results
snakemake --cores 4 --use-conda || exit 

cd .. || exit 
cd .. || exit 

## Adapted esom_sga workflow for RDM runs: Git repository URL 
# repo_url="https://github.com/AgnesBelt/glucose_esom_gsa.git" 

# Directory to clone the repository into 
GLUCOSE_rdm_dir="AgnesBelt/glucose_esom_gsa/"

## Navigate into the cloned repository directory 
echo Navigate to the folder: AgnesBeltr/glucose_esom_gsa/
cd "$GLUCOSE_dir" || exit 
# git branch envs_glucose || exit

## Execute the adapted snakemake workflow for RDM based on esom_gsa:
# pip install -r requirements.txt ||exit

## Copy the GLUCOSE scenario of reference to the glucose_esom_gsa/congif folder
echo Copy the GLUCOSE scenario of reference to the glucose_esom_gsa/congif folder
# cd input_data
# cp -r /Users/agnesebeltramo/Documents/GitHub_repo/KTH-dESA/GLUCOSE/input_data/GLUCOSE_noDA2CS_14_9   /Users/agnesebeltramo/Documents/GitHub_repo/AgnesBelt/glucose_esom_gsa/congif/model_input

SOURCE="input_data"
DESTINATION="/Users/agnesebeltramo/Documents/GitHub_repo/AgnesBelt/glucose_esom_gsa/config"

echo "${DESTINATION}/model_input/"

# cp -r "$SOURCE/GLUCOSE_noDA2CS_14_9"*  "$DESTINATION/model_input/"
cp -r "${SOURCE}/GLUCOSE_noDA2CS_14_9/"*  "${DESTINATION}/model_input"

## Execute the glucose_esom_gsa workflow
echo Execute the glucose_esom_gsa workflow 
snakemake --use-conda --cores 4 --resources mem_mb=16000 disk_mb=30000 || exit

