# main.py

from data_loader import *
resumes_df = load_resumes('data/resumes/resumes.csv')
jobs_df = load_jobs('data/jobs/jobs.csv')

print("Loaded resumes:", resumes_df.shape[0])
print("Loaded jobs:", jobs_df.shape[0])

print(resumes_df.head())
print(jobs_df.head())