# match_pdf_resume.py
import numpy as np
import pandas as pd
import re
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from resume_parser import parse_resume

# Using preprocess_text from utils.py instead of defining it here

print("Loading BERT model...")
model = SentenceTransformer("all-MiniLM-L6-v2")
#dxs
# Load jobs directly from the source file instead of relying on saved vectors
from data_loader import load_jobs
from utils import preprocess_text as utils_preprocess_text
from matcher_bert import compute_bert_similarity

jobs_df = load_jobs('AiRanker/data/jobs/jobs.csv')
print(f"Loaded {len(jobs_df)} jobs from source file")

# Preprocess job descriptions
jobs_df['cleaned_job_desc'] = jobs_df['Job Description'].apply(utils_preprocess_text)

# Ensure we have the job title column
if 'Job Title' not in jobs_df.columns:
    raise ValueError("No 'Job Title' column found in jobs_df!")

job_title_col = 'Job Title'

resume_path = "AiRanker/data/resumes/taissirCV.pdf"
resume_text = parse_resume(resume_path)

if not resume_text.strip():
    print("No text found in the PDF resume.")
else:
    # Use the same preprocessing as in the main pipeline
    resume_clean = utils_preprocess_text(resume_text)
    print(f"Preprocessed resume text: {resume_clean[:100]}...")
    
    # Encode resume and job descriptions
    resume_vec = model.encode([resume_clean])
    job_vecs = model.encode(jobs_df['cleaned_job_desc'].tolist(), convert_to_numpy=True, show_progress_bar=True)
    
    # Compute similarities
    sims = cosine_similarity(resume_vec, job_vecs)[0]
    top_indices = sims.argsort()[::-1][:3]

    print(f"\nTop job matches for: {resume_path}")
    for i, idx in enumerate(top_indices):
        print(f"{i+1}. {jobs_df.iloc[idx][job_title_col]} (Score: {sims[idx]:.3f})")
