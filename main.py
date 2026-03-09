import os
import pandas as pd

# print(os.listdir("data/all_categorized_data"))

kategori = os.listdir("data/all_categorized_data")

kategori_dct = {}

for i in kategori:
    kategori_dct[i[:-5]] = []
    
n = 0

for i in kategori:
    file = "data/all_categorized_data/" + i
    # print(file)

    df = pd.read_excel(file)
    len_all = len(df)

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

    # print(len_all)
    # print(len_aft)
    # print(len_pre)
    n += len_pre

    kategori_dct[i[:-5]] = list(df_pre2020["Kode"])

# print(n)

x = 0
for i in kategori_dct:
    x += len(kategori_dct[i])
# print(x)

file = "data/all_data/DaftarSaham.xlsx"
# print(file)
df = pd.read_excel(file)
len_all = len(df)
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
# print(len_all)
# print(len_aft)

# print(len_pre)

print(kategori_dct)