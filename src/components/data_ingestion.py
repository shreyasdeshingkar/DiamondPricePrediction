import os
import sys
import logging

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

## Initialize the data ingestion configuration

@dataclass
class DataIngestionconfig:
    train_data_path=os.path.join('artifacts','train.csv')
    test_data_path=os.path.join('artifacts','test.csv')
    raw_data_path=os.path.join('artifacts','raw.csv')

## Create a data ingestion class
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionconfig()
        print(f"Data Ingestion Configuration: {self.ingestion_config}")

    def initiate_data_ingestion(self):
        print('Data Ingestion method starts')
        logging.info('Data Ingestion method starts')

        try:
            print("Attempting to read the dataset...")
            data_file_path = r"D:\DiamondPricePrediction\notebook\data\gemstone.csv"
            print(f"Attempting to read the dataset from: {data_file_path}")
            df = pd.read_csv(data_file_path)
            print("Dataset successfully read as pandas DataFrame.")
            logging.info('Dataset read as pandas DataFrame')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            print(f"Directory {os.path.dirname(self.ingestion_config.raw_data_path)} created.")

            df.to_csv(self.ingestion_config.raw_data_path, index=False)
            print(f"Raw data saved at {self.ingestion_config.raw_data_path}")

            print("Performing train-test split...")
            logging.info("Train-test split")
            train_set, test_set = train_test_split(df, test_size=0.30, random_state=42)
            print("Train-test split completed.")

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            print(f"Train data saved at {self.ingestion_config.train_data_path}")
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            print(f"Test data saved at {self.ingestion_config.test_data_path}")

            logging.info('Ingestion of data is completed')
            print('Ingestion of data is completed')

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except FileNotFoundError as e:
            print(f"Error: The file was not found. Please check the path: {e}")
            logging.error(f"FileNotFoundError: {e}")
            return None, None
        except Exception as e:
            print(f"Error occurred in Data Ingestion: {e}")
            logging.error(f"Error occurred in Data Ingestion: {e}")
            return None, None
