
# ---------------------------------------------------------------------------------------------------
# ----------- mv_oberrhein Existing Sgen Allocation -------------------------------------------------
# Here Load (MW) values are not important, because we are only checking the existing sgen allocation
# Date: 20251202
# ---------------------------------------------------------------------------------------------------

import pandapower.networks as pn
import pandas as pd

# Load the network
net = pn.mv_oberrhein()

# === Cluster definitions (copy from your class) ===
industrial_clusters = {
    "C1": [72, 108, 289, 269, 110, 75, 196, 103, 101, 106],
    "C2": [6, 5, 7, 241, 24, 290, 4, 242, 243, 244, 8, 245],
    "C3": [71, 81, 73, 77, 119, 80, 117, 35, 45, 47, 148, 120, 49, 52, 55, 146, 145],
}
residential_clusters = {
    "C1": [48, 50, 44, 192, 42, 51, 34, 76],
    "C2": [161, 38, 173, 174, 162],
}
commercial_clusters = {
    "C1": [82, 79, 190, 64, 65, 36],
}
mixed_clusters = {
    "C1": [235, 94, 95, 102, 142, 98, 134, 100, 132, 137, 107,
           195, 215, 216, 210, 205, 207, 194, 213, 201, 109,
           219, 239, 236, 223, 229, 224, 227, 231],
    "C2": [136, 170, 116, 111, 237, 138,
           133, 140, 144, 172, 141, 149, 54, 147,
           169, 275, 287, 286, 288, 285, 178, 176],
    "C3": [313, 315, 246, 314, 304, 312, 273, 168, 301, 303, 281, 271, 305,
           188, 186, 181, 129, 197, 167, 199, 184, 198, 200, 153,
           316, 157, 155, 159],
}


# === Helper to find cluster for a bus ===
def find_cluster_for_bus(bus_idx):
    for cname, buses in industrial_clusters.items():
        if bus_idx in buses:
            return f"Industrial_{cname}"
    for cname, buses in residential_clusters.items():
        if bus_idx in buses:
            return f"Residential_{cname}"
    for cname, buses in commercial_clusters.items():
        if bus_idx in buses:
            return f"Commercial_{cname}"
    for cname, buses in mixed_clusters.items():
        if bus_idx in buses:
            return f"Mixed_{cname}"
    return "Unassigned"

# ----------------- Identify sgens that are in Unassigned buses ----------------------
unassigned_sgen_idx = []
for sgen_idx, bus_id in zip(net.sgen.index, net.sgen["bus"].values):
    if find_cluster_for_bus(bus_id) == "Unassigned":
        unassigned_sgen_idx.append(sgen_idx)

# print("Dropping sgen entries at Unassigned buses:", unassigned_sgen_idx)

# Drop them
# net.sgen.drop(index=unassigned_sgen_idx, inplace=True)
# === Only keep sgens that belong to a cluster ===
# net.sgen = net.sgen[net.sgen["bus"].apply(lambda x: find_cluster_for_bus(x) != "Unassigned")]

# print(net.sgen[["bus", "p_mw"]])

# Ensure numeric capacity values
caps = pd.to_numeric(net.sgen["p_mw"], errors="coerce").fillna(0.0).values
buses = net.sgen["bus"].values
bus_index = net.sgen["bus"].index.values

# print(f" {'Bus index':>8}  {'Bus':>6}   {'PV Capacity (MW)':>12}  {'Load (MW)':>10}  {'Cluster':>20}")
# print("-" * 80)
for b_i, b, p in zip(bus_index, buses, caps):
    load_sum = net.load.loc[net.load["bus"] == b, "p_mw"].sum()
    cluster_name = find_cluster_for_bus(b)
    # print(f"{b_i:6d}   {b:6d}   {p:18.3f}  {load_sum:10.3f}    {cluster_name:>20}")

# print("\nTotal PV capacity:", caps.sum(), "MW")