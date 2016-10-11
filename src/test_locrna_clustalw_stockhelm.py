import unittest
from unittest import mock


from locrna_clustalw_stockhelm import fill_consensus_sequenece, parse_stockholm, parse_clustalw

class TestClustalWStockhelm(unittest.TestCase):


    def test_parse_clustalw(self):

        return_value =  [
            "                           ....",
            "SeqA         UACA",
            "SeqB          UACA",
            "                           ....",
            "",
            "                           ....",
            "SeqA         UACT",
            "SeqB          UACT",
            "                           ...."
        ]

        m = iter(return_value)


        sequence_id, consensus_structure, complete_sequence_a, complete_sequence_b = parse_clustalw(m)

        self.assertEqual(sequence_id, 'SeqA_vs_SeqB')
        self.assertEqual(complete_sequence_a, 'UACAUACT')
        self.assertEqual(consensus_structure, '........')




    def test_fill_consensus_sequence(self):
        sequenceA = 'ATGAGAGAGA-AGAGAG-AGAGAGACATG'
        sequenceB = '-AGAGAGAAGTTAGUAGTTA-ATCGCGGC'
        expected_consensus = 'ATGAGAGAGATAGAGAGTAGAGAGACATG'
        consensus_sequence = fill_consensus_sequenece(sequenceA, sequenceB)
        self.assertEqual(expected_consensus, consensus_sequence)

    def test_stockhom_sequence(self):
        sequence = 'ATGCATGC'
        structure = '........'
        seq_id = 'seqA'

        expected = """\
# STOCKHOLM 1.0
#=GR seqA SS ........
seqA ATGCATGC
//"""
        results = parse_stockholm(seq_id, sequence, structure)
        self.assertEqual(results, expected)





















if __name__ == '__main__':
    unittest.main()
