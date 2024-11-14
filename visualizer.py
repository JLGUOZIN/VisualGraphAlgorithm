# visualizer.py

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def visualize_daily_logins(df):
    """
    Visualize the number of logins per day with reduced x-axis ticks.

    Args:
        df (pd.DataFrame): The preprocessed login data.
    """
    login_counts_per_day = df.resample('D').size()

    plt.figure(figsize=(12, 6))
    login_counts_per_day.plot(kind='bar', color='skyblue')
    plt.title('Daily Login Counts')
    plt.xlabel('Date')
    plt.ylabel('Number of Logins')

    # Set major ticks to show every month
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def visualize_hourly_logins(df):
    """
    Visualize the number of logins per hour.

    Args:
        df (pd.DataFrame): The preprocessed login data.
    """
    login_counts_per_hour = df.resample('h').size()
    plt.figure(figsize=(12, 6))
    login_counts_per_hour.plot()
    plt.title('Hourly Login Counts')
    plt.xlabel('Hour')
    plt.ylabel('Number of Logins')
    plt.tight_layout()
    plt.show()

def visualize_logins_by_user(df):
    """
    Visualize total logins per user.

    Args:
        df (pd.DataFrame): The preprocessed login data.
    """
    login_counts_by_user = df.groupby('buyer_id').size()
    plt.figure(figsize=(10, 6))
    login_counts_by_user.plot(kind='bar')
    plt.title('Total Logins per User')
    plt.xlabel('User ID')
    plt.ylabel('Number of Logins')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def visualize_peak_login_hours(df):
    """
    Visualize peak login hours.

    Args:
        df (pd.DataFrame): The preprocessed login data.
    """
    df['hour'] = df.index.hour
    login_counts_by_hour = df.groupby('hour').size()
    plt.figure(figsize=(10, 6))
    login_counts_by_hour.plot(kind='bar')
    plt.title('Peak Login Hours')
    plt.xlabel('Hour of Day')
    plt.ylabel('Number of Logins')
    plt.tight_layout()
    plt.show()

def preprocess_login_data(df):
    # Validate that 'userid' column exists and is not null
    if 'userid' not in df.columns or df['userid'].isnull().any():
        raise ValueError("'userid' column is missing or contains null values.")
    # Existing preprocessing steps
    # ...
    return df
