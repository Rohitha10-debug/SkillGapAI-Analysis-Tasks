# Task 3: Experience Extractor
# Infosys Springboard - Python Mini Project

# This program extracts the number of years of experience
# from a sentence like:
# "I have 3 years of experience in Python."

# Take input sentence from the user
sentence = input("Enter experience sentence: ")

# Split the sentence into words
words = sentence.split()

years = None

# Go through each word and look for digits
for word in words:
    # Keep only digit characters from the word
    digits_only = ""
    for ch in word:
        if ch.isdigit():
            digits_only += ch

    # If we found digits and it forms a valid number
    if digits_only.isdigit():
        years = int(digits_only)
        break

# Display result
if years is not None:
    print("Experience Detected:", years, "Years")
else:
    print("No experience information found.")
