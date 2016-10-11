import os

carna_dir = 'out/carna/clustalw'
stock_dir  = 'out/carna/stock/'
command  = 'RNAalifold'




carna_files = os.listdir(carna_dir)


for x in carna_files:
    clustalfiles = os.path.join(carna_dir, x)
    stockfiles = os.path.join(stock_dir, x)
    cmd = "{script_file} {clustalfiles} > {stockfiles}".format(
        script_file = command,
        clustalfiles = clustalfiles,
        stockfiles = stockfiles

    )
    print(cmd)






