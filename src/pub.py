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

    