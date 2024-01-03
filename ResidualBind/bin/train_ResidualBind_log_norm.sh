#!/bin/bash
#SBATCH --partition carter-gpu
#SBATCH --account carter-gpu
#SBATCH --gpus=1
#SBATCH --output=/cellar/users/aklie/projects/ML4GLand/use_cases/ResidualBind/bin/slurm_logs/%x.%A.out
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=16G
#SBATCH --time=14-00:00:00

#####
# USAGE: 
# sbatch --job-name=train_ResidualBind_log_norm_2024_01_03 train_ResidualBind_log_norm.sh
#####

# Date
date
echo -e "Job ID: $SLURM_JOB_ID\n"

# Configuring env (choose either singularity or conda)
source activate ml4gland
script_path=/cellar/users/aklie/projects/ML4GLand/use_cases/ResidualBind/bin/train_ResidualBind_log_norm_v2.py

# Run script
cmd="python $script_path"
echo $cmd
eval $cmd

# End
echo "Done."
date