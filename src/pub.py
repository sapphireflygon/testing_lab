class Pub:
    def __init__(self, input_name, input_till, input_drinks_list, input_food_list):
        self.name = input_name
        self.till = input_till
        self.drinks_list = input_drinks_list
        self.food_list = input_food_list

    def find_item_by_name(self, item_name):
        for item in self.drinks_list:
            if item_name == item.name:
                return item

        for item in self.food_list:
            if item_name == item.name:
                return item
    
    def add_money_to_till(self, amount):
        self.till += amount

    def customer_is_over_18(self, customer):
        if customer.age >= 18:
            return True

    def sell_item_to_customer(self, desired_item, customer):
        desired_item_data = self.find_item_by_name(desired_item)

        if desired_item_data != None:
            if hasattr(desired_item_data, "is_drink") == True:
                if self.customer_is_over_18(customer) == True and customer.drunkenness_level <= 20:
                    customer.add_to_customer_drunkenness(desired_item_data.alcohol_level)
                else:
                    return
            else:
                customer.drunkenness_level -= desired_item_data.rejuvenation_level
            
            customer.remove_money_from_customer(desired_item_data.price)
            self.add_money_to_till(desired_item_data.price)

