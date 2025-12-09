print("----- JOB TITLE NORMALIZER -----")

job_title = input("Enter Job Title: ")

job_title = job_title.lower().strip()

normalized_titles = {
    "sde": "software engineer",
    "software developer": "software engineer",
    "frontend dev": "frontend developer",
    "backend dev": "backend developer",
    "data scientist": "data scientist",
    "ml engineer": "machine learning engineer",
    "ai engineer": "artificial intelligence engineer"
}

if job_title in normalized_titles:
    print("Normalized Job Title:", normalized_titles[job_title])
else:
    print("Normalized Job Title:", job_title)
