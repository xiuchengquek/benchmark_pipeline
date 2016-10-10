qsub -cwd -b y -j y -pe smp 1  -t 1:100 -V -N workers 'python src/benchmark_pipeline/src/carna_zeromq/worker.py'



