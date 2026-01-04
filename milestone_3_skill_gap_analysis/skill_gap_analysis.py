from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample skills
candidate_skills = [
    "Python",
    "SQL",
    "Machine Learning",
    "Communication",
    "Data Analysis"
]

job_skills = [
    "Python",
    "Deep Learning",
    "SQL",
    "AWS",
    "Statistics"
]

# Load BERT model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Generate embeddings
candidate_embeddings = model.encode(candidate_skills)
job_embeddings = model.encode(job_skills)

# Compute similarity matrix
similarity_matrix = cosine_similarity(candidate_embeddings, job_embeddings)

# Create DataFrame
df_similarity = pd.DataFrame(
    similarity_matrix,
    index=candidate_skills,
    columns=job_skills
)

print("\nSimilarity Matrix:\n")
print(df_similarity)

# Plot heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df_similarity, annot=True, cmap="YlGnBu", fmt=".2f")
plt.title("Skill Similarity Matrix")
plt.tight_layout()
plt.savefig("similarity_matrix.png")
plt.show()

# Skill gap analysis
matched = []
partial = []
missing = []

for skill in job_skills:
    max_score = df_similarity[skill].max()
    if max_score >= 0.75:
        matched.append(skill)
    elif max_score >= 0.5:
        partial.append(skill)
    else:
        missing.append(skill)

print("\nMatched Skills:", matched)
print("Partially Matched Skills:", partial)
print("Missing Skills:", missing)

