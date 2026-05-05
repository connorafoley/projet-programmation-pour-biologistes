#! /usr/bin/env python3

import sys
import os
import argparse


def get_args():
	# create an ArgumentParser object ('parser') that will hold all the information necessary to parse the command line
	parser = argparse.ArgumentParser()

	# add arguments
	parser.add_argument( "job", help="Job name" )
	parser.add_argument( "--queue", "-q", help="Pinnacle queue (comp06, comp72, himem06, himem72, tres06, tres72)", default="comp72" )
	group = parser.add_argument_group()
	group.add_argument( "--conda", "-c", help="Load conda (boolean, default = False)", action="store_true" )
	group.add_argument( "--conda_env", "-e", help="Name of conda environment to activate" )

	return parser.parse_args()


def get_cpus_time():
	num_cpus = 0
	time     = 0
	qos      = ''

	if args.queue == 'comp01':
		num_cpus = 32
		time = 1
		qos = 'comp'
	if args.queue == 'comp06':
		num_cpus = 32
		time = 6
		qos = 'comp'
	elif args.queue == 'comp72':
		num_cpus = 32
		time = 72
		qos = 'comp'
	elif args.queue == 'himem06':
		num_cpus = 24
		time = 6
		qos = 'comp'
	elif args.queue == 'himem72':
		num_cpus = 24
		time = 72
		qos = 'comp'
	elif args.queue == 'tres06':
		num_cpus = 32
		time = 6
		qos = 'tres'
	elif args.queue == 'tres72':
		num_cpus = 32
		time = 72
		qos = 'tres'

	return(time, num_cpus, qos)


def print_slurm():

	if(args.conda and not args.conda_env):
		sys.exit("When specifying '--conda', must also specify '--conda_env'")

	time, num_cpu, qos = get_cpus_time()

	print('#!/bin/bash' + '\n')
	print('#SBATCH --job-name=' + args.job)
	print('#SBATCH --partition' + ' ' + args.queue)
	print('#SBATCH --nodes=1')
	print('#SBATCH --qos', qos)
	print('#SBATCH --tasks-per-node=' + str(num_cpu))
	print('#SBATCH --time=' + str(time) + ':00:00')
	print('#SBATCH -o', args.job + '_%j.out')
	print('#SBATCH -e', args.job + '_%j.err')
	print('#SBATCH --mail-type=ALL')
	print('#SBATCH --mail-user=aja@uark.edu')
	
	print()
	print('export OMP_NUM_THREADS=' + str(num_cpu))
	print()

	print('module purge')
	print('module load intel/18.0.1 impi/18.0.1 mkl/18.0.1')

	if(args.conda):
		print('module load python/3.7.3-anaconda')
		print()
		print('conda init bash')
		print('source activate ~/.conda/envs/' + str(args.conda_env))
		print('OMPI_MCA_opal_cuda_support=true')

	print()
	print('cd $SLURM_SUBMIT_DIR')
	# print('rsync -arl * /scratch/$SLURM_JOB_ID/')
	# print()
	# print('cd /scratch/$SLURM_JOB_ID')

	print('# job command here')

	print()
	# print('cd $SLURM_SUBMIT_DIR')
	# print('rsync -arl /scratch/$SLURM_JOB_ID/* .')
	# print()

def main():
	print_slurm()


# get the arguments before calling main
args = get_args()


# execute the program by calling main
if __name__ == "__main__":
	main()

