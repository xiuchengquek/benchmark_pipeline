#!/usr/bin/env bash



python src/benchmark_pipeline/src/split_fasta.py data/reference_alignments/fasta_file.tsv



python src/benchmark_pipeline/src/get_pairwise_alignments.py data/reference_alignments/fasta_file.tsv