# TASK 6: SKILL FREQUENCY CHECKER
# Infosys Springboard - Skill Gap AI Project

print("----- SKILL FREQUENCY CHECKER -----")

# Sample resume text (can be replaced with actual resume)
resume_text = """
Rohitha is a Computer Science Engineering student with interest in Python, 
Machine Learning, Web Development and Cybersecurity. She has worked on 
projects using Python, HTML, CSS and basic SQL. She is also learning data analysis.
"""

# Convert entire resume text to lowercase for case-insensitive matching
resume_text_lower = resume_text.lower()

# Take skills to check from the user
skills_input = input("Enter skills to check (comma separated): ")

# Convert input string to a clean list
skills = [skill.strip().lower() for skill in skills_input.split(",") if skill.strip() != ""]

print("\nSkill Frequency in Resume:\n")

# For each skill, count how many times it appears in the resume text
for skill in skills:
    count = resume_text_lower.count(skill)
    print(f"{skill} : {count}")
