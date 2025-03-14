import pandas as pd
import os

def clean_dataset(input_file, output_file):
    try:
        # Read the dataset (handle missing headers)
        df = pd.read_csv(input_file, encoding="utf-8", on_bad_lines='skip')  # Changed error_bad_lines to on_bad_lines

        print("Dataset read successfully. Checking columns...")
        print("Columns found:", df.columns.tolist())

        # Ensure required columns exist
        required_columns = ["Resume_str", "Category"]
        for col in ['Resume_str', 'Category']:
            if col not in df.columns:
                raise ValueError(f"Column '{col}' is missing from dataset.")

        # Select only the required columns
        df = df[['Resume_str', 'Category']]

        # Remove missing or empty values
        df = df.dropna(subset=['Resume_str', 'Category'])
        df = df[df['Resume_str'].str.strip() != ""]  # Remove rows with empty Resume_str

        # Basic text cleaning (removing extra spaces)
        df['Resume_str'] = df['Resume_str'].str.replace(r'\s+', ' ', regex=True)

        # Save the cleaned dataset
        df.to_csv(output_file, index=False)

        # Verify if file is created successfully
        if os.path.exists(output_file):
            print(f"✅ Cleaned dataset saved to {output_file} with {len(df)} rows.")
        else:
            print("❌ Error: File not created!")

    except Exception as e:
        print(f"🚨 Error: {e}")
