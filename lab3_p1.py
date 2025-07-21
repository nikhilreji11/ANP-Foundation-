#1.write a programm to check if a string is palindrome or not

text=input("Enter a string:")
if text==text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
