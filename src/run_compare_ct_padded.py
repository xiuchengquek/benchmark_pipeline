

import sys
import os

reference = sys.argv[1]
tested = sys.argv[2]
out = sys.argv[3]
error = sys.argv[4]

script_file = 'home/xiuque/Projects/benchmark_analysis/src/benchmark_pipeline/src/rnaalifold_to_ct_padded.py'



reference_files = os.listdir(reference)


fh_err = open(error, 'w')


for x in reference_files:
    test_file = os.path.join(tested, x)
    ref_file = os.path.join(reference, x)



    out_path = os.path.join(out, x)
    out_path = out_path.replace('.rnafold.tsv', '.compare_ct')

    if os.path.exists(test_file):
        print('python {script_file} {ref} {test} > {out_path}'.format(script_file = script_file, ref = ref_file, test = test_file, out_path = out_path))
    else:
         fh_err.write('missing file %s\n' % test_file)




fh_err.close()





