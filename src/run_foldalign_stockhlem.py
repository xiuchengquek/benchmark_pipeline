





import os

foldalign_dir = 'out/foldalign/output/'
stock_dir  = 'out/foldalign/stock/'
script_file = '/home/xiuque/Projects/benchmark_analysis/src/benchmark_pipeline/src/foldalign_stockhelm.py'




foldalign_files = os.listdir(foldalign_dir)


for x in foldalign_files:
    clustalfiles = os.path.join(foldalign_dir, x)
    stockfiles = os.path.join(stock_dir, x)
    stockfiles = stockfiles.replace('.txt', '.stock')
    cmd = "python {script_file} {clustalfiles} {stockfiles}".format(
        script_file = script_file,
        clustalfiles = clustalfiles,
        stockfiles = stockfiles

    )
    print(cmd)





