#Allow user 3 login attempts. Raise PermissionError if login fails 3 times.
#Requirement:
#Use a loop with exception raising
#Use break if login is successful

correct_username = "admin"
correct_password = "1234"
attempts = 3
for attempt in range(1, attempts + 1):
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == correct_username and password == correct_password:
        print("Login successful ✅")
        break
    else:
        print(f"Incorrect credentials. Attempts left: {attempts - attempt}")
    if attempt == attempts:
        raise PermissionError("Login failed 3 times. Access denied.")
