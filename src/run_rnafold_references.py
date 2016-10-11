import os

reference_dir = 'out/reference/clustalw'
stock_dir  = 'out/reference/rnaalifold/'
command  = 'RNAalifold'




reference_files = os.listdir(reference_dir)


for x in reference_files:
    clustalfiles = os.path.join(reference_dir, x)
    stockfiles = os.path.join(stock_dir, x)
    stockfiles = stockfiles.replace('.clustalw', '.rnafold.tsv')
    cmd = "{script_file} --noLP {clustalfiles} > {stockfiles}".format(
        script_file = command,
        clustalfiles = clustalfiles,
        stockfiles = stockfiles

    )
    print(cmd)






