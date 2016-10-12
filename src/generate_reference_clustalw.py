
from split_fasta import split_fasta_no_replacement
import sys
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





if __name__ == '__main__':

    fasta_sequence = split_fasta_no_replacement(sys.argv[1])
    seq_a_id = sys.argv[2]
    seq_b_id = sys.argv[3]
    generate_clustalW(seq_a_id, fasta_sequence[seq_a_id], seq_b_id, fasta_sequence[seq_b_id], sys.argv[4])












