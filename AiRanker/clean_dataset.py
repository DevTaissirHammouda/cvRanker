import pandas as pd
import os
import nltk
from nltk.corpus import stopwords
from imblearn.over_sampling import SMOTE

nltk.download('stopwords')
STOPWORDS = set(stopwords.words('english'))

def clean_dataset(input_file, output_file):
    try:
        # Load dataset
        df = pd.read_csv(input_file, encoding="utf-8", on_bad_lines='skip')

        print(f"✅ Dataset loaded with {len(df)} rows. Cleaning started...")

        # Ensure required columns
        if 'Resume_str' not in df.columns or 'Category' not in df.columns:
            raise ValueError("Dataset must contain 'Resume_str' and 'Category' columns")

        # Remove duplicates
        df = df.drop_duplicates()

        # Remove stopwords from resumes
        df['Resume_str'] = df['Resume_str'].apply(lambda text: ' '.join([word for word in text.split() if word.lower() not in STOPWORDS]))

        # Handle missing values
        df = df.dropna(subset=['Resume_str', 'Category'])
        df = df[df['Resume_str'].str.strip() != ""]

        # Fix imbalanced data using SMOTE
        smote = SMOTE()
        X_resampled, y_resampled = smote.fit_resample(df[['Resume_str']], df['Category'])
        df = pd.DataFrame({'Resume_str': X_resampled['Resume_str'], 'Category': y_resampled})

        # Save cleaned dataset
        df.to_csv(output_file, index=False)

        print(f"✅ Cleaned dataset saved to {output_file} with {len(df)} rows.")

    except Exception as e:
        print(f"🚨 Error in dataset cleaning: {e}")
