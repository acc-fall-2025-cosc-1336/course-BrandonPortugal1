import unittest

'''
The file at /src/homework/b_in_proc_out/output has 
the function get_number.
'''
from src.homework.b_in_proc_out.output import get_number

class Test_Config(unittest.TestCase):

    def test_get_number_1(self):
        #test that the function get_number returns 1
        self.assertEqual(1, get_number(1))
    
    def test_get_number_2(self):
        #test that the function get_number returns 2
        self.assertEqual(2, get_number(2))

import unittest
from src.homework.b_in_proc_out.output import get_number, multiply_numbers

class TestMultiplyNumbers(unittest.TestCase):
    def test_multiply_positive(self):
        self.assertEqual(multiply_numbers(get_number(7), get_number(7)), 49)
        self.assertEqual(multiply_numbers(get_number(5), get_number(5)), 25)

    def test_get_number(self):
        self.assertEqual(get_number(10), 10)
        self.assertEqual(get_number(-3), -3)

if __name__ == '__main__':
    unittest.main()

