# 2024.07.25

import pandas as pd
import numpy as np
import pandapower as pp
from copy import deepcopy

# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)

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
# -------------------------- 2031 --------------------------
e_demand_2031_jan = e_load_time_series_jan*1.2789
e_demand_2031_jul = e_load_time_series_jul*1.2789
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


from bess_20240725 import BESSFleet

# =========================================== Power Flow Calc ===========================================


class power_system:
    def __init__(self, net, x_pv_bus, x_pv_mw, x_wt_bus, x_wt_mw,
                 x_bess_bus, x_bess_mw, bess_params=None, **kwargs):
        #  chp_bus, chp_p_mw, hp_bus, hp_cap_mw, p2g_input_mw,
        # , x_gen_bus_12, x_gen_bus_12_mw, x_gen_bus_1, x_gen_bus_1_mw, **kwargs):

        self.net = net
        # self.x = x
        self.x_pv_bus = x_pv_bus
        self.x_pv_mw = x_pv_mw
        self.x_wt_bus = x_wt_bus
        self.x_wt_mw = x_wt_mw
        self.x_bess_bus = x_bess_bus
        self.x_bess_mw = x_bess_mw
        self.bess_params = {
            "duration_h": 2.0,  # using Tau = 2 hr, because 2 h is popular for fast response/ancillary services.
                                # Check source in OneNote.
            "eta_ch": 0.95,
            "eta_dis": 0.95,
            "soc_init_frac": 0.5,
            "soc_min_frac": 0.1,
            "soc_max_frac": 0.9,
            "dt_h": 1.0
        }

        # Build BESS fleet once
        self.bess_fleet = BESSFleet(self.net, self.x_bess_bus, self.x_bess_mw, self.bess_params)
        self.bess_fleet.build()

    def power_flow_2026_jan(self):      # January with 7 days time series

        results = pd.DataFrame()
        net_update = []

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

        # ---------------------------------- Time series analysis ----------------------------------
        for t, (load_idx, load_row) in enumerate(e_demand_2026_feb[0:5].iterrows()):
            print("time =", t)

            # ------------------ Time series input data for PV and WT ------------------
            irradiance_row = irradiance_feb.iloc[t]
            wind_row = wt_ts_feb.iloc[t]

            # Reset all loads to original values at the start of each time step
            self.net.load['p_mw'] = original_loads.copy()

            for load_idx, load in self.net.load.iterrows():
                bus_idx = load['bus']
                p_mw = load['p_mw']

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
            # print("Updated Loads:")
            # print("Total load MW =", self.net.load['p_mw'].sum(), " at time step ", t)
            # print("length of loads =", len(self.net.load))
            # print()

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

        #     # *************************** CHP ***************************
        #     # self.net.sgen.at[15, 'p_mw'] = self.chp_p_mw
        #     # print(self.net.sgen)

            # # =================================== BESS *******************************************
            # # print("bess_mw", bess_mw)
            # # print("tot_sgen =", self.net.sgen['p_mw'].sum())
            # # print("tot_demand_e =", self.net.load['p_mw'].sum())
            # # print()
            # bess = BESS(net=self.net, sgen_mwh=self.net.sgen['p_mw'].sum(), demand_e_mwh=self.net.load['p_mw'].sum(),
            #             bess_mw=bess_mw,
            #             bess_mwh=bess_mwh,
            #             # bess_soc=bess_soc,
            #             # current_energy=bess_current_energy,
            #             # bess_max_energy=bess_max_energy,
            #             # bess_min_energy=bess_min_energy,
            #             bess_update_mwh=bess_update_mwh)
            # res_bess_mw = bess.adjust_bess()[0]
            # res_bess_mwh = bess.adjust_bess()[1]
            #
            # self.net.storage.at[0, 'p_mw'] = res_bess_mw
            # # bess_mw_update += res_bess_mwh
            # bess_update_mwh = res_bess_mwh
            # # print("bess_mw_update =", bess_mw_update)
            # # print(self.net.storage)

            # print("Loads:")
            # print(self.net.load['p_mw'].sum())
            # print("PVs = \n", self.net.sgen['p_mw'].sum())

            # Simple global balance to decide BESS charging/discharging before runpp
            # ------------------- Compute residual signal for BESS dispatch -------------------
            # 4) Compute residual signal for BESS dispatch
            total_load = self.net.load['p_mw'].sum()
            total_res_gen = self.net.sgen['p_mw'].sum() if len(self.net.sgen) else 0.0

            # print("Total Load =", total_load)
            # print("Total RES gen =", total_res_gen)

            # Normalize residual signal between 0 and 1 (crude scaling)
            # residual > 0 means more load than RES gen
            residual = total_load - total_res_gen

            total_deficit_mw = residual     # > 0 means deficit
            # print("total_deficit_mw =", total_deficit_mw)
            self.bess_fleet.dispatch(total_deficit_mw)

            # 20251124:
            # scale: residual_signal = residual / (total_load + 1e-6) clipped into [0,1]
            # residual_signal = np.clip(residual / (total_load + 1e-6), 0.0, 1.0)
            # print("Residual signal =", residual_signal)
            # self._dispatch_bess_step(t, residual_signal)

            pp.runpp(self.net)

            # print("Power flow:")

            # Using to copy the updated net before using the remove function. This values are used in the CAPEX func.
            # net_update is copying the new net after each time step, means it creates a new net for each time step.
            # For example: if I have 24 time steps, then I will have 24 nets in the net_update list. This applies for
            # PV, loads and all net elements.
            net_update.append(deepcopy(self.net))
            # print("Net Update =\n", self.net.load['p_mw'])

            bess_mwh = (
                self.net.storage['e_mwh'].sum()
                if (len(self.net.storage) and 'e_mwh' in self.net.storage.columns)
                else 0.0
            )

            # print("t=", t, "storage id=", id(self.net.storage), "cols=", list(self.net.storage.columns))
            # print(self.net.storage.head())
            # print("Has e_mwh?", 'e_mwh' in self.net.storage.columns)

            result = {
                # 'time_step': t,
                'demand_mw': self.net.res_load.p_mw.sum(),  # summing the total load at each hour (t)
                # 'line_loss_mw': self.net.res_line.pl_mw.values[0],
                # 'gas_gen_mw': self.net.res_gen.p_mw.sum(),
                'pv_wt_chp_mw': self.net.res_sgen.p_mw.sum(),  # summing the total PV gen at each hour (t)
                # 'bess_mw': self.net.res_storage.p_mw.sum(),
                # 'bess_mwh': self.net.storage['e_mwh'].sum(),
                'bess_mwh': bess_mwh,   # using the variable bess_mwh which is calculated above to avoid KeyError when 'e_mwh' column is missing
                'bess_p_mw': self.net.res_storage.p_mw.sum() if len(self.net.storage) else 0.0,
                # bess_p_mw Negative means discharging, positive means charging
                'bess_soc': self.bess_fleet.soc_frac(),
                'ext_grid_mw': self.net.res_ext_grid.p_mw.sum()  # Negative means export, positive means import
            }

            for bus_idx in self.net.bus.index:
                result[f'bus_{int(bus_idx)}_voltage_pu'] = self.net.res_bus.vm_pu[bus_idx]

            results = results.append(result, ignore_index=True)

            power_system.remove_sgen(self)  # it works only if I remove the PVs end of each for loop
            # power_system.remove_load(self)  # I don't need this because: self.net.load['p_mw'] = original_loads.copy()
            # p_sys.remove_gen()
            # p_sys.remove_load()
            # power_system.remove_bess(self)

        # print(net_update)
        # print(results[['demand_mw', 'pv_wt_chp_mw', 'bess_mwh', 'bess_p_mw', 'bess_soc', 'ext_grid_mw']])
        # print(x)
        return results, net_update

    def power_flow_2031_jan(self):      # Winter/January with 7 days time series

        # -------------------------------------------------
        # What to change in the code:
        # 1. Change the e_demand time series data to 2031 data.
        # 2. Change the irradiance and wind data.
        # 3. Change the heat_demand time series data to 2031 data.

        e_demand = e_demand_2031_jan
        irradiance = irradiance_feb
        wind = wt_ts_feb

        results = pd.DataFrame()
        net_update = []

        # --------------------- Store original load values ---------------------
        original_loads = self.net.load['p_mw'].copy()

        # --------------------------------- Decision variables for PV WT CHP ---------------------------------
        x_pv_bus = self.x_pv_bus
        x_pv_mw = self.x_pv_mw
        x_wt_bus = self.x_wt_bus
        x_wt_mw = self.x_wt_mw

        # ---------------------------------- Time series analysis ----------------------------------
        for t, (load_idx, load_row) in enumerate(e_demand[0:4].iterrows()):
            print("time =", t)

            # ------------------ Time series input data for PV and WT ------------------
            irradiance_row = irradiance.iloc[t]
            wind_row = wind.iloc[t]

            # Reset all loads to original values at the start of each time step
            self.net.load['p_mw'] = original_loads.copy()

            for load_idx, load in self.net.load.iterrows():
                bus_idx = load['bus']
                p_mw = load['p_mw']

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
            # print("Updated Loads:")
            # print("Total load MW =", self.net.load['p_mw'].sum(), " at time step ", t)
            # print("length of loads =", len(self.net.load))
            # print()

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

            #     # *************************** CHP ***************************
            #     # self.net.sgen.at[15, 'p_mw'] = self.chp_p_mw
            #     # print(self.net.sgen)

            # Simple global balance to decide BESS charging/discharging before runpp
            # ------------------- Compute residual signal for BESS dispatch -------------------
            # 4) Compute residual signal for BESS dispatch
            total_load = self.net.load['p_mw'].sum()
            total_res_gen = self.net.sgen['p_mw'].sum() if len(self.net.sgen) else 0.0

            # print("Total Load =", total_load)
            # print("Total RES gen =", total_res_gen)

            # Normalize residual signal between 0 and 1 (crude scaling)
            # residual > 0 means more load than RES gen
            residual = total_load - total_res_gen

            total_deficit_mw = residual  # > 0 means deficit
            # print("total_deficit_mw =", total_deficit_mw)
            self.bess_fleet.dispatch(total_deficit_mw)

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
                'bess_mwh': self.net.storage['e_mwh'].sum(),
                'bess_p_mw': self.net.res_storage.p_mw.sum() if len(self.net.storage) else 0.0,
                'bess_soc': self.bess_fleet.soc_frac(),
                'ext_grid_mw': self.net.res_ext_grid.p_mw.sum()
            }

            for bus_idx in self.net.bus.index:
                result[f'bus_{int(bus_idx)}_voltage_pu'] = self.net.res_bus.vm_pu[bus_idx]

            results = results.append(result, ignore_index=True)

            power_system.remove_sgen(self)  # it works only if I remove the PVs end of each for loop

        # print(net_update)
        # print(results[['demand_mw', 'pv_wt_chp_mw', 'bess_mwh', 'bess_p_mw', 'bess_soc', 'ext_grid_mw']])
        # print(x)
        return results, net_update

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