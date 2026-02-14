import pandapower as pp

class net_bus_clustering:
    def __init__(self, net):
        self.net = net

    def network_with_clustered_loads(self):
        # -------------------------------------------------
        # 1. Clear existing loads and sgens
        # -------------------------------------------------
        self.net.load.drop(self.net.load.index, inplace=True)
        self.net.sgen.drop(self.net.sgen.index, inplace=True)

        all_buses = set(self.net.bus.index)

        # -------------------------------------------------
        # 2. Define predefined clusters
        # -------------------------------------------------
        self.industrial_clusters = {
            "C1": [72, 108, 289, 269, 110, 75, 196, 103, 101, 106],
            "C2": [6, 5, 7, 241, 290, 4, 242, 243, 244, 8, 245],  # removed 24
            "C3": [71, 81, 73, 77, 119, 80, 117, 35, 45, 47, 148,
                   120, 49, 52, 55, 146, 145],
        }

        self.residential_clusters = {
            "C1": [48, 50, 44, 192, 42, 51, 34, 76],
            "C2": [161, 38, 173, 174, 162],
        }

        self.commercial_clusters = {
            "C1": [82, 79, 190, 64, 65, 36],
        }

        # -------------------------------------------------
        # 3. Automatically create mixed cluster
        # -------------------------------------------------
        predefined_buses = set().union(
            *self.industrial_clusters.values(),
            *self.residential_clusters.values(),
            *self.commercial_clusters.values()
        )

        remaining_buses = sorted(all_buses - predefined_buses)

        self.mixed_clusters = {
            "C1": remaining_buses
        }

        # -------------------------------------------------
        # 4. Define load parameters per category
        # -------------------------------------------------
        # Here, the mixed bus are getting residential time-series. So there is a 200W load difference.
        load_params = {
            "industrial":  dict(p_mw=0.50, q_mvar=0.0),
            "commercial":  dict(p_mw=0.40, q_mvar=0.0),
            "residential": dict(p_mw=0.25, q_mvar=0.0),
            "mixed":       dict(p_mw=0.30, q_mvar=0.0),  # example value
        }

        # -------------------------------------------------
        # 5. Add loads
        # -------------------------------------------------
        def add_loads(cluster_dict, load_type):
            for cluster_name, buses in cluster_dict.items():
                for b in buses:
                    if b not in self.net.bus.index:
                        continue

                    pp.create_load(
                        self.net,
                        bus=b,
                        name=f"{load_type}_{cluster_name}_bus{b}",
                        type=load_type,
                        **load_params[load_type]
                    )

        add_loads(self.industrial_clusters, "industrial")
        add_loads(self.residential_clusters, "residential")
        add_loads(self.commercial_clusters, "commercial")
        add_loads(self.mixed_clusters, "mixed")

        # -------------------------------------------------
        # 6. Print cluster summary
        # -------------------------------------------------
        print("\n===== BUS CLUSTER SUMMARY =====")

        def print_cluster(name, clusters):
            buses = sorted({b for cl in clusters.values() for b in cl})
            print(f"{name:12s}: {len(buses):3d} buses -> {buses}")

        print_cluster("Industrial", self.industrial_clusters)
        print_cluster("Residential", self.residential_clusters)
        print_cluster("Commercial", self.commercial_clusters)
        print_cluster("Mixed", self.mixed_clusters)

        all_clustered_buses = set().union(
            *self.industrial_clusters.values(),
            *self.residential_clusters.values(),
            *self.commercial_clusters.values(),
            *self.mixed_clusters.values()
        )

        missing = all_buses - all_clustered_buses
        if missing:
            print("\n⚠️  Buses not assigned to any cluster:", sorted(missing))
        else:
            print("\n✅ All busbars are assigned to exactly one cluster.")

        # -------------------------------------------------
        # 7. Return requested objects
        # -------------------------------------------------
        return (
            self.net,
            self.industrial_clusters,
            self.residential_clusters,
            self.commercial_clusters,
            self.mixed_clusters
        )