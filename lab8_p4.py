#Accept a password and check if it's at least 8 characters long. If not, raise an exception.
#Requirement:
#Use raise ValueError("Weak password")
#Use try-except block to catch and print custom message


try:
    password = input("Enter your password: ")
    if len(password) < 8:
        raise ValueError("Weak password")  
    print("Password accepted ")
except ValueError as e:
    print("Error:", e)
