

import sys
import os

fold_align = sys.argv[1]
clustalw = sys.argv[2]


script_file = '/home/xiuque/Projects/benchmark_analysis/src/benchmark_pipeline/src/foldalign_to_clustalw.py'
fold_align_files = os.listdir(fold_align)


for x in fold_align_files:
    in_file = os.path.join(fold_align, x)
    out_file = os.path.join(clustalw, x)



    if os.path.exists(in_file):
        print('python {script_file} {in_file} {out_file}'.format(in_file, in_file, out_file = out_file))
    else:
        raise Exception('missing input %s ' % in_file)










