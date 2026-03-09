import os
import pandas as pd

# print(os.listdir("data/all_categorized_data"))

file = "data/all_categorized_data/Energy.xlsx"

df = pd.read_excel(file)
len_all = len(df)

# print(df.head())

# Mapping bulan Indonesia ke Inggris
bulan_map = {
    "Jan": "Jan",
    "Feb": "Feb",
    "Mar": "Mar",
    "Apr": "Apr",
    "Mei": "May",
    "Jun": "Jun",
    "Jul": "Jul",
    "Agt": "Aug",
    "Sep": "Sep",
    "Okt": "Oct",
    "Nov": "Nov",
    "Des": "Dec"
}

# Replace bulan
for indo, eng in bulan_map.items():
    df["Tanggal Pencatatan"] = df["Tanggal Pencatatan"].str.replace(indo, eng)

# Convert ke datetime
df["Tanggal Pencatatan"] = pd.to_datetime(df["Tanggal Pencatatan"], dayfirst=True)

# print(df.head())

# Select ticker that listed after 2020
df_aft2020 = df[df["Tanggal Pencatatan"] >= "2020-01-01"]
len_aft = len(df_aft2020)

# Select ticker that listed before 2020
df_pre2020 = df[df["Tanggal Pencatatan"] <= "2020-01-01"]
len_pre = len(df_pre2020)

print(len_all)
print(len_aft)
print(len_pre)