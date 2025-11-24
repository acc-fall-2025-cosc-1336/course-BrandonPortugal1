import unittest
from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory_widget


class Test_Config(unittest.TestCase):

    def test_add_inventory(self):
        inventory = {}

        # Add Widget1 with quantity 10
        add_inventory(inventory, "Widget1", 10)
        self.assertEqual(inventory["Widget1"], 10)

        # Update Widget1 with +25 → total should be 35
        add_inventory(inventory, "Widget1", 25)
        self.assertEqual(inventory["Widget1"], 35)

        # Add negative amount: -10 → total should be 25
        add_inventory(inventory, "Widget1", -10)
        self.assertEqual(inventory["Widget1"], 25)

    def test_remove_inventory_widget(self):
        inventory = {}

        # Add two widgets
        add_inventory(inventory, "widget1", 10)
        add_inventory(inventory, "widget2", 20)

        # Remove widget1
        result = remove_inventory_widget(inventory, "widget1")
        self.assertEqual(result, "Record deleted")

        # Only widget2 should remain
        self.assertEqual(len(inventory), 1)
        self.assertIn("widget2", inventory)


if __name__ == '__main__':
    unittest.main()