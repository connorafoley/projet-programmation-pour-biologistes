# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 14:57:01 2026

gff_parse.py

Assignment for Programming For Biologists, Dr. Andrew Alverson, Spring Semester 2026

@author: conno
"""

#!/usr/bin/env puthon3

import argparse
import gff_functions

def get_args():
    parser = argparse.ArgumentParser(description="Haec scripta computat numerum in locis lectis in seriem fibonacciem")
    
    parser.add_argument("--fasta_name","-fa", help = 'FASTA file name.')
    
    parser.add_argument("--gff_name","-gf", help = "GFF file sequence.")
    
    args = parser.parse_args()

    return args
def main():
    args = get_args()
    fasta_name = args.fasta_name
    gff_name = args.gff_name
    fas = gff_functions.read_fasta(fasta_name)
    gff = gff_functions.read_gff(gff_name)
    gff_functions.write_output(fas,gff)

if __name__ == "__main__":
    main()
