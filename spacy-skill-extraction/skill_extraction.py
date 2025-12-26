# TASK 1: Install & load spaCy model
import spacy
from spacy.matcher import PhraseMatcher

nlp = spacy.load("en_core_web_sm")

# -----------------------------
# COMMON SKILL LISTS
# -----------------------------
technical_skills = [
    "Python", "SQL", "NLP", "Machine Learning", "Data Analysis"
]

soft_skills = [
    "communication", "teamwork", "leadership", "problem solving", "time management"
]

# -----------------------------
# TASK 3: Convert technical skills into PhraseMatcher patterns
# TASK 8: Case-insensitive matching
# -----------------------------
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
patterns = [nlp(skill) for skill in technical_skills]
matcher.add("TECH_SKILLS", patterns)

# -----------------------------
# MAIN EXTRACTION FUNCTION
# -----------------------------
def extract_skills(text):
    doc = nlp(text)

    tech_found = []
    soft_found = []

    # TASK 2,6,10,11: Extract technical skills
    matches = matcher(doc)
    for match_id, start, end in matches:
        skill = doc[start:end].text.lower()
        tech_found.append(skill)

    # TASK 7 & 12: Extract soft skills using token comparison
    for token in doc:
        if token.text.lower() in soft_skills:
            soft_found.append(token.text.lower())

    # TASK 4 & 5: Normalize & remove duplicates
    tech_found = list(set(tech_found))
    soft_found = list(set(soft_found))

    # TASK 9: JSON output
    return {
        "technical_skills": tech_found,
        "soft_skills": soft_found
    }

# -----------------------------
# TASK 14: Match SQL but NOT NoSQL
# -----------------------------
def extract_sql_only(text):
    doc = nlp(text)
    sql_found = []

    for token in doc:
        if token.text.lower() == "sql":
            sql_found.append("sql")

    return list(set(sql_found))

# -----------------------------
# TASK 15: Resume & JD separately
# -----------------------------
resume_text = "Experienced in Python, SQL and strong communication skills."
jd_text = "Looking for NLP, Machine Learning with teamwork abilities."

resume_skills = extract_skills(resume_text)
jd_skills = extract_skills(jd_text)

# -----------------------------
# TEST CASES (Covers remaining tasks)
# -----------------------------
if __name__ == "__main__":
    sample_text = "Experience in Python, NLP, and Machine Learning with SQL."
    print("Extracted Skills:", extract_skills(sample_text))

    print("SQL Only:", extract_sql_only("SQL, NoSQL, MySQL"))

    print("Resume Skills:", resume_skills)
    print("JD Skills:", jd_skills)
