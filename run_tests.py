import unittest
'''
The file in /tests/homework/e_functions/test_functions.py
has the test functions
'''
from tests.homework.e_functions import test_functions

suite = unittest.TestLoader().loadTestsFromModule(test_functions)
unittest.TextTestRunner(verbosity=2).run(suite)