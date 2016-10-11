




import os
import sys



outdir = 'out/referenece/clustalw'
script_file = '/home/xiuque/Projects/benchmark_analysis/src/benchmark_pipeline/src/generate_reference_clustalw.py'



with open(sys.argv[1]) as f:
    for line in f:
        fields = line.strip().split('\t')
        output = '{seq_a}_vs_{seq_b}.clustalw'
        output = os.path.join(outdir, output)
        cmd = "{script_file} {fasta_file} {seq_a} {seq_b} {output}".format(script_file = fields[0],
                                                                  seq_a =fields[1],
                                                                  seq_b =fields[2],
                                                                    output = output)
        print(cmd)



