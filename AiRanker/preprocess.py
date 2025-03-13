import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download required NLTK datasets
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")

def preprocess_text(text):
    # Remove special characters and extra spaces
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = text.lower()  # Convert to lowercase

    # Tokenization
    words = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word not in stop_words]

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]

    return " ".join(words)

# Example Usage
raw_text = "John Doe, Software Engineer. Skills: Python, Java, AI."
cleaned_text = preprocess_text(raw_text)
print(cleaned_text)
