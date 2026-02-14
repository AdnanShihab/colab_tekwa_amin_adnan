
# ........... NOT USING IT ...............2024.07.26
# ........... NOT USING IT ...............
# ........... NOT USING IT ...............


import pandas as pd

# pd.set_option('display.max_columns', None)

# Time series

# print(gas_demand_jan)


class BESS:
    def __init__(self, net, bess_mw, bess_mwh, sgen_mwh, demand_e_mwh, bess_update_mwh, **kwargs):
        # current_energy, bess_max_energy,
        # bess_min_energy,
        self.net = net
        self.bess_mw = bess_mw
        self.bess_mwh = bess_mwh
        # self.bess_soc = bess_soc
        # self.surplus_mw = surplus_mw
        # self.current_energy = current_energy
        # self.bess_max_energy = bess_max_energy
        # self.bess_min_energy = bess_min_energy
        self.sgen_mwh = sgen_mwh
        self.demand_e_mwh = demand_e_mwh
        self.bess_update_mwh = bess_update_mwh

    def adjust_bess(self):

        ch_dis_rate_mw = self.bess_mw
        bess_max_ch_energy_mwh = self.bess_mwh * 12 * 0.9  # C rate 0.5 - 90% max limit; 12 = total cycle per 24 hrs
        bess_max_dis_energy_mwh = self.bess_mwh * 12 * 0.1  # C rate 0.5 - 10% max limit
        # 0.5 C rate means that it will take two hours to fully charge or discharge,
        # i.e.: 12 cycle of charging and discharging for 24 hr operation.

        res_bess_mw = 0
        res_bess_mwh = self.bess_update_mwh  # Initialize with the current energy state

        current_bess_update_mwh = res_bess_mwh
        # print("BESS from Net Func:")
        # print("ch_dis_rate_mw =", ch_dis_rate_mw)
        # print("current_bess_update_mwh =", current_bess_update_mwh)
        # print("bess_max_ch_energy_mwh =", bess_max_ch_energy_mwh)
        # print("bess_max_dis_energy_mwh =", bess_max_dis_energy_mwh)
        # print()

        eta_storage_ch = 0.95
        eta_storage_dis = 0.95

        # bess_max_energy = 0.9 * self.bess_capacity_mwh
        # bess_min_energy = 0.1 * self.bess_capacity_mwh
        # current_energy = self.bess_capacity_mwh * self.bess_soc    #self.net.storage['soc_percent']   # soc = 50%
        # print("current_energy", current_energy)
        # print()

        surplus_mw = self.sgen_mwh - self.demand_e_mwh
        # print("surplus_mw =", surplus_mw)

        # surplus_mw = self.net.sgen['p_mw'].sum() - self.net.load['p_mw'].sum()

        # for bess_idx, bess_idx in enumerate(self.bess_capacity_mwh):
        if surplus_mw > 0:
            # Charging
            # print("Charging:")
            charge_power = ch_dis_rate_mw * eta_storage_ch

            if current_bess_update_mwh < bess_max_ch_energy_mwh:
                # print("current_energy < bess_max_energy")
                res_bess_mw = charge_power   # Charging power (positive because it's charging)
                res_bess_mwh = current_bess_update_mwh + charge_power  # -> charging

                if res_bess_mwh > bess_max_ch_energy_mwh:
                    res_bess_mw = charge_power
                    res_bess_mwh = bess_max_ch_energy_mwh
                else:
                    pass
            else:   # current_energy >= max_ch_mwh
                res_bess_mw = 0
                res_bess_mwh = bess_max_ch_energy_mwh

            # res_bess_mw += bess_update_mw
            # current_energy_update_mwh += current_energy_update_mwh

        else:  # surplus_mw < 0
            # Discharging
            # print("Discharging:")
            # deficit_mw = self.demand_e_mwh - self.sgen_mwh
            discharge_power = ch_dis_rate_mw * eta_storage_dis

            if current_bess_update_mwh > bess_max_dis_energy_mwh:

                # print("current_energy > bess_min_energy")

                res_bess_mw = -discharge_power  # DisCharging power (negative because it's discharging)
                res_bess_mwh = current_bess_update_mwh - discharge_power   # -> discharging

                if res_bess_mwh < bess_max_dis_energy_mwh:
                    res_bess_mw = -discharge_power
                    res_bess_mwh = bess_max_dis_energy_mwh
                else:
                    pass
            else:   # current_bess_energy <= min_bess_dis_energy
                # print("current_bess_update_mwh", current_bess_update_mwh)
                res_bess_mw = 0
                res_bess_mwh = current_bess_update_mwh

                # bess_update_mw = 0
                # current_energy_update_mwh = current_energy_update_mwh + bess_update_mw

            # # res_bess_mw += bess_update_mwh
            # res_bess_mw += bess_update_mw
            # current_energy_update_mwh += current_energy_update_mwh

        # print()
        # print("res_bess_mw=", res_bess_mw)
        # print("current_energy_update_mwh=", res_bess_mwh)
        # print()
        return res_bess_mw, res_bess_mwh

    def bms_update(self):

        ch_dis_rate_mw = self.bess_mw       # with C rate 1 = max capacity charge and discharge in 1 hr.
        bess_max_ch_energy_mwh = self.bess_mwh * 0.9  # 90% max charge energy
        bess_min_dis_energy_mwh = self.bess_mwh * 0.1  # 10% nin discharge energy

        res_bess_mw = 0
        res_bess_mwh = self.bess_update_mwh  # Initialize with the current energy state

        current_bess_update_mwh = res_bess_mwh    # Current energy state
        # print("BESS from Net Func:")
        # print("ch_dis_rate_mw =", ch_dis_rate_mw)
        # print("current_bess_update_mwh =", current_bess_update_mwh)
        # print("bess_max_ch_energy_mwh =", bess_max_ch_energy_mwh)
        # print("bess_max_dis_energy_mwh =", bess_max_dis_energy_mwh)
        # print()

        eta_storage_ch = 0.90   # Source: MANGO
        eta_storage_dis = 0.90  # Source: MANGO

        # bess_max_energy = 0.9 * self.bess_capacity_mwh
        # bess_min_energy = 0.1 * self.bess_capacity_mwh
        # current_energy = self.bess_capacity_mwh * self.bess_soc    #self.net.storage['soc_percent']   # soc = 50%
        # print("current_energy", current_energy)
        # print()

        surplus_mw = self.sgen_mwh - self.demand_e_mwh
        # print("surplus_mw =", surplus_mw)

        # surplus_mw = self.net.sgen['p_mw'].sum() - self.net.load['p_mw'].sum()

        # for bess_idx, bess_idx in enumerate(self.bess_capacity_mwh):
        if surplus_mw > 0:
            # Charging
            # print("Charging:")
            charge_power = ch_dis_rate_mw * eta_storage_ch

            res_bess_power_deficit_mwh = 0

            if current_bess_update_mwh < bess_max_ch_energy_mwh:        # Can charge
                # print("current_energy < bess_max_energy")
                res_bess_mw = charge_power   # Charging power (positive because it's charging)
                res_bess_mwh = current_bess_update_mwh + charge_power  # -> charging
                # print('bess capacity at ch', res_bess_mwh)

                if res_bess_mwh > bess_max_ch_energy_mwh:       # Can charge, but cannot go over the max limit
                    # print('power loss mwh =', res_bess_mwh - bess_max_ch_energy_mwh)
                    res_bess_power_loss_mwh = res_bess_mwh - bess_max_ch_energy_mwh
                    res_bess_mw = charge_power
                    res_bess_mwh = bess_max_ch_energy_mwh
                else:           # Can charge
                    res_bess_power_loss_mwh = 0
                    res_bess_mw = charge_power
                    res_bess_mwh = res_bess_mwh
            else:   # current_energy >= max_ch_mwh      # Cannot charge, BESS is full
                res_bess_mw = 0
                res_bess_mwh = res_bess_mwh
                res_bess_power_loss_mwh = 0
                # print('bess capacity FULL =', res_bess_mwh)

                # add mwh and power loss in the main output results....

            # res_bess_mw += bess_update_mw
            # current_energy_update_mwh += current_energy_update_mwh

        else:  # surplus_mw < 0 == Demand > PV+WT
            # Discharging
            # print("Can discharge?:")
            # print('current_bess_update_mwh =', current_bess_update_mwh)
            # deficit_mw = self.demand_e_mwh - self.sgen_mwh
            discharge_power = ch_dis_rate_mw * eta_storage_dis

            res_bess_power_loss_mwh = 0     # No charging, so no power loss for bess is possible.

            if current_bess_update_mwh > bess_min_dis_energy_mwh:

                res_bess_mw = -discharge_power  # DisCharging power (negative because it's discharging)
                res_bess_mwh = current_bess_update_mwh - discharge_power   # -> discharging

                if res_bess_mwh < bess_min_dis_energy_mwh:  # BESS capacity cant be less than min capacity 10%

                    res_bess_power_deficit_mwh = bess_min_dis_energy_mwh - res_bess_mwh
                    res_bess_mw = -discharge_power
                    res_bess_mwh = bess_min_dis_energy_mwh

                    # print("YES")
                    # print('res_bess_power_deficit_mwh =', res_bess_power_deficit_mwh)
                else:   # res_bess_mwh > bess_min_dis_energy_mwh and
                    res_bess_power_deficit_mwh = 0      # No deficit, because enough charge in BESS
                    res_bess_mw = -discharge_power
                    res_bess_mwh = res_bess_mwh

            else:   # current_bess_energy <= min_bess_dis_energy
                # print("NO")
                res_bess_mw = 0
                res_bess_mwh = current_bess_update_mwh
                res_bess_power_deficit_mwh = 0
                # print('res_bess_mwh =', res_bess_mwh)

                # bess_update_mw = 0
                # current_energy_update_mwh = current_energy_update_mwh + bess_update_mw

            # # res_bess_mw += bess_update_mwh
            # res_bess_mw += bess_update_mw
            # current_energy_update_mwh += current_energy_update_mwh

        # print()
        # print("res_bess_mw=", res_bess_mw)
        # print("current_energy_update_mwh=", res_bess_mwh)
        # print()
        return res_bess_mw, res_bess_mwh, res_bess_power_loss_mwh, res_bess_power_deficit_mwh

# ************************************* Model Testing *************************************
# import pandapower.networks as pn
#
# # Power grid:
# net = pn.create_cigre_network_mv(with_der=False)
#
# net.load.drop(index=net.load.index, inplace=True)
# net.sgen.drop(index=net.sgen.index, inplace=True)
# net.gen.drop(index=net.gen.index, inplace=True)
# net.xward.drop(net.xward.index, inplace=True)
# net.shunt.drop(index=net.shunt.index, inplace=True)
#
# bess = BESS(net=net, sgen_mwh=100, demand_e_mwh=0.20,
#                         bess_mw=10,
#                         bess_mwh=10*1,
#                         bess_soc=0.5,
#                         # current_energy=bess_current_energy,
#                         # bess_max_energy=bess_max_energy,
#                         # bess_min_energy=bess_min_energy,
#                         bess_update_mwh=10*0.5)
# bess_mwh = bess.adjust_bess()
#
# print(bess_mwh)


# ************************************* NEW BESS Model 20251124 *************************************

import numpy as np
import pandapower as pp


class BESSFleet:
    def __init__(self, net, buses, p_rated_mw, params):
        self.net = net
        # Only keep valid units (bus not None and p_rated > 0)
        self.buses = [b for b in buses if b is not None]
        self.p_rated_mw = [p for b, p in zip(buses, p_rated_mw) if b is not None and p > 0.0]

        # Parameters
        self.duration_h = params.get("duration_h", 2.0)
        self.eta_ch = params.get("eta_ch", 0.95)
        self.eta_dis = params.get("eta_dis", 0.80)
        self.soc_init_frac = params.get("soc_init_frac", 0.5)
        self.soc_min_frac = params.get("soc_min_frac", 0.1)
        self.soc_max_frac = params.get("soc_max_frac", 0.9)
        self.dt_h = params.get("dt_h", 1.0)     # time step in hours for dispatch calculations

        # Derived quantities
        self.E_cap = [p * self.duration_h for p in self.p_rated_mw]  # MWh
        self.SOC = [self.soc_init_frac * E for E in self.E_cap]    # MWh

        self.storage_idx = []  # pandapower storage indices

    def build(self):
        # This is old code: Gave 'e_mwh' key ERROR for gen = 10 Pop = 20.
        # Create storage elements with p_mw=0 initially
        # for bus, E in zip(self.buses, self.E_cap):
        #     idx = pp.create_storage(self.net, bus=bus, p_mw=0.0, max_e_mwh=E, q_mvar=0.0,
        #                             name=f"BESS_bus_{bus}", type="batt")
        #     self.storage_idx.append(idx)

        # NEW way to add 'e_mwh' column to net.storage
        # Create storage elements with p_mw=0 initially
        for bus, E in zip(self.buses, self.E_cap):
            idx = pp.create_storage(self.net, bus=bus, p_mw=0.0, max_e_mwh=E, q_mvar=0.0,
                                    name=f"BESS_bus_{bus}", type="batt")
            self.storage_idx.append(idx)

            # initialize e_mwh column for all created storages
        self.net.storage.loc[self.storage_idx, 'e_mwh'] = self.SOC

    def dispatch(self, total_deficit_mw):
        """
        Simple global dispatch:
        - If total_deficit_mw > 0: discharge to cover deficits
        - If total_deficit_mw < 0: charge using surplus
        Dispatch is apportioned proportionally to power rating.
        """
        if len(self.storage_idx) == 0:
            return

        dt = self.dt_h
        P_rated = np.array(self.p_rated_mw, dtype=float)
        weights = P_rated / (P_rated.sum() if P_rated.sum() > 0 else 1.0)
        # print("Storage before dispatch:")
        # print(self.net.storage)
        # print("p_mw:", P_rated)
        # print("weights:", weights)

        if total_deficit_mw > 1e-6:
            # Discharge
            # print("Discharge:")
            alloc = total_deficit_mw
            for i, idx in enumerate(self.storage_idx):
                # Power limit from rating
                p_max_rated = P_rated[i]
                # Power limit from SOC floor: SOC' = SOC - (p_dis/eta_dis)*dt >= soc_min_frac * E_cap
                e_avail_mwh = self.SOC[i] - self.soc_min_frac * self.E_cap[i]
                p_max_soc = max(0.0, e_avail_mwh * self.eta_dis / dt)
                p_set = min(alloc * weights[i], p_max_rated, p_max_soc)
                # Set discharge power (positive)
                self.net.storage.at[idx, 'p_mw'] = -p_set      # Changed from + p_set to - p_set
                # Update SOC
                self.SOC[i] -= (p_set / self.eta_dis) * dt      # MWh
        elif total_deficit_mw < -1e-6:
            # Charge
            # print("Charge")
            surplus = -total_deficit_mw
            for i, idx in enumerate(self.storage_idx):
                p_max_rated = P_rated[i]
                # SOC ceiling: SOC' = SOC + p_ch*eta_ch*dt <= soc_max_frac * E_cap
                e_room_mwh = self.soc_max_frac * self.E_cap[i] - self.SOC[i]
                p_max_soc = max(0.0, e_room_mwh / (self.eta_ch * dt))
                p_set = min(surplus * weights[i], p_max_rated, p_max_soc)
                # Set charge power (negative)
                self.net.storage.at[idx, 'p_mw'] = p_set    # Changed from - p_set to + p_set
                # Update SOC
                self.SOC[i] += (p_set * self.eta_ch) * dt
        else:
            # Near-balance: idle
            print("Near-balance: idle")
            for idx in self.storage_idx:
                self.net.storage.at[idx, 'p_mw'] = 0.0
        soc_frac = [self.SOC[i] / self.E_cap[i] for i in range(len(self.SOC))]

        # NEW way to add 'e_mwh' column to net.storage and update it with the current SOC values
        # self.net.storage['e_mwh'] = self.SOC  # Was used before, but gave 'e_mwh' key ERROR for gen = 10 Pop = 20.
        self.net.storage.loc[self.storage_idx, 'e_mwh'] = self.SOC

        missing = set(self.storage_idx) - set(self.net.storage.index)
        if missing:
            raise RuntimeError(f"Stale storage_idx not in net.storage.index: {missing}")

        # -------------------------- Print for debugging --------------------------
        # print()
        # print("Storage after discharge (MWh):")
        # print("Storage after dispatch (MWh):")
        # print(self.net.storage.columns)
        # print(self.net.storage)
        # print()

        # print("SOC_MWh =", self.SOC)
        # print("SOC_frac =", soc_frac)

    def total_soc_mwh(self):
        return float(np.sum(self.SOC))

    def soc_frac(self):
        # soc_frac = [self.SOC[i] / self.E_cap[i] for i in range(len(self.SOC))]
        # return soc_frac[0]

        # To tackle the error: for soc_frac[0], IndexError: list index out of range
        if len(self.SOC) == 0:
            return 0.0  # or np.nan
        return float(np.sum(self.SOC) / (np.sum(self.E_cap) + 1e-12))

    def clear_power(self):
        for idx in self.storage_idx:
            self.net.storage.at[idx, 'p_mw'] = 0.0