# Could Sonnet 4 analyze wind power data from 2019, extracting and normalizing specific weeks
# Feb 15-21, Jun 15-21, and Oct 15-21

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler


def extract_and_normalize_weeks(filename):
    """
    Simple function to extract and normalize specific weeks
    """
    # Load data
    df = pd.read_csv(filename)

    # Create datetime index
    start_date = '2019-01-01 00:00:00'
    datetime_index = pd.date_range(start=start_date, periods=len(df), freq='H')
    df.index = datetime_index

    # Define weeks to extract
    weeks = [
        {"start": "2019-02-15", "end": "2019-02-21", "label": "feb"},
        {"start": "2019-06-15", "end": "2019-06-21", "label": "jun"},
        {"start": "2019-10-15", "end": "2019-10-21", "label": "oct"}
    ]

    # Initialize result dataframe
    result_data = {}

    for week in weeks:
        # Extract week data
        mask = (df.index >= week["start"]) & (df.index <= week["end"] + ' 23:59:59')
        week_data = df.loc[mask]['wt_power'].values

        # Normalize using min-max
        scaler = MinMaxScaler()
        week_data_norm = scaler.fit_transform(week_data.reshape(-1, 1)).flatten()

        # Add to result
        result_data[f'wt_power_{week["label"]}'] = week_data
        result_data[f'wt_power_{week["label"]}_norm'] = week_data_norm

        print(f"{week['label'].upper()} week ({week['start']} to {week['end']}):")
        print(f"  Original range: {week_data.min():.3f} - {week_data.max():.3f} kW")
        print(f"  Normalized range: {week_data_norm.min():.3f} - {week_data_norm.max():.3f}")
        print()

    # Create DataFrame
    # Find maximum length to handle different week lengths
    max_len = max(len(v) for v in result_data.values())

    # Pad shorter arrays with NaN
    for key, values in result_data.items():
        if len(values) < max_len:
            padded = np.full(max_len, np.nan)
            padded[:len(values)] = values
            result_data[key] = padded

    result_df = pd.DataFrame(result_data)

    # Save to CSV
    result_df.to_csv('input_data_wind_power_normalized_weeks.csv', index=False)
    print("Data saved to: input_data_wind_power_normalized_weeks.csv")

    return result_df


# Run the extraction
if __name__ == "__main__":
    filename = "wind_power_kw_ninja_main.csv"
    df = extract_and_normalize_weeks(filename)
    print("\nFirst 10 rows of the result:")
    print(df.head(10))