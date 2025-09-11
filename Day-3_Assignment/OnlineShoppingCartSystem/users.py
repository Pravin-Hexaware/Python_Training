class User:
    def __init__(self,name):
        self.name=name
        

    def show_total(self,cart):
        total = cart.calculate_total()
        print(f"{self.name} cart total: {total}")
