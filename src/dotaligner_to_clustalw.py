
import sys
import os

from generate_reference_clustalw import  generate_clustalW



if __name__ == '__main__':

    fh_in = open(sys.argv[1])
    dotaligner_content = fh_in.read()
    fh_in.close()


    fields = dotaligner_content.strip().split()
    seq_a_id = os.path.basename(fields[0]).replace('_dp.pp', '' )
    seq_b_id =  os.path.basename(fields[1]).replace('_dp.pp', '')

    seq_a = fields[8]
    seq_b =fields[6]

    generate_clustalW(seq_a_id, seq_a, seq_b_id, seq_b, sys.argv[2])
