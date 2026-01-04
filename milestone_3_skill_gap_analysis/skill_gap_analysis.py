from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Sample skills
candidate_skills = ["Python", "SQL", "Communication", "Machine Learning"]
job_skills = ["Python", "Deep Learning", "SQL", "AWS"]

model = SentenceTransformer('all-MiniLM-L6-v2')

candidate_embeddings = model.encode(candidate_skills)
job_embeddings = model.encode(job_skills)

similarity_matrix = cosine_similarity(candidate_embeddings, job_embeddings)

print("Similarity Matrix:")
print(similarity_matrix)
