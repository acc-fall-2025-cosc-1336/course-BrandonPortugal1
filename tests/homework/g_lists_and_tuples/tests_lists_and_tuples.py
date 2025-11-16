import os
import sys
import unittest

# ensure the top-level "src" folder is importable when running tests from the tests directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'src')))

from homework.g_lists_and_tuples.lists import get_p_distance, get_p_distance_matrix

class Test_Config(unittest.TestCase):

    def test_p_distance(self):
        list1 = ['T','T','T','C','C','A','T','T','T','A']
        list2 = ['G','A','T','T','C','A','T','T','T','C']

        result = get_p_distance(list1, list2)
        self.assertAlmostEqual(result, 0.4, places=3)

    def test_get_p_distance_matrix(self):
        dna_lists = [
            ['T','T','T','C','C','A','T','T','T','A'],
            ['G','A','T','T','C','A','T','T','T','C'],
            ['T','T','T','C','C','A','T','T','T','T'],
            ['G','T','T','C','C','A','T','T','T','A']
        ]

        expected = [
            [0.0, 0.4, 0.1, 0.1],
            [0.4, 0.0, 0.4, 0.3],
            [0.1, 0.4, 0.0, 0.2],
            [0.1, 0.3, 0.2, 0.0]
        ]

        result = get_p_distance_matrix(dna_lists)

        for i in range(4):
            for j in range(4):
                self.assertAlmostEqual(result[i][j], expected[i][j], places=3)