from user import User

class PremiumUser(User):
    def show_total(self):
        total = self.order.calculate_total()
        discount = total * 0.15
        final_total = total - discount
        print(f"{self.name} amount is: {final_total}")