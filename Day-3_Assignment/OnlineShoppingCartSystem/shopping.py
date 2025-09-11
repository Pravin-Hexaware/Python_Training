class Cart:
    def __init__(self,id):
        self.id=id
        self.user_products=[]
    def addProducts(self,product):
        if(product.stock_quantity>0):
            self.user_products.append(product)
            product.stock_quantity-=1
            print("product added")
        else:
            print("product not added stock empty")
    

    def removeProducts(self,product):
        if product in self.user_products:
            self.user_products.remove(product)
            product.stock_quantity+=1
            print("product removed")
        else:
            print("product deleted")

    
    def viewAllItems(self):
        for item in self.user_products:
            print("items:",item)
    
    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total

            

    
