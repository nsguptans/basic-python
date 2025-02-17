'''1. Write a Python program to Count all letters, digits, and special symbols from the given string

 Input = “P@#yn26at^&i5ve” 

Output: Chars = 8 Digits = 3 Symbol = 4 '''
input_str = "P@#yn26at^&i5ve"

# Initialize counters
char_count = digit_count = symbol_count = 0

# Iterate through each character in the string
for ch in input_str:
    if ch.isalpha():  # Check if it's a letter
        char_count += 1
    elif ch.isdigit():  # Check if it's a digit
        digit_count += 1
    else:  # Otherwise, it's a special symbol
        symbol_count += 1

# Display the results
print(f"Chars = {char_count} Digits = {digit_count} Symbol = {symbol_count}")
'''2. Write a Python program to remove duplicate characters of a given string.

 Input = “String and String Function” 

Output: String and Function '''
input_str = "String and String Function"

# Initialize a set to track seen characters
seen = set()
output = []

# Iterate through each character in the string
for char in input_str:
    if char not in seen:
        output.append(char)
        seen.add(char)

# Join the list of characters back into a string
result = "".join(output)

# Display the result
print(result)
'''3. Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string

 Input = “Hell0 W0rld ! 123 * # welcome to pYtHoN” 

Output: UpperCase : 5 LowerCase : 18 NumberCase : 5 SpecialCase : 11'''
input_str = "Hell0 W0rld ! 123 * # welcome to pYtHoN"

# Initialize counters
uppercase_count = lowercase_count = numeric_count = special_count = 0

# Iterate through each character in the string
for char in input_str:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1
    elif char.isdigit():
        numeric_count += 1
    else:
        special_count += 1

# Display the results
print(f"UpperCase: {uppercase_count}")
print(f"LowerCase: {lowercase_count}")
print(f"NumberCase: {numeric_count}")
print(f"SpecialCase: {special_count}")
'''4. Write a Python Count vowels in a string 

input= “Welcome to Python Assignment” 

Output: Total vowels are: 8'''
input_str = "Welcome to Python Assignment"

# Initialize a counter for vowels
vowel_count = 0

# Define the vowels
vowels = "aeiouAEIOU"

# Iterate through each character in the string
for char in input_str:
    if char in vowels:
        vowel_count += 1

# Display the result
print(f"Total vowels are: {vowel_count}")









