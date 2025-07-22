import numpy as np

def skills_to_vector(skills, skill_to_idx):
    vec = np.zeros(len(skill_to_idx), dtype=bool)
    for skill in skills:
        idx = skill_to_idx.get(skill)
        if idx is not None:
            vec[idx] = True
    return vec

def compute_skill_similarity_matrix(resume_skill_vectors, job_skill_vectors):
    intersection = np.dot(resume_skill_vectors, job_skill_vectors.T)
    resume_counts = resume_skill_vectors.sum(axis=1, keepdims=True)
    job_counts = job_skill_vectors.sum(axis=1, keepdims=True).T
    union = resume_counts + job_counts - intersection
    union = np.where(union == 0, 1, union)
    return intersection / union
