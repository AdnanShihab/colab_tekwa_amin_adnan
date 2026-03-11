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
from mv_oberrhein_bus_clustering import net_bus_clustering
from e_net_mv_20250716 import power_system
from CAPEX_fuct_20250724 import capex
from OPEX_func_20250726 import opex


# ........................ Power grid ........................
net = pn.mv_oberrhein()
# net.sgen.drop(index=net.sgen.index, inplace=True)
net_update = net_bus_clustering.network_with_clustered_loads(net)

bus_indices = net.bus.index.to_list()   # Get the actual bus indices as a list
# print("bus_indices =", bus_indices)
n_bus = len(bus_indices)
# print("no loads outside =\n", len(net.load))

# net update on 20250809
print(net)
print(shit)
# ........................ Fixed parameters ........................
discount_rate = 0.08

min_v_drop = 0.95
max_v_drop = 1.05

# ........................ Optimization Function ........................


class MyProblem(ElementwiseProblem):
    def __init__(self, stage, stage_years, carried_cap_pv_array_mw, **kwargs):
        variables = dict()

        self.stage = stage
        self.stage_years = stage_years
        # self.carried_capacity = carried_capacity
        # self.carried_capacity_pv = carried_capacity_pv
        self.carried_cap_pv_array_mw = carried_cap_pv_array_mw

        # ........................ Decision variables ........................
        # Find bus-bars connected to the transformers (110kV and 20kV) for WT connection points
        transformer_buses = list(set(net.trafo['hv_bus'].tolist() + net.trafo['lv_bus'].tolist()))
        self.transformer_bus_to_idx = {bus: idx for idx, bus in enumerate(transformer_buses)}  # Mapping
        self.idx_to_transformer_bus = {idx: bus for bus, idx in self.transformer_bus_to_idx.items()}  # Reverse mapping
        print("Transformer buses:", transformer_buses)

        for i in range(n_bus):
            # ---------------------- PV ------------------------------
            # Option 1: Binary - PV connected or not
            variables[f"x_pv_bin{i}"] = Binary()

            # Option 2: Integer - PV connected to bus
            variables[f"x_pv_int{i}"] = Integer(bounds=(0, n_bus-1))

            # Option 3: Real - PV size (MW) at each bus
            max_pv_capacity = 2.0  # example max PV size in MW
            variables[f"x_pv_mw{i}"] = Real(bounds=(0.0, max_pv_capacity))

            # ---------------------- WT ------------------------------
            for idx, bus in enumerate(transformer_buses):
                # Define WT decision variables only for transformer buses
                variables[f"x_wt_bin{idx}"] = Binary()  # Binary variable for WT presence
                variables[f"x_wt_int{idx}"] = Integer(
                    bounds=(0, len(transformer_buses) - 1))  # Restrict to transformer buses
                variables[f"x_wt_mw{idx}"] = Real(bounds=(0.0, 10.0))  # Max WT capacity

        # ---------------------- BESS ------------------------------
        variables[f"x_bess_bin"] = Binary()  # Binary variable for BESS presence
        variables[f"x_bess_int"] = Integer(bounds=(0, n_bus-1))  # BESS connected to a bus
        variables[f"x_bess_mw"] = Real(bounds=(0.0, 10.0))  # Max BESS capacity

        # size of PV generators for all bus-bars
        # for k in range(14, 28):
        #     variables[f"x{k:01}"] = Real(bounds=(0, 1))  # [MW]

        super().__init__(vars=variables, n_obj=1, n_ieq_constr=1, **kwargs)

    def _evaluate(self, x, out, *args, **kwargs):

        # Create a fresh copy of the network for each evaluation
        import copy
        net_local = copy.deepcopy(net)  # Use local copy instead of global net

        # ----------------------------- Define x values -----------------------------
        x_pv_bin = np.array([x[f"x_pv_bin{k:01}"] for k in range(0, n_bus)])
        # x_pv_bus = np.array([x[f"x_pv_int{k:01}"] for k in range(0, n_bus)])
        x_pv_bus = np.array([bus_indices[x[f"x_pv_int{k:01}"]] for k in range(0, n_bus)])
        x_pv_mw = np.array([x[f"x_pv_mw{k:01}"] for k in range(0, n_bus)])

        # For wind turbine variables, only consider transformer buses
        transformer_buses = list(self.transformer_bus_to_idx.keys())  # Get transformer bus indices
        x_wt_bin = np.array([x[f"x_wt_bin{self.transformer_bus_to_idx[bus]}"] for bus in transformer_buses])
        # x_wt_bus = np.array([self.idx_to_transformer_bus[x[f"x_wt_int{self.transformer_bus_to_idx[bus]}"]] for bus in
        #                      transformer_buses])
        x_wt_bus = np.array(transformer_buses)
        x_wt_mw = np.array([x[f"x_wt_mw{self.transformer_bus_to_idx[bus]}"] for bus in transformer_buses])

        # print("PV-MW =\n", (x_pv_mw*x_pv_bin))
        # print(x_pv_bus)
        # print("x_wt_bus =\n", (x_wt_bus))
        print("WT_bin =\n", x_wt_bin)
        print("WT_mw =\n", x_wt_mw)

        # ------------------------- Predefine parameters--------------------------
        total_stage_cost = 0
        # obj_value_eur = 0
        # # obj_value_tco2 = 0

        g1_power_grid_jan, g1_power_grid_jul = 0, 0

        # penalty = 0  # also added as G

        #  ------------------------- Calculation per year ---------------------------------
        # Calculate power grid for January and July
        for year in self.stage_years:

            # Calculate year-specific operational parameters
            year_index = year - 2025  # Relative year for discounting
            # print("year_index =", year_index)

            if year == 2026:
                print("year 2026")

                # ----------------------------- POWER SYSTEM & BESS -----------------------------
                # print("Power System 2025 Jan:")
                p_sys = power_system(net=net_local, x=x,
                                     x_pv_bus=x_pv_bus, x_pv_mw=x_pv_mw * x_pv_bin,
                                     x_wt_bus=x_wt_bus, x_wt_mw=x_wt_mw * x_wt_bin)

                res_p_sys_2026_jan = p_sys.power_flow_2026_jan()

                results, net_update = res_p_sys_2026_jan

                net_hour_0 = net_update[0]  # Using to define the location of the bus-bars.
                # net_hour_11 = net_update[11]
                power_balance_2026_jan = results.iloc[:, 0:3]
                vm_jan = results.iloc[:, 4:185]
                print(shit)
                # print("Power Sys 2026 Jan:\n", power_balance_2026_jan)
                # print("vm_jan_2026 =\n", vm_jan)
                # print("loads = \n", net_hour_0.load['p_mw'])    # For CAPEX I can just use [0], because it is enough to define \
                # the bus-bars if it is industrial or etc.
                # print("PV = \n", net_hour_0.sgen['p_mw'])

                # ----------------------------- Calculation per Stage -----------------------------
                # --------------------------------------- CAPEX -----------------------------------
                cost_capex = capex(stage=self.stage, year=year_index,
                                   x_pv_bus=x_pv_bus, x_pv_mw=x_pv_mw,
                                   net_update=net)  # CHANGE: net_update=net_hour_0

                capex_stage = cost_capex.capex_pv_2026()  # Adjust method name as needed
                # print("capex_stage 2026 =", capex_stage)

                # Apply NPV discount to CAPEX (discount to beginning of stage)
                stage_start_year = self.stage_years[0]
                years_from_base = stage_start_year - 2025  # Assuming 2025 is base year
                # print()

                capex_stage_npv = capex_stage * (1 / (1 + discount_rate) ** years_from_base)
                print(f"Stage {self.stage} CAPEX NPV: {capex_stage_npv}")

                total_stage_cost += capex_stage_npv

                # --------------------------------------- OPEX 2026 --------------------------------------
                stage_opex_total = 0
                cost_opex = opex(stage=self.stage, year=year_index, net_update=net,
                                 x_pv_bus=x_pv_bus, x_pv_mw=x_pv_mw)    # CHANGE: net_update=net_hour_0

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
            elif year == 2027:
                print("year 2027")
                # Add net and opex only

                # total_stage_cost += opex_year
            elif year == 2028:
                print("year 2028")
                # Add net and opex only

                # total_stage_cost += opex_year
            elif year == 2029:
                print("year 2029")
                # Add net and opex only

                # total_stage_cost += opex_year
            elif year == 2030:
                print("year 2030")
                # Add net and opex only

                # total_stage_cost += opex_year
            elif year == 2031:
                print("year 2031")
                # Repeat similar calculations for 2027
                # Assuming the same structure as 2026, adjust as needed
                cost_capex = capex(stage=self.stage, year=year_index,
                                   x_pv_bus=x_pv_bus, x_pv_mw=x_pv_mw,
                                   net_update=net)  # CHANGE: net_update=net_hour_0

                capex_stage = cost_capex.capex_pv_2026()  # CHANGE: capex_pv_2027()
                # print("capex_stage 2031 =", capex_stage)

                stage_start_year = self.stage_years[0]
                years_from_base = stage_start_year - 2025  # Assuming 2025 is base year

                capex_stage_npv = capex_stage * (1 / (1 + discount_rate) ** years_from_base)
                # print(f"Stage {self.stage} CAPEX NPV: {capex_stage_npv}")
                # print()

                total_stage_cost += capex_stage_npv

                # total_stage_cost += opex_year
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
        out["G"] = [g1_power_grid_jan]
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
all_stage_results = []
total_project_cost = 0

# years = list(range(2026, 2027))

gen_size = 2
pop_size = 3


# ================= STAGE-LEVEL OPTIMIZATION =================
for stage_num in [1, 2]:     # CHANGE: for stage_num in [1, 2, 3]:
    stage_years = stages[stage_num]

    print(f"\n{'=' * 50}")
    print(f"OPTIMIZING STAGE {stage_num}")
    print(f"Years: {stage_years}")
    print(f"Carried PV Capacity: {cumulative_capacities_pv.sum()}")
    print(f"{'=' * 50}\n")

    # Create problem for this stage
    prob = MyProblem(stage=stage_num,
                     stage_years=stage_years,
                     carried_cap_pv_array_mw=cumulative_capacities_pv)

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

    print(f"\nStage {stage_num} Results:")
    print(f"Best Cost: {best_cost}")

    # Extract new PV capacities for this stage
    new_pv_bin = np.array([best_solution[f"x_pv_bin{k}"] for k in range(n_bus)])
    new_pv_mw = np.array([best_solution[f"x_pv_mw{k}"] for k in range(n_bus)])
    new_pv_capacity = new_pv_mw * new_pv_bin

    # Update cumulative capacities for next stage
    cumulative_capacities_pv += new_pv_capacity

    # Store stage results
    stage_result = {
        'stage': stage_num,
        'years': stage_years,
        'stage_cost': best_cost,
        'new_pv_capacity': new_pv_capacity.copy(),
        'cumulative_pv_capacity': cumulative_capacities_pv.copy(),
        'best_solution': best_solution
    }

    all_stage_results.append(stage_result)
    total_project_cost += best_cost

    print(f"New PV Capacity Added: {new_pv_capacity.sum():.2f} MW")
    print(f"Cumulative PV Capacity: {cumulative_capacities_pv.sum():.2f} MW")

# ================= FINAL RESULTS =================
print(f"\n{'='*50}")
print("FINAL PROJECT RESULTS")
print(f"{'='*50}")
print(f"Total Project Cost (NPV): {total_project_cost} EUR")
print(f"Total PV Capacity Installed: {cumulative_capacities_pv.sum():.2f} MW")