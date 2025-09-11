from users import User
from shopping import Cart as cart
from products import Products
from PremiumUser import PremiumUser


chocolate = Products("Chocolate", 1000, 3)
facewash = Products("Facewash", 50, 5)

amal = User("Amal", 101)
john = PremiumUser("John", 102)


amal.cart.addProduct(chocolate)
amal.cart.addProduct(facewash)
amal.cart.viewAllItems()
amal.show_total()


john.cart.addProduct(chocolate)
john.cart.viewAllItems()
john.show_total()

amal.cart.removeProduct(facewash)
amal.cart.viewAllItems()
amal.show_total()
