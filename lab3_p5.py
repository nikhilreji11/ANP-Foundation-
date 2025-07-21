#extract domain from email(user@example.com)

def extract_domain(email):
    return email.split("@")[1]
email = input("Enter an email address: ")
domain = extract_domain(email)
print("Domain is:", domain)
