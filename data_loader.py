# data_loader.py

import pandas as pd

def load_login_data(file_path):
    """
    Load login data from a CSV file.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: DataFrame containing the login data.
    """
    try:
        df = pd.read_csv(file_path, parse_dates=['last_login'])
        return df
    except Exception as e:
        raise Exception(f"Error loading data: {e}")
