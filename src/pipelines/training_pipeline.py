import os
import sys
# from src.logger import logging
# from src.exception import CustomException
import pandas as pd

# from src.components.data_ingestion import DataIngestion

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.data_ingestion import DataIngestion


if __name__ == '__main__':
    obj = DataIngestion()
    train_data_path, test_data_path = obj.initiate_data_ingestion()

    if train_data_path is None or test_data_path is None:
        print("Data ingestion failed.")
    else:
        print(f"Train data path: {train_data_path}")
        print(f"Test data path: {test_data_path}")

    
