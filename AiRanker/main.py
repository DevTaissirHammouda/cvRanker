from chunking import chunk_text
from extract_entities_from_cv import CVNER
from extract_text import extract_text_from_pdf
from post_processing import filter_entities
from preprocess import preprocess_text
from clean_dataset import clean_dataset
from train_cv_classification_model import train_cv_classification_model  # Import the classification model
import os

def main():
    try:
        # Paths to files
        pdf_file = "taissirCV.pdf"  # Update with the correct path
        input_file = 'Resume.csv'  # Path to your original dataset
        output_file = 'cleaned_dataset.csv'  # Path to save the cleaned dataset

        # Step 1: Clean the dataset
        print("Step 1: Cleaning dataset...")
        clean_dataset(input_file, output_file)

        # Ensure the cleaned dataset exists
        if not os.path.exists(output_file):
            raise FileNotFoundError(f"The cleaned dataset {output_file} was not created successfully.")

        # Step 2: Fine-tune the model on the cleaned dataset
        # print("Step 2: Fine-tuning model...")
        # fine_tune_model(output_file)

        # Step 2: Train and evaluate the BERT-based classification model
        print("Step 2: Training and evaluating the BERT-based model...")
        train_cv_classification_model(output_file)  # Train and evaluate the model using the cleaned dataset

        # Step 3: Start CV analysis pipeline
        print("-" * 50)
        print("Starting CV analysis pipeline...")

        # Extract text from PDF
        print("Step 3: Extracting text from PDF...")
        raw_text = extract_text_from_pdf(pdf_file)
        print("Extracted Text (sample):\n", raw_text[:300], " ...\n")

        # Preprocess text
        print("-" * 50)
        print("Step 4: Preprocessing text...")
        cleaned_text = preprocess_text(raw_text)
        print("Preprocessed Text (sample):\n", cleaned_text[:300], " ...\n")

        # Split into chunks
        print("-" * 50)
        print("Step 5: Chunking text...")
        chunks = chunk_text(cleaned_text)
        print(f"Text split into {len(chunks)} chunks.")

        # Perform Named Entity Recognition (NER)
        print("-" * 50)
        print("Step 6: Creating NER instance...")
        cv_ner = CVNER()

        print("-" * 50)
        print("Step 7: Detecting language...")
        language = cv_ner.detect_language(raw_text)  # Use raw text for better language detection
        print(f"Detected Language: {language.upper()}\n")

        # Perform NER on each chunk
        print("-" * 50)
        print("Step 8: Performing Named Entity Recognition...")
        all_entities = []
        for i, chunk in enumerate(chunks):
            print(f"Processing chunk {i + 1}/{len(chunks)}...")
            ner_results = cv_ner.recognize_entities(chunk, language)
            all_entities.extend(ner_results)

        # Filter the entities
        filtered_entities = filter_entities(all_entities)
        needed_entities = cv_ner.get_needed_entities(filtered_entities)

        print("\nNER completed.")
        print("-" * 50)
        print("Extracted Named Entities:")

        if not needed_entities:
            print("No relevant entities were detected. This might indicate an issue with the model or the input text.")
        else:
            for entity in needed_entities:
                print(f"  - {entity['word']} ({entity['entity']})")

        print("\nCV analysis complete!")

    except Exception as e:
        print(f"\nError in CV analysis pipeline: {e}")
        import traceback
        traceback.print_exc()


# Call the main function directly
main()
