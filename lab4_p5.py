#Count how many times a name appears in a list

names = ["Alice", "Bob", "Alice", "Charlie", "Alice", "Bob"]
name_to_count = input("Enter the name to count: ")
count = names.count(name_to_count)
print(name_to_count, "appears", count, "time(s) in the list.")
