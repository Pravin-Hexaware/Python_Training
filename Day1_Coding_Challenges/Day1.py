name=input("Enter your name: ")
age=14
grade=input("Enter your grade: ")
def show_info():
    print("Student Name:",name,", Age:",age,", Grade:",grade)
show_info()






item1=int(input("Enter price of item 1: "))
item2=int(input("Enter price of item 2: "))
item3=int(input("Enter price of item 3: "))
total=item1+item2+item3
if total>100:
    discount=total*10/100
    final=total-discount
    print("Cart Total:",total)
    print("Discount Applied:",discount)
    print("Final Total:",final)
else:
    print("Cart Total:",total)
    print("No Discount Applied")
    print("Final Total:",total)






def check_number(n):
    if n%2==0:
        print("Number",n,"is Even")
    else:
        print("Number",n,"is Odd")

num=int(input("Enter a number: "))
check_number(num)





celsius = float(input("Enter temperature in Celsius: "))
fahrenheit_result = celsius * 9 / 5 + 32
print(str(celsius) + "C = " + str(round(fahrenheit_result, 1)) + "F")
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius_result = (fahrenheit - 32) * 5 / 9
print(str(fahrenheit) + "F = " + str(round(celsius_result, 2)) + "C")




num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
add_result = num1 + num2
sub_result = num1 - num2
mul_result = num1 * num2
div_result = num1 / num2
print("Add:", add_result)
print("Subtract:", sub_result)
print("Multiply:", mul_result)
print("Divide:", div_result)






balance = 1000
deposit_amount = float(input("Enter amount to deposit: "))
balance = balance + deposit_amount
print("Balance:", balance)
withdraw_amount = float(input("Enter amount to withdraw: "))
if withdraw_amount <= balance:
    balance = balance - withdraw_amount
    print("Balance:", balance)
else:
    print("Insufficient funds! Balance:", balance)






n = int(input("Enter first number: "))
m = int(input("Enter second number: "))
product = n * m
i = 1
is_perfect_square = False
while i * i <= product:
    if i * i == product:
        is_perfect_square = True
        break
    i = i + 1
if is_perfect_square:
    print("yes")
else:
    print("no")






n = int(input("Enter first number: "))
m = int(input("Enter second number: "))
sum = n + m
if sum % 2 == 0:
    print("even")
else:
    print("odd")






numbers = input("Enter 10 numbers separated by space: ").split()
min_value = int(numbers[0])
i = 1
while i < 10:
    current = int(numbers[i])
    if current < min_value:
        min_value = current
    i = i + 1
print(min_value)







n = int(input())
numbers = input().split()
min_value = int(numbers[0])
max_value = int(numbers[0])
min_index = 1
max_index = 1
i = 1
while i < n:
    current = int(numbers[i])
    if current < min_value:
        min_value = current
        min_index = i + 1
    if current > max_value:
        max_value = current
        max_index = i + 1
    i = i + 1
print(min_index, max_index)









n = int(input("Enter first number: "))
m = int(input("Enter second number: "))
if n == 0 or m == 0:
    print(-1)
else:
    i = 1
    gcd = 1
    while i <= n and i <= m:
        if n % i == 0 and m % i == 0:
            gcd = i
        i = i + 1
    print(gcd)





k = int(input("Enter a number: "))
sum = 0
i = 1
while i <= k:
    sum = sum + i
    i = i + 1
print(sum)






n = int(input())
l = int(input())
r = int(input())
if n > l and n < r:
    print("yes")
else:
    print("no")








n = int(input())
temp = n
sum_digits = 0
product_digits = 1
while temp > 0:
    digit = temp % 10
    sum_digits = sum_digits + digit
    product_digits = product_digits * digit
    temp = temp // 10
if sum_digits + product_digits == n:
    print("Great")
else:
    print("no")


