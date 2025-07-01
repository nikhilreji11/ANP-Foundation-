#Using input function take two number and then swap the number
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
print(f"Before swapping: a = {a}, b = {b}")
a, b = b, a
print(f"After swapping: a = {a}, b = {b}")
