import unittest
from src.drink import Drink



class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("water", 2, 100, 0)

    # @unittest.skip("Delete this line to run the test")
    def test_drink_name(self):
        self.assertEqual("water", self.drink.name)

    # @unittest.skip("Delete this line to run the test")
    def test_drink_has_price(self):
        self.assertEqual(2, self.drink.price)

    # @unittest.skip("Delete this line to run the test")
    def test_drink_has_stock(self):
        self.assertEqual(100, self.drink.stock)

    # @unittest.skip("Delete this line to run the test")
    def test_drink_has_alcohol_level(self):
        self.assertEqual(0, self.drink.alcohol_level)