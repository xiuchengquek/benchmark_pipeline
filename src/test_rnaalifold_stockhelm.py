import unittest
from unittest import mock


from rnaalifold_stockhelm import parse_rna_alifold, parse_clustalw_without_structure


class MyTestCase(unittest.TestCase):
    def test_parse_rna_alifold(self):
        m = mock.mock_open(read_data='__GAGAGA__\n..((..)).. (-22.0 = -3 + 2)\n')
        with mock.patch('builtins.open', m):


            structure = parse_rna_alifold(m)

        self.assertEqual('..((..))..', structure)

    def test_parse_clustalw_without_structure(self):
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


        sequence_id, complete_sequence_a, complete_sequence_b = parse_clustalw_without_structure(m)

        self.assertEqual(sequence_id, 'SeqA_vs_SeqB')
        self.assertEqual(complete_sequence_a, 'UACAUACT')





if __name__ == '__main__':
    unittest.main()
