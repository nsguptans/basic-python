'''1. Write a Python program to count the occurrences of each word in a

given sentence

string = “To change the overall look of your document. To change the look

available in the gallery”'''
from collections import Counter

# Given string
string = "To change the overall look of your document. To change the look available in the gallery"

# Convert to lowercase and remove punctuation
string = string.lower().replace(".", "")

# Split the string into words
words = string.split()

# Count occurrences using Counter
word_count = Counter(words)

# Display the word count
for word, count in word_count.items():
    print(f"'{word}': {count}")
#2. Write a Python program to remove a newline in Python

#String = "\nBest \nDeeptech \nPython \nTraining\n"
string = "\nBest \nDeeptech \nPython \nTraining\n"

# Remove newlines using replace()
cleaned_string = string.replace("\n", " ")

# Print the result
print(cleaned_string.strip())
#3. Write a Python program to reverse words in a string
#String = “Deeptech Python Training”

string = "Deeptech Python Training"

# Split the string into words, reverse the order, and join them back
reversed_string = " ".join(string.split()[::-1])

# Print the result
print(reversed_string)
#4 4. Write a Python program to count and display the vowels of a given text
#String=”Welcome to python Training”
string = "Welcome to python Training"

# Convert to lowercase for case insensitivity
string = string.lower()

# Define vowels
vowels = "aeiou"

# Find and count vowels
vowel_count = {v: string.count(v) for v in vowels if v in string}

# Display results
print("Vowel Count:", sum(vowel_count.values()))
print("Vowels Found:", ", ".join([v * vowel_count[v] for v in vowel_count]))






