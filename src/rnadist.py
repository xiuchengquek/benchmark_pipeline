

import sys
import os
import tempfile
import subprocess

from multiprocessing import Lock, Process, Queue, current_process


def get_structure(reference):
    ref_in = open(reference)
    ref = ref_in.readlines()
    ref_in.close()

    ref = ref[-1].strip()
    ref = ref.split()[0]
    return ref


def rnadist(value):
    ref_structure = get_structure(value[0])
    test_structure = get_structure(value[1])

    f = tempfile.NamedTemporaryFile(delete=False)
    sequenceStr = "%s\n%s\n" % (ref_structure, test_structure)

    f.write(sequenceStr)
    f.close()

    cmd = 'RNAdistance < {fname} > {fname}.rnad_results'.format(fname = f.name)
    subprocess.call(cmd, shell=True)

    fh_in = open('{fname}.rnad_results'.format(fname=f.name))
    out = fh_in.read()
    fh_in.close()

    out = out.strip()
    res = out.replace('f: ','')
    res = res.strip()

    os.remove(f.name)
    os.remove('{fname}.rnad_results'.format(fname = f.name))

    return "%s\t%s" % (os.path.basename(value[0]),  res)




def multiple_process_chain(input, output):
    for value in iter(input.get, 'STOP'):
        results = rnadist(value)
        output.put([results])



def run():


    reference_folder = sys.argv[1]
    test_folder = sys.argv[2]
    error_log = sys.argv[3]


    fh_err = open(error_log, 'w')

    reference_files = os.listdir(reference_folder)


    files_pair = [[os.path.join(reference_folder, x), os.path.join(test_folder, x)] for x in reference_files]
    TASK = []
    for x in files_pair :

        if os.path.exists(x[0]) and os.path.exists(x[1]):
            TASK.append(x)
        elif not os.path.exists(x[0]):
            fh_err.write("%s is missing" % x[0])
        elif not os.path.exists(x[1]):
            fh_err.write("%s is missing" % x[1])
    fh_err.close()




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
    sys.argv[1] = reference_folder
    sys.argv[2] = test_folder
    sys.argv[4] = results

    python src/benchmark_pipeline/src/rnadist.py out/reference/rnaali/f out/test/rnaali/f err/reference_rnadist.err out/test/rnd_dist.results
    """
    results = run()
    with open(sys.argv[4], 'w+') as f:
        for x in results :
            line = x[0]
            f.write("%s\n" % line)


    #res = rnadist(sys.argv[1], sys.argv[2])
    #output = os.path.basename(sys.argv[1])

