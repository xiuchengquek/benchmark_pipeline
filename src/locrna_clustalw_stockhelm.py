






import sys



def fill_consensus_sequenece(sequenceA, sequenceB):
    sequenceA = list(sequenceA)
    gapsA = [i for i,x in enumerate(sequenceA) if x == '-']
    for x in gapsA:
        sequenceA[x] = sequenceB[x]

    return "".join(sequenceA)





def parse_stockholm(sequence_id ,sequence, structure):
    header = "# STOCKHOLM 1.0"
    footer = "//"
    structure_line = "#=GR {sequence_id} SS {structure}".format(sequence_id= sequence_id,
                                               structure = structure)
    sequence_line = "{sequence_id} {sequence}".format(sequence_id = sequence_id, sequence=sequence)

    stockholm_line = "\n".join([header, structure_line, sequence_line, footer])
    return stockholm_line


def parse_clustalw(stream) :

    consensus_structure = ''
    complete_sequence_a = ''
    complete_sequence_b = ''
    sequence_pair_id = ''

    for line in stream:
        line = line.strip()
        if line:
            print(line)
            structureA = line.strip()
            sequenceA = next(stream).strip()
            sequenceA_id, sequenceA_fasta  = sequenceA.split()
            sequenceB = next(stream).strip()
            sequenceB_id, sequenceB_fasta = sequenceB.split()

            next(stream).strip()
            complete_sequence_a += sequenceA_fasta
            complete_sequence_b += sequenceB_fasta
            sequence_pair_id = '%s_vs_%s' % ( sequenceA_id, sequenceB_id)
            consensus_structure += structureA

    return [sequence_pair_id, consensus_structure, complete_sequence_a, complete_sequence_b]




if __name__ == '__main__' :
    with open(sys.argv[1]) as f :
        next(f) # remove the first 2 lines
        next(f)
        sequence_pair_id, consensus_structure, complete_sequence_a, complete_sequence_b = parse_clustalw(f)


    consensus_sequence = fill_consensus_sequenece(complete_sequence_a, complete_sequence_b)
    consensus_structure = consensus_structure.replace('-', '')

    stockholm_string = parse_stockholm(sequence_pair_id, consensus_sequence, consensus_structure)

    with open(sys.argv[2], 'w') as f:
        f.write(stockholm_string)




















