#check if a password has at least 8 character,one uppercase,one number

def is_valid_password(password):
    if len(password) < 8:
        return False
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    return has_upper and has_digit
password = input("Enter a password: ")
if is_valid_password(password):
    print("Valid password")
else:
    print("Invalid password")

