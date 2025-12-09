# TASK 4: JOB TITLE NORMALIZER
# Infosys Springboard - Skill Gap AI Project

print("----- JOB TITLE NORMALIZER -----")

# Take input from user
job_title = input("Enter job title: ").strip().lower()

# Dictionary of job title variations
job_title_mapping = {
    "software engineer": ["software engineer", "sde", "developer", "programmer"],
    "data scientist": ["data scientist", "data analyst", "ml engineer"],
    "web developer": ["web developer", "frontend developer", "backend developer", "full stack developer"],
    "tester": ["tester", "qa engineer", "test engineer"]
}

normalized_title = "Unknown Job Title"

# Normalize the job title
for standard_title, variations in job_title_mapping.items():
    if job_title in variations:
        normalized_title = standard_title
        break

# Display result
print("\nNormalized Job Title:", normalized_title)
