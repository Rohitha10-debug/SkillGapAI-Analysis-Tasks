from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embeddings(skills):
    return model.encode(skills)

def compute_similarity_matrix(resume_emb, jd_emb):
    return cosine_similarity(resume_emb, jd_emb)
