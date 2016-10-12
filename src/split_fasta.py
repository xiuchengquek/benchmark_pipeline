




import sys




def split_fasta(fasta_file):
    fasta = open(fasta_file).readlines()
    fasta = [x.strip() for x in fasta]

    seq_a_id = fasta[0].replace('>', '')
    seq_a_fasta = fasta[1].replace('-', '')
    seq_b_id = fasta[2].replace('>', '')
    seq_b_fasta = fasta[3].replace('-', '')

    return {
        seq_a_id : seq_a_fasta,
        seq_b_id : seq_b_fasta

    }


def split_fasta_no_replacement(fasta_file):
    fasta = open(fasta_file).readlines()
    fasta = [x.strip() for x in fasta]

    seq_a_id = fasta[0].replace('>', '')
    seq_a_fasta = fasta[1]
    seq_b_id = fasta[2].replace('>', '')
    seq_b_fasta = fasta[3]

    return {
        seq_a_id : seq_a_fasta,
        seq_b_id : seq_b_fasta

    }

def gather_fasta_sequences(sequences_file):
    sequences = open(sequences_file).readlines()
    sequences = [x.strip() for x in sequences ]
    seq_id_sequence_map = {}
    for x in sequences:
        sequences_content= split_fasta(x)
        print(sequences_content, x)
        seq_id_sequence_map.update(sequences_content)
    return seq_id_sequence_map



def print_fasta_to_folder(seq_id_sequence_map):
    for sequence_id, sequence in seq_id_sequence_map.items():
        file_name = "data/fasta/%s.fa" % sequence_id
        with open(file_name,'w') as f:
            f.write(">%s\n%s\n" % (sequence_id, sequence))




def get_pair_wise_alignments(sequences_file):
    sequences = open(sequences_file).readlines()
    sequences = [x.strip() for x in sequences ]
    seq_pairs = {}
    for x in sequences:
        sequences_content = split_fasta(x)
        seq_pairs[x] = list(sequences_content.keys())
    for key, value in seq_pairs.items():
        print("%s\t%s\t%s" %(key, value[0], value[1]))












if __name__ == '__main__' :

     sequences_file = sys.argv[1]
     seq_id_sequence_map = gather_fasta_sequences(sequences_file)
     print_fasta_to_folder(seq_id_sequence_map)

































