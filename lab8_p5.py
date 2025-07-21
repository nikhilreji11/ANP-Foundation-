# a custom exception class NegativeNumberError and raise it if user inputs a negative number.
#Requirement:
#Define your own exception class
#Handle it using try-except


class NegativeNumberError(Exception):
    pass
try:
    num = int(input("Enter a positive number: "))
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")  
    print("You entered:", num)
except NegativeNumberError as e:
    print("Error:", e)
except ValueError:
    print("Error: Please enter a valid integer.")

