from data_loader import *
from utils import *
from matcher import compute_similarity
from skills import *
import numpy as np
import pandas as pd

print("Starting script...")

# Load data
print("Loading resumes...")
resumes_df = load_resumes('AiRanker/data/resumes/resumes.csv')
print(f"Loaded {len(resumes_df)} resumes")

print("Loading jobs...")
jobs_df = load_jobs('AiRanker/data/jobs/jobs.csv')
print(f"Loaded {len(jobs_df)} jobs")

# Preprocess text columns
print("Preprocessing resumes...")
resumes_df['cleaned_resume'] = resumes_df['Resume'].apply(preprocess_text)
print("Preprocessing jobs...")
jobs_df['cleaned_job_desc'] = jobs_df['Job Description'].apply(preprocess_text)

print("Loading skills...")
skills_set = load_skills('AiRanker/data/skills/skills.csv')
print(f"Loaded {len(skills_set)} unique skills")

print("Extracting skills from resumes...")
resumes_df['skills'] = resumes_df['cleaned_resume'].apply(lambda x: extract_skills(x, skills_set))
print("Extracting skills from jobs...")
jobs_df['skills'] = jobs_df['cleaned_job_desc'].apply(lambda x: extract_skills(x, skills_set))

print("Computing text similarity (this may take some time)...")
similarity = compute_similarity(resumes_df['cleaned_resume'], jobs_df['cleaned_job_desc'])
print("Text similarity computed.")

print("Mapping skills to vectors...")
skill_to_idx = {skill: idx for idx, skill in enumerate(skills_set)}

def skills_to_vector(skills, skill_to_idx):
    vec = np.zeros(len(skill_to_idx), dtype=bool)
    for skill in skills:
        idx = skill_to_idx.get(skill)
        if idx is not None:
            vec[idx] = True
    return vec

print("Creating resume skill vectors...")
resume_skill_vectors = np.array([skills_to_vector(skills, skill_to_idx) for skills in resumes_df['skills']])
print("Creating job skill vectors...")
job_skill_vectors = np.array([skills_to_vector(skills, skill_to_idx) for skills in jobs_df['skills']])

print("Computing skill similarity matrix...")
intersection = np.dot(resume_skill_vectors, job_skill_vectors.T)

resume_skill_counts = resume_skill_vectors.sum(axis=1, keepdims=True)
job_skill_counts = job_skill_vectors.sum(axis=1, keepdims=True).T

union = resume_skill_counts + job_skill_counts - intersection
union = np.where(union == 0, 1, union)

skill_sim_matrix = intersection / union
print("Skill similarity matrix computed.")

print("Combining text and skill similarity...")
combined_similarity = 0.7 * similarity + 0.3 * skill_sim_matrix

top_n = 3

for resume_idx in range(len(resumes_df)):
    top_indices = np.argsort(combined_similarity[resume_idx])[::-1][:top_n]
    print(f"\nTop {top_n} job matches for Resume {resume_idx} ({resumes_df.iloc[resume_idx]['Category']}):")

    for i, job_idx in enumerate(top_indices):
        score = combined_similarity[resume_idx][job_idx]
        title = jobs_df.iloc[job_idx]['Job Title']
        print(f"{i+1}. {title} (Score: {score:.2f})")

print("Script finished.")
