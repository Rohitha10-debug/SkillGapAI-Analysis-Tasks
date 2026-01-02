# Tasks for Milestone 3 – Skill Gap Analysis using Sentence-BERT

## 📌 Overview

This module implements **Milestone 3** of the Skill Gap Analysis project.
The goal of this milestone is to **compare resume skills and job description skills** using **Sentence-BERT embeddings**, compute similarity scores, and generate a **structured skill gap report**.

The implementation focuses on building a **complete, modular, and extensible pipeline** for skill gap analysis using NLP and semantic similarity.

---

## 🎯 Objectives Covered

This implementation addresses the core Milestone 3 tasks, including:

* Skill cleaning, normalization, and de-duplication
* Sentence-BERT based embedding generation
* Cosine similarity computation between skills
* Resume vs Job Description skill comparison
* Similarity matrix generation and analysis
* Threshold-based skill classification:

  * Matched skills
  * Partially matched skills
  * Missing skills
* Overall resume–job alignment score
* Structured JSON skill gap report
* Heatmap visualization of similarity matrix
* Modular pipeline design for scalability

---

## 🛠️ Technologies Used

* **Python**
* **Sentence-BERT** (`all-MiniLM-L6-v2`)
* **scikit-learn** (cosine similarity)
* **pandas**
* **matplotlib & seaborn** (visualization)
* **JSON** (report generation)

---

## 📂 Folder Structure

```
tasks_for_milestone3/
│
├── skill_gap_analysis.py     # Main pipeline execution
├── text_normalizer.py        # Skill normalization & abbreviation handling
├── similarity_utils.py       # Embedding & similarity utilities
├── visualization.py          # Similarity heatmap visualization
├── requirements.txt          # Required Python libraries
├── skill_gap_report.json     # Generated skill gap report
└── README.md                 # Documentation
```

---

## ⚙️ Pipeline Description

### 1. Skill Normalization

* Converts all skills to lowercase
* Removes duplicates
* Expands abbreviations (e.g., ML → Machine Learning)

### 2. Embedding Generation

* Uses pretrained **Sentence-BERT**
* Generates embeddings for resume and job description skills

### 3. Similarity Computation

* Computes cosine similarity between skill embeddings
* Generates a full similarity matrix

### 4. Skill Gap Classification

* Skills are classified based on similarity thresholds:

  * **Matched**
  * **Partially Matched**
  * **Missing**

### 5. Reporting

* Generates a structured **JSON skill gap report**
* Computes an overall alignment score

### 6. Visualization

* Visualizes similarity matrix using a heatmap
* Highlights strong and weak skill matches

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python skill_gap_analysis.py
```

---

## 📤 Sample Output (skill_gap_report.json)

```json
{
  "matched_skills": ["python"],
  "partially_matched_skills": ["machine learning"],
  "missing_skills": ["deep learning"],
  "overall_alignment_score": 0.71
}
```

---

## 🔮 Future Enhancements

* Comparison using multiple Sentence-BERT models
* Embedding caching for performance optimization
* Separate similarity thresholds for technical and soft skills
* Export combined reports and visualizations
* Integration with spaCy-based skill extraction pipeline

---

## ✅ Conclusion

This module demonstrates a **complete end-to-end Skill Gap Analysis system** using Sentence-BERT.
It forms a strong foundation for intelligent resume screening and job matching applications.

---

## 📌 Author

**Rohitha Panchamukhi M**

Infosys Springboard Internship
