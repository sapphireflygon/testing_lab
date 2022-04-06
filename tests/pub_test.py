import unittest
from src.drink import Drink
from src.pub import Pub
from src.customer import Customer


class TestPub(unittest.TestCase):
    def setUp(self):
        drinks_list = [Drink("water", 2, 100), Drink("gin and tonic", 5, 20)]
        self.pub = Pub("CodeClan Pub", 0, drinks_list)

    @unittest.skip("Delete this line to run the test")
    def test_pub_has_name(self):
        self.assertEqual("CodeClan Pub", self.pub.name)

    @unittest.skip("Delete this line to run the test")
    def test_pub_amount_in_till(self):
        self.assertEqual(0, self.pub.till)

    @unittest.skip("Delete this line to run the test")
    def test_pub_has_drink(self):
        pass