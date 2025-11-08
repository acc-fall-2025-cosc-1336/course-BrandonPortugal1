import unittest
import os
import sys
# ensure repository root is on sys.path so `src` can be imported when running tests directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))
from src.homework.g_lists_and_tuples.lists import get_lowest_list_value, get_highest_list_value

class TestListFunctions(unittest.TestCase):

    def test_get_lowest_list_value(self):
        data = [8, 10, 1, 50, 20]
        result = get_lowest_list_value(data)
        self.assertEqual(result, 1)

    def test_get_highest_list_value(self):
        data = [8, 10, 1, 50, 20]
        result = get_highest_list_value(data)
        self.assertEqual(result, 50)

if __name__ == '__main__':
    unittest.main()