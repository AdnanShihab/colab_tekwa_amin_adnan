
"""
Cost evolution for OPEX components with different escalation/de-escalation rates.
For now just PV, WT OPEX are included.
"""

# ---------------------------------- PV ----------------------------------
LAND_AREA_PV = 16187  # m2 per MW
LAND_ESCALATION = 0.03          # +3 %
ROOFTOP_ESCALATION = 0.01       # +1 %
FOM_DEESCALATION = -0.02        # −2 %

# Beloe the base year are defined based on the origin of the data.
# For example, the rooftop leasing cost for commercial areas is based on the 2026 value,
# as it is expected that the cost will increase in the future.
# The fixed O&M cost for PV ground is based on the 2025 value,
# as it is expected that the cost will decrease in the future due to technological advancements and economies of scale.
PV_OPEX_PARAMS_ESCALATE = {
    "industrial": {
        "type": "rooftop",
        "roof_cost_base": 0.35,     # EUR/m2/year (2025)
        "roof_base_year": 2025,
        "roof_escalation": ROOFTOP_ESCALATION,

        "fom_base": 10000,          # EUR/MW/year (2025)
        "fom_base_year": 2025,
        "fom_deescalation": FOM_DEESCALATION
    },
    "commercial": {
        "type": "rooftop",
        "roof_cost_base": 1.5,  # EUR/m2/year (2026)
        "roof_base_year": 2026,
        "roof_escalation": ROOFTOP_ESCALATION,

        "fom_base": 7000,
        "fom_base_year": 2025,
        "fom_deescalation": FOM_DEESCALATION
    },
    "residential": {
        "type": "rooftop",
        "roof_cost_base": 3.0,      # EUR/m2/year (2026)
        "roof_base_year": 2026,
        "roof_escalation": ROOFTOP_ESCALATION,

        "fom_base": 7000,
        "fom_base_year": 2025,
        "fom_deescalation": FOM_DEESCALATION,
    },
    "mixed": {
        # conservative assumption → rooftop commercial
        "type": "rooftop",
        "roof_cost_base": 1.5,
        "roof_base_year": 2026,
        "roof_escalation": ROOFTOP_ESCALATION,

        "fom_base": 7000,
        "fom_base_year": 2025,
        "fom_deescalation": FOM_DEESCALATION,
    }
}

# # ---------------------------------- WT ----------------------------------
WT_LIFETIME = 30

# Base year
WT_BASE_YEAR = 2025

# Land
COST_LAND_LEASE_WT_2025 = 0.061      # EUR/m2/year
LAND_AREA_WT = 80937.2               # m2 per MW
LAND_ESCALATION_WT = 0.03            # e.g. +3 %

# Fixed O&M
COST_FOM_WT_2025 = 38000             # EUR/MW/year
# FOM_DEESCALATION_WT = -0.01           # e.g. −1 %


# -------------------------------------- CHP Parameters --------------------------------------
land_area_chp = 46.67       # m2/MW

cost_fom_chp_2025 = 855000 * 0.03   # 3% of the investment cost

cost_ch4_import_2025 = 77           # [EUR/MWh]

# -------------------------------------- HP Parameters --------------------------------------
land_area_hp = 7.48     # m2/MW

cost_fom_hp_2025 = 30000


# -------------------------------------- P2G Parameters --------------------------------------
land_area_p2g = 29.28   # m2/MW

cost_fom_p2g_2025 = 2320000 * 0.04      # 4% of the CAPEX

import_tariff = 1   # 0%
tax = 0.6

cost_h2_import_2025 = (190)+(190*tax)
cost_h2_import_2026 = (180)+(180*tax)
cost_h2_import_2027 = (170)+(170*tax)
cost_h2_import_2028 = (160)+(160*tax)
cost_h2_import_2029 = (150)+(150*tax)
cost_h2_import_2030 = (140)+(140*tax)
cost_h2_import_2031 = (130*import_tariff)+(130*tax)
cost_h2_import_2032 = (125*import_tariff)+(125*tax)
cost_h2_import_2033 = (122*import_tariff)+(122*tax)
cost_h2_import_2034 = (120*import_tariff)+(120*tax)


# -------------------------------------- BESS Parameters --------------------------------------
bess_life_time = 15     # Hoppecke li-ion 3150 Ah battery pack

cost_land_business_2025 = 91        # [EUR/m2] To purchase land --> used for P2G, BESS
cost_land_residential_2025 = 206    # To purchase land --> used for BESS, CHP, heat pump and th storage

land_area_bess = 49.88  # [m2 per 1 MW Battery pack]

cost_fom_bess_2025 = 4598.5


# -------------------------------------- Th Storage Parameters --------------------------------------
land_area_th_storage = 20   # m2/MW

cost_fom_th_storage_2025 = 10000


# -------------------------------------- H2 Storage Parameters --------------------------------------
# Add H2 storage parameters


# -------------------------------------- Gas Gen Parameters --------------------------------------
land_area_gen = 46.67       # Same as CHP plant
cost_fom_gen_2025 = 19050


# -------------------------------------- Power Grid Parameters --------------------------------------
# Switzerland
e_price__import_eur_mwh_2025 = 166
e_price_import_eur_mwh_2026 = 169
e_price_import_eur_mwh_2027 = 171
e_price_import_eur_mwh_2028 = 173
e_price_import_eur_mwh_2029 = 175
e_price_import_eur_mwh_2030 = 177
e_price_import_eur_mwh_2031 = 179
e_price_import_eur_mwh_2032 = 181
e_price_import_eur_mwh_2033 = 183
e_price_import_eur_mwh_2034 = 184

# Germany [vbw  - Oberer Preispfad]
# e_price__import_eur_mwh_2025 = 254
# e_price_import_eur_mwh_2026 = 226
# e_price_import_eur_mwh_2027 = 202
# e_price_import_eur_mwh_2028 = 170
# e_price_import_eur_mwh_2029 = 141
# e_price_import_eur_mwh_2030 = 120
# e_price_import_eur_mwh_2031 = 120
# e_price_import_eur_mwh_2032 = 119
# e_price_import_eur_mwh_2033 = 117
# e_price_import_eur_mwh_2034 = 116

# Switzerland
e_price_export_eur_mwh_2025 = 55
e_price_export_eur_mwh_2026 = 56
e_price_export_eur_mwh_2027 = 57
e_price_export_eur_mwh_2028 = 58
e_price_export_eur_mwh_2029 = 58
e_price_export_eur_mwh_2030 = 59
e_price_export_eur_mwh_2031 = 60
e_price_export_eur_mwh_2032 = 60
e_price_export_eur_mwh_2033 = 61
e_price_export_eur_mwh_2034 = 61

# Germany [vbw - Unterer Preispfad]
# e_price_export_eur_mwh_2025 = 88
# e_price_export_eur_mwh_2026 = 82
# e_price_export_eur_mwh_2027 = 77
# e_price_export_eur_mwh_2028 = 66
# e_price_export_eur_mwh_2029 = 59
# e_price_export_eur_mwh_2030 = 54
# e_price_export_eur_mwh_2031 = 55
# e_price_export_eur_mwh_2032 = 55
# e_price_export_eur_mwh_2033 = 55
# e_price_export_eur_mwh_2034 = 55

e_price_curt_eur_mwh_2025 = 80
e_price_curt_eur_mwh_2026 = 80
e_price_curt_eur_mwh_2027 = 80
e_price_curt_eur_mwh_2028 = 80
e_price_curt_eur_mwh_2029 = 80
e_price_curt_eur_mwh_2030 = 80
e_price_curt_eur_mwh_2031 = 80
e_price_curt_eur_mwh_2032 = 80
e_price_curt_eur_mwh_2033 = 80
e_price_curt_eur_mwh_2034 = 80


class opex:
    def __init__(self, stage, year,
                 bus_to_cluster,
                 x_pv_bus, x_pv_mw,
                 x_wt_mw, **kwargs):

                 # demand_e_mwh_jan, sgen_mwh_jan, bess_mwh_jan, gas_gen_mwh_jan, ext_e_mwh_jan,
                 # x_chp_bus, x_chp_mw, chp_ch4_import_jan, chp_ch4_import_jul,
                 # x_hp_bus, x_hp_size, x_storage_th_size, x_p2g_size_mw,
                 # x_storage_h2_mwh, h2_import_jan, h2_import_jul, x_bess_bus, x_bess_mw,
                 # demand_e_mwh_jul, sgen_mwh_jul, bess_mwh_jul, gas_gen_mwh_jul, ext_e_mwh_jul,
                 # x_gen_bus_12_mw, x_gen_bus_1_mw, **kwargs):

        self.stage = stage
        self.year = year
        self.bus_to_cluster = bus_to_cluster
        # self.net_update = net_update
        self.x_pv_bus = x_pv_bus
        self.x_pv_mw = x_pv_mw
        self.x_wt_mw = x_wt_mw

    def evolve_cost(self, base_cost, base_year, target_year, annual_rate):
        """
        Generic cost evolution.
        annual_rate > 0  → escalation
        annual_rate < 0  → de-escalation
        """

        return base_cost * (1 + annual_rate) ** (target_year - base_year)

    def opex_pv(self):
        total_opex = 0.0
        year = self.year
        for bus, pv_mw in zip(self.x_pv_bus, self.x_pv_mw):
            # print("bus_idx =", bus)
            # print("pv_mw =", pv_mw)
            if pv_mw <= 0:
                continue

            label = self.bus_to_cluster.get(bus)    # e.g. "industrial_C1"
            cluster_type = label.split("_", 1)[0]   # e.g. "industrial"

            params = PV_OPEX_PARAMS_ESCALATE[cluster_type]
            # print(params)

            # ------------------- Fixed O&M cost (DE-escalating) -------------------
            fom = self.evolve_cost(
                params["fom_base"],
                params["fom_base_year"],
                year,
                params["fom_deescalation"]
            )
            # print("fom =", fom)
            fom_cost = pv_mw * fom
            # print("fom_cost =", fom_cost)
            # ------------------- Location cost (ESCALATING) -------------------
            roof_cost = self.evolve_cost(
                params["roof_cost_base"],
                params["roof_base_year"],
                year,
                params["roof_escalation"]
            )
            # print("roof_cost =", roof_cost)
            loc_cost = pv_mw * roof_cost * LAND_AREA_PV
            # print("loc_cost =", loc_cost)

            total_opex += fom_cost + loc_cost
            # print("total_opex =", total_opex)

            # ---> For Sanity test to check correct cluster assignment, correct cost (FOM and location) -->
            # print(
            #     f"Bus {bus} | {cluster_type} | "
            #     f"PV={pv_mw} MW | "
            #     f"FOM={fom_cost:.1f} | LOC={loc_cost:.1f}"
            # )

        return total_opex

    def evolve_wt_fom(self, base_cost, year):
        """
        Piecewise de-escalation of WT fixed O&M.
        2026–2030:  -1.08 % / year
        2031–2045:  -0.34 % / year
        Base year = 2025
        """

        if year <= 2025:
            return base_cost
        # Phase 1: 2026–2030
        cost_2030 = base_cost * (1 - 0.0108) ** min(year - 2025, 5)

        if year <= 2030:
            return cost_2030
        # Phase 2: 2031–2045
        return cost_2030 * (1 - 0.0034) ** (year - 2030)

    def evolve_wt_land_cost(self, base_cost, base_year, target_year, rate):
        return base_cost * (1 + rate) ** (target_year - base_year)

    def opex_wt(self):
        """
        Wind turbine OPEX for all years.
        - Land lease: escalating
        - FOM: piecewise de-escalating
        """

        total_opex = 0.0
        year = self.year
        print("Year =", year)

        for wt_mw in self.x_wt_mw:
            if wt_mw <= 0:
                continue

            # -------- Land lease (ESCALATING) --------
            land_cost = self.evolve_wt_land_cost(
                COST_LAND_LEASE_WT_2025,
                2025,
                year,
                LAND_ESCALATION_WT
            )
            land_opex = wt_mw * land_cost * LAND_AREA_WT
            print(f"WT MW={wt_mw} | Land Cost={land_cost:.4f} EUR/m2/year | |land area={LAND_AREA_WT:.2f}| "
                  f"Land OPEX={land_opex:.1f} EUR/year")

            # -------- Fixed O&M (PIECEWISE DE-ESCALATION) --------
            fom_mw = self.evolve_wt_fom(
                COST_FOM_WT_2025,
                year
            )
            fom_opex = wt_mw * fom_mw
            print(f"WT MW={wt_mw} | FOM Cost={fom_mw:.1f} EUR/MW/year | FOM OPEX={fom_opex:.1f} EUR/year")

            total_opex += land_opex + fom_opex
            print(f"Total OPEX={total_opex:.1f} EUR/year")
            print()

        return total_opex
