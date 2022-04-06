import unittest
from src.customer import Customer


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("John", 50)

    # @unittest.skip("Delete this line to run the test")
    def test_customer_has_name(self):
        self.assertEqual("John", self.customer.name)

    # @unittest.skip("Delete this line to run the test")
    def test_customer_amount_in_wallet(self):
        self.assertEqual(50, self.customer.wallet)

    