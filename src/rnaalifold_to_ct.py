









import sys
import os
import tempfile
import subprocess
import shutil

def rnaali_dot_bracket(rnaali):
    sequence = ''
    stucture = ''
    with open(sys.argv[1]) as f:
        lines = f.readlines()
        sequence = lines[0].strip()
        structure = lines[1].strip()

    structure = structure.split()[0]
    sequence_name = os.path.basename(sys.argv[1]).replace('rnafold.tsv', '')
    f = tempfile.NamedTemporaryFile(delete=False)
    f.write(">{seq_name}\n{sequence}\n{structure}".format(
        seq_name = sequence_name,
        sequence = sequence,
        structure = structure
    ))


    f.close()
    return [f.name, sequence_name]


def dot_to_ct(dot_bracket_file):
    cmd = '/home/xiuque/Projects/DotAlignerMatthew/paul/dot2ct'
    f = tempfile.NamedTemporaryFile(delete=False)
    f.close()

    subprocess.call("{dot2ct} {dot} {ct}".format(
        dot2ct = cmd,
        dot = dot_bracket_file,
        ct = f.name
    ))


    return f.name

if __name__ == '__main__' :
    dot_bracket_file = rnaali_dot_bracket(sys.argv[1])
    ct_file_name = dot_to_ct(dot_bracket_file)
    shutil.move(ct_file_name, sys.argv[2])



























