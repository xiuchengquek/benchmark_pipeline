



from locrna_clustalw_stockhelm  import parse_stockholm, fill_consensus_sequenece
import sys


def parse_clustalw_without_structure(stream):

    complete_sequence_a = ''
    complete_sequence_b = ''
    sequence_pair_id = ''

    for line in stream:
        line = line.strip()
        if line:
            sequenceA_id, sequenceA_fasta  = line.split()
            sequenceB = next(stream).strip()
            sequenceB_id, sequenceB_fasta = sequenceB.split()

            complete_sequence_a += sequenceA_fasta
            complete_sequence_b += sequenceB_fasta
            sequence_pair_id = '%s_vs_%s' % ( sequenceA_id, sequenceB_id)

    return [sequence_pair_id, complete_sequence_a, complete_sequence_b]








def parse_rna_alifold(alifold):
    f = open(alifold).readlines()
    structure = f[1]
    structure = structure.split()[0]
    return structure



if __name__ == '__main__' :
    alifold_file = sys.argv[1]
    clustal_file = sys.argv[2]

    structure = parse_rna_alifold(alifold_file)
    with open(clustal_file) as f :
        next(f) # remove the first 2 lines
        next(f)
        sequence_pair_id, complete_sequence_a, complete_sequence_b = parse_clustalw_without_structure(f)

    consensus_sequence  = fill_consensus_sequenece(complete_sequence_a, complete_sequence_b)
    stockholm_string = parse_stockholm(sequence_pair_id, consensus_sequence, structure)
    with open(sys.argv[3], 'w') as f:
       f.write(stockholm_string)

















