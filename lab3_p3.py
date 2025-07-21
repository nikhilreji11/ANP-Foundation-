#Replace all spaces with "-" in a text

def replace_spaces(text):
    return text.replace(" ", "-")
text = input("Enter a text: ")
new_text = replace_spaces(text)
print("Text after replacing spaces:", new_text)
