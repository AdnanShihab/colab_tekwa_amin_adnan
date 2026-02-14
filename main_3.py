# New structure with CAPEX outside the for loop of stage calculation:

import time
start_time = time.time()  # Start the simulation

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=DeprecationWarning)


import pandas as pd
import numpy as np
# import pandapower as pp

# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)

# .......................... PandaPower ...........................
import pandapower.networks as pn

# .......................... Pymoo ...........................
from pymoo.core.problem import ElementwiseProblem
from pymoo.core.variable import Real, Integer, Binary


# ........................ External functions ........................
from net_clustering_20260126 import net_bus_clustering
from e_net_20260128 import power_system
from CAPEX_fuct_20250724 import CAPEX
from OPEX_func_20250726 import opex
# from mv_oberrhein_exisitng_sgen_allocation import find_cluster_for_bus

# ........................ Power grid ........................
net_old = pn.mv_oberrhein()
print("Original Network Info:")
# print(net_old.load[['bus', 'p_mw']])
print("len bus", len(net_old.bus.index))
print()

# ============================ Bus Clustering with Commercial, Residential and Industrial Busbar =====================
# We have the following clusters: comm 45 buses, res 53 buses, ind 38 buses, mixed 79 buses
net_update = net_bus_clustering(net_old)
net_new = net_update.network_with_clustered_loads()
net, industrial_bus, residential_bus, commercial_bus, mixed_bus = net_new
bus_indices = net.bus.index.to_list()   # Get the actual bus indices as a list
n_bus = len(bus_indices)

# Checking existance of specific bus index (e.g., 24)
# has_24 = 24 in net.bus.index
# print("Bus 24 exists:", has_24)

# ============================================= Managing existing sgen & loads ========================================
# ----------------- Identify sgens that are in Unassigned buses ----------------------
"""
# Not using existing sgen anymore, because they are very small capacities (total ~0.5 MW). Also, they are 
creating problem with the stage 1 total sgen_mw. Plus, when existing sgen are used, the entire PV_MW is sold to the 
grid. Also the BESS is charging at the middle of the night. Makes not sense to use it...

print("Existing PV after Dropping Unassigned buses & Initial Loads:")
unassigned_sgen_idx = []
for sgen_idx, bus_id in zip(net.sgen.index, net.sgen["bus"].values):
    if find_cluster_for_bus(bus_id) == "Unassigned":
        unassigned_sgen_idx.append(sgen_idx)

net.sgen = net.sgen[net.sgen["bus"].apply(lambda x: find_cluster_for_bus(x) != "Unassigned")]

caps = pd.to_numeric(net.sgen["p_mw"], errors="coerce").fillna(0.0).values
buses = net.sgen["bus"].values
buses_load = net.load["bus"].values
bus_index = net.sgen["bus"].index.values

print(f" {'Bus index':>8}  {'Bus':>6}   {'PV Capacity (MW)':>12}  {'Load (MW)':>10}  {'Cluster':>20}")
print("-" * 80)
for b_i, b, p in zip(bus_index, buses, caps):
    load_sum = net.load.loc[net.load["bus"] == b, "p_mw"].sum()
    cluster_name = find_cluster_for_bus(b)
    # print(f"{b_i:6d}   {b:6d}   {p:18.3f}  {load_sum:10.3f}    {cluster_name:>20}")

print("\nTotal Existing PV capacity:", caps.sum(), "MW")
print("Total busbars in network:", n_bus)
print("Total used busbar by existing PV in network:", len(buses))
print("Total used busbar by loads in network:", len(buses_load))
"""
# ........................ Fixed parameters ........................
discount_rate = 0.08

min_v_drop = 0.95
max_v_drop = 1.05

# ============================================== Optimization Function ===========================================


class MyProblem(ElementwiseProblem):
    def __init__(self, stage, stage_years,
                 carried_cap_pv_array_mw,
                 carried_cap_wt_array_mw,
                 carried_cap_bess_mw_by_cluster,
                 carried_bess_bus_by_cluster,
                 industrial_clusters,
                 residential_clusters,
                 commercial_clusters,
                 mixed_clusters, **kwargs):

        variables = dict()

        self.stage = stage
        self.stage_years = stage_years
        # self.carried_capacity = carried_capacity
        # self.carried_capacity_pv = carried_capacity_pv
        self.carried_cap_pv_array_mw = carried_cap_pv_array_mw
        self.carried_cap_wt_array_mw = carried_cap_wt_array_mw
        self.carried_cap_bess_mw_by_cluster = carried_cap_bess_mw_by_cluster
        self.carried_bess_bus_by_cluster = carried_bess_bus_by_cluster

        # -------- Build the 9 cluster definitions --------
        # Expected dict inputs like {"C1":[...], "C2":[...], "C3":[...]}
        # Residential has 2 clusters, Commercial 1, Mixed 3 -> total 9
        self.cluster_definitions = [
            ("ind_C1", industrial_clusters["C1"]),
            ("ind_C2", industrial_clusters["C2"]),
            ("ind_C3", industrial_clusters["C3"]),
            ("res_C1", residential_clusters["C1"]),
            ("res_C2", residential_clusters["C2"]),
            ("com_C1", commercial_clusters["C1"]),
            ("mix_C1", mixed_clusters["C1"]),
            # ("mix_C2", mixed_clusters["C2"]),
            # ("mix_C3", mixed_clusters["C3"]),
        ]
        print("Num of Clusters =", len(self.cluster_definitions))

        # =================================== Decision variables ==========================================
        # -------------------------- PV ------------------------------
        max_pv_capacity = 2.0  # example max PV size in MW
        for i in range(n_bus):
            # Option 1: Binary - PV connected or not
            variables[f"x_pv_bin{i}"] = Binary()

            # Option 2: Integer - PV connected to bus
            variables[f"x_pv_int{i}"] = Integer(bounds=(0, n_bus-1))

            # Option 3: Real - PV size (MW) at each bus
            variables[f"x_pv_mw{i}"] = Real(bounds=(0.0, max_pv_capacity))

        # -------------------------- WT ------------------------------
        # --- Find bus-bars connected to the transformers (110kV and 20kV) for WT connection points ---
        transformer_buses = list(set(net.trafo['hv_bus'].tolist() + net.trafo['lv_bus'].tolist()))
        self.transformer_bus_to_idx = {bus: idx for idx, bus in enumerate(transformer_buses)}  # Mapping
        self.idx_to_transformer_bus = {idx: bus for bus, idx in
                                       self.transformer_bus_to_idx.items()}  # Reverse mapping
        # print("Transformer buses:", transformer_buses)

        for idx, bus in enumerate(transformer_buses):
            # Define WT decision variables only for transformer buses
            variables[f"x_wt_bin{idx}"] = Binary()  # Binary variable for WT presence
            variables[f"x_wt_int{idx}"] = Integer(bounds=(0, len(transformer_buses) - 1))
            # Restrict to transformer buses
            variables[f"x_wt_mw{idx}"] = Real(bounds=(0.0, 10.0))  # Max WT capacity

        # ---------------------- BESS ------------------------------
        # variables[f"x_bess_bin"] = Binary()  # Binary variable for BESS presence
        # variables[f"x_bess_int"] = Integer(bounds=(0, n_bus-1))  # BESS connected to a bus
        # variables[f"x_bess_mw"] = Real(bounds=(0.0, 10.0))  # Max BESS capacity

        # ----------- BESS variables per cluster -----------
        max_bess_mw = 10.0  # Example max BESS size in MW per cluster
        for label, bus_list in self.cluster_definitions:
            n_choices = len(bus_list)
            if n_choices == 0:
                # Edge case: no buses (shouldn't happen, but guard)
                # Provide a dummy fixed var so shape remains consistent
                variables[f"x_bess_bin_{label}"] = Binary()
                variables[f"x_bess_int_{label}"] = Integer(bounds=(0, 0))
                variables[f"x_bess_mw_{label}"] = Real(bounds=(0.0, 0.0))
                continue

            variables[f"x_bess_bin_{label}"] = Binary()
            # Integer index 0..n_choices-1 choosing position inside bus_list
            variables[f"x_bess_int_{label}"] = Integer(bounds=(0, n_choices - 1))
            variables[f"x_bess_mw_{label}"] = Real(bounds=(0.0, max_bess_mw))

        # ---------------------- BESS carried Capacity variables per cluster -----------
        # carry BESS as dicts keyed by cluster label (fits your cluster-based decision variables)
        cluster_labels = ["ind_C1", "ind_C2", "ind_C3", "res_C1", "res_C2", "com_C1", "mix_C1"]
        carried_cap_bess_mw_by_cluster = {lab: 0.0 for lab in cluster_labels}
        carried_bess_bus_by_cluster = {lab: None for lab in cluster_labels}

        self.cluster_labels = [label for label, _ in self.cluster_definitions]

        # MW carried per cluster
        self.carried_cap_bess_mw_by_cluster = {
            label: float(carried_cap_bess_mw_by_cluster.get(label, 0.0))
            for label in self.cluster_labels
        }

        # BUS carried per cluster (pandapower bus id) or None
        self.carried_bess_bus_by_cluster = {
            label: carried_bess_bus_by_cluster.get(label, None)
            for label in self.cluster_labels
        }

        super().__init__(vars=variables, n_obj=1, n_ieq_constr=2, **kwargs)

    def _evaluate(self, x, out, *args, **kwargs):

        # print("\nEvaluating new solution...")

        # --- Create a fresh copy of the network for each evaluation ---
        import copy
        net_local = copy.deepcopy(net)  # Use local copy instead of global net

        # =============================== Define x values ===============================
        # ----------------------------- PV -----------------------------
        x_pv_bin = np.array([x[f"x_pv_bin{k:01}"] for k in range(0, n_bus)])
        # x_pv_bus = np.array([x[f"x_pv_int{k:01}"] for k in range(0, n_bus)])
        # x_pv_bus = np.array([bus_indices[x[f"x_pv_int{k:01}"]] for k in range(0, n_bus)])
        x_pv_int = np.array([x[f"x_pv_int{i:01}"] for i in range(n_bus)])
        x_pv_mw = np.array([x[f"x_pv_mw{k:01}"] for k in range(0, n_bus)])

        # Create list of PV dictionaries
        pv_x = []  # list of dicts for later use
        for i in range(n_bus):
            bin_var = x_pv_bin[i]
            idx_var = x_pv_int[i]
            size_var = x_pv_mw[i]

            if bin_var == 1:
                # Map index to actual bus
                chosen_bus = bus_indices[idx_var]
                pv_x.append({
                    "bus": chosen_bus,
                    "size_mw": size_var
                })
            else:
                pv_x.append({
                    "bus": None,
                    "size_mw": 0.0
                })

        x_pv_bus = [d["bus"] for d in pv_x if d["bus"] is not None and d["size_mw"] > 0]
        x_pv_mw = [d["size_mw"] for d in pv_x if d["bus"] is not None and d["size_mw"] > 0]

        # ----------------------------------- WT ---------------------------------------
        # --- For wind turbine variables, only consider transformer buses ---
        transformer_buses = list(self.transformer_bus_to_idx.keys())  # Get transformer bus indices
        n_wt = len(transformer_buses)  # or len(transformer_buses)

        x_wt_bin = np.array([x[f"x_wt_bin{self.transformer_bus_to_idx[bus]}"] for bus in transformer_buses])
        # x_wt_bus = np.array([self.idx_to_transformer_bus[x[f"x_wt_int{self.transformer_bus_to_idx[bus]}"]] for bus in
        #                      transformer_buses])
        x_wt_bus = np.array(transformer_buses)
        x_wt_mw = np.array([x[f"x_wt_mw{self.transformer_bus_to_idx[bus]}"] for bus in transformer_buses])

        # ----------------------- BESS ------------------------------
        # n_clusters = 9  # Number of clusters in the network
        # x_bess_bin = np.array([x[f"x_bess_bin{k:01}"] for k in range(0, n_clusters)])

        bess_x = []  # list of dicts for later use
        for label, bus_list in self.cluster_definitions:
            print("", bus_list)
            bin_var = x[f"x_bess_bin_{label}"]
            idx_var = x[f"x_bess_int_{label}"]
            size_var = x[f"x_bess_mw_{label}"]

            if bin_var == 1:
                # Map index -> actual bus
                chosen_bus = bus_list[idx_var]
                bess_x.append({
                    "cluster": label,
                    "bus": chosen_bus,
                    "size_mw": size_var
                })
            else:
                # chosen_bus = bus_list[idx_var]
                bess_x.append({
                    "cluster": label,
                    "bus": None,
                    "size_mw": 0.0
                })

        x_bess_bus = [d["bus"] for d in bess_x if d["bus"] is not None and d["size_mw"] > 0]
        x_bess_mw = [d["size_mw"] for d in bess_x if d["bus"] is not None and d["size_mw"] > 0]

        # NEW decision (this stage) as dicts keyed by cluster label for Carried capacity calculation
        new_bess_mw_by_cluster = {d["cluster"]: float(d["size_mw"]) for d in bess_x}
        new_bess_bus_by_cluster = {d["cluster"]: d["bus"] for d in bess_x}  # None if bin=0

        # print()
        # print("len x PV main =", len(x_pv_bus))
        # print("x_pv_mw =\n", x_pv_mw)
        # print("x_pv_mw SUM =", sum(x_pv_mw))
        # print("x_pv_mw SUM =\n", x_pv_mw.sum())
        # print("x_wt_bus =\n", x_wt_bus)
        # print("bess_bus =\n", x_bess_bus)
        # print()

        # Notes: do not add P2G, Heat load, and EVs for now.
        # Notes: Add CHP now and make all the stages now.

        # ------------------------- Predefine parameters--------------------------
        total_stage_cost = 0
        # obj_value_eur = 0
        # # obj_value_tco2 = 0

        g2026_power_grid, g1_power_grid_jul, g2031_power_grid = 0, 0, 0

        penalty = 0  # also added as G

        # ---------------------- Inter-Stage Interconnection: Carried capacity from previous stage --------------------
        # ---------------------- PV, WT carried capacity from previous stage ----------------------
        # Build a per-bus (length n_bus=179) array for NEW PV additions; default 0
        new_pv_mw_array = np.zeros(n_bus, dtype=float)
        new_wt_mw_array = np.zeros(n_wt, dtype=float)

        # Map pandapower bus id -> position 0..n_bus-1 (based on your bus_indices list)
        bus_to_pos = {bus: i for i, bus in enumerate(bus_indices)}

        # Fill the 179-length array with the NEW PV values at the selected buses
        for bus, mw in zip(x_pv_bus, x_pv_mw):
            new_pv_mw_array[bus_to_pos[bus]] += float(mw)  # += in case duplicates choose same bus
            # new_wt_mw_array[bus_to_pos[bus]] += float(mw)

        # Fill NEW WT (per transformer index)
        new_wt_mw_array[:] = np.asarray(x_wt_mw, dtype=float) * np.asarray(x_wt_bin, dtype=float)

        if self.stage == 2:
            # df_carried_capacity_pv = pd.DataFrame(self.carried_cap_pv_array_mw, columns=['pv_mw'])
            # for i, x_pv_mw_new, x_pv_mw_carried in zip(x_pv_mw, df_carried_capacity_pv):
            #     print(f"New PV capacity added: {x_pv_mw_new:.2f} MW")
            #     pv_total_mw = x_pv_mw_new + x_pv_mw_carried
            #     new_pv_mw_array = np.append(new_pv_mw_array, pv_total_mw)
            #     x_pv_mw = new_pv_mw_array

            carried_pv = np.asarray(self.carried_cap_pv_array_mw, dtype=float)  # shape (n_bus,)
            carried_wt = np.asarray(self.carried_cap_wt_array_mw, dtype=float)

            # new = new_pv_mw_array
            # total = carried + new
            # x_pv_mw = total
            # new_wt = new_wt_mw_array
            # total_wt = carried_wt + new_wt
            # x_wt_mw = total_wt

            # TOTAL installed after stage 2
            x_pv_mw = carried_pv + new_pv_mw_array  # (n_bus,)
            x_wt_mw = carried_wt + new_wt_mw_array  # (n_wt,)

            # print("len carried =", len(carried_pv), "len x_pv_mw =", len(x_pv_mw), "n_bus =", n_bus, "len bus_indices =", len(bus_indices))
            print("Carried PV capacity from stage 1 (MW):", carried_pv.sum())
            print("New PV capacity in stage 2 (MW):", new_pv_mw_array.sum())
            # print("Total PV capacity after stage 2 (MW):", x_pv_mw.sum())
            print()
            print("Carried WT capacity from stage 1 (MW):", carried_wt.sum())
            print("New WT capacity in stage 2 (MW):", new_wt_mw_array.sum())
            # print("Total WT capacity after stage 2 (MW):", x_wt_mw.sum())

            # ------------------ BESS Carried Capacity per Cluster ------------------
            x_bess_bus_total = []
            x_bess_mw_total = []

            for label in self.cluster_labels:
                carried_mw = float(self.carried_cap_bess_mw_by_cluster.get(label, 0.0))
                carried_bus = self.carried_bess_bus_by_cluster.get(label, None)

                new_mw = float(new_bess_mw_by_cluster.get(label, 0.0))
                new_bus = new_bess_bus_by_cluster.get(label, None)

                total_mw = carried_mw + new_mw
                if total_mw <= 0:
                    continue

                # choose location: new bus if new built, otherwise carried bus
                bus_total = new_bus if (new_bus is not None and new_mw > 0) else carried_bus

                if bus_total is None:
                    raise ValueError(
                        f"BESS total MW exists for cluster {label} (= {total_mw} MW) but bus location is None. "
                        f"(carried_bus=None and new_bus=None)"
                    )

                x_bess_bus_total.append(bus_total)
                x_bess_mw_total.append(total_mw)

            # NEW lists (for CAPEX)
            x_bess_bus = [d["bus"] for d in bess_x if d["bus"] is not None and d["size_mw"] > 0]
            x_bess_mw = [d["size_mw"] for d in bess_x if d["bus"] is not None and d["size_mw"] > 0]

        elif self.stage == 3:
            print("Calc Carried Capacity for stage 3...")

        #  ------------------------- Calculation per year ---------------------------------
        # print("Calculating stage cost...")
        # Calculate power grid for January and July
        for year in self.stage_years:

            # Calculate year-specific operational parameters
            year_index = year - 2025  # Relative year for discounting
            # print("year_index =", year_index)

            if year == 2026:
                print("=" * 50 + " Year 2026 " + "=" * 50)

                # ----------------------------- POWER SYSTEM & BESS -----------------------------

                # print(x_pv_mw)
                # print("x_pv_mw * x_pv_bin =", x_pv_mw * x_pv_bin)
                #
                # print(x_wt_mw)
                # print("x_wt_mw * x_wt_bin =", x_wt_mw * x_wt_bin)

                p_sys = power_system(net=net_local, x=x,
                                     x_pv_bus=x_pv_bus, x_pv_mw=x_pv_mw,
                                     x_wt_bus=x_wt_bus, x_wt_mw=x_wt_mw * x_wt_bin,
                                     x_bess_bus=x_bess_bus, x_bess_mw=x_bess_mw, bess_params=None
                                     )

                res_p_sys_2026_jan = p_sys.power_flow_2026_jan()
                results, net_update = res_p_sys_2026_jan

                # print("Power System Results 2026 Jan:\n", results)
                # print("Updated Network 2026 Jan:\n", net_update)

                # net_hour_0 = net_update[0]  # Using to define the location of the bus-bars.
                # net_hour_11 = net_update[11]

                power_balance_2026_jan = results.iloc[:, 0:6]
                vm_jan = results.iloc[:, 6:186]
                print("Power Balance 2026 Jan:\n", power_balance_2026_jan)
                print(f"{'-' * 50}")

                # print("loads = \n", net_hour_0.load['p_mw'])
                # For CAPEX I can just use [0], because it is enough to define \
                # the bus-bars if it is industrial or etc.
                # print("PV = \n", net_hour_0.sgen['p_mw'])

                # ----------------------------- Calculation per Stage -----------------------------
                # --------------------------------------- CAPEX -----------------------------------
                cost_capex = CAPEX(stage=self.stage, year=year,
                                   net=net_local,
                                   x_pv_bus=x_pv_bus, x_pv_mw=x_pv_mw,     # only taking pv size if bin=1
                                   x_wt_bus=x_wt_bus, x_wt_mw=x_wt_mw*x_wt_bin,     # making WT size 0 if bin=0
                                   x_bess_bus=x_bess_bus, x_bess_mw=x_bess_mw,  # only taking bess_mw if bin=0
                                   tau_bess=p_sys.bess_params["duration_h"],
                                   )  # CHANGE: net_update=net_local

                capex_pv = cost_capex.capex_pv()
                capex_wt = cost_capex.capex_wt_2026()
                capex_bess = cost_capex.capex_bess_2026()

                capex_stage = capex_pv + capex_wt + capex_bess

                print(f"{'-' * 50}")
                print("capex_pv_2026 =", capex_pv)
                print("capex_wt_2026 =", capex_wt)
                print("capex_bess_2026 =", capex_bess)
                print()
                print("capex_2026 =", capex_stage)

                # Apply NPV discount to CAPEX (discount to beginning of stage)
                stage_start_year = self.stage_years[0]      # Make sure to add the first year of each stage
                years_from_base = stage_start_year - 2025   # Assuming 2025 is base year

                # print("stage_start_year =", stage_start_year)
                # print("years_from_base =", years_from_base)
                print()

                capex_stage_npv = capex_stage * (1 / (1 + discount_rate) ** years_from_base)
                print(f"Stage {self.stage} CAPEX NPV: {capex_stage_npv}")
                print(f"{'-' * 50}")

                total_stage_cost += capex_stage_npv

                # --------------------------------------- OPEX 2026 --------------------------------------
                # DO IT AFTER ALL THE FIRST YEAR OF ALL STAGES CALCULATIONS.....
                """
                stage_opex_total = 0
                cost_opex = opex(stage=self.stage, year=year_index, net_update=net_local,
                                 x_pv_bus=x_pv_bus, x_pv_mw=x_pv_mw*x_pv_bin)    # CHANGE: net_update=net_hour_0

                opex_var_loc_elem_2026 = cost_opex.opex_var_loc_elem_2026()
                # print("OPEX_2026 =", opex_var_loc_elem_2026)

                # OLD:
                # opex_fix_loc_elem_2025 = cost_opex.opex_fixed_loc_elem_2025()
                # opex_e_net_2025 = cost_opex.opex_e_net_2025()

                opex_year = opex_var_loc_elem_2026

                opex_year_npv = opex_year * (1 / (1 + discount_rate) ** year_index)
                stage_opex_total += opex_year_npv

                print(f"Year {year} OPEX NPV: {opex_year_npv}")

                total_stage_cost += stage_opex_total
                """
            elif year == 2027:
                print("year 2027")
                # ----------------------------- POWER SYSTEM & BESS -----------------------------
                # ----------------------------- Add net and opex only -----------------------------

                # total_stage_cost += opex_year
            elif year == 2028:
                print("year 2028")
                # ----------------------------- POWER SYSTEM & BESS -----------------------------
                # ----------------------------- Add net and opex only -----------------------------

                # total_stage_cost += opex_year
            elif year == 2029:
                print("year 2029")
                # ----------------------------- POWER SYSTEM & BESS -----------------------------
                # ----------------------------- Add net and opex only -----------------------------

                # total_stage_cost += opex_year
            elif year == 2030:
                print("year 2030")
                # ----------------------------- POWER SYSTEM & BESS -----------------------------

                # ----------------------------- Add net and opex only -----------------------------

                # total_stage_cost += opex_year

            # =============================================== Stage 2 ================================================
            elif year == 2031:
                print("="*50 + " Year 2031 " + "="*50)

                # ----------------------------- POWER SYSTEM & BESS -----------------------------
                p_sys = power_system(net=net_local, x=x,
                                     x_pv_bus=x_pv_bus, x_pv_mw=x_pv_mw,
                                     x_wt_bus=x_wt_bus, x_wt_mw=x_wt_mw * x_wt_bin,
                                     x_bess_bus=x_bess_bus, x_bess_mw=x_bess_mw, bess_params=None
                                     )

                res_p_sys_jan = p_sys.power_flow_2031_jan()
                results, net_update = res_p_sys_jan

                # print("Power System Results 2026 Jan:\n", results)
                # print("Updated Network 2026 Jan:\n", net_update)

                # net_hour_0 = net_update[0]  # Using to define the location of the bus-bars.
                # net_hour_11 = net_update[11]

                power_balance_jan = results.iloc[:, 0:6]
                vm_jan = results.iloc[:, 6:186]
                # print("Power Balance 2031 Jan:\n", power_balance_jan)
                print(f"{'-' * 50}")

                # print("loads = \n", net_hour_0.load['p_mw'])
                # For CAPEX I can just use [0], because it is enough to define \
                # the bus-bars if it is industrial or etc.
                # print("PV = \n", net_hour_0.sgen['p_mw'])

                # ----------------------------- Calculation per Stage -----------------------------
                # --------------------------------------- CAPEX -----------------------------------
                cost_capex = CAPEX(stage=self.stage, year=year_index,
                                   net=net_local,
                                   x_pv_bus=x_pv_bus, x_pv_mw=x_pv_mw,  # only taking pv size if bin=1
                                   x_wt_bus=x_wt_bus, x_wt_mw=x_wt_mw * x_wt_bin,  # making WT size 0 if bin=0
                                   x_bess_bus=x_bess_bus, x_bess_mw=x_bess_mw,  # only taking bess_mw if bin=0
                                   tau_bess=p_sys.bess_params["duration_h"],
                                   )  # CHANGE: net_update=net_local

                capex_pv = cost_capex.capex_pv_2026()
                capex_wt = cost_capex.capex_wt_2026()
                capex_bess = cost_capex.capex_bess_2026()

                capex_stage = capex_pv + capex_wt + capex_bess

                print(f"{'-' * 50}")
                print("capex_pv =", capex_pv)
                print("capex_wt =", capex_wt)
                print("capex_bess =", capex_bess)
                print("capex Stage =", capex_stage)

                # Apply NPV discount to CAPEX (discount to beginning of stage)
                stage_start_year = self.stage_years[0]  # Make sure to add the first year of each stage
                years_from_base = stage_start_year - 2025  # Assuming 2025 is base year
                # print("stage_start_year =", stage_start_year)
                # print("years_from_base =", years_from_base)
                print()

                capex_stage_npv = capex_stage * (1 / (1 + discount_rate) ** years_from_base)
                print(f"Stage {self.stage} CAPEX NPV: {capex_stage_npv}")
                print(f"{'-' * 50}")

                total_stage_cost += capex_stage_npv

            elif year == 2032:
                print("year 2032")
                # Add net and opex only

                # total_stage_cost += opex_year
            elif year == 2033:
                print("year 2033")
                # Add net and opex only

                # total_stage_cost += opex_year
            elif year == 2034:
                print("year 2034")
                # Add net and opex only

                # total_stage_cost += opex_year
            elif year == 2035:
                print("year 2035")
                # Add net and opex only

                # total_stage_cost += opex_year
            elif year == 2036:
                print("year 2036")
                # Repeat similar calculations for 2028
                # cost_capex = capex(stage=self.stage, year=year_index,
                #                    x_pv_bus=x_pv_bus, x_pv_mw=x_pv_mw,
                #                    net_update=net)

                # OPEX:
        print(f"Stage {self.stage} Total Cost: {total_stage_cost}")

        # out["penalty"] = penalty
        out["G"] = [g2026_power_grid, g2031_power_grid]
        out["F"] = [total_stage_cost]


from pymoo.algorithms.moo.nsga2 import NSGA2, RankAndCrowdingSurvival
from pymoo.core.mixed import MixedVariableMating, MixedVariableGA, MixedVariableSampling, MixedVariableDuplicateElimination
from pymoo.optimize import minimize
from pymoo.factory import get_termination

# from pymoo.algorithms.soo.nonconvex.ga import GA
from pymoo.operators.crossover.sbx import SimulatedBinaryCrossover
from pymoo.operators.mutation.pm import PolynomialMutation
from pymoo.util.plotting import plot

# Simulated Binary Crossover (SBX) with a custom eta and probability
crossover = SimulatedBinaryCrossover(prob=0.9, eta=20)
mutation = PolynomialMutation(prob=0.1, eta=20)  # prob is the mutation probability, eta controls mutation spread

stages = {
    1: [2026, 2027, 2028, 2029, 2030],    # Stage 1
    2: [2031, 2032, 2033, 2034, 2035],    # Stage 2
    3: [2036, 2037, 2038, 2039, 2040],    # Stage 3
}

# Initialize tracking variables
cumulative_capacities_pv = np.zeros(n_bus)  # Track cumulative PV capacity

transformer_buses = pd.unique(
        np.r_[net.trafo['hv_bus'].to_numpy(), net.trafo['lv_bus'].to_numpy()]
    ).tolist()
n_wt = len(transformer_buses)
cumulative_capacities_wt = np.zeros(n_wt)  # Track cumulative WT capacity

# -------------- BESS cumulative capacity per cluster --------------
cluster_definitions = [
    ("ind_C1", industrial_bus["C1"]),
    ("ind_C2", industrial_bus["C2"]),
    ("ind_C3", industrial_bus["C3"]),
    ("res_C1", residential_bus["C1"]),
    ("res_C2", residential_bus["C2"]),
    ("com_C1", commercial_bus["C1"]),
    ("mix_C1", mixed_bus["C1"]),
]
cluster_labels = [label for label, _ in cluster_definitions]
label_to_i = {label: i for i, label in enumerate(cluster_labels)}
n_clusters = len(cluster_labels)

cumulative_cap_bess_mw = np.zeros(len(cluster_labels))
carried_bess_bus_by_cluster = np.full(n_clusters, -1, dtype=int)  # -1 means "no bus yet"

all_stage_results = []
total_project_cost = 0

# years = list(range(2026, 2027))

gen_size = 25
pop_size = 50


# ================= STAGE-LEVEL OPTIMIZATION =================
for stage_num in [1, 2]:     # CHANGE: for stage_num in [1, 2, 3]:
    stage_years = stages[stage_num]

    print(f"\n{'=' * 50}")
    print(f"OPTIMIZING STAGE {stage_num}")
    print(f"Years: {stage_years}")
    print(f"Carried PV Capacity: {cumulative_capacities_pv.sum()}")
    print(f"Carried WT Capacity: {cumulative_capacities_wt.sum()}")
    # print(f"Carried BESS Capacity: {cumulative_cap_bess_mw}")
    # print(f"Carried BESS Bus-bars: {carried_bess_bus_by_cluster}")  # -1 means "no bus yet"
    print(f"{'=' * 50}\n")

    # Create problem for this stage
    prob = MyProblem(stage=stage_num,
                     stage_years=stage_years,
                     carried_cap_pv_array_mw=cumulative_capacities_pv,
                     carried_cap_wt_array_mw=cumulative_capacities_wt,
                     carried_cap_bess_mw_by_cluster=cumulative_cap_bess_mw,
                     carried_bess_bus_by_cluster=carried_bess_bus_by_cluster,
                     industrial_clusters=industrial_bus,
                     residential_clusters=residential_bus,
                     commercial_clusters=commercial_bus,
                     mixed_clusters=mixed_bus
                     )

    # Setup algorithm
    algorithm = MixedVariableGA(
        pop_size=pop_size,
        sampling=MixedVariableSampling(),
        mating=MixedVariableMating(eliminate_duplicates=MixedVariableDuplicateElimination()),
        eliminate_duplicates=MixedVariableDuplicateElimination(),
        survival=RankAndCrowdingSurvival(),
        crossover=crossover,
        mutation=mutation
    )

    termination = get_termination("n_gen", gen_size)

    # Optimize for this stage
    res = minimize(prob, algorithm, termination, seed=1, verbose=True)

    # OLD:
    # # Extract best solution
    # # best_idx = np.argmin(res.F[:, 0])
    # best_idx = res.F
    # # best_solution = res.X[best_idx]
    # best_solution = res.X
    # # best_cost = res.F[best_idx, 0]
    # best_cost = res.F

    # CORRECTED: Extract best solution properly
    if len(res.F.shape) > 1:  # Multiple solutions
        best_idx = np.argmin(res.F[:, 0])
        best_solution = res.X[best_idx]
        best_cost = res.F[best_idx, 0]
    else:  # Single solution
        best_idx = 0
        best_solution = res.X
        best_cost = res.F[0] if hasattr(res.F, '__len__') else res.F

    print("-"*50)
    print(f"\nStage {stage_num} Results:")
    print(f"Best Cost: {best_cost}")

    # Extract new PV capacities for this stage
    new_pv_bin = np.array([best_solution[f"x_pv_bin{k}"] for k in range(n_bus)])
    new_pv_mw = np.array([best_solution[f"x_pv_mw{k}"] for k in range(n_bus)])
    new_pv_capacity = new_pv_mw * new_pv_bin

    # Extract new WT capacities for this stage
    # n_wt = len(prob.transformer_bus_to_idx)  # or len(transformer_buses)
    new_wt_bin = np.array([best_solution[f"x_wt_bin{k}"] for k in range(n_wt)])
    new_wt_mw = np.array([best_solution[f"x_wt_mw{k}"] for k in range(n_wt)])
    new_wt_capacity = new_wt_mw * new_wt_bin

    # Extract new BESS capacities for this stage (per cluster)
    # cluster_labels = ["ind_C1", "ind_C2", "ind_C3", "res_C1", "res_C2", "com_C1", "mix_C1"]

    # carried_cap_bess_mw_by_cluster = {label: 0.0 for label in cluster_labels}
    # carried_bess_bus_by_cluster = {label: None for label in cluster_labels}
    #
    # new_bess_mw_by_cluster = {}
    # new_bess_bus_by_cluster = {}
    #
    # for label, bus_list in prob.cluster_definitions:
    #     bin_var = best_solution[f"x_bess_bin_{label}"]
    #     idx_var = best_solution[f"x_bess_int_{label}"]
    #     size_var = best_solution[f"x_bess_mw_{label}"]
    #
    #     if bin_var == 1 and size_var > 0:
    #         new_bess_mw_by_cluster[label] = float(size_var)
    #         new_bess_bus_by_cluster[label] = bus_list[int(idx_var)]
    #     else:
    #         new_bess_mw_by_cluster[label] = 0.0
    #         new_bess_bus_by_cluster[label] = None

    # Update cumulative capacities for next stage
    cumulative_capacities_pv += new_pv_capacity
    cumulative_capacities_wt += new_wt_capacity
    # for label in new_bess_mw_by_cluster:
    #     if new_bess_mw_by_cluster[label] > 0:
    #         carried_cap_bess_mw_by_cluster[label] += new_bess_mw_by_cluster[label]
    #         carried_bess_bus_by_cluster[label] = new_bess_bus_by_cluster[label]
    #         # (assumes at most one BESS per cluster and building again "replaces/relocates" the bus)
    # # cumulative_cap_bess_mw += carried_cap_bess_mw_by_cluster

    new_bess_mw = np.zeros(n_clusters, dtype=float)
    new_bess_bus = np.full(n_clusters, -1, dtype=int)

    for label, bus_list in prob.cluster_definitions:
        i = label_to_i[label]

        bin_var = best_solution[f"x_bess_bin_{label}"]
        idx_var = int(best_solution[f"x_bess_int_{label}"])
        size_var = float(best_solution[f"x_bess_mw_{label}"])

        if bin_var == 1 and size_var > 0:
            new_bess_mw[i] = size_var
            new_bess_bus[i] = int(bus_list[idx_var])

    # ---- Update carried/cumulative for next stage ----
    cumulative_cap_bess_mw += new_bess_mw

    # update carried bus location only where a new BESS was built
    mask = new_bess_mw > 0
    carried_bess_bus_by_cluster[mask] = new_bess_bus[mask]

    # Store stage results
    stage_result = {
        'stage': stage_num,
        'years': stage_years,
        'stage_cost': best_cost,
        'new_pv_capacity': new_pv_capacity.copy(),
        'cumulative_pv_capacity': cumulative_capacities_pv.copy(),
        'new_wt_capacity': new_wt_capacity.copy(),
        'cumulative_wt_capacity': cumulative_capacities_wt.copy(),
        'new_bess_mw_by_cluster': new_bess_mw.copy(),
        'cumulative_bess_mw': cumulative_cap_bess_mw.copy(),
        'best_solution': best_solution
    }

    all_stage_results.append(stage_result)
    total_project_cost += best_cost

    print(f"New PV Capacity Added: {new_pv_capacity.sum():.2f} MW")
    print(f"Cumulative PV Capacity: {cumulative_capacities_pv.sum():.2f} MW")

    print(f"New WT Capacity Added: {new_wt_capacity.sum():.2f} MW")
    print(f"Cumulative WT Capacity: {cumulative_capacities_wt.sum():.2f} MW")

    # print("New BESS Capacity Added by Cluster (MW):", new_bess_mw_by_cluster)
    # print("Cumulative BESS Capacity by Cluster (MW):", cumulative_cap_bess_mw.sum())

    print("New BESS Capacity Added by Cluster (MW):", dict(zip(cluster_labels, new_bess_mw)))
    print("Cumulative BESS Capacity by Cluster (MW):", dict(zip(cluster_labels, cumulative_cap_bess_mw)))
    print("Carried BESS bus by cluster:", dict(zip(cluster_labels, carried_bess_bus_by_cluster)))

    print("-" * 50)

# ================= FINAL RESULTS =================
print(f"\n{'='*50}")
print("FINAL PROJECT RESULTS")
print(f"{'='*50}")
print(f"Total Project Cost (NPV): {total_project_cost} EUR")
print(f"Total PV Capacity Installed: {cumulative_capacities_pv.sum():.2f} MW")

end_time = time.time()  # End the simulation
elapsed_time = end_time - start_time
print(f"Simulation ran for {elapsed_time:.2f} seconds")
hours = elapsed_time / 3600
print(f"Simulation ran for {hours:.2f} hours")