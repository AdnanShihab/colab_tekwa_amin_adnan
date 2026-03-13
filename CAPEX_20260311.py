"""
Stages:
stage1 = 2026-2030
stage2 = 2031-2035
stage3 =

Cost evolution for CAPEX components
For now just PV, WT and BESS CAPEX are included.

"""
from mv_oberrhein_bus_clustering_function import net_bus_clustering
from costs import PV_CAPEX
from costs import WT_CAPEX
from costs import BESS_CAPEX


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

    # def get_cluster_type(self, bus):
    #
    #     # Check each cluster type in order
    #     # if bus in [item for sublist in self.industrial_clusters.values() for item in sublist]:
    #     #     return 'industrial'
    #     # elif bus in [item for sublist in self.residential_clusters.values() for item in sublist]:
    #     #     return 'residential'
    #     # elif bus in [item for sublist in self.commercial_clusters.values() for item in sublist]:
    #     #     return 'commercial'
    #     # elif bus in [item for sublist in self.mixed_clusters.values() for item in sublist]:
    #     #     return 'mixed'
    #     # else:
    #     #     return 'other'  # Bus not found in any cluster
    #
    #     # Instantiate the clustering class
    #     cluster = net_bus_clustering(self.net)
    #     cluster.network_with_clustered_loads()
    #
    #     if any(bus in cluster for cluster in cluster.industrial_clusters.values()):
    #         return 'industrial'
    #     elif any(bus in cluster for cluster in cluster.residential_clusters.values()):
    #         return 'residential'
    #     elif any(bus in cluster for cluster in cluster.commercial_clusters.values()):
    #         return 'commercial'
    #     elif any(bus in cluster for cluster in cluster.mixed_clusters.values()):
    #         return 'mixed'
    #     else:
    #         return 'other'

    def _get_year_value(self, table, year=None):
        y = self.year if year is None else year
        # print("Requested year for CAPEX =", y)
        if y not in table:
            raise ValueError(f"No CAPEX data for year={y}")
        return table[y]

    # =================================== PV ===================================
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

    # =================================== WT ===================================
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
    def capex_bess(self):
        total_capex_bess = 0

        unit_cost = self._get_year_value(BESS_CAPEX)

        e_bess_mwh = sum(self.x_bess_mw) * self.tau_bess

        inv_cost_bess = e_bess_mwh * unit_cost
        total_capex_bess += inv_cost_bess

        return total_capex_bess

