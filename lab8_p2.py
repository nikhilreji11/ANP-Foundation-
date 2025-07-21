#Take an email input. If it doesn’t contain "@" and ".", raise a ValueError.
#Requirement:
#Custom message: "Invalid email format"

def check_email():
    try:
        email = input("Enter your email: ")
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email format")
        print("Valid email!")
    except ValueError as e:
        print("Error:", e)
check_email()
