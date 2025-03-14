import time
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
import joblib

def train_cv_classification_model(csv_path):
    start_time = time.time()  # Start the timer

    # Step 1: Load and clean the dataset
    df = pd.read_csv(csv_path)
    print("Dataset loaded:", df.head())

    # Ensure the dataset contains the necessary columns
    if 'Resume_str' not in df.columns or 'Category' not in df.columns:
        raise ValueError("Dataset must contain 'Resume_str' and 'Category' columns")

    # Encode the categories (target labels) into numerical values
    label_encoder = LabelEncoder()
    df["category"] = label_encoder.fit_transform(df["Category"])

    # Step 2: Split the dataset into train and validation sets
    train_df, val_df = train_test_split(df, test_size=0.2)

    # Step 3: Text Vectorization (TF-IDF)
    tfidf_vectorizer = TfidfVectorizer(max_features=5000)

    # Fit and transform the training data and transform the validation data
    X_train_tfidf = tfidf_vectorizer.fit_transform(train_df["Resume_str"])
    X_val_tfidf = tfidf_vectorizer.transform(val_df["Resume_str"])

    # Step 4: Prepare the target variable
    y_train = train_df["category"]
    y_val = val_df["category"]

    # Step 5: Train a Logistic Regression model
    print("Training model...")
    train_start = time.time()  # Start timer for training
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train_tfidf, y_train)
    train_end = time.time()  # End timer for training
    print(f"Training completed in {train_end - train_start:.2f} seconds")

    # Step 6: Evaluate the model
    y_pred = model.predict(X_val_tfidf)

    # Step 7: Print evaluation metrics
    accuracy = accuracy_score(y_val, y_pred)
    print("Accuracy:", accuracy)
    print("Classification Report:\n", classification_report(y_val, y_pred, target_names=label_encoder.classes_))

    # Step 8: Save the model and vectorizer
    joblib.dump(model, "cv_classifier_model.pkl")
    joblib.dump(tfidf_vectorizer, "tfidf_vectorizer.pkl")
    print("Model and vectorizer saved successfully!")

    # End the total execution timer
    end_time = time.time()
    print(f"Total execution time: {end_time - start_time:.2f} seconds")

# Run the function with the path to your dataset
