from data.data_creation.create_raw_data import create_raw_data
import matplotlib.pyplot as plt
import pandas as pd

df_distances_travelled = create_raw_data()

df_distances_travelled

# here we will cast an example dataframe of co2 emmisions per vehicle type

data = {1: 0.7, 2: 0}
df_dim_emmissions = pd.DataFrame(list(data.items()), columns=["vehicle_type", "co2_per_km"])

# join the output of the distances travelled to the emissions to get a co2 production per month

df_emmissions = df_distances_travelled.merge(df_dim_emmissions, on="vehicle_type", how="left")
df_emmissions["total_emissions"] = df_emmissions["distance_travelled"] * df_emmissions["co2_per_km"]


# Convert date to datetime format
df_emmissions["date"] = pd.to_datetime(df_emmissions["date"])

# Aggregate total emissions per month
monthly_emissions = df_emmissions.groupby(df_emmissions["date"].dt.to_period("M"))["total_emissions"].sum()

# Plot the graph
plt.figure(figsize=(10, 5))
monthly_emissions.plot(kind="bar", color="royalblue")
plt.xlabel("Month")
plt.ylabel("Total CO2 Emissions")
plt.title("Total Aggregated CO2 Emissions per Month")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)

# show and save plot
plt.show()
