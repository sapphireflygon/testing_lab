import unittest
from src.food import Food


class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food("pizza", 15, 5)

    # @unittest.skip("Delete this line to run the test")
    def test_food_has_name(self):
        self.assertEqual("pizza", self.food.name)

    # @unittest.skip("Delete this line to run the test")
    def test_food_has_price(self):
        self.assertEqual(15, self.food.price)

    # @unittest.skip("Delete this line to run the test")
    def test_food_has_rejuvenation_level(self):
        self.assertEqual(5, self.food.rejuvenation_level)
    
