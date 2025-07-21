#count a number of vowels in a text

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
text = input("Enter a text: ")
vowel_count = count_vowels(text)
print("Number of vowels:", vowel_count)
