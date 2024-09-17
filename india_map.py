import geopandas as gpd
import matplotlib.pyplot as plt
import random

shapefile_path = '/mnt/c/Users/jbtff/OneDrive/Documents/india_ds.shp'
gdf = gpd.read_file(shapefile_path)

def generate_random_colors(num_colors):
    return ["#"+''.join([random.choice('0123456789ABCDEF') for _ in range(6)]) for _ in range(num_colors)]

num_colors = int(input("Enter the number of colors to use: "))

colors = generate_random_colors(num_colors)

gdf['color'] = [random.choice(colors) for _ in range(len(gdf))]

fig, ax = plt.subplots(figsize=(10, 10))
gdf.plot(ax=ax, color=gdf['color'], edgecolor='black')

ax.set_title(f"India Map with {num_colors} Random Colors", fontsize=15)
plt.show()
