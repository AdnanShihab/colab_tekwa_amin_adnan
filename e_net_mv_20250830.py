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


from bess_20240725 import BESSFleet

# =========================================== Power Flow Calc ===========================================


class power_system:
    def __init__(self, net, x_pv_bus, x_pv_mw, x_wt_bus, x_wt_mw,
                 x_bess_bus, x_bess_mw, bess_params=None, **kwargs): #  chp_bus, chp_p_mw, hp_bus, hp_cap_mw, p2g_input_mw,
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

        # Build BESS fleet once
        self.bess_fleet = BESSFleet(self.net, self.x_bess_bus, self.x_bess_mw, self.bess_params)
        self.bess_fleet.build()

    # --------------------------- Asset creation ---------------------------
    def _create_bess_assets(self):

        # Default BESS params
        defaults = dict(energy_hours=2.0, eta_ch=0.95, eta_dis=0.95,
                        soc_init_frac=0.5, peak_threshold=0.65, valley_threshold=0.35)
        if self.bess_params:
            defaults.update(self.bess_params)
        self.bess_params = defaults

        # Placeholder for BESS internal tracking
        self.bess_assets = []  # list of dict: {bus, p_max, e_max, soc, storage_idx}
        self.bess_log = []  # time series log of operations

        # One storage element per bus (cluster) selected
        params = self.bess_params
        for i, (bus, p_bess) in enumerate(zip(self.x_bess_bus, self.x_bess_mw)):
            # p_bess is the power rating (MW) of that BESS candidate at the given cluster/bus —
            # i.e. the maximum charge or discharge power you allowed for that battery
            # (the value from x_bess_mw aligned with its bus).
            # “p_bess” used to size instantaneous power;
            # the energy capacity is later derived (e.g. E_max = energy_hours * p_bess).
            if p_bess <= 0: continue
            e_bess = p_bess * params['energy_hours']
            soc0 = params['soc_init_frac'] * e_bess
            storage_idx = pp.create_storage(self.net,
                                            bus=bus,
                                            p_mw=0.0,
                                            max_e_mwh=e_bess,
                                            min_e_mwh=0.0,
                                            soc_percent=100.0 * soc0 / e_bess if e_bess > 0 else 0.0,
                                            max_p_mw=p_bess,
                                            min_p_mw=-p_bess,
                                            name=f"BESS_{i}",
                                            type="bess")
            self.bess_assets.append(dict(id=i, bus=bus, p_bess=p_bess,
                                         e_bess=e_bess, soc=soc0,
                                         storage_idx=storage_idx))

    # -------------------------- BESS dispatch heuristic --------------------------
    def _dispatch_bess_step(self, t, residual_signal, dt=1.0):
        p_total = 0.0
        params = self.bess_params
        eta_ch = params['eta_ch']
        eta_dis = params['eta_dis']

        for asset in self.bess_assets:
            p_cmd = 0.0  # positive discharge to grid, negative charge
            soc = asset['soc']
            e_max = asset['e_max']
            p_max = asset['p_max']

            # Simple logic:
            # residual_signal normalized 0..1 maybe (your choice before calling)
            if residual_signal > params['peak_threshold']:
                # Discharge
                p_available = min(p_max, soc * eta_dis / dt)  # limit by SoC
                p_cmd = p_available
                soc_new = soc - (p_cmd / eta_dis) * dt
            elif residual_signal < params['valley_threshold']:
                # Charge
                headroom = e_max - soc
                p_available = min(p_max, headroom / (eta_ch * dt))
                p_cmd = -p_available
                soc_new = soc + (abs(p_cmd) * eta_ch) * dt
            else:
                soc_new = soc

            # Update
            asset['soc'] = soc_new
            # Update storage element power (p_mw positive = discharge)
            self.net.storage.at[asset['storage_idx'], 'p_mw'] = p_cmd
            self.net.storage.at[asset['storage_idx'], 'soc_percent'] = 100.0 * soc_new / e_max if e_max > 0 else 0.0

            # Log
            self.bess_log.append(dict(t=t, asset_id=asset['id'],
                                      bus=asset['bus'],
                                      p_mw=p_cmd, soc_mwh=soc_new,
                                      soc_frac=soc_new / e_max if e_max > 0 else 0.0))
            p_total += p_cmd
            print("Battery power (p_mw):", p_cmd)
            print(x)
        return p_total

    def power_flow_2026_jan(self):      # January with 7 days time series

        results = pd.DataFrame()
        net_update = []

        # ************************ Create loads on the fixed bus bars with 0 p_mw ******************************
        # loads = self.net.load
        # print(loads[['bus', 'p_mw']])

        # bus_idx_86 = 86
        # loads_at_bus_86 = self.net.load[self.net.load['bus'] == bus_idx_86]
        # self.net.load.drop(loads_at_bus_86.index, inplace=True)
        # pp.create_load(self.net, bus=bus_idx_86, p_mw=1, name="NEW Load 86")
        #
        # bus_idx_126 = 126
        # loads_at_bus_126 = self.net.load[self.net.load['bus'] == bus_idx_126]
        # self.net.load.drop(loads_at_bus_126.index, inplace=True)
        # pp.create_load(self.net, bus=bus_idx_126, p_mw=1, name="NEW Load 126")
        #
        # bus_idx_6 = 6
        # loads_at_bus_6 = self.net.load[self.net.load['bus'] == bus_idx_6]
        # self.net.load.drop(loads_at_bus_6.index, inplace=True)
        # pp.create_load(self.net, bus=bus_idx_6, p_mw=1, name="NEW Load 6")

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
        #
        # bess_mw = self.bess_p_mw  # this is already for 1 hour = MWh for each battery
        # bess_mwh = self.bess_p_mw * 1    # for each hour
        # bess_soc = 0.5
        #
        # bess_init_mwh = bess_mwh * bess_soc
        # bess_update_mwh = bess_init_mwh

        # $$$$ CHAT GPT BES Model $$$$$
        # storage_idx = pp.create_storage(self.net, bus=self.bess_bus, p_mw=0.0, max_e_mwh=5.0, soc_percent=0.50,
        #                                 min_p_mw=-bess_mw, max_p_mw=bess_mw, max_q_mvar=0.5, min_q_mvar=-0.5,
        #                                 name="BESS_0")

        # ---------------------------------- Time series analysis ----------------------------------
        for t, (load_idx, load_row) in enumerate(e_demand_2026_feb[0:24].iterrows()):
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

                # ---------------- Chem industry loads ----------------(Removed because not connecting Ind loads now)
                # self.net.load.at[147, 'p_mw'] = load_row['LG 01']  # Assuming Chem Industry Load 1 is at index 147
                # self.net.load.at[148, 'p_mw'] = load_row['LG 07']  # Assuming Chem Industry Load 1 is at index 148
                # self.net.load.at[149, 'p_mw'] = load_row['LG 03']  # Assuming small Industry Load 1 is at index 149

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

            # print("Renewable generation:")
            # sgen = self.net.sgen[['bus', 'p_mw']]
            # print(sgen)
            # print()

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
            # power_system.remove_load(self)  # I don't need this because: self.net.load['p_mw'] = original_loads.copy()
            # p_sys.remove_gen()
            # p_sys.remove_load()
            # p_sys.remove_bess()

        # print(net_update)
        # print(results[['demand_mw', 'pv_wt_chp_mw', 'bess_mwh', 'bess_p_mw', 'bess_soc', 'ext_grid_mw']])
        # print(x)
        return results, net_update

    def power_flow_2030_jan(self):      # January with 7 days time series

        # working on it........................................................................................

        results = pd.DataFrame()
        net_update = []

        # ************************ Create loads on the fixed bus bars with 0 p_mw ******************************
        # loads = self.net.load
        # print(loads[['bus', 'p_mw']])

        # bus_idx_86 = 86
        # loads_at_bus_86 = self.net.load[self.net.load['bus'] == bus_idx_86]
        # self.net.load.drop(loads_at_bus_86.index, inplace=True)
        # pp.create_load(self.net, bus=bus_idx_86, p_mw=1, name="NEW Load 86")
        #
        # bus_idx_126 = 126
        # loads_at_bus_126 = self.net.load[self.net.load['bus'] == bus_idx_126]
        # self.net.load.drop(loads_at_bus_126.index, inplace=True)
        # pp.create_load(self.net, bus=bus_idx_126, p_mw=1, name="NEW Load 126")
        #
        # bus_idx_6 = 6
        # loads_at_bus_6 = self.net.load[self.net.load['bus'] == bus_idx_6]
        # self.net.load.drop(loads_at_bus_6.index, inplace=True)
        # pp.create_load(self.net, bus=bus_idx_6, p_mw=1, name="NEW Load 6")

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
        #
        # bess_mw = self.bess_p_mw  # this is already for 1 hour = MWh for each battery
        # bess_mwh = self.bess_p_mw * 1    # for each hour
        # bess_soc = 0.5
        #
        # bess_init_mwh = bess_mwh * bess_soc
        # bess_update_mwh = bess_init_mwh

        # $$$$ CHAT GPT BES Model $$$$$
        # storage_idx = pp.create_storage(self.net, bus=self.bess_bus, p_mw=0.0, max_e_mwh=5.0, soc_percent=0.50,
        #                                 min_p_mw=-bess_mw, max_p_mw=bess_mw, max_q_mvar=0.5, min_q_mvar=-0.5,
        #                                 name="BESS_0")

        # ---------------------------------- Time series analysis ----------------------------------
        for t, (load_idx, load_row) in enumerate(e_demand_2026_feb[0:1].iterrows()):
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

                # ---------------- Chem industry loads ----------------(Removed because not connecting Ind loads now)
                # self.net.load.at[147, 'p_mw'] = load_row['LG 01']  # Assuming Chem Industry Load 1 is at index 147
                # self.net.load.at[148, 'p_mw'] = load_row['LG 07']  # Assuming Chem Industry Load 1 is at index 148
                # self.net.load.at[149, 'p_mw'] = load_row['LG 03']  # Assuming small Industry Load 1 is at index 149

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

            # print("Renewable generation:")
            # sgen = self.net.sgen[['bus', 'p_mw']]
            # print(sgen)
            # print()

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

            total_deficit_mw = residual     # >0 means deficit
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
            # power_system.remove_load(self)  # I don't need this because: self.net.load['p_mw'] = original_loads.copy()
            # p_sys.remove_gen()
            # p_sys.remove_load()
            # p_sys.remove_bess()

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