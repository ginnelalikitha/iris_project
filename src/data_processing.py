import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
import os
from src.logger import get_logger
from src.custom_exception import CustomException


logger = get_logger(__name__)

class DataProcessing:

    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None
        self.processed_data_path = "artifacts/processed"
        os.makedirs(self.processed_data_path, exist_ok=True)

    def load_data(self):

        try:
            self.df = pd.read_csv(self.file_path)
            logger.info('Read the data successfully...')
            logger.info(self.df.shape)
            logger.info(self.df.head())
        except Exception as e:
            logger.error(f'Error while loading the data {e}')
            raise CustomException('Failed to read data', e)
    
    
    def run(self):
        self.load_data()
    
if __name__ == "__main__":
    data_processor = DataProcessing('artifacts/raw/data.csv')
    data_processor.run()