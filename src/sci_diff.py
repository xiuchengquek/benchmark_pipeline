

import os
import subprocess
import re
import tempfile
import sys
from collections import defaultdict
from multiprocessing import Lock, Process, Queue, current_process
MEFSCORERE = re.compile('.*\(([\s\-0-9\.]+)\)\\\\n\'')



def run_rna_fold(sequence):
    """
    This function serves to run rnafold and get the MFE score using regular expression


    :param sequence: string containing sequence
    :return score: float contain MFE score of aligned sequences
    """
    sequence = sequence.replace('-', '')
    sequence = str.encode(sequence)
    cmd = ['RNAfold']

    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    try :
        outs, errs = p.communicate(input=sequence,timeout=600) # set time out, should finish in 600secs

    except TimeoutError:
        p.kill()
        outs, errs = p.communicate()

    ## will throw array if fails
    result = str(outs)
    score = MEFSCORERE.search(result).group(1)
    score = float(score)


    return score



def parse_rnaali(alifile):
    """

    :param alifile: filename of rna ali fold file and get the score
    :return: return score
    """

    lines = open(alifile).readlines()
    result = [ x.strip() for x in lines]
    result = result[-1].split(' ',1)
    result = result[-1]
    result = result.replace('(', '')
    result = result.replace(')', '')
    score = re.split('[=\+]', result)
    score = [float(x.strip()) for x in score]
    return score

def parse_clustalw(stream) :

    consensus_structure = ''
    complete_sequence_a = ''
    complete_sequence_b = ''
    sequence_pair_id = ''
    next(stream)

    for line in stream:
        line = line.strip()
        if line:
            if '(' not in line:
                sequenceA = line
                sequenceA_id, sequenceA_fasta  = sequenceA.split()
                sequenceB = next(stream).strip()
                sequenceB_id, sequenceB_fasta = sequenceB.split()
                complete_sequence_a += sequenceA_fasta
                complete_sequence_b += sequenceB_fasta

    return [sequenceA_id, sequenceB_id, complete_sequence_a, complete_sequence_b]


def rnafold_clustalw_process_chain(input_files):
    """
    This function is written mainly to help with the multiple processin module of python

    :param sequence_pair: tuple conatining 2 items. The first is the clustalwfile and the 2nd is alignfold file
    :return: output
    """
    clustalw_file = input_files[0]
    alifold_file = input_files[1]

    sequenceA_id = ''
    sequenceB_id = ''
    complete_sequence_a = ''
    complete_sequence_b = ''



    with open(clustalw_file) as f:
        sequenceA_id , sequenceB_id, complete_sequence_a, complete_sequence_b = parse_clustalw(f)

    mfe_a = run_rna_fold(complete_sequence_a)
    mfe_b  = run_rna_fold(complete_sequence_b)

    score  = parse_rnaali(alifold_file)
    sci =  score[0] / ((mfe_a + mfe_b) / 2 )
    score = "\t".join([str(x) for x in score])
    output = [sequenceA_id, sequenceB_id, mfe_a, mfe_b, score, sci]
    output = "\t".join([ str(x) for x in output])
    return output


def multiple_process_chain(input, output):
    for value in iter(input.get, 'STOP'):
        results = rnafold_clustalw_process_chain(value)
        output.put([results])


def run():


    clustalw_folder = sys.argv[1]
    rnaali_folder = sys.argv[2]
    error_log = sys.argv[3]


    fh_err = open(error_log, 'w')

    clustalw_files = os.listdir(clustalw_folder)


    files_pair = [[os.path.join(clustalw_folder, x), os.path.join(rnaali_folder, x.replace('.clustalw', '.rnafold.tsv'))] for x in clustalw_files]
    TASK = []
    for x in files_pair :

        if os.path.exists(x[0]) and os.path.exists(x[1]):
            TASK.append(x)
        elif not os.path.exists(x[0]):
            fh_err.write("%s is missing" % x[0])
        elif not os.path.exists(x[1]):
            fh_err.write("%s is missing" % x[1])




    input = Queue()
    output = Queue()


    n = sys.argv[5]

    for task in TASK:
        input.put(task)

    for w in range(int(n)):
        Process(target=multiple_process_chain, args=(input, output)).start()


    for i in range(int(n)):
        input.put('STOP')

    results = []
    for w in range(len(TASK)):
        results.append(output.get())
    return results


if __name__ == '__main__':
    """
    sys.argv[1] = clustalw_folder
    sys.argv[2] = rnaali_folder
    sys.argv[3] = err
    sys.argv[4] = results
    sys.argv[5] = ncores

    python src/benchmark_pipeline/src/sci_diff.py out/reference/clustalw/ out/reference/rnaalifold/ err/reference_sci.err out/reference/sci.results 4
    """
    """
    results = run()
    with open(sys.argv[4], 'w+') as f:
        for x in results:
            line = x[0]
            f.write("%s\n" % line)

    """
    with open(sys.argv[1]) as f:
        print(parse_clustalw(f))


