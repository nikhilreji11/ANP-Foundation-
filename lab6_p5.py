#Write a Python program to find common hobbies between two friends using sets.
#Take comma-separated hobby inputs from two users (e.g., "reading, painting, cricket").
#Convert the inputs into two sets.
#Display:
#Common hobbies using set intersection.
#All hobbies using set union.
#Hobbies unique to each friend.

hobbies1 = input("Enter hobbies of Friend 1 (comma-separated): ")
hobbies2 = input("Enter hobbies of Friend 2 (comma-separated): ")
set1 = set(hobby.strip().lower() for hobby in hobbies1.split(","))
set2 = set(hobby.strip().lower() for hobby in hobbies2.split(","))
common_hobbies = set1 & set2
all_hobbies = set1 | set2
unique_friend1 = set1 - set2
unique_friend2 = set2 - set1
print("\n--- HOBBY COMPARISON ---")
print("Common hobbies:", common_hobbies)
print("All hobbies:", all_hobbies)
print("Hobbies unique to Friend 1:", unique_friend1)
print("Hobbies unique to Friend 2:", unique_friend2)
