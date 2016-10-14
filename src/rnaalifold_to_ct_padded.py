




from rnaalifold_to_ct import rnaali_dot_bracket, write_dot_bracket,dot_to_ct

import os
import sys
import subprocess


def add_padding(sequence_a, sequence_b):
    """
    see code rnaalifodl to ct
    :param sequence_a: { sequence_name  : '..' , 'sequence' : '..' ,  'structure' : '..'
    :param sequence_b: see sequence_a
    :return: sequence_a and sequence_b with padding
    """

    seq_a_len = len(sequence_a['sequence'])
    seq_b_len = len(sequence_b['sequence'])

    seq_diff = seq_a_len - seq_b_len

    if seq_diff > 0:
        sequence_b['sequence'] = sequence_b['sequence'] + '_' * abs(seq_diff)
        sequence_b['structure'] = sequence_b['structure'] + '_' * abs(seq_diff)
    elif seq_diff < 0:
        sequence_a['sequence_b'] = sequence_a['sequence'] + '_' * abs(seq_diff)
        sequence_a['structure'] = sequence_a['structure'] + '_' * abs(seq_diff)


    return [sequence_a, sequence_b]











if __name__ == '__main__' :
    reference = sys.argv[1]
    test = sys.argv[2]
    out_file  =sys.argv[3]

    script_file = '/home/xiuque/Projects/benchmark_analysis/src/benchmark_pipeline/src/compare_ct.pl'

    reference_dot = rnaali_dot_bracket(reference)
    test_dot = rnaali_dot_bracket(test)
    reference_dot , test_dot = add_padding(reference_dot, test_dot)

    reference_dotfile, reference_name = write_dot_bracket(reference_dot['sequence_name'], reference_dot['sequence'], reference_dot['structure'])
    test_dotfile, test_name = write_dot_bracket(test_dot['sequence_name'], test_dot['sequence'], test_dot['structure'])
    reference_ct = dot_to_ct(reference_dotfile)
    test_ct = dot_to_ct(test_dotfile)

    subprocess.call('{script_file} {ref_ct} {test_ct} > {out_file}'.format(script_file = script_file, ref_ct = reference_ct, test_ct = test_ct), shell=True)




































