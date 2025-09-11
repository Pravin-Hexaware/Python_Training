class Products:
    def __init__(self,name,price,stock_quantity):
        self.name=name
        self.price=price
        self.stock_quantity=stock_quantity
    
    def display_products(self):
        print(f" Product name: {self.name}, Price: {self.price},Quantity: {self.stock_quantity} ")


