"""
Stages:
stage1 = 2026-2030
stage2 = 2031-2035
stage3 =
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

