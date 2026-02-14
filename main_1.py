# Could Sonnet 4 created

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
from e_net_mv_20250716 import power_system
from CAPEX_fuct_20250724 import capex
from OPEX_func_20250726 import opex


# ........................ Power grid ........................
net = pn.mv_oberrhein()
net.sgen.drop(index=net.sgen.index, inplace=True)

bus_indices = net.bus.index.to_list()   # Get the actual bus indices as a list
# print("bus_indices =", bus_indices)
n_bus = len(bus_indices)
# print("no loads outside =\n", len(net.load))

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
        # ........................ PV stage 1 ........................
        # bus-bars for the PV generators in industrial area
        # for k in range(0, 180):
        #     variables[f"x{k:01}"] = Integer(bounds=(1, 2))

        for i in range(n_bus):
            # Option 1: Binary - PV connected or not
            variables[f"x_pv_bin{i}"] = Binary()

            # Option 2: Integer - PV connected to bus
            variables[f"x_pv_int{i}"] = Integer(bounds=(0, n_bus-1))

            # Option 3: Real - PV size (MW) at each bus
            max_pv_capacity = 2.0  # example max PV size in MW
            variables[f"x_pv_mw{i}"] = Real(bounds=(0.0, max_pv_capacity))

        # size of PV generators for all bus-bars
        # for k in range(14, 28):
        #     variables[f"x{k:01}"] = Real(bounds=(0, 1))  # [MW]

        super().__init__(vars=variables, n_obj=1, n_ieq_constr=1, **kwargs)

    def _evaluate(self, x, out, *args, **kwargs):

        # ----------------------------- Define x values -----------------------------
        x_pv_bin = np.array([x[f"x_pv_bin{k:01}"] for k in range(0, n_bus)])
        # x_pv_bus = np.array([x[f"x_pv_int{k:01}"] for k in range(0, n_bus)])
        x_pv_bus = np.array([bus_indices[x[f"x_pv_int{k:01}"]] for k in range(0, n_bus)])
        x_pv_mw = np.array([x[f"x_pv_mw{k:01}"] for k in range(0, n_bus)])

        # print("PV-bus =\n", x_pv_bus)
        print("PV-MW =\n", x_pv_mw*x_pv_bin)
        # print("x_pv_len =\n", len(x_pv_mw))
        # print("Net_load =\n", net.load['p_mw'])

        # ------------------------- Predefine parameters--------------------------
        total_stage_cost = 0
        obj_value_eur = 0
        # obj_value_tco2 = 0

        g1_power_grid_jan, g1_power_grid_jul = 0, 0

        penalty = 0  # also added as G

        # ----------------------------- Parameters -----------------------------
        print()
        print("to Functions -->>")
        print()

        # --------------------------------------- CAPEX 2026 --------------------------------------
        cost_capex = capex(stage=self.stage, year=1,
                           x_pv_bus=x_pv_bus, x_pv_mw=x_pv_mw, net_update=net)  # CHANGE: net_update=net_hour_0,

        # capex_pv = cost_capex.capex_pv_2026()
        # capex_2026_tot_eur = capex_pv
        # capex_2026_npv = capex_2026_tot_eur * (1 / (1 + discount_rate) ** self.stage)  # Present value
        # print("capex_2026_npv =", capex_2026_npv)

        capex_stage = cost_capex.capex_pv_2026()  # Adjust method name as needed

        # Apply NPV discount to CAPEX (discount to beginning of stage)
        stage_start_year = self.stage_years[0]
        years_from_base = stage_start_year - 2025  # Assuming 2025 is base year
        print("years_from_base =", years_from_base)
        capex_stage_npv = capex_stage * (1 / (1 + discount_rate) ** years_from_base)

        total_stage_cost += capex_stage_npv

        print(f"Stage {self.stage} CAPEX NPV: {capex_stage_npv}")

        # ================= OPEX CALCULATION (FOR EACH YEAR IN STAGE) =================
        stage_opex_total = 0

        for year in self.stage_years:
            print(f"Calculating OPEX for year {year}")

            # Calculate year-specific operational parameters
            year_index = year - 2025  # Relative year for discounting
            print("year_index =", year_index)

            # ----------------------------- POWER SYSTEM & BESS -----------------------------
            # print("Power System 2025 Jan:")
            p_sys = power_system(net=net, x=x, x_pv_bus=x_pv_bus, x_pv_mw=x_pv_mw*x_pv_bin) #,
                                 # x_wt_bus=x_wt_bus, x_wt_mw=x_wt_mw,
                                 # chp_bus=x_chp_bus, chp_p_mw=res_chp_p_mwh,
                                 # hp_bus=x_hp_bus, hp_cap_mw=x_hp_size,
                                 # p2g_input_mw=x_p2g_size_mw, bess_bus=x_bess_bus, bess_p_mw=x_bess_mw,
                                 # x_gen_bus_12=x_gen_bus_12, x_gen_bus_12_mw=x_gen_bus_12_mw,
                                 # x_gen_bus_1=x_gen_bus_1, x_gen_bus_1_mw=x_gen_bus_1_mw)
            # res_p_sys_2026_jan = p_sys.power_flow_2026_jan()    # FINAL line used

            # OLD:
            # vm_jan = res_p_sys_2026_jan.iloc[:, 4:185]
            # power_balance_2026_jan = res_p_sys_2026_jan.iloc[:, 0:3]
            # net_update = res_p_sys_2026_jan[1]
            # res_line_loss_mw_2025_jan_mwh = res_p_sys_2023_jan['line_loss_mw'].sum()

            # NEW:
            # results, net_update = res_p_sys_2026_jan    # FINAL line used

            # net_hour_0 = net_update[0]  # Using to define the location of the bus-bars.
            # net_hour_11 = net_update[11]
            # power_balance_2026_jan = results.iloc[:, 0:3]
            # vm_jan = results.iloc[:, 4:185]

            # print("Power Sys 2026 Jan:\n", power_balance_2026_jan)
            # print("vm_jan_2026 =\n", vm_jan)
            # print("loads = \n", net_hour_0.load['p_mw'])    # For CAPEX I can just use [0], because it is enough to define \
            # the bus-bars if it is industrial or etc.

            # ================================================= F1 2026 ===========================================


            # capex_2026_eaa = capex_2026_pv / ((1-(1/(1+discount_rate)**self.stage))/discount_rate)   # Equivalent Annual Annuity
            # print("capex_2026_eaa =", capex_2026_eaa)

            # --------------------------------------- OPEX 2026 --------------------------------------
            cost_opex = opex(stage=self.stage, year=year_index, net_update=net, # CHANGE: net_update=net_hour_0,
                             x_pv_bus=x_pv_bus, x_pv_mw=x_pv_mw)

            opex_var_loc_elem_2026 = cost_opex.opex_var_loc_elem_2026()
            # print("OPEX_2026 =", opex_var_loc_elem_2026)

            # OLD:
            # opex_fix_loc_elem_2025 = cost_opex.opex_fixed_loc_elem_2025()
            # opex_e_net_2025 = cost_opex.opex_e_net_2025()

            opex_year = opex_var_loc_elem_2026
            print("opex_year =", opex_year)
            opex_year_npv = opex_year * (1 / (1 + discount_rate) ** year_index)
            stage_opex_total += opex_year_npv

            print(f"Year {year} OPEX NPV: {opex_year_npv}")

            # ============================================== G 2026===================================================

            # ----------------------------------- Power grid -----------------------------------
            # Note: This will calculate g1 based on the maximum deviation of the voltage
            # values from the acceptable range [0.95, 1.05].

            # test: ------------------------------------------>
            # vm_jan = pd.DataFrame([0.92]*24, columns=['value'])
            # print("vm_jan =", vm_jan)

            # Jan:
            # for idx, row in vm_jan.iterrows():
            #     for col in vm_jan.columns[1:]:
            #         val = row[col]
            #         violation = max(min_v_drop - val, val - max_v_drop)
            #         if violation > 0:
            #             g1_power_grid_jan += violation
            #             penalty += 1e6 * violation
            #     # print("g1_power_grid_jan =", g1_power_grid_jan)
            #     print("penalty =", penalty)

            # Jun:
            # for idx, row in vm_jul.iterrows():
            #     for col in vm_jul.columns[1:]:
            #         val = row[col]
            #         violation = max(min_v_drop - val, val - max_v_drop)
            #         if violation > 0:
            #             g1_power_grid_jul += violation
            #             penalty += 1e6 * violation

        # elif self.year == 2027:
        #     exit()

        total_stage_cost += stage_opex_total

        print(f"Stage {self.stage} Total Cost: {total_stage_cost}")

        out["penalty"] = penalty
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

gen_size = 5
pop_size = 10


# installed_capacities_pv_per_year_mw = {
#     2025: {}, 2026: {}, 2027: {}, 2028: {}, 2029: {}, 2030: {}, 2031: {}, 2032: {}, 2033: {}, 2034: {}, 2035: {},
#     2036: {}, 2037: {}, 2038: {}, 2039: {}, 2040: {}
# }
#
#
# all_X = []
# all_F = []
# results = []
# carried_cap_pv_array_mw = np.array([])
# cumulative_capacities_pv = {}
# carried_cap_pv_array_mw = np.zeros(n_bus)  # Preallocate array for 14 PV capacities
# results_df = pd.DataFrame(columns=["Year", "Cost (EUR)"]) #, "CO2 (tCO2)"])

# ================= STAGE-LEVEL OPTIMIZATION =================
for stage_num in [1, 2, 3]:
    stage_years = stages[stage_num]

    print(f"\n{'=' * 50}")
    print(f"OPTIMIZING STAGE {stage_num}")
    print(f"Years: {stage_years}")
    print(f"Carried PV Capacity: {cumulative_capacities_pv}")
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

    # Extract best solution
    # best_idx = np.argmin(res.F[:, 0])
    best_idx = res.F
    # best_solution = res.X[best_idx]
    best_solution = res.X
    # best_cost = res.F[best_idx, 0]
    best_cost = res.F

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
print(f"Total Project Cost (NPV): {total_project_cost:.2f} EUR")
print(f"Total PV Capacity Installed: {cumulative_capacities_pv.sum():.2f} MW")

# Create summary DataFrame
summary_data = []
for result in all_stage_results:
    summary_data.append({
        'Stage': result['stage'],
        'Years': f"{result['years'][0]}-{result['years'][-1]}",
        'Stage Cost (EUR)': result['stage_cost'],
        'New PV Capacity (MW)': result['new_pv_capacity'].sum(),
        'Cumulative PV Capacity (MW)': result['cumulative_pv_capacity'].sum()
    })

summary_df = pd.DataFrame(summary_data)
print("\nStage Summary:")
print(summary_df)


# for year in years:
#     print("----------------- YEAR: ----------------------")
#     print('------------------', year, '---------------------')
#     print("----------------------------------------------")
#
#     if year == 2026 and 2027 and 2028 and 2029 and 2030:
#         stage = 1
#     elif year == 2031 and 2032 and 2033 and 2034 and 2035:
#         stage = 2
#     elif year == 2036 and 2037 and 2038 and 2039 and 2040:
#         stage = 3
#
#     # Pass carried capacity for the current year
#
#     # prob = MyProblem(year=year, stage=stage)
#     prob = MyProblem(year=year, stage=stage, carried_cap_pv_array_mw=carried_cap_pv_array_mw)
#
#     algorithm = MixedVariableGA(pop_size=pop_size,
#                                 Sampling=MixedVariableSampling(),
#                                 mating=MixedVariableMating(eliminate_duplicates=MixedVariableDuplicateElimination()),
#                                 element_duplicates=MixedVariableDuplicateElimination(),
#                                 survival=RankAndCrowdingSurvival(),
#                                 crossover=crossover,
#                                 mutation=mutation,
#                                 eliminate_duplicates=False
#                                 )
#
#     termination = get_termination("n_gen", gen_size)
#
#     res = minimize(prob,
#                    algorithm,
#                    termination,
#                    seed=1,
#                    # output=MyOutput(),
#                    save_history=True,
#                    verbose=True)
#
#     X = res.X
#     F = res.F
#     # print("F =", F)
#
#     # Choose the best solution for this year # 06.09.2024
#     # best_idx = np.argmin(F[:, 0])
#     # best_solution = X[best_idx]  # old: X
#     # best_objective = F[best_idx]
#     # print("Best Solution:", best_solution)
#     # print("Best Objective Value:", best_objective)
#
#     all_X.append(X)
#     all_F.append(F)
#
#     # Convert F to a DataFrame and add the year
#     year_df = pd.DataFrame(F, columns=["Cost (EUR)"])   #, "CO2 (tCO2)"])
#     year_df["Year"] = year
#
#     # Sort the DataFrame by "Cost (EUR)" (F1) in descending order
#     year_df = year_df.sort_values(by="Cost (EUR)", ascending=False)
#
#     # Append the results to the main DataFrame
#     results_df = pd.concat([results_df, year_df], ignore_index=True)
#     print(results_df)
#
#     # X:
#     best_solution_x = X
#     best_solution_x_df = pd.DataFrame(list(best_solution_x.items()), columns=['Strings', 'Results'])
#     # print("Best Solution: \n", best_solution_x_df[179:537])
#
#     # Get the first set: idx 179-357 (Python index is exclusive, so 358 is not included)
#     col1_pv_bus = best_solution_x_df.iloc[179:358].reset_index(drop=True)
#     # Get the second set: idx 358-536 (again, exclusive, so 537 not included)
#     col2_pv_mw = best_solution_x_df.iloc[358:537].reset_index(drop=True)
#
#     # Put them side by side
#     result_df = pd.DataFrame({
#         'PV_BusBar': col1_pv_bus['Results'],
#         'PV_MW': col2_pv_mw['Results']
#     })
#
#     print(result_df)
#
#     # ------------------------------ Update installed capacities for next year ------------------------------
#     # ------------- PV -------------
#     pv_mw = result_df['PV_MW']
#     print(pv_mw)
#     print(shit)
#
#     best_solution_pv_production = list(pv_mw.values())
#     # print('best solu PV =', sum(best_solution_pv_production))
#
#     for idx, best_solution_pv in enumerate(best_solution_pv_production):
#         installed_capacities_pv_per_year_mw[year][f'PV{idx + 1}'] = best_solution_pv
#         carried_cap_pv_array_mw[idx] = installed_capacities_pv_per_year_mw[year][f'PV{idx + 1}']
#         cumulative_capacities_pv[year] = carried_cap_pv_array_mw.copy()  # Store a copy to avoid overwriting
#     # print('carried_cap_pv_mw =', carried_cap_pv_array_mw)
#     # Store each year's cumulative carried PV array
#     total_future_capacity_pv = np.sum(list(cumulative_capacities_pv.values()), axis=0)
#     # print('total_future_capacity_pv =', total_future_capacity_pv)
#
#     if year != 2025:
#         carried_cap_pv_array_mw = total_future_capacity_pv
#     # print('carried_cap_pv_mw_sum =', sum(carried_cap_pv_array_mw))
#
#
# # print("X =", all_X)
# # print("F =", all_F)