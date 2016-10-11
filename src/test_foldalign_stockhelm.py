import unittest
from unittest import mock
from foldalign_stockhelm import get_align_lines, get_alignments

class MyTestCase(unittest.TestCase):
    def test_get_align_lines(self):
        entry = """
; REALIGNING          (1 51, 1 51)
; FOLDALIGN           2.1.1
; REFERENCE           J.H. Havgaard, E. Torarinsson and J. Gorodkin
; REFERENCE           Fast pairwise local structural RNA alignments by pruning
; REFERENCE           of the dynamical programming matrix
; REFERENCE           PLOS computational biology, 2007
; ALIGNMENT_ID        n.a.
; ALIGNING            AB001040.1_156-206 against D14484.1_9261-9311
; SEQUENCE_1_COMMENT
; SEQUENCE_2_COMMENT
; ALIGN
; ALIGN               Score: 1269
; ALIGN               Identity: 94 % ( 48 / 51 )
; ALIGN
; ALIGN               AB001040.1_15 Begin 1
; ALIGN               D14484.1_9261 Begin 1
; ALIGN
; ALIGN               AB001040.1_15 UACAGCGGGG GAGACAUAUA UCACAGCCUG UCUCGCGCCC
; ALIGN               Structure     ..(((((((( ..((((.... ........)) ))(((....)
; ALIGN               D14484.1_9261 UACAGUGGGG GAGACAUAUA UCACAGCCUG UCUCGUGCCC
; ALIGN
; ALIGN               AB001040.1_15 GACCCUGCUG G
; ALIGN               Structure     )))))))))) .
; ALIGN               D14484.1_9261 GACCCCGCUG G
; ALIGN
; ALIGN               AB001040.1_15 End 51
; ALIGN               D14484.1_9261 End 51
; ==============================================================================
"""

        expected =["; ALIGN               AB001040.1_15 UACAGCGGGG GAGACAUAUA UCACAGCCUG UCUCGCGCCC",
         "; ALIGN               Structure     ..(((((((( ..((((.... ........)) ))(((....)",
         "; ALIGN               D14484.1_9261 UACAGUGGGG GAGACAUAUA UCACAGCCUG UCUCGUGCCC",
         "; ALIGN",
         "; ALIGN               AB001040.1_15 GACCCUGCUG G",
         "; ALIGN               Structure     )))))))))) .",
         "; ALIGN               D14484.1_9261 GACCCCGCUG G"

         ]

        m = mock.mock_open(read_data=entry)
        with mock.patch('builtins.open', m):
            self.assertEqual(expected, get_align_lines(m))

    def test_get_alignments(self):

        align_lines =["; ALIGN               seqA UACAGCGGGG GAGACAUAUA UCACAGCCUG UCUCGCGCCC",
         "; ALIGN               Structure     ..(((((((( ..((((.... ........)) ))(((....)",
         "; ALIGN               seqB UACAGUGGGG GAGACAUAUA UCACAGCCUG UCUCGUGCCC",
         "; ALIGN",
         "; ALIGN               seqA GACCCUGCUG G",
         "; ALIGN               Structure     )))))))))) .",
         "; ALIGN               seqB GACCCCGCUG G"

         ]

        sequence_id,complete_sequence_a, complete_sequence_b, consenses_structure = get_alignments(align_lines)

        self.assertEqual(sequence_id ,'seqA_vs_seqB')
        self.assertEqual(complete_sequence_a, "UACAGCGGGGGAGACAUAUAUCACAGCCUGUCUCGCGCCCGACCCUGCUGG")
        self.assertEqual(complete_sequence_b, "UACAGUGGGGGAGACAUAUAUCACAGCCUGUCUCGUGCCCGACCCCGCUGG")
        self.assertEqual(consenses_structure, "..((((((((..((((............))))(((....))))))))))).")
















if __name__ == '__main__':
    unittest.main()
