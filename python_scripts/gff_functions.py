# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 09:47:25 2026

gff_parse.py

Assignment for Programming For Biologists, Dr. Andrew Alverson, Spring Semester 2026

@author: conno
"""
import pandas as pd
#!/usr/bin/env puthon3

def read_fasta(fasta_name):
    f = fasta_name
    keys = []
    fasta = dict()
    with open(f,'r') as file:
        lines = file.readlines()

        for line in lines:
            if line.startswith('>'):
                keys.append(line.strip())             
                fasta[(keys[-1])] = ''
                continue
            else:
                fasta[keys[-1]] += line.strip()
    return fasta

def read_gff(gff_name):
    gff = gff_name
    gfile = [('seqid', 'source', 'type', 'start', 'end', 'score', 'strand', 'phase', 'attributes')]
    with open(gff,'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith('#'):
                continue
            else:
                parts = line.strip().split('\t')
                if len(parts) == 9:                 
                    gfile.append(tuple(parts))
    return gfile


def write_output(fasta,gfile):
    gff = pd.DataFrame(gfile[1:],columns=gfile[0])
    fid, gen = next(iter(fasta.items()))
    lines = []
    for _, row in gff.iterrows():
        seqid = row['seqid']
        if seqid not in fid:
            continue
        start = int(row['start']) - 1
        end = int(row['end'])
        Atts = row['attributes']
        gene = gen[start:end]
        fields = Atts.split(';')
        attrs = {}
        typ = row['type']
        if not 'gene' in typ:
            continue
        for field in fields:
            if '=' in field:
                key, value = field.split('=', 1)
                attrs[key] = value
        header = f">{seqid}  {attrs.get('ID')} {attrs.get('Name')}"
        lines.append(header + '\n')
        lines.append(gene + '\n')
        
    with open('covid_genes.fasta','w') as f:
        f.writelines(lines)
        
        