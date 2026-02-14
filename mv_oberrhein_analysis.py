# Starting date: 2025.07.15

import time
start_time = time.time()  # Start the simulation

import pandas as pd

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=DeprecationWarning)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

import pandapower as pp
import matplotlib.pyplot as plt

# .......................... PandaPower ...........................
import pandapower.networks as pn
import pandapower.plotting as plot


# ........................ External functions ........................
# ........................ Functions ........................
# from e_net_mv_20250716 import power_system


# ........................ Power grid ........................
net = pn.mv_oberrhein()
# net.load.drop(index=net.load.index, inplace=True)
net.sgen.drop(index=net.sgen.index, inplace=True)
print("Bus 110kV =\n", net.bus[net.bus['vn_kv'] == 110])
print(net.bus)
# print(len(net.bus))
# print("Trafos: ", net.trafo)
print()

bus_idx = 81
loads_at_bus = net.load[net.load['bus'] == bus_idx]
net.load.drop(loads_at_bus.index, inplace=True)
pp.create_load(net, bus=bus_idx, p_mw=10)
# print(net.load)

# print("Tot bus-bars:", len(net.bus))

bus_demand = net.load.groupby('bus')['p_mw'].mean()
sorted_bus = bus_demand.sort_values(ascending=False)
# print(sorted_bus)
# print()

max_load = sorted_bus.max()
min_load = sorted_bus.min()
max_bus = sorted_bus.idxmax()
min_bus = sorted_bus.idxmin()
# print(f"Bus with max load: {max_bus}, Load: {max_load} MW")
# print(f"Bus with min load: {min_bus}, Load: {min_load} MW")
# print()

# Mapping the busbars bases on connected loads
loads = net.load

industrial_loads = loads[loads['p_mw'] >= 0.50]
# industrial_loads_small = loads[(loads['p_mw'] > 0.4) & (loads['p_mw'] <= 0.60)]
commercial_loads = loads[(loads['p_mw'] > 0.3) & (loads['p_mw'] < 0.50)]
residential_loads = loads[loads['p_mw'] < 0.3]

industrial_buses = industrial_loads['bus'].unique()
# industrial_buses_small = industrial_loads_small['bus'].unique()
commercial_buses = commercial_loads['bus'].unique()
residential_buses = residential_loads['bus'].unique()

# print("Industrial buses:", (industrial_buses))
# # print("Industrial buses_small:", len(industrial_buses_small))
# print("Commercial buses:", (commercial_buses))
# print("Residential buses:", (residential_buses))
# print()


bus_geodata = net.bus_geodata

fig, ax = plt.subplots()
plot.simple_plot(net, ax=ax, bus_size=1.0, line_width=1.5, show_plot=False)

for idx, row in bus_geodata.iterrows():
    # Get the load for this bus, default to 0 if not present
    load = bus_demand.get(idx, 0)
    ax.text(
        row['x'], row['y'],  f"{idx}\n{load:.2f} MW",  # Display load value, str(idx),
        color='red', fontsize=8, ha='center', va='center', zorder=10,
        fontweight='bold', bbox=dict(facecolor='white', alpha=1.0, edgecolor='none', pad=0.5)
    )

plt.show()

# Filter busbars with vn_kv = 110
bus_110kv = net.bus[net.bus['vn_kv'] == 110]
bus_110kv_geodata = bus_geodata.loc[bus_110kv.index]

# Plot the network
fig, ax = plt.subplots()
plot.simple_plot(net, ax=ax, bus_size=1.0, line_width=1.5, show_plot=False)

# Highlight and annotate the 110kV busbars
for idx, row in bus_110kv_geodata.iterrows():
    ax.scatter(row['x'], row['y'], color='red', s=50, zorder=5, label='110kV Bus' if idx == bus_110kv_geodata.index[0] else "")
    ax.text(
        row['x'], row['y'], f"{idx}",
        color='red', fontsize=8, ha='center', va='center', zorder=10,
        fontweight='bold', bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.5)
    )

# Add legend and show the plot
ax.legend()
plt.show()

# # Filter buses with vn_kv below 20 kV
# buses_below_20kv = net.bus[net.bus['vn_kv'] < 20]
#
# # Check if any such buses exist
# if not buses_below_20kv.empty:
#     print(f"Buses with vn_kv below 20 kV:\n{buses_below_20kv}")
# else:
#     print("No buses with vn_kv below 20 kV found.")