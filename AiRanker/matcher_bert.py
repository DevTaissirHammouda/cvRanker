# matcher_bert.py
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def compute_bert_similarity(resumes, jobs_df, save_embeddings=True, save_path="AiRanker/output"):
    """
    resumes: pd.Series of cleaned resume texts
    jobs_df: pd.DataFrame with at least 'cleaned_job_desc' column
    save_embeddings: whether to save embeddings and jobs_df csv
    save_path: directory to save to

    Returns similarity matrix resume x job
    """
    job_texts = jobs_df['cleaned_job_desc'].tolist()
    resume_embeddings = model.encode(resumes.tolist(), convert_to_numpy=True, show_progress_bar=True)
    job_embeddings = model.encode(job_texts, convert_to_numpy=True, show_progress_bar=True)

    if save_embeddings:
        np.save(f"{save_path}/job_bert_vectors.npy", job_embeddings)
        jobs_df.to_csv(f"{save_path}/jobs.csv", index=False)  # Save full DataFrame including Job Title etc.

    return cosine_similarity(resume_embeddings, job_embeddings)
