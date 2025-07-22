# match_job_to_resumes.py
import numpy as np
import pandas as pd
import argparse
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Import from our existing modules
from data_loader import load_resumes
from utils import preprocess_text
from skills import load_skills, extract_skills
from skill_vector import skills_to_vector, compute_skill_similarity_matrix

def match_job_to_resumes(job_description, top_n=3, use_skills=True):
    print("Loading BERT model...")
    model = SentenceTransformer("all-MiniLM-L6-v2")
    
    print("Loading resumes...")
    resumes_df = load_resumes('AiRanker/data/resumes/resumes.csv')
    print(f"Loaded {len(resumes_df)} resumes")
    
    print("Preprocessing resumes...")
    resumes_df['cleaned_resume'] = resumes_df['Resume'].apply(preprocess_text)
    
    # Preprocess the input job description
    print("Preprocessing job description...")
    cleaned_job_desc = preprocess_text(job_description)
    print(f"Preprocessed job description: {cleaned_job_desc[:100]}...")
    
    # Compute BERT embeddings
    print("Computing embeddings...")
    resume_texts = resumes_df['cleaned_resume'].tolist()
    resume_embeddings = model.encode(resume_texts, convert_to_numpy=True, show_progress_bar=True)
    job_embedding = model.encode([cleaned_job_desc], convert_to_numpy=True)
    
    # Compute BERT similarity
    bert_sims = cosine_similarity(job_embedding, resume_embeddings)[0]
    
    # If using skills, incorporate skill matching
    if use_skills:
        print("Loading skills...")
        skills_set = load_skills('AiRanker/data/skills/skills.csv')
        
        print("Extracting skills...")
        resumes_df['skills'] = resumes_df['cleaned_resume'].apply(lambda x: extract_skills(x, skills_set))
        job_skills = extract_skills(cleaned_job_desc, skills_set)
        
        print("Vectorizing skills...")
        skill_to_idx = {skill: idx for idx, skill in enumerate(skills_set)}
        resume_skill_vecs = np.array([skills_to_vector(s, skill_to_idx) for s in resumes_df['skills']])
        job_skill_vec = np.array([skills_to_vector(job_skills, skill_to_idx)])
        
        # Compute skill similarity
        skill_sims = cosine_similarity(job_skill_vec, resume_skill_vecs)[0]
        
        # Combine similarities (equal weight)
        combined_sims = 0.5 * bert_sims + 0.5 * skill_sims
    else:
        combined_sims = bert_sims
    
    # Get top matches
    top_indices = combined_sims.argsort()[::-1][:top_n]
    
    print(f"\nTop {top_n} resume matches for the job description:")
    for i, idx in enumerate(top_indices):
        category = resumes_df.iloc[idx]['Category']
        score = combined_sims[idx]
        print(f"{i+1}. Resume {idx} (Category: {category}) - Score: {score:.3f}")
        # Print a snippet of the resume
        resume_snippet = resumes_df.iloc[idx]['Resume'][:200] + "..."
        print(f"   Snippet: {resume_snippet}")
        print(f"   Skills: {', '.join(list(resumes_df.iloc[idx]['skills'])[:10])}")
        print()
    
    return top_indices, combined_sims

def main():
    parser = argparse.ArgumentParser(description='Match a job description to the best resumes')
    parser.add_argument('--job_desc', type=str, help='Job description text')
    parser.add_argument('--job_desc_file', type=str, help='File containing job description')
    parser.add_argument('--top_n', type=int, default=3, help='Number of top matches to return')
    parser.add_argument('--no_skills', action='store_true', help='Disable skill matching')
    
    args = parser.parse_args()
    
    # Get job description from arguments or prompt user
    job_description = ""
    if args.job_desc:
        job_description = args.job_desc
    elif args.job_desc_file:
        with open(args.job_desc_file, 'r', encoding='utf-8') as f:
            job_description = f.read()
    else:
        print("Please enter a job description (type 'END' on a new line when finished):")
        lines = []
        while True:
            line = input()
            if line.strip() == 'END':
                break
            lines.append(line)
        job_description = '\n'.join(lines)
    
    if not job_description.strip():
        print("Error: No job description provided")
        return
    
    match_job_to_resumes(job_description, args.top_n, not args.no_skills)

if __name__ == '__main__':
    main()