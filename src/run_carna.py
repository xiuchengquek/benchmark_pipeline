



import sys





with open(sys.argv[1]) as f:
    for line in f:
        fields = line.strip().split('\t')

        print('locarna --noLP  --write_structures  --clustal=out/locarna/clustalw/{alignment} data/fasta/{sequence_a}.fa data/fasta/{sequence_b}.fa'.format(
            alignment = fields[0],
            sequence_a =fields[1],
            sequence_b = fields[2]
        ))
