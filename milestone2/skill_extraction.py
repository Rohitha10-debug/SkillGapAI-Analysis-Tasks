import spacy
import pdfplumber
from skills import TECHNICAL_SKILLS, SOFT_SKILLS

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text()
    return text.lower()

def extract_skills(text):
    doc = nlp(text)
    technical = set()
    soft = set()

    for token in doc:
        if token.text in TECHNICAL_SKILLS:
            technical.add(token.text)
        if token.text in SOFT_SKILLS:
            soft.add(token.text)

    return technical, soft

if __name__ == "__main__":
    resume_text = extract_text_from_pdf("resume.pdf")
    tech_skills, soft_skills = extract_skills(resume_text)

    print("Technical Skills:")
    for skill in tech_skills:
        print("-", skill.title())

    print("\nSoft Skills:")
    for skill in soft_skills:
        print("-", skill.title())
