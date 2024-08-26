import os
import pandas as pd

dp_files = pd.read_csv('config/dp_files.txt')

scenario_path = os.path.join("input_data")
SCENARIOS = [x.name for x in os.scandir(scenario_path) if x.is_dir()]

SCENARIOS = ['GLUCOSE']

rule all:
    input:
        expand("results/{scen}/results_csv", scen=SCENARIOS)

rule convert_dp:
    message: "Converting csv input data to .txt for {wildcards.scen}"
    input:
        other = expand("input_data/{{scen}}/data_csv/{files}", scen=SCENARIOS, files=dp_files),
        dp_path = "input_data/{scen}/data_csv"
    output:
        df_path = "working_directory/{scen}.txt"
    log:
        "working_directory/otoole_{scen}.log"
    conda:
        "envs/otoole_env.yaml"
    shell:
        "otoole convert csv datafile {input.dp_path} {output.df_path}"

# rule pre_process:
#     message: "Pre-processing of {input}"
#     input:
#         "working_directory/{scen}.txt"
#     output:
#         temporary("working_directory/{scen}.pre")
#     conda:
#     # conda activate base
#         "envs/otoole_env.yaml"
#     shell:
#         "python scripts/workflow/pre_process.py otoole {input} {output}"

rule build_lp:
    message: "Building the .lp file"  #for {input}"
    input:
        df_path = "working_directory/{scen}.txt"
    params:
        model_path = "model/osemosys_fast.txt",
    output:
        temp("working_directory/{scen}.lp")
    log:
        "working_directory/{scen}.log"
    threads: 1
    resources:
        mem_mb=62000
    shell:
        "glpsol -m {params.model_path} -d {input.df_path} --wlp {output} --check > {log}"

rule run_model:
    message: "Solving the LP file" #for '{input}'"
    input:
        "working_directory/{scen}.lp",
    output:
        temp("working_directory/{scen}.sol"),
        directory("working_directory/{scen}_duals")
        # Unhash the line above, and the dic_duals and write_duals (in the run.py) if you want dual values as output
    conda:
        "envs/gurobi_env.yaml"
    log:
        "working_directory/gurobi/{scen}.log",
    threads: 32
    resources:
        mem_mb=62000
    script:
        "scripts/workflow/run.py"

rule convert_sol:
    message: "Convert results file {input.sol_path} with otoole "
    input:
        sol_path = "working_directory/{scen}.sol",
        # dp_path = "input_data/{scen}/data"
        df_path = "working_directory/{scen}.txt"
    # params:
        # res_folder = "results/{scen}/results_csv",
        # config = "config/config.yaml"
    output:
        directory("results/{scen}/results_csv/")
    conda:
        "envs/otoole_env.yaml"
    shell:
        "otoole results gurobi csv {input.sol_path} {output} --input_datafile {input.df_path}"


rule clean:
    shell:
        "rm -rf results/* && rm -rf working_directory/*"
