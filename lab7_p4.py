#Write a Python program to get the key, value and item in a dictionary.
#Input: input_dict = {1: 10, 2: 20, 3:None, 4: 40, 5: None, 6: 60}

input_dict = {1: 10, 2: 20, 3: None, 4: 40, 5: None, 6: 60}
print("Keys:")
for key in input_dict.keys():
    print(key)
print("\nValues:")
for value in input_dict.values():
    print(value)
print("\nItems (key-value pairs):")
for key, value in input_dict.items():
    print(f"{key}: {value}")
