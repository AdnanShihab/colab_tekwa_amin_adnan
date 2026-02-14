import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import pandapower as pp
import pandapower.networks as pn
import pandapower.topology as top
import pandapower.plotting as plot

# Optional display config
pd.set_option('display.max_rows', None)

# -----------------------------
# Parameters you can tune
# -----------------------------
# Industrial clustering radius (in number of graph hops from trafo LV buses)
hop_distance = 6  # smaller => leaves more buses for res/com

# Load sizes (MW)
ind_p = 0.50
res_p = 0.25
com_p = 0.40

# Power factors
pf_ind = 0.95
pf_res = 0.98
pf_com = 0.95

# k-NN neighbors for spatial density
knn_k_default = 5
dens_percentile_for_commercial = 60  # top 40% density => commercial

# Buses to keep unclassified (no loads)
excluded_buses = {298, 248, 253, 85, 33, 83, 317, 41, 37, 76,
                  82, 31, 238, 40, 247, 237,

                  192, 56, 50, 34,

                  36}


# -----------------------------
# Helpers
# -----------------------------
def q_from_p_pf(p_mw: float, pf: float) -> float:
    phi = math.acos(pf)
    return p_mw * math.tan(phi)

# -----------------------------
# Load network and clear loads
# -----------------------------

net = pn.mv_oberrhein()
net.load.drop(net.load.index, inplace=True)

# -----------------------------
# Build graph (ignore switch states to avoid fragmentation)
# -----------------------------
graph = top.create_nxgraph(net, respect_switches=False)

# -----------------------------
# Industrial: pick buses within hop_distance of any trafo LV bus
# -----------------------------
trafo_lv_buses = net.trafo["lv_bus"].unique()
industrial_buses = set()

# Ensure these buses are not considered industrial
industrial_buses -= excluded_buses

for lv_bus in trafo_lv_buses:
    distances = nx.single_source_shortest_path_length(graph, lv_bus, cutoff=hop_distance)
    industrial_buses.update(distances.keys())

# Add industrial loads
ind_q = q_from_p_pf(ind_p, pf_ind)
for b in sorted(industrial_buses):
    pp.create_load(net, bus=b, p_mw=ind_p, q_mvar=ind_q, name=f"IndLoad_{b}", type="industrial")

print(f"Added {len(industrial_buses)} industrial loads @ {ind_p} MW each.")

# -----------------------------
# Classify remaining buses into residential / commercial
# -----------------------------
all_buses = set(net.bus.index)
candidate_buses = all_buses - industrial_buses

# Degree-based heuristic
deg = dict(graph.degree(candidate_buses))

# Use geodata for density-based split for degree==2
coords_df = net.bus_geodata.loc[list(candidate_buses), ["x", "y"]].copy()
coords_df = coords_df.dropna()
candidate_with_geo = set(coords_df.index)

residential_buses = set()
commercial_buses = set()

if len(candidate_with_geo) > 0:
    X = coords_df.values
    idx_list = coords_df.index.to_numpy()

    # Pairwise distances (no sklearn)
    diff = X[:, None, :] - X[None, :, :]
    dists = np.hypot(diff[..., 0], diff[..., 1])
    np.fill_diagonal(dists, np.inf)

    k = min(knn_k_default, max(1, len(candidate_with_geo) - 1))
    mean_knn = np.sort(dists, axis=1)[:, :k].mean(axis=1)
    density = 1.0 / (mean_knn + 1e-12)
    density_map = {int(idx_list[i]): float(density[i]) for i in range(len(idx_list))}
    dens_thresh = np.percentile(density, dens_percentile_for_commercial)

    for b in candidate_with_geo:
        d = deg.get(b, 0)
        if d <= 1:
            residential_buses.add(b)
        elif d >= 3:
            commercial_buses.add(b)
        else:
            # degree == 2 -> use density
            if density_map[b] >= dens_thresh:
                commercial_buses.add(b)
            else:
                residential_buses.add(b)

# Buses without geodata default to residential
no_geo = candidate_buses - candidate_with_geo
residential_buses.update(no_geo)

# Ensure these buses remain unclassified (no res/com loads)
residential_buses -= excluded_buses
commercial_buses -= excluded_buses

# Fallback: if hop distance covered everything, overlay res/com on industrial buses
if len(residential_buses) == 0 and len(commercial_buses) == 0 and len(industrial_buses) > 0:
    inds = sorted(industrial_buses)
    split = len(inds) // 2
    residential_buses = set(inds[:split])
    commercial_buses = set(inds[split:])
    print("Fallback: no candidate buses left; overlaying residential/commercial on industrial buses.")

print(f"Classified {len(residential_buses)} residential and {len(commercial_buses)} commercial buses.")

# -----------------------------
# Add residential and commercial loads
# -----------------------------
res_q = q_from_p_pf(res_p, pf_res)
com_q = q_from_p_pf(com_p, pf_com)

for b in sorted(residential_buses):
    pp.create_load(net, bus=b, p_mw=res_p, q_mvar=res_q, name=f"ResLoad_{b}", type="residential")

for b in sorted(commercial_buses):
    pp.create_load(net, bus=b, p_mw=com_p, q_mvar=com_q, name=f"ComLoad_{b}", type="commercial")

print("Load summary by type (count, total MW):")
print(net.load.groupby("type")["p_mw"].agg(["count", "sum"]))

# print("Load MW =\n", net.load.p_mw)

# -----------------------------
# Optional: run power flow sanity check
# -----------------------------
try:
    pp.runpp(net)
    print(f"Bus voltages pu: min={net.res_bus.vm_pu.min():.3f}, max={net.res_bus.vm_pu.max():.3f}")
    if len(net.res_line):
        print(net.res_line.loading_percent.describe())
except Exception as e:
    print("Power flow did not converge:", e)

# -----------------------------
# Plotting with legend
# -----------------------------
color_map = {b: "grey" for b in net.bus.index}
for b in residential_buses:
    color_map[b] = "green"
for b in commercial_buses:
    color_map[b] = "blue"
for b in industrial_buses:
    color_map[b] = "red"

bus_colors = [color_map[b] for b in net.bus.index]

fig, ax = plt.subplots(figsize=(12, 10))
plot.simple_plot(
    net,
    bus_color=bus_colors,
    bus_size=1.2,
    line_width=0.5,
    ax=ax,
    show_plot=False
)
plt.title("MV Oberrhein - Industrial (red), Commercial (blue), Residential (green)", fontsize=14)

import matplotlib.patches as mpatches
legend_patches = [
    mpatches.Patch(color="red", label="Industrial"),
    mpatches.Patch(color="blue", label="Commercial"),
    mpatches.Patch(color="green", label="Residential"),
    mpatches.Patch(color="grey", label="Unclassified"),
]
plt.legend(handles=legend_patches, loc="lower left")
plt.tight_layout()
plt.show()


def buses_by_type(net, t):
    loads_t = net.load[net.load.type == t]
    return sorted(loads_t.bus.unique().tolist())

ind_buses = buses_by_type(net, "industrial")
res_buses = buses_by_type(net, "residential")
com_buses = buses_by_type(net, "commercial")

print(f"Industrial buses (n={len(ind_buses)}): {ind_buses}")
print(f"Residential buses (n={len(res_buses)}): {res_buses}")
print(f"Commercial buses (n={len(com_buses)}): {com_buses}")