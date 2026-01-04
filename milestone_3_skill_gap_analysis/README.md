# Milestone 3: Skill Gap Analysis and Similarity Matching Module

## Description
This module performs Skill Gap Analysis by comparing candidate skills with required job skills using semantic similarity.

BERT embeddings are generated for skills and cosine similarity is used to identify:
- Matched skills
- Partially matched skills
- Missing skills

A similarity matrix is visualized to understand skill alignment.

---

## Features
- BERT-based skill embeddings
- Cosine similarity computation
- Skill match categorization (High, Partial, Low)
- Skill gap identification
- Similarity matrix visualization

---

## Technologies Used
- Python
- BERT (Sentence Transformers)
- Scikit-learn
- NumPy
- Matplotlib / Seaborn

---

## Output Screenshots

### Similarity Matrix Heatmap
![Similarity Matrix](screenshots/similarity_matrix.png)

### Skill Match Overview
![Skill Match Overview](screenshots/skill_match_overview.png)

### Skill Gap Report
![Skill Gap Report](screenshots/skill_gap_report.png)

---

## Conclusion
This module helps identify missing and partially matched skills, enabling targeted upskilling and better job-candidate alignment.
