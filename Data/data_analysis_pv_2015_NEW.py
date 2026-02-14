import pandas as pd
import numpy as np
from datetime import datetime, timedelta


def analyze_seasonal_pv_data(csv_filename):
    """
    Analyze PV power data for three specific weeks in 2015 and convert to hourly resolution

    Args:
        csv_filename (str): Path to the CSV file containing PV time series data

    Returns:
        pandas.DataFrame: Combined hourly data for all three weeks
    """

    # Read the CSV file
    print(f"Reading data from {csv_filename}...")
    try:
        df = pd.read_csv(csv_filename)
        print(f"Data loaded successfully. Shape: {df.shape}")
        print(f"Columns: {list(df.columns)}")

    except FileNotFoundError:
        print(f"Error: File {csv_filename} not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

    # Get the power column name
    power_col = df.columns[0]  # Should be "pv_data"
    print(f"Power column: {power_col}")
    print(f"Total data points: {len(df)}")

    # Create timestamp index assuming minute resolution starting from 2015-01-01
    start_timestamp = pd.Timestamp('2015-01-01 00:00:00')
    timestamps = pd.date_range(start=start_timestamp, periods=len(df), freq='T')
    df.index = timestamps

    print(f"Data spans from {df.index.min()} to {df.index.max()}")

    # Define the three weeks to extract
    date_ranges = {
        'feb': ('2015-02-15', '2015-02-21 23:59:59'),
        'jun': ('2015-06-15', '2015-06-21 23:59:59'),
        'oct': ('2015-10-15', '2015-10-21 23:59:59')
    }

    weekly_data = {}

    # Extract data for each week
    for week_name, (start_date, end_date) in date_ranges.items():
        print(f"\nProcessing {week_name.upper()} week: {start_date} to {end_date}")

        try:
            # Filter data for the specific week
            week_df = df.loc[start_date:end_date].copy()

            if week_df.empty:
                print(f"No data found for {week_name} week")
                continue

            print(f"  - Data points found: {len(week_df)}")
            print(f"  - Actual date range: {week_df.index.min()} to {week_df.index.max()}")

            # Convert to hourly resolution
            hourly_week = week_df.resample('H').agg({
                power_col: 'mean'
            })

            # Remove hours with insufficient data (less than 30 minutes)
            minute_counts = week_df.resample('H').count()
            hourly_week = hourly_week[minute_counts[power_col] >= 30]

            # Store the hourly data
            weekly_data[week_name] = hourly_week[power_col]

            print(f"  - Hourly data points: {len(hourly_week)}")
            print(f"  - Average power: {hourly_week[power_col].mean():.2f} watts")
            print(f"  - Peak power: {hourly_week[power_col].max():.2f} watts")

        except Exception as e:
            print(f"Error processing {week_name} week: {e}")
            continue

    return weekly_data


def create_combined_dataset(weekly_data):
    """
    Create a combined dataset with all weeks aligned by hour of day

    Args:
        weekly_data (dict): Dictionary containing hourly data for each week

    Returns:
        pandas.DataFrame: Combined dataset with normalized columns
    """

    if not weekly_data:
        print("No weekly data available to combine")
        return None

    print("\nCreating combined dataset...")

    # Create a master dataframe with datetime index covering all weeks
    all_dates = []
    for week_name, data in weekly_data.items():
        all_dates.extend(data.index.tolist())

    # Create combined dataframe
    combined_df = pd.DataFrame(index=sorted(all_dates))

    # Add data for each week
    for week_name, data in weekly_data.items():
        # Power in watts
        col_watts = f'pv_{week_name}_watts'
        combined_df[col_watts] = data

        # Power in kilowatts
        col_kw = f'pv_{week_name}_kw'
        combined_df[col_kw] = data / 1000.0

        # Normalized power (0-1 scale based on week's maximum)
        col_norm = f'pv_{week_name}_norm'
        week_max = data.max()
        if week_max > 0:
            combined_df[col_norm] = data / week_max
        else:
            combined_df[col_norm] = 0

    # Add time-based columns for analysis
    combined_df['hour_of_day'] = combined_df.index.hour
    combined_df['day_of_week'] = combined_df.index.day_name()
    combined_df['date'] = combined_df.index.date
    combined_df['month'] = combined_df.index.month_name()

    print(f"Combined dataset shape: {combined_df.shape}")

    return combined_df


def analyze_seasonal_patterns(combined_df):
    """
    Analyze seasonal patterns in the PV data

    Args:
        combined_df (pandas.DataFrame): Combined dataset
    """

    if combined_df is None:
        return

    print("\n" + "=" * 60)
    print("SEASONAL ANALYSIS RESULTS")
    print("=" * 60)

    # Get the kW columns for analysis
    kw_columns = [col for col in combined_df.columns if col.endswith('_kw')]

    for col in kw_columns:
        week_name = col.replace('pv_', '').replace('_kw', '').upper()
        week_data = combined_df[col].dropna()

        if len(week_data) > 0:
            print(f"\n{week_name} WEEK (Feb/Jun/Oct 15-21, 2015):")
            print(f"  • Total data points: {len(week_data)} hours")
            print(f"  • Average power: {week_data.mean():.3f} kW")
            print(f"  • Peak power: {week_data.max():.3f} kW")
            print(f"  • Total energy: {week_data.sum():.2f} kWh")
            print(f"  • Capacity factor*: {(week_data.mean() / week_data.max() * 100):.1f}%")

            # Daily totals
            daily_totals = combined_df[combined_df[col].notna()].groupby('date')[col].sum()
            print(f"  • Daily energy range: {daily_totals.min():.2f} - {daily_totals.max():.2f} kWh")

            # Peak hour
            hourly_avg = combined_df[combined_df[col].notna()].groupby('hour_of_day')[col].mean()
            peak_hour = hourly_avg.idxmax()
            print(f"  • Peak production hour: {peak_hour}:00 ({hourly_avg.max():.3f} kW avg)")

    print(f"\n* Capacity factor based on week's peak power as reference")

    # Seasonal comparison
    print(f"\n" + "-" * 40)
    print("SEASONAL COMPARISON:")
    print("-" * 40)

    seasonal_stats = {}
    for col in kw_columns:
        week_name = col.replace('pv_', '').replace('_kw', '')
        week_data = combined_df[col].dropna()
        if len(week_data) > 0:
            seasonal_stats[week_name] = {
                'avg_kw': week_data.mean(),
                'peak_kw': week_data.max(),
                'total_kwh': week_data.sum()
            }

    if len(seasonal_stats) > 1:
        # Find best performing week
        best_energy = max(seasonal_stats.items(), key=lambda x: x[1]['total_kwh'])
        best_peak = max(seasonal_stats.items(), key=lambda x: x[1]['peak_kw'])

        print(f"Highest total energy: {best_energy[0].upper()} ({best_energy[1]['total_kwh']:.2f} kWh)")
        print(f"Highest peak power: {best_peak[0].upper()} ({best_peak[1]['peak_kw']:.3f} kW)")

        # Relative performance
        print(f"\nRelative performance (vs best week):")
        for week, stats in seasonal_stats.items():
            energy_ratio = stats['total_kwh'] / best_energy[1]['total_kwh'] * 100
            peak_ratio = stats['peak_kw'] / best_peak[1]['peak_kw'] * 100
            print(f"  {week.upper()}: {energy_ratio:.1f}% energy, {peak_ratio:.1f}% peak")


def create_hourly_comparison_table(combined_df):
    """
    Create a table comparing power output by hour of day across all weeks

    Args:
        combined_df (pandas.DataFrame): Combined dataset

    Returns:
        pandas.DataFrame: Hourly comparison table
    """

    kw_columns = [col for col in combined_df.columns if col.endswith('_kw')]

    # Create hourly averages for each week
    hourly_comparison = pd.DataFrame(index=range(24))
    hourly_comparison.index.name = 'hour_of_day'

    for col in kw_columns:
        week_name = col.replace('pv_', '').replace('_kw', '')
        hourly_avg = combined_df.groupby('hour_of_day')[col].mean()
        hourly_comparison[f'{week_name}_avg_kw'] = hourly_avg

    return hourly_comparison


def plot_seasonal_comparison(combined_df):
    """
    Create plots comparing the three weeks

    Args:
        combined_df (pandas.DataFrame): Combined dataset
    """
    try:
        import matplotlib.pyplot as plt

        # Get kW columns
        kw_columns = [col for col in combined_df.columns if col.endswith('_kw')]

        if len(kw_columns) == 0:
            print("No kW data available for plotting")
            return

        # Create subplots
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('PV Power Analysis - Seasonal Comparison (2015)', fontsize=16, fontweight='bold')

        # Plot 1: Time series for each week
        ax1 = axes[0, 0]
        colors = ['blue', 'green', 'orange']

        for i, col in enumerate(kw_columns):
            week_name = col.replace('pv_', '').replace('_kw', '').upper()
            data = combined_df[col].dropna()
            if len(data) > 0:
                # Create relative time index (hours from start of week)
                hours_from_start = [(t - data.index[0]).total_seconds() / 3600 for t in data.index]
                ax1.plot(hours_from_start, data.values, label=f'{week_name} Week',
                         color=colors[i % len(colors)], linewidth=1.5, alpha=0.8)

        ax1.set_xlabel('Hours from start of week')
        ax1.set_ylabel('Power (kW)')
        ax1.set_title('Weekly Power Generation Profiles')
        ax1.legend()
        ax1.grid(True, alpha=0.3)

        # Plot 2: Average daily patterns
        ax2 = axes[0, 1]
        hourly_comparison = create_hourly_comparison_table(combined_df)

        for i, col in enumerate(hourly_comparison.columns):
            week_name = col.replace('_avg_kw', '').upper()
            ax2.plot(hourly_comparison.index, hourly_comparison[col],
                     marker='o', label=f'{week_name} Week', color=colors[i % len(colors)],
                     linewidth=2, markersize=4)

        ax2.set_xlabel('Hour of Day')
        ax2.set_ylabel('Average Power (kW)')
        ax2.set_title('Average Daily Power Patterns')
        ax2.set_xticks(range(0, 24, 2))
        ax2.legend()
        ax2.grid(True, alpha=0.3)

        # Plot 3: Daily energy totals
        ax3 = axes[1, 0]
        daily_data = []
        week_labels = []

        for col in kw_columns:
            week_name = col.replace('pv_', '').replace('_kw', '').upper()
            daily_totals = combined_df[combined_df[col].notna()].groupby('date')[col].sum()
            if len(daily_totals) > 0:
                daily_data.append(daily_totals.values)
                week_labels.append(week_name)

        if daily_data:
            ax3.boxplot(daily_data, labels=week_labels)
            ax3.set_ylabel('Daily Energy (kWh)')
            ax3.set_title('Daily Energy Distribution by Week')
            ax3.grid(True, alpha=0.3)

        # Plot 4: Normalized comparison
        ax4 = axes[1, 1]
        norm_columns = [col for col in combined_df.columns if col.endswith('_norm')]

        for i, col in enumerate(norm_columns):
            week_name = col.replace('pv_', '').replace('_norm', '').upper()
            hourly_norm = combined_df.groupby('hour_of_day')[col].mean()
            ax4.plot(hourly_norm.index, hourly_norm.values,
                     marker='s', label=f'{week_name} Week', color=colors[i % len(colors)],
                     linewidth=2, markersize=3)

        ax4.set_xlabel('Hour of Day')
        ax4.set_ylabel('Normalized Power (0-1)')
        ax4.set_title('Normalized Daily Patterns')
        ax4.set_xticks(range(0, 24, 2))
        ax4.legend()
        ax4.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.savefig('pv_seasonal_analysis.png', dpi=300, bbox_inches='tight')
        print(f"\nPlot saved as 'pv_seasonal_analysis.png'")
        plt.show()

    except ImportError:
        print("Matplotlib not available. Skipping plot generation.")


if __name__ == "__main__":
    # Configuration
    input_csv = "20210323_PV_time_series.csv"
    output_csv = "input_data_pv_seasonal_comparison_2015.csv"
    hourly_output_csv = "pv_hourly_patterns_2015.csv"

    print("PV Seasonal Analysis Script")
    print("=" * 60)
    print(f"Input file: {input_csv}")
    print(f"Analysis weeks:")
    print(f"  • February 15-21, 2015")
    print(f"  • June 15-21, 2015")
    print(f"  • October 15-21, 2015")
    print(f"Output format: kW and normalized values")
    print("=" * 60)

    # Extract weekly data
    weekly_data = analyze_seasonal_pv_data(input_csv)

    if weekly_data:
        # Create combined dataset
        combined_df = create_combined_dataset(weekly_data)

        if combined_df is not None:
            # Save main results
            combined_df.to_csv(output_csv)
            print(f"\nCombined dataset saved to: {output_csv}")

            # Create and save hourly comparison table
            hourly_comparison = create_hourly_comparison_table(combined_df)
            hourly_comparison.to_csv(hourly_output_csv)
            print(f"Hourly patterns saved to: {hourly_output_csv}")

            # Analyze patterns
            analyze_seasonal_patterns(combined_df)

            # Create plots
            plot_seasonal_comparison(combined_df)

            print(f"\n" + "=" * 60)
            print("ANALYSIS COMPLETE!")
            print("=" * 60)
            print(f"✓ Main output: {output_csv}")
            print(f"✓ Hourly patterns: {hourly_output_csv}")
            print(f"✓ Visualization: pv_seasonal_analysis.png")
            print(f"✓ Total weeks processed: {len(weekly_data)}")

            # Show column summary
            kw_cols = [col for col in combined_df.columns if '_kw' in col]
            norm_cols = [col for col in combined_df.columns if '_norm' in col]
            print(f"✓ Power columns (kW): {', '.join(kw_cols)}")
            print(f"✓ Normalized columns: {', '.join(norm_cols)}")

        else:
            print("Failed to create combined dataset")
    else:
        print("No weekly data extracted. Please check your input file.")