import unittest
from src.customer import Customer


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("John", 50, 0, 30)

    # @unittest.skip("Delete this line to run the test")
    def test_customer_has_name(self):
        self.assertEqual("John", self.customer.name)

    # @unittest.skip("Delete this line to run the test")
    def test_customer_amount_in_wallet(self):
        self.assertEqual(50, self.customer.wallet)

    # @unittest.skip("Delete this line to run the test")
    def test_remove_money_from_customer(self):
        self.customer.remove_money_from_customer(5)
        self.assertEqual(45, self.customer.wallet)

    # @unittest.skip("Delete this line to run the test")
    def test_customer_drunkenness_level(self):
        self.assertEqual(0, self.customer.drunkenness_level)

    # @unittest.skip("Delete this line to run the test")
    def test_customer_age(self):
        self.assertEqual(30, self.customer.age)