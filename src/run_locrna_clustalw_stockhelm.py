

import os

locarna_dir = 'out/locarna/clustalw'
stock_dir  = 'out/locarna/stock'
script_file = '/home/xiuque/Projects/benchmark_analysis/src/benchmark_pipeline/src/locrna_clustalw_stockhelm.py'




locarna_files = os.listdir(locarna_dir)


for x in locarna_files:
    clustalfiles = os.path.join(locarna_dir, x)
    stockfiles = os.path.join(stock_dir, x)
    cmd = "python {script_file} {clustalfiles} {stockfiles}".format(
        script_file = script_file,
        clustalfiles = clustalfiles,
        stockfiles = stockfiles

    )
    print(cmd)









