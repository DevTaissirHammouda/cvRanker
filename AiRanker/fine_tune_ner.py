from transformers import Trainer, TrainingArguments, AutoTokenizer, AutoModelForTokenClassification
from datasets import load_dataset

def fine_tune_model(dataset_path):
    # Load the CV dataset
    dataset = load_dataset(dataset_path)

    # Load the pre-trained model and tokenizer
    tokenizer = AutoTokenizer.from_pretrained("dbmdz/bert-large-cased-finetuned-conll03-english")
    model = AutoModelForTokenClassification.from_pretrained("dbmdz/bert-large-cased-finetuned-conll03-english")

    # Tokenize and prepare dataset
    def tokenize_function(examples):
        return tokenizer(examples["text"], padding="max_length", truncation=True)

    tokenized_datasets = dataset.map(tokenize_function, batched=True)

    # Training arguments
    training_args = TrainingArguments(
        output_dir="./results",
        evaluation_strategy="epoch",
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        num_train_epochs=3,
        logging_dir="./logs",
    )

    # Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_datasets["train"],
        eval_dataset=tokenized_datasets["test"],
    )

    # Fine-tune the model
    trainer.train()

if __name__ == "__main__":
    fine_tune_model("path_to_your_dataset")
