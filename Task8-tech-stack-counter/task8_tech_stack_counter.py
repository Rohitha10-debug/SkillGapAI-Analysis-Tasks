# TASK 8: TECH STACK COUNTER
# Infosys Springboard - Skill Gap AI Project

print("----- TECH STACK COUNTER -----")

# Sample resume / project description text
text = """
Rohitha has worked with Python, Java, HTML, CSS, JavaScript and React.
She has also used SQL and MongoDB for databases and basic AWS services
for deployment. Her projects include web apps and simple machine learning models.
"""

# Convert text to lowercase for case-insensitive search
text_lower = text.lower()

# List of technologies to count
tech_stack = [
    "python",
    "java",
    "c",
    "c++",
    "html",
    "css",
    "javascript",
    "react",
    "node",
    "sql",
    "mongodb",
    "aws",
    "docker",
    "linux"
]

print("Tech stack frequency in the given text:\n")

# Count how many times each technology appears
for tech in tech_stack:
    count = text_lower.count(tech)
    if count > 0:
        print(f"{tech} : {count}")
