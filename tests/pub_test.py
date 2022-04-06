import unittest
from src.drink import Drink
from src.pub import Pub
from src.customer import Customer
from src.food import Food


class TestPub(unittest.TestCase):
    def setUp(self):
        drinks_list = [Drink("water", 2, 0, 100), Drink("gin and tonic", 5, 10, 20), Drink("beer", 3, 5, 50)]
        food_list = [Food("pizza", 15, 20, 5), Food("salad", 7, 50, 3)]
        self.pub = Pub("CodeClan Pub", 0, drinks_list, food_list)
        self.customer_example = Customer("John", 50, 0, 30)
        self.underage_customer = Customer("Josh", 100, 0, 16)
        self.drunk_customer = Customer("Bob", 40, 100, 23)

    # @unittest.skip("Delete this line to run the test")
    def test_pub_has_name(self):
        self.assertEqual("CodeClan Pub", self.pub.name)

    # @unittest.skip("Delete this line to run the test")
    def test_pub_amount_in_till(self):
        self.assertEqual(0, self.pub.till)

    # @unittest.skip("Delete this line to run the test")
    def test_find_drink_by_name(self):
        first_drink = self.pub.drinks_list[1]
        desired_drink = self.pub.find_item_by_name("gin and tonic")
        self.assertEqual(first_drink, desired_drink)

    # @unittest.skip("Delete this line to run the test")
    def test_find_drink_by_name__fail(self):
        desired_drink = self.pub.find_item_by_name("cider")
        self.assertEqual(None, desired_drink)

    # @unittest.skip("Delete this line to run the test")
    def test_find_item_by_name__drink(self):
        first_drink = self.pub.drinks_list[1]
        desired_item = self.pub.find_item_by_name("gin and tonic")
        self.assertEqual(first_drink, desired_item)

    # @unittest.skip("Delete this line to run the test")
    def test_find_item_by_name__food(self):
        first_food = self.pub.food_list[0]
        desired_item = self.pub.find_item_by_name("pizza")
        self.assertEqual(first_food, desired_item)


    # @unittest.skip("Delete this line to run the test")
    def test_add_money_to_till(self):
        self.pub.add_money_to_till(5)
        self.assertEqual(5, self.pub.till)

    # @unittest.skip("Delete this line to run the test")
    def test_customer_is_in_pub(self):
        self.assertEqual("John", self.customer_example.name)

    # @unittest.skip("Delete this line to run the test")
    def test_customer_is_over_18(self):
        customer_over_age = self.pub.customer_is_over_18(self.customer_example)
        self.assertEqual(True, customer_over_age)

    # @unittest.skip("Delete this line to run the test")
    def test_sell_drink_to_customer(self):
        desired_drink = self.pub.find_item_by_name("beer")
        self.pub.sell_drink_to_customer(desired_drink, self.customer_example)
        self.assertEqual(47, self.customer_example.wallet)
        self.assertEqual(3, self.pub.till)
        self.assertEqual(5, self.customer_example.drunkenness_level)

    # @unittest.skip("Delete this line to run the test")
    def test_sell_drink_to_customer__fail_age(self):
        desired_drink = self.pub.find_item_by_name("gin and tonic")
        self.pub.sell_drink_to_customer(desired_drink, self.underage_customer)
        self.assertEqual(100, self.underage_customer.wallet)
        self.assertEqual(0, self.pub.till)

    # @unittest.skip("Delete this line to run the test")
    def test_sell_drink_to_customer__fail_drunk(self):
        desired_drink = self.pub.find_item_by_name("beer")
        self.pub.sell_drink_to_customer(desired_drink, self.drunk_customer)
        self.assertEqual(40, self.drunk_customer.wallet)
        self.assertEqual(0, self.pub.till)