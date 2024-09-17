import geopandas as gpd
import matplotlib.pyplot as plt
import random

# Load the shapefile of India (Make sure to provide the path to the downloaded shapefile)
shapefile_path = '/mnt/c/Users/jbtff/OneDrive/Documents/india_ds.shp'  # Update this with the correct path
gdf = gpd.read_file(shapefile_path)

# Function to generate random colors for each state
def generate_random_colors(num_colors):
    return ["#"+''.join([random.choice('0123456789ABCDEF') for _ in range(6)]) for _ in range(num_colors)]

# Ask the user for the number of unique colors
num_colors = int(input("Enter the number of colors to use: "))

# Generate random colors
colors = generate_random_colors(num_colors)

# Apply coloring to each state randomly
gdf['color'] = [random.choice(colors) for _ in range(len(gdf))]

# Plot the map with the colors
fig, ax = plt.subplots(figsize=(10, 10))
gdf.plot(ax=ax, color=gdf['color'], edgecolor='black')

# Set title and display the map
ax.set_title(f"India Map with {num_colors} Random Colors", fontsize=15)
plt.show()
