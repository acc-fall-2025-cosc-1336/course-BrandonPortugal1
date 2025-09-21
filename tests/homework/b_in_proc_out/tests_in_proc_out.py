import sys
import os
import unittest


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../src/homework/b_in_proc_out')))


from output import get_sales_tax_amount, get_tip_amount

class TestRestaurantBill(unittest.TestCase):

    def test_get_sales_tax_amount(self):
        self.assertAlmostEqual(get_sales_tax_amount(20), 1.35)
        self.assertAlmostEqual(get_sales_tax_amount(100), 6.75)

    def test_get_tip_amount(self):
        self.assertAlmostEqual(get_tip_amount(20, 15), 3.0)
        self.assertAlmostEqual(get_tip_amount(100, 20), 20.0)

if __name__ == "__main__":
    unittest.main()