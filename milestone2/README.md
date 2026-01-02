# Milestone 2 – Skill Extraction using NLP (spaCy)

## 📌 Overview

This project is part of **Milestone 2** of the Skill Gap Analysis internship.
The objective of this module is to **extract skills from a resume PDF** using **Natural Language Processing (NLP)**.

The system identifies and categorizes:

* **Technical Skills**
* **Soft Skills**

using the **spaCy** NLP library.

---

## 🧠 Problem Statement

Manual resume screening is time-consuming and error-prone.
This project automates the process of skill extraction from resumes and presents them in a structured format.

---

## 🛠️ Technologies Used

* **Python**
* **spaCy** (NLP processing)
* **pdfplumber** (PDF text extraction)

---

## 📂 Project Structure

```
milestone2/
│
├── skill_extraction.py     # Main script for skill extraction
├── skills.py               # Technical & soft skill dictionary
├── resume.pdf              # Sample resume (input)
├── requirements.txt        # Required Python libraries
└── README.md               # Project documentation
```

---

## ⚙️ How It Works

1. Resume text is extracted from a **PDF file**
2. Text is processed using **spaCy NLP**
3. Skills are matched against predefined skill lists
4. Skills are separated into:

   * Technical Skills
   * Soft Skills
5. Output is displayed in a readable format

---

## ▶️ How to Run the Project

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python skill_extraction.py
```

---

## 📤 Output

* List of **Technical Skills**
* List of **Soft Skills**

(Screenshots of output are provided as part of submission)

---

## ✅ Outcome

This project successfully demonstrates:

* Resume parsing using NLP
* Skill extraction automation
* Structured categorization of skills

---

## 📌 Author

**Rohitha Panchamukhi M**
Infosys Springboard Internship

