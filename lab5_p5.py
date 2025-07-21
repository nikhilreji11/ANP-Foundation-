#Write a Python program to create a simple billing system for a shop using tuples.
#The program should:
#Ask the user how many products they want to enter.
#For each product, take the following inputs:
#Product name (string)
#Product price (float)
#Quantity purchased (integer)
#Store each product's information as a tuple: (product_name, price, quantity).
#Store all product tuples in a list.
#After collecting all data, display a detailed bill, showing:
#Product name
#Price per unit
#Quantity
#Total amount for each product (price × quantity)
#Finally, display the total bill amount for all products
#Expected output:
#Enter number of products: 2
#Enter name of product 1: Pen
#Enter price of Pen: 10
#Enter quantity of Pen: 5
#Enter name of product 2: Notebook
#Enter price of Notebook: 40
#Enter quantity of Notebook: 2
#--- BILL DETAILS ---
#Pen: ₹10.0 x 5 = ₹50.0
#Notebook: ₹40.0 x 2 = ₹80.0
#Total Amount to Pay: ₹130.0


products = []
num_products = int(input("Enter number of products: "))
for i in range(1, num_products + 1):
    name = input(f"Enter name of product {i}: ")
    price = float(input(f"Enter price of {name}: "))
    quantity = int(input(f"Enter quantity of {name}: "))
    product = (name, price, quantity)
    products.append(product)
print("\n--- BILL DETAILS ---")
total_bill = 0
for name, price, quantity in products:
    total = price * quantity
    total_bill += total
    print(f"{name}: ₹{price} x {quantity} = ₹{total}")
print(f"\nTotal Amount to Pay: ₹{total_bill}")

