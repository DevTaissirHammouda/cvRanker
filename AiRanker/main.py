# main.py

from data_loader import *
from utils import *

resumes_df = load_resumes('AiRanker/data/resumes/resumes.csv')
jobs_df = load_jobs('AiRanker/data/jobs/jobs.csv')


# Apply preprocessing
resumes_df['cleaned_resume'] = resumes_df['Resume'].apply(preprocess_text)
jobs_df['cleaned_job_desc'] = jobs_df['Job Description'].apply(preprocess_text)

print(resumes_df[['Category', 'cleaned_resume']].head())
print(jobs_df[['Job Title', 'cleaned_job_desc']].head())