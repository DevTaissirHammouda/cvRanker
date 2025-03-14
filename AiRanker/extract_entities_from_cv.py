from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
from langdetect import detect

class CVNER:
    def __init__(self):
        self.model_name = "dbmdz/bert-large-cased-finetuned-conll03-english"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForTokenClassification.from_pretrained(self.model_name)
        self.nlp = pipeline("ner", model=self.model, tokenizer=self.tokenizer)

    def detect_language(self, text):
        return detect(text)

    def recognize_entities(self, text, language):
        # If the language is not English, use a different model (you can load multi-language NER models here)
        if language != 'en':
            print("Non-English text detected, may require different model...")
        # Return NER results
        return self.nlp(text)

    def get_needed_entities(self, entities):
        """Filter and return only the needed entities."""
        needed_labels = ["PER", "ORG", "LOC", "MISC"]  # Adjust this based on needed entities for CV
        filtered_entities = [entity for entity in entities if entity['entity'] in needed_labels]
        return filtered_entities
