# pylint: disable=import-error
import os
import sys

import numpy as np
import dill
import yaml
from pandas import DataFrame

from us_visa.exception import USvisaException
from us_visa.logger import logging




def read_yaml_file(file_path: str) -> dict:
    '''
    The selected code is a function named read_yaml_file that reads a YAML file and returns its content as a dictionary. It uses the yaml library to load the YAML file in a secure manner. 
    '''
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise USvisaException(e, sys) from e


def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    '''
    The selected code is a function named write_yaml_file that writes a YAML file with the given content. It takes three parameters: file_path (the path of the file to be written), content (the content to be written in the YAML file), and replace (a boolean value that specifies whether to replace the existing file if it already exists).
    '''

    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w",encoding = "UTF-8") as file:
            yaml.dump(content, file)
    except Exception as e:
        raise USvisaException(e, sys) from e


def load_object(file_path: str) -> object:
    '''
    The selected code is a function named load_object that reads a serialized object from a file using the dill library. The function takes a file path as input and returns the deserialized object. It also logs an informational message when entering and exiting the function. If an exception occurs during the process, it raises a USvisaException with the appropriate error message and traceback.
    '''
    logging.info("Entered the load_object method of utils")

    try:

        with open(file_path, "rb") as file_obj:
            obj = dill.load(file_obj)

        logging.info("Exited the load_object method of utils")

        return obj

    except Exception as e:
        raise USvisaException(e, sys) from e

def save_numpy_array_data(file_path: str, array: np.array):
    """
    Save numpy array data to file
    file_path: str location of file to save
    array: np.array data to save
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise USvisaException(e, sys) from e


def load_numpy_array_data(file_path: str) -> np.array:
    """
    load numpy array data from file
    file_path: str location of file to load
    return: np.array data loaded
    """
    try:
        with open(file_path, 'rb') as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise USvisaException(e, sys) from e


def save_object(file_path: str, obj: object) -> None:
    logging.info("Entered the save_object method of utils")

    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

        logging.info("Exited the save_object method of utils")

    except Exception as e:
        raise USvisaException(e, sys) from e


def drop_columns(df: DataFrame, cols: list)-> DataFrame:

    """
    drop the columns form a pandas DataFrame
    df: pandas DataFrame
    cols: list of columns to be dropped
    """
    logging.info("Entered drop_columns method of utils")

    try:
        df = df.drop(columns=cols, axis=1)

        logging.info("Exited the drop_columns method of utils")
        
        return df
    except Exception as e:
        raise USvisaException(e, sys) from e