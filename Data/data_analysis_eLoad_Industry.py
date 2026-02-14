# 2024.05

import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)

# Load the CSV file
data = pd.read_csv('LoadProfile_30IPs_2017.csv', sep=';', skiprows=1, usecols=range(30))  # Replace 'your_file.csv' with the path to your CSV file
# print(data.head(5))

# Sum every 4 rows to represent each hour
hourly_data = data.groupby(data.index // 4).sum()
hourly_data = hourly_data * 1.039801

# Now hourly_data contains the aggregated values representing each hour
# print(hourly_data.head(24))  # You can optionally print the data to verify

# Calculate the total number of days
total_days = data.shape[0] // 24

# Select days: from day 15 (Jan 15) to day 21 (Jan 21) - 7 days total
start_day = 15
end_day = 22  # Note: end_day is exclusive, so 22 means up to day 21
week_data = hourly_data.iloc[start_day * 24: end_day * 24]

print(week_data)

# Select days: day 15 = January 15; day 197 = July 15
# day = 15
# day_jul_data = hourly_data.iloc[day * 24: (day + 1) * 24]

min_val = week_data['LG 11'].min()
max_val = week_data['LG 11'].max()
week_data['eload_med_ind'] = (week_data['LG 11'] - min_val) / (max_val - min_val)

min_val = week_data['LG 01'].min()
max_val = week_data['LG 01'].max()
week_data['eload_small_ind'] = (week_data['LG 01'] - min_val) / (max_val - min_val)

min_val = week_data['LG 13'].min()
max_val = week_data['LG 13'].max()
week_data['eload_comm'] = (week_data['LG 13'] - min_val) / (max_val - min_val)


# min_val = day_jul_data['LG 07'].min()
# max_val = day_jul_data['LG 07'].max()
# day_jul_data['load7'] = (day_jul_data['LG 07'] - min_val) / (max_val - min_val)
#
# min_val = day_jul_data['LG 08'].min()
# max_val = day_jul_data['LG 08'].max()
# day_jul_data['load8'] = (day_jul_data['LG 08'] - min_val) / (max_val - min_val)

print("Week Data New =\n", week_data.head(5))

week_data.to_csv('data_ind_comm_eloads_days_Jan15_21_normalised_FINAL.csv', index=False)    # [kW/hr]