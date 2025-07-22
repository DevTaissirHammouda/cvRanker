# matcher_bert.py
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def compute_bert_similarity(resumes, jobs, save_embeddings=True, save_path="AiRanker/output"):
    """
    resumes: pd.Series of cleaned resume texts
    jobs: pd.Series of cleaned job description texts
    save_embeddings: whether to save embeddings and jobs csv
    save_path: directory to save to

    Returns similarity matrix resume x job
    """
    job_texts = jobs.tolist()
    resume_embeddings = model.encode(resumes.tolist(), convert_to_numpy=True, show_progress_bar=True)
    job_embeddings = model.encode(job_texts, convert_to_numpy=True, show_progress_bar=True)

    if save_embeddings:
        np.save(f"{save_path}/job_bert_vectors.npy", job_embeddings)
        # Note: We're no longer saving jobs to CSV as we only have the Series, not the full DataFrame

    return cosine_similarity(resume_embeddings, job_embeddings)
