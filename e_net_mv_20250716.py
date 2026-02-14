
# 2024.07.25

import pandas as pd
import pandapower as pp
from copy import deepcopy

# pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Time series
# =============================================== e Demand ===============================================
# -------------------------- 2025 --------------------------
e_load_time_series_jan = pd.read_csv("input_data_eload_jan15_mixed_load_MW_2020_20240715.csv")     # Base year e_demand [MW]
e_load_time_series_jul = pd.read_csv("eload_jul15_mixed_load_MW_2020_20240715.csv")
# -------------------------- 2026 --------------------------
e_demand_2026_feb = e_load_time_series_jan*1.0255
e_demand_2026_jul = e_load_time_series_jul*1.0255
# -------------------------- 2027 --------------------------
# e_demand_2027_jan = e_load_time_series_jan*1.063
# e_demand_2027_jul = e_load_time_series_jul*1.063
# # -------------------------- 2028 --------------------------
# e_demand_2028_jan = e_load_time_series_jan*1.1139
# e_demand_2028_jul = e_load_time_series_jul*1.1139
# # -------------------------- 2029 --------------------------
# e_demand_2029_jan = e_load_time_series_jan*1.1632
# e_demand_2029_jul = e_load_time_series_jul*1.1632
# # -------------------------- 2030 --------------------------
# e_demand_2030_jan = e_load_time_series_jan*1.2346
# e_demand_2030_jul = e_load_time_series_jul*1.2346
# # -------------------------- 2031 --------------------------
# e_demand_2031_jan = e_load_time_series_jan*1.2789
# e_demand_2031_jul = e_load_time_series_jul*1.2789
# # -------------------------- 2032 --------------------------
# e_demand_2032_jan = e_load_time_series_jan*1.3333
# e_demand_2032_jul = e_load_time_series_jul*1.3333
# # -------------------------- 2033 --------------------------
# e_demand_2033_jan = e_load_time_series_jan*1.3860
# e_demand_2033_jul = e_load_time_series_jul*1.3860
# # -------------------------- 2034 --------------------------
# e_demand_2034_jan = e_load_time_series_jan*1.4438
# e_demand_2034_jul = e_load_time_series_jul*1.4438
# print(e_load_time_series_jan)
# print(e_demand_2026_jan)

# =============================================== Heat demand 2025 ===============================================
# -------------------------- 2025 --------------------------
heat_demand_2025_jan = pd.read_csv("th_load_38_household_dec15.csv")
heat_demand_2025_jul = pd.read_csv("th_load_38_household_jul15.csv")

# # -------------------------- 2026 OLD --------------------------
# heat_demand_2026_jan = heat_demand_2025_jan*0.94    # reduction of heat demand 6% from 2025
# heat_demand_2026_jul = heat_demand_2025_jul*0.94    # reduction of heat demand 6% from 2025
# --------------------------------- 2026 ---------------------------------
heat_demand_2026_feb = heat_demand_2025_jan*(1 - 0.0094)    # reduction of heat demand 0.94% from 2025
heat_demand_2026_jul = heat_demand_2025_jul*(1 - 0.0094)    # reduction of heat demand 0.94% from 2025
# --------------------------------- 2027 ---------------------------------
heat_demand_2027_jan = heat_demand_2026_feb*(1 - 0.0095)    # reduction of heat demand 0.95% from 2026
heat_demand_2027_jul = heat_demand_2026_jul*(1 - 0.0095)    # reduction of heat demand 0.95% from 2026
# --------------------------------- 2028 ---------------------------------
heat_demand_2028_jan = heat_demand_2027_jan*(1 - 0.0096)    # reduction of heat demand 0.96% from 2027
heat_demand_2028_jul = heat_demand_2027_jul*(1 - 0.0096)    # reduction of heat demand 0.96% from 2027
# --------------------------------- 2029 ---------------------------------
heat_demand_2029_jan = heat_demand_2028_jan*(1 - 0.0109)    # reduction of heat demand 1.09% from 2028
heat_demand_2029_jul = heat_demand_2028_jul*(1 - 0.0109)    # reduction of heat demand 1.09% from 2028
# --------------------------------- 2030 ---------------------------------
heat_demand_2030_jan = heat_demand_2029_jan*(1 - 0.0)    # reduction of heat demand 0% from 2029
heat_demand_2030_jul = heat_demand_2029_jul*(1 - 0.0)    # reduction of heat demand 0% from 2029
# --------------------------------- 2031 ---------------------------------
heat_demand_2031_jan = heat_demand_2030_jan*(1 - 0.0115)    # reduction of heat demand 0% from 2029
heat_demand_2031_jul = heat_demand_2030_jul*(1 - 0.0115)    # reduction of heat demand 0% from 2029
# --------------------------------- 2032 ---------------------------------
heat_demand_2032_jan = heat_demand_2031_jan*(1 - 0.0117)    # reduction of heat demand 0% from 2029
heat_demand_2032_jul = heat_demand_2031_jul*(1 - 0.0117)    # reduction of heat demand 0% from 2029
# --------------------------------- 2033 ---------------------------------
heat_demand_2033_jan = heat_demand_2032_jan*(1 - 0.0118)    # reduction of heat demand 0% from 2032
heat_demand_2033_jul = heat_demand_2032_jul*(1 - 0.0118)    # reduction of heat demand 0% from 2032
# --------------------------------- 2034 ---------------------------------
heat_demand_2034_jan = heat_demand_2033_jan*(1 - 0.0119)    # reduction of heat demand 0% from 2033
heat_demand_2034_jul = heat_demand_2033_jul*(1 - 0.0116)    # reduction of heat demand 0% from 2033
# print(heat_demand_jan)
# print(heat_demand_2026_jan)

# -------------------------- PV irradiance --------------------------
# pv_time_series = pd.read_csv("input_data_pv_normalised.csv")
pv_time_series = pd.read_csv("input_data_pv_seasonal_comparison_2015.csv")
irradiance_feb = pd.DataFrame(pv_time_series['pv_feb_norm'])
irradiance_jun = pd.DataFrame(pv_time_series['pv_jun_norm'])
irradiance_oct = pd.DataFrame(pv_time_series['pv_oct_norm'])

# -------------------------- Wind profile --------------------------
wind_time_series = pd.read_csv("input_data_wind_power_normalized_weeks.csv")
wt_ts_feb = pd.DataFrame(wind_time_series['wt_power_feb_norm'])
wt_ts_jun = pd.DataFrame(wind_time_series['wt_power_jun_norm'])
wt_ts_oct = pd.DataFrame(wind_time_series['wt_power_oct_norm'])
# print(wind_time_series)


from bess_20240725 import BESS

# =========================================== Power Flow Calc ===========================================


class power_system:
    def __init__(self, net, x_pv_bus, x_pv_mw, x_wt_bus, x_wt_mw, **kwargs): #  chp_bus, chp_p_mw, hp_bus, hp_cap_mw, p2g_input_mw,
                 # , x_gen_bus_12, x_gen_bus_12_mw, x_gen_bus_1, x_gen_bus_1_mw, **kwargs):

        self.net = net
        # self.x = x
        self.x_pv_bus = x_pv_bus
        self.x_pv_mw = x_pv_mw
        self.x_wt_bus = x_wt_bus
        self.x_wt_mw = x_wt_mw
        # self.x_bess_bus = x_bess_bus
        # self.x_bess_p_mw = x_bess_mw
        # self.chp_bus = chp_bus
        # self.chp_p_mw = chp_p_mw
        # self.hp_bus = hp_bus
        # self.hp_cap_mw = hp_cap_mw
        # self.p2g_input_mw = p2g_input_mw
        # self.x_gen_bus_12 = x_gen_bus_12
        # self.x_gen_bus_12_mw = x_gen_bus_12_mw
        # self.x_gen_bus_1 = x_gen_bus_1
        # self.x_gen_bus_1_mw = x_gen_bus_1_mw

        # self.added_load_indices = []  # List to track added loads

    # def add_load(self, bus_idx, p_mw, name):
    #     load_idx = pp.create_load(self.net, bus=bus_idx, p_mw=p_mw, name=name)
    #     self.added_load_indices.append(load_idx)  # Track the added load index
    #
    # def remove_added_loads(self):
    #     for load_idx in self.added_load_indices:
    #         self.net.load.drop(load_idx, inplace=True)  # Remove only the tracked loads
    #     self.added_load_indices.clear()  # Clear the list for the next iteration

    def power_flow_2026_jan(self):      # January with 7 days time series

        results = pd.DataFrame()
        net_update = []



        # ************************ Create loads on the fixed bus bars with 0 p_mw ******************************
        # loads = self.net.load
        # print(loads[['bus', 'p_mw']])

        bus_idx_86 = 86
        loads_at_bus_86 = self.net.load[self.net.load['bus'] == bus_idx_86]
        self.net.load.drop(loads_at_bus_86.index, inplace=True)
        pp.create_load(self.net, bus=bus_idx_86, p_mw=1, name="NEW Load 86")

        bus_idx_126 = 126
        loads_at_bus_126 = self.net.load[self.net.load['bus'] == bus_idx_126]
        self.net.load.drop(loads_at_bus_126.index, inplace=True)
        pp.create_load(self.net, bus=bus_idx_126, p_mw=1, name="NEW Load 126")

        bus_idx_6 = 6
        loads_at_bus_6 = self.net.load[self.net.load['bus'] == bus_idx_6]
        self.net.load.drop(loads_at_bus_6.index, inplace=True)
        pp.create_load(self.net, bus=bus_idx_6, p_mw=1, name="NEW Load 6")

        # print("Loads at bus 86:\n", self.net.load[self.net.load['bus'] == bus_idx_86])
        # print("Loads at bus 126:\n", self.net.load[self.net.load['bus'] == bus_idx_126])
        # print("Loads at bus 6:\n", self.net.load[self.net.load['bus'] == bus_idx_6])

        # --------------------- Store original load values ---------------------
        original_loads = self.net.load['p_mw'].copy()

        # ************************* Special loads **********************************
        # HP load at household bus
        # pp.create_load(self.net, bus=6, p_mw=0, name="HP load for Households")
        # P2G load at bus = 12
        # pp.create_load(self.net, bus=12, p_mw=0, name="P2G load")

        # ******************************* Create Gas gen at bus 12 ********************************************
        # pp.create_gen(self.net, bus=12, p_mw=self.x_gen_bus_12_mw, vm_pu=1.0, name="Gas Power bus 37")  # Peak load = 29.3 MW
        # Gas gen at bus 1
        # pp.create_gen(self.net, bus=1, p_mw=self.x_gen_bus_1_mw, vm_pu=1.0, name="Gas Power bus 37")  # Peak load = 20.8 MW
        # print(self.net.gen)

        # --------------------------------- Decision variables for PV WT CHP ---------------------------------
        x_pv_bus = self.x_pv_bus
        x_pv_mw = self.x_pv_mw
        x_wt_bus = self.x_wt_bus
        x_wt_mw = self.x_wt_mw
        # print("PV_MW=", x_pv_mw.sum())

        # # ----- PV -----
        # for bus, p_mw in zip(x_pv_bus, x_pv_mw):
        #     pp.create_sgen(self.net, bus=bus, p_mw=p_mw, q_mvar=0, name="PV")
        # print(self.net.sgen)
        # ----- WT
        # x_wt_bus = self.x_wt_bus
        # for bus in x_wt_bus:
        #     pp.create_sgen(self.net, bus=bus, p_mw=0, q_mvar=0, name="WT")
        # ----- CHP
        # x_chp_bus = self.chp_bus
        # pp.create_sgen(self.net, bus=x_chp_bus, p_mw=0, q_mvar=0, name="CHP")

        # ****************************************** Create BESS ********************************************
        # pp.create_storage(self.net, bus=self.bess_bus, p_mw=0, max_e_mwh=self.bess_p_mw*12*0.9,
        #                   soc_percent=0.5, name="BESS")

        # bess_mw = self.bess_p_mw  # this is already for 1 hour = MWh for each battery
        # bess_mwh = self.bess_p_mw * 1    # for each hour
        # bess_soc = 0.5

        # bess_init_mwh = bess_mwh * bess_soc
        # bess_update_mwh = bess_init_mwh

        # $$$$ CHAT GPT BES Model $$$$$
        # storage_idx = pp.create_storage(self.net, bus=self.bess_bus, p_mw=0.0, max_e_mwh=5.0, soc_percent=0.50,
        #                                 min_p_mw=-bess_mw, max_p_mw=bess_mw, max_q_mvar=0.5, min_q_mvar=-0.5,
        #                                 name="BESS_0")

        # ---------------------------------- Time series analysis ----------------------------------
        for t, (load_idx, load_row) in enumerate(e_demand_2026_feb.iterrows()):

            print("time =", t)

            # ------------------ Time series input data for PV and WT ------------------
            irradiance_row = irradiance_feb.iloc[t]
            wind_row = wt_ts_feb.iloc[t]

            # Reset all loads to original values at the start of each time step
            self.net.load['p_mw'] = original_loads.copy()

            for load_idx, load in self.net.load.iterrows():
                bus_idx = load['bus']
                p_mw = load['p_mw']
                # print(f"Load at bus {bus_idx}: {p_mw} MW")
                # print("Load_time_series", load_row['SFH9'])

                # ---------------- Chem industry loads ----------------
                self.net.load.at[147, 'p_mw'] = load_row['LG 01']  # Assuming Chem Industry Load 1 is at index 147
                self.net.load.at[148, 'p_mw'] = load_row['LG 07']  # Assuming Chem Industry Load 1 is at index 148
                self.net.load.at[149, 'p_mw'] = load_row['LG 03']  # Assuming small Industry Load 1 is at index 149

                # ---------------- Inclusion of the time series ----------------
                # Small industrial loads    --> Temporary loads with time series
                if p_mw >= 0.50:
                    # self.net.load.at[load_idx, 'p_mw'] = load_row['small_ind_load_1'] * p_mw
                    self.net.load.at[load_idx, 'p_mw'] = load_row['eload_med_ind'] * p_mw
                    # print(f"Small industrial load at bus {bus_idx} = {self.net.load.at[load_idx, 'p_mw']} MW")
                # Residential loads
                elif p_mw < 0.3:
                    self.net.load.at[load_idx, 'p_mw'] = load_row['SFH9'] * p_mw
                    # print(f"Residential load at bus {bus_idx} = {self.net.load.at[load_idx, 'p_mw']} MW")
                # Commercial loads
                else:
                    self.net.load.at[load_idx, 'p_mw'] = load_row['eload_comm'] * p_mw

            # print(self.net.load[['bus', 'p_mw']])

                # # ************************ Special loads **************************
                # # HP load @ Household bus
                # self.net.load.at[12, 'p_mw'] = heat_demand_2025_jan['th_load_38_household'][i]
                # # P2G at bus = 12
                # self.net.load.at[13, 'p_mw'] = self.p2g_input_mw

            # ---------------------------------- PV & WT ----------------------------------
            # ----- PV -----
            for bus, p_mw in zip(x_pv_bus, x_pv_mw):
                pp.create_sgen(self.net, bus=bus, p_mw=p_mw * irradiance_row, q_mvar=0, name="PV")
            # print(self.net.sgen.head(5))

            # ----- WT -----
            for bus, p_mw in zip(x_wt_bus, x_wt_mw):
                pp.create_sgen(self.net, bus=bus, p_mw=p_mw * wind_row, q_mvar=0, name="WT")
            print(self.net.sgen.head(5))

            # print("PV Idx =", self.net.sgen.index)
            # print("pv-bus =", self.x_pv_bus[t])
            # print("pv-mw =", self.x_pv_mw)
            # print("irradiance_row =", irradiance_row['jan'])

            # for pv_idx, pv_mw in self.net.sgen.iterrows():
            #     # print(pv_idx)
            #     # print(pv_mw)
            #
            #     self.net.sgen.at[self.net.sgen.index[t], 'p_mw'] = self.x_pv_mw[t]*irradiance_row['jan']
            # pp.create_sgen(self.net, bus=self.x_pv_bus[t], p_mw=irradiance_row['jan'] * self.x_pv_mw[t])

            # self.net.sgen.at[1, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[1]
            # self.net.sgen.at[2, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[2]
            # self.net.sgen.at[3, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[3]
            # self.net.sgen.at[4, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[4]
            # self.net.sgen.at[5, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[5]
            # self.net.sgen.at[6, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[6]
            # self.net.sgen.at[7, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[7]
            # self.net.sgen.at[8, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[8]
            # self.net.sgen.at[9, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[9]
            # self.net.sgen.at[10, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[10]
            # self.net.sgen.at[11, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[11]
            # self.net.sgen.at[12, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[12]
            # self.net.sgen.at[13, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[13]

            # ---------------------------------- WT ----------------------------------
        #     # print("wt_time_series =", wind_time_series['wind_normalized_jan'][i])
        #     # self.net.sgen.at[14, 'p_mw'] = wind_time_series['wind_normalized_jan'][i] * self.x_wt_mw
        #     # Assuming WT 1 is at index 14
        #
        #     # *************************** CHP ***************************
        #     # self.net.sgen.at[15, 'p_mw'] = self.chp_p_mw
        #     # print(self.net.sgen)
        #
        #     # ***************************** BESS *******************************************
        #     # print("bess_mw", bess_mw)
        #     # print("tot_sgen =", self.net.sgen['p_mw'].sum())
        #     # print("tot_demand_e =", self.net.load['p_mw'].sum())
        #     # print()
        #     bess = BESS(net=self.net, sgen_mwh=self.net.sgen['p_mw'].sum(), demand_e_mwh=self.net.load['p_mw'].sum(),
        #                 bess_mw=bess_mw,
        #                 bess_mwh=bess_mwh,
        #                 # bess_soc=bess_soc,
        #                 # current_energy=bess_current_energy,
        #                 # bess_max_energy=bess_max_energy,
        #                 # bess_min_energy=bess_min_energy,
        #                 bess_update_mwh=bess_update_mwh)
        #     res_bess_mw = bess.adjust_bess()[0]
        #     res_bess_mwh = bess.adjust_bess()[1]
        #
        #     self.net.storage.at[0, 'p_mw'] = res_bess_mw
        #     # bess_mw_update += res_bess_mwh
        #     bess_update_mwh = res_bess_mwh
        #     # print("bess_mw_update =", bess_mw_update)
        #     # print(self.net.storage)

            # print("Loads:")
            # print(self.net.load['p_mw'].sum())
            # print("PVs = \n", self.net.sgen['p_mw'].sum())

            pp.runpp(self.net)

            # print("Power flow:")

            # Using to copy the updated net before using the remove function. This values are used in the CAPEX func.
            # net_update is copying the new net after each time step, means it creates a new net for each time step.
            # For example: if I have 24 time steps, then I will have 24 nets in the net_update list. This applies for
            # PV, loads and all net elements.
            net_update.append(deepcopy(self.net))
            # print("Net Update =\n", self.net.load['p_mw'])

            result = {
                # 'time_step': t,
                'demand_mw': self.net.res_load.p_mw.sum(),  # summing the total load at each hour (t)
                # 'line_loss_mw': self.net.res_line.pl_mw.values[0],
                # 'gas_gen_mw': self.net.res_gen.p_mw.sum(),
                'pv_wt_chp_mw': self.net.res_sgen.p_mw.sum(),  # summing the total PV gen at each hour (t)
                # 'bess_mw': self.net.res_storage.p_mw.sum(),
                'ext_grid_mw': self.net.res_ext_grid.p_mw.sum(),
                # 'bess_mwh': res_bess_mwh
            }

            for bus_idx in self.net.bus.index:
                result[f'bus_{int(bus_idx)}_voltage_pu'] = self.net.res_bus.vm_pu[bus_idx]

            results = results.append(result, ignore_index=True)

            power_system.remove_sgen(self)  # it works only if I remove the PVs end of each for loop
            # power_system.remove_load(self)  # I don't need this because: self.net.load['p_mw'] = original_loads.copy()
            # p_sys.remove_gen()
            # p_sys.remove_load()
            # p_sys.remove_bess()

        # print(net_update)
        # print(results)
        # print(x)

        return results, net_update


    def power_flow_2025_jan_NEW(self):

        results = pd.DataFrame()

        # ************************ Create loads on the fixed bus bars with 0 p_mw ******************************
        pp.create_load(self.net, bus=1, p_mw=0, name="Chem Ind Load 1")
        pp.create_load(self.net, bus=12, p_mw=0, name="Chem Ind Load 2")
        pp.create_load(self.net, bus=2, p_mw=0, name="Medium Ind Load 1")
        pp.create_load(self.net, bus=13, p_mw=0, name="Small Ind Load 1")
        pp.create_load(self.net, bus=14, p_mw=0, name="Small Ind Load 2")
        # Commercial loads
        pp.create_load(self.net, bus=3, p_mw=0, name="Commercial load 1")
        pp.create_load(self.net, bus=4, p_mw=0, name="Commercial load 2")
        pp.create_load(self.net, bus=5, p_mw=0, name="Commercial load 3")
        pp.create_load(self.net, bus=9, p_mw=0, name="Commercial load 4")
        pp.create_load(self.net, bus=10, p_mw=0, name="Commercial load 5")
        pp.create_load(self.net, bus=11, p_mw=0, name="Commercial load 6")
        # Household load
        pp.create_load(self.net, bus=6, p_mw=0, name="Household load")  # 38 households
        # print(self.net.load)

        # # ************************* Special loads **********************************
        # # HP load at household bus
        # pp.create_load(self.net, bus=6, p_mw=0, name="HP load for Households")
        # # P2G load at bus = 12
        # pp.create_load(self.net, bus=12, p_mw=0, name="P2G load")

        # ******************************* Create Gas gen/CHP at bus 12 & 1 ********************************************
        pp.create_gen(self.net, bus=12, p_mw=self.x_gen_bus_12_mw, vm_pu=1.0, name="Gas Power bus 37")  # Peak load = 29.3 MW
        pp.create_gen(self.net, bus=1, p_mw=self.x_gen_bus_1_mw, vm_pu=1.0, name="Gas Power bus 37")  # Peak load = 20.8 MW

        # CHP
        x_chp_bus = self.chp_bus
        pp.create_gen(self.net, bus=x_chp_bus, p_mw=self.chp_p_mw, name="CHP")
        # print(self.net.gen)

        # ******************** PV WT CHP ***********************
        # Create sgens (PV+WT) at each of the specified x_bus-bar with initial p_mw = 0
        x_pv_bus = self.x_pv_bus
        # PV
        for bus in x_pv_bus:
            pp.create_sgen(self.net, bus=bus, p_mw=0, q_mvar=0, name="PV")

        # WT
        x_wt_bus = self.x_wt_bus
        for bus in x_wt_bus:
            pp.create_sgen(self.net, bus=bus, p_mw=0, q_mvar=0, name="WT")

        # ****************************************** Create BESS ********************************************
        pp.create_storage(self.net, bus=self.bess_bus, p_mw=0, max_e_mwh=self.bess_p_mw*12*0.9,
                          soc_percent=0.5, name="BESS")
        # print("x_bess_mw =", self.bess_p_mw)
        # print(self.net.storage)

        bess_mw = self.bess_p_mw  # this is already for 1 hour = MWh for each battery
        bess_mwh = self.bess_p_mw * 1    # for each hour
        bess_soc = 0.5

        bess_init_mwh = bess_mwh * bess_soc
        bess_update_mwh = bess_init_mwh
        # print("current_bess_energy", bess_update_mwh)

        # $$$$ CHAT GPT BES Model $$$$$
        # storage_idx = pp.create_storage(self.net, bus=self.bess_bus, p_mw=0.0, max_e_mwh=5.0, soc_percent=0.50,
        #                                 min_p_mw=-bess_mw, max_p_mw=bess_mw, max_q_mvar=0.5, min_q_mvar=-0.5,
        #                                 name="BESS_0")

        for i, ((load_idx, load_row), (irradiance_idx, irradiance_row)) in \
                enumerate(zip(e_load_time_series_jan.iterrows(),
                              df_irradiance_jan.iterrows())):
            # print("i_jan =", i)
            # print("eload_jan =", load_row['LG 07'])
            # print("PV_irr_jan =", irradiance_row)
            # print("w_speed_jan =", wind_time_series['wind_normalized_jan'][i])
            # # print("th_demand_jan", heat_demand_jan['th_load_38_household'][i])
            # print()

            # ********************* Update the load values at the specified buses *********************
            # Ind, comm and res loads
            self.net.load.at[0, 'p_mw'] = load_row['LG 01']  # Assuming Chem Industry Load 1 is at index 0
            self.net.load.at[1, 'p_mw'] = load_row['LG 07']  # Peak load = 29.3 MW - Chem Industry Load 2 is at index 1
            self.net.load.at[2, 'p_mw'] = load_row['LG 03']     # Medium industry
            self.net.load.at[3, 'p_mw'] = load_row['small_ind_load_1']
            self.net.load.at[4, 'p_mw'] = load_row['small_ind_load_2']
            # Commercial loads
            self.net.load.at[5, 'p_mw'] = load_row['load_bus3']  # load at bus3
            self.net.load.at[6, 'p_mw'] = load_row['load_bus4']
            self.net.load.at[7, 'p_mw'] = load_row['load_bus5']
            self.net.load.at[8, 'p_mw'] = load_row['load_bus9']
            self.net.load.at[9, 'p_mw'] = load_row['load_bus10']
            self.net.load.at[10, 'p_mw'] = load_row['load_bus11']
            # Household load
            self.net.load.at[11, 'p_mw'] = load_row['load_bus6']  # *10 around 38*10 households

            # # ************************ Special loads **************************
            # # HP load @ Household bus
            # self.net.load.at[12, 'p_mw'] = heat_demand_2025_jan['th_load_38_household'][i]
            # # P2G at bus = 12
            # self.net.load.at[13, 'p_mw'] = self.p2g_input_mw

            # print(self.net.load)

            # *************************** PV ***************************
            # print(self.x[14])
            # print(self.x_pv_mw[0])
            self.net.sgen.at[0, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[0]  # Assuming PV 1 is at index 0
            self.net.sgen.at[1, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[1]
            self.net.sgen.at[2, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[2]
            self.net.sgen.at[3, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[3]
            self.net.sgen.at[4, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[4]
            self.net.sgen.at[5, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[5]
            self.net.sgen.at[6, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[6]
            self.net.sgen.at[7, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[7]
            self.net.sgen.at[8, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[8]
            self.net.sgen.at[9, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[9]
            self.net.sgen.at[10, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[10]
            self.net.sgen.at[11, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[11]
            self.net.sgen.at[12, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[12]
            self.net.sgen.at[13, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[13]

            # *************************** WT ***************************
            # print("wt_time_series =", wind_time_series['wind_normalized_jan'][i])
            self.net.sgen.at[14, 'p_mw'] = wind_time_series['wind_normalized_jan'][i] * self.x_wt_mw
            # Assuming WT 1 is at index 14

            # *************************** CHP ***************************
            # self.net.sgen.at[15, 'p_mw'] = self.chp_p_mw

            # print(self.net.sgen)

            # ***************************** BESS *******************************************
            # print("bess_mw", bess_mw)
            # print("tot_sgen =", self.net.sgen['p_mw'].sum())
            # print("tot_demand_e =", self.net.load['p_mw'].sum())
            # print()
            bess = BESS(net=self.net, sgen_mwh=self.net.sgen['p_mw'].sum(), demand_e_mwh=self.net.load['p_mw'].sum(),
                        bess_mw=bess_mw,
                        bess_mwh=bess_mwh,
                        bess_update_mwh=bess_update_mwh)
            res_bess_mw = bess.adjust_bess()[0]
            res_bess_mwh = bess.adjust_bess()[1]

            self.net.storage.at[0, 'p_mw'] = res_bess_mw
            # bess_mw_update += res_bess_mwh
            bess_update_mwh = res_bess_mwh
            # print("bess_mwh_update =", bess_update_mwh)
            # print(self.net.storage)

            pp.runpp(self.net)

            result = {
                # 'time_step': i,
                'demand_mw': self.net.res_load.p_mw.sum(),  # summing the total load at each hour (t)
                'line_loss_mw': self.net.res_line.pl_mw.values[0],
                'gas_gen_mw': self.net.res_gen.p_mw.sum(),
                'pv_wt_chp_mw': self.net.res_sgen.p_mw.sum(),  # summing the total PV gen at each hour (t)
                'bess_mw': self.net.res_storage.p_mw.sum(),
                'ext_grid_mw': self.net.res_ext_grid.p_mw.values[0],
                'bess_mwh': res_bess_mwh
            }

            for bus_idx in self.net.bus.index:
                result[f'bus_{int(bus_idx)}_voltage_pu'] = self.net.res_bus.vm_pu[bus_idx]

            results = results.append(result, ignore_index=True)
        # print(results)
        return results

    # ============================================= 2025 - July =============================================
    def power_flow_2025_jul(self):

        results = pd.DataFrame()

        # --------------------- Create loads on the fixed bus bars with p_mw=0 ---------------------
        pp.create_load(self.net, bus=1, p_mw=0, name="Chem Ind Load 1")
        pp.create_load(self.net, bus=12, p_mw=0, name="Chem Ind Load 2")
        pp.create_load(self.net, bus=2, p_mw=0, name="Medium Ind Load 1")
        pp.create_load(self.net, bus=13, p_mw=0, name="Small Ind Load 1")
        pp.create_load(self.net, bus=14, p_mw=0, name="Small Ind Load 2")
        # Commercial loads
        pp.create_load(self.net, bus=3, p_mw=0, name="Commercial load 1")
        pp.create_load(self.net, bus=4, p_mw=0, name="Commercial load 2")
        pp.create_load(self.net, bus=5, p_mw=0, name="Commercial load 3")
        pp.create_load(self.net, bus=9, p_mw=0, name="Commercial load 4")
        pp.create_load(self.net, bus=10, p_mw=0, name="Commercial load 5")
        pp.create_load(self.net, bus=11, p_mw=0, name="Commercial load 6")
        # Household load
        pp.create_load(self.net, bus=6, p_mw=0, name="Household load")  # 38 households

        # --------------------- Special loads ---------------------
        # HP load at household bus=6
        pp.create_load(self.net, bus=6, p_mw=0, name="HP load for Households")
        # P2G load at bus=12
        pp.create_load(self.net, bus=12, p_mw=0, name="P2G load")

        # --------------------- Create Gas-Gen at bus=12 ---------------------
        pp.create_gen(self.net, bus=12, p_mw=self.x_gen_bus_12_mw, vm_pu=1.0, name="Gas Power bus 37")  # Peak load = 29.3 MW
        # Gas gen at bus 1
        pp.create_gen(self.net, bus=1, p_mw=self.x_gen_bus_1_mw, vm_pu=1.0, name="Gas Power bus 37")  # Peak load = 20.8 MW
        # print(self.net.gen)

        # --------------------- Create Sgen at x_bus-bar with p_mw=0 ---------------------
        # PV
        x_pv_bus = self.x_pv_bus
        for bus in x_pv_bus:
            pp.create_sgen(self.net, bus=bus, p_mw=0, q_mvar=0, name="PV")

        # WT
        x_wt_bus = self.x_wt_bus
        for bus in x_wt_bus:
            pp.create_sgen(self.net, bus=bus, p_mw=0, q_mvar=0, name="WT")

        # CHP
        x_chp_bus = self.chp_bus
        pp.create_sgen(self.net, bus=x_chp_bus, p_mw=0, q_mvar=0, name="CHP")

        # print(self.net.sgen)

        # --------------------- Create BESS at x_bus-bar with p_mw=0 ---------------------
        pp.create_storage(self.net, bus=self.bess_bus, p_mw=0, max_e_mwh=self.bess_p_mw*12*0.9,
                          soc_percent=0.5, name="BESS")

        bess_mw = self.bess_p_mw            # this is already for 1 hour = MWh for each battery
        bess_mwh = self.bess_p_mw * 1       # for each hour
        bess_soc = 0.5

        bess_init_mwh = bess_mwh * bess_soc
        bess_update_mwh = bess_init_mwh
        # print("current_bess_energy", bess_update_mwh)

        # ------------------------------------------- 2025 - July -----------------------------------------
        for i, ((load_idx, load_row), (irradiance_idx, irradiance_row)) in \
                enumerate(zip(e_load_time_series_jul.iterrows(), df_irradiance_jul.iterrows())):

            # print("i_jul =", i)
            # print("eload_jul =", load_row['LG 07'])
            # print("PV_irr_jul =", irradiance_row)
            # print("w speed jul =", wind_time_series['wind_normalized_jul'][i])
            # # print("th_jul =", heat_demand_jul['th_load_38_household'])
            # print()

            # ----------------------- Update the load values at the specified buses -----------------------
            # Ind, comm and res loads
            self.net.load.at[0, 'p_mw'] = load_row['LG 01']  # Assuming Chem Industry Load 1 is at index 0
            self.net.load.at[1, 'p_mw'] = load_row['LG 07']  # Peak load = 29.3 MW - Chem Industry Load 2 is at index 1
            self.net.load.at[2, 'p_mw'] = load_row['LG 03']     # Medium industry
            self.net.load.at[3, 'p_mw'] = load_row['small_ind_load_1']
            self.net.load.at[4, 'p_mw'] = load_row['small_ind_load_2']
            # Commercial loads
            self.net.load.at[5, 'p_mw'] = load_row['load_bus3']  # load at bus3
            self.net.load.at[6, 'p_mw'] = load_row['load_bus4']
            self.net.load.at[7, 'p_mw'] = load_row['load_bus5']
            self.net.load.at[8, 'p_mw'] = load_row['load_bus9']
            self.net.load.at[9, 'p_mw'] = load_row['load_bus10']
            self.net.load.at[10, 'p_mw'] = load_row['load_bus11']
            # Household load
            self.net.load.at[11, 'p_mw'] = load_row['load_bus6']  # *10 around 38*10 households

            # ----------------------- Special loads -----------------------
            # HP load at Household bus=6
            self.net.load.at[12, 'p_mw'] = heat_demand_2025_jul['th_load_38_household'][i]
            # P2G at bus=12
            self.net.load.at[13, 'p_mw'] = self.p2g_input_mw

            # print(self.net.load)

            # ----------------------- PV Update -----------------------
            # print(self.x[14:28])
            self.net.sgen.at[0, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[0]  # Assuming PV 1 is at index 0
            self.net.sgen.at[1, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[1]
            self.net.sgen.at[2, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[2]
            self.net.sgen.at[3, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[3]
            self.net.sgen.at[4, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[4]
            self.net.sgen.at[5, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[5]
            self.net.sgen.at[6, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[6]
            self.net.sgen.at[7, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[7]
            self.net.sgen.at[8, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[8]
            self.net.sgen.at[9, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[9]
            self.net.sgen.at[10, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[10]
            self.net.sgen.at[11, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[11]
            self.net.sgen.at[12, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[12]
            self.net.sgen.at[13, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[13]

            # ----------------------- WT Update -----------------------
            # print("x_wt_mw =", self.x[29])
            # print("wt_time_series =", wind_time_series['wind_normalized_jul'][i]*self.x[29])
            self.net.sgen.at[14, 'p_mw'] = wind_time_series['wind_normalized_jul'][i] * self.x_wt_mw
            # Assuming WT 1 is at index 14

            # *************************** CHP ***************************
            self.net.sgen.at[15, 'p_mw'] = self.chp_p_mw
            # print(self.net.sgen)

            # ***************************** Update BESS *******************************************

            # print("bess_mw", bess_mw)
            # print("tot_sgen =", self.net.sgen['p_mw'].sum())
            # print("tot_demand_e =", self.net.load['p_mw'].sum())
            # print()

            bess = BESS(net=self.net, sgen_mwh=self.net.sgen['p_mw'].sum(), demand_e_mwh=self.net.load['p_mw'].sum(),
                        bess_mw=bess_mw,
                        bess_mwh=bess_mwh,
                        # bess_soc=bess_soc,
                        # current_energy=bess_current_energy,
                        # bess_max_energy=bess_max_energy,
                        # bess_min_energy=bess_min_energy,
                        bess_update_mwh=bess_update_mwh)
            res_bess_mw = bess.adjust_bess()[0]
            res_bess_mwh = bess.adjust_bess()[1]

            self.net.storage.at[0, 'p_mw'] = res_bess_mw
            # bess_mw_update += res_bess_mwh
            bess_update_mwh = res_bess_mwh
            # print("bess_mw_update =", bess_mw_update)
            # print(self.net.storage)

            pp.runpp(self.net)

            result = {
                # 'time_step': i,
                'demand_mw': self.net.res_load.p_mw.sum(),  # summing the total load at each hour (t)
                'line_loss_mw': self.net.res_line.pl_mw.values[0],
                'gas_gen_mw': self.net.res_gen.p_mw.sum(),
                'pv_wt_chp_mw': self.net.res_sgen.p_mw.sum(),  # summing the total PV gen at each hour (t)
                'bess_mw': self.net.res_storage.p_mw.sum(),
                'ext_grid_mw': self.net.res_ext_grid.p_mw.values[0],
                'bess_mwh': res_bess_mwh
            }

            for bus_idx in self.net.bus.index:
                result[f'bus_{int(bus_idx)}_voltage_pu'] = self.net.res_bus.vm_pu[bus_idx]

            results = results.append(result, ignore_index=True)

            # print(results.iloc[:, 0:6])

        return results

    # ===================================================== 2026 ======================================================
    # NOTE: Data input to change: 1. e_demand (Jan/July), 2. PV irradiance & WIND profile  3. heat_demand (Jan/July)
    def power_flow_2026_jan_(self):

        results = pd.DataFrame()

        # -------------------------- Create loads on the fixed bus bars with 0 p_mw --------------------------
        pp.create_load(self.net, bus=1, p_mw=0, name="Chem Ind Load 1")
        pp.create_load(self.net, bus=12, p_mw=0, name="Chem Ind Load 2")
        pp.create_load(self.net, bus=2, p_mw=0, name="Medium Ind Load 1")
        pp.create_load(self.net, bus=13, p_mw=0, name="Small Ind Load 1")
        pp.create_load(self.net, bus=14, p_mw=0, name="Small Ind Load 2")
        # Commercial loads
        pp.create_load(self.net, bus=3, p_mw=0, name="Commercial load 1")
        pp.create_load(self.net, bus=4, p_mw=0, name="Commercial load 2")
        pp.create_load(self.net, bus=5, p_mw=0, name="Commercial load 3")
        pp.create_load(self.net, bus=9, p_mw=0, name="Commercial load 4")
        pp.create_load(self.net, bus=10, p_mw=0, name="Commercial load 5")
        pp.create_load(self.net, bus=11, p_mw=0, name="Commercial load 6")
        # Household load
        pp.create_load(self.net, bus=6, p_mw=0, name="Household load")  # 38 households

        # --------------------------Special loads --------------------------
        # HP load at household bus
        pp.create_load(self.net, bus=6, p_mw=0, name="HP load for Households")
        # P2G load at bus = 12
        pp.create_load(self.net, bus=12, p_mw=0, name="P2G load")

        # -------------------------- Create Gas gen at bus 12 --------------------------
        pp.create_gen(self.net, bus=12, p_mw=self.x_gen_bus_12_mw, vm_pu=1.0, name="Gas Power bus 37")  # Peak load = 29.3 MW
        # Gas gen at bus 1
        pp.create_gen(self.net, bus=1, p_mw=self.x_gen_bus_1_mw, vm_pu=1.0, name="Gas Power bus 37")  # Peak load = 20.8 MW
        # print(self.net.gen)

        # --------------------------PV, WT & CHP --------------------------
        # Create sgens (PV+WT) at each of the specified x_bus-bar with initial p_mw = 0
        x_pv_bus = self.x_pv_bus
        # PV
        for bus in x_pv_bus:
            pp.create_sgen(self.net, bus=bus, p_mw=0, q_mvar=0, name="PV")
        # WT
        x_wt_bus = self.x_wt_bus
        for bus in x_wt_bus:
            pp.create_sgen(self.net, bus=bus, p_mw=0, q_mvar=0, name="WT")
        # CHP
        x_chp_bus = self.chp_bus
        pp.create_sgen(self.net, bus=x_chp_bus, p_mw=0, q_mvar=0, name="CHP")

        # ----------------------------------------- Create BESS -----------------------------------------
        pp.create_storage(self.net, bus=self.bess_bus, p_mw=0, max_e_mwh=self.bess_p_mw*12*0.9,
                          soc_percent=0.5, name="BESS")
        # print(self.net.storage)

        bess_mw = self.bess_p_mw        # this is already for 1 hour = MWh for each battery
        bess_mwh = self.bess_p_mw * 1    # C rate = 1 = max capacity charge and discharge in 1 hr.
        bess_soc = 0.1

        bess_init_mwh = bess_mwh * bess_soc
        bess_update_mwh = bess_init_mwh
        # print("current_bess_energy", bess_update_mwh)

        for i, ((load_idx, load_row), (irradiance_idx, irradiance_row)) in \
                enumerate(zip(e_demand_2026_jan.iterrows(),
                              df_irradiance_jan.iterrows())):
            # print("i_jan =", i)
            # print("eload_jan =", load_row['LG 07'])
            # print("PV_irr_jan =", irradiance_row)
            # print("w_speed_jan =", wind_time_series['wind_normalized_jan'][i])
            # # print("th_demand_jan", heat_demand_jan['th_load_38_household'][i])
            # print()

            # ********************* Update the load values at the specified buses *********************
            # Ind, comm and res loads
            self.net.load.at[0, 'p_mw'] = load_row['LG 01']  # Assuming Chem Industry Load 1 is at index 0
            self.net.load.at[1, 'p_mw'] = load_row['LG 07']  # Peak load = 29.3 MW - Chem Industry Load 2 is at index 1
            self.net.load.at[2, 'p_mw'] = load_row['LG 03']     # Medium industry
            self.net.load.at[3, 'p_mw'] = load_row['small_ind_load_1']
            self.net.load.at[4, 'p_mw'] = load_row['small_ind_load_2']
            # Commercial loads
            self.net.load.at[5, 'p_mw'] = load_row['load_bus3']  # load at bus3
            self.net.load.at[6, 'p_mw'] = load_row['load_bus4']
            self.net.load.at[7, 'p_mw'] = load_row['load_bus5']
            self.net.load.at[8, 'p_mw'] = load_row['load_bus9']
            self.net.load.at[9, 'p_mw'] = load_row['load_bus10']
            self.net.load.at[10, 'p_mw'] = load_row['load_bus11']
            # Household load
            self.net.load.at[11, 'p_mw'] = load_row['load_bus6']  # *10 around 38*10 households

            # ************************ Special loads & heat demand **************************
            # HP load @ Household bus
            self.net.load.at[12, 'p_mw'] = heat_demand_2026_jan['th_load_38_household'][i]
            # P2G at bus = 12
            self.net.load.at[13, 'p_mw'] = self.p2g_input_mw

            # print(self.net.load)

            # *************************** PV ***************************
            # print(self.x[14])
            # print(self.x_pv_mw[0])
            self.net.sgen.at[0, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[0]  # Assuming PV 1 is at index 0
            self.net.sgen.at[1, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[1]
            self.net.sgen.at[2, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[2]
            self.net.sgen.at[3, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[3]
            self.net.sgen.at[4, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[4]
            self.net.sgen.at[5, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[5]
            self.net.sgen.at[6, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[6]
            self.net.sgen.at[7, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[7]
            self.net.sgen.at[8, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[8]
            self.net.sgen.at[9, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[9]
            self.net.sgen.at[10, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[10]
            self.net.sgen.at[11, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[11]
            self.net.sgen.at[12, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[12]
            self.net.sgen.at[13, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[13]

            # *************************** WT ***************************
            # print("wt_time_series =", wind_time_series['wind_normalized_jan'][i])
            self.net.sgen.at[14, 'p_mw'] = wind_time_series['wind_normalized_jan'][i] * self.x_wt_mw
            # Assuming WT 1 is at index 14

            # *************************** CHP ***************************
            self.net.sgen.at[15, 'p_mw'] = self.chp_p_mw
            # print(self.net.sgen)

            # ***************************** BESS *******************************************
            # print("bess_mw", bess_mw)
            # print("tot_sgen =", self.net.sgen['p_mw'].sum())
            # print("tot_demand_e =", self.net.load['p_mw'].sum())
            # print()
            bess = BESS(net=self.net, sgen_mwh=self.net.sgen['p_mw'].sum(), demand_e_mwh=self.net.load['p_mw'].sum(),
                        bess_mw=bess_mw,
                        bess_mwh=bess_mwh,
                        # bess_soc=bess_soc,
                        # current_energy=bess_current_energy,
                        # bess_max_energy=bess_max_energy,
                        # bess_min_energy=bess_min_energy,
                        bess_update_mwh=bess_update_mwh)
            res_bess_mw = bess.bms_update()[0]
            res_bess_mwh = bess.bms_update()[1]
            res_bess_power_loss_mwh = bess.bms_update()[2]
            res_bess_power_deficit_mwh = bess.bms_update()[3]

            self.net.storage.at[0, 'p_mw'] = res_bess_mw
            # bess_mw_update += res_bess_mwh
            bess_update_mwh = res_bess_mwh
            # print("bess_mw_update =", bess_mw_update)
            # print(self.net.storage)

            pp.runpp(self.net)

            result = {
                # 'time_step': i,
                'demand_mw': self.net.res_load.p_mw.sum(),  # summing the total load at each hour (t)
                'line_loss_mw': self.net.res_line.pl_mw.values[0],
                'gas_gen_mw': self.net.res_gen.p_mw.sum(),
                'pv_wt_chp_mw': self.net.res_sgen.p_mw.sum(),  # summing the total PV gen at each hour (t)
                'bess_mw': self.net.res_storage.p_mw.sum(),
                'ext_grid_mw': self.net.res_ext_grid.p_mw.values[0],
                'bess_mwh': res_bess_mwh
                # 'res_bess_power_loss_mwh': res_bess_power_loss_mwh,
                # 'res_bess_power_deficit_mwh': res_bess_power_deficit_mwh
            }

            for bus_idx in self.net.bus.index:
                result[f'bus_{int(bus_idx)}_voltage_pu'] = self.net.res_bus.vm_pu[bus_idx]

            results = results.append(result, ignore_index=True)
        # print(results)
        return results

    # ----------------------------------------- 2026 July -----------------------------------------
    # NOTE: Data input to change: 1. e_demand (Jan/July), 2. PV irradiance & WIND profile  3. heat_demand (Jan/July)
    def power_flow_2026_jul(self):

        results = pd.DataFrame()

        # -------------------------- Create loads on the fixed bus bars with 0 p_mw --------------------------
        pp.create_load(self.net, bus=1, p_mw=0, name="Chem Ind Load 1")
        pp.create_load(self.net, bus=12, p_mw=0, name="Chem Ind Load 2")
        pp.create_load(self.net, bus=2, p_mw=0, name="Medium Ind Load 1")
        pp.create_load(self.net, bus=13, p_mw=0, name="Small Ind Load 1")
        pp.create_load(self.net, bus=14, p_mw=0, name="Small Ind Load 2")
        # Commercial loads
        pp.create_load(self.net, bus=3, p_mw=0, name="Commercial load 1")
        pp.create_load(self.net, bus=4, p_mw=0, name="Commercial load 2")
        pp.create_load(self.net, bus=5, p_mw=0, name="Commercial load 3")
        pp.create_load(self.net, bus=9, p_mw=0, name="Commercial load 4")
        pp.create_load(self.net, bus=10, p_mw=0, name="Commercial load 5")
        pp.create_load(self.net, bus=11, p_mw=0, name="Commercial load 6")
        # Household load
        pp.create_load(self.net, bus=6, p_mw=0, name="Household load")  # 38 households

        # -------------------------- Special loads --------------------------
        # HP load at household bus
        pp.create_load(self.net, bus=6, p_mw=0, name="HP load for Households")
        # P2G load at bus = 12
        pp.create_load(self.net, bus=12, p_mw=0, name="P2G load")

        # -------------------------- Create Gas gen at bus 12 --------------------------
        pp.create_gen(self.net, bus=12, p_mw=self.x_gen_bus_12_mw, vm_pu=1.0,
                      name="Gas Power bus 37")  # Peak load = 29.3 MW
        # Gas gen at bus 1
        pp.create_gen(self.net, bus=1, p_mw=self.x_gen_bus_1_mw, vm_pu=1.0,
                      name="Gas Power bus 37")  # Peak load = 20.8 MW
        # print(self.net.gen)

        # -------------------------- PV, WT & CHP --------------------------
        # Create sgens (PV+WT) at each of the specified x_bus-bar with initial p_mw = 0
        x_pv_bus = self.x_pv_bus
        # PV
        for bus in x_pv_bus:
            pp.create_sgen(self.net, bus=bus, p_mw=0, q_mvar=0, name="PV")
        # WT
        x_wt_bus = self.x_wt_bus
        for bus in x_wt_bus:
            pp.create_sgen(self.net, bus=bus, p_mw=0, q_mvar=0, name="WT")
        # CHP
        x_chp_bus = self.chp_bus
        pp.create_sgen(self.net, bus=x_chp_bus, p_mw=0, q_mvar=0, name="CHP")

        # ----------------------------------------- Create BESS -----------------------------------------
        pp.create_storage(self.net, bus=self.bess_bus, p_mw=0, max_e_mwh=self.bess_p_mw * 12 * 0.9,
                          soc_percent=0.5, name="BESS")
        # print(self.net.storage)

        bess_mw = self.bess_p_mw  # this is already for 1 hour = MWh for each battery
        bess_mwh = self.bess_p_mw * 1  # C rate = 1 = max capacity charge and discharge in 1 hr.
        bess_soc = 0.1

        bess_init_mwh = bess_mwh * bess_soc
        bess_update_mwh = bess_init_mwh
        # print("current_bess_energy", bess_update_mwh)

        for i, ((load_idx, load_row), (irradiance_idx, irradiance_row)) in \
                enumerate(zip(e_demand_2026_jul.iterrows(),
                              df_irradiance_jul.iterrows())):
            # print("i_jan =", i)
            # print("eload_jan =", load_row['LG 07'])
            # print("PV_irr_jan =", irradiance_row)
            # print("w_speed_jan =", wind_time_series['wind_normalized_jan'][i])
            # # print("th_demand_jan", heat_demand_jan['th_load_38_household'][i])
            # print()

            # ********************* Update the load values at the specified buses *********************
            # Ind, comm and res loads
            self.net.load.at[0, 'p_mw'] = load_row['LG 01']  # Assuming Chem Industry Load 1 is at index 0
            self.net.load.at[1, 'p_mw'] = load_row[
                'LG 07']  # Peak load = 29.3 MW - Chem Industry Load 2 is at index 1
            self.net.load.at[2, 'p_mw'] = load_row['LG 03']  # Medium industry
            self.net.load.at[3, 'p_mw'] = load_row['small_ind_load_1']
            self.net.load.at[4, 'p_mw'] = load_row['small_ind_load_2']
            # Commercial loads
            self.net.load.at[5, 'p_mw'] = load_row['load_bus3']  # load at bus3
            self.net.load.at[6, 'p_mw'] = load_row['load_bus4']
            self.net.load.at[7, 'p_mw'] = load_row['load_bus5']
            self.net.load.at[8, 'p_mw'] = load_row['load_bus9']
            self.net.load.at[9, 'p_mw'] = load_row['load_bus10']
            self.net.load.at[10, 'p_mw'] = load_row['load_bus11']
            # Household load
            self.net.load.at[11, 'p_mw'] = load_row['load_bus6']  # *10 around 38*10 households

            # ************************ Special loads & heat demand **************************
            # HP load @ Household bus
            self.net.load.at[12, 'p_mw'] = heat_demand_2026_jul['th_load_38_household'][i]
            # P2G at bus = 12
            self.net.load.at[13, 'p_mw'] = self.p2g_input_mw

            # print(self.net.load)

            # *************************** PV ***************************
            # print(self.x[14])
            # print(self.x_pv_mw[0])
            self.net.sgen.at[0, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[0]  # Assuming PV 1 is at index 0
            self.net.sgen.at[1, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[1]
            self.net.sgen.at[2, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[2]
            self.net.sgen.at[3, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[3]
            self.net.sgen.at[4, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[4]
            self.net.sgen.at[5, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[5]
            self.net.sgen.at[6, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[6]
            self.net.sgen.at[7, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[7]
            self.net.sgen.at[8, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[8]
            self.net.sgen.at[9, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[9]
            self.net.sgen.at[10, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[10]
            self.net.sgen.at[11, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[11]
            self.net.sgen.at[12, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[12]
            self.net.sgen.at[13, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[13]

            # *************************** WT ***************************
            # print("wt_time_series =", wind_time_series['wind_normalized_jan'][i])
            self.net.sgen.at[14, 'p_mw'] = wind_time_series['wind_normalized_jul'][i] * self.x_wt_mw
            # Assuming WT 1 is at index 14

            # *************************** CHP ***************************
            self.net.sgen.at[15, 'p_mw'] = self.chp_p_mw
            # print(self.net.sgen)

            # ***************************** BESS *******************************************
            # print("bess_mw", bess_mw)
            # print("tot_sgen =", self.net.sgen['p_mw'].sum())
            # print("tot_demand_e =", self.net.load['p_mw'].sum())
            # print()
            bess = BESS(net=self.net, sgen_mwh=self.net.sgen['p_mw'].sum(),
                        demand_e_mwh=self.net.load['p_mw'].sum(),
                        bess_mw=bess_mw,
                        bess_mwh=bess_mwh,
                        # bess_soc=bess_soc,
                        # current_energy=bess_current_energy,
                        # bess_max_energy=bess_max_energy,
                        # bess_min_energy=bess_min_energy,
                        bess_update_mwh=bess_update_mwh)
            res_bess_mw = bess.bms_update()[0]
            res_bess_mwh = bess.bms_update()[1]
            res_bess_power_loss_mwh = bess.bms_update()[2]
            res_bess_power_deficit_mwh = bess.bms_update()[3]

            self.net.storage.at[0, 'p_mw'] = res_bess_mw
            # bess_mw_update += res_bess_mwh
            bess_update_mwh = res_bess_mwh
            # print("bess_mw_update =", bess_mw_update)
            # print(self.net.storage)

            pp.runpp(self.net)

            result = {
                # 'time_step': i,
                'demand_mw': self.net.res_load.p_mw.sum(),  # summing the total load at each hour (t)
                'line_loss_mw': self.net.res_line.pl_mw.values[0],
                'gas_gen_mw': self.net.res_gen.p_mw.sum(),
                'pv_wt_chp_mw': self.net.res_sgen.p_mw.sum(),  # summing the total PV gen at each hour (t)
                'bess_mw': self.net.res_storage.p_mw.sum(),
                'ext_grid_mw': self.net.res_ext_grid.p_mw.values[0],
                'bess_mwh': res_bess_mwh
                # 'res_bess_power_loss_mwh': res_bess_power_loss_mwh,
                # 'res_bess_power_deficit_mwh': res_bess_power_deficit_mwh
            }

            for bus_idx in self.net.bus.index:
                result[f'bus_{int(bus_idx)}_voltage_pu'] = self.net.res_bus.vm_pu[bus_idx]

            results = results.append(result, ignore_index=True)

        return results

    # =================================================== 2027 Jan ===================================================
    # NOTE: Data input to change: 1. e_demand (Jan/July), 2. PV irradiance & WIND profile  3. heat_demand (Jan/July)
    def power_flow_2027_jan(self):

        results = pd.DataFrame()

        # -------------------------- Create loads on the fixed bus bars with 0 p_mw --------------------------
        pp.create_load(self.net, bus=1, p_mw=0, name="Chem Ind Load 1")
        pp.create_load(self.net, bus=12, p_mw=0, name="Chem Ind Load 2")
        pp.create_load(self.net, bus=2, p_mw=0, name="Medium Ind Load 1")
        pp.create_load(self.net, bus=13, p_mw=0, name="Small Ind Load 1")
        pp.create_load(self.net, bus=14, p_mw=0, name="Small Ind Load 2")
        # Commercial loads
        pp.create_load(self.net, bus=3, p_mw=0, name="Commercial load 1")
        pp.create_load(self.net, bus=4, p_mw=0, name="Commercial load 2")
        pp.create_load(self.net, bus=5, p_mw=0, name="Commercial load 3")
        pp.create_load(self.net, bus=9, p_mw=0, name="Commercial load 4")
        pp.create_load(self.net, bus=10, p_mw=0, name="Commercial load 5")
        pp.create_load(self.net, bus=11, p_mw=0, name="Commercial load 6")
        # Household load
        pp.create_load(self.net, bus=6, p_mw=0, name="Household load")  # 38 households

        # --------------------------Special loads --------------------------
        # HP load at household bus
        pp.create_load(self.net, bus=6, p_mw=0, name="HP load for Households")
        # P2G load at bus = 12
        pp.create_load(self.net, bus=12, p_mw=0, name="P2G load")

        # -------------------------- Create Gas gen at bus 12 --------------------------
        pp.create_gen(self.net, bus=12, p_mw=self.x_gen_bus_12_mw, vm_pu=1.0,
                      name="Gas Power bus 37")  # Peak load = 29.3 MW
        # Gas gen at bus 1
        pp.create_gen(self.net, bus=1, p_mw=self.x_gen_bus_1_mw, vm_pu=1.0,
                      name="Gas Power bus 37")  # Peak load = 20.8 MW
        # print(self.net.gen)

        # --------------------------PV, WT & CHP --------------------------
        # Create sgens (PV+WT) at each of the specified x_bus-bar with initial p_mw = 0
        x_pv_bus = self.x_pv_bus
        # PV
        for bus in x_pv_bus:
            pp.create_sgen(self.net, bus=bus, p_mw=0, q_mvar=0, name="PV")
        # WT
        x_wt_bus = self.x_wt_bus
        for bus in x_wt_bus:
            pp.create_sgen(self.net, bus=bus, p_mw=0, q_mvar=0, name="WT")
        # CHP
        x_chp_bus = self.chp_bus
        pp.create_sgen(self.net, bus=x_chp_bus, p_mw=0, q_mvar=0, name="CHP")

        # ----------------------------------------- Create BESS -----------------------------------------
        pp.create_storage(self.net, bus=self.bess_bus, p_mw=0, max_e_mwh=self.bess_p_mw * 12 * 0.9,
                          soc_percent=0.5, name="BESS")
        # print(self.net.storage)

        bess_mw = self.bess_p_mw  # this is already for 1 hour = MWh for each battery
        bess_mwh = self.bess_p_mw * 1  # C rate = 1 = max capacity charge and discharge in 1 hr.
        bess_soc = 0.1

        bess_init_mwh = bess_mwh * bess_soc
        bess_update_mwh = bess_init_mwh
        # print("current_bess_energy", bess_update_mwh)

        # Note Year 2027 Jan: change e_demand, irradiance, WIND profile, heat_demand:
        for i, ((load_idx, load_row), (irradiance_idx, irradiance_row)) in \
                enumerate(zip(e_demand_2027_jan.iterrows(),
                              df_irradiance_jan.iterrows())):
            # print("i_jan =", i)
            # print("eload_jan =", load_row['LG 07'])
            # print("PV_irr_jan =", irradiance_row)
            # print("w_speed_jan =", wind_time_series['wind_normalized_jan'][i])
            # # print("th_demand_jan", heat_demand_jan['th_load_38_household'][i])

            # ********************* Update the load values at the specified buses *********************
            # Ind, comm and res loads
            self.net.load.at[0, 'p_mw'] = load_row['LG 01']  # Assuming Chem Industry Load 1 is at index 0
            self.net.load.at[1, 'p_mw'] = load_row[
                'LG 07']  # Peak load = 29.3 MW - Chem Industry Load 2 is at index 1
            self.net.load.at[2, 'p_mw'] = load_row['LG 03']  # Medium industry
            self.net.load.at[3, 'p_mw'] = load_row['small_ind_load_1']
            self.net.load.at[4, 'p_mw'] = load_row['small_ind_load_2']
            # Commercial loads
            self.net.load.at[5, 'p_mw'] = load_row['load_bus3']  # load at bus3
            self.net.load.at[6, 'p_mw'] = load_row['load_bus4']
            self.net.load.at[7, 'p_mw'] = load_row['load_bus5']
            self.net.load.at[8, 'p_mw'] = load_row['load_bus9']
            self.net.load.at[9, 'p_mw'] = load_row['load_bus10']
            self.net.load.at[10, 'p_mw'] = load_row['load_bus11']
            # Household load
            self.net.load.at[11, 'p_mw'] = load_row['load_bus6']  # *10 around 38*10 households

            # ************************ Special loads & heat demand **************************
            # !@#$%^&*(------------------ Change Heat Demand ------------------!@#$%^&*(
            # HP load @ Household bus
            self.net.load.at[12, 'p_mw'] = heat_demand_2027_jan['th_load_38_household'][i]
            # P2G at bus = 12
            self.net.load.at[13, 'p_mw'] = self.p2g_input_mw

            # print(self.net.load)

            # *************************** PV ***************************
            # print(self.x[14])
            # print(self.x_pv_mw[0])
            self.net.sgen.at[0, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[0]  # Assuming PV 1 is at index 0
            self.net.sgen.at[1, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[1]
            self.net.sgen.at[2, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[2]
            self.net.sgen.at[3, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[3]
            self.net.sgen.at[4, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[4]
            self.net.sgen.at[5, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[5]
            self.net.sgen.at[6, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[6]
            self.net.sgen.at[7, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[7]
            self.net.sgen.at[8, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[8]
            self.net.sgen.at[9, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[9]
            self.net.sgen.at[10, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[10]
            self.net.sgen.at[11, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[11]
            self.net.sgen.at[12, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[12]
            self.net.sgen.at[13, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[13]

            # *************************** WT ***************************
            # print("wt_time_series =", wind_time_series['wind_normalized_jan'][i])
            self.net.sgen.at[14, 'p_mw'] = wind_time_series['wind_normalized_jan'][i] * self.x_wt_mw
            # Assuming WT 1 is at index 14

            # *************************** CHP ***************************
            self.net.sgen.at[15, 'p_mw'] = self.chp_p_mw
            # print(self.net.sgen)

            # ***************************** BESS *******************************************
            # print("bess_mw", bess_mw)
            # print("tot_sgen =", self.net.sgen['p_mw'].sum())
            # print("tot_demand_e =", self.net.load['p_mw'].sum())
            # print()
            bess = BESS(net=self.net, sgen_mwh=self.net.sgen['p_mw'].sum(),
                        demand_e_mwh=self.net.load['p_mw'].sum(),
                        bess_mw=bess_mw,
                        bess_mwh=bess_mwh,
                        # bess_soc=bess_soc,
                        # current_energy=bess_current_energy,
                        # bess_max_energy=bess_max_energy,
                        # bess_min_energy=bess_min_energy,
                        bess_update_mwh=bess_update_mwh)
            res_bess_mw = bess.bms_update()[0]
            res_bess_mwh = bess.bms_update()[1]
            res_bess_power_loss_mwh = bess.bms_update()[2]
            res_bess_power_deficit_mwh = bess.bms_update()[3]

            self.net.storage.at[0, 'p_mw'] = res_bess_mw
            # bess_mw_update += res_bess_mwh
            bess_update_mwh = res_bess_mwh
            # print("bess_mw_update =", bess_mw_update)
            # print(self.net.storage)

            pp.runpp(self.net)

            result = {
                # 'time_step': i,
                'demand_mw': self.net.res_load.p_mw.sum(),  # summing the total load at each hour (t)
                'line_loss_mw': self.net.res_line.pl_mw.values[0],
                'gas_gen_mw': self.net.res_gen.p_mw.sum(),
                'pv_wt_chp_mw': self.net.res_sgen.p_mw.sum(),  # summing the total PV gen at each hour (t)
                'bess_mw': self.net.res_storage.p_mw.sum(),
                'ext_grid_mw': self.net.res_ext_grid.p_mw.values[0],
                'bess_mwh': res_bess_mwh
                # 'res_bess_power_loss_mwh': res_bess_power_loss_mwh,
                # 'res_bess_power_deficit_mwh': res_bess_power_deficit_mwh
            }

            for bus_idx in self.net.bus.index:
                result[f'bus_{int(bus_idx)}_voltage_pu'] = self.net.res_bus.vm_pu[bus_idx]

            results = results.append(result, ignore_index=True)
        # print(results)
        return results

    # ---------------------------------------------- 2027 July ----------------------------------------------
    # NOTE: Data input to change: 1. e_demand (Jan/July), 2. PV irradiance & WIND profile  3. heat_demand (Jan/July)
    def power_flow_2027_jul(self):

        results = pd.DataFrame()

        # -------------------------- Create loads on the fixed bus bars with 0 p_mw --------------------------
        pp.create_load(self.net, bus=1, p_mw=0, name="Chem Ind Load 1")
        pp.create_load(self.net, bus=12, p_mw=0, name="Chem Ind Load 2")
        pp.create_load(self.net, bus=2, p_mw=0, name="Medium Ind Load 1")
        pp.create_load(self.net, bus=13, p_mw=0, name="Small Ind Load 1")
        pp.create_load(self.net, bus=14, p_mw=0, name="Small Ind Load 2")
        # Commercial loads
        pp.create_load(self.net, bus=3, p_mw=0, name="Commercial load 1")
        pp.create_load(self.net, bus=4, p_mw=0, name="Commercial load 2")
        pp.create_load(self.net, bus=5, p_mw=0, name="Commercial load 3")
        pp.create_load(self.net, bus=9, p_mw=0, name="Commercial load 4")
        pp.create_load(self.net, bus=10, p_mw=0, name="Commercial load 5")
        pp.create_load(self.net, bus=11, p_mw=0, name="Commercial load 6")
        # Household load
        pp.create_load(self.net, bus=6, p_mw=0, name="Household load")  # 38 households

        # -------------------------- Special loads --------------------------
        # HP load at household bus
        pp.create_load(self.net, bus=6, p_mw=0, name="HP load for Households")
        # P2G load at bus = 12
        pp.create_load(self.net, bus=12, p_mw=0, name="P2G load")

        # -------------------------- Create Gas gen at bus 12 --------------------------
        pp.create_gen(self.net, bus=12, p_mw=self.x_gen_bus_12_mw, vm_pu=1.0,
                      name="Gas Power bus 37")  # Peak load = 29.3 MW
        # Gas gen at bus 1
        pp.create_gen(self.net, bus=1, p_mw=self.x_gen_bus_1_mw, vm_pu=1.0,
                      name="Gas Power bus 37")  # Peak load = 20.8 MW
        # print(self.net.gen)

        # -------------------------- PV, WT & CHP --------------------------
        # Create sgens (PV+WT) at each of the specified x_bus-bar with initial p_mw = 0
        x_pv_bus = self.x_pv_bus
        # PV
        for bus in x_pv_bus:
            pp.create_sgen(self.net, bus=bus, p_mw=0, q_mvar=0, name="PV")
        # WT
        x_wt_bus = self.x_wt_bus
        for bus in x_wt_bus:
            pp.create_sgen(self.net, bus=bus, p_mw=0, q_mvar=0, name="WT")
        # CHP
        x_chp_bus = self.chp_bus
        pp.create_sgen(self.net, bus=x_chp_bus, p_mw=0, q_mvar=0, name="CHP")

        # ----------------------------------------- Create BESS -----------------------------------------
        pp.create_storage(self.net, bus=self.bess_bus, p_mw=0, max_e_mwh=self.bess_p_mw * 12 * 0.9,
                          soc_percent=0.5, name="BESS")
        # print(self.net.storage)

        bess_mw = self.bess_p_mw  # this is already for 1 hour = MWh for each battery
        bess_mwh = self.bess_p_mw * 1  # C rate = 1 = max capacity charge and discharge in 1 hr.
        bess_soc = 0.1

        bess_init_mwh = bess_mwh * bess_soc
        bess_update_mwh = bess_init_mwh
        # print("current_bess_energy", bess_update_mwh)

        # Note Year ------- 2027 Jul ------- : change e_demand, irradiance, heat_demand & WIND profile:
        for i, ((load_idx, load_row), (irradiance_idx, irradiance_row)) in \
                enumerate(zip(e_demand_2027_jul.iterrows(),
                              df_irradiance_jul.iterrows())):
            # print("i_jan =", i)
            # print("eload_jan =", load_row['LG 07'])
            # print("PV_irr_jan =", irradiance_row)
            # print("w_speed_jan =", wind_time_series['wind_normalized_jan'][i])
            # # print("th_demand_jan", heat_demand_jan['th_load_38_household'][i])

            # ********************* Update the load values at the specified buses *********************
            # Ind, comm and res loads
            self.net.load.at[0, 'p_mw'] = load_row['LG 01']  # Assuming Chem Industry Load 1 is at index 0
            self.net.load.at[1, 'p_mw'] = load_row[
                'LG 07']  # Peak load = 29.3 MW - Chem Industry Load 2 is at index 1
            self.net.load.at[2, 'p_mw'] = load_row['LG 03']  # Medium industry
            self.net.load.at[3, 'p_mw'] = load_row['small_ind_load_1']
            self.net.load.at[4, 'p_mw'] = load_row['small_ind_load_2']
            # Commercial loads
            self.net.load.at[5, 'p_mw'] = load_row['load_bus3']  # load at bus3
            self.net.load.at[6, 'p_mw'] = load_row['load_bus4']
            self.net.load.at[7, 'p_mw'] = load_row['load_bus5']
            self.net.load.at[8, 'p_mw'] = load_row['load_bus9']
            self.net.load.at[9, 'p_mw'] = load_row['load_bus10']
            self.net.load.at[10, 'p_mw'] = load_row['load_bus11']
            # Household load
            self.net.load.at[11, 'p_mw'] = load_row['load_bus6']  # *10 around 38*10 households

            # ************************ Special loads & heat demand **************************
            # !@#$%^&*(------------------ Change Heat Demand ------------------!@#$%^&*(
            # HP load @ Household bus
            self.net.load.at[12, 'p_mw'] = heat_demand_2027_jul['th_load_38_household'][i]
            # P2G at bus = 12
            self.net.load.at[13, 'p_mw'] = self.p2g_input_mw

            # print(self.net.load)

            # *************************** PV ***************************
            # print(self.x[14])
            # print(self.x_pv_mw[0])
            self.net.sgen.at[0, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[0]  # Assuming PV 1 is at index 0
            self.net.sgen.at[1, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[1]
            self.net.sgen.at[2, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[2]
            self.net.sgen.at[3, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[3]
            self.net.sgen.at[4, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[4]
            self.net.sgen.at[5, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[5]
            self.net.sgen.at[6, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[6]
            self.net.sgen.at[7, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[7]
            self.net.sgen.at[8, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[8]
            self.net.sgen.at[9, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[9]
            self.net.sgen.at[10, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[10]
            self.net.sgen.at[11, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[11]
            self.net.sgen.at[12, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[12]
            self.net.sgen.at[13, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[13]

            # *************************** WT ***************************
            # print("wt_time_series =", wind_time_series['wind_normalized_jan'][i])
            self.net.sgen.at[14, 'p_mw'] = wind_time_series['wind_normalized_jul'][i] * self.x_wt_mw
            # Assuming WT 1 is at index 14

            # *************************** CHP ***************************
            self.net.sgen.at[15, 'p_mw'] = self.chp_p_mw
            # print(self.net.sgen)

            # ***************************** BESS *******************************************
            # print("bess_mw", bess_mw)
            # print("tot_sgen =", self.net.sgen['p_mw'].sum())
            # print("tot_demand_e =", self.net.load['p_mw'].sum())
            # print()
            bess = BESS(net=self.net, sgen_mwh=self.net.sgen['p_mw'].sum(),
                        demand_e_mwh=self.net.load['p_mw'].sum(),
                        bess_mw=bess_mw,
                        bess_mwh=bess_mwh,
                        # bess_soc=bess_soc,
                        # current_energy=bess_current_energy,
                        # bess_max_energy=bess_max_energy,
                        # bess_min_energy=bess_min_energy,
                        bess_update_mwh=bess_update_mwh)
            res_bess_mw = bess.bms_update()[0]
            res_bess_mwh = bess.bms_update()[1]
            res_bess_power_loss_mwh = bess.bms_update()[2]
            res_bess_power_deficit_mwh = bess.bms_update()[3]

            self.net.storage.at[0, 'p_mw'] = res_bess_mw
            # bess_mw_update += res_bess_mwh
            bess_update_mwh = res_bess_mwh
            # print("bess_mw_update =", bess_mw_update)
            # print(self.net.storage)

            pp.runpp(self.net)

            result = {
                # 'time_step': i,
                'demand_mw': self.net.res_load.p_mw.sum(),  # summing the total load at each hour (t)
                'line_loss_mw': self.net.res_line.pl_mw.values[0],
                'gas_gen_mw': self.net.res_gen.p_mw.sum(),
                'pv_wt_chp_mw': self.net.res_sgen.p_mw.sum(),  # summing the total PV gen at each hour (t)
                'bess_mw': self.net.res_storage.p_mw.sum(),
                'ext_grid_mw': self.net.res_ext_grid.p_mw.values[0],
                'bess_mwh': res_bess_mwh
                # 'res_bess_power_loss_mwh': res_bess_power_loss_mwh,
                # 'res_bess_power_deficit_mwh': res_bess_power_deficit_mwh
            }

            for bus_idx in self.net.bus.index:
                result[f'bus_{int(bus_idx)}_voltage_pu'] = self.net.res_bus.vm_pu[bus_idx]

            results = results.append(result, ignore_index=True)

        return results

    # =================================================== 2028 Jan ===================================================
    # NOTE: Data input to change: 1. e_demand (Jan/July), 2. PV irradiance & WIND profile  3. heat_demand (Jan/July)
    def power_flow_2028_jan(self):

        results = pd.DataFrame()

        # -------------------------- Create loads on the fixed bus bars with 0 p_mw --------------------------
        pp.create_load(self.net, bus=1, p_mw=0, name="Chem Ind Load 1")
        pp.create_load(self.net, bus=12, p_mw=0, name="Chem Ind Load 2")
        pp.create_load(self.net, bus=2, p_mw=0, name="Medium Ind Load 1")
        pp.create_load(self.net, bus=13, p_mw=0, name="Small Ind Load 1")
        pp.create_load(self.net, bus=14, p_mw=0, name="Small Ind Load 2")
        # Commercial loads
        pp.create_load(self.net, bus=3, p_mw=0, name="Commercial load 1")
        pp.create_load(self.net, bus=4, p_mw=0, name="Commercial load 2")
        pp.create_load(self.net, bus=5, p_mw=0, name="Commercial load 3")
        pp.create_load(self.net, bus=9, p_mw=0, name="Commercial load 4")
        pp.create_load(self.net, bus=10, p_mw=0, name="Commercial load 5")
        pp.create_load(self.net, bus=11, p_mw=0, name="Commercial load 6")
        # Household load
        pp.create_load(self.net, bus=6, p_mw=0, name="Household load")  # 38 households

        # --------------------------Special loads --------------------------
        # HP load at household bus
        pp.create_load(self.net, bus=6, p_mw=0, name="HP load for Households")
        # P2G load at bus = 12
        pp.create_load(self.net, bus=12, p_mw=0, name="P2G load")

        # -------------------------- Create Gas gen at bus 12 --------------------------
        pp.create_gen(self.net, bus=12, p_mw=self.x_gen_bus_12_mw, vm_pu=1.0,
                      name="Gas Power bus 37")  # Peak load = 29.3 MW
        # Gas gen at bus 1
        pp.create_gen(self.net, bus=1, p_mw=self.x_gen_bus_1_mw, vm_pu=1.0,
                      name="Gas Power bus 37")  # Peak load = 20.8 MW
        # print(self.net.gen)

        # --------------------------PV, WT & CHP --------------------------
        # Create sgens (PV+WT) at each of the specified x_bus-bar with initial p_mw = 0
        x_pv_bus = self.x_pv_bus
        # PV
        for bus in x_pv_bus:
            pp.create_sgen(self.net, bus=bus, p_mw=0, q_mvar=0, name="PV")
        # WT
        x_wt_bus = self.x_wt_bus
        for bus in x_wt_bus:
            pp.create_sgen(self.net, bus=bus, p_mw=0, q_mvar=0, name="WT")
        # CHP
        x_chp_bus = self.chp_bus
        pp.create_sgen(self.net, bus=x_chp_bus, p_mw=0, q_mvar=0, name="CHP")

        # ----------------------------------------- Create BESS -----------------------------------------
        pp.create_storage(self.net, bus=self.bess_bus, p_mw=0, max_e_mwh=self.bess_p_mw * 12 * 0.9,
                          soc_percent=0.5, name="BESS")
        # print(self.net.storage)

        bess_mw = self.bess_p_mw  # this is already for 1 hour = MWh for each battery
        bess_mwh = self.bess_p_mw * 1  # C rate = 1 = max capacity charge and discharge in 1 hr.
        bess_soc = 0.1

        bess_init_mwh = bess_mwh * bess_soc
        bess_update_mwh = bess_init_mwh
        # print("current_bess_energy", bess_update_mwh)

        # <<<<< ----------- Note: Year 2028 Jan: change e_demand, irradiance, WIND profile, heat_demand: ------>>>>>>>
        for i, ((load_idx, load_row), (irradiance_idx, irradiance_row)) in \
                enumerate(zip(e_demand_2028_jan.iterrows(),
                              df_irradiance_jan.iterrows())):
            # print("i_jan =", i)
            # print("eload_jan =", load_row['LG 07'])
            # print("PV_irr_jan =", irradiance_row)
            # print("w_speed_jan =", wind_time_series['wind_normalized_jan'][i])
            # # print("th_demand_jan", heat_demand_jan['th_load_38_household'][i])

            # ********************* Update the load values at the specified buses *********************
            # Ind, comm and res loads
            self.net.load.at[0, 'p_mw'] = load_row['LG 01']  # Assuming Chem Industry Load 1 is at index 0
            self.net.load.at[1, 'p_mw'] = load_row['LG 07']  # Peak load = 29.3 MW - Chem Industry Load 2 is at index 1
            self.net.load.at[2, 'p_mw'] = load_row['LG 03']  # Medium industry
            self.net.load.at[3, 'p_mw'] = load_row['small_ind_load_1']
            self.net.load.at[4, 'p_mw'] = load_row['small_ind_load_2']
            # Commercial loads
            self.net.load.at[5, 'p_mw'] = load_row['load_bus3']  # load at bus3
            self.net.load.at[6, 'p_mw'] = load_row['load_bus4']
            self.net.load.at[7, 'p_mw'] = load_row['load_bus5']
            self.net.load.at[8, 'p_mw'] = load_row['load_bus9']
            self.net.load.at[9, 'p_mw'] = load_row['load_bus10']
            self.net.load.at[10, 'p_mw'] = load_row['load_bus11']
            # Household load
            self.net.load.at[11, 'p_mw'] = load_row['load_bus6']  # *10 around 38*10 households

            # ************************ Special loads & heat demand **************************
            # <<<<< ----------------------------- Change Heat Demand ------------------------>>>>>>>
            # HP load @ Household bus
            self.net.load.at[12, 'p_mw'] = heat_demand_2028_jan['th_load_38_household'][i]
            # P2G at bus = 12
            self.net.load.at[13, 'p_mw'] = self.p2g_input_mw

            # print(self.net.load)

            # *************************** PV ***************************
            # print(self.x[14])
            # print(self.x_pv_mw[0])
            self.net.sgen.at[0, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[0]  # Assuming PV 1 is at index 0
            self.net.sgen.at[1, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[1]
            self.net.sgen.at[2, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[2]
            self.net.sgen.at[3, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[3]
            self.net.sgen.at[4, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[4]
            self.net.sgen.at[5, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[5]
            self.net.sgen.at[6, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[6]
            self.net.sgen.at[7, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[7]
            self.net.sgen.at[8, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[8]
            self.net.sgen.at[9, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[9]
            self.net.sgen.at[10, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[10]
            self.net.sgen.at[11, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[11]
            self.net.sgen.at[12, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[12]
            self.net.sgen.at[13, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[13]

            # *************************** WT ***************************
            # print("wt_time_series =", wind_time_series['wind_normalized_jan'][i])
            self.net.sgen.at[14, 'p_mw'] = wind_time_series['wind_normalized_jan'][i] * self.x_wt_mw
            # Assuming WT 1 is at index 14

            # *************************** CHP ***************************
            self.net.sgen.at[15, 'p_mw'] = self.chp_p_mw
            # print(self.net.sgen)

            # ***************************** BESS *******************************************
            # print("bess_mw", bess_mw)
            # print("tot_sgen =", self.net.sgen['p_mw'].sum())
            # print("tot_demand_e =", self.net.load['p_mw'].sum())
            # print()
            bess = BESS(net=self.net, sgen_mwh=self.net.sgen['p_mw'].sum(),
                        demand_e_mwh=self.net.load['p_mw'].sum(),
                        bess_mw=bess_mw,
                        bess_mwh=bess_mwh,
                        # bess_soc=bess_soc,
                        # current_energy=bess_current_energy,
                        # bess_max_energy=bess_max_energy,
                        # bess_min_energy=bess_min_energy,
                        bess_update_mwh=bess_update_mwh)
            res_bess_mw = bess.bms_update()[0]
            res_bess_mwh = bess.bms_update()[1]
            res_bess_power_loss_mwh = bess.bms_update()[2]
            res_bess_power_deficit_mwh = bess.bms_update()[3]

            self.net.storage.at[0, 'p_mw'] = res_bess_mw
            # bess_mw_update += res_bess_mwh
            bess_update_mwh = res_bess_mwh
            # print("bess_mw_update =", bess_mw_update)
            # print(self.net.storage)

            pp.runpp(self.net)

            result = {
                # 'time_step': i,
                'demand_mw': self.net.res_load.p_mw.sum(),  # summing the total load at each hour (t)
                'line_loss_mw': self.net.res_line.pl_mw.values[0],
                'gas_gen_mw': self.net.res_gen.p_mw.sum(),
                'pv_wt_chp_mw': self.net.res_sgen.p_mw.sum(),  # summing the total PV gen at each hour (t)
                'bess_mw': self.net.res_storage.p_mw.sum(),
                'ext_grid_mw': self.net.res_ext_grid.p_mw.values[0],
                'bess_mwh': res_bess_mwh
                # 'res_bess_power_loss_mwh': res_bess_power_loss_mwh,
                # 'res_bess_power_deficit_mwh': res_bess_power_deficit_mwh
            }

            for bus_idx in self.net.bus.index:
                result[f'bus_{int(bus_idx)}_voltage_pu'] = self.net.res_bus.vm_pu[bus_idx]

            results = results.append(result, ignore_index=True)
        # print(results)
        return results

    # ---------------------------------------------- 2028 July ----------------------------------------------
    # NOTE: Data input to change: 1. e_demand (Jan/July), 2. PV irradiance & WIND profile  3. heat_demand (Jan/July)
    def power_flow_2028_jul(self):

        results = pd.DataFrame()

        # -------------------------- Create loads on the fixed bus bars with 0 p_mw --------------------------
        pp.create_load(self.net, bus=1, p_mw=0, name="Chem Ind Load 1")
        pp.create_load(self.net, bus=12, p_mw=0, name="Chem Ind Load 2")
        pp.create_load(self.net, bus=2, p_mw=0, name="Medium Ind Load 1")
        pp.create_load(self.net, bus=13, p_mw=0, name="Small Ind Load 1")
        pp.create_load(self.net, bus=14, p_mw=0, name="Small Ind Load 2")
        # Commercial loads
        pp.create_load(self.net, bus=3, p_mw=0, name="Commercial load 1")
        pp.create_load(self.net, bus=4, p_mw=0, name="Commercial load 2")
        pp.create_load(self.net, bus=5, p_mw=0, name="Commercial load 3")
        pp.create_load(self.net, bus=9, p_mw=0, name="Commercial load 4")
        pp.create_load(self.net, bus=10, p_mw=0, name="Commercial load 5")
        pp.create_load(self.net, bus=11, p_mw=0, name="Commercial load 6")
        # Household load
        pp.create_load(self.net, bus=6, p_mw=0, name="Household load")  # 38 households

        # -------------------------- Special loads --------------------------
        # HP load at household bus
        pp.create_load(self.net, bus=6, p_mw=0, name="HP load for Households")
        # P2G load at bus = 12
        pp.create_load(self.net, bus=12, p_mw=0, name="P2G load")

        # -------------------------- Create Gas gen at bus 12 --------------------------
        pp.create_gen(self.net, bus=12, p_mw=self.x_gen_bus_12_mw, vm_pu=1.0,
                      name="Gas Power bus 37")  # Peak load = 29.3 MW
        # Gas gen at bus 1
        pp.create_gen(self.net, bus=1, p_mw=self.x_gen_bus_1_mw, vm_pu=1.0,
                      name="Gas Power bus 37")  # Peak load = 20.8 MW
        # print(self.net.gen)

        # -------------------------- PV, WT & CHP --------------------------
        # Create sgens (PV+WT) at each of the specified x_bus-bar with initial p_mw = 0
        x_pv_bus = self.x_pv_bus
        # PV
        for bus in x_pv_bus:
            pp.create_sgen(self.net, bus=bus, p_mw=0, q_mvar=0, name="PV")
        # WT
        x_wt_bus = self.x_wt_bus
        for bus in x_wt_bus:
            pp.create_sgen(self.net, bus=bus, p_mw=0, q_mvar=0, name="WT")
        # CHP
        x_chp_bus = self.chp_bus
        pp.create_sgen(self.net, bus=x_chp_bus, p_mw=0, q_mvar=0, name="CHP")

        # ----------------------------------------- Create BESS -----------------------------------------
        pp.create_storage(self.net, bus=self.bess_bus, p_mw=0, max_e_mwh=self.bess_p_mw * 12 * 0.9,
                          soc_percent=0.5, name="BESS")
        # print(self.net.storage)

        bess_mw = self.bess_p_mw  # this is already for 1 hour = MWh for each battery
        bess_mwh = self.bess_p_mw * 1  # C rate = 1 = max capacity charge and discharge in 1 hr.
        bess_soc = 0.1

        bess_init_mwh = bess_mwh * bess_soc
        bess_update_mwh = bess_init_mwh
        # print("current_bess_energy", bess_update_mwh)

        # <<<<<< ---- Note: Year 2028 Jul - change e_demand, irradiance, heat_demand & WIND profile: ----- >>>>>>
        for i, ((load_idx, load_row), (irradiance_idx, irradiance_row)) in \
                enumerate(zip(e_demand_2028_jul.iterrows(),
                              df_irradiance_jul.iterrows())):
            # print("i_jan =", i)
            # print("eload_jan =", load_row['LG 07'])
            # print("PV_irr_jan =", irradiance_row)
            # print("w_speed_jan =", wind_time_series['wind_normalized_jan'][i])
            # # print("th_demand_jan", heat_demand_jan['th_load_38_household'][i])

            # ********************* Update the load values at the specified buses *********************
            # Ind, comm and res loads
            self.net.load.at[0, 'p_mw'] = load_row['LG 01']  # Assuming Chem Industry Load 1 is at index 0
            self.net.load.at[1, 'p_mw'] = load_row[
                'LG 07']  # Peak load = 29.3 MW - Chem Industry Load 2 is at index 1
            self.net.load.at[2, 'p_mw'] = load_row['LG 03']  # Medium industry
            self.net.load.at[3, 'p_mw'] = load_row['small_ind_load_1']
            self.net.load.at[4, 'p_mw'] = load_row['small_ind_load_2']
            # Commercial loads
            self.net.load.at[5, 'p_mw'] = load_row['load_bus3']  # load at bus3
            self.net.load.at[6, 'p_mw'] = load_row['load_bus4']
            self.net.load.at[7, 'p_mw'] = load_row['load_bus5']
            self.net.load.at[8, 'p_mw'] = load_row['load_bus9']
            self.net.load.at[9, 'p_mw'] = load_row['load_bus10']
            self.net.load.at[10, 'p_mw'] = load_row['load_bus11']
            # Household load
            self.net.load.at[11, 'p_mw'] = load_row['load_bus6']  # *10 around 38*10 households

            # ************************ Special loads & heat demand **************************
            # <<<<<<<<<<<<<< ------------------ Change Heat Demand ------------------ >>>>>>>>>>>>>>>>>>>>
            # HP load @ Household bus
            self.net.load.at[12, 'p_mw'] = heat_demand_2028_jul['th_load_38_household'][i]
            # P2G at bus = 12
            self.net.load.at[13, 'p_mw'] = self.p2g_input_mw

            # print(self.net.load)

            # *************************** PV ***************************
            # print(self.x[14])
            # print(self.x_pv_mw[0])
            self.net.sgen.at[0, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[0]  # Assuming PV 1 is at index 0
            self.net.sgen.at[1, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[1]
            self.net.sgen.at[2, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[2]
            self.net.sgen.at[3, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[3]
            self.net.sgen.at[4, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[4]
            self.net.sgen.at[5, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[5]
            self.net.sgen.at[6, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[6]
            self.net.sgen.at[7, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[7]
            self.net.sgen.at[8, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[8]
            self.net.sgen.at[9, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[9]
            self.net.sgen.at[10, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[10]
            self.net.sgen.at[11, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[11]
            self.net.sgen.at[12, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[12]
            self.net.sgen.at[13, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[13]

            # *************************** WT ***************************
            # print("wt_time_series =", wind_time_series['wind_normalized_jan'][i])
            self.net.sgen.at[14, 'p_mw'] = wind_time_series['wind_normalized_jul'][i] * self.x_wt_mw
            # Assuming WT 1 is at index 14

            # *************************** CHP ***************************
            self.net.sgen.at[15, 'p_mw'] = self.chp_p_mw
            # print(self.net.sgen)

            # ***************************** BESS *******************************************
            # print("bess_mw", bess_mw)
            # print("tot_sgen =", self.net.sgen['p_mw'].sum())
            # print("tot_demand_e =", self.net.load['p_mw'].sum())
            # print()
            bess = BESS(net=self.net, sgen_mwh=self.net.sgen['p_mw'].sum(),
                        demand_e_mwh=self.net.load['p_mw'].sum(),
                        bess_mw=bess_mw,
                        bess_mwh=bess_mwh,
                        # bess_soc=bess_soc,
                        # current_energy=bess_current_energy,
                        # bess_max_energy=bess_max_energy,
                        # bess_min_energy=bess_min_energy,
                        bess_update_mwh=bess_update_mwh)
            res_bess_mw = bess.bms_update()[0]
            res_bess_mwh = bess.bms_update()[1]
            res_bess_power_loss_mwh = bess.bms_update()[2]
            res_bess_power_deficit_mwh = bess.bms_update()[3]

            self.net.storage.at[0, 'p_mw'] = res_bess_mw
            # bess_mw_update += res_bess_mwh
            bess_update_mwh = res_bess_mwh
            # print("bess_mw_update =", bess_mw_update)
            # print(self.net.storage)

            pp.runpp(self.net)

            result = {
                # 'time_step': i,
                'demand_mw': self.net.res_load.p_mw.sum(),  # summing the total load at each hour (t)
                'line_loss_mw': self.net.res_line.pl_mw.values[0],
                'gas_gen_mw': self.net.res_gen.p_mw.sum(),
                'pv_wt_chp_mw': self.net.res_sgen.p_mw.sum(),  # summing the total PV gen at each hour (t)
                'bess_mw': self.net.res_storage.p_mw.sum(),
                'ext_grid_mw': self.net.res_ext_grid.p_mw.values[0],
                'bess_mwh': res_bess_mwh
                # 'res_bess_power_loss_mwh': res_bess_power_loss_mwh,
                # 'res_bess_power_deficit_mwh': res_bess_power_deficit_mwh
            }

            for bus_idx in self.net.bus.index:
                result[f'bus_{int(bus_idx)}_voltage_pu'] = self.net.res_bus.vm_pu[bus_idx]

            results = results.append(result, ignore_index=True)

        return results

    # =================================================== 2029 Jan ===================================================
    # NOTE: Data input to change: 1. e_demand (Jan/July), 2. PV irradiance & WIND profile  3. heat_demand (Jan/July)
    def power_flow_2029_jan(self):

        results = pd.DataFrame()

        # -------------------------- Create loads on the fixed bus bars with 0 p_mw --------------------------
        pp.create_load(self.net, bus=1, p_mw=0, name="Chem Ind Load 1")
        pp.create_load(self.net, bus=12, p_mw=0, name="Chem Ind Load 2")
        pp.create_load(self.net, bus=2, p_mw=0, name="Medium Ind Load 1")
        pp.create_load(self.net, bus=13, p_mw=0, name="Small Ind Load 1")
        pp.create_load(self.net, bus=14, p_mw=0, name="Small Ind Load 2")
        # Commercial loads
        pp.create_load(self.net, bus=3, p_mw=0, name="Commercial load 1")
        pp.create_load(self.net, bus=4, p_mw=0, name="Commercial load 2")
        pp.create_load(self.net, bus=5, p_mw=0, name="Commercial load 3")
        pp.create_load(self.net, bus=9, p_mw=0, name="Commercial load 4")
        pp.create_load(self.net, bus=10, p_mw=0, name="Commercial load 5")
        pp.create_load(self.net, bus=11, p_mw=0, name="Commercial load 6")
        # Household load
        pp.create_load(self.net, bus=6, p_mw=0, name="Household load")  # 38 households

        # --------------------------Special loads --------------------------
        # HP load at household bus
        pp.create_load(self.net, bus=6, p_mw=0, name="HP load for Households")
        # P2G load at bus = 12
        pp.create_load(self.net, bus=12, p_mw=0, name="P2G load")

        # -------------------------- Create Gas gen at bus 12 --------------------------
        pp.create_gen(self.net, bus=12, p_mw=self.x_gen_bus_12_mw, vm_pu=1.0,
                      name="Gas Power bus 37")  # Peak load = 29.3 MW
        # Gas gen at bus 1
        pp.create_gen(self.net, bus=1, p_mw=self.x_gen_bus_1_mw, vm_pu=1.0,
                      name="Gas Power bus 37")  # Peak load = 20.8 MW
        # print(self.net.gen)

        # --------------------------PV, WT & CHP --------------------------
        # Create sgens (PV+WT) at each of the specified x_bus-bar with initial p_mw = 0
        x_pv_bus = self.x_pv_bus
        # PV
        for bus in x_pv_bus:
            pp.create_sgen(self.net, bus=bus, p_mw=0, q_mvar=0, name="PV")
        # WT
        x_wt_bus = self.x_wt_bus
        for bus in x_wt_bus:
            pp.create_sgen(self.net, bus=bus, p_mw=0, q_mvar=0, name="WT")
        # CHP
        x_chp_bus = self.chp_bus
        pp.create_sgen(self.net, bus=x_chp_bus, p_mw=0, q_mvar=0, name="CHP")

        # ----------------------------------------- Create BESS -----------------------------------------
        pp.create_storage(self.net, bus=self.bess_bus, p_mw=0, max_e_mwh=self.bess_p_mw * 12 * 0.9,
                          soc_percent=0.5, name="BESS")
        # print(self.net.storage)

        bess_mw = self.bess_p_mw  # this is already for 1 hour = MWh for each battery
        bess_mwh = self.bess_p_mw * 1  # C rate = 1 = max capacity charge and discharge in 1 hr.
        bess_soc = 0.1

        bess_init_mwh = bess_mwh * bess_soc
        bess_update_mwh = bess_init_mwh
        # print("current_bess_energy", bess_update_mwh)

        # <<<<< ----------- Note: Year 2028 Jan: change e_demand, irradiance, WIND profile, heat_demand: ------>>>>>>>>>>
        for i, ((load_idx, load_row), (irradiance_idx, irradiance_row)) in \
                enumerate(zip(e_demand_2029_jan.iterrows(),
                              df_irradiance_jan.iterrows())):

            # ********************* Update the load values at the specified buses *********************
            # Ind, comm and res loads
            self.net.load.at[0, 'p_mw'] = load_row['LG 01']  # Assuming Chem Industry Load 1 is at index 0
            self.net.load.at[1, 'p_mw'] = load_row['LG 07']  # Peak load = 29.3 MW - Chem Industry Load 2 is at index 1
            self.net.load.at[2, 'p_mw'] = load_row['LG 03']  # Medium industry
            self.net.load.at[3, 'p_mw'] = load_row['small_ind_load_1']
            self.net.load.at[4, 'p_mw'] = load_row['small_ind_load_2']
            # Commercial loads
            self.net.load.at[5, 'p_mw'] = load_row['load_bus3']  # load at bus3
            self.net.load.at[6, 'p_mw'] = load_row['load_bus4']
            self.net.load.at[7, 'p_mw'] = load_row['load_bus5']
            self.net.load.at[8, 'p_mw'] = load_row['load_bus9']
            self.net.load.at[9, 'p_mw'] = load_row['load_bus10']
            self.net.load.at[10, 'p_mw'] = load_row['load_bus11']
            # Household load
            self.net.load.at[11, 'p_mw'] = load_row['load_bus6']  # *10 around 38*10 households

            # ************************ Special loads & heat demand **************************
            # <<<<< ----------------------------- Change Heat Demand ------------------------>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # HP load @ Household bus
            self.net.load.at[12, 'p_mw'] = heat_demand_2029_jan['th_load_38_household'][i]
            # P2G at bus = 12
            self.net.load.at[13, 'p_mw'] = self.p2g_input_mw

            # print(self.net.load)

            # *************************** PV ***************************
            # print(self.x_pv_mw[0])
            self.net.sgen.at[0, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[0]  # Assuming PV 1 is at index 0
            self.net.sgen.at[1, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[1]
            self.net.sgen.at[2, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[2]
            self.net.sgen.at[3, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[3]
            self.net.sgen.at[4, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[4]
            self.net.sgen.at[5, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[5]
            self.net.sgen.at[6, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[6]
            self.net.sgen.at[7, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[7]
            self.net.sgen.at[8, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[8]
            self.net.sgen.at[9, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[9]
            self.net.sgen.at[10, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[10]
            self.net.sgen.at[11, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[11]
            self.net.sgen.at[12, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[12]
            self.net.sgen.at[13, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[13]

            # *************************** WT ***************************
            # print("wt_time_series =", wind_time_series['wind_normalized_jan'][i])
            self.net.sgen.at[14, 'p_mw'] = wind_time_series['wind_normalized_jan'][i] * self.x_wt_mw
            # Assuming WT 1 is at index 14

            # *************************** CHP ***************************
            self.net.sgen.at[15, 'p_mw'] = self.chp_p_mw
            # print(self.net.sgen)

            # ***************************** BESS *******************************************
            # print("bess_mw", bess_mw)
            bess = BESS(net=self.net, sgen_mwh=self.net.sgen['p_mw'].sum(),
                        demand_e_mwh=self.net.load['p_mw'].sum(),
                        bess_mw=bess_mw,
                        bess_mwh=bess_mwh,
                        # bess_soc=bess_soc,
                        # current_energy=bess_current_energy,
                        # bess_max_energy=bess_max_energy,
                        # bess_min_energy=bess_min_energy,
                        bess_update_mwh=bess_update_mwh)
            res_bess_mw = bess.bms_update()[0]
            res_bess_mwh = bess.bms_update()[1]
            res_bess_power_loss_mwh = bess.bms_update()[2]
            res_bess_power_deficit_mwh = bess.bms_update()[3]

            self.net.storage.at[0, 'p_mw'] = res_bess_mw
            # bess_mw_update += res_bess_mwh
            bess_update_mwh = res_bess_mwh
            # print("bess_mw_update =", bess_mw_update)
            # print(self.net.storage)

            pp.runpp(self.net)

            result = {
                # 'time_step': i,
                'demand_mw': self.net.res_load.p_mw.sum(),  # summing the total load at each hour (t)
                'line_loss_mw': self.net.res_line.pl_mw.values[0],
                'gas_gen_mw': self.net.res_gen.p_mw.sum(),
                'pv_wt_chp_mw': self.net.res_sgen.p_mw.sum(),  # summing the total PV gen at each hour (t)
                'bess_mw': self.net.res_storage.p_mw.sum(),
                'ext_grid_mw': self.net.res_ext_grid.p_mw.values[0],
                'bess_mwh': res_bess_mwh
                # 'res_bess_power_loss_mwh': res_bess_power_loss_mwh,
                # 'res_bess_power_deficit_mwh': res_bess_power_deficit_mwh
            }

            for bus_idx in self.net.bus.index:
                result[f'bus_{int(bus_idx)}_voltage_pu'] = self.net.res_bus.vm_pu[bus_idx]

            results = results.append(result, ignore_index=True)
        # print(results)
        return results

    # ---------------------------------------------- 2029 July ----------------------------------------------
    # NOTE: Data input to change: 1. e_demand (Jan/July), 2. PV irradiance & WIND profile  3. heat_demand (Jan/July)
    def power_flow_2029_jul(self):

        results = pd.DataFrame()

        # -------------------------- Create loads on the fixed bus bars with 0 p_mw --------------------------
        pp.create_load(self.net, bus=1, p_mw=0, name="Chem Ind Load 1")
        pp.create_load(self.net, bus=12, p_mw=0, name="Chem Ind Load 2")
        pp.create_load(self.net, bus=2, p_mw=0, name="Medium Ind Load 1")
        pp.create_load(self.net, bus=13, p_mw=0, name="Small Ind Load 1")
        pp.create_load(self.net, bus=14, p_mw=0, name="Small Ind Load 2")
        # Commercial loads
        pp.create_load(self.net, bus=3, p_mw=0, name="Commercial load 1")
        pp.create_load(self.net, bus=4, p_mw=0, name="Commercial load 2")
        pp.create_load(self.net, bus=5, p_mw=0, name="Commercial load 3")
        pp.create_load(self.net, bus=9, p_mw=0, name="Commercial load 4")
        pp.create_load(self.net, bus=10, p_mw=0, name="Commercial load 5")
        pp.create_load(self.net, bus=11, p_mw=0, name="Commercial load 6")
        # Household load
        pp.create_load(self.net, bus=6, p_mw=0, name="Household load")  # 38 households

        # -------------------------- Special loads --------------------------
        # HP load at household bus
        pp.create_load(self.net, bus=6, p_mw=0, name="HP load for Households")
        # P2G load at bus = 12
        pp.create_load(self.net, bus=12, p_mw=0, name="P2G load")

        # -------------------------- Create Gas gen at bus 12 --------------------------
        pp.create_gen(self.net, bus=12, p_mw=self.x_gen_bus_12_mw, vm_pu=1.0,
                      name="Gas Power bus 37")  # Peak load = 29.3 MW
        # Gas gen at bus 1
        pp.create_gen(self.net, bus=1, p_mw=self.x_gen_bus_1_mw, vm_pu=1.0,
                      name="Gas Power bus 37")  # Peak load = 20.8 MW
        # print(self.net.gen)

        # -------------------------- PV, WT & CHP --------------------------
        # Create sgens (PV+WT) at each of the specified x_bus-bar with initial p_mw = 0
        x_pv_bus = self.x_pv_bus
        # PV
        for bus in x_pv_bus:
            pp.create_sgen(self.net, bus=bus, p_mw=0, q_mvar=0, name="PV")
        # WT
        x_wt_bus = self.x_wt_bus
        for bus in x_wt_bus:
            pp.create_sgen(self.net, bus=bus, p_mw=0, q_mvar=0, name="WT")
        # CHP
        x_chp_bus = self.chp_bus
        pp.create_sgen(self.net, bus=x_chp_bus, p_mw=0, q_mvar=0, name="CHP")

        # ----------------------------------------- Create BESS -----------------------------------------
        pp.create_storage(self.net, bus=self.bess_bus, p_mw=0, max_e_mwh=self.bess_p_mw * 12 * 0.9,
                          soc_percent=0.5, name="BESS")
        # print(self.net.storage)

        bess_mw = self.bess_p_mw  # this is already for 1 hour = MWh for each battery
        bess_mwh = self.bess_p_mw * 1  # C rate = 1 = max capacity charge and discharge in 1 hr.
        bess_soc = 0.1

        bess_init_mwh = bess_mwh * bess_soc
        bess_update_mwh = bess_init_mwh
        # print("current_bess_energy", bess_update_mwh)

        # <<<<<< ---- Note: Year 2028 Jul - change e_demand, irradiance, heat_demand & WIND profile: ----- >>>>>>>>>>>>>>
        for i, ((load_idx, load_row), (irradiance_idx, irradiance_row)) in \
                enumerate(zip(e_demand_2029_jul.iterrows(),
                              df_irradiance_jul.iterrows())):
            # print("i_jan =", i)
            # print("eload_jan =", load_row['LG 07'])
            # print("PV_irr_jan =", irradiance_row)
            # print("w_speed_jan =", wind_time_series['wind_normalized_jan'][i])
            # # print("th_demand_jan", heat_demand_jan['th_load_38_household'][i])

            # ********************* Update the load values at the specified buses *********************
            # Ind, comm and res loads
            self.net.load.at[0, 'p_mw'] = load_row['LG 01']  # Assuming Chem Industry Load 1 is at index 0
            self.net.load.at[1, 'p_mw'] = load_row[
                'LG 07']  # Peak load = 29.3 MW - Chem Industry Load 2 is at index 1
            self.net.load.at[2, 'p_mw'] = load_row['LG 03']  # Medium industry
            self.net.load.at[3, 'p_mw'] = load_row['small_ind_load_1']
            self.net.load.at[4, 'p_mw'] = load_row['small_ind_load_2']
            # Commercial loads
            self.net.load.at[5, 'p_mw'] = load_row['load_bus3']  # load at bus3
            self.net.load.at[6, 'p_mw'] = load_row['load_bus4']
            self.net.load.at[7, 'p_mw'] = load_row['load_bus5']
            self.net.load.at[8, 'p_mw'] = load_row['load_bus9']
            self.net.load.at[9, 'p_mw'] = load_row['load_bus10']
            self.net.load.at[10, 'p_mw'] = load_row['load_bus11']
            # Household load
            self.net.load.at[11, 'p_mw'] = load_row['load_bus6']  # *10 around 38*10 households

            # ************************ Special loads & heat demand **************************
            # <<<<<<<<<<<<<< ------------------ Change Heat Demand ------------------ >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # HP load @ Household bus
            self.net.load.at[12, 'p_mw'] = heat_demand_2029_jul['th_load_38_household'][i]
            # P2G at bus = 12
            self.net.load.at[13, 'p_mw'] = self.p2g_input_mw

            # print(self.net.load)

            # *************************** PV ***************************
            # print(self.x[14])
            # print(self.x_pv_mw[0])
            self.net.sgen.at[0, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[0]  # Assuming PV 1 is at index 0
            self.net.sgen.at[1, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[1]
            self.net.sgen.at[2, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[2]
            self.net.sgen.at[3, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[3]
            self.net.sgen.at[4, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[4]
            self.net.sgen.at[5, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[5]
            self.net.sgen.at[6, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[6]
            self.net.sgen.at[7, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[7]
            self.net.sgen.at[8, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[8]
            self.net.sgen.at[9, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[9]
            self.net.sgen.at[10, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[10]
            self.net.sgen.at[11, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[11]
            self.net.sgen.at[12, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[12]
            self.net.sgen.at[13, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[13]

            # *************************** WT ***************************
            # print("wt_time_series =", wind_time_series['wind_normalized_jan'][i])
            self.net.sgen.at[14, 'p_mw'] = wind_time_series['wind_normalized_jul'][i] * self.x_wt_mw
            # Assuming WT 1 is at index 14

            # *************************** CHP ***************************
            self.net.sgen.at[15, 'p_mw'] = self.chp_p_mw
            # print(self.net.sgen)

            # ***************************** BESS *******************************************
            bess = BESS(net=self.net, sgen_mwh=self.net.sgen['p_mw'].sum(),
                        demand_e_mwh=self.net.load['p_mw'].sum(),
                        bess_mw=bess_mw,
                        bess_mwh=bess_mwh,
                        # bess_soc=bess_soc,
                        # current_energy=bess_current_energy,
                        # bess_max_energy=bess_max_energy,
                        # bess_min_energy=bess_min_energy,
                        bess_update_mwh=bess_update_mwh)
            res_bess_mw = bess.bms_update()[0]
            res_bess_mwh = bess.bms_update()[1]
            res_bess_power_loss_mwh = bess.bms_update()[2]
            res_bess_power_deficit_mwh = bess.bms_update()[3]

            self.net.storage.at[0, 'p_mw'] = res_bess_mw
            # bess_mw_update += res_bess_mwh
            bess_update_mwh = res_bess_mwh
            # print("bess_mw_update =", bess_mw_update)
            # print(self.net.storage)

            pp.runpp(self.net)

            result = {
                # 'time_step': i,
                'demand_mw': self.net.res_load.p_mw.sum(),  # summing the total load at each hour (t)
                'line_loss_mw': self.net.res_line.pl_mw.values[0],
                'gas_gen_mw': self.net.res_gen.p_mw.sum(),
                'pv_wt_chp_mw': self.net.res_sgen.p_mw.sum(),  # summing the total PV gen at each hour (t)
                'bess_mw': self.net.res_storage.p_mw.sum(),
                'ext_grid_mw': self.net.res_ext_grid.p_mw.values[0],
                'bess_mwh': res_bess_mwh
                # 'res_bess_power_loss_mwh': res_bess_power_loss_mwh,
                # 'res_bess_power_deficit_mwh': res_bess_power_deficit_mwh
            }

            for bus_idx in self.net.bus.index:
                result[f'bus_{int(bus_idx)}_voltage_pu'] = self.net.res_bus.vm_pu[bus_idx]

            results = results.append(result, ignore_index=True)

        return results

    # =================================================== 2030 Jan ===================================================
    # NOTE: Data input to change: 1. e_demand (Jan/July), 2. PV irradiance & WIND profile  3. heat_demand (Jan/July)
    def power_flow_2030_jan(self):

        results = pd.DataFrame()

        # -------------------------- Create loads on the fixed bus bars with 0 p_mw --------------------------
        pp.create_load(self.net, bus=1, p_mw=0, name="Chem Ind Load 1")
        pp.create_load(self.net, bus=12, p_mw=0, name="Chem Ind Load 2")
        pp.create_load(self.net, bus=2, p_mw=0, name="Medium Ind Load 1")
        pp.create_load(self.net, bus=13, p_mw=0, name="Small Ind Load 1")
        pp.create_load(self.net, bus=14, p_mw=0, name="Small Ind Load 2")
        # Commercial loads
        pp.create_load(self.net, bus=3, p_mw=0, name="Commercial load 1")
        pp.create_load(self.net, bus=4, p_mw=0, name="Commercial load 2")
        pp.create_load(self.net, bus=5, p_mw=0, name="Commercial load 3")
        pp.create_load(self.net, bus=9, p_mw=0, name="Commercial load 4")
        pp.create_load(self.net, bus=10, p_mw=0, name="Commercial load 5")
        pp.create_load(self.net, bus=11, p_mw=0, name="Commercial load 6")
        # Household load
        pp.create_load(self.net, bus=6, p_mw=0, name="Household load")  # 38 households

        # --------------------------Special loads --------------------------
        # HP load at household bus
        pp.create_load(self.net, bus=6, p_mw=0, name="HP load for Households")
        # P2G load at bus = 12
        pp.create_load(self.net, bus=12, p_mw=0, name="P2G load")

        # -------------------------- Create Gas gen at bus 12 --------------------------
        pp.create_gen(self.net, bus=12, p_mw=self.x_gen_bus_12_mw, vm_pu=1.0,
                      name="Gas Power bus 37")  # Peak load = 29.3 MW
        # Gas gen at bus 1
        pp.create_gen(self.net, bus=1, p_mw=self.x_gen_bus_1_mw, vm_pu=1.0,
                      name="Gas Power bus 37")  # Peak load = 20.8 MW
        # print(self.net.gen)

        # --------------------------PV, WT & CHP --------------------------
        # Create sgens (PV+WT) at each of the specified x_bus-bar with initial p_mw = 0
        x_pv_bus = self.x_pv_bus
        # PV
        for bus in x_pv_bus:
            pp.create_sgen(self.net, bus=bus, p_mw=0, q_mvar=0, name="PV")
        # WT
        x_wt_bus = self.x_wt_bus
        for bus in x_wt_bus:
            pp.create_sgen(self.net, bus=bus, p_mw=0, q_mvar=0, name="WT")
        # CHP
        x_chp_bus = self.chp_bus
        pp.create_sgen(self.net, bus=x_chp_bus, p_mw=0, q_mvar=0, name="CHP")

        # ----------------------------------------- Create BESS -----------------------------------------
        pp.create_storage(self.net, bus=self.bess_bus, p_mw=0, max_e_mwh=self.bess_p_mw * 12 * 0.9,
                          soc_percent=0.5, name="BESS")
        # print(self.net.storage)

        bess_mw = self.bess_p_mw  # this is already for 1 hour = MWh for each battery
        bess_mwh = self.bess_p_mw * 1  # C rate = 1 = max capacity charge and discharge in 1 hr.
        bess_soc = 0.1

        bess_init_mwh = bess_mwh * bess_soc
        bess_update_mwh = bess_init_mwh
        # print("current_bess_energy", bess_update_mwh)

        # CHANGE: >>>>>>>>>-- change e_demand, irradiance, WIND profile, heat_demand: >>>>>>>>
        for i, ((load_idx, load_row), (irradiance_idx, irradiance_row)) in \
                enumerate(zip(e_demand_2030_jan.iterrows(),
                              df_irradiance_jan.iterrows())):

            # ********************* Update the load values at the specified buses *********************
            # Ind, comm and res loads
            self.net.load.at[0, 'p_mw'] = load_row['LG 01']  # Assuming Chem Industry Load 1 is at index 0
            self.net.load.at[1, 'p_mw'] = load_row[
                'LG 07']  # Peak load = 29.3 MW - Chem Industry Load 2 is at index 1
            self.net.load.at[2, 'p_mw'] = load_row['LG 03']  # Medium industry
            self.net.load.at[3, 'p_mw'] = load_row['small_ind_load_1']
            self.net.load.at[4, 'p_mw'] = load_row['small_ind_load_2']
            # Commercial loads
            self.net.load.at[5, 'p_mw'] = load_row['load_bus3']  # load at bus3
            self.net.load.at[6, 'p_mw'] = load_row['load_bus4']
            self.net.load.at[7, 'p_mw'] = load_row['load_bus5']
            self.net.load.at[8, 'p_mw'] = load_row['load_bus9']
            self.net.load.at[9, 'p_mw'] = load_row['load_bus10']
            self.net.load.at[10, 'p_mw'] = load_row['load_bus11']
            # Household load
            self.net.load.at[11, 'p_mw'] = load_row['load_bus6']  # *10 around 38*10 households

            # ************************ Special loads & heat demand **************************
            # <<<<< ------------------------ Change Heat Demand ---------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # HP load @ Household bus
            self.net.load.at[12, 'p_mw'] = heat_demand_2030_jan['th_load_38_household'][i]
            # P2G at bus = 12
            self.net.load.at[13, 'p_mw'] = self.p2g_input_mw

            # print(self.net.load)

            # *************************** PV ***************************
            # print(self.x_pv_mw[0])
            self.net.sgen.at[0, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[0]  # Assuming PV 1 is at index 0
            self.net.sgen.at[1, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[1]
            self.net.sgen.at[2, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[2]
            self.net.sgen.at[3, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[3]
            self.net.sgen.at[4, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[4]
            self.net.sgen.at[5, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[5]
            self.net.sgen.at[6, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[6]
            self.net.sgen.at[7, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[7]
            self.net.sgen.at[8, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[8]
            self.net.sgen.at[9, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[9]
            self.net.sgen.at[10, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[10]
            self.net.sgen.at[11, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[11]
            self.net.sgen.at[12, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[12]
            self.net.sgen.at[13, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[13]

            # *************************** WT ***************************
            # >>>>>>>>>>>>>>>>>>>>>>> ----- CHANGE WT time series ----- >>>>>>>>>>>>>>>>>>>>
            self.net.sgen.at[14, 'p_mw'] = wind_time_series['wind_normalized_jan'][i] * self.x_wt_mw
            # Assuming WT 1 is at index 14

            # *************************** CHP ***************************
            self.net.sgen.at[15, 'p_mw'] = self.chp_p_mw
            # print(self.net.sgen)

            # ***************************** BESS *******************************************
            # print("bess_mw", bess_mw)
            bess = BESS(net=self.net, sgen_mwh=self.net.sgen['p_mw'].sum(),
                        demand_e_mwh=self.net.load['p_mw'].sum(),
                        bess_mw=bess_mw,
                        bess_mwh=bess_mwh,
                        # bess_soc=bess_soc,
                        # current_energy=bess_current_energy,
                        # bess_max_energy=bess_max_energy,
                        # bess_min_energy=bess_min_energy,
                        bess_update_mwh=bess_update_mwh)
            res_bess_mw = bess.bms_update()[0]
            res_bess_mwh = bess.bms_update()[1]
            res_bess_power_loss_mwh = bess.bms_update()[2]
            res_bess_power_deficit_mwh = bess.bms_update()[3]

            self.net.storage.at[0, 'p_mw'] = res_bess_mw
            # bess_mw_update += res_bess_mwh
            bess_update_mwh = res_bess_mwh
            # print("bess_mw_update =", bess_mw_update)
            # print(self.net.storage)

            pp.runpp(self.net)

            result = {
                # 'time_step': i,
                'demand_mw': self.net.res_load.p_mw.sum(),  # summing the total load at each hour (t)
                'line_loss_mw': self.net.res_line.pl_mw.values[0],
                'gas_gen_mw': self.net.res_gen.p_mw.sum(),
                'pv_wt_chp_mw': self.net.res_sgen.p_mw.sum(),  # summing the total PV gen at each hour (t)
                'bess_mw': self.net.res_storage.p_mw.sum(),
                'ext_grid_mw': self.net.res_ext_grid.p_mw.values[0],
                'bess_mwh': res_bess_mwh
                # 'res_bess_power_loss_mwh': res_bess_power_loss_mwh,
                # 'res_bess_power_deficit_mwh': res_bess_power_deficit_mwh
            }

            for bus_idx in self.net.bus.index:
                result[f'bus_{int(bus_idx)}_voltage_pu'] = self.net.res_bus.vm_pu[bus_idx]

            results = results.append(result, ignore_index=True)
        # print(results)
        return results

    # ---------------------------------------------- 2030 July ----------------------------------------------
    # NOTE: Data input to change: 1. e_demand (Jan/July), 2. PV irradiance & WIND profile  3. heat_demand (Jan/July)
    def power_flow_2030_jul(self):
        results = pd.DataFrame()
        # -------------------------- Create loads on the fixed bus bars with 0 p_mw --------------------------
        pp.create_load(self.net, bus=1, p_mw=0, name="Chem Ind Load 1")
        pp.create_load(self.net, bus=12, p_mw=0, name="Chem Ind Load 2")
        pp.create_load(self.net, bus=2, p_mw=0, name="Medium Ind Load 1")
        pp.create_load(self.net, bus=13, p_mw=0, name="Small Ind Load 1")
        pp.create_load(self.net, bus=14, p_mw=0, name="Small Ind Load 2")
        # Commercial loads
        pp.create_load(self.net, bus=3, p_mw=0, name="Commercial load 1")
        pp.create_load(self.net, bus=4, p_mw=0, name="Commercial load 2")
        pp.create_load(self.net, bus=5, p_mw=0, name="Commercial load 3")
        pp.create_load(self.net, bus=9, p_mw=0, name="Commercial load 4")
        pp.create_load(self.net, bus=10, p_mw=0, name="Commercial load 5")
        pp.create_load(self.net, bus=11, p_mw=0, name="Commercial load 6")
        # Household load
        pp.create_load(self.net, bus=6, p_mw=0, name="Household load")  # 38 households

        # -------------------------- Special loads --------------------------
        # HP load at household bus
        pp.create_load(self.net, bus=6, p_mw=0, name="HP load for Households")
        # P2G load at bus = 12
        pp.create_load(self.net, bus=12, p_mw=0, name="P2G load")

        # -------------------------- Create Gas gen at bus 12 --------------------------
        pp.create_gen(self.net, bus=12, p_mw=self.x_gen_bus_12_mw, vm_pu=1.0,
                      name="Gas Power bus 37")  # Peak load = 29.3 MW
        # Gas gen at bus 1
        pp.create_gen(self.net, bus=1, p_mw=self.x_gen_bus_1_mw, vm_pu=1.0,
                      name="Gas Power bus 37")  # Peak load = 20.8 MW
        # print(self.net.gen)

        # -------------------------- PV, WT & CHP --------------------------
        # Create sgens (PV+WT) at each of the specified x_bus-bar with initial p_mw = 0
        x_pv_bus = self.x_pv_bus
        # PV
        for bus in x_pv_bus:
            pp.create_sgen(self.net, bus=bus, p_mw=0, q_mvar=0, name="PV")
        # WT
        x_wt_bus = self.x_wt_bus
        for bus in x_wt_bus:
            pp.create_sgen(self.net, bus=bus, p_mw=0, q_mvar=0, name="WT")
        # CHP
        x_chp_bus = self.chp_bus
        pp.create_sgen(self.net, bus=x_chp_bus, p_mw=0, q_mvar=0, name="CHP")

        # ----------------------------------------- Create BESS -----------------------------------------
        pp.create_storage(self.net, bus=self.bess_bus, p_mw=0, max_e_mwh=self.bess_p_mw * 12 * 0.9,
                          soc_percent=0.5, name="BESS")
        # print(self.net.storage)

        bess_mw = self.bess_p_mw  # this is already for 1 hour = MWh for each battery
        bess_mwh = self.bess_p_mw * 1  # C rate = 1 = max capacity charge and discharge in 1 hr.
        bess_soc = 0.1

        bess_init_mwh = bess_mwh * bess_soc
        bess_update_mwh = bess_init_mwh
        # print("current_bess_energy", bess_update_mwh)

        # <<<<<< ---- Note: change e_demand, irradiance, heat_demand & WIND profile: ----- >>>>>>>>>>>>
        for i, ((load_idx, load_row), (irradiance_idx, irradiance_row)) in \
                enumerate(zip(e_demand_2030_jul.iterrows(),
                              df_irradiance_jul.iterrows())):

            # ********************* Update the load values at the specified buses *********************
            # Ind, comm and res loads
            self.net.load.at[0, 'p_mw'] = load_row['LG 01']  # Assuming Chem Industry Load 1 is at index 0
            self.net.load.at[1, 'p_mw'] = load_row[
                'LG 07']  # Peak load = 29.3 MW - Chem Industry Load 2 is at index 1
            self.net.load.at[2, 'p_mw'] = load_row['LG 03']  # Medium industry
            self.net.load.at[3, 'p_mw'] = load_row['small_ind_load_1']
            self.net.load.at[4, 'p_mw'] = load_row['small_ind_load_2']
            # Commercial loads
            self.net.load.at[5, 'p_mw'] = load_row['load_bus3']  # load at bus3
            self.net.load.at[6, 'p_mw'] = load_row['load_bus4']
            self.net.load.at[7, 'p_mw'] = load_row['load_bus5']
            self.net.load.at[8, 'p_mw'] = load_row['load_bus9']
            self.net.load.at[9, 'p_mw'] = load_row['load_bus10']
            self.net.load.at[10, 'p_mw'] = load_row['load_bus11']
            # Household load
            self.net.load.at[11, 'p_mw'] = load_row['load_bus6']  # *10 around 38*10 households

            # ************************ Special loads & heat demand **************************
            # <<<<<<<<<<<<<< ------------------ Change Heat Demand -------------- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # HP load @ Household bus
            self.net.load.at[12, 'p_mw'] = heat_demand_2030_jul['th_load_38_household'][i]
            # P2G at bus = 12
            self.net.load.at[13, 'p_mw'] = self.p2g_input_mw

            # print(self.net.load)

            # *************************** PV ***************************
            # print(self.x[14])
            # print(self.x_pv_mw[0])
            self.net.sgen.at[0, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[0]  # Assuming PV 1 is at index 0
            self.net.sgen.at[1, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[1]
            self.net.sgen.at[2, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[2]
            self.net.sgen.at[3, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[3]
            self.net.sgen.at[4, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[4]
            self.net.sgen.at[5, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[5]
            self.net.sgen.at[6, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[6]
            self.net.sgen.at[7, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[7]
            self.net.sgen.at[8, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[8]
            self.net.sgen.at[9, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[9]
            self.net.sgen.at[10, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[10]
            self.net.sgen.at[11, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[11]
            self.net.sgen.at[12, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[12]
            self.net.sgen.at[13, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[13]

            # *************************** WT ***************************
            # # >>>>>>>>>>>>>>>>>>>>>>> ----- CHANGE WT time series ----- >>>>>>>>>>>>>>>>>>>>
            self.net.sgen.at[14, 'p_mw'] = wind_time_series['wind_normalized_jul'][i] * self.x_wt_mw
            # Assuming WT 1 is at index 14

            # *************************** CHP ***************************
            self.net.sgen.at[15, 'p_mw'] = self.chp_p_mw
            # print(self.net.sgen)

            # ***************************** BESS *******************************************
            bess = BESS(net=self.net, sgen_mwh=self.net.sgen['p_mw'].sum(),
                        demand_e_mwh=self.net.load['p_mw'].sum(),
                        bess_mw=bess_mw,
                        bess_mwh=bess_mwh,
                        # bess_soc=bess_soc,
                        # current_energy=bess_current_energy,
                        # bess_max_energy=bess_max_energy,
                        # bess_min_energy=bess_min_energy,
                        bess_update_mwh=bess_update_mwh)
            res_bess_mw = bess.bms_update()[0]
            res_bess_mwh = bess.bms_update()[1]
            res_bess_power_loss_mwh = bess.bms_update()[2]
            res_bess_power_deficit_mwh = bess.bms_update()[3]

            self.net.storage.at[0, 'p_mw'] = res_bess_mw
            # bess_mw_update += res_bess_mwh
            bess_update_mwh = res_bess_mwh
            # print("bess_mw_update =", bess_mw_update)
            # print(self.net.storage)

            pp.runpp(self.net)

            result = {
                # 'time_step': i,
                'demand_mw': self.net.res_load.p_mw.sum(),  # summing the total load at each hour (t)
                'line_loss_mw': self.net.res_line.pl_mw.values[0],
                'gas_gen_mw': self.net.res_gen.p_mw.sum(),
                'pv_wt_chp_mw': self.net.res_sgen.p_mw.sum(),  # summing the total PV gen at each hour (t)
                'bess_mw': self.net.res_storage.p_mw.sum(),
                'ext_grid_mw': self.net.res_ext_grid.p_mw.values[0],
                'bess_mwh': res_bess_mwh
                # 'res_bess_power_loss_mwh': res_bess_power_loss_mwh,
                # 'res_bess_power_deficit_mwh': res_bess_power_deficit_mwh
            }

            for bus_idx in self.net.bus.index:
                result[f'bus_{int(bus_idx)}_voltage_pu'] = self.net.res_bus.vm_pu[bus_idx]

            results = results.append(result, ignore_index=True)

        return results

    # =================================================== 2031 Jan ===================================================
    # NOTE: Data input to change: 1. e_demand (Jan/July), 2. PV irradiance & WIND profile  3. heat_demand (Jan/July)
    def power_flow_2031_jan(self):

        results = pd.DataFrame()

        # -------------------------- Create loads on the fixed bus bars with 0 p_mw --------------------------
        pp.create_load(self.net, bus=1, p_mw=0, name="Chem Ind Load 1")
        pp.create_load(self.net, bus=12, p_mw=0, name="Chem Ind Load 2")
        pp.create_load(self.net, bus=2, p_mw=0, name="Medium Ind Load 1")
        pp.create_load(self.net, bus=13, p_mw=0, name="Small Ind Load 1")
        pp.create_load(self.net, bus=14, p_mw=0, name="Small Ind Load 2")
        # Commercial loads
        pp.create_load(self.net, bus=3, p_mw=0, name="Commercial load 1")
        pp.create_load(self.net, bus=4, p_mw=0, name="Commercial load 2")
        pp.create_load(self.net, bus=5, p_mw=0, name="Commercial load 3")
        pp.create_load(self.net, bus=9, p_mw=0, name="Commercial load 4")
        pp.create_load(self.net, bus=10, p_mw=0, name="Commercial load 5")
        pp.create_load(self.net, bus=11, p_mw=0, name="Commercial load 6")
        # Household load
        pp.create_load(self.net, bus=6, p_mw=0, name="Household load")  # 38 households

        # --------------------------Special loads --------------------------
        # HP load at household bus
        pp.create_load(self.net, bus=6, p_mw=0, name="HP load for Households")
        # P2G load at bus = 12
        pp.create_load(self.net, bus=12, p_mw=0, name="P2G load")

        # -------------------------- Create Gas gen at bus 12 --------------------------
        pp.create_gen(self.net, bus=12, p_mw=self.x_gen_bus_12_mw, vm_pu=1.0,
                      name="Gas Power bus 37")  # Peak load = 29.3 MW
        # Gas gen at bus 1
        pp.create_gen(self.net, bus=1, p_mw=self.x_gen_bus_1_mw, vm_pu=1.0,
                      name="Gas Power bus 37")  # Peak load = 20.8 MW
        # print(self.net.gen)

        # --------------------------PV, WT & CHP --------------------------
        # Create sgens (PV+WT) at each of the specified x_bus-bar with initial p_mw = 0
        x_pv_bus = self.x_pv_bus
        # PV
        for bus in x_pv_bus:
            pp.create_sgen(self.net, bus=bus, p_mw=0, q_mvar=0, name="PV")
        # WT
        x_wt_bus = self.x_wt_bus
        for bus in x_wt_bus:
            pp.create_sgen(self.net, bus=bus, p_mw=0, q_mvar=0, name="WT")
        # CHP
        x_chp_bus = self.chp_bus
        pp.create_sgen(self.net, bus=x_chp_bus, p_mw=0, q_mvar=0, name="CHP")

        # ----------------------------------------- Create BESS -----------------------------------------
        pp.create_storage(self.net, bus=self.bess_bus, p_mw=0, max_e_mwh=self.bess_p_mw * 12 * 0.9,
                          soc_percent=0.5, name="BESS")
        # print(self.net.storage)

        bess_mw = self.bess_p_mw  # this is already for 1 hour = MWh for each battery
        bess_mwh = self.bess_p_mw * 1  # C rate = 1 = max capacity charge and discharge in 1 hr.
        bess_soc = 0.1

        bess_init_mwh = bess_mwh * bess_soc
        bess_update_mwh = bess_init_mwh
        # print("current_bess_energy", bess_update_mwh)

        # CHANGE: >>>>>>>>>-- change e_demand, irradiance, WIND profile, heat_demand: >>>>>>>>
        for i, ((load_idx, load_row), (irradiance_idx, irradiance_row)) in \
                enumerate(zip(e_demand_2031_jan.iterrows(),
                              df_irradiance_jan.iterrows())):

            # ********************* Update the load values at the specified buses *********************
            # Ind, comm and res loads
            self.net.load.at[0, 'p_mw'] = load_row['LG 01']  # Assuming Chem Industry Load 1 is at index 0
            self.net.load.at[1, 'p_mw'] = load_row[
                'LG 07']  # Peak load = 29.3 MW - Chem Industry Load 2 is at index 1
            self.net.load.at[2, 'p_mw'] = load_row['LG 03']  # Medium industry
            self.net.load.at[3, 'p_mw'] = load_row['small_ind_load_1']
            self.net.load.at[4, 'p_mw'] = load_row['small_ind_load_2']
            # Commercial loads
            self.net.load.at[5, 'p_mw'] = load_row['load_bus3']  # load at bus3
            self.net.load.at[6, 'p_mw'] = load_row['load_bus4']
            self.net.load.at[7, 'p_mw'] = load_row['load_bus5']
            self.net.load.at[8, 'p_mw'] = load_row['load_bus9']
            self.net.load.at[9, 'p_mw'] = load_row['load_bus10']
            self.net.load.at[10, 'p_mw'] = load_row['load_bus11']
            # Household load
            self.net.load.at[11, 'p_mw'] = load_row['load_bus6']  # *10 around 38*10 households

            # ************************ Special loads & heat demand **************************
            # <<<<< ------------------------ Change Heat Demand ---------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # HP load @ Household bus
            self.net.load.at[12, 'p_mw'] = heat_demand_2031_jan['th_load_38_household'][i]
            # P2G at bus = 12
            self.net.load.at[13, 'p_mw'] = self.p2g_input_mw

            # print(self.net.load)

            # *************************** PV ***************************
            # print(self.x_pv_mw[0])
            self.net.sgen.at[0, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[0]  # Assuming PV 1 is at index 0
            self.net.sgen.at[1, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[1]
            self.net.sgen.at[2, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[2]
            self.net.sgen.at[3, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[3]
            self.net.sgen.at[4, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[4]
            self.net.sgen.at[5, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[5]
            self.net.sgen.at[6, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[6]
            self.net.sgen.at[7, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[7]
            self.net.sgen.at[8, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[8]
            self.net.sgen.at[9, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[9]
            self.net.sgen.at[10, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[10]
            self.net.sgen.at[11, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[11]
            self.net.sgen.at[12, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[12]
            self.net.sgen.at[13, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[13]

            # *************************** WT ***************************
            # >>>>>>>>>>>>>>>>>>>>>>> ----- CHANGE WT time series ----- >>>>>>>>>>>>>>>>>>>>
            self.net.sgen.at[14, 'p_mw'] = wind_time_series['wind_normalized_jan'][i] * self.x_wt_mw
            # Assuming WT 1 is at index 14

            # *************************** CHP ***************************
            self.net.sgen.at[15, 'p_mw'] = self.chp_p_mw
            # print(self.net.sgen)

            # ***************************** BESS *******************************************
            # print("bess_mw", bess_mw)
            bess = BESS(net=self.net, sgen_mwh=self.net.sgen['p_mw'].sum(),
                        demand_e_mwh=self.net.load['p_mw'].sum(),
                        bess_mw=bess_mw,
                        bess_mwh=bess_mwh,
                        # bess_soc=bess_soc,
                        # current_energy=bess_current_energy,
                        # bess_max_energy=bess_max_energy,
                        # bess_min_energy=bess_min_energy,
                        bess_update_mwh=bess_update_mwh)
            res_bess_mw = bess.bms_update()[0]
            res_bess_mwh = bess.bms_update()[1]
            res_bess_power_loss_mwh = bess.bms_update()[2]
            res_bess_power_deficit_mwh = bess.bms_update()[3]

            self.net.storage.at[0, 'p_mw'] = res_bess_mw
            # bess_mw_update += res_bess_mwh
            bess_update_mwh = res_bess_mwh
            # print("bess_mw_update =", bess_mw_update)
            # print(self.net.storage)

            pp.runpp(self.net)

            result = {
                # 'time_step': i,
                'demand_mw': self.net.res_load.p_mw.sum(),  # summing the total load at each hour (t)
                'line_loss_mw': self.net.res_line.pl_mw.values[0],
                'gas_gen_mw': self.net.res_gen.p_mw.sum(),
                'pv_wt_chp_mw': self.net.res_sgen.p_mw.sum(),  # summing the total PV gen at each hour (t)
                'bess_mw': self.net.res_storage.p_mw.sum(),
                'ext_grid_mw': self.net.res_ext_grid.p_mw.values[0],
                'bess_mwh': res_bess_mwh
                # 'res_bess_power_loss_mwh': res_bess_power_loss_mwh,
                # 'res_bess_power_deficit_mwh': res_bess_power_deficit_mwh
            }

            for bus_idx in self.net.bus.index:
                result[f'bus_{int(bus_idx)}_voltage_pu'] = self.net.res_bus.vm_pu[bus_idx]

            results = results.append(result, ignore_index=True)
        # print(results)
        return results

    # ---------------------------------------------- 2031 July ----------------------------------------------
    # NOTE: Data input to change: 1. e_demand (Jan/July), 2. PV irradiance & WIND profile  3. heat_demand (Jan/July)
    def power_flow_2031_jul(self):
        results = pd.DataFrame()
        # -------------------------- Create loads on the fixed bus bars with 0 p_mw --------------------------
        pp.create_load(self.net, bus=1, p_mw=0, name="Chem Ind Load 1")
        pp.create_load(self.net, bus=12, p_mw=0, name="Chem Ind Load 2")
        pp.create_load(self.net, bus=2, p_mw=0, name="Medium Ind Load 1")
        pp.create_load(self.net, bus=13, p_mw=0, name="Small Ind Load 1")
        pp.create_load(self.net, bus=14, p_mw=0, name="Small Ind Load 2")
        # Commercial loads
        pp.create_load(self.net, bus=3, p_mw=0, name="Commercial load 1")
        pp.create_load(self.net, bus=4, p_mw=0, name="Commercial load 2")
        pp.create_load(self.net, bus=5, p_mw=0, name="Commercial load 3")
        pp.create_load(self.net, bus=9, p_mw=0, name="Commercial load 4")
        pp.create_load(self.net, bus=10, p_mw=0, name="Commercial load 5")
        pp.create_load(self.net, bus=11, p_mw=0, name="Commercial load 6")
        # Household load
        pp.create_load(self.net, bus=6, p_mw=0, name="Household load")  # 38 households

        # -------------------------- Special loads --------------------------
        # HP load at household bus
        pp.create_load(self.net, bus=6, p_mw=0, name="HP load for Households")
        # P2G load at bus = 12
        pp.create_load(self.net, bus=12, p_mw=0, name="P2G load")

        # -------------------------- Create Gas gen at bus 12 --------------------------
        pp.create_gen(self.net, bus=12, p_mw=self.x_gen_bus_12_mw, vm_pu=1.0,
                      name="Gas Power bus 37")  # Peak load = 29.3 MW
        # Gas gen at bus 1
        pp.create_gen(self.net, bus=1, p_mw=self.x_gen_bus_1_mw, vm_pu=1.0,
                      name="Gas Power bus 37")  # Peak load = 20.8 MW
        # print(self.net.gen)

        # -------------------------- PV, WT & CHP --------------------------
        # Create sgens (PV+WT) at each of the specified x_bus-bar with initial p_mw = 0
        x_pv_bus = self.x_pv_bus
        # PV
        for bus in x_pv_bus:
            pp.create_sgen(self.net, bus=bus, p_mw=0, q_mvar=0, name="PV")
        # WT
        x_wt_bus = self.x_wt_bus
        for bus in x_wt_bus:
            pp.create_sgen(self.net, bus=bus, p_mw=0, q_mvar=0, name="WT")
        # CHP
        x_chp_bus = self.chp_bus
        pp.create_sgen(self.net, bus=x_chp_bus, p_mw=0, q_mvar=0, name="CHP")

        # ----------------------------------------- Create BESS -----------------------------------------
        pp.create_storage(self.net, bus=self.bess_bus, p_mw=0, max_e_mwh=self.bess_p_mw * 12 * 0.9,
                          soc_percent=0.5, name="BESS")
        # print(self.net.storage)

        bess_mw = self.bess_p_mw  # this is already for 1 hour = MWh for each battery
        bess_mwh = self.bess_p_mw * 1  # C rate = 1 = max capacity charge and discharge in 1 hr.
        bess_soc = 0.1

        bess_init_mwh = bess_mwh * bess_soc
        bess_update_mwh = bess_init_mwh
        # print("current_bess_energy", bess_update_mwh)

        # <<<<<< ---- Note: change e_demand, irradiance, heat_demand & WIND profile: ----- >>>>>>>>>>>>
        for i, ((load_idx, load_row), (irradiance_idx, irradiance_row)) in \
                enumerate(zip(e_demand_2031_jul.iterrows(),
                              df_irradiance_jul.iterrows())):

            # ********************* Update the load values at the specified buses *********************
            # Ind, comm and res loads
            self.net.load.at[0, 'p_mw'] = load_row['LG 01']  # Assuming Chem Industry Load 1 is at index 0
            self.net.load.at[1, 'p_mw'] = load_row[
                'LG 07']  # Peak load = 29.3 MW - Chem Industry Load 2 is at index 1
            self.net.load.at[2, 'p_mw'] = load_row['LG 03']  # Medium industry
            self.net.load.at[3, 'p_mw'] = load_row['small_ind_load_1']
            self.net.load.at[4, 'p_mw'] = load_row['small_ind_load_2']
            # Commercial loads
            self.net.load.at[5, 'p_mw'] = load_row['load_bus3']  # load at bus3
            self.net.load.at[6, 'p_mw'] = load_row['load_bus4']
            self.net.load.at[7, 'p_mw'] = load_row['load_bus5']
            self.net.load.at[8, 'p_mw'] = load_row['load_bus9']
            self.net.load.at[9, 'p_mw'] = load_row['load_bus10']
            self.net.load.at[10, 'p_mw'] = load_row['load_bus11']
            # Household load
            self.net.load.at[11, 'p_mw'] = load_row['load_bus6']  # *10 around 38*10 households

            # ************************ Special loads & heat demand **************************
            # <<<<<<<<<<<<<< ------------------ Change Heat Demand -------------- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # HP load @ Household bus
            self.net.load.at[12, 'p_mw'] = heat_demand_2031_jul['th_load_38_household'][i]
            # P2G at bus = 12
            self.net.load.at[13, 'p_mw'] = self.p2g_input_mw

            # print(self.net.load)

            # *************************** PV ***************************
            # print(self.x[14])
            # print(self.x_pv_mw[0])
            self.net.sgen.at[0, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[0]  # Assuming PV 1 is at index 0
            self.net.sgen.at[1, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[1]
            self.net.sgen.at[2, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[2]
            self.net.sgen.at[3, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[3]
            self.net.sgen.at[4, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[4]
            self.net.sgen.at[5, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[5]
            self.net.sgen.at[6, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[6]
            self.net.sgen.at[7, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[7]
            self.net.sgen.at[8, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[8]
            self.net.sgen.at[9, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[9]
            self.net.sgen.at[10, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[10]
            self.net.sgen.at[11, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[11]
            self.net.sgen.at[12, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[12]
            self.net.sgen.at[13, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[13]

            # *************************** WT ***************************
            # # >>>>>>>>>>>>>>>>>>>>>>> ----- CHANGE WT time series ----- >>>>>>>>>>>>>>>>>>>>
            self.net.sgen.at[14, 'p_mw'] = wind_time_series['wind_normalized_jul'][i] * self.x_wt_mw
            # Assuming WT 1 is at index 14

            # *************************** CHP ***************************
            self.net.sgen.at[15, 'p_mw'] = self.chp_p_mw
            # print(self.net.sgen)

            # ***************************** BESS *******************************************
            bess = BESS(net=self.net, sgen_mwh=self.net.sgen['p_mw'].sum(),
                        demand_e_mwh=self.net.load['p_mw'].sum(),
                        bess_mw=bess_mw,
                        bess_mwh=bess_mwh,
                        # bess_soc=bess_soc,
                        # current_energy=bess_current_energy,
                        # bess_max_energy=bess_max_energy,
                        # bess_min_energy=bess_min_energy,
                        bess_update_mwh=bess_update_mwh)
            res_bess_mw = bess.bms_update()[0]
            res_bess_mwh = bess.bms_update()[1]
            res_bess_power_loss_mwh = bess.bms_update()[2]
            res_bess_power_deficit_mwh = bess.bms_update()[3]

            self.net.storage.at[0, 'p_mw'] = res_bess_mw
            # bess_mw_update += res_bess_mwh
            bess_update_mwh = res_bess_mwh
            # print("bess_mw_update =", bess_mw_update)
            # print(self.net.storage)

            pp.runpp(self.net)

            result = {
                # 'time_step': i,
                'demand_mw': self.net.res_load.p_mw.sum(),  # summing the total load at each hour (t)
                'line_loss_mw': self.net.res_line.pl_mw.values[0],
                'gas_gen_mw': self.net.res_gen.p_mw.sum(),
                'pv_wt_chp_mw': self.net.res_sgen.p_mw.sum(),  # summing the total PV gen at each hour (t)
                'bess_mw': self.net.res_storage.p_mw.sum(),
                'ext_grid_mw': self.net.res_ext_grid.p_mw.values[0],
                'bess_mwh': res_bess_mwh
                # 'res_bess_power_loss_mwh': res_bess_power_loss_mwh,
                # 'res_bess_power_deficit_mwh': res_bess_power_deficit_mwh
            }

            for bus_idx in self.net.bus.index:
                result[f'bus_{int(bus_idx)}_voltage_pu'] = self.net.res_bus.vm_pu[bus_idx]

            results = results.append(result, ignore_index=True)

        return results

    # =================================================== 2032 Jan ===================================================
    # NOTE: Data input to change: 1. e_demand (Jan/July), 2. PV irradiance & WIND profile  3. heat_demand (Jan/July)

    def power_flow_2032_jan(self):

        results = pd.DataFrame()

        # -------------------------- Create loads on the fixed bus bars with 0 p_mw --------------------------
        pp.create_load(self.net, bus=1, p_mw=0, name="Chem Ind Load 1")
        pp.create_load(self.net, bus=12, p_mw=0, name="Chem Ind Load 2")
        pp.create_load(self.net, bus=2, p_mw=0, name="Medium Ind Load 1")
        pp.create_load(self.net, bus=13, p_mw=0, name="Small Ind Load 1")
        pp.create_load(self.net, bus=14, p_mw=0, name="Small Ind Load 2")
        # Commercial loads
        pp.create_load(self.net, bus=3, p_mw=0, name="Commercial load 1")
        pp.create_load(self.net, bus=4, p_mw=0, name="Commercial load 2")
        pp.create_load(self.net, bus=5, p_mw=0, name="Commercial load 3")
        pp.create_load(self.net, bus=9, p_mw=0, name="Commercial load 4")
        pp.create_load(self.net, bus=10, p_mw=0, name="Commercial load 5")
        pp.create_load(self.net, bus=11, p_mw=0, name="Commercial load 6")
        # Household load
        pp.create_load(self.net, bus=6, p_mw=0, name="Household load")  # 38 households

        # --------------------------Special loads --------------------------
        # HP load at household bus
        pp.create_load(self.net, bus=6, p_mw=0, name="HP load for Households")
        # P2G load at bus = 12
        pp.create_load(self.net, bus=12, p_mw=0, name="P2G load")

        # -------------------------- Create Gas gen at bus 12 --------------------------
        pp.create_gen(self.net, bus=12, p_mw=self.x_gen_bus_12_mw, vm_pu=1.0,
                      name="Gas Power bus 37")  # Peak load = 29.3 MW
        # Gas gen at bus 1
        pp.create_gen(self.net, bus=1, p_mw=self.x_gen_bus_1_mw, vm_pu=1.0,
                      name="Gas Power bus 37")  # Peak load = 20.8 MW
        # print(self.net.gen)

        # --------------------------PV, WT & CHP --------------------------
        # Create sgens (PV+WT) at each of the specified x_bus-bar with initial p_mw = 0
        x_pv_bus = self.x_pv_bus
        # PV
        for bus in x_pv_bus:
            pp.create_sgen(self.net, bus=bus, p_mw=0, q_mvar=0, name="PV")
        # WT
        x_wt_bus = self.x_wt_bus
        for bus in x_wt_bus:
            pp.create_sgen(self.net, bus=bus, p_mw=0, q_mvar=0, name="WT")
        # CHP
        x_chp_bus = self.chp_bus
        pp.create_sgen(self.net, bus=x_chp_bus, p_mw=0, q_mvar=0, name="CHP")

        # ----------------------------------------- Create BESS -----------------------------------------
        pp.create_storage(self.net, bus=self.bess_bus, p_mw=0, max_e_mwh=self.bess_p_mw * 12 * 0.9,
                          soc_percent=0.5, name="BESS")
        # print(self.net.storage)

        bess_mw = self.bess_p_mw  # this is already for 1 hour = MWh for each battery
        bess_mwh = self.bess_p_mw * 1  # C rate = 1 = max capacity charge and discharge in 1 hr.
        bess_soc = 0.1

        bess_init_mwh = bess_mwh * bess_soc
        bess_update_mwh = bess_init_mwh
        # print("current_bess_energy", bess_update_mwh)

        # CHANGE: >>>>>>>>>-- change e_demand, irradiance, WIND profile, heat_demand: >>>>>>>>
        for i, ((load_idx, load_row), (irradiance_idx, irradiance_row)) in \
                enumerate(zip(e_demand_2032_jan.iterrows(),
                              df_irradiance_jan.iterrows())):

            # ********************* Update the load values at the specified buses *********************
            # Ind, comm and res loads
            self.net.load.at[0, 'p_mw'] = load_row['LG 01']  # Assuming Chem Industry Load 1 is at index 0
            self.net.load.at[1, 'p_mw'] = load_row[
                'LG 07']  # Peak load = 29.3 MW - Chem Industry Load 2 is at index 1
            self.net.load.at[2, 'p_mw'] = load_row['LG 03']  # Medium industry
            self.net.load.at[3, 'p_mw'] = load_row['small_ind_load_1']
            self.net.load.at[4, 'p_mw'] = load_row['small_ind_load_2']
            # Commercial loads
            self.net.load.at[5, 'p_mw'] = load_row['load_bus3']  # load at bus3
            self.net.load.at[6, 'p_mw'] = load_row['load_bus4']
            self.net.load.at[7, 'p_mw'] = load_row['load_bus5']
            self.net.load.at[8, 'p_mw'] = load_row['load_bus9']
            self.net.load.at[9, 'p_mw'] = load_row['load_bus10']
            self.net.load.at[10, 'p_mw'] = load_row['load_bus11']
            # Household load
            self.net.load.at[11, 'p_mw'] = load_row['load_bus6']  # *10 around 38*10 households

            # ************************ Special loads & heat demand **************************
            # <<<<< ------------------------ Change Heat Demand ---------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # HP load @ Household bus
            self.net.load.at[12, 'p_mw'] = heat_demand_2032_jan['th_load_38_household'][i]
            # P2G at bus = 12
            self.net.load.at[13, 'p_mw'] = self.p2g_input_mw

            # print(self.net.load)

            # *************************** PV ***************************
            # print(self.x_pv_mw[0])
            self.net.sgen.at[0, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[0]  # Assuming PV 1 is at index 0
            self.net.sgen.at[1, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[1]
            self.net.sgen.at[2, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[2]
            self.net.sgen.at[3, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[3]
            self.net.sgen.at[4, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[4]
            self.net.sgen.at[5, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[5]
            self.net.sgen.at[6, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[6]
            self.net.sgen.at[7, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[7]
            self.net.sgen.at[8, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[8]
            self.net.sgen.at[9, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[9]
            self.net.sgen.at[10, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[10]
            self.net.sgen.at[11, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[11]
            self.net.sgen.at[12, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[12]
            self.net.sgen.at[13, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[13]

            # *************************** WT ***************************
            # >>>>>>>>>>>>>>>>>>>>>>> ----- CHANGE WT time series ----- >>>>>>>>>>>>>>>>>>>>
            self.net.sgen.at[14, 'p_mw'] = wind_time_series['wind_normalized_jan'][i] * self.x_wt_mw
            # Assuming WT 1 is at index 14

            # *************************** CHP ***************************
            self.net.sgen.at[15, 'p_mw'] = self.chp_p_mw
            # print(self.net.sgen)

            # ***************************** BESS *******************************************
            # print("bess_mw", bess_mw)
            bess = BESS(net=self.net, sgen_mwh=self.net.sgen['p_mw'].sum(),
                        demand_e_mwh=self.net.load['p_mw'].sum(),
                        bess_mw=bess_mw,
                        bess_mwh=bess_mwh,
                        # bess_soc=bess_soc,
                        # current_energy=bess_current_energy,
                        # bess_max_energy=bess_max_energy,
                        # bess_min_energy=bess_min_energy,
                        bess_update_mwh=bess_update_mwh)
            res_bess_mw = bess.bms_update()[0]
            res_bess_mwh = bess.bms_update()[1]
            res_bess_power_loss_mwh = bess.bms_update()[2]
            res_bess_power_deficit_mwh = bess.bms_update()[3]

            self.net.storage.at[0, 'p_mw'] = res_bess_mw
            # bess_mw_update += res_bess_mwh
            bess_update_mwh = res_bess_mwh
            # print("bess_mw_update =", bess_mw_update)
            # print(self.net.storage)

            pp.runpp(self.net)

            result = {
                # 'time_step': i,
                'demand_mw': self.net.res_load.p_mw.sum(),  # summing the total load at each hour (t)
                'line_loss_mw': self.net.res_line.pl_mw.values[0],
                'gas_gen_mw': self.net.res_gen.p_mw.sum(),
                'pv_wt_chp_mw': self.net.res_sgen.p_mw.sum(),  # summing the total PV gen at each hour (t)
                'bess_mw': self.net.res_storage.p_mw.sum(),
                'ext_grid_mw': self.net.res_ext_grid.p_mw.values[0],
                'bess_mwh': res_bess_mwh
                # 'res_bess_power_loss_mwh': res_bess_power_loss_mwh,
                # 'res_bess_power_deficit_mwh': res_bess_power_deficit_mwh
            }

            for bus_idx in self.net.bus.index:
                result[f'bus_{int(bus_idx)}_voltage_pu'] = self.net.res_bus.vm_pu[bus_idx]

            results = results.append(result, ignore_index=True)
        # print(results)
        return results

    # ---------------------------------------------- 2032 July ----------------------------------------------
    # NOTE: Data input to change: 1. e_demand (Jan/July), 2. PV irradiance & WIND profile  3. heat_demand (Jan/July)
    def power_flow_2032_jul(self):
        results = pd.DataFrame()
        # -------------------------- Create loads on the fixed bus bars with 0 p_mw --------------------------
        pp.create_load(self.net, bus=1, p_mw=0, name="Chem Ind Load 1")
        pp.create_load(self.net, bus=12, p_mw=0, name="Chem Ind Load 2")
        pp.create_load(self.net, bus=2, p_mw=0, name="Medium Ind Load 1")
        pp.create_load(self.net, bus=13, p_mw=0, name="Small Ind Load 1")
        pp.create_load(self.net, bus=14, p_mw=0, name="Small Ind Load 2")
        # Commercial loads
        pp.create_load(self.net, bus=3, p_mw=0, name="Commercial load 1")
        pp.create_load(self.net, bus=4, p_mw=0, name="Commercial load 2")
        pp.create_load(self.net, bus=5, p_mw=0, name="Commercial load 3")
        pp.create_load(self.net, bus=9, p_mw=0, name="Commercial load 4")
        pp.create_load(self.net, bus=10, p_mw=0, name="Commercial load 5")
        pp.create_load(self.net, bus=11, p_mw=0, name="Commercial load 6")
        # Household load
        pp.create_load(self.net, bus=6, p_mw=0, name="Household load")  # 38 households

        # -------------------------- Special loads --------------------------
        # HP load at household bus
        pp.create_load(self.net, bus=6, p_mw=0, name="HP load for Households")
        # P2G load at bus = 12
        pp.create_load(self.net, bus=12, p_mw=0, name="P2G load")

        # -------------------------- Create Gas gen at bus 12 --------------------------
        pp.create_gen(self.net, bus=12, p_mw=self.x_gen_bus_12_mw, vm_pu=1.0,
                      name="Gas Power bus 37")  # Peak load = 29.3 MW
        # Gas gen at bus 1
        pp.create_gen(self.net, bus=1, p_mw=self.x_gen_bus_1_mw, vm_pu=1.0,
                      name="Gas Power bus 37")  # Peak load = 20.8 MW
        # print(self.net.gen)

        # -------------------------- PV, WT & CHP --------------------------
        # Create sgens (PV+WT) at each of the specified x_bus-bar with initial p_mw = 0
        x_pv_bus = self.x_pv_bus
        # PV
        for bus in x_pv_bus:
            pp.create_sgen(self.net, bus=bus, p_mw=0, q_mvar=0, name="PV")
        # WT
        x_wt_bus = self.x_wt_bus
        for bus in x_wt_bus:
            pp.create_sgen(self.net, bus=bus, p_mw=0, q_mvar=0, name="WT")
        # CHP
        x_chp_bus = self.chp_bus
        pp.create_sgen(self.net, bus=x_chp_bus, p_mw=0, q_mvar=0, name="CHP")

        # ----------------------------------------- Create BESS -----------------------------------------
        pp.create_storage(self.net, bus=self.bess_bus, p_mw=0, max_e_mwh=self.bess_p_mw * 12 * 0.9,
                          soc_percent=0.5, name="BESS")
        # print(self.net.storage)

        bess_mw = self.bess_p_mw  # this is already for 1 hour = MWh for each battery
        bess_mwh = self.bess_p_mw * 1  # C rate = 1 = max capacity charge and discharge in 1 hr.
        bess_soc = 0.1

        bess_init_mwh = bess_mwh * bess_soc
        bess_update_mwh = bess_init_mwh
        # print("current_bess_energy", bess_update_mwh)

        # <<<<<< ---- Note: change e_demand, irradiance, heat_demand & WIND profile: ----- >>>>>>>>>>>>
        for i, ((load_idx, load_row), (irradiance_idx, irradiance_row)) in \
                enumerate(zip(e_demand_2032_jul.iterrows(),
                              df_irradiance_jul.iterrows())):

            # ********************* Update the load values at the specified buses *********************
            # Ind, comm and res loads
            self.net.load.at[0, 'p_mw'] = load_row['LG 01']  # Assuming Chem Industry Load 1 is at index 0
            self.net.load.at[1, 'p_mw'] = load_row[
                'LG 07']  # Peak load = 29.3 MW - Chem Industry Load 2 is at index 1
            self.net.load.at[2, 'p_mw'] = load_row['LG 03']  # Medium industry
            self.net.load.at[3, 'p_mw'] = load_row['small_ind_load_1']
            self.net.load.at[4, 'p_mw'] = load_row['small_ind_load_2']
            # Commercial loads
            self.net.load.at[5, 'p_mw'] = load_row['load_bus3']  # load at bus3
            self.net.load.at[6, 'p_mw'] = load_row['load_bus4']
            self.net.load.at[7, 'p_mw'] = load_row['load_bus5']
            self.net.load.at[8, 'p_mw'] = load_row['load_bus9']
            self.net.load.at[9, 'p_mw'] = load_row['load_bus10']
            self.net.load.at[10, 'p_mw'] = load_row['load_bus11']
            # Household load
            self.net.load.at[11, 'p_mw'] = load_row['load_bus6']  # *10 around 38*10 households

            # ************************ Special loads & heat demand **************************
            # <<<<<<<<<<<<<< ------------------ Change Heat Demand -------------- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # HP load @ Household bus
            self.net.load.at[12, 'p_mw'] = heat_demand_2032_jul['th_load_38_household'][i]
            # P2G at bus = 12
            self.net.load.at[13, 'p_mw'] = self.p2g_input_mw

            # print(self.net.load)

            # *************************** PV ***************************
            # print(self.x[14])
            # print(self.x_pv_mw[0])
            self.net.sgen.at[0, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[0]  # Assuming PV 1 is at index 0
            self.net.sgen.at[1, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[1]
            self.net.sgen.at[2, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[2]
            self.net.sgen.at[3, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[3]
            self.net.sgen.at[4, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[4]
            self.net.sgen.at[5, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[5]
            self.net.sgen.at[6, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[6]
            self.net.sgen.at[7, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[7]
            self.net.sgen.at[8, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[8]
            self.net.sgen.at[9, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[9]
            self.net.sgen.at[10, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[10]
            self.net.sgen.at[11, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[11]
            self.net.sgen.at[12, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[12]
            self.net.sgen.at[13, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[13]

            # *************************** WT ***************************
            # # >>>>>>>>>>>>>>>>>>>>>>> ----- CHANGE WT time series ----- >>>>>>>>>>>>>>>>>>>>
            self.net.sgen.at[14, 'p_mw'] = wind_time_series['wind_normalized_jul'][i] * self.x_wt_mw
            # Assuming WT 1 is at index 14

            # *************************** CHP ***************************
            self.net.sgen.at[15, 'p_mw'] = self.chp_p_mw
            # print(self.net.sgen)

            # ***************************** BESS *******************************************
            bess = BESS(net=self.net, sgen_mwh=self.net.sgen['p_mw'].sum(),
                        demand_e_mwh=self.net.load['p_mw'].sum(),
                        bess_mw=bess_mw,
                        bess_mwh=bess_mwh,
                        # bess_soc=bess_soc,
                        # current_energy=bess_current_energy,
                        # bess_max_energy=bess_max_energy,
                        # bess_min_energy=bess_min_energy,
                        bess_update_mwh=bess_update_mwh)
            res_bess_mw = bess.bms_update()[0]
            res_bess_mwh = bess.bms_update()[1]
            res_bess_power_loss_mwh = bess.bms_update()[2]
            res_bess_power_deficit_mwh = bess.bms_update()[3]

            self.net.storage.at[0, 'p_mw'] = res_bess_mw
            # bess_mw_update += res_bess_mwh
            bess_update_mwh = res_bess_mwh
            # print("bess_mw_update =", bess_mw_update)
            # print(self.net.storage)

            pp.runpp(self.net)

            result = {
                # 'time_step': i,
                'demand_mw': self.net.res_load.p_mw.sum(),  # summing the total load at each hour (t)
                'line_loss_mw': self.net.res_line.pl_mw.values[0],
                'gas_gen_mw': self.net.res_gen.p_mw.sum(),
                'pv_wt_chp_mw': self.net.res_sgen.p_mw.sum(),  # summing the total PV gen at each hour (t)
                'bess_mw': self.net.res_storage.p_mw.sum(),
                'ext_grid_mw': self.net.res_ext_grid.p_mw.values[0],
                'bess_mwh': res_bess_mwh
                # 'res_bess_power_loss_mwh': res_bess_power_loss_mwh,
                # 'res_bess_power_deficit_mwh': res_bess_power_deficit_mwh
            }

            for bus_idx in self.net.bus.index:
                result[f'bus_{int(bus_idx)}_voltage_pu'] = self.net.res_bus.vm_pu[bus_idx]

            results = results.append(result, ignore_index=True)

        return results

    # =================================================== 2033 Jan ===================================================
    # NOTE: Data input to change: 1. e_demand (Jan/July), 2. PV irradiance & WIND profile  3. heat_demand (Jan/July)
    def power_flow_2033_jan(self):

        results = pd.DataFrame()

        # -------------------------- Create loads on the fixed bus bars with 0 p_mw --------------------------
        pp.create_load(self.net, bus=1, p_mw=0, name="Chem Ind Load 1")
        pp.create_load(self.net, bus=12, p_mw=0, name="Chem Ind Load 2")
        pp.create_load(self.net, bus=2, p_mw=0, name="Medium Ind Load 1")
        pp.create_load(self.net, bus=13, p_mw=0, name="Small Ind Load 1")
        pp.create_load(self.net, bus=14, p_mw=0, name="Small Ind Load 2")
        # Commercial loads
        pp.create_load(self.net, bus=3, p_mw=0, name="Commercial load 1")
        pp.create_load(self.net, bus=4, p_mw=0, name="Commercial load 2")
        pp.create_load(self.net, bus=5, p_mw=0, name="Commercial load 3")
        pp.create_load(self.net, bus=9, p_mw=0, name="Commercial load 4")
        pp.create_load(self.net, bus=10, p_mw=0, name="Commercial load 5")
        pp.create_load(self.net, bus=11, p_mw=0, name="Commercial load 6")
        # Household load
        pp.create_load(self.net, bus=6, p_mw=0, name="Household load")  # 38 households

        # --------------------------Special loads --------------------------
        # HP load at household bus
        pp.create_load(self.net, bus=6, p_mw=0, name="HP load for Households")
        # P2G load at bus = 12
        pp.create_load(self.net, bus=12, p_mw=0, name="P2G load")

        # -------------------------- Create Gas gen at bus 12 --------------------------
        pp.create_gen(self.net, bus=12, p_mw=self.x_gen_bus_12_mw, vm_pu=1.0,
                      name="Gas Power bus 37")  # Peak load = 29.3 MW
        # Gas gen at bus 1
        pp.create_gen(self.net, bus=1, p_mw=self.x_gen_bus_1_mw, vm_pu=1.0,
                      name="Gas Power bus 37")  # Peak load = 20.8 MW
        # print(self.net.gen)

        # --------------------------PV, WT & CHP --------------------------
        # Create sgens (PV+WT) at each of the specified x_bus-bar with initial p_mw = 0
        x_pv_bus = self.x_pv_bus
        # PV
        for bus in x_pv_bus:
            pp.create_sgen(self.net, bus=bus, p_mw=0, q_mvar=0, name="PV")
        # WT
        x_wt_bus = self.x_wt_bus
        for bus in x_wt_bus:
            pp.create_sgen(self.net, bus=bus, p_mw=0, q_mvar=0, name="WT")
        # CHP
        x_chp_bus = self.chp_bus
        pp.create_sgen(self.net, bus=x_chp_bus, p_mw=0, q_mvar=0, name="CHP")

        # ----------------------------------------- Create BESS -----------------------------------------
        pp.create_storage(self.net, bus=self.bess_bus, p_mw=0, max_e_mwh=self.bess_p_mw * 12 * 0.9,
                          soc_percent=0.5, name="BESS")
        # print(self.net.storage)

        bess_mw = self.bess_p_mw  # this is already for 1 hour = MWh for each battery
        bess_mwh = self.bess_p_mw * 1  # C rate = 1 = max capacity charge and discharge in 1 hr.
        bess_soc = 0.1

        bess_init_mwh = bess_mwh * bess_soc
        bess_update_mwh = bess_init_mwh
        # print("current_bess_energy", bess_update_mwh)

        # CHANGE: >>>>>>>>>-- change e_demand, irradiance, WIND profile, heat_demand: >>>>>>>>
        for i, ((load_idx, load_row), (irradiance_idx, irradiance_row)) in \
                enumerate(zip(e_demand_2033_jan.iterrows(),
                              df_irradiance_jan.iterrows())):

            # ********************* Update the load values at the specified buses *********************
            # Ind, comm and res loads
            self.net.load.at[0, 'p_mw'] = load_row['LG 01']  # Assuming Chem Industry Load 1 is at index 0
            self.net.load.at[1, 'p_mw'] = load_row[
                'LG 07']  # Peak load = 29.3 MW - Chem Industry Load 2 is at index 1
            self.net.load.at[2, 'p_mw'] = load_row['LG 03']  # Medium industry
            self.net.load.at[3, 'p_mw'] = load_row['small_ind_load_1']
            self.net.load.at[4, 'p_mw'] = load_row['small_ind_load_2']
            # Commercial loads
            self.net.load.at[5, 'p_mw'] = load_row['load_bus3']  # load at bus3
            self.net.load.at[6, 'p_mw'] = load_row['load_bus4']
            self.net.load.at[7, 'p_mw'] = load_row['load_bus5']
            self.net.load.at[8, 'p_mw'] = load_row['load_bus9']
            self.net.load.at[9, 'p_mw'] = load_row['load_bus10']
            self.net.load.at[10, 'p_mw'] = load_row['load_bus11']
            # Household load
            self.net.load.at[11, 'p_mw'] = load_row['load_bus6']  # *10 around 38*10 households

            # ************************ Special loads & heat demand **************************
            # <<<<< ------------------------ Change Heat Demand ---------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # HP load @ Household bus
            self.net.load.at[12, 'p_mw'] = heat_demand_2033_jan['th_load_38_household'][i]
            # P2G at bus = 12
            self.net.load.at[13, 'p_mw'] = self.p2g_input_mw

            # print(self.net.load)

            # *************************** PV ***************************
            # print(self.x_pv_mw[0])
            self.net.sgen.at[0, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[0]  # Assuming PV 1 is at index 0
            self.net.sgen.at[1, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[1]
            self.net.sgen.at[2, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[2]
            self.net.sgen.at[3, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[3]
            self.net.sgen.at[4, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[4]
            self.net.sgen.at[5, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[5]
            self.net.sgen.at[6, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[6]
            self.net.sgen.at[7, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[7]
            self.net.sgen.at[8, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[8]
            self.net.sgen.at[9, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[9]
            self.net.sgen.at[10, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[10]
            self.net.sgen.at[11, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[11]
            self.net.sgen.at[12, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[12]
            self.net.sgen.at[13, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[13]

            # *************************** WT ***************************
            # >>>>>>>>>>>>>>>>>>>>>>> ----- CHANGE WT time series ----- >>>>>>>>>>>>>>>>>>>>
            self.net.sgen.at[14, 'p_mw'] = wind_time_series['wind_normalized_jan'][i] * self.x_wt_mw
            # Assuming WT 1 is at index 14

            # NOTE: NO MORE Changes needed ------>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # *************************** CHP ***************************
            self.net.sgen.at[15, 'p_mw'] = self.chp_p_mw
            # print(self.net.sgen)

            # ***************************** BESS *******************************************
            # print("bess_mw", bess_mw)
            bess = BESS(net=self.net, sgen_mwh=self.net.sgen['p_mw'].sum(),
                        demand_e_mwh=self.net.load['p_mw'].sum(),
                        bess_mw=bess_mw,
                        bess_mwh=bess_mwh,
                        # bess_soc=bess_soc,
                        # current_energy=bess_current_energy,
                        # bess_max_energy=bess_max_energy,
                        # bess_min_energy=bess_min_energy,
                        bess_update_mwh=bess_update_mwh)
            res_bess_mw = bess.bms_update()[0]
            res_bess_mwh = bess.bms_update()[1]
            res_bess_power_loss_mwh = bess.bms_update()[2]
            res_bess_power_deficit_mwh = bess.bms_update()[3]

            self.net.storage.at[0, 'p_mw'] = res_bess_mw
            # bess_mw_update += res_bess_mwh
            bess_update_mwh = res_bess_mwh
            # print("bess_mw_update =", bess_mw_update)
            # print(self.net.storage)

            pp.runpp(self.net)

            result = {
                # 'time_step': i,
                'demand_mw': self.net.res_load.p_mw.sum(),  # summing the total load at each hour (t)
                'line_loss_mw': self.net.res_line.pl_mw.values[0],
                'gas_gen_mw': self.net.res_gen.p_mw.sum(),
                'pv_wt_chp_mw': self.net.res_sgen.p_mw.sum(),  # summing the total PV gen at each hour (t)
                'bess_mw': self.net.res_storage.p_mw.sum(),
                'ext_grid_mw': self.net.res_ext_grid.p_mw.values[0],
                'bess_mwh': res_bess_mwh
                # 'res_bess_power_loss_mwh': res_bess_power_loss_mwh,
                # 'res_bess_power_deficit_mwh': res_bess_power_deficit_mwh
            }

            for bus_idx in self.net.bus.index:
                result[f'bus_{int(bus_idx)}_voltage_pu'] = self.net.res_bus.vm_pu[bus_idx]

            results = results.append(result, ignore_index=True)
        # print(results)
        return results

    # ---------------------------------------------- 2033 July ----------------------------------------------
    # NOTE: Data input to change: 1. e_demand (Jan/July), 2. PV irradiance & WIND profile  3. heat_demand (Jan/July)
    def power_flow_2033_jul(self):
        results = pd.DataFrame()
        # -------------------------- Create loads on the fixed bus bars with 0 p_mw --------------------------
        pp.create_load(self.net, bus=1, p_mw=0, name="Chem Ind Load 1")
        pp.create_load(self.net, bus=12, p_mw=0, name="Chem Ind Load 2")
        pp.create_load(self.net, bus=2, p_mw=0, name="Medium Ind Load 1")
        pp.create_load(self.net, bus=13, p_mw=0, name="Small Ind Load 1")
        pp.create_load(self.net, bus=14, p_mw=0, name="Small Ind Load 2")
        # Commercial loads
        pp.create_load(self.net, bus=3, p_mw=0, name="Commercial load 1")
        pp.create_load(self.net, bus=4, p_mw=0, name="Commercial load 2")
        pp.create_load(self.net, bus=5, p_mw=0, name="Commercial load 3")
        pp.create_load(self.net, bus=9, p_mw=0, name="Commercial load 4")
        pp.create_load(self.net, bus=10, p_mw=0, name="Commercial load 5")
        pp.create_load(self.net, bus=11, p_mw=0, name="Commercial load 6")
        # Household load
        pp.create_load(self.net, bus=6, p_mw=0, name="Household load")  # 38 households

        # -------------------------- Special loads --------------------------
        # HP load at household bus
        pp.create_load(self.net, bus=6, p_mw=0, name="HP load for Households")
        # P2G load at bus = 12
        pp.create_load(self.net, bus=12, p_mw=0, name="P2G load")

        # -------------------------- Create Gas gen at bus 12 --------------------------
        pp.create_gen(self.net, bus=12, p_mw=self.x_gen_bus_12_mw, vm_pu=1.0,
                      name="Gas Power bus 37")  # Peak load = 29.3 MW
        # Gas gen at bus 1
        pp.create_gen(self.net, bus=1, p_mw=self.x_gen_bus_1_mw, vm_pu=1.0,
                      name="Gas Power bus 37")  # Peak load = 20.8 MW
        # print(self.net.gen)

        # -------------------------- PV, WT & CHP --------------------------
        # Create sgens (PV+WT) at each of the specified x_bus-bar with initial p_mw = 0
        x_pv_bus = self.x_pv_bus
        # PV
        for bus in x_pv_bus:
            pp.create_sgen(self.net, bus=bus, p_mw=0, q_mvar=0, name="PV")
        # WT
        x_wt_bus = self.x_wt_bus
        for bus in x_wt_bus:
            pp.create_sgen(self.net, bus=bus, p_mw=0, q_mvar=0, name="WT")
        # CHP
        x_chp_bus = self.chp_bus
        pp.create_sgen(self.net, bus=x_chp_bus, p_mw=0, q_mvar=0, name="CHP")

        # ----------------------------------------- Create BESS -----------------------------------------
        pp.create_storage(self.net, bus=self.bess_bus, p_mw=0, max_e_mwh=self.bess_p_mw * 12 * 0.9,
                          soc_percent=0.5, name="BESS")
        # print(self.net.storage)

        bess_mw = self.bess_p_mw  # this is already for 1 hour = MWh for each battery
        bess_mwh = self.bess_p_mw * 1  # C rate = 1 = max capacity charge and discharge in 1 hr.
        bess_soc = 0.1

        bess_init_mwh = bess_mwh * bess_soc
        bess_update_mwh = bess_init_mwh
        # print("current_bess_energy", bess_update_mwh)

        # <<<<<< ---- Note: change e_demand, irradiance, heat_demand & WIND profile: ----- >>>>>>>>>>>>
        for i, ((load_idx, load_row), (irradiance_idx, irradiance_row)) in \
                enumerate(zip(e_demand_2033_jul.iterrows(),
                              df_irradiance_jul.iterrows())):

            # ********************* Update the load values at the specified buses *********************
            # Ind, comm and res loads
            self.net.load.at[0, 'p_mw'] = load_row['LG 01']  # Assuming Chem Industry Load 1 is at index 0
            self.net.load.at[1, 'p_mw'] = load_row[
                'LG 07']  # Peak load = 29.3 MW - Chem Industry Load 2 is at index 1
            self.net.load.at[2, 'p_mw'] = load_row['LG 03']  # Medium industry
            self.net.load.at[3, 'p_mw'] = load_row['small_ind_load_1']
            self.net.load.at[4, 'p_mw'] = load_row['small_ind_load_2']
            # Commercial loads
            self.net.load.at[5, 'p_mw'] = load_row['load_bus3']  # load at bus3
            self.net.load.at[6, 'p_mw'] = load_row['load_bus4']
            self.net.load.at[7, 'p_mw'] = load_row['load_bus5']
            self.net.load.at[8, 'p_mw'] = load_row['load_bus9']
            self.net.load.at[9, 'p_mw'] = load_row['load_bus10']
            self.net.load.at[10, 'p_mw'] = load_row['load_bus11']
            # Household load
            self.net.load.at[11, 'p_mw'] = load_row['load_bus6']  # *10 around 38*10 households

            # ************************ Special loads & heat demand **************************
            # <<<<<<<<<<<<<< ------------------ Change Heat Demand -------------- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # HP load @ Household bus
            self.net.load.at[12, 'p_mw'] = heat_demand_2033_jul['th_load_38_household'][i]
            # P2G at bus = 12
            self.net.load.at[13, 'p_mw'] = self.p2g_input_mw

            # print(self.net.load)

            # *************************** PV ***************************
            # print(self.x[14])
            # print(self.x_pv_mw[0])
            self.net.sgen.at[0, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[0]  # Assuming PV 1 is at index 0
            self.net.sgen.at[1, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[1]
            self.net.sgen.at[2, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[2]
            self.net.sgen.at[3, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[3]
            self.net.sgen.at[4, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[4]
            self.net.sgen.at[5, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[5]
            self.net.sgen.at[6, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[6]
            self.net.sgen.at[7, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[7]
            self.net.sgen.at[8, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[8]
            self.net.sgen.at[9, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[9]
            self.net.sgen.at[10, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[10]
            self.net.sgen.at[11, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[11]
            self.net.sgen.at[12, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[12]
            self.net.sgen.at[13, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[13]

            # *************************** WT ***************************
            # # >>>>>>>>>>>>>>>>>>>>>>> ----- CHANGE WT time series ----- >>>>>>>>>>>>>>>>>>>>
            self.net.sgen.at[14, 'p_mw'] = wind_time_series['wind_normalized_jul'][i] * self.x_wt_mw
            # Assuming WT 1 is at index 14

            # NOTE: NO MORE Changes needed ------>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # *************************** CHP ***************************
            self.net.sgen.at[15, 'p_mw'] = self.chp_p_mw
            # print(self.net.sgen)

            # ***************************** BESS *******************************************
            bess = BESS(net=self.net, sgen_mwh=self.net.sgen['p_mw'].sum(),
                        demand_e_mwh=self.net.load['p_mw'].sum(),
                        bess_mw=bess_mw,
                        bess_mwh=bess_mwh,
                        # bess_soc=bess_soc,
                        # current_energy=bess_current_energy,
                        # bess_max_energy=bess_max_energy,
                        # bess_min_energy=bess_min_energy,
                        bess_update_mwh=bess_update_mwh)
            res_bess_mw = bess.bms_update()[0]
            res_bess_mwh = bess.bms_update()[1]
            res_bess_power_loss_mwh = bess.bms_update()[2]
            res_bess_power_deficit_mwh = bess.bms_update()[3]

            self.net.storage.at[0, 'p_mw'] = res_bess_mw
            # bess_mw_update += res_bess_mwh
            bess_update_mwh = res_bess_mwh
            # print("bess_mw_update =", bess_mw_update)
            # print(self.net.storage)

            pp.runpp(self.net)

            result = {
                # 'time_step': i,
                'demand_mw': self.net.res_load.p_mw.sum(),  # summing the total load at each hour (t)
                'line_loss_mw': self.net.res_line.pl_mw.values[0],
                'gas_gen_mw': self.net.res_gen.p_mw.sum(),
                'pv_wt_chp_mw': self.net.res_sgen.p_mw.sum(),  # summing the total PV gen at each hour (t)
                'bess_mw': self.net.res_storage.p_mw.sum(),
                'ext_grid_mw': self.net.res_ext_grid.p_mw.values[0],
                'bess_mwh': res_bess_mwh
                # 'res_bess_power_loss_mwh': res_bess_power_loss_mwh,
                # 'res_bess_power_deficit_mwh': res_bess_power_deficit_mwh
            }

            for bus_idx in self.net.bus.index:
                result[f'bus_{int(bus_idx)}_voltage_pu'] = self.net.res_bus.vm_pu[bus_idx]

            results = results.append(result, ignore_index=True)

        return results

    # =================================================== 2034 Jan ===================================================
    # NOTE: Data input to change: 1. e_demand (Jan/July), 2. PV irradiance & WIND profile  3. heat_demand (Jan/July)
    def power_flow_2034_jan(self):

        results = pd.DataFrame()

        # -------------------------- Create loads on the fixed bus bars with 0 p_mw --------------------------
        pp.create_load(self.net, bus=1, p_mw=0, name="Chem Ind Load 1")
        pp.create_load(self.net, bus=12, p_mw=0, name="Chem Ind Load 2")
        pp.create_load(self.net, bus=2, p_mw=0, name="Medium Ind Load 1")
        pp.create_load(self.net, bus=13, p_mw=0, name="Small Ind Load 1")
        pp.create_load(self.net, bus=14, p_mw=0, name="Small Ind Load 2")
        # Commercial loads
        pp.create_load(self.net, bus=3, p_mw=0, name="Commercial load 1")
        pp.create_load(self.net, bus=4, p_mw=0, name="Commercial load 2")
        pp.create_load(self.net, bus=5, p_mw=0, name="Commercial load 3")
        pp.create_load(self.net, bus=9, p_mw=0, name="Commercial load 4")
        pp.create_load(self.net, bus=10, p_mw=0, name="Commercial load 5")
        pp.create_load(self.net, bus=11, p_mw=0, name="Commercial load 6")
        # Household load
        pp.create_load(self.net, bus=6, p_mw=0, name="Household load")  # 38 households

        # --------------------------Special loads --------------------------
        # HP load at household bus
        pp.create_load(self.net, bus=6, p_mw=0, name="HP load for Households")
        # P2G load at bus = 12
        pp.create_load(self.net, bus=12, p_mw=0, name="P2G load")

        # -------------------------- Create Gas gen at bus 12 --------------------------
        pp.create_gen(self.net, bus=12, p_mw=self.x_gen_bus_12_mw, vm_pu=1.0,
                      name="Gas Power bus 37")  # Peak load = 29.3 MW
        # Gas gen at bus 1
        pp.create_gen(self.net, bus=1, p_mw=self.x_gen_bus_1_mw, vm_pu=1.0,
                      name="Gas Power bus 37")  # Peak load = 20.8 MW
        # print(self.net.gen)

        # --------------------------PV, WT & CHP --------------------------
        # Create sgens (PV+WT) at each of the specified x_bus-bar with initial p_mw = 0
        x_pv_bus = self.x_pv_bus
        # PV
        for bus in x_pv_bus:
            pp.create_sgen(self.net, bus=bus, p_mw=0, q_mvar=0, name="PV")
        # WT
        x_wt_bus = self.x_wt_bus
        for bus in x_wt_bus:
            pp.create_sgen(self.net, bus=bus, p_mw=0, q_mvar=0, name="WT")
        # CHP
        x_chp_bus = self.chp_bus
        pp.create_sgen(self.net, bus=x_chp_bus, p_mw=0, q_mvar=0, name="CHP")

        # ----------------------------------------- Create BESS -----------------------------------------
        pp.create_storage(self.net, bus=self.bess_bus, p_mw=0, max_e_mwh=self.bess_p_mw * 12 * 0.9,
                          soc_percent=0.5, name="BESS")
        # print(self.net.storage)

        bess_mw = self.bess_p_mw  # this is already for 1 hour = MWh for each battery
        bess_mwh = self.bess_p_mw * 1  # C rate = 1 = max capacity charge and discharge in 1 hr.
        bess_soc = 0.1

        bess_init_mwh = bess_mwh * bess_soc
        bess_update_mwh = bess_init_mwh
        # print("current_bess_energy", bess_update_mwh)

        # CHANGE: >>>>>>>>>-- change e_demand, irradiance, WIND profile, heat_demand: >>>>>>>>
        for i, ((load_idx, load_row), (irradiance_idx, irradiance_row)) in \
                enumerate(zip(e_demand_2034_jan.iterrows(),
                              df_irradiance_jan.iterrows())):

            # ********************* Update the load values at the specified buses *********************
            # Ind, comm and res loads
            self.net.load.at[0, 'p_mw'] = load_row['LG 01']  # Assuming Chem Industry Load 1 is at index 0
            self.net.load.at[1, 'p_mw'] = load_row[
                'LG 07']  # Peak load = 29.3 MW - Chem Industry Load 2 is at index 1
            self.net.load.at[2, 'p_mw'] = load_row['LG 03']  # Medium industry
            self.net.load.at[3, 'p_mw'] = load_row['small_ind_load_1']
            self.net.load.at[4, 'p_mw'] = load_row['small_ind_load_2']
            # Commercial loads
            self.net.load.at[5, 'p_mw'] = load_row['load_bus3']  # load at bus3
            self.net.load.at[6, 'p_mw'] = load_row['load_bus4']
            self.net.load.at[7, 'p_mw'] = load_row['load_bus5']
            self.net.load.at[8, 'p_mw'] = load_row['load_bus9']
            self.net.load.at[9, 'p_mw'] = load_row['load_bus10']
            self.net.load.at[10, 'p_mw'] = load_row['load_bus11']
            # Household load
            self.net.load.at[11, 'p_mw'] = load_row['load_bus6']  # *10 around 38*10 households

            # ************************ Special loads & heat demand **************************
            # <<<<< ------------------------ Change Heat Demand ---------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # HP load @ Household bus
            self.net.load.at[12, 'p_mw'] = heat_demand_2034_jan['th_load_38_household'][i]
            # P2G at bus = 12
            self.net.load.at[13, 'p_mw'] = self.p2g_input_mw

            # print(self.net.load)

            # *************************** PV ***************************
            # print(self.x_pv_mw[0])
            self.net.sgen.at[0, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[0]  # Assuming PV 1 is at index 0
            self.net.sgen.at[1, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[1]
            self.net.sgen.at[2, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[2]
            self.net.sgen.at[3, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[3]
            self.net.sgen.at[4, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[4]
            self.net.sgen.at[5, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[5]
            self.net.sgen.at[6, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[6]
            self.net.sgen.at[7, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[7]
            self.net.sgen.at[8, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[8]
            self.net.sgen.at[9, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[9]
            self.net.sgen.at[10, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[10]
            self.net.sgen.at[11, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[11]
            self.net.sgen.at[12, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[12]
            self.net.sgen.at[13, 'p_mw'] = irradiance_row['jan'] * self.x_pv_mw[13]

            # *************************** WT ***************************
            # >>>>>>>>>>>>>>>>>>>>>>> ----- CHANGE WT time series ----- >>>>>>>>>>>>>>>>>>>>
            self.net.sgen.at[14, 'p_mw'] = wind_time_series['wind_normalized_jan'][i] * self.x_wt_mw
            # Assuming WT 1 is at index 14

            # NOTE: NO MORE Changes needed ------>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # *************************** CHP ***************************
            self.net.sgen.at[15, 'p_mw'] = self.chp_p_mw
            # print(self.net.sgen)

            # ***************************** BESS *******************************************
            # print("bess_mw", bess_mw)
            bess = BESS(net=self.net, sgen_mwh=self.net.sgen['p_mw'].sum(),
                        demand_e_mwh=self.net.load['p_mw'].sum(),
                        bess_mw=bess_mw,
                        bess_mwh=bess_mwh,
                        # bess_soc=bess_soc,
                        # current_energy=bess_current_energy,
                        # bess_max_energy=bess_max_energy,
                        # bess_min_energy=bess_min_energy,
                        bess_update_mwh=bess_update_mwh)
            res_bess_mw = bess.bms_update()[0]
            res_bess_mwh = bess.bms_update()[1]
            res_bess_power_loss_mwh = bess.bms_update()[2]
            res_bess_power_deficit_mwh = bess.bms_update()[3]

            self.net.storage.at[0, 'p_mw'] = res_bess_mw
            # bess_mw_update += res_bess_mwh
            bess_update_mwh = res_bess_mwh
            # print("bess_mw_update =", bess_mw_update)
            # print(self.net.storage)

            pp.runpp(self.net)

            result = {
                # 'time_step': i,
                'demand_mw': self.net.res_load.p_mw.sum(),  # summing the total load at each hour (t)
                'line_loss_mw': self.net.res_line.pl_mw.values[0],
                'gas_gen_mw': self.net.res_gen.p_mw.sum(),
                'pv_wt_chp_mw': self.net.res_sgen.p_mw.sum(),  # summing the total PV gen at each hour (t)
                'bess_mw': self.net.res_storage.p_mw.sum(),
                'ext_grid_mw': self.net.res_ext_grid.p_mw.values[0],
                'bess_mwh': res_bess_mwh
                # 'res_bess_power_loss_mwh': res_bess_power_loss_mwh,
                # 'res_bess_power_deficit_mwh': res_bess_power_deficit_mwh
            }

            for bus_idx in self.net.bus.index:
                result[f'bus_{int(bus_idx)}_voltage_pu'] = self.net.res_bus.vm_pu[bus_idx]

            results = results.append(result, ignore_index=True)
        # print(results)
        return results

    # ---------------------------------------------- 2034 July ----------------------------------------------
    # NOTE: Data input to change: 1. e_demand (Jan/July), 2. PV irradiance & WIND profile  3. heat_demand (Jan/July)
    def power_flow_2034_jul(self):
        results = pd.DataFrame()
        # -------------------------- Create loads on the fixed bus bars with 0 p_mw --------------------------
        pp.create_load(self.net, bus=1, p_mw=0, name="Chem Ind Load 1")
        pp.create_load(self.net, bus=12, p_mw=0, name="Chem Ind Load 2")
        pp.create_load(self.net, bus=2, p_mw=0, name="Medium Ind Load 1")
        pp.create_load(self.net, bus=13, p_mw=0, name="Small Ind Load 1")
        pp.create_load(self.net, bus=14, p_mw=0, name="Small Ind Load 2")
        # Commercial loads
        pp.create_load(self.net, bus=3, p_mw=0, name="Commercial load 1")
        pp.create_load(self.net, bus=4, p_mw=0, name="Commercial load 2")
        pp.create_load(self.net, bus=5, p_mw=0, name="Commercial load 3")
        pp.create_load(self.net, bus=9, p_mw=0, name="Commercial load 4")
        pp.create_load(self.net, bus=10, p_mw=0, name="Commercial load 5")
        pp.create_load(self.net, bus=11, p_mw=0, name="Commercial load 6")
        # Household load
        pp.create_load(self.net, bus=6, p_mw=0, name="Household load")  # 38 households

        # -------------------------- Special loads --------------------------
        # HP load at household bus
        pp.create_load(self.net, bus=6, p_mw=0, name="HP load for Households")
        # P2G load at bus = 12
        pp.create_load(self.net, bus=12, p_mw=0, name="P2G load")

        # -------------------------- Create Gas gen at bus 12 --------------------------
        pp.create_gen(self.net, bus=12, p_mw=self.x_gen_bus_12_mw, vm_pu=1.0,
                      name="Gas Power bus 37")  # Peak load = 29.3 MW
        # Gas gen at bus 1
        pp.create_gen(self.net, bus=1, p_mw=self.x_gen_bus_1_mw, vm_pu=1.0,
                      name="Gas Power bus 37")  # Peak load = 20.8 MW
        # print(self.net.gen)

        # -------------------------- PV, WT & CHP --------------------------
        # Create sgens (PV+WT) at each of the specified x_bus-bar with initial p_mw = 0
        x_pv_bus = self.x_pv_bus
        # PV
        for bus in x_pv_bus:
            pp.create_sgen(self.net, bus=bus, p_mw=0, q_mvar=0, name="PV")
        # WT
        x_wt_bus = self.x_wt_bus
        for bus in x_wt_bus:
            pp.create_sgen(self.net, bus=bus, p_mw=0, q_mvar=0, name="WT")
        # CHP
        x_chp_bus = self.chp_bus
        pp.create_sgen(self.net, bus=x_chp_bus, p_mw=0, q_mvar=0, name="CHP")

        # ----------------------------------------- Create BESS -----------------------------------------
        pp.create_storage(self.net, bus=self.bess_bus, p_mw=0, max_e_mwh=self.bess_p_mw * 12 * 0.9,
                          soc_percent=0.5, name="BESS")
        # print(self.net.storage)

        bess_mw = self.bess_p_mw  # this is already for 1 hour = MWh for each battery
        bess_mwh = self.bess_p_mw * 1  # C rate = 1 = max capacity charge and discharge in 1 hr.
        bess_soc = 0.1

        bess_init_mwh = bess_mwh * bess_soc
        bess_update_mwh = bess_init_mwh
        # print("current_bess_energy", bess_update_mwh)

        # <<<<<< ---- Note: change e_demand, irradiance, heat_demand & WIND profile: ----- >>>>>>>>>>>>
        for i, ((load_idx, load_row), (irradiance_idx, irradiance_row)) in \
                enumerate(zip(e_demand_2034_jul.iterrows(),
                              df_irradiance_jul.iterrows())):

            # ********************* Update the load values at the specified buses *********************
            # Ind, comm and res loads
            self.net.load.at[0, 'p_mw'] = load_row['LG 01']  # Assuming Chem Industry Load 1 is at index 0
            self.net.load.at[1, 'p_mw'] = load_row[
                'LG 07']  # Peak load = 29.3 MW - Chem Industry Load 2 is at index 1
            self.net.load.at[2, 'p_mw'] = load_row['LG 03']  # Medium industry
            self.net.load.at[3, 'p_mw'] = load_row['small_ind_load_1']
            self.net.load.at[4, 'p_mw'] = load_row['small_ind_load_2']
            # Commercial loads
            self.net.load.at[5, 'p_mw'] = load_row['load_bus3']  # load at bus3
            self.net.load.at[6, 'p_mw'] = load_row['load_bus4']
            self.net.load.at[7, 'p_mw'] = load_row['load_bus5']
            self.net.load.at[8, 'p_mw'] = load_row['load_bus9']
            self.net.load.at[9, 'p_mw'] = load_row['load_bus10']
            self.net.load.at[10, 'p_mw'] = load_row['load_bus11']
            # Household load
            self.net.load.at[11, 'p_mw'] = load_row['load_bus6']  # *10 around 38*10 households

            # ************************ Special loads & heat demand **************************
            # <<<<<<<<<<<<<< ------------------ Change Heat Demand -------------- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # HP load @ Household bus
            self.net.load.at[12, 'p_mw'] = heat_demand_2034_jul['th_load_38_household'][i]
            # P2G at bus = 12
            self.net.load.at[13, 'p_mw'] = self.p2g_input_mw

            # print(self.net.load)

            # *************************** PV ***************************
            # print(self.x[14])
            # print(self.x_pv_mw[0])
            self.net.sgen.at[0, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[0]  # Assuming PV 1 is at index 0
            self.net.sgen.at[1, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[1]
            self.net.sgen.at[2, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[2]
            self.net.sgen.at[3, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[3]
            self.net.sgen.at[4, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[4]
            self.net.sgen.at[5, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[5]
            self.net.sgen.at[6, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[6]
            self.net.sgen.at[7, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[7]
            self.net.sgen.at[8, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[8]
            self.net.sgen.at[9, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[9]
            self.net.sgen.at[10, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[10]
            self.net.sgen.at[11, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[11]
            self.net.sgen.at[12, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[12]
            self.net.sgen.at[13, 'p_mw'] = irradiance_row['jul'] * self.x_pv_mw[13]

            # *************************** WT ***************************
            # # >>>>>>>>>>>>>>>>>>>>>>> ----- CHANGE WT time series ----- >>>>>>>>>>>>>>>>>>>>
            self.net.sgen.at[14, 'p_mw'] = wind_time_series['wind_normalized_jul'][i] * self.x_wt_mw
            # Assuming WT 1 is at index 14

            # NOTE: NO MORE Changes needed ------>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # *************************** CHP ***************************
            self.net.sgen.at[15, 'p_mw'] = self.chp_p_mw
            # print(self.net.sgen)

            # ***************************** BESS *******************************************
            bess = BESS(net=self.net, sgen_mwh=self.net.sgen['p_mw'].sum(),
                        demand_e_mwh=self.net.load['p_mw'].sum(),
                        bess_mw=bess_mw,
                        bess_mwh=bess_mwh,
                        # bess_soc=bess_soc,
                        # current_energy=bess_current_energy,
                        # bess_max_energy=bess_max_energy,
                        # bess_min_energy=bess_min_energy,
                        bess_update_mwh=bess_update_mwh)
            res_bess_mw = bess.bms_update()[0]
            res_bess_mwh = bess.bms_update()[1]
            res_bess_power_loss_mwh = bess.bms_update()[2]
            res_bess_power_deficit_mwh = bess.bms_update()[3]

            self.net.storage.at[0, 'p_mw'] = res_bess_mw
            # bess_mw_update += res_bess_mwh
            bess_update_mwh = res_bess_mwh
            # print("bess_mw_update =", bess_mw_update)
            # print(self.net.storage)

            pp.runpp(self.net)

            result = {
                # 'time_step': i,
                'demand_mw': self.net.res_load.p_mw.sum(),  # summing the total load at each hour (t)
                'line_loss_mw': self.net.res_line.pl_mw.values[0],
                'gas_gen_mw': self.net.res_gen.p_mw.sum(),
                'pv_wt_chp_mw': self.net.res_sgen.p_mw.sum(),  # summing the total PV gen at each hour (t)
                'bess_mw': self.net.res_storage.p_mw.sum(),
                'ext_grid_mw': self.net.res_ext_grid.p_mw.values[0],
                'bess_mwh': res_bess_mwh
                # 'res_bess_power_loss_mwh': res_bess_power_loss_mwh,
                # 'res_bess_power_deficit_mwh': res_bess_power_deficit_mwh
            }

            for bus_idx in self.net.bus.index:
                result[f'bus_{int(bus_idx)}_voltage_pu'] = self.net.res_bus.vm_pu[bus_idx]

            results = results.append(result, ignore_index=True)

        return results
    # =================================================== 2035 Jan ===================================================
    # NOTE: Data input to change: 1. e_demand (Jan/July), 2. PV irradiance & WIND profile  3. heat_demand (Jan/July)

    # ---------------------------------------------- 2035 July ----------------------------------------------
    # NOTE: Data input to change: 1. e_demand (Jan/July), 2. PV irradiance & WIND profile  3. heat_demand (Jan/July)

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Remove Functions for PandaPower Grid %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    def remove_sgen(self):
        for idx in self.net.sgen.index:
            self.net.sgen.in_service[idx] = False
            pp.drop_out_of_service_elements(self.net)

    def remove_gen(self):
        for idx in self.net.gen.index:
            self.net.gen.in_service[idx] = False
            pp.drop_out_of_service_elements(self.net)

    def remove_load(self):
        for idx in self.net.load.index:
            self.net.load.in_service[idx] = False
            pp.drop_out_of_service_elements(self.net)

    def remove_bess(self):
        for idx in self.net.storage.index:
            self.net.storage.in_service[idx] = False
            pp.drop_out_of_service_elements(self.net)

# ======================================================= Test =======================================================
# import pandapower.networks as pn
#
# net = pn.create_cigre_network_mv(with_der=False)
#
# net.load.drop(index=net.load.index, inplace=True)
# net.sgen.drop(index=net.sgen.index, inplace=True)
# net.gen.drop(index=net.gen.index, inplace=True)
# net.xward.drop(net.xward.index, inplace=True)
# net.shunt.drop(index=net.shunt.index, inplace=True)
#
# # x = [2.00000000e+00, 1.00000000e+00, 1.30000000e+01, 1.20000000e+01,
# #  1.30000000e+01, 4.00000000e+00, 5.00000000e+00, 5.00000000e+00,
# #  9.00000000e+00, 1.00000000e+01, 9.00000000e+00, 9.00000000e+00,
# #  8.00000000e+00, 6.00000000e+00, 1.40386939e+00, 8.00744569e+00,
# #  3.13424178e+00, 8.76389152e+00, 8.50442114e-01, 1.69830420e+00,
# #  9.83468338e-01, 9.57889530e+00, 6.91877114e+00, 6.86500928e+00,
# #  1.82882773e-01, 9.88861089e+00, 2.80443992e+00, 1.03226007e+00,
# #  0.00000000e+00, 4.54297752e+02, 6.00000000e+00, 6.00000000e-01,
# #  6.00000000e+00, 5.09683479e-01, 2.11628116e-01, 2.45786580e+00,
# #  1.14823521e+00, 6.,  6.,  6.,  6.,  6.,  6., 6.,
# #      1.63794645, 1.44594756, 1.03401915, 1.39276347, 1.97676837, 1.2750858, 1.50812103]
#
# x = [2.00000000e+00, 1.00000000e+00, 1.30000000e+01, 1.20000000e+01,
#  1.30000000e+01, 4.00000000e+00, 5.00000000e+00, 5.00000000e+00,
#  9.00000000e+00, 1.00000000e+01, 9.00000000e+00, 9.00000000e+00,
#  8.00000000e+00, 6.00000000e+00, 1.40386939e+00, 8.00744569e+00,
#  3.13424178e+00, 8.76389152e+00, 8.50442114e-01, 1.69830420e+00,
#  9.83468338e-01, 9.57889530e+00, 6.91877114e+00, 6.86500928e+00,
#  1.82882773e-01, 9.88861089e+00, 2.80443992e+00, 1.03226007e+00,
#  0.00000000e+00, 4.54297752e+02, 6.00000000e+00, 1.43887669e-01,
#  6.00000000e+00, 1.93669579e-02, 2.11628116e-01, 2.45786580e+00,
#  1.14823521e+00, 1.10000000e+01, 1.02334429e+00, 1.20000000e+01,
#  1.04160024e+01, 1.00000000e+00, 2.49767295e-02]
#
#
# net_res = power_system(net=net, x_pv_bus=x[0:14], x_pv_mw=x[14:28], x_wt_bus=x[28:29], x_wt_mw=x[29],
#                        chp_bus=x[30], chp_p_mw=x[31], hp_bus=x[32], hp_cap_mw=x[33],
#                        p2g_input_mw=0,
#                        bess_bus=x[37], bess_p_mw=5,
#                        x_gen_bus_12=x[39], x_gen_bus_12_mw=x[40], x_gen_bus_1=x[41], x_gen_bus_1_mw=x[42])
#
# pf_res = net_res.power_flow_2026_jan().iloc[:, 0:9]
# res_line_loss_mwh = pf_res['line_loss_mw'].sum()
# res_bess_power_loss_2026_jan_mwh = pf_res['res_bess_power_loss_mwh'].sum()
# res_bess_power_deficit_2026_jan_mwh = pf_res['res_bess_power_deficit_mwh'].sum()
#
# print(pf_res)
# print('res_bess_power_loss_2026_jan_mwh =', res_bess_power_loss_2026_jan_mwh)
# print('res_bess_power_deficit_2026_jan_mwh =', res_bess_power_deficit_2026_jan_mwh)
# print('res_line_loss_mwh =', res_line_loss_mwh)

