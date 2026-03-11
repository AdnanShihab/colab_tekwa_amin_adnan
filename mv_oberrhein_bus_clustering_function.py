
# Industrial busses idx:
# Cluster 1:                 72, 108, 289, 269, 110, 75, 196, 103, 101, 106
# Cluster 2:                 6, 5, 7, 241, 24, 290, 4, 242, 243, 244, 8, 245
# Cluster 3:                 71, 81, 73, 77, 119, 80, 117, 35, 45, 47, 148, 120, 49, 52, 55, 146, 145

# Residential busses idx:
# Cluster 1:                48, 50, 44, 192, 42, 51, 34, 76
# Cluster 2:                161, 38, 173, 174, 162

# Commercial busses idx:
# Cluster 1:                82, 79, 190, 64, 65, 36

# Residential and commercial buses:
# Cluster 1:                235, 94, 95, 102, 142, 98, 134, 100, 132, 137, 107,
#                           195, 215, 216, 210, 205,207, 194, 213, 201, 109,
#                           219, 239, 236, 223, 229, 224, 227, 231
# Cluster 2:                136, 170, 116, 111, 237, 138,
#                           133, 140, 144, 172, 141, 149, 54, 147,
#                           169, 275, 287, 286, 288, 285, 178, 176,
# Cluster 3:                313, 315, 246, 314, 304, 312, 273, 168, 301, 303, 281, 271, 305,
#                           188, 186, 181, 129, 197, 167, 199, 184, 198, 200, 153,
#                           316, 157, 155, 159


import pandapower as pp

# import pandapower.networks as pn
# import pandas as pd
# import matplotlib.pyplot as plt
# import pandapower.plotting as plot

# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)


class net_bus_clustering():

    def __init__(self, net, **kwargs):

        self.net = net

    def network_with_clustered_loads(self):

        all_buses = set(self.net.bus.index)     # added on 20251215

        # ---- Load network and clear existing loads ----
        # net = pn.mv_oberrhein()
        self.net.load.drop(self.net.load.index, inplace=True)
        self.net.sgen.drop(index=self.net.sgen.index, inplace=True)
        # Not using existing sgen anymore, because they are very small capacities (total ~0.5 MW). Also, they are
        # creating problem with the stage 1 total sgen_mw. Plus, when existing sgen are used, the entire PV_MW is
        # sold to the grid. Also the BESS is charging at the middle of the night. Makes not sense to use it...

        # ---- Define clusters bus numbers ----
        self.industrial_clusters = {
            "C1": [72, 108, 289, 269, 110, 75, 196, 103, 101, 106],
            "C2": [6, 5, 7, 241, 24, 290, 4, 242, 243, 244, 8, 245],
            "C3": [71, 81, 73, 77, 119, 80, 117, 35, 45, 47, 148, 120, 49, 52, 55, 146, 145],
        }
        self.residential_clusters = {
            "C1": [48, 50, 44, 192, 42, 51, 34, 76, ],
            "C2": [161, 38, 173, 174, 162],
        }
        self.commercial_clusters = {
            "C1": [82, 79, 190, 64, 65, 36],
        }

        # ----------------------------------------- 20251215 -----------------------------------------
        # Update on the clustering bus bars. Some bus bars are not present in the network.
        # So, we need to add those bus bars in the mixed clusters lists. Now all bus bars are covered.

        predefined_buses = set()
        for cluster in self.industrial_clusters.values():
            predefined_buses.update(cluster)
        for cluster in self.residential_clusters.values():
            predefined_buses.update(cluster)
        for cluster in self.commercial_clusters.values():
            predefined_buses.update(cluster)

        # Calculate buses that are not in any predefined cluster
        remaining_buses = all_buses - predefined_buses

        # Create the mixed cluster
        self.mixed_clusters = {
            "C1": list(remaining_buses)
        }

        # Commented out on 20251215 ---------------------------------------------------------------------------------
        # mixed_clusters = {
        #     "C1": [235, 94, 95, 102, 142, 98, 134, 100, 132, 137, 107,
        #            195, 215, 216, 210, 205, 207, 194, 213, 201, 109,
        #            219, 239, 236, 223, 229, 224, 227, 231],
        #     "C2": [136, 170, 116, 111, 237, 138,
        #            133, 140, 144, 172, 141, 149, 54, 147,
        #            169, 275, 287, 286, 288, 285, 178, 176],
        #     "C3": [313, 315, 246, 314, 304, 312, 273, 168, 301, 303, 281, 271, 305,
        #            188, 186, 181, 129, 197, 167, 199, 184, 198, 200, 153,
        #            316, 157, 155, 159],
        # }

        # Flatten lists (keep order; duplicates across categories are allowed -> multiple loads on a bus)
        industrial_buses = [b for cl in self.industrial_clusters.values() for b in cl]
        residential_buses = [b for cl in self.residential_clusters.values() for b in cl]
        commercial_buses = [b for cl in self.commercial_clusters.values() for b in cl]

        # Optional: report overlaps (they will result in multiple loads on the same bus)
        overlap_ir = sorted(set(industrial_buses).intersection(residential_buses))
        overlap_ic = sorted(set(industrial_buses).intersection(commercial_buses))
        overlap_rc = sorted(set(residential_buses).intersection(commercial_buses))

        if overlap_ir or overlap_ic or overlap_rc:
            # print("Note: some buses appear in multiple categories; loads will be added for each category at that bus.")
            if overlap_ir: print("  Industrial ∩ Residential:", overlap_ir)
            if overlap_ic: print("  Industrial ∩ Commercial :", overlap_ic)
            if overlap_rc: print("  Residential ∩ Commercial:", overlap_rc)

        # ---- Helper to add loads safely ----
        def add_loads(net, bus_list, p_mw, q_mvar=0.0, load_type=""):
            missing = []
            added = 0
            for b in bus_list:
                if b in net.bus.index:
                    pp.create_load(net, bus=b, p_mw=p_mw, q_mvar=q_mvar,
                                   name=f"{load_type.capitalize()}Load_{b}", type=load_type or None)
                    added += 1
                else:
                    missing.append(b)
            # if missing:
            #     print(f"Warning: {len(missing)} {load_type} bus indices not found in net.bus and were skipped: {sorted(missing)}")
            return added

        # ---- Add loads by category ----
        n_ind = add_loads(self.net, industrial_buses, p_mw=0.50, q_mvar=0.0, load_type="industrial")
        n_com = add_loads(self.net, commercial_buses, p_mw=0.40, q_mvar=0.0, load_type="commercial")
        n_res = add_loads(self.net, residential_buses, p_mw=0.25, q_mvar=0.0, load_type="residential")

        # print(f"Added loads -> Industrial: {n_ind}, Commercial: {n_com}, Residential: {n_res}")
        # print("Loads: \n", net.load[["bus", "p_mw", "type"]])
        # print()

        # -----------------------------------------
        # Mixed buses: randomly assign either residential (0.25 MW) OR commercial (0.4 MW) per bus, no overlap
        # -----------------------------------------

        # ---- Utilities ----
        def unique_preserve_order(seq):
            seen = set()
            out = []
            for x in seq:
                if x not in seen:
                    out.append(x)
                    seen.add(x)
            return out

        # Removed: 20260126
        # Reproducible randomness: change the seed if you want a different split
        import numpy as np
        rng = np.random.default_rng(42)

        mixed_all = [b for cl in self.mixed_clusters.values() for b in cl]
        mixed_buses = unique_preserve_order(mixed_all)

        # Removed: 20260126
        # Optional: avoid adding mixed loads to buses already used above (set True to avoid overlaps across categories)
        avoid_overlap_with_existing = True
        if avoid_overlap_with_existing:
            already_used = set(industrial_buses) | set(residential_buses) | set(commercial_buses)
            mixed_buses = [b for b in mixed_buses if b not in already_used]

        missing_mixed = []
        added_mixed_res = 0
        added_mixed_com = 0

        for b in mixed_buses:
            if b not in self.net.bus.index:
                missing_mixed.append(b)
                continue
            if rng.random() < 0.5:
                pp.create_load(self.net, bus=b, p_mw=0.25, q_mvar=0.0, name=f"ResLoad_{b}", type="residential")
                added_mixed_res += 1
            else:
                pp.create_load(self.net, bus=b, p_mw=0.40, q_mvar=0.0, name=f"ComLoad_{b}", type="commercial")
                added_mixed_com += 1

        # print("---- Bus Clustering ----")
        # print(f"Added loads -> Industrial: {n_ind}, Commercial: {n_com}, Residential: {n_res}")
        # print(f"Mixed buses assigned -> Residential: {added_mixed_res}, Commercial: {added_mixed_com}, Total mixed: {added_mixed_res + added_mixed_com}")

        # if missing_mixed:
        #     print(f"Warning: {len(missing_mixed)} mixed bus indices not found and were skipped: {sorted(missing_mixed)}")

        # ---- Summary ----
        # try:
        #     print(self.net.load.groupby("type")["p_mw"].agg(["count", "sum"]))
        # except Exception:
        #     print(self.net.load[["name", "bus", "p_mw", "q_mvar"]].head(10))
        # print("Loads: \n", self.net.load[["bus", "p_mw", "type"]])
        # print("Total buses after clustering =", n_ind+n_com+n_res+added_mixed_res+added_mixed_com)
        # print()

        return self.net, self.industrial_clusters, self.residential_clusters, self.commercial_clusters, self.mixed_clusters

        # ---------------------------------------------------
        # Plot only the newly created load buses with colors by type
        # ---------------------------------------------------
        # Build bus sets by load type from net.load

        # ind_buses = set(self.net.load.loc[self.net.load["type"] == "industrial", "bus"])
        # com_buses = set(self.net.load.loc[self.net.load["type"] == "commercial", "bus"])
        # res_buses = set(self.net.load.loc[self.net.load["type"] == "residential", "bus"])
        #
        # # Ensure each bus is plotted once with precedence: Industrial > Commercial > Residential
        # plot_ind = ind_buses
        # plot_com = com_buses - plot_ind
        # plot_res = res_buses - plot_ind - plot_com
        #
        # # Create collections
        # fig, ax = plt.subplots(figsize=(12, 10))
        #
        # # 1) Original lines (light gray)
        # lc = plot.create_line_collection(net, color="lightgray", linewidths=0.7)
        # # 2) External grid(s)
        # try:
        #     egc = plot.create_ext_grid_collection(net, size=120, color="gold")
        #     collections = [lc, egc]
        # except Exception:
        #     # Fallback: scatter ext_grid buses if collection function is unavailable
        #     collections = [lc]
        #     if len(net.ext_grid):
        #         eg_buses = net.ext_grid.bus.values.tolist()
        #         geo = net.bus_geodata
        #         ex = geo.loc[[b for b in eg_buses if b in geo.index]].dropna(subset=["x", "y"])
        #         ax.scatter(ex["x"], ex["y"], s=140, c="gold", marker="*", edgecolors="k", linewidths=0.6, label="External Grid", zorder=5)
        #
        # # 3) Newly created load buses by type (use bus collections)
        # if len(plot_ind):
        #     bc_i = plot.create_bus_collection(net, buses=list(plot_ind), size=40, color="red")
        #     collections.append(bc_i)
        # if len(plot_com):
        #     bc_c = plot.create_bus_collection(net, buses=list(plot_com), size=40, color="blue")
        #     collections.append(bc_c)
        # if len(plot_res):
        #     bc_r = plot.create_bus_collection(net, buses=list(plot_res), size=40, color="green")
        #     collections.append(bc_r)
        #
        # # Draw all collections
        # if collections:
        #     plot.draw_collections(collections, ax=ax)
        #
        # # Legend
        # handles = []
        # import matplotlib.patches as mpatches
        # handles.append(mpatches.Patch(color="red", label="Industrial loads"))
        # handles.append(mpatches.Patch(color="blue", label="Commercial loads"))
        # handles.append(mpatches.Patch(color="green", label="Residential loads"))
        # handles.append(mpatches.Patch(color="lightgray", label="Lines"))
        # # External grid legend handle (if not drawn via collection fallback it might not auto-legend)
        # handles.append(mpatches.Patch(color="gold", label="External grid"))
        # ax.legend(handles=handles, loc="best")
        #
        # ax.set_title("MV Oberrhein: Lines, External Grid, and Newly Created Load Buses")
        # ax.set_aspect("equal", adjustable="box")
        # ax.grid(True, alpha=0.2)
        # plt.tight_layout()
        # plt.show()

