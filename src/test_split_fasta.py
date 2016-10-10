


import unittest
from unittest import mock
from unittest.mock import patch, MagicMock


from split_fasta import split_fasta, gather_fasta_sequences

class TestSplitFasta(unittest.TestCase):

    def setUp(self):

        self.fasta_file_content  = [

            '>seq_a' ,
            'ATGC',
            '>seq_b',
            'ATGA'
        ]

        self.fasta_sequences = {
            'seq_a' : 'ATGC',
            'seq_b' : 'ATGA'
        }


        self.fasta_sequences_b = {
            'seq_a' : 'ATGC',
            'seq_c' : 'GGGG'
        }

        self.fasta_sequences_combined = {
            'seq_a' : 'ATGC',
            'seq_b' : 'ATGA',
            'seq_c' : 'GGGG'

        }








    def test_split_fasta(self):
        m = mock.mock_open(read_data= "\n".join(self.fasta_file_content))
        with mock.patch('builtins.open' , m) :
            results = split_fasta('random_fasta_file')
        self.assertDictEqual(results, self.fasta_sequences)






    def test_gather_fasta_sequences(self):
        sequences_file_content = "fileA\nfileB"
        m = mock.mock_open(read_data=sequences_file_content)

        values = {
            'fileA' : self.fasta_sequences,
            'fileB' : self.fasta_sequences_b
        }

        def side_effects(arg):
            return values[arg]

        with mock.patch('builtins.open' , m) :
            with mock.patch('split_fasta.split_fasta') as split_fasta_m:
                split_fasta_m.side_effect = side_effects


                results = gather_fasta_sequences('sequence_file')

        self.assertDictEqual(results, self.fasta_sequences_combined)






















if __name__ == '__main__':
    unittest.main()
