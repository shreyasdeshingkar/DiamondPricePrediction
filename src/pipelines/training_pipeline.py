import os
import sys
import pandas as pd
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import save_object

from components.data_ingestion import DataIngestion
from components.data_transformation import DataTransformation, DataTransformationConfig
from components.model_trainer import ModelTrainer

if __name__ == '__main__':
    obj = DataIngestion()
    train_data_path, test_data_path = obj.initiate_data_ingestion()

    if train_data_path is None or test_data_path is None:
        print("Data ingestion failed.")
    else:
        print(f"Train data path: {train_data_path}")
        print(f"Test data path: {test_data_path}")

    # Pass the DataTransformationConfig instance to DataTransformation
    config = DataTransformationConfig()
    data_transformation = DataTransformation(config=config)

    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data_path, test_data_path)

    model_trainer = ModelTrainer()
    model_trainer.initiate_model_training(train_arr, test_arr)








