import unittest
from src.homework.e_functions.value_return_functions import get_gross_pay, get_fica_tax, get_federal_tax

class TestPayrollFunctions(unittest.TestCase):

    def test_regular_hours(self):
        self.assertEqual(get_gross_pay(40, 10), 400)
        self.assertAlmostEqual(get_fica_tax(400), 30.6, places=2)
        self.assertAlmostEqual(get_federal_tax(400), 32.0, places=2)

    def test_overtime_hours(self):
        self.assertEqual(get_gross_pay(45, 10), 475)
        self.assertAlmostEqual(get_fica_tax(475), 36.34, places=2)
        self.assertAlmostEqual(get_federal_tax(475), 38.0, places=2)

    def test_under_40_hours(self):
        self.assertEqual(get_gross_pay(30, 10), 300)
        self.assertAlmostEqual(get_fica_tax(300), 22.95, places=2)
        self.assertAlmostEqual(get_federal_tax(300), 24.0, places=2)



