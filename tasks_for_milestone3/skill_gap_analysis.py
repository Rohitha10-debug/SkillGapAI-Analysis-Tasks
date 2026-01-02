import json
import numpy as np
from text_normalizer import normalize_skills
from similarity_utils import generate_embeddings, compute_similarity_matrix
from visualization import plot_heatmap

resume_skills = ["Python", "ML", "SQL", "Communication"]
jd_skills = ["Python", "Machine Learning", "Deep Learning", "Teamwork"]

resume_skills = normalize_skills(resume_skills)
jd_skills = normalize_skills(jd_skills)

resume_emb = generate_embeddings(resume_skills)
jd_emb = generate_embeddings(jd_skills)

similarity_matrix = compute_similarity_matrix(resume_emb, jd_emb)

threshold_match = 0.75
threshold_partial = 0.5

matched = []
partial = []
missing = []

for j, jd_skill in enumerate(jd_skills):
    scores = similarity_matrix[:, j]
    best_score = max(scores)

    if best_score >= threshold_match:
        matched.append(jd_skill)
    elif best_score >= threshold_partial:
        partial.append(jd_skill)
    else:
        missing.append(jd_skill)

report = {
    "matched_skills": matched,
    "partially_matched_skills": partial,
    "missing_skills": missing,
    "overall_alignment_score": float(np.mean(similarity_matrix))
}

with open("skill_gap_report.json", "w") as f:
    json.dump(report, f, indent=4)

print(report)

plot_heatmap(similarity_matrix, resume_skills, jd_skills)
