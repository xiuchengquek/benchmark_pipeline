

import sys
import os

reference = sys.argv[1]
tested = sys.argv[2]
out = sys.argv[3]

script_file = '/share/ClusterShare/software/contrib/marsmi/infernal-1.0.2/easel/bin/esl-compstruct'



reference_files = os.listdir(reference)




for x in reference_files:
    test_file = os.path.join(tested, x)
    ref_file = os.path.join(reference, x)



    out_path = os.path.join(out, x)
    out_path = out_path.replace('.stock', '.esl-comp')

    if os.path.exists(test_file):
        print('{script_file} {ref} {test} > {out_path}'.format(script_file = script_file, ref = ref_file, test = test_file, out_path = out_path))
    else:
        raise Exception('missing file %s' % test_file)





