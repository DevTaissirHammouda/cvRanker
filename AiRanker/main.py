import time
from extract_text import extract_text_from_pdf
from preprocess import preprocess_text
from extract_entities_from_cv import CVNER
from chunking import chunk_text
from post_processing import filter_entities

def main():
    try:
        # Path to CV
        pdf_file = "taissirCV.pdf"

        print("Starting CV analysis pipeline...")
        print("-" * 50)

        # Extract text from PDF
        print("Step 1: Extracting text from PDF...")
        raw_text = extract_text_from_pdf(pdf_file)
        print("Extracted Text (sample):\n", raw_text[:300], "...\n")

        # Preprocess text
        print("-" * 50)
        print("Step 2: Preprocessing text...")
        cleaned_text = preprocess_text(raw_text)
        print("Preprocessed Text (sample):\n", cleaned_text[:300], "...\n")

        # Split into chunks
        print("-" * 50)
        print("Step 3: Chunking text...")
        chunks = chunk_text(cleaned_text)
        print(f"Text split into {len(chunks)} chunks.")

        # Perform Named Entity Recognition (NER)
        print("-" * 50)
        print("Step 4: Creating NER instance...")
        cv_ner = CVNER()

        print("-" * 50)
        print("Step 5: Detecting language...")
        language = cv_ner.detect_language(raw_text)  # Use raw text for better language detection
        print(f"Detected Language: {language.upper()}\n")

        # Perform NER on each chunk
        print("-" * 50)
        print("Step 6: Performing Named Entity Recognition...")
        all_entities = []
        for i, chunk in enumerate(chunks):
            print(f"Processing chunk {i + 1}/{len(chunks)}...")
            ner_results = cv_ner.recognize_entities(chunk, language)
            all_entities.extend(ner_results)

        # Filter the entities
        all_entities = filter_entities(all_entities)

        print("\nNER completed.")
        print("-" * 50)
        print("Extracted Named Entities:")

        if not all_entities:
            print("No entities were detected. This might indicate an issue with the model or the input text.")
        else:
            for entity_type, entities in all_entities.items():
                print(f"\n{entity_type}:")
                for entity in entities:
                    print(f"  - {entity}")

        print("\nCV analysis complete!")

    except Exception as e:
        print(f"\nError in CV analysis pipeline: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
