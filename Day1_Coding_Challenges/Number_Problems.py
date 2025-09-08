
num = int(input("Enter a number: "))
num_str = str(num)
length = len(num_str)
if length % 2 == 0:
    first = int(num_str[:length // 2])
    second = int(num_str[length // 2:])
    total = first+ second
    if total*total==num:
        print("Tech Number")
    else:
        print("Not a Tech Number")
else:
    print("Not a Tech Number")




num = int(input("Enter a number: "))
temp = num
total = 0

while temp > 0:
    digit = temp % 10
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    total += fact
    temp //= 10

if total == num:
    print("Peterson Number")
else:
    print("Not a Peterson Number")





num = int(input("Enter a number: "))
next_num = num + 1
is_square = False
for i in range(1, next_num + 1):
    if i * i == next_num:
        is_square = True
        break

if is_square:
    print("Sunny Number")
else:
    print("Not a Sunny Number")




num = int(input("Enter a number: "))
temp = num
sum_digits = 0
product_digits = 1

while temp > 0:
    digit = temp % 10
    sum_digits += digit
    product_digits *= digit
    temp //= 10

if sum_digits == product_digits:
    print("Spy Number")
else:
    print("Not a Spy Number")





num = int(input("Enter a number: "))
square = num * num
total = 0
while square > 0:
    digit = square % 10
    total += digit
    square //= 10
if total == num:
    print("Neon Number")
else:
    print("Not a Neon Number")





num = int(input("Enter a number: "))
temp = num
digits = []
count = 0
while temp > 0:
    count += 1
    digits.insert(0, temp % 10)
    temp //= 10
sequence = digits[:]
while True:
    next_term = 0
    for i in range(count):
        next_term += sequence[len(sequence) - count + i]
    if next_term == num:
        print("Keith Number")
        break
    elif next_term > num:
        print("Not a Keith Number")
        break
    sequence.append(next_term)






def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def reverse_number(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev
num = int(input("Enter a number: "))
rev_num = reverse_number(num)
if is_prime(num) and is_prime(rev_num) and num != rev_num:
    print("Emirp Number")
else:
    print("Not an Emirp Number")





num = int(input("Enter a number: "))

if num % 10 == 7 or num % 7 == 0:
    print("Buzz Number")
else:
    print("Not a Buzz Number")
