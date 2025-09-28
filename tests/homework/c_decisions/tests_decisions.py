import unittest
from homework.c_decisions.decisions import get_letter_grade, get_letter_grade_switch

class TestDecisions(unittest.TestCase):
    def test_get_letter_grade(self):
        self.assertEqual(get_letter_grade(95), 'A')
        self.assertEqual(get_letter_grade(85), 'B')
        self.assertEqual(get_letter_grade(75), 'C')
        self.assertEqual(get_letter_grade(65), 'D')
        self.assertEqual(get_letter_grade(50), 'F')

    def test_get_letter_grade_switch(self):
        self.assertEqual(get_letter_grade_switch(95), 'A')
        self.assertEqual(get_letter_grade_switch(85), 'B')
        self.assertEqual(get_letter_grade_switch(75), 'C')
        self.assertEqual(get_letter_grade_switch(65), 'D')
        self.assertEqual(get_letter_grade_switch(50), 'F')

if __name__ == '__main__':
    unittest.main()