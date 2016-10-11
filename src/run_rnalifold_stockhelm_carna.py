


import sys
import os

clustal_folder = sys.argv[1]

structure_folder = sys.argv[2]

output_folder = sys.argv[3]

script_file = '/home/xiuque/Projects/benchmark_analysis/src/benchmark_pipeline/src/rnaalifold_stockhelm.py'



clustal_files = os.listdir(clustal_folder)



for x in clustal_files:
    rnaalifold_files = os.path.join(structure_folder, x)
    rnaalifold_files.replace('.clustalw', '.rnafold.tsv')

    clustal_path = os.path.join(clustal_folder, x)

    out_path = os.path.join(output_folder, x)


    if os.path.exists(rnaalifold_files):
        print('{script_file} {rnaali} {clustal} {out_path}')
    else:
        raise Exception('missing file %s' % rnaalifold_files)








