
import osmnx as ox
from shapely.geometry import LineString, MultiLineString
import matplotlib.pyplot as plt

north = 53.1450   # top edge (lat)
south = 53.1410   # bottom edge (lat)
east  = 8.2200    # right edge (lon)
west  = 8.2100    # left edge (lon)

G = ox.graph_from_bbox(
    north=north,
    south=south,
    east=east,
    west=west,
    network_type="drive"
)

buildings = ox.geometries_from_bbox(
    north=north,
    south=south,
    east=east,
    west=west,
    tags={"building": True}
)

edges = ox.graph_to_gdfs(G, nodes=False)

edges = ox.project_gdf(edges)
buildings = ox.project_gdf(buildings)

fig, ax = plt.subplots(figsize=(10, 10))

buildings.plot(ax=ax, color="lightgrey", edgecolor="black", linewidth=0.2)
edges.plot(ax=ax, color="white", linewidth=1)

ax.axis("off")
plt.show()
