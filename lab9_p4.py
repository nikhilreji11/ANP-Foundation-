#Write a function display_words() in python to read lines from a text file "story.txt", and display those words, which are less than 4 characters.

def display_words():
    try:
        with open("story.txt", "r") as file:
            print("Words with less than 4 characters:\n")
            for line in file:
                words = line.strip().split()
                for word in words:
                    if len(word) < 4:
                        print(word)
    except FileNotFoundError:
        print("Error: File 'story.txt' not found.")
display_words()
