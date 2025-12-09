# TASK 1: BASIC SKILL MATCHER
# Python Mini Project - Infosys Springboard

# Step 1: Job Description taken from Internet
job_description = "Job Description for Web Developer: HTML, CSS, JavaScript, Python, SQL, React"

# Step 2: Resume Skills taken from a Sample Resume (Internet / Your Own Resume)
resume_skills = ["Python", "HTML", "CSS", "Communication", "Problem Solving"]

# Step 3: Job Required Skills taken as input (from JD template)
job_input = input("Enter Job Required Skills (comma separated): ")
job_skills = job_input.split(",")

# Step 4: Clean both lists
for i in range(len(resume_skills)):
    resume_skills[i] = resume_skills[i].strip().lower()

for i in range(len(job_skills)):
    job_skills[i] = job_skills[i].strip().lower()

# Step 5: Compare both the lists
matched_skills = []
missing_skills = []

for skill in job_skills:
    if skill in resume_skills:
        matched_skills.append(skill)
    else:
        missing_skills.append(skill)

# Step 6: Display Output
print("\n----- JOB DESCRIPTION -----")
print(job_description)

print("\n----- RESUME SKILLS -----")
print(resume_skills)

print("\n----- JOB REQUIRED SKILLS -----")
print(job_skills)

print("\n----- MATCHED SKILLS -----")
print(matched_skills)

print("\n----- MISSING SKILLS -----")
print(missing_skills)
