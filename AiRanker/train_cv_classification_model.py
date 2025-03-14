import time
import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report

def train_cv_classification_model(csv_path):
    start_time = time.time()  # Start timing

    # Load cleaned dataset
    df = pd.read_csv(csv_path)
    print(f"✅ Dataset loaded with {len(df)} rows. Preparing training...")

    # Encode categories
    label_encoder = LabelEncoder()
    df["category"] = label_encoder.fit_transform(df["Category"])

    # Split into train/validation sets
    train_df, val_df = train_test_split(df, test_size=0.2, stratify=df["category"])

    # TF-IDF Vectorization with bigrams and 10,000 features
    tfidf_vectorizer = TfidfVectorizer(max_features=10000, ngram_range=(1, 2))
    X_train_tfidf = tfidf_vectorizer.fit_transform(train_df["Resume_str"])
    X_val_tfidf = tfidf_vectorizer.transform(val_df["Resume_str"])

    y_train = train_df["category"]
    y_val = val_df["category"]

    # Train XGBoost model
    print("🚀 Training XGBoost model...")
    train_start = time.time()
    model = XGBClassifier(n_estimators=200, max_depth=6, learning_rate=0.05)
    model.fit(X_train_tfidf, y_train)
    train_end = time.time()
    print(f"✅ Training completed in {train_end - train_start:.2f} seconds")

    # Evaluate model
    y_pred = model.predict(X_val_tfidf)
    accuracy = accuracy_score(y_val, y_pred)
    print(f"🎯 Model Accuracy: {accuracy:.4f}")
    print("📊 Classification Report:\n", classification_report(y_val, y_pred, target_names=label_encoder.classes_))

    # Save model & vectorizer
    joblib.dump(model, "models/cv_classifier_model.pkl")
    joblib.dump(tfidf_vectorizer, "models/tfidf_vectorizer.pkl")
    print("✅ Model and vectorizer saved!")

    # Total execution time
    end_time = time.time()
    print(f"⏳ Total execution time: {end_time - start_time:.2f} seconds")
