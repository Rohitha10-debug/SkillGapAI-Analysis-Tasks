import spacy
import json
from spacy.matcher import PhraseMatcher
from skills_master import TECHNICAL_SKILLS, SOFT_SKILLS

nlp = spacy.load("en_core_web_sm")

def extract_skills(text):
    doc = nlp(text.lower())
    matcher = PhraseMatcher(nlp.vocab, attr="LOWER")

    tech_patterns = [nlp(skill) for skill in TECHNICAL_SKILLS]
    soft_patterns = [nlp(skill) for skill in SOFT_SKILLS]

    matcher.add("TECHNICAL", tech_patterns)
    matcher.add("SOFT", soft_patterns)

    technical = set()
    soft = set()

    matches = matcher(doc)
    for match_id, start, end in matches:
        label = nlp.vocab.strings[match_id]
        skill = doc[start:end].text
        if label == "TECHNICAL":
            technical.add(skill)
        else:
            soft.add(skill)

    return {
        "technical_skills": list(technical),
        "soft_skills": list(soft)
    }

if __name__ == "__main__":
    sample_text = """
    Experienced data scientist skilled in Python, Machine Learning,
    SQL, teamwork and communication.
    """

    skills = extract_skills(sample_text)

    with open("final_skills.json", "w") as f:
        json.dump(skills, f, indent=4)

    print(skills)
