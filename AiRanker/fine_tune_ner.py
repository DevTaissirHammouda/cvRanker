import pandas as pd
from transformers import (
    Trainer, TrainingArguments, AutoTokenizer, AutoModelForSequenceClassification
)
from datasets import Dataset
from sklearn.preprocessing import LabelEncoder
import torch

def fine_tune_model(csv_path):
    # Detect GPU or CPU
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    # Load dataset
    print("Loading dataset...")
    df = pd.read_csv(csv_path)
    print(df.head())

    # Encode labels
    label_encoder = LabelEncoder()
    df["Category"] = label_encoder.fit_transform(df["Category"])

    # Convert dataset to Hugging Face format
    dataset = Dataset.from_pandas(df)

    # Load pre-trained tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
    model = AutoModelForSequenceClassification.from_pretrained(
        "bert-base-uncased", num_labels=len(label_encoder.classes_)
    ).to(device)  # Move model to GPU/CPU

    # Tokenization function
    def tokenize_function(examples):
        tokens = tokenizer(examples["Resume_str"], padding="max_length", truncation=True)
        tokens["labels"] = examples["Category"]
        return tokens

    # Tokenize dataset
    print("Tokenizing dataset...")
    tokenized_datasets = dataset.map(tokenize_function, batched=True)

    # Split dataset
    train_test_split_ratio = tokenized_datasets.train_test_split(test_size=0.2)
    train_dataset = train_test_split_ratio["train"]
    val_dataset = train_test_split_ratio["test"]

    # Ensure PyTorch tensors are used
    train_dataset.set_format(type="torch", columns=["input_ids", "attention_mask", "labels"])
    val_dataset.set_format(type="torch", columns=["input_ids", "attention_mask", "labels"])

    # Define Training Arguments
    training_args = TrainingArguments(
        output_dir="./results",
        evaluation_strategy="epoch",  # Ensure it's the same as "save_strategy"
        save_strategy="epoch",  # Ensures checkpoint saving matches evaluation
        save_total_limit=2,  # Limit saved checkpoints
        load_best_model_at_end=True,  # Automatically load the best model
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        num_train_epochs=3,
        logging_dir="./logs",
        logging_steps=500,
        metric_for_best_model="accuracy",
        report_to="none",  # Disables W&B and TensorBoard logging
    )

    # Define Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=val_dataset,
    )

    # Train model
    print("Training model...")
    trainer.train()

    # Save best model
    model.save_pretrained("./fine_tuned_bert")
    tokenizer.save_pretrained("./fine_tuned_bert")

    print("✅ Model fine-tuned and saved successfully!")

# Replace with your actual CSV file
