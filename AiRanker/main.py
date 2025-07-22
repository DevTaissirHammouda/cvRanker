from data_loader import *
from utils import *
from matcher_tfidf import *
from matcher_bert import *
from skill_vector import *
from ranking import *
from skills import *
import numpy as np

def main():
    print("Loading resumes...")
    resumes_df = load_resumes('AiRanker/data/resumes/resumes.csv')
    print(f"{len(resumes_df)} resumes loaded.")

    print("Loading jobs...")
    jobs_df = load_jobs('AiRanker/data/jobs/jobs.csv')
    print(f"{len(jobs_df)} jobs loaded.")

    print("Preprocessing text...")
    resumes_df['cleaned_resume'] = resumes_df['Resume'].apply(preprocess_text)
    jobs_df['cleaned_job_desc'] = jobs_df['Job Description'].apply(preprocess_text)

    print("Loading skills...")
    skills_set = load_skills('AiRanker/data/skills/skills.csv')

    print("Extracting skills...")
    resumes_df['skills'] = resumes_df['cleaned_resume'].apply(lambda x: extract_skills(x, skills_set))
    jobs_df['skills'] = jobs_df['cleaned_job_desc'].apply(lambda x: extract_skills(x, skills_set))

    print("Vectorizing skills...")
    skill_to_idx = {skill: idx for idx, skill in enumerate(skills_set)}
    resume_skill_vecs = np.array([skills_to_vector(s, skill_to_idx) for s in resumes_df['skills']])
    job_skill_vecs = np.array([skills_to_vector(s, skill_to_idx) for s in jobs_df['skills']])

    print("Computing skill similarity matrix...")
    skill_sim_matrix = compute_skill_similarity_matrix(resume_skill_vecs, job_skill_vecs)

    print("Computing TF-IDF similarity...")
    tfidf_sim = compute_tfidf_similarity(resumes_df['cleaned_resume'], jobs_df['cleaned_job_desc'])

    print("Computing SBERT similarity...")
    bert_sim = compute_bert_similarity(resumes_df['cleaned_resume'], jobs_df['cleaned_job_desc'])

    print("Combining similarities...")
    tfidf_combined = combine_similarities(tfidf_sim, skill_sim_matrix)
    bert_combined = combine_similarities(bert_sim, skill_sim_matrix)

    top_n = 3
    tfidf_top_matches = get_top_matches(tfidf_combined, top_n)
    bert_top_matches = get_top_matches(bert_combined, top_n)

    for i in range(len(resumes_df)):
        print(f"\nResume {i} ({resumes_df.iloc[i]['Category']}):")
        print("  TF-IDF Top Matches:")
        for rank, (job_idx, score) in enumerate(tfidf_top_matches[i], 1):
            print(f"    {rank}. {jobs_df.iloc[job_idx]['Job Title']} (Score: {score:.3f})")
        print("  SBERT Top Matches:")
        for rank, (job_idx, score) in enumerate(bert_top_matches[i], 1):
            print(f"    {rank}. {jobs_df.iloc[job_idx]['Job Title']} (Score: {score:.3f})")

if __name__ == '__main__':
    main()
