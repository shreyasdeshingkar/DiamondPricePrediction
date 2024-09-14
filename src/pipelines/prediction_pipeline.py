import sys
import os
from logger import logging
from src.utils import load_object
import pandas as pd

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            # Paths to preprocessor and model
            preprocessor_path = os.path.join('D:\DiamondPricePrediction\\src\\pipelines\\artifacts\\preprocessor.pkl')
            model_path = os.path.join('D:\DiamondPricePrediction\\src\\pipelines\\artifacts\\model.pkl')

            # Load preprocessor and model
            preprocessor = load_object(preprocessor_path)
            if preprocessor is None:
                logging.error(f"Failed to load preprocessor from {preprocessor_path}")
                return None

            model = load_object(model_path)
            if model is None:
                logging.error(f"Failed to load model from {model_path}")
                return None

            # Transform features and make predictions
            data_scaled = preprocessor.transform(features)
            pred = model.predict(data_scaled)
            return pred

        except Exception as e:
            logging.exception(f"Exception occurred in prediction: {str(e)}")
            return None


class CustomData:
    def __init__(self,
                 carat: float,
                 depth: float,
                 table: float,
                 x: float,
                 y: float,
                 z: float,
                 cut: str,
                 color: str,
                 clarity: str):
        
        self.carat = carat
        self.depth = depth
        self.table = table
        self.x = x
        self.y = y
        self.z = z
        self.cut = cut
        self.color = color
        self.clarity = clarity

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'carat': [self.carat],
                'depth': [self.depth],
                'table': [self.table],
                'x': [self.x],
                'y': [self.y],
                'z': [self.z],
                'cut': [self.cut],
                'color': [self.color],
                'clarity': [self.clarity]
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        except Exception as e:
            logging.exception(f"Exception occurred in get_data_as_dataframe: {str(e)}")
            return None
