#Write a Python program to get the key, value and item in a dictionary.
#input:dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("Keys:")
for key in dict_num.keys():
    print(key)
print("\nValues:")
for value in dict_num.values():
    print(value)
print("\nItems (key-value pairs):")
for item in dict_num.items():
    print(item)
