#Check if a product is available in a shopping cart

shopping_cart = ["apple", "banana", "milk", "bread"]
product = input("Enter product to check: ")
if product in shopping_cart:
    print(product, "is available in the cart.")
else:
    print(product, "is NOT available in the cart.")
