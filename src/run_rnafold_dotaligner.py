import os

clustalw_high = 'out/dotaligner/clustalw_high/'
clustalw_low = 'out/dotaligner/clustalw_low/'
high_da  = 'out/dotaligner/rnaalifold_high/'
low_da  = 'out/dotaligner/rnaalifold_low/'

command  = 'RNAalifold'




clustalw_high_files = os.listdir(clustalw_high)


for x in clustalw_high_files:


    high_files = os.path.join(clustalw_high, x)
    high_rnaali = os.path.join(high_da, x).replace('.clustalw', '.rnafold.tsv')


    low_files = os.path.join(clustalw_low, x)
    low_rnaali = os.path.join(low_da, x).replace('.clustalw', '.rnafold.tsv')



    hi_cmd = "{script_file} --noLP {clustalfiles} > {stockfiles}".format(
        script_file = command,
        clustalfiles = high_files,
        stockfiles = high_rnaali

    )

    low_cmd = "{script_file} --noLP {clustalfiles} > {stockfiles}".format(
        script_file = command,
        clustalfiles = low_files,
        stockfiles = low_rnaali

    )
    print(hi_cmd)
    print(low_cmd)







