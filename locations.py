import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from collections import Counter

# Load processed data
df = pd.read_csv("processed_ufo_articles.csv")

# Count the frequency of each location mentioned
location_counts = Counter([loc for locations in df["entities"].apply(eval).apply(lambda x: x["LOCATIONS"]) for loc in locations])

# Convert to DataFrame for easier manipulation
location_df = pd.DataFrame(location_counts.items(), columns=["Location", "Count"])

# Plotting (if specific locations can be matched to coordinates)
location_df.plot(kind="bar", x="Location", y="Count", title="UFO Sightings by Location")
plt.ylabel("Frequency")
plt.show()
