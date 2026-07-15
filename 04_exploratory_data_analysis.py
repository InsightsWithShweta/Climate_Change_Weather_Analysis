import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\jranv\OneDrive\Documents\Desktop\Climate_Change_Weather_ Analysis\Dataset\india_climate_2000_2025.csv")

# Which state has highest avg temp

state_temp=df.groupby("state")["avg_temp_c"].mean()
state_temp=state_temp.sort_values(ascending=False)  # sort in descending order
plt.figure(figsize=(12,6))
plt.bar(state_temp.index, state_temp.values)
plt.title("Average Temperature by State")
plt.xlabel("State")
plt.ylabel("Average Temperature (°C)")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
print(state_temp)
print("\nState with highest avg temperature:")
print(state_temp.head(1))

# which state receive highest rainfall

state_rainfall=df.groupby("state")["rainfall_mm"].mean()
state_rainfall=state_rainfall.sort_values(ascending=False)
plt.figure(figsize=(12,6))
plt.bar(state_rainfall.index, state_rainfall.values)
plt.title("Average Rainfall by State")
plt.xlabel("State")
plt.ylabel("Rainfall (mm)")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
print("\nAverage Rainfall by state")
print(state_rainfall)
print("\nState with highest avg rainfall:")
print(state_rainfall.head(1))

# which season is hottest

season_temp=df.groupby("season")["avg_temp_c"].mean()
season_temp=season_temp.sort_values(ascending=False)
plt.figure(figsize=(8,5))
plt.bar(season_temp.index, season_temp.values)
plt.title("Average Temperature by Season")
plt.xlabel("Season")
plt.ylabel("Average Temperature (°C)")
plt.tight_layout()
plt.show()
print("\nAverage Temp by Season:")
print(season_temp)
print("\nHottest Season:")
print(season_temp.head(1))

# which region has highest avg humidity

region_humidity=df.groupby("region")["humidity_pct"].mean()
region_humidity=region_humidity.sort_values(ascending=False)
plt.figure(figsize=(8,5))
plt.bar(region_humidity.index, region_humidity.values)
plt.title("Average Humidity by Region")
plt.xlabel("Region")
plt.ylabel("Humidity (%)")
plt.tight_layout()
plt.show()
print("\nAverage humidity by region")
print(region_humidity)
print("\nRegion with highest avg humidity")
print(region_humidity.head(1))

# Temperature trend

year_temp = df.groupby("year")["avg_temp_c"].mean()

plt.figure(figsize=(12,6))
plt.plot(year_temp.index, year_temp.values, marker="o")
plt.title("Average Temperature Trend (2000–2025)")
plt.xlabel("Year")
plt.ylabel("Average Temperature (°C)")
plt.grid(True)
plt.tight_layout()
plt.show()
print(year_temp)

#avg rainfall changed from 2000-2025

year_rain = df.groupby("year")["rainfall_mm"].mean()
plt.figure(figsize=(12,6))
plt.plot(year_rain.index, year_rain.values, marker="o")
plt.title("Average Rainfall Trend (2000–2025)")
plt.xlabel("Year")
plt.ylabel("Rainfall (mm)")
plt.grid(True)
plt.tight_layout()
plt.show()
print(year_rain)

# el nino vs avg temp

elnino_temp = df.groupby("el_nino_flag")["avg_temp_c"].mean()

plt.figure(figsize=(6,5))
plt.bar(elnino_temp.index.astype(str), elnino_temp.values)
plt.title("El Niño vs Average Temperature")
plt.xlabel("El Niño Flag")
plt.ylabel("Average Temperature (°C)")
plt.tight_layout()
plt.show()
print(elnino_temp)

#  elnino vs avg  rainfall

elnino_rain = df.groupby("el_nino_flag")["rainfall_mm"].mean()

plt.figure(figsize=(6,5))
plt.bar(elnino_rain.index.astype(str), elnino_rain.values)
plt.title("El Niño vs Average Rainfall")
plt.xlabel("El Niño Flag")
plt.ylabel("Average Rainfall (mm)")
plt.tight_layout()
plt.show()
print(elnino_rain)

# top 10 drought prone states

drought = df[df["drought_flag"] == 1]
drought_state = drought.groupby("state").size().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
plt.barh(drought_state.index, drought_state.values)
plt.title("Top 10 Drought-Prone States")
plt.xlabel("Number of Drought Records")
plt.tight_layout()
plt.show()
print(drought_state)

# state with highest heat index

heat_index = df.groupby("state")["heat_index"].mean().sort_values(ascending=False)
plt.figure(figsize=(12,6))
plt.bar(heat_index.index, heat_index.values)

plt.title("Average Heat Index by State")
plt.xlabel("State")
plt.ylabel("Heat Index")

plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
print(heat_index)

# relation between rainfall and humidity

correlation = df["rainfall_mm"].corr(df["humidity_pct"])
print("Correlation between Rainfall and Humidity:", correlation)
plt.figure(figsize=(8,6))

plt.scatter(df["rainfall_mm"], df["humidity_pct"])

plt.title("Rainfall vs Humidity")
plt.xlabel("Rainfall (mm)")
plt.ylabel("Humidity (%)")

plt.tight_layout()
plt.show()

# relationship bet temp and heat index

correlation = df["avg_temp_c"].corr(df["heat_index"])

print("Correlation between Temperature and Heat Index:", correlation)
plt.figure(figsize=(8,6))

plt.scatter(df["avg_temp_c"], df["heat_index"])

plt.title("Temperature vs Heat Index")
plt.xlabel("Average Temperature (°C)")
plt.ylabel("Heat Index")

plt.tight_layout()
plt.show()