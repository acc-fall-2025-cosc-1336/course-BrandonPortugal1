import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from src.homework.b_in_proc_out.output import multiply_numbers
import unittest

class TestMultiplyNumbers(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(multiply_numbers(7, 7), 49)
        self.assertEqual(multiply_numbers(5, 5), 25)

    def test_zero(self):
        self.assertEqual(multiply_numbers(0, 10), 0)

    def test_negative_numbers(self):
        self.assertEqual(multiply_numbers(-3, 5), -15)
        self.assertEqual(multiply_numbers(-3, -5), 15)

if __name__ == '__main__':
    unittest.main()
