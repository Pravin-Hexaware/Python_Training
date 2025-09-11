class FoodItem:
    def __init__(self, name, price, available=True):
        self.name = name
        self.price = price
        self.available = available

    def display(self):
        print(f" name:{self.name} price:{self.price}")