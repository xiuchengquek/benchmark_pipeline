









import sys
import os


structure_folder = sys.argv[1]
output_folder = sys.argv[2]

script_file = '/home/xiuque/Projects/benchmark_analysis/src/benchmark_pipeline/src/rnaalifold_to_ct.py'



structure_files = os.listdir(structure_folder)



for x in structure_files:
    rnaalifold_files = os.path.join(structure_folder, x)
    out_path = os.path.join(output_folder, x)
    out_path = out_path.replace('.rnafold.tsv', '.ct')

    if os.path.exists(rnaalifold_files):
        print('python {script_file} {rnaali} {out_path}'.format(
            script_file = script_file, rnaali = rnaalifold_files,
            out_path = out_path))
    else:
        raise Exception('missing file %s' % rnaalifold_files)








