
import sys
import re
import os



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


    cycle_align_lines = iter(align_lines)
    for x in cycle_align_lines:
        fields = x.split()
        if len(fields) > 2:

            sequence_a_id = fields[2]
            sequence_a = fields[3:]

            structure = next(cycle_align_lines)
            structure = structure.split()

            sequence_b = next(cycle_align_lines)
            sequence_b = sequence_b.split()
            sequence_b_id = sequence_b[2]
            sequence_b = sequence_b[3:]

            sequence_id = "%s_vs_%s" % (sequence_a_id, sequence_b_id)
            consensus_structure += "".join(structure[3:])
            complete_sequence_a += "".join(sequence_a)
            complete_sequence_b += "".join(sequence_b)



    return [complete_sequence_a,  complete_sequence_b, consensus_structure]


def generate_clustalW(seq_a_id, seq_a, seq_b_id, seq_b, output):
    """
    This function create a temporary clustalW file for running rnaalifold.

    :param seq_a: String - first sequence of the pair
    :param seq_b: String - second sequence of the pair
    :return f.name: temporary name of clustalW file
    """
    f = open(output, 'w')
    clusterStr = "CLUSTALW\n\n" + \
                 "%s\t%s\n" % (seq_a_id, seq_a )+ \
                 "%s\t%s\n" % (seq_b_id, seq_b)

    f.write(clusterStr)
    f.close()



if __name__ == '__main__' :
    fa_out = sys.argv[1]
    clustalw = sys.argv[2]


    sequence_names = os.path.basename(fa_out)
    sequence_names = sequence_names.replace('.txt', '')
    seq_a_id, seq_b_id  =sequence_names.split('_vs_')

    fa_content = get_align_lines(fa_out)
    complete_sequence_a, complete_sequence_b, consensus_structure = get_alignments(fa_content)
    generate_clustalW(seq_a_id, complete_sequence_a, seq_b_id, complete_sequence_b, clustalw)

















