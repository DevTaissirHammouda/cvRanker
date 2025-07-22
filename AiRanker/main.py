# main.py

from data_loader import *
from utils import *
from matcher import compute_similarity
import numpy as np
resumes_df = load_resumes('AiRanker/data/resumes/resumes.csv')
jobs_df = load_jobs('AiRanker/data/jobs/jobs.csv')


# Apply preprocessing
resumes_df['cleaned_resume'] = resumes_df['Resume'].apply(preprocess_text)
jobs_df['cleaned_job_desc'] = jobs_df['Job Description'].apply(preprocess_text)

similarity = compute_similarity(resumes_df['cleaned_resume'], jobs_df['cleaned_job_desc'])





top_n = 3

for resume_idx in range(len(resumes_df)):
    top_indices = np.argsort(similarity[resume_idx])[::-1][:top_n]
    print(f"\nTop {top_n} job matches for Resume {resume_idx} ({resumes_df.iloc[resume_idx]['Category']}):")

    for i, job_idx in enumerate(top_indices):
        score = similarity[resume_idx][job_idx]
        title = jobs_df.iloc[job_idx]['Job Title']
        print(f"{i+1}. {title} (Score: {score:.2f})")
