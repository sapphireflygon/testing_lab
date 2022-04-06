class Customer:
    def __init__(self, input_name, input_wallet, input_drunkenness_level, input_age):
        self.name = input_name
        self.wallet = input_wallet
        self.drunkenness_level = input_drunkenness_level
        self.age = input_age
    
    def remove_money_from_customer(self, amount):
        self.wallet -= amount
    
    def add_to_customer_drunkenness(self, alcohol_level):
        self.drunkenness_level += alcohol_level