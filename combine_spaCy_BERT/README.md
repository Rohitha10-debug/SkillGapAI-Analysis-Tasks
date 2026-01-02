# Combined spaCy & BERT Skill Extraction – Practice Implementation

## 📌 Overview

This module contains the **implementation of practice questions** related to **skill extraction using NLP**, combining **spaCy-based techniques** and a **BERT-ready design**.

The objective is to extract, normalize, merge, and categorize skills from resume or job description text in a structured and extensible manner.

---

## 🎯 Objectives Covered

This implementation addresses the following key objectives from the practice set:

* Extraction of skills using **spaCy PhraseMatcher**
* Matching skills against a **predefined master skill list**
* Normalization of extracted skills (lowercasing & duplicate removal)
* Categorization of skills into:

  * Technical Skills
  * Soft Skills
* Merging outputs from multiple spaCy-based pipelines
* Generating a **final structured output** in JSON format
* Designing the pipeline to be **extensible for BERT integration**

---

## 🛠️ Technologies Used

* **Python**
* **spaCy**
* **spaCy PhraseMatcher**
* **JSON** for structured output

*(Sentence-BERT integration is kept extensible and can be added in future iterations.)*

---

## 📂 Folder Structure

```
combine_spaCy_BERT/
│
├── combined_skill_extraction.py   # Main implementation
├── skills_master.py               # Master list of technical & soft skills
├── requirements.txt               # Required libraries
├── final_skills.json              # Generated structured output (on execution)
└── README.md                      # Documentation
```

---

## ⚙️ Implementation Details

### 1. Skill Matching

* Uses **spaCy PhraseMatcher** to detect skill phrases
* Matches resume text against predefined skill lists

### 2. Skill Normalization

* Converts all skills to lowercase
* Removes duplicates using set-based logic

### 3. Skill Categorization

* Skills are stored separately as:

  * `technical_skills`
  * `soft_skills`

### 4. Merging Logic

* Outputs from different spaCy-based approaches are merged
* Ensures only **one standardized version** of each skill is retained

### 5. Structured Output

* Final extracted skills are saved as:

```
final_skills.json
```

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python combined_skill_extraction.py
```

---

## 📤 Sample Output

```json
{
    "technical_skills": ["python", "machine learning", "sql"],
    "soft_skills": ["communication", "teamwork"]
}
```

---

## 🔮 Future Enhancements

* Sentence-BERT based similarity matching
* Skill conflict resolution (abbreviations vs full forms)
* Confidence scoring for extracted skills
* Resume vs Job Description skill comparison

---

## ✅ Conclusion

This module demonstrates a **structured and scalable approach** to skill extraction using NLP.
It forms a strong foundation for advanced AI-based resume analysis systems.

---

## 📌 Author

**Rohitha Panchamukhi M**

Infosys Springboard Internship

