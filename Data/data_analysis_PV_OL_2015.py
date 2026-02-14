# Copilot with model Cloud Sonnet 4 - Analyze PV Power Data from January 15-22, 2015

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

csv_filename = pd.read_csv("20210323_PV_time_series.csv")


def analyze_pv_data(csv_filename):
    """
    Analyze PV power data: filter for Jan 15-22, 2015 and convert to hourly resolution

    Args:
        csv_filename (str): Path to the CSV file containing PV time series data

    Returns:
        pandas.DataFrame: Hourly averaged PV power data for the specified date range
    """

    # Read the CSV file
    print(f"Reading data from {csv_filename}...")
    try:
        # Assuming the CSV has columns like 'timestamp' and 'power_watts'
        # Adjust column names based on your actual CSV structure
        df = pd.read_csv(csv_filename)
        print(f"Data loaded successfully. Shape: {df.shape}")
        print(f"Columns: {list(df.columns)}")

    except FileNotFoundError:
        print(f"Error: File {csv_filename} not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

    # Display first few rows to understand the data structure
    print("\nFirst 5 rows of data:")
    print(df.head())

    # Since there's only one column with power data, we need to create timestamps
    # Assuming minute resolution starting from 2015-01-01 00:00:00
    power_col = df.columns[0]  # This should be "pv_data"

    print(f"\nPower column: {power_col}")
    print(f"Total data points: {len(df)}")

    # Create timestamp index assuming minute resolution starting from 2015-01-01
    start_timestamp = pd.Timestamp('2015-01-01 00:00:00')
    timestamps = pd.date_range(start=start_timestamp, periods=len(df), freq='T')  # 'T' = minute frequency

    # Set the timestamp as index
    df.index = timestamps

    print(f"Data spans from {df.index.min()} to {df.index.max()}")

    # Filter for January 15-22, 2015
    start_date = '2015-01-15 00:00:00'
    end_date = '2015-01-22 23:59:59'

    print(f"\nFiltering data for {start_date} to {end_date}...")

    try:
        filtered_df = df.loc[start_date:end_date].copy()
    except KeyError:
        print("Date range not found in data. Let me check what dates are available...")
        print(f"Available date range: {df.index.min()} to {df.index.max()}")

        # Check if January 15-22 exists in the data
        jan_15 = pd.Timestamp('2015-01-15')
        jan_22 = pd.Timestamp('2015-01-22 23:59:59')

        if df.index.max() < jan_15:
            print("Error: Data ends before January 15, 2015")
            return None
        elif df.index.min() > jan_22:
            print("Error: Data starts after January 22, 2015")
            return None
        else:
            # Adjust the date range to what's available
            actual_start = max(df.index.min(), jan_15)
            actual_end = min(df.index.max(), jan_22)
            filtered_df = df.loc[actual_start:actual_end].copy()
            print(f"Adjusted filter range to: {actual_start} to {actual_end}")

    if filtered_df.empty:
        print("No data found for the specified date range.")
        return None

    print(f"Filtered data shape: {filtered_df.shape}")
    print(f"Date range in filtered data: {filtered_df.index.min()} to {filtered_df.index.max()}")

    # Convert from minute resolution to hourly resolution
    print("\nConverting to hourly resolution...")

    # Resample to hourly frequency using mean
    hourly_df = filtered_df.resample('H').agg({
        power_col: ['mean', 'max', 'min', 'std', 'count']
    })

    # Flatten column names
    hourly_df.columns = ['power_mean_jan_normalised', 'power_max_normalised', 'power_min_normalised',
                         'power_std_normalised', 'data_points_count']

    # Remove hours with insufficient data (less than 30 minutes of data)
    hourly_df = hourly_df[hourly_df['data_points_count'] >= 30]

    print(f"Hourly data shape: {hourly_df.shape}")

    return hourly_df


def save_results(hourly_data, output_filename):
    """
    Save the hourly data to a CSV file

    Args:
        hourly_data (pandas.DataFrame): Hourly PV power data
        output_filename (str): Output CSV filename
    """
    if hourly_data is not None:
        hourly_data.to_csv(output_filename)
        print(f"\nHourly data saved to {output_filename}")

        # Display summary statistics
        print("\nSummary Statistics:")
        print(hourly_data.describe())

        # Display the actual data
        print(f"\nHourly PV Power Data (Jan 15-22, 2015):")
        print(hourly_data)


def plot_results(hourly_data):
    """
    Create a simple plot of the hourly PV power data

    Args:
        hourly_data (pandas.DataFrame): Hourly PV power data
    """
    try:
        import matplotlib.pyplot as plt

        plt.figure(figsize=(12, 6))
        plt.plot(hourly_data.index, hourly_data['power_mean_watts'],
                 marker='o', linewidth=2, markersize=4)
        plt.fill_between(hourly_data.index,
                         hourly_data['power_min_watts'],
                         hourly_data['power_max_watts'],
                         alpha=0.3, label='Min-Max Range')

        plt.title('PV Power Generation - Hourly Average (Jan 15-22, 2015)')
        plt.xlabel('Date and Time')
        plt.ylabel('Power (Watts)')
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    except ImportError:
        print("Matplotlib not available. Skipping plot generation.")


if __name__ == "__main__":
    # Configuration
    input_csv = "20210323_PV_time_series.csv"
    output_csv = "pv_hourly_data_jan15_22_2015_normalised.csv"

    # Analyze the data
    hourly_data = analyze_pv_data(input_csv)

    if hourly_data is not None:
        # Save results
        save_results(hourly_data, output_csv)

        # Create a plot (optional)
        # plot_results(hourly_data)

        print(f"\nAnalysis complete!")
        print(f"- Input file: {input_csv}")
        print(f"- Output file: {output_csv}")
        print(f"- Date range: January 15-22, 2015")
        print(f"- Resolution: Converted from minutes to hours")
        print(f"- Total hourly data points: {len(hourly_data)}")
    else:
        print("Analysis failed. Please check your input file and try again.")