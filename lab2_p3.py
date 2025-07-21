#Using max() and min() functions display the maximum and minimum of 5 random numbers.

import random
numbers = [random.randint(1, 100) for _ in range(5)]
print("Random numbers:", numbers)
print("Maximum number:", max(numbers))
print("Minimum number:", min(numbers))
