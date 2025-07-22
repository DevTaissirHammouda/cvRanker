from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def compute_bert_similarity(resumes, jobs):
    resume_embeddings = model.encode(resumes.tolist(), convert_to_numpy=True)
    job_embeddings = model.encode(jobs.tolist(), convert_to_numpy=True)
    bert_job_embeddings = model.encode(jobs_df['cleaned_job_desc'].tolist(), show_progress_bar=True)
    # Save to disk
    np.save("AiRanker/output/job_bert_vectors.npy", bert_job_embeddings)
    jobs_df.to_csv("AiRanker/output/jobs.csv", index=False)
    return cosine_similarity(resume_embeddings, job_embeddings)
