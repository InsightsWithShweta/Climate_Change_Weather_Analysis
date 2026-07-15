import pandas as pd
df=pd.read_csv(r"C:\Users\jranv\OneDrive\Documents\Desktop\Climate_Change_Weather_ Analysis\Dataset\india_climate_2000_2025.csv")

print("Original Shape")
print(df.shape)

print("\nMissing values:")
print(df.isnull().sum())

df=df.drop_duplicates()

df.reset_index(drop=True,inplace=True)                #reset index after removing duplicates

print("\nShape after removing duplicates:")
print(df.shape)

df.to_csv(r"C:\Users\jranv\OneDrive\Documents\Desktop\Climate_Change_Weather_ Analysis\Dataset\india_climate_2000_2025.csv",index=False)
print("Data Cleaning Completed Successfully")

