










import os

dotaligner_high_dir = 'out/dotaligner/high/'
dotaligner_low_dir = 'out/dotaligner/low'


clustalw_high  = 'out/dotaligner/clustalw_high/'
clustalw_low = 'out/dotaligner/clustalw_low/'
script_file = '/home/xiuque/Projects/benchmark_analysis/src/benchmark_pipeline/src/dotaligner_to_clustalw.py'





dotaligner_files = os.listdir(dotaligner_high_dir)


for x in dotaligner_files:

    da_files = os.path.join(dotaligner_high_dir, x)
    da_low_files = os.path.join(dotaligner_low_dir, x)
    clustalw_high_files  = os.path.join(clustalw_high, x).replace('.dotaligner', '.clustalw')
    clustalw_low_files  = os.path.join(clustalw_low, x).replace('.dotaligner', '.clustalw')


    high_cmd = "{script_file} {da} {clustal}".format(
        script_file = script_file,
        da = da_files,
        clustal = clustalw_high_files

    )

    low_cmd = "{script_file} {da} {clustal}".format(
        script_file = script_file,
        da = da_low_files,
        clustal = clustalw_low_files

    )
    print(high_cmd)
    print(low_cmd)









