#!/bin/bash
# Load the glpk mode which includes glpsol, please check version this command is specific for Tegner
# Set the path to glpk (need to change) if not on Tegner
module add glpk/4.65


# Your Git repository URL 
repo_url="https://github.com/AgnesBelt/GLUCOSE.git" 
 
# Directory to clone the repository into 
clone_dir="repo_clone" 

# Clone the Git repository 
git clone "$repo_url" "$clone_dir" 

# Navigate into the cloned repository directory 
cd "$clone_dir" || exit 

# Execute the snakemake workflow for GLUCOSE:
    # 1. read input_data in .csv
    # 2. generate .lp, run the model with GUROBI
    # 3. generate solution .sol file
    # 4. convert .sol file into .csv results files
    # 5. process results and generate results visualisation

snakemake --cores 4 --use-conda


