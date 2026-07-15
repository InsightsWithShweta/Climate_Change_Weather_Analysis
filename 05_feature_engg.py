import pandas as pd

df=pd.read_csv(r"C:\Users\jranv\OneDrive\Documents\Desktop\Climate_Change_Weather_ Analysis\Dataset\india_climate_2000_2025.csv")

# Temp category

df["temp_category"]=df["avg_temp_c"].apply(lambda x:"Cold" if x<20 else "Moderate" if x<30 else "Hot")

# Rainfall Category

df["Rainfall_category"]=df["rainfall_mm"].apply(lambda x:"Low" if x<2 else"Medium" if x<8 else "High")

# Humidity category

df["humidity_category"]=df["humidity_pct"].apply(lambda x:"Low" if x <40 else "Moderate" if x<70 else "High")

# Heat Risk level

df["heat_risk"]=df["heat_index"].apply(lambda x:"Low" if x <27 else "Moderate" if x<32 else "High")

# Decades

df["decade"]=(df["year"]//10)*10

# Temperature difference

df["temp_diff"]=(df["max_temp_c"]-df["min_temp_c"])

print(df.head())
df.info()
print(df)
print("\nNew columns added:")
print(df.columns)

df.to_csv(r"C:\Users\jranv\OneDrive\Documents\Desktop\Climate_Change_Weather_ Analysis\Dataset\india_climate_2000_2025.csv",index=False)
print("\nFeature Engineering Completed Successfully")