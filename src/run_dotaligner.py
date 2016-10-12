




import sys
import os


pairwise_alignment = sys.argv[1]
high_parameters = sys.argv[2]
low_parameters = sys.argv[3]
dotaligner = '/share/ClusterShare/software/contrib/marsmi/dotaligner_0.3/DotAligner'



high_fh = open(high_parameters, 'w')
low_fh = open(low_parameters, 'w')





#T-5_s-1_k-0.5_t-0.8_o-1_e-0.05
#T-10_s-1_k-0.3_t-0.5_o-1_e-0.05




with open(pairwise_alignment) as f:
    for line in f:
        line = line.strip()
        fields = line.split()
        seq_a = fields[1]
        seq_b = fields[2]

        seq_pair = "%s_vs_%s.dotaligner" % (seq_a, seq_b)
        seq_a_pp_file = "data/ps/ps/%s_dp.pp" % seq_a
        seq_b_pp_file = "data/ps/ps/%s_dp.pp" % seq_b

        out_high = os.path.join('out/dotaligner/high/', seq_pair)
        out_low = os.path.join('out/dotaligner/low/', seq_pair)


        high_cmd = '{dotaligner} -T 5 -s 1 -k 0.5 -t 0.8 -o 1 -e 0.05 -d {seq_a} -d {seq_b} > {out}'.format(
            dotaligner = dotaligner,
            seq_a = seq_a_pp_file,
            seq_b = seq_b_pp_file,
            out = out_high
        )


        low_cmd = '{dotaligner} -T 10 -s 1 -k 0.3 -t 0.5 -o 1 -e 0.05 -d {seq_a} -d {seq_b} > {out}'.format(
            dotaligner = dotaligner,
            seq_a = seq_a_pp_file,
            seq_b = seq_b_pp_file,
            out = out_low
        )

        high_fh.write("%s\n" % high_cmd)
        low_fh.write("%s\n" % low_cmd)



high_fh.close()
low_fh.close()
















