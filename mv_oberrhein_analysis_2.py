import pandapower.networks as pn
import pandapower as pp
import pandas as pd
import pandapower.topology as top
import networkx as nx

import pandapower.plotting as plot
import matplotlib.pyplot as plt

# pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Load the MV Oberrhein network
net = pn.mv_oberrhein()
print(net.bus)

# ---------------- Plot the network with bus coloring ----------------
# Sum load at each bus
load_bus_p_mw = net.load.groupby('bus')['p_mw'].sum()

# Define bus categories by load
black_buses = load_bus_p_mw[load_bus_p_mw > 0.5].index.tolist()
blue_buses = load_bus_p_mw[load_bus_p_mw < 0.3].index.tolist()
grey_buses = list(set(net.bus.index) - set(black_buses) - set(blue_buses))

# Assign bus colors
bus_colors = []
for idx in net.bus.index:
    if idx in black_buses:
        bus_colors.append("black")
    elif idx in blue_buses:
        bus_colors.append("blue")
    else:
        bus_colors.append("grey")

# Plot network with bus coloring
fig, ax = plt.subplots(figsize=(12, 10))
plot.simple_plot(net, bus_color=bus_colors, ax=ax, show_plot=False)
plt.title("MV Oberrhein Network (Bus Colors by Load)", fontsize=14)
plt.tight_layout()
plt.show()


# # ---------------- New net with new loards ----------------
#
# # Remove all existing loads
# net.load.drop(net.load.index, inplace=True)
#
# # Parameters
# hop_distance = 10   # how many line/trafo steps from trafo LV bus to consider
# load_size = 0.5    # MW
#
# # Create networkx graph (ignore switches for simplicity)
# graph = top.create_nxgraph(net)
#
# # Find LV buses of all transformers
# trafo_lv_buses = net.trafo["lv_bus"].unique()
#
# # Track buses to add loads to
# buses_for_loads = set()
#
# # Find nearby buses for each transformer LV bus
# for lv_bus in trafo_lv_buses:
#     distances = nx.single_source_shortest_path_length(graph, lv_bus, cutoff=hop_distance)
#     buses_for_loads.update(distances.keys())
#
# # Add 0.5 MW loads to each selected bus
# for bus in sorted(buses_for_loads):
#     pp.create_load(net, bus=bus, p_mw=load_size, q_mvar=0)
#
# print(f"Added {len(buses_for_loads)} loads of {load_size} MW each.")
#
# print("Loads =\n", net.load)
#
# # --- Plotting ---
# # Colors: red = new loads, grey = no load
# bus_colors = ["red" if idx in buses_for_loads else "grey" for idx in net.bus.index]
#
# # Get bus coordinates directly from bus_geodata
# bus_coords = {bus: (x, y) for bus, x, y in zip(net.bus_geodata.index,
#                                                net.bus_geodata.x,
#                                                net.bus_geodata.y)}
#
# # Plot network
# fig, ax = plt.subplots(figsize=(12, 10))
# plot.simple_plot(
#     net,
#     bus_color=bus_colors,
#     bus_size=1.2,
#     line_width=0.5,
#     ax=ax,
#     show_plot=False
# )
#
# plt.title("MV Oberrhein - New Load Locations", fontsize=14)
# plt.tight_layout()
# plt.show()