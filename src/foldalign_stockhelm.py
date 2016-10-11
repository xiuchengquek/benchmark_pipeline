


import sys
import re

from locrna_clustalw_stockhelm import fill_consensus_sequenece, parse_stockholm

def get_align_lines(file):
    align_lines = []
    f = open(file).readlines()

    for line in f:
        print(line)
        if re.match('^; ALIGN\s' , line):

            align_lines.append(line.strip())

    align_lines = align_lines[7:-3]
    return align_lines


def get_alignments(align_lines):

    consensus_structure = ''
    complete_sequence_a = ''
    complete_sequence_b = ''

    for x in align_lines:
        fields = x.split()
        if len(fields) > 2:

            sequence_a_id = fields[2]
            sequence_a = fields[3:]

            structure = next(align_lines)
            structure = structure.split()

            sequence_b = next(align_lines)
            sequence_b = sequence_b.split()
            sequence_b_id = sequence_b[2]
            sequence_b = sequence_b[3:]

            sequence_id = "%s_vs_%s" % (sequence_a_id, sequence_b_id)
            consensus_structure += "".join(structure[3:])
            complete_sequence_a += "".join(sequence_a)
            complete_sequence_b += "".join(sequence_b)



    return [sequence_id,complete_sequence_a,  complete_sequence_b, consensus_structure]



if __name__ == '__main__':
    align_lines = get_align_lines(sys.argv[1])
    sequence_pair_id, complete_sequence_a, complete_sequence_b, consensus_structure = get_alignments(align_lines)
    consenses_sequence = fill_consensus_sequenece(complete_sequence_a, complete_sequence_b)
    stockholm_string = parse_stockholm(sequence_pair_id, consenses_sequence, consensus_structure)
    with open(sys.argv[2], 'w') as f:
       f.write(stockholm_string)





