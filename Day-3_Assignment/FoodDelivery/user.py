from order import Order

class User:
    def __init__(self, name):
        self.name = name
        self.order = Order()

    def show_total(self):
        total = self.order.calculate_total()
        print(f" Total cost: {total}")