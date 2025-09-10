import cart as ca
import payment as p
print(p.simulate_payment())
print("---------------")
print("1.Add item")
print("2.Remove item")
print("3.Total Items")
print("---------------")
choice=int(input("Enter the choice:"))
while True:
    choice=int(input("Enter the choice:"))
    if(choice==1):
        key=int(input("Enter the value of key:"))
        value=input("Enter the value:")
        print(ca.addItems(key,value))
    elif(choice==2):
         key=int(input("Enter the value of key:"))
         print(ca.removeItems(key))
    elif(choice==3):
        print("Total Items: ",ca.totalItems())
    else:
        break

