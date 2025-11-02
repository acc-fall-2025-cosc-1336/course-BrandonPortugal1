import sys
from pathlib import Path
# ensure project root is on sys.path so "h_strings" can be imported when running tests
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

import unittest
from src.homework.h_strings.strings import get_hamming_distance, get_dna_complement

class Test_Config(unittest.TestCase):

    def test_get_hamming_distance(self):
        result = get_hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT")
        self.assertEqual(result, 7)

    def test_get_dna_complement(self):
        result = get_dna_complement("AAAACCCGGT")
        self.assertEqual(result, "ACCGGGTTTT")