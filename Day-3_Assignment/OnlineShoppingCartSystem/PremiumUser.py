from users import User
class PremiumUser(User):
    def show_total(self,cart):
        total = cart.calculate_total()
        discount = total * 0.10
        final_total = total - discount
        print(f"{User.name} with discount is {final_total}")

