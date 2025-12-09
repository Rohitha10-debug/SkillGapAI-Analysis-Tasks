# Task 2: Resume Word Counter
# Infosys Springboard - Python Mini Project

# Sample resume text (can be replaced with real resume text)
resume_text = """
Rohitha Panchamukhi is a Computer Science Engineering student specializing in
IoT, Cybersecurity, and Blockchain Technology. She has strong communication
skills and basic knowledge of Python, SQL, and Data Analysis.
"""

# Remove extra spaces and split into words
words = resume_text.split()

# Count total words
word_count = len(words)

# Display result
print("----- RESUME WORD COUNTER -----")
print("Total number of words in the resume:", word_count)
