#Write a Python program and calculate the mean of the below dictionary.
#test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4}
#Output: 6.2


test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}
values = test_dict.values()
mean = sum(values) / len(values)
print("Mean of dictionary values:", mean)
