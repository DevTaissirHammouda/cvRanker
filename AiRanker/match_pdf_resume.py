# match_pdf_resume.py
import numpy as np
import pandas as pd
import re
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from resume_parser import parse_resume

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\W+', ' ', text)
    return text.strip()

print("Loading BERT model and saved job vectors...")
model = SentenceTransformer("all-MiniLM-L6-v2")

job_vectors = np.load("AiRanker/output/job_bert_vectors.npy")
jobs_df = pd.read_csv("AiRanker/output/jobs.csv")

print("Columns in jobs_df:", jobs_df.columns.tolist())

# Find job title column name robustly
job_title_col = None
for col in jobs_df.columns:
    if col.lower().replace(" ", "") == "jobtitle":
        job_title_col = col
        break

if job_title_col is None:
    raise ValueError("No 'Job Title' column found in jobs_df!")

resume_path = "AiRanker/data/resumes/taissirCV.pdf"
resume_text = parse_resume(resume_path)

if not resume_text.strip():
    print("No text found in the PDF resume.")
else:
    resume_clean = preprocess_text(resume_text)
    resume_vec = model.encode([resume_clean])

    sims = cosine_similarity(resume_vec, job_vectors)[0]
    top_indices = sims.argsort()[::-1][:3]

    print(f"\nTop job matches for: {resume_path}")
    for i, idx in enumerate(top_indices):
        print(f"{i+1}. {jobs_df.iloc[idx][job_title_col]} (Score: {sims[idx]:.3f})")
