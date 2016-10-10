

import os

datafile = config['datafile']
classification = config['rna_classes_file']


fasta_files = []


rna_classes = {}
sequences = []

with open(classification) as f:
    for line in classification :
        rna_class, sequence_name  = line.strip().split()
        rna_classes[rna_class] = sequence_name
        sequences.append(sequence_name)

with open(datafile) as f:
    for line in f :
        fasta_files.append(line.strip())

rule all:
    input : expand('data/fasta/{sequences_name}.fa', sequences_name = sequences)


rule get_fasta:
    input: datafile
    output : expand('data/fasta/{sequences_name}.fa', sequences_name = sequences)
    shell : 'python src/split_fasta.py {input}'







