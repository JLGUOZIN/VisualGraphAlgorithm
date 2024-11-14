
# Visual Graph Algorithm - Login Data Analysis and Visualization

## Project Description

This project is a Python-based tool designed to analyze and visualize login data. It processes login data from a CSV file, resamples the data by day and hour, and generates insightful visualizations to observe login trends. This can be particularly useful for applications where understanding user login behavior is important, such as monitoring user engagement.

## Features

- Load and preprocess login data from a CSV file
- Resample login data by day and hour
- Generate visualizations for:
  - Daily login counts
  - Hourly login counts
  - Total logins by user
  - Peak login hours
- Modular code structure to make it easy to extend functionality

## Project Structure

```
VisualGraphAlgorithm/
├── data_loader.py          # Handles loading data from the CSV file
├── preprocessor.py         # Preprocesses data, including datetime parsing and indexing
├── visualizer.py           # Contains functions to generate various visualizations
├── main.py                 # Main script to execute the analysis and visualizations
├── README.md               # Project documentation (this file)
└── requirements.txt        # List of required Python packages
```

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/JLGUOZIN/VisualGraphAlgorithm.git
   cd VisualGraphAlgorithm
   ```

2. **Set Up a Virtual Environment (Optional but Recommended)**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Prepare Your CSV File**:
   - Ensure that your CSV file has at least two columns: `buyer_id` and `last_login`.
   - The `last_login` column should contain timestamps in a format that can be parsed by pandas, ideally in ISO 8601 format.

   **Example CSV Structure**:
   ```
   "buyer_id","last_login"
   "22422","2021-04-25 23:02:51.488"
   ```

2. **Run the Main Script**:
   - Place your CSV file in the project directory.
   - Edit the `main.py` script if necessary to point to your CSV file.
   - Run the script:
     ```bash
     python main.py
     ```

3. **View the Output**:
   - The visualizations for daily logins, hourly logins, total logins per user, and peak hours will be displayed as charts.

## Customization

- **Adjust Date Ranges**: You can modify the date ranges for visualizations in `visualizer.py` functions.
- **Add More Visualizations**: The code is organized in a modular way, making it easy to add new visualizations or analysis types.
- **Change Column Names**: If your CSV file has different column names, update them in `data_loader.py` and `preprocessor.py`.

## Project Files

- **main.py**: The entry point for running the login data analysis and visualization.
- **data_loader.py**: Module for loading the CSV file.
- **preprocessor.py**: Module for data preprocessing, including date parsing and indexing.
- **visualizer.py**: Module containing various visualization functions.

## Dependencies

This project requires the following Python libraries, which are listed in `requirements.txt`:
- pandas
- matplotlib
- seaborn

Install them with:
```bash
pip install -r requirements.txt
```

## Example Visualizations

### Daily Login Counts
This chart shows the number of logins per day, providing a high-level view of daily user activity.

### Hourly Login Counts
This chart displays login counts by hour, helping you understand the times of day when users are most active.

### Total Logins by User
This chart shows the total logins for each user, which can be helpful for identifying your most active users.

### Peak Login Hours
This chart reveals peak login times, showing which hours of the day see the most activity.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements. Make sure to follow the existing code style and include tests for any new features.

## Contact

For any questions or feedback, please reach out to [JEFFREY LAI](mailto:guozin@yahoo.com).
