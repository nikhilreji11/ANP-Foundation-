#Write a function in Python to count uppercase character in a text file “ABC.txt”

def count_uppercase_characters():
    try:
        with open("ABC.txt", "r") as file:
            content = file.read()
            count = sum(1 for char in content if char.isupper())
            print("Total number of uppercase characters in ABC.txt:", count)
    except FileNotFoundError:
        print("Error: File 'ABC.txt' not found.")
count_uppercase_characters()

