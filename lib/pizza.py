import ipdb

class Pizza:

    def __init__(self, name, ingredients, price=25.99):
    #    print(self)
    #   pirnt("new pizza added")
    #   print(name)
        self.name = name
        self.ingredients = ingredients
        self.price = price

    def get_name(self):
        return self.name

    def set_name(self, value):
        if type(value) == str:
            self.name = value
        else:
            raise TypeError

    name = property(get_name, set_name)

    # def set_name(self):
    #     self.name = "cheese pizza"


pepperoni_pizza = Pizza("Pepperoni Pizza", "Pepperoni, cheese", 24.99)
supreme_pizza = Pizza("Supreme Pizza", "Sausage, peppers, onions, cheese")

ipdb.set_trace()