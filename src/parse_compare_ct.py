



import os
import sys
import re
from collections import defaultdict



if __name__ == '__main__':



    alignment = defaultdict(dict)

    result_folder = sys.argv[1]
    software = sys.argv[2]
    result_files = os.listdir(result_folder)


    for x in result_files:
        in_file = os.path.join(result_folder, x)
        sample = x.replace('.compare_ct', '')
        sensitivity = ''
        selectivity = ''
        approx_correlation = ''
        cor_coef = ''
        mat_coef = ''



        with open(x) as f:
            for line in f:
                line = line.strip()
                if line.startswith('sensitivity'):
                    sensitivity = line.split()[-1]
                if line.startswith('selectivity'):
                    selectivity = line.split()[-1]
                if line.startswith('Approximate correlation'):
                    approx_correlation  = line.split()[-1]
                if line.startswith('Correlation Coefficient'):
                    cor_coef  = line.split()[-1]
                if line.startswith('Matthews'):
                    mat_coef  = line.split()[-1]

        print('{sample}\t{software}\t{sensitivity}\t{selectivity}\t{approx_co}\t{cor}\t{mat_coef}'.format(
            sample = sample,
            software = software,
            sensitivity = sensitivity,
            selectivity = selectivity,
            approx_co = approx_correlation,
            cor = cor_coef,
            mat_coef = mat_coef
        ))


















