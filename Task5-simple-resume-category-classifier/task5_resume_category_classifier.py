# TASK 5: SIMPLE RESUME CATEGORY CLASSIFIER
# Infosys Springboard - Skill Gap AI Project

print("----- SIMPLE RESUME CATEGORY CLASSIFIER -----")

# Take skills as comma-separated input from user
skills_input = input("Enter your skills (comma separated): ")

# Convert to list and clean
skills = [skill.strip().lower() for skill in skills_input.split(",") if skill.strip() != ""]

# Define keyword sets for each category
data_ml_skills = ["machine learning", "ml", "data science", "data analysis", "pandas", "numpy", "statistics"]
web_dev_skills = ["html", "css", "javascript", "react", "angular", "node", "php", "bootstrap"]
software_dev_skills = ["java", "python", "c", "c++", "c#", "oop", "software development", "git"]

category = "Other"

for skill in skills:
    if skill in data_ml_skills:
        category = "Data/ML"
        break
    elif skill in web_dev_skills:
        category = "Web Development"
        break
    elif skill in software_dev_skills:
        category = "Software Development"
        break

print("\nPredicted Resume Category:", category)
