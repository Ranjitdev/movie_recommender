import sys
import os
import pandas as pd
import dill

path = r'notebook/data.csv'

from src.exception import CustomException
from src.logger import logging


def save_obj(file_path, obj):
    try:
        dir_name = os.path.dirname(file_path)
        os.makedirs(dir_name, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
        logging.info(f'File Saved Successfully in {file_path}')
    except Exception as e:
        raise CustomException(e, sys)


def load_obj(file_path):
    try:
        with open(file_path, 'rb') as file_obj:
            logging.info('file loaded successfully sent to pipeline')
            return dill.load(file_obj)
    except Exception as e:
        raise CustomException(e, sys)


class MovieData:
    def __init__(self):
        self.path = path
        self.data = pd.read_csv(path, index_col=None)
        self.columns = self.data.columns
        self.titles = list(self.data['Title'])



