# TASK 7: SIMPLE EMAIL EXTRACTOR
# Infosys Springboard - Skill Gap AI Project

import re

print("----- SIMPLE EMAIL EXTRACTOR -----")

# Take resume text as input from the user
resume_text = input("Enter resume text (or a sentence containing email): ")

# Regular expression pattern for emails
email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

# Find all emails in the text
emails_found = re.findall(email_pattern, resume_text)

# Display result
if emails_found:
    print("\nEmails found:")
    for email in emails_found:
        print("-", email)
else:
    print("\nNo email address found in the given text.")
