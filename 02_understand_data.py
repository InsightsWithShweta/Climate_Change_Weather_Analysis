import pandas as pd
df=pd.read_csv(r"C:\Users\jranv\OneDrive\Documents\Desktop\Climate_Change_Weather_ Analysis\Dataset\india_climate_2000_2025.csv")

print("First 5 rows:")
print(df.head())

print("\nShape of Dataset:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nCheck missing values:")
print(df.isnull().sum())
