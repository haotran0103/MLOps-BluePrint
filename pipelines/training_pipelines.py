import logging
from zenml import pipeline
from steps.ingestion_data import ingest_data
from steps.model_train import train_model
from steps.clean_data import preprocess_data
from steps.evaluation import evaluation

@pipeline
def train_pipeline(data_path: str):
    df = ingest_data(data_path)
    preprocess_data(df)
    train_model(df)
    evaluation(df)