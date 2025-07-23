import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from data_loader import load_resumes, load_skills
from utils import preprocess_text
from skills import extract_skills
from skill_vector import skills_to_vector, compute_skill_similarity_matrix

print("Loading model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load resumes and skills
resumes_df = load_resumes('AiRanker/data/resumes/resumes.csv')
skills_set = load_skills('AiRanker/data/skills/skills.csv')

# Preprocess resumes
resumes_df['cleaned_resume'] = resumes_df['Resume'].apply(preprocess_text)
resumes_df['skills'] = resumes_df['cleaned_resume'].apply(lambda x: extract_skills(x, skills_set))

# Prepare skill vectors
skill_to_idx = {skill: idx for idx, skill in enumerate(skills_set)}
resume_skill_vecs = np.array([skills_to_vector(s, skill_to_idx) for s in resumes_df['skills']])

# === INPUT JOB DESCRIPTION ===
job_title = "Data Scientist"
job_description = """
We are seeking a Data Scientist with expertise in Python, machine learning, and statistical analysis. 
You will work on building models and extracting insights from structured and unstructured data.
"""

# Preprocess and vectorize job
job_clean = preprocess_text(job_description)
job_skill_set = extract_skills(job_clean, skills_set)
job_skill_vec = skills_to_vector(job_skill_set, skill_to_idx)

# Encode BERT vectors
resume_embeddings = model.encode(resumes_df['cleaned_resume'].tolist(), convert_to_numpy=True, show_progress_bar=True)
job_embedding = model.encode([job_clean], convert_to_numpy=True)

# Similarities
bert_sim = cosine_similarity(resume_embeddings, job_embedding).flatten()
skill_sim = cosine_similarity(resume_skill_vecs, [job_skill_vec]).flatten()

# Combine similarities (tune weights if desired)
combined_sim = 0.7 * bert_sim + 0.3 * skill_sim

# Get top resumes
top_n = 3
top_indices = np.argsort(combined_sim)[::-1][:top_n]

print(f"\nTop {top_n} resumes for job: {job_title}")
for i, idx in enumerate(top_indices, 1):
    score = combined_sim[idx]
    category = resumes_df.iloc[idx]['Category']
    print(f"{i}. Resume {idx} ({category}) - Score: {score:.3f}")
