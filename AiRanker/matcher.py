# matcher.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def compute_similarity(resumes, jobs):
    """
    resumes: pd.Series of cleaned resumes
    jobs: pd.Series of cleaned job descriptions
    Returns: similarity matrix (resumes x jobs)
    """
    all_docs = pd.concat([resumes, jobs])
    vectorizer = TfidfVectorizer(max_features=5000)
    tfidf_matrix = vectorizer.fit_transform(all_docs)

    resume_vecs = tfidf_matrix[:len(resumes)]
    job_vecs = tfidf_matrix[len(resumes):]

    similarity_matrix = cosine_similarity(resume_vecs, job_vecs)
    
    return similarity_matrix
