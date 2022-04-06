class Pub:
    def __init__(self, input_name, input_till, input_drinks_list):
        self.name = input_name
        self.till = input_till
        self.drinks_list = input_drinks_list

    def find_drink_by_name(self, drink_name):
        for drink in self.drinks_list:
            if drink_name == drink.name:
                return drink
    
    def add_money_to_till(self, amount):
        self.till += amount

    def customer_is_over_18(self, customer):
        if customer.age >= 18:
            return True

    def sell_drink_to_customer(self, desired_drink, customer):
        if self.customer_is_over_18(customer) == True:
            customer.remove_money_from_customer(desired_drink.price)
            self.add_money_to_till(desired_drink.price)

    