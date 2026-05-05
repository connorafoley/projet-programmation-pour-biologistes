#!/usr/bin/env bash
#SBATCH --job-name=watermelonslurm
#SBATCH --partition=comp01
#SBATCH --nodes=1
#SBATCH --qos=cloud72
#SBATCH --cpus-per-task=32
#SBATCH --time=99
#SBATCH --output=%x.%j.out
#SBATCH --error=%x.%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=caf030@uark.edu
module load blast
blastn -query watermelon.fsa -subject watermelon.fsa > wat.vs.wat.blastn