num=int(input("Enter a number:"))
if num <=1:
    print(f"{num} is not a prime number")
else:
    for i in rang(2, int(num**0.5)+1):
        if num % i==0:
            print(f"{num} is not a prime number")
            break
        else:
            print("{num} is a prime number")
