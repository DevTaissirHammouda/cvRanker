from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def compute_bert_similarity(resumes, jobs):
    resume_embeddings = model.encode(resumes.tolist(), convert_to_numpy=True)
    job_embeddings = model.encode(jobs.tolist(), convert_to_numpy=True)

    return cosine_similarity(resume_embeddings, job_embeddings)
