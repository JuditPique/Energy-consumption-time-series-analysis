import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("PJME_hourly.csv")
data = data.head(5000)

# Convert datetime
data["Datetime"] = pd.to_datetime(data["Datetime"])

# Sort values
data = data.sort_values("Datetime")

# Basic info
print(data.head())

# Basic stats
max_row = data.loc[data["PJME_MW"].idxmax()]
min_row = data.loc[data["PJME_MW"].idxmin()]

print("Average consumption:", data["PJME_MW"].mean())
print("Max consumption:", data["PJME_MW"].max())
print("Min consumption:", data["PJME_MW"].min())

# Plot
plt.figure(figsize=(10,5))
plt.plot(data["Datetime"], data["PJME_MW"])
plt.title("Energy consumption over time")
plt.xlabel("Time")
plt.ylabel("MW")
plt.grid()

plt.savefig("energy_plot.png")
plt.show()

# Simple rolling average (trend)
data["rolling_avg"] = data["PJME_MW"].rolling(window=24).mean()

plt.figure(figsize=(10,5))
plt.plot(data["Datetime"], data["PJME_MW"], alpha=0.5)
plt.plot(data["Datetime"], data["rolling_avg"], color="red")

plt.title("Energy consumption with trend")
plt.xlabel("Time")
plt.ylabel("MW")
plt.grid()

plt.savefig("energy_trend.png")
plt.show()