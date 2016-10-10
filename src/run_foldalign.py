



import sys





with open(sys.argv[1]) as f:
    for line in f:
        fields = line.strip().split('\t')

        print('/share/ClusterShare/software/contrib/marsmi/foldalign-2.1.1/bin/foldalign data/fasta/{sequence_a}.fa data/fasta/{sequence_b}.fa > out/foldalign/output/{sequence_a}_vs_{sequence_b}.txt '.format(
            alignment = fields[0],
            sequence_a =fields[1],
            sequence_b = fields[2]
        ))


## python run_carna.py pairwise
