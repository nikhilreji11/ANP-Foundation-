#Write a Python program to calculate the sum of the numbers in a given tuple.
#Input: tuples_list = [(1, 2), (3,4), (5,6)]
#Output:
#Sum of values in the tuples: 21


tuples_list = [(1, 2), (3, 4), (5, 6)]
total = sum(sum(t) for t in tuples_list)
print("Sum of values in the tuples:", total)
