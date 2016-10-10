



import sys





with open(sys.argv[1]) as f:
    for line in f:
        fields = line.strip().split('\t')

        print('locarna --noLP  --write-structure  --clustal=out/locarna/clustalw/{sequence_a}_vs_{sequence_b}.clustalw data/fasta/{sequence_a}.fa data/fasta/{sequence_b}.fa'.format(
            alignment = fields[0],
            sequence_a =fields[1],
            sequence_b = fields[2]
        ))


## python run_carna.py pairwise
