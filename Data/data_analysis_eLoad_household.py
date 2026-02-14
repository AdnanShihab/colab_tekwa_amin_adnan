# Collected the original data "data_household_eload_data_5households_Original".
# Set the days in the function, "__name__ == "__main__":"
# Used to normalize the load data.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


class HouseholdPowerAnalyzer:
    def __init__(self, csv_file_path):
        """
        Initialize the analyzer with the CSV file
        """
        self.df = pd.read_csv('data_household_eload_data_5households_Original.csv')
        self.households = self.df.columns.tolist()
        self.total_hours = len(self.df)
        self.total_days = self.total_hours // 24

        print(f"Loaded data for {len(self.households)} households")
        print(f"Total hours: {self.total_hours}")
        print(f"Total days: {self.total_days}")
        print(f"Households: {self.households}")

    def extract_days(self, start_day, end_day):
        """
        Extract data for specific day range

        Parameters:
        start_day (int): Starting day (1-based indexing)
        end_day (int): Ending day (inclusive)

        Returns:
        pandas.DataFrame: Filtered data for the specified days
        """
        if start_day < 1 or end_day > self.total_days:
            raise ValueError(f"Day range must be between 1 and {self.total_days}")

        if start_day > end_day:
            raise ValueError("Start day must be less than or equal to end day")

        # Convert to 0-based indexing for array slicing
        start_hour = (start_day - 1) * 24
        end_hour = end_day * 24

        # Extract the data
        extracted_data = self.df.iloc[start_hour:end_hour].copy()

        # Add time information
        extracted_data['Day'] = [(i // 24) + start_day for i in range(len(extracted_data))]
        extracted_data['Hour'] = [i % 24 for i in range(len(extracted_data))]

        return extracted_data

    def get_daily_summary(self, start_day, end_day):
        """
        Get daily summary statistics for the specified day range
        """
        data = self.extract_days(start_day, end_day)

        daily_summary = []
        for day in range(start_day, end_day + 1):
            day_data = data[data['Day'] == day]
            day_stats = {}
            day_stats['Day'] = day

            for household in self.households:
                household_data = day_data[household]
                # Handle missing values (assuming 0 represents missing data)
                valid_data = household_data[household_data > 0]

                day_stats[f'{household}_total'] = household_data.sum()
                day_stats[f'{household}_avg'] = valid_data.mean() if len(valid_data) > 0 else 0
                day_stats[f'{household}_max'] = valid_data.max() if len(valid_data) > 0 else 0
                day_stats[f'{household}_min'] = valid_data.min() if len(valid_data) > 0 else 0
                day_stats[f'{household}_missing_hours'] = len(household_data[household_data == 0])

            daily_summary.append(day_stats)

        return pd.DataFrame(daily_summary)

    def plot_daily_profiles(self, start_day, end_day, households=None):
        """
        Plot daily consumption profiles for specified days and households
        """
        if households is None:
            households = self.households

        data = self.extract_days(start_day, end_day)

        fig, axes = plt.subplots(len(households), 1, figsize=(12, 3 * len(households)))
        if len(households) == 1:
            axes = [axes]

        for idx, household in enumerate(households):
            for day in range(start_day, end_day + 1):
                day_data = data[data['Day'] == day]
                hours = day_data['Hour']
                consumption = day_data[household]

                # Replace 0 values with NaN for better visualization
                consumption_clean = consumption.replace(0, np.nan)

                axes[idx].plot(hours, consumption_clean, label=f'Day {day}', marker='o', markersize=3)

            axes[idx].set_title(f'{household} - Daily Consumption Profile')
            axes[idx].set_xlabel('Hour of Day')
            axes[idx].set_ylabel('Power Consumption')
            axes[idx].grid(True, alpha=0.3)
            axes[idx].legend()
            axes[idx].set_xlim(0, 23)

        plt.tight_layout()
        plt.show()

    def export_extracted_data(self, start_day, end_day, output_file):
        """
        Export extracted data to CSV file
        """
        data = self.extract_days(start_day, end_day)
        data.to_csv(output_file, index=False)
        print(f"Data exported to {output_file}")


# Example usage
if __name__ == "__main__":
    # Initialize the analyzer
    analyzer = HouseholdPowerAnalyzer('data_household_eload_data_5households_Original.csv')

    # Extract data for days 315 to 321
    start_day = 315
    end_day = 321

    print(f"\nExtracting data for days {start_day} to {end_day}...")

    # Get the extracted data
    extracted_data = analyzer.extract_days(start_day, end_day)
    print(f"Extracted {len(extracted_data)} hours of data")

    # Display first few rows
    print("\nFirst 10 rows of extracted data:")
    print(extracted_data.head(10))

    # Get daily summary
    print(f"\nDaily summary for days {start_day} to {end_day}:")
    daily_summary = analyzer.get_daily_summary(start_day, end_day)
    print(daily_summary)

    # Plot daily profiles
    analyzer.plot_daily_profiles(start_day, end_day)

    # Export to CSV
    analyzer.export_extracted_data(start_day, end_day, f'extracted_days_{start_day}_to_{end_day}.csv')

    # Example: Extract data for a single household
    print(f"\nSFH10 consumption for days {start_day} to {end_day}:")
    sfh10_data = extracted_data[['Day', 'Hour', 'SFH10']]
    print(sfh10_data)

# Initialize with your CSV file
analyzer = HouseholdPowerAnalyzer('household_eload_data_5HH.csv')

# Extract data for days 315-321
data = analyzer.extract_days(315, 321)

# Get daily summary statistics
summary = analyzer.get_daily_summary(315, 321)


# Plot consumption profiles
# analyzer.plot_daily_profiles(315, 321)

# Export extracted data
analyzer.export_extracted_data(315, 321, 'data_HH_loads_days_315_321.csv')


# Function to normalize exported data
def normalize_exported_data(input_file, output_file):
    # Read the exported CSV file
    df = pd.read_csv(input_file)

    # Identify numeric columns to normalize
    numeric_columns = df.select_dtypes(include=['number']).columns

    # Apply Min-Max normalization
    for column in numeric_columns:
        min_val = df[column].min()
        max_val = df[column].max()

        # Avoid division by zero
        if max_val > min_val:
            df[column] = (df[column] - min_val) / (max_val - min_val)
        else:
            df[column] = 0  # If all values are the same, set to 0

    # Save the normalized data to a new CSV file
    df.to_csv(output_file, index=False)
    print(f"Normalized data exported to {output_file}")


# Example usage
normalize_exported_data('data_HH_loads_days_315_321.csv', 'data_HH_loads_days_315_321_normalised.csv')
