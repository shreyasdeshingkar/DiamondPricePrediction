import os
import sys
import logging

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# Configure logging to display the debug messages in the console
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

@dataclass
class DataIngestionconfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionconfig()
        logging.debug(f"Data Ingestion Configuration: {self.ingestion_config}")

    def initiate_data_ingestion(self):
        logging.info('Data Ingestion method starts')

        try:
            logging.info("Attempting to read the dataset...")
            data_file_path = r"D:\DiamondPricePrediction\\notebook\data\\gemstone.csv"
            logging.debug(f"Attempting to read the dataset from: {data_file_path}")
            df = pd.read_csv(data_file_path)
            logging.info("Dataset successfully read as pandas DataFrame.")

            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            logging.info(f"Directory {os.path.dirname(self.ingestion_config.raw_data_path)} created.")

            # Save the raw data to the defined path
            df.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info(f"Raw data saved at {self.ingestion_config.raw_data_path}")

            # Perform train-test split
            logging.info("Performing train-test split...")
            train_set, test_set = train_test_split(df, test_size=0.30, random_state=42)
            logging.info("Train-test split completed.")

            # Save train and test data to the defined paths
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            logging.info(f"Train data saved at {self.ingestion_config.train_data_path}")
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info(f"Test data saved at {self.ingestion_config.test_data_path}")

            logging.info('Ingestion of data is completed')

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except FileNotFoundError as e:
            logging.error(f"FileNotFoundError: {e}")
            return None, None
        except Exception as e:
            logging.error(f"Error occurred in Data Ingestion: {e}")
            return None, None


