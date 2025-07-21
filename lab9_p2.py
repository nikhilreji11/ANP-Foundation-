#Write a function in Python to count and display the total number of words in a text file “ABC.txt”


def count_words_in_file():
    try:
        with open("ABC.txt", "r") as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            print("Total number of words in ABC.txt:", word_count)
    except FileNotFoundError:
        print("Error: File 'ABC.txt' not found.")
count_words_in_file()
