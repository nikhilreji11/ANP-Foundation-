#Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.

def read_file_line_by_line():
    try:
        with open("ABC.txt", "r") as file:
            print("Contents of ABC.txt:\n")
            for line in file:
                print(line.strip())  # strip() removes trailing newline
    except FileNotFoundError:
        print("Error: File 'ABC.txt' not found.")
read_file_line_by_line()
