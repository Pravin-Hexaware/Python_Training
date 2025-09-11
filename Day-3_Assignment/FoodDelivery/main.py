from food_items import FoodItem
from user import User
from premium_user import PremiumUser


pizza = FoodItem("Pizza", 500)
burger = FoodItem("Burger", 250)
sushi = FoodItem("Sushi", 300, available=False)


john = User("John")
amal = PremiumUser("Amal")


john.order.add_item(pizza)
john.order.add_item(burger)
john.order.remove_item("Burger")
john.show_total()


amal.order.add_item(pizza)
amal.order.add_item(sushi)  
amal.show_total()