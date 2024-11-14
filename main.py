# main.py

from data_loader import load_login_data
from preprocessor import preprocess_login_data
from visualizer import visualize_daily_logins, visualize_hourly_logins, visualize_logins_by_user


def main():
    # Load data
    df = load_login_data('last_login_data.csv')

    # Preprocess data
    df_preprocessed = preprocess_login_data(df)

    # Check if 'last_login' parsing was successful
    if df_preprocessed.index.isna().any():
        print("Error: There are unparseable dates in 'last_login'. Please check your data.")
        return

    # Visualize data
    visualize_daily_logins(df_preprocessed)
    visualize_hourly_logins(df_preprocessed)
    visualize_logins_by_user(df_preprocessed)


if __name__ == '__main__':
    main()
