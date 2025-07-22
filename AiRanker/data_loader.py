#data_loader
import pandas as pd

def load_resumes(path):
    df = pd.read_csv(path)
    if 'Category' not in df.columns or 'Resume' not in df.columns:
        raise ValueError("Resumes CSV must have 'Category' and 'Resume' columns")

    # Drop rows where 'Resume' is null
    df = df.dropna(subset=['Resume'])
    return df

def load_jobs(path):
    df = pd.read_csv(path)
    if 'id' not in df.columns or 'Job Title' not in df.columns or 'Job Description' not in df.columns:
        raise ValueError("Jobs CSV must have 'id', 'Job Title', 'Job Description'")
    
    # Drop rows where 'Job Description' is null
    df = df.dropna(subset=['Job Description'])
    return df

def load_skills(path):
    df = pd.read_csv(path)
    if 'Skill' not in df.columns:
        raise ValueError("CSV must contain a 'Skill' column")

    skills = (
        df['Skill']
        .dropna()
        .str.strip()
        .str.lower()
        .str.replace(r'[^a-z0-9+.# ]', '', regex=True)
        .unique()
        .tolist()
    )

    return set(skills)
