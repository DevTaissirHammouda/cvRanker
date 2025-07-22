import pandas as pd

def load_resumes(path):
    df = pd.read_csv(path)
    # Make sure columns exist
    if 'Category' not in df.columns or 'Resume' not in df.columns:
        raise ValueError("Resumes CSV must have 'Category' and 'Resume' columns")
    return df

def load_jobs(path):
    df = pd.read_csv(path)
    if 'id' not in df.columns or 'Job Title' not in df.columns or 'Job Description' not in df.columns:
        raise ValueError("Jobs CSV must have 'id', 'Job Title', 'Job Description'")
    return df