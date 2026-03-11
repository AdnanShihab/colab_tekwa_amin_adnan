"""
Obj function

stage1 = 2025-2025
stage2 = 2026-2030
stage3 = 2031-2035
"""
from mv_oberrhein_bus_clustering_function import net_bus_clustering
from costs import PV_CAPEX
from costs import WT_CAPEX
from costs import BESS_CAPEX

# =========================================== Gas Gen Parameters ===========================================
# Considered already installed and invested

# =========================================== PV Parameters ===========================================
# land_area_pv = 9290  # [m2 per 1 MW solar]
# roof_top_area_pv = 6000  # [m2 per 1 MW solar]
#
# cost_pv_installation_2025 = 797000     # EUR/MW --> including the land development cost
# cost_pv_installation_2026 = cost_pv_installation_2025-(cost_pv_installation_2025*0.12)
# cost_pv_installation_2027 = cost_pv_installation_2026-(cost_pv_installation_2026*0.12)
# cost_pv_installation_2028 = cost_pv_installation_2027-(cost_pv_installation_2027*0.12)
# cost_pv_installation_2029 = cost_pv_installation_2028-(cost_pv_installation_2028*0.12)
# cost_pv_installation_2030 = cost_pv_installation_2029-(cost_pv_installation_2029*0.12)
# cost_pv_installation_2031 = cost_pv_installation_2030-(cost_pv_installation_2030*0.12)
# cost_pv_installation_2032 = cost_pv_installation_2031-(cost_pv_installation_2031*0.12)
# cost_pv_installation_2033 = cost_pv_installation_2032-(cost_pv_installation_2032*0.12)
# cost_pv_installation_2034 = cost_pv_installation_2033-(cost_pv_installation_2033*0.12)

# cost_land_industry_2026 = 0.35      # [EUR/m2/year]
# cost_land_industry_2027 = cost_land_industry_2026*1.78  # Source: Perplexity check the record pls

# pv_capex_industrial_2025 = 800000  # EUR/MW
# pv_capex_industrial_2026 = pv_capex_industrial_2025 - (pv_capex_industrial_2025*0.12)
# pv_capex_industrial_2027 = pv_capex_industrial_2026 - (pv_capex_industrial_2026*0.12)
# pv_capex_industrial_2028 = pv_capex_industrial_2027 - (pv_capex_industrial_2027*0.12)
# pv_capex_industrial_2029 = pv_capex_industrial_2028 - (pv_capex_industrial_2028*0.12)
# pv_capex_industrial_2030 = pv_capex_industrial_2029 - (pv_capex_industrial_2029*0.12)
# pv_capex_industrial_2031 = pv_capex_industrial_2030 - (pv_capex_industrial_2030*0.12)
# pv_capex_industrial_2032 = pv_capex_industrial_2031 - (pv_capex_industrial_2031*0.12)
# pv_capex_industrial_2033 = pv_capex_industrial_2032 - (pv_capex_industrial_2032*0.12)
# pv_capex_industrial_2034 = pv_capex_industrial_2033 - (pv_capex_industrial_2033*0.12)
# pv_capex_industrial_2035 = pv_capex_industrial_2034 - (pv_capex_industrial_2034*0.12)
# pv_capex_industrial_2036 = pv_capex_industrial_2035 - (pv_capex_industrial_2035*0.12)
# pv_capex_industrial_2037 = pv_capex_industrial_2036 - (pv_capex_industrial_2036*0.12)
# pv_capex_industrial_2038 = pv_capex_industrial_2037 - (pv_capex_industrial_2037*0.12)
# pv_capex_industrial_2039 = pv_capex_industrial_2038 - (pv_capex_industrial_2038*0.12)
# pv_capex_industrial_2040 = pv_capex_industrial_2039 - (pv_capex_industrial_2039*0.12)
# pv_capex_industrial_2041 = pv_capex_industrial_2040 - (pv_capex_industrial_2040*0.12)
# pv_capex_industrial_2042 = pv_capex_industrial_2041 - (pv_capex_industrial_2041*0.12)
# pv_capex_industrial_2043 = pv_capex_industrial_2042 - (pv_capex_industrial_2042*0.12)
# pv_capex_industrial_2044 = pv_capex_industrial_2043 - (pv_capex_industrial_2043*0.12)
# pv_capex_industrial_2045 = pv_capex_industrial_2044 - (pv_capex_industrial_2044*0.12)
#
# # .................................Old code...............................
# # cost_pv_system_rooftop_business_installation_2025 = 1000000  # EUR/MW
# # cost_pv_system_rooftop_business_installation_2026 = cost_pv_system_rooftop_business_installation_2025 - \
# #                                            (cost_pv_system_rooftop_business_installation_2025*0.12)
#
# pv_capex_commercial_2025 = 1000000  # EUR/MW
# pv_capex_commercial_2026 = pv_capex_commercial_2025 - (pv_capex_commercial_2025*0.12)
# pv_capex_commercial_2027 = pv_capex_commercial_2026 - (pv_capex_commercial_2026*0.12)
# pv_capex_commercial_2028 = pv_capex_commercial_2027 - (pv_capex_commercial_2027*0.12)
# pv_capex_commercial_2029 = pv_capex_commercial_2028 - (pv_capex_commercial_2028*0.12)
# pv_capex_commercial_2030 = pv_capex_commercial_2029 - (pv_capex_commercial_2029*0.12)
# pv_capex_commercial_2031 = pv_capex_commercial_2030 - (pv_capex_commercial_2030*0.12)
# pv_capex_commercial_2032 = pv_capex_commercial_2031 - (pv_capex_commercial_2031*0.12)
# pv_capex_commercial_2033 = pv_capex_commercial_2032 - (pv_capex_commercial_2032*0.12)
# pv_capex_commercial_2034 = pv_capex_commercial_2033 - (pv_capex_commercial_2033*0.12)
# pv_capex_commercial_2035 = pv_capex_commercial_2034 - (pv_capex_commercial_2034*0.12)
# pv_capex_commercial_2036 = pv_capex_commercial_2035 - (pv_capex_commercial_2035*0.12)
# pv_capex_commercial_2037 = pv_capex_commercial_2036 - (pv_capex_commercial_2036*0.12)
# pv_capex_commercial_2038 = pv_capex_commercial_2037 - (pv_capex_commercial_2037*0.12)
# pv_capex_commercial_2039 = pv_capex_commercial_2038 - (pv_capex_commercial_2038*0.12)
# pv_capex_commercial_2040 = pv_capex_commercial_2039 - (pv_capex_commercial_2039*0.12)
# pv_capex_commercial_2041 = pv_capex_commercial_2040 - (pv_capex_commercial_2040*0.12)
# pv_capex_commercial_2042 = pv_capex_commercial_2041 - (pv_capex_commercial_2041*0.12)
# pv_capex_commercial_2043 = pv_capex_commercial_2042 - (pv_capex_commercial_2042*0.12)
# pv_capex_commercial_2044 = pv_capex_commercial_2043 - (pv_capex_commercial_2043*0.12)
# pv_capex_commercial_2045 = pv_capex_commercial_2044 - (pv_capex_commercial_2044*0.12)
#
# # .............................. Old code ..................................
# # cost_pv_system_rooftop_household_installation_2025 = 1650000  # EUR/MW;
# # cost_pv_system_rooftop_household_installation_2026 = cost_pv_system_rooftop_household_installation_2025 - \
# #                                            (cost_pv_system_rooftop_household_installation_2025*0.12)
#
# pv_capex_residential_2025 = 1650000  # EUR/MW
# pv_capex_residential_2026 = pv_capex_residential_2025 - (pv_capex_residential_2025*0.12)
# pv_capex_residential_2027 = pv_capex_residential_2026 - (pv_capex_residential_2026*0.12)
# pv_capex_residential_2028 = pv_capex_residential_2027 - (pv_capex_residential_2027*0.12)
# pv_capex_residential_2029 = pv_capex_residential_2028 - (pv_capex_residential_2028*0.12)
# pv_capex_residential_2030 = pv_capex_residential_2029 - (pv_capex_residential_2029*0.12)
# pv_capex_residential_2031 = pv_capex_residential_2030 - (pv_capex_residential_2030*0.12)
#
# pv_capex_mixed_2025 = 1320000  # EUR/MW (Taken as average of residential and commercial PV capex in 2025)
# pv_capex_mixed_2026 = pv_capex_mixed_2025 - (pv_capex_mixed_2025*0.12)
# pv_capex_mixed_2027 = pv_capex_mixed_2026 - (pv_capex_mixed_2026*0.12)
# pv_capex_mixed_2028 = pv_capex_mixed_2027 - (pv_capex_mixed_2027*0.12)
# pv_capex_mixed_2029 = pv_capex_mixed_2028 - (pv_capex_mixed_2028*0.12)
# pv_capex_mixed_2030 = pv_capex_mixed_2029 - (pv_capex_mixed_2029*0.12)
# pv_capex_mixed_2031 = pv_capex_mixed_2030 - (pv_capex_mixed_2030*0.12)

# =========================================== WT Parameters ===========================================
# cost_wt_capex_2025 = 950000
# cost_wt_capex_2026 = 940000
# cost_wt_capex_2027 = 930000
# cost_wt_capex_2028 = 920000
# cost_wt_capex_2029 = 910000
# cost_wt_capex_2030 = 900000
# cost_wt_capex_2031 = 897000
# cost_wt_capex_2032 = 894000
# cost_wt_capex_2033 = 890000
# cost_wt_capex_2034 = 888000
# cost_wt_capex_2035 = 885000
# cost_wt_capex_2036 = 882000
# cost_wt_capex_2037 = 879000
# cost_wt_capex_2038 = 876000

# =========================================== CHP Parameters ===========================================
cost_chp_capex_2025 = 855000
cost_chp_capex_2026 = 850000
cost_chp_capex_2027 = 845000
cost_chp_capex_2028 = 840000
cost_chp_capex_2029 = 835000
cost_chp_capex_2030 = 830000
cost_chp_capex_2031 = 828000
cost_chp_capex_2032 = 827000
cost_chp_capex_2033 = 825000
cost_chp_capex_2034 = 824000
cost_chp_capex_2035 = 822500
cost_chp_capex_2036 = 821000
cost_chp_capex_2037 = 819500
cost_chp_capex_2038 = 818000


# =========================================== HP Parameters ===========================================
cost_hp_capex_2025 = 1250000
cost_hp_capex_2026 = 1250000
cost_hp_capex_2027 = 1250000
cost_hp_capex_2028 = 1250000
cost_hp_capex_2029 = 1250000
cost_hp_capex_2030 = 1250000
cost_hp_capex_2031 = 1125000    # changed
cost_hp_capex_2032 = 1125000
cost_hp_capex_2033 = 1125000
cost_hp_capex_2034 = 1125000
cost_hp_capex_2035 = 1125000
cost_hp_capex_2036 = 1012500    # changed
cost_hp_capex_2037 = 1012500
cost_hp_capex_2038 = 1012500


# =========================================== P2G Parameters ===========================================
cost_p2g_capex_2025 = 2320000
cost_p2g_capex_2026 = 1926000
cost_p2g_capex_2027 = 1532000
cost_p2g_capex_2028 = 1138000
cost_p2g_capex_2029 = 744000
cost_p2g_capex_2030 = 350000
cost_p2g_capex_2031 = 346550
cost_p2g_capex_2032 = 343100
cost_p2g_capex_2033 = 339650
cost_p2g_capex_2034 = 336200
cost_p2g_capex_2035 = 332750
cost_p2g_capex_2036 = 329300
cost_p2g_capex_2037 = 325850
cost_p2g_capex_2038 = 322400


# =========================================== BESS Parameters ===========================================
cost_bess_capex_2025 = 221629       # EUR/MWh
cost_bess_capex_2026 = 217418
cost_bess_capex_2027 = 213287
cost_bess_capex_2028 = 209234
cost_bess_capex_2029 = 205258
cost_bess_capex_2030 = 201358
cost_bess_capex_2031 = 197532
cost_bess_capex_2032 = 193779
cost_bess_capex_2033 = 190097
cost_bess_capex_2034 = 186485
cost_bess_capex_2035 = 182942
cost_bess_capex_2036 = 179466
cost_bess_capex_2037 = 176056
cost_bess_capex_2038 = 172711


# =========================================== TH Storage Parameters ===========================================
cost_storage_th_capex_2025 = 155.28
cost_storage_th_capex_2026 = 155.28
cost_storage_th_capex_2027 = 155.28
cost_storage_th_capex_2028 = 155.28
cost_storage_th_capex_2029 = 155.28
cost_storage_th_capex_2030 = 155.28
cost_storage_th_capex_2031 = 155.28
cost_storage_th_capex_2032 = 155.28
cost_storage_th_capex_2033 = 155.28
cost_storage_th_capex_2034 = 155.28
cost_storage_th_capex_2035 = 155.28
cost_storage_th_capex_2036 = 155.28
cost_storage_th_capex_2037 = 155.28
cost_storage_th_capex_2038 = 155.28


# =========================================== H2 Storage Parameters ===========================================
cost_storage_h2_capex_2025 = 0      # need to find
cost_storage_h2_capex_2026 = 0      # need to find
cost_storage_h2_capex_2027 = 0
cost_storage_h2_capex_2028 = 0
cost_storage_h2_capex_2029 = 0
cost_storage_h2_capex_2030 = 0
cost_storage_h2_capex_2031 = 0
cost_storage_h2_capex_2032 = 0
cost_storage_h2_capex_2033 = 0
cost_storage_h2_capex_2034 = 0
cost_storage_h2_capex_2035 = 0
cost_storage_h2_capex_2036 = 0
cost_storage_h2_capex_2037 = 0
cost_storage_h2_capex_2038 = 0


class CAPEX:
    def __init__(self, stage, year,
                 x_pv_bus, x_pv_mw,
                 x_wt_bus, x_wt_mw,
                 x_bess_bus, x_bess_mw, tau_bess,
                 bus_to_cluster=None, **kwargs):
                 # net, x_chp_bus, x_chp_mw, x_hp_bus, x_hp_size, x_storage_th_size, x_p2g_size_mw,
                 # x_storage_h2_mwh,  **kwargs):
        # self.net = net
        self.stage = stage
        self.year = year
        self.bus_to_cluster = bus_to_cluster or {}
        self.x_pv_bus = x_pv_bus
        self.x_pv_mw = x_pv_mw
        self.x_wt_bus = x_wt_bus
        self.x_wt_mw = x_wt_mw
        self.x_bess_bus = x_bess_bus
        self.x_bess_mw = x_bess_mw
        self.tau_bess = tau_bess    # tau = duration of BESS in hours
                                    # Tau is how many hours the battery can discharge at its rated power until empty

        # self.x_chp_bus = x_chp_bus
        # self.x_chp_mw = x_chp_mw
        # self.x_hp_bus = x_hp_bus
        # self.x_hp_size = x_hp_size
        # self.x_storage_th_size = x_storage_th_size
        # self.x_p2g_size_mw = x_p2g_size_mw
        # self.x_storage_h2_mwh = x_storage_h2_mwh
        # self.x_bess_bus = x_bess_bus
        # self.x_bess_mw = x_bess_mw

        # self.demand_e_mwh = demand_e_mwh
        # self.sgen_mwh = sgen_mwh
        # self.bess_mwh = bess_mwh
        # self.gas_gen_mwh = gas_gen_mwh
        # self.ext_e_mwh = ext_e_mwh

        # ------------------------------- Define the clusters -------------------------------
        # self.industrial_clusters = {
        #     "C1": [72, 108, 289, 269, 110, 75, 196, 103, 101, 106],
        #     "C2": [6, 5, 7, 241, 24, 290, 4, 242, 243, 244, 8, 245],
        #     "C3": [71, 81, 73, 77, 119, 80, 117, 35, 45, 47, 148, 120, 49, 52, 55, 146, 145],
        # }
        # self.residential_clusters = {
        #     "C1": [48, 50, 44, 192, 42, 51, 34, 76],
        #     "C2": [161, 38, 173, 174, 162],
        # }
        # self.commercial_clusters = {
        #     "C1": [82, 79, 190, 64, 65, 36],
        # }
        # self.mixed_clusters = {
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

    def get_cluster_type(self, bus):

        # Check each cluster type in order
        # if bus in [item for sublist in self.industrial_clusters.values() for item in sublist]:
        #     return 'industrial'
        # elif bus in [item for sublist in self.residential_clusters.values() for item in sublist]:
        #     return 'residential'
        # elif bus in [item for sublist in self.commercial_clusters.values() for item in sublist]:
        #     return 'commercial'
        # elif bus in [item for sublist in self.mixed_clusters.values() for item in sublist]:
        #     return 'mixed'
        # else:
        #     return 'other'  # Bus not found in any cluster

        # Instantiate the clustering class
        cluster = net_bus_clustering(self.net)
        cluster.network_with_clustered_loads()

        if any(bus in cluster for cluster in cluster.industrial_clusters.values()):
            return 'industrial'
        elif any(bus in cluster for cluster in cluster.residential_clusters.values()):
            return 'residential'
        elif any(bus in cluster for cluster in cluster.commercial_clusters.values()):
            return 'commercial'
        elif any(bus in cluster for cluster in cluster.mixed_clusters.values()):
            return 'mixed'
        else:
            return 'other'

    def _get_year_value(self, table, year=None):
        y = self.year if year is None else year
        # print("Requested year for CAPEX =", y)
        if y not in table:
            raise ValueError(f"No CAPEX data for year={y}")
        return table[y]

    # =================================================== 2026 ==================================================
    # ---------------------------- PV CAPEX ----------------------------
    def capex_pv_2026(self):
        total_capex_pv = 0  # it should be zero at the beginning

        # for idx, row in self.net.load.iterrows():
        #     print("idx =", idx)
        #     print("row =", row['p_mw'])
        #     print("len load =", len(self.net.load))
        #     print("len x_pv_mw =", len(self.x_pv_mw))
        #
        #     # --- Industrial loads ---
        #     if row['p_mw'] >= 0.50:
        #         # print("Ind loads bus idx =\n", row['bus'])
        #         # bus_ind = row['bus']
        #
        #         print("PV in Industrial area")
        #         pv_mw = self.x_pv_mw[idx]
        #         # print("pv_size =", pv_mw)
        #
        #         inv_cost_pv = (pv_mw * pv_capex_industrial_2026)
        #         total_capex_pv += inv_cost_pv
        #         # print("total_capex_pv_industrial =\n", total_capex_pv)
        #
        #     # --- Residential loads ---
        #     elif row['p_mw'] < 0.3:
        #         print("pv in Residential area")
        #         # print("Res loads bus idx =\n", row['bus'])
        #
        #         pv_mw = self.x_pv_mw[idx]
        #         # print("pv_size =\n", pv_mw)
        #
        #         inv_cost_pv = (pv_mw * pv_capex_residential_2026)
        #         total_capex_pv += inv_cost_pv
        #         # print("total_capex_pv_residential =\n", total_capex_pv)
        #         # print("Actual calc =\n", 701360*pv_mw)
        #
        #     # --- Commercial loads ---
        #     else:
        #         print("PV in Commercial area")
        #         pv_mw = self.x_pv_mw[idx]
        #         inv_cost_pv = (pv_mw * pv_capex_commercial_2026)
        #         total_capex_pv += inv_cost_pv
        #         # print("capex_pv_commercial =", total_capex_pv)
        #
        # # print("total_capex_pv =\n", total_capex_pv)
        # # print()

        # for i in range(len(self.x_pv_bus)):
        #     bus = self.x_pv_bus[i]
        #     pv_mw = self.x_pv_mw[i]
        #     cluster_type = self.get_cluster_type(bus)

        for bus, pv_mw in zip(self.x_pv_bus, self.x_pv_mw):
            label = self.bus_to_cluster.get(bus)  # e.g. "industrial_C1"

            cluster_type = label.split("_", 1)[0]  # -> "industrial"

            if cluster_type == 'industrial':
                inv_cost = pv_mw * pv_capex_industrial_2026
                # print("industrial inv_cost=", inv_cost)
            elif cluster_type == 'residential':
                inv_cost = pv_mw * pv_capex_residential_2026
            elif cluster_type == 'commercial':
                inv_cost = pv_mw * pv_capex_commercial_2026
            elif cluster_type == 'mixed':
                inv_cost = pv_mw * pv_capex_mixed_2026
                # print("mixed inv_cost=", inv_cost)
            else:
                inv_cost = 0
                print(f"Warning: Bus {bus} not found in any cluster.")

            total_capex_pv += inv_cost

        # print(f"Total CAPEX for PV in 2026: {total_capex_pv} EUR")
        return total_capex_pv

        # OLD CODE:
        # for i_x_pv_bus, i_x_pv_size in zip(self.x_pv_bus, self.x_pv_mw):
        #     print(i_x_pv_bus)
        #     print(i_x_pv_size)
        #
        #     if v_x_pv_bus == 1:  # Che Ind area
        #         # print("PV in Industrial area - bus 1")
        #         pv_size = v_x_pv_size
        #         # print("pv_size =", pv_size)
        #         inv_cost_pv = (pv_size * cost_pv_installation_2025)
        #         total_price_investment_pv_2025 += inv_cost_pv
        #         # print(inv_cost_pv)
        #     elif v_x_pv_bus == 2:
        #         # print("PV in Industrial area - bus 2")
        #         pv_size = v_x_pv_size
        #         # print("pv_size =", pv_size)
        #         inv_cost_pv = (pv_size * cost_pv_installation_2025)
        #         total_price_investment_pv_2025 += inv_cost_pv
        #         # print("price =", inv_cost_pv)
        #     elif v_x_pv_bus == 12:
        #         # print("PV in Industrial area - bus 12")
        #         pv_size = v_x_pv_size
        #         # print("pv_size =", pv_size)
        #         inv_cost_pv = (pv_size * cost_pv_installation_2025)
        #         total_price_investment_pv_2025 += inv_cost_pv
        #         # print(inv_cost_pv)
        #     elif v_x_pv_bus == 13:
        #         # print("PV in Industrial area - bus 13")
        #         pv_size = v_x_pv_size
        #         # print("pv_size =", pv_size)
        #         inv_cost_pv = (pv_size * cost_pv_installation_2025)
        #         total_price_investment_pv_2025 += inv_cost_pv
        #         # print(inv_cost_pv)
        #     elif v_x_pv_bus == 14:
        #         # print("PV in Industrial area - bus 13")
        #         pv_size = v_x_pv_size
        #         # print("pv_size =", pv_size)
        #         inv_cost_pv = (pv_size * cost_pv_installation_2025)
        #         total_price_investment_pv_2025 += inv_cost_pv
        #         # print(inv_cost_pv)
        #     elif v_x_pv_bus == 3:  # commercial area
        #         pv_size = v_x_pv_size
        #         # print("pv_size =", pv_size)
        #         inv_cost_pv = (pv_size * cost_pv_system_rooftop_business_installation_2025)
        #         total_price_investment_pv_2025 += inv_cost_pv
        #         # print(inv_cost_pv)
        #     elif v_x_pv_bus == 4:   # commercial area
        #         pv_size = v_x_pv_size
        #         # print("pv_size =", pv_size)
        #         inv_cost_pv = (pv_size * cost_pv_system_rooftop_business_installation_2025)
        #         total_price_investment_pv_2025 += inv_cost_pv
        #     elif v_x_pv_bus == 5:  # commercial area
        #         pv_size = v_x_pv_size
        #         # print("pv_size =", pv_size)
        #         inv_cost_pv = (pv_size * cost_pv_system_rooftop_business_installation_2025)
        #         total_price_investment_pv_2025 += inv_cost_pv
        #         # print(inv_cost_pv)
        #     elif v_x_pv_bus == 7:  # commercial area
        #         pv_size = v_x_pv_size
        #         # print("pv_size =", pv_size)
        #         inv_cost_pv = (pv_size * cost_pv_system_rooftop_business_installation_2025)
        #         total_price_investment_pv_2025 += inv_cost_pv
        #         # print(inv_cost_pv)
        #     elif v_x_pv_bus == 8:  # commercial area
        #         pv_size = v_x_pv_size
        #         # print("pv_size =", pv_size)
        #         inv_cost_pv = (pv_size * cost_pv_system_rooftop_business_installation_2025)
        #         total_price_investment_pv_2025 += inv_cost_pv
        #         # print(inv_cost_pv)
        #     elif v_x_pv_bus == 9:  # commercial area
        #         pv_size = v_x_pv_size
        #         # print("pv_size =", pv_size)
        #         inv_cost_pv = (pv_size * cost_pv_system_rooftop_business_installation_2025)
        #         total_price_investment_pv_2025 += inv_cost_pv
        #         # print(inv_cost_pv)
        #     elif v_x_pv_bus == 10:  # commercial area
        #         pv_size = v_x_pv_size
        #         # print("pv_size =", pv_size)
        #         inv_cost_pv = (pv_size * cost_pv_system_rooftop_business_installation_2025)
        #         total_price_investment_pv_2025 += inv_cost_pv
        #         # print(inv_cost_pv)
        #     elif v_x_pv_bus == 11:  # commercial area
        #         pv_size = v_x_pv_size
        #         # print("pv_size =", pv_size)
        #         inv_cost_pv = (pv_size * cost_pv_system_rooftop_business_installation_2025)
        #         total_price_investment_pv_2025 += inv_cost_pv
        #         # print(inv_cost_pv)
        #     elif v_x_pv_bus == 6:  # Household bus
        #         pv_size = v_x_pv_size
        #         # print("pv_size =", pv_size)
        #         inv_cost_pv = (pv_size * cost_pv_system_rooftop_household_installation_2025)
        #         total_price_investment_pv_2025 += inv_cost_pv
        #         # print("price =", inv_cost_pv)
        #     else:
        #         print("missing bus bars in the grid")
        #
        # return total_investment_cost_pv_2026

    def capex_pv_202603(self):      # Updated on 20260223, I dont have to add CAPEX prices separately.
                                    # No net required
        total_capex_pv = 0.0
        # e.g. {"industrial": ..., "residential": ..., "commercial": ..., "mixed": ...}
        pv_capex_by_type = self._get_year_value(PV_CAPEX)
        # print("pv_capex_by_type:", pv_capex_by_type)
        for bus, pv_mw in zip(self.x_pv_bus, self.x_pv_mw):
            label = self.bus_to_cluster.get(bus)  # e.g. "industrial_C1"

            cluster_type = label.split("_", 1)[0]

            unit_cost = pv_capex_by_type.get(cluster_type)

            total_capex_pv += pv_mw * unit_cost
            # print(f"Bus {bus}: cluster={cluster_type}, pv_mw={pv_mw}, unit_cost={unit_cost}, capex={pv_mw * unit_cost}")

        return total_capex_pv

    def capex_pv_test(self):

        total_capex_pv = 0  # it should be zero at the beginning
        print("Year", self.year)

        if self.year == 2026:
            for i in range(len(self.x_pv_bus)):
                bus = self.x_pv_bus[i]
                pv_mw = self.x_pv_mw[i]
                cluster_type = self.get_cluster_type(bus)

                if cluster_type == 'industrial':
                    inv_cost = pv_mw * pv_capex_industrial_2026
                    # print("industrial inv_cost=", inv_cost)
                elif cluster_type == 'residential':
                    inv_cost = pv_mw * pv_capex_residential_2026
                elif cluster_type == 'commercial':
                    inv_cost = pv_mw * pv_capex_commercial_2026
                elif cluster_type == 'mixed':
                    inv_cost = pv_mw * pv_capex_mixed_2026
                    # print("mixed inv_cost=", inv_cost)
                else:
                    inv_cost = 0
                    print(f"Warning: Bus {bus} not found in any cluster.")

                total_capex_pv += inv_cost

        elif self.year == 2031:
            # -----------------------------
            # --- Change pv_capex_industrial/commercial/residential_YEAR
            # -----------------------------

            for i in range(len(self.x_pv_bus)):
                bus = self.x_pv_bus[i]
                pv_mw = self.x_pv_mw[i]
                cluster_type = self.get_cluster_type(bus)

                if cluster_type == 'industrial':
                    inv_cost = pv_mw * pv_capex_industrial_2031
                    # print("industrial inv_cost=", inv_cost)
                elif cluster_type == 'residential':
                    inv_cost = pv_mw * pv_capex_residential_2031
                elif cluster_type == 'commercial':
                    inv_cost = pv_mw * pv_capex_commercial_2031
                elif cluster_type == 'mixed':
                    inv_cost = pv_mw * pv_capex_mixed_2031
                    # print("mixed inv_cost=", inv_cost)
                else:
                    inv_cost = 0
                    print(f"Warning: Bus {bus} not found in any cluster.")

                total_capex_pv += inv_cost

        # print(f"Total CAPEX for PV in 2026: {total_capex_pv} EUR")
        return total_capex_pv

    # ---------------------------- PV ----------------------------
    def capex_pv(self):  # This needs Net for the calculation
        pv_capex_by_cluster = self._get_year_value(PV_CAPEX)  # dict by cluster type
        total = 0.0
        for bus, pv_mw in zip(self.x_pv_bus, self.x_pv_mw):
            cluster = self.get_cluster_type(bus)
            unit = pv_capex_by_cluster.get(cluster)
            if unit is None:
                # either skip, warn, or raise
                continue
            total += pv_mw * unit
        print("Total CAPEX for PV in", self.year, ":", total, "EUR")
        return total

# =================================== WT ===================================
    def capex_wt_2026(self):
        # -----------------------------
        # --- Change cost_wt_capex_YEAR
        # -----------------------------

        total_capex_wt = 0

        # print("WT size =", self.x_wt_mw)

        inv_cost_wt = (self.x_wt_mw * cost_wt_capex_2026)
        total_capex_wt += inv_cost_wt.sum()     # I have 4 WTs, so I am summing here

        # print("total_capex_wt =\n", total_capex_wt)
        # print()

        return total_capex_wt

    def capex_wt(self):
        # -------------------------------
        # Updated on 20260223
        # CAPEX WT where I do not have to add CAPEX prices separately.
        # I can just call the cost_wt_capex_YEAR from the _get_year_value table.
        # No Net required
        # -------------------------------
        total_capex_wt = 0

        unit_cost = self._get_year_value(WT_CAPEX)
        for wt_mw in self.x_wt_mw:
            total_capex_wt += wt_mw * unit_cost

        return total_capex_wt

# =================================== BESS ===================================
    def capex_bess_2026(self):
        # -------------------------------
        # --- Change bess_capex_"YEAR"
        # -------------------------------

        total_capex_bess = 0

        # print("BESS X MW =", self.x_bess_mw)
        # print("BESS X MW Total =", sum(self.x_bess_mw))
        # print("BESS size MWh =", sum(self.x_bess_mw)*self.tau_bess)

        # NOTE: Total capacity of BESS in MWh = sum of all BESS power in MW * tau (duration in hours)
        # Be aware that soc_init in 50%. So bess_mwh_initial = 0.5 * (sum(self.x_bess_mw) * self.tau_bess)

        # Calculating E-bess:
        e_bess_mwh = sum(self.x_bess_mw) * self.tau_bess       # [MW * h = MWh]
        # tau (τ) = Duration (hours)
        # Tau is how many hours the battery can discharge at its rated power until empty

        inv_cost_bess = e_bess_mwh * cost_bess_capex_2026   # [MWh*EUR/MWh = EUR]

        total_capex_bess += inv_cost_bess

        # print("e_bess_mwh =", e_bess_mwh)
        # print("total_capex_bess =", total_capex_bess)

        return total_capex_bess

    def capex_bess(self):
        total_capex_bess = 0

        unit_cost = self._get_year_value(BESS_CAPEX)

        e_bess_mwh = sum(self.x_bess_mw) * self.tau_bess

        inv_cost_bess = e_bess_mwh * unit_cost
        total_capex_bess += inv_cost_bess

        return total_capex_bess

    # ---------------------------- CHP CAPEX calc 2025 ----------------------------
    def price_capex_chp_2025(self):
        total_price_capex_chp_2025 = 0

        inv_cost_chp = (self.x_chp_mw * cost_chp_capex_2025)
        total_price_capex_chp_2025 += inv_cost_chp

        return total_price_capex_chp_2025

    # ---------------------------- HP CAPEX calc 2025 ----------------------------
    def price_capex_hp_2025(self):
        total_price_capex_hp_2025 = 0

        inv_cost_hp = (self.x_hp_size * cost_hp_capex_2025)
        total_price_capex_hp_2025 += inv_cost_hp

        return total_price_capex_hp_2025

    # ---------------------------- Th_Storage CAPEX calc 2025 ----------------------------
    def price_capex_storage_th_2025(self):
        total_price_capex_storage_th_2025 = 0

        inv_cost_storage_th = (self.x_storage_th_size * cost_storage_th_capex_2025)
        total_price_capex_storage_th_2025 += inv_cost_storage_th

        return total_price_capex_storage_th_2025

    # ---------------------------- P2G CAPEX calc 2025 ----------------------------
    def price_capex_p2g_2025(self):
        total_price_capex_p2g_2025 = 0

        inv_cost_p2g = (self.x_p2g_size_mw * cost_p2g_capex_2025)
        total_price_capex_p2g_2025 += inv_cost_p2g

        return total_price_capex_p2g_2025

    # ---------------------------- H2 Storage CAPEX calc 2025 ----------------------------
    def price_capex_h2_storage_2025(self):
        total_price_capex_h2_storage_2025 = 0

        inv_cost_h2_storage = (self.x_storage_h2_mwh * cost_storage_h2_capex_2025)
        total_price_capex_h2_storage_2025 += inv_cost_h2_storage

        return total_price_capex_h2_storage_2025



    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2026 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def price_capex_2026(self):

        capex_tot_2026 = 0

        # -------------------------- PV --------------------------
        pv_tot_mw = self.x_pv_size.sum()
        inv_cost_pv = pv_tot_mw * cost_pv_installation_2026

        # ---------------------------- WT ----------------------------
        inv_cost_wt = self.x_wt_mw * cost_wt_capex_2026

        # ---------------------------- CHP ----------------------------
        inv_cost_chp = self.x_chp_mw * cost_chp_capex_2026

        # ---------------------------- HP  ----------------------------
        inv_cost_hp = self.x_hp_size * cost_hp_capex_2026

        # ---------------------------- Th_Storage  ----------------------------
        inv_cost_storage_th = self.x_storage_th_size * cost_storage_th_capex_2026

        # ---------------------------- P2G ----------------------------
        inv_cost_p2g = self.x_p2g_size_mw * cost_p2g_capex_2026

        # ---------------------------- H2 Storage ----------------------------
        inv_cost_h2_storage = self.x_storage_h2_mwh * cost_storage_h2_capex_2026

        # ---------------------------- BESS ----------------------------
        inv_cost_bess = self.x_bess_mw * cost_bess_capex_2026

        capex_tot_2026 += inv_cost_pv + inv_cost_wt + inv_cost_chp + inv_cost_hp + inv_cost_storage_th + \
                          inv_cost_p2g + inv_cost_h2_storage + inv_cost_bess

        return capex_tot_2026

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2027 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # Note: cost_pv_installation_YEAR, cost_wt_capex_YEAR, cost_chp_capex_YEAR,
    def price_capex_2027(self):
        capex_tot_2027 = 0

        # -------------------------- PV --------------------------
        pv_tot_mw = self.x_pv_size.sum()
        inv_cost_pv = pv_tot_mw * cost_pv_installation_2027

        # ---------------------------- WT ----------------------------
        inv_cost_wt = self.x_wt_mw * cost_wt_capex_2027

        # ---------------------------- CHP ----------------------------
        inv_cost_chp = self.x_chp_mw * cost_chp_capex_2027

        # ---------------------------- HP  ----------------------------
        inv_cost_hp = self.x_hp_size * cost_hp_capex_2027

        # ---------------------------- Th_Storage  ----------------------------
        inv_cost_storage_th = self.x_storage_th_size * cost_storage_th_capex_2027

        # ---------------------------- P2G ----------------------------
        inv_cost_p2g = self.x_p2g_size_mw * cost_p2g_capex_2027

        # ---------------------------- H2 Storage ----------------------------
        inv_cost_h2_storage = self.x_storage_h2_mwh * cost_storage_h2_capex_2027

        # ---------------------------- BESS ----------------------------
        inv_cost_bess = self.x_bess_mw * cost_bess_capex_2027

        capex_tot_2027 += inv_cost_pv + inv_cost_wt + inv_cost_chp + inv_cost_hp + inv_cost_storage_th + \
                          inv_cost_p2g + inv_cost_h2_storage + inv_cost_bess

        return capex_tot_2027

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2028 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # Note: cost_pv_installation_YEAR, cost_wt_capex_YEAR, cost_chp_capex_YEAR, cost_hp_capex_YEAR
    def price_capex_2028(self):
        capex_tot_2028 = 0

        # -------------------------- PV --------------------------
        pv_tot_mw = self.x_pv_size.sum()
        inv_cost_pv = pv_tot_mw * cost_pv_installation_2028

        # ---------------------------- WT ----------------------------
        inv_cost_wt = self.x_wt_mw * cost_wt_capex_2028

        # ---------------------------- CHP ----------------------------
        inv_cost_chp = self.x_chp_mw * cost_chp_capex_2028

        # ---------------------------- HP  ----------------------------
        inv_cost_hp = self.x_hp_size * cost_hp_capex_2028

        # ---------------------------- Th_Storage  ----------------------------
        inv_cost_storage_th = self.x_storage_th_size * cost_storage_th_capex_2028

        # ---------------------------- P2G ----------------------------
        inv_cost_p2g = self.x_p2g_size_mw * cost_p2g_capex_2028

        # ---------------------------- H2 Storage ----------------------------
        inv_cost_h2_storage = self.x_storage_h2_mwh * cost_storage_h2_capex_2028

        # ---------------------------- BESS ----------------------------
        inv_cost_bess = self.x_bess_mw * cost_bess_capex_2028

        capex_tot_2028 += inv_cost_pv + inv_cost_wt + inv_cost_chp + inv_cost_hp + inv_cost_storage_th + \
                          inv_cost_p2g + inv_cost_h2_storage + inv_cost_bess

        return capex_tot_2028

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2029 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # Note: cost_pv_installation_YEAR, cost_wt_capex_YEAR, cost_chp_capex_YEAR, cost_hp_capex_YEAR
    def price_capex_2029(self):
        capex_tot_2029 = 0

        # -------------------------- PV --------------------------
        pv_tot_mw = self.x_pv_size.sum()
        inv_cost_pv = pv_tot_mw * cost_pv_installation_2029

        # ---------------------------- WT ----------------------------
        inv_cost_wt = self.x_wt_mw * cost_wt_capex_2029

        # ---------------------------- CHP ----------------------------
        inv_cost_chp = self.x_chp_mw * cost_chp_capex_2029

        # ---------------------------- HP  ----------------------------
        inv_cost_hp = self.x_hp_size * cost_hp_capex_2029

        # ---------------------------- Th_Storage  ----------------------------
        inv_cost_storage_th = self.x_storage_th_size * cost_storage_th_capex_2029

        # ---------------------------- P2G ----------------------------
        inv_cost_p2g = self.x_p2g_size_mw * cost_p2g_capex_2029

        # ---------------------------- H2 Storage ----------------------------
        inv_cost_h2_storage = self.x_storage_h2_mwh * cost_storage_h2_capex_2029

        # ---------------------------- BESS ----------------------------
        inv_cost_bess = self.x_bess_mw * cost_bess_capex_2029

        capex_tot_2029 += inv_cost_pv + inv_cost_wt + inv_cost_chp + inv_cost_hp + inv_cost_storage_th + \
                          inv_cost_p2g + inv_cost_h2_storage + inv_cost_bess

        return capex_tot_2029

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2030 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # Note: cost_pv_installation_YEAR, cost_wt_capex_YEAR, cost_chp_capex_YEAR, cost_hp_capex_YEAR
    def price_capex_2030(self):
        capex_tot_2030 = 0

        # -------------------------- PV --------------------------
        pv_tot_mw = self.x_pv_size.sum()
        inv_cost_pv = pv_tot_mw * cost_pv_installation_2030

        # ---------------------------- WT ----------------------------
        inv_cost_wt = self.x_wt_mw * cost_wt_capex_2030

        # ---------------------------- CHP ----------------------------
        inv_cost_chp = self.x_chp_mw * cost_chp_capex_2030

        # ---------------------------- HP  ----------------------------
        inv_cost_hp = self.x_hp_size * cost_hp_capex_2030

        # ---------------------------- Th_Storage  ----------------------------
        inv_cost_storage_th = self.x_storage_th_size * cost_storage_th_capex_2030

        # ---------------------------- P2G ----------------------------
        inv_cost_p2g = self.x_p2g_size_mw * cost_p2g_capex_2030

        # ---------------------------- H2 Storage ----------------------------
        inv_cost_h2_storage = self.x_storage_h2_mwh * cost_storage_h2_capex_2030

        # ---------------------------- BESS ----------------------------
        inv_cost_bess = self.x_bess_mw * cost_bess_capex_2030

        capex_tot_2030 += inv_cost_pv + inv_cost_wt + inv_cost_chp + inv_cost_hp + inv_cost_storage_th + \
                          inv_cost_p2g + inv_cost_h2_storage + inv_cost_bess

        return capex_tot_2030

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2031 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # Note: cost_pv_installation_YEAR, cost_wt_capex_YEAR, cost_chp_capex_YEAR, cost_hp_capex_YEAR
    def price_capex_2031(self):
        capex_tot_2031 = 0

        # -------------------------- PV --------------------------
        pv_tot_mw = self.x_pv_size.sum()
        inv_cost_pv = pv_tot_mw * cost_pv_installation_2031

        # ---------------------------- WT ----------------------------
        inv_cost_wt = self.x_wt_mw * cost_wt_capex_2031

        # ---------------------------- CHP ----------------------------
        inv_cost_chp = self.x_chp_mw * cost_chp_capex_2031

        # ---------------------------- HP  ----------------------------
        inv_cost_hp = self.x_hp_size * cost_hp_capex_2031

        # ---------------------------- Th_Storage  ----------------------------
        inv_cost_storage_th = self.x_storage_th_size * cost_storage_th_capex_2031

        # ---------------------------- P2G ----------------------------
        inv_cost_p2g = self.x_p2g_size_mw * cost_p2g_capex_2031

        # ---------------------------- H2 Storage ----------------------------
        inv_cost_h2_storage = self.x_storage_h2_mwh * cost_storage_h2_capex_2031

        # ---------------------------- BESS ----------------------------
        inv_cost_bess = self.x_bess_mw * cost_bess_capex_2031

        capex_tot_2031 += inv_cost_pv + inv_cost_wt + inv_cost_chp + inv_cost_hp + inv_cost_storage_th + \
                          inv_cost_p2g + inv_cost_h2_storage + inv_cost_bess

        return capex_tot_2031

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2032 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # Note: cost_pv_installation_YEAR, cost_wt_capex_YEAR, cost_chp_capex_YEAR, cost_hp_capex_YEAR
    def price_capex_2032(self):
        capex_tot_2032 = 0

        # -------------------------- PV --------------------------
        pv_tot_mw = self.x_pv_size.sum()
        inv_cost_pv = pv_tot_mw * cost_pv_installation_2032

        # ---------------------------- WT ----------------------------
        inv_cost_wt = self.x_wt_mw * cost_wt_capex_2032

        # ---------------------------- CHP ----------------------------
        inv_cost_chp = self.x_chp_mw * cost_chp_capex_2032

        # ---------------------------- HP  ----------------------------
        inv_cost_hp = self.x_hp_size * cost_hp_capex_2032

        # ---------------------------- Th_Storage  ----------------------------
        inv_cost_storage_th = self.x_storage_th_size * cost_storage_th_capex_2032

        # ---------------------------- P2G ----------------------------
        inv_cost_p2g = self.x_p2g_size_mw * cost_p2g_capex_2032

        # ---------------------------- H2 Storage ----------------------------
        inv_cost_h2_storage = self.x_storage_h2_mwh * cost_storage_h2_capex_2032

        # ---------------------------- BESS ----------------------------
        inv_cost_bess = self.x_bess_mw * cost_bess_capex_2032

        capex_tot_2032 += inv_cost_pv + inv_cost_wt + inv_cost_chp + inv_cost_hp + inv_cost_storage_th + \
                          inv_cost_p2g + inv_cost_h2_storage + inv_cost_bess

        return capex_tot_2032

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2033 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # Note: cost_pv_installation_YEAR, cost_wt_capex_YEAR, cost_chp_capex_YEAR, cost_hp_capex_YEAR
    def price_capex_2033(self):
        # >>>>>>>>>>>>> CHANGE >>>>>>>>>>>>>>>
        capex_tot_2033 = 0

        # -------------------------- PV --------------------------
        pv_tot_mw = self.x_pv_size.sum()
        inv_cost_pv = pv_tot_mw * cost_pv_installation_2033

        # ---------------------------- WT ----------------------------
        inv_cost_wt = self.x_wt_mw * cost_wt_capex_2033

        # ---------------------------- CHP ----------------------------
        inv_cost_chp = self.x_chp_mw * cost_chp_capex_2033

        # ---------------------------- HP  ----------------------------
        inv_cost_hp = self.x_hp_size * cost_hp_capex_2033

        # ---------------------------- Th_Storage  ----------------------------
        inv_cost_storage_th = self.x_storage_th_size * cost_storage_th_capex_2033

        # ---------------------------- P2G ----------------------------
        inv_cost_p2g = self.x_p2g_size_mw * cost_p2g_capex_2033

        # ---------------------------- H2 Storage ----------------------------
        inv_cost_h2_storage = self.x_storage_h2_mwh * cost_storage_h2_capex_2033

        # ---------------------------- BESS ----------------------------
        inv_cost_bess = self.x_bess_mw * cost_bess_capex_2033

        capex_tot_2033 += inv_cost_pv + inv_cost_wt + inv_cost_chp + inv_cost_hp + inv_cost_storage_th + \
                          inv_cost_p2g + inv_cost_h2_storage + inv_cost_bess

        return capex_tot_2033

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2034 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # Note: cost_pv_installation_YEAR, cost_wt_capex_YEAR, cost_chp_capex_YEAR, cost_hp_capex_YEAR
    def price_capex_2034(self):
        # >>>>>>>>>>>>> CHANGE >>>>>>>>>>>>>>>
        capex_tot_2034 = 0

        # >>>>>>>>>>>>> CHANGE for all the element price >>>>>>>>>>>>>>>
        # -------------------------- PV --------------------------
        pv_tot_mw = self.x_pv_size.sum()
        inv_cost_pv = pv_tot_mw * cost_pv_installation_2034

        # ---------------------------- WT ----------------------------
        inv_cost_wt = self.x_wt_mw * cost_wt_capex_2034

        # ---------------------------- CHP ----------------------------
        inv_cost_chp = self.x_chp_mw * cost_chp_capex_2034

        # ---------------------------- HP  ----------------------------
        inv_cost_hp = self.x_hp_size * cost_hp_capex_2034

        # ---------------------------- Th_Storage  ----------------------------
        inv_cost_storage_th = self.x_storage_th_size * cost_storage_th_capex_2034

        # ---------------------------- P2G ----------------------------
        inv_cost_p2g = self.x_p2g_size_mw * cost_p2g_capex_2034

        # ---------------------------- H2 Storage ----------------------------
        inv_cost_h2_storage = self.x_storage_h2_mwh * cost_storage_h2_capex_2034

        # ---------------------------- BESS ----------------------------
        inv_cost_bess = self.x_bess_mw * cost_bess_capex_2034

        capex_tot_2034 += inv_cost_pv + inv_cost_wt + inv_cost_chp + inv_cost_hp + inv_cost_storage_th + \
                          inv_cost_p2g + inv_cost_h2_storage + inv_cost_bess

        return capex_tot_2034