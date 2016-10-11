import os

carna_dir = 'out/carna/clustalw'
stock_dir  = 'out/carna/rnaalifold/'
command  = 'RNAalifold'




carna_files = os.listdir(carna_dir)


for x in carna_files:
    clustalfiles = os.path.join(carna_dir, x)
    stockfiles = os.path.join(stock_dir, x)
    stockfiles = stockfiles.replace('.clustalw', '.rnafold.tsv')
    cmd = "{script_file} --noLP {clustalfiles} > {stockfiles}".format(
        script_file = command,
        clustalfiles = clustalfiles,
        stockfiles = stockfiles

    )
    print(cmd)






