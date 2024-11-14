# preprocessor.py

import pandas as pd

def preprocess_login_data(df):
    """
    Preprocess the login data.

    Args:
        df (pd.DataFrame): The login data DataFrame.

    Returns:
        pd.DataFrame: Preprocessed DataFrame.
    """
    try:
        # Attempt to parse using ISO8601 format (for pandas >= 2.0)
        df['last_login'] = pd.to_datetime(df['last_login'], format='ISO8601')
    except ValueError:
        # Fallback for older pandas versions or if parsing fails
        df['last_login'] = pd.to_datetime(df['last_login'], infer_datetime_format=True)

    # Set 'last_login' as the index
    df.set_index('last_login', inplace=True)
    return df
