#Create a list of even numbers from 1 to 20

even_numbers = []
for num in range(1, 21):
    if num % 2 == 0:
        even_numbers.append(num)
print("Even numbers from 1 to 20:", even_numbers)
