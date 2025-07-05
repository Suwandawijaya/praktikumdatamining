import pandas as pd

# Parameter daya
daya_ac_kw = 1.0        # 1000 watt = 1 kW
daya_lampu_kw = 0.15    # 150 watt = 0.15 kW

# Buat dataset realistis
data_real = {
    "Tanggal": pd.date_range(start="2025-06-01", periods=30, freq='D'),
    "Hari": (["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"] * 5)[:30],
    "Suhu (°C)": [30, 29, 31, 32, 28, 30, 29, 31, 33, 30] * 3,
    "Durasi AC (jam)": [8, 6, 9, 10, 5, 7, 6, 9, 11, 8] * 3,
    "Durasi Lampu (jam)": [10, 12, 9, 11, 8, 10, 12, 9, 11, 10] * 3,
    "Jumlah Lampu": [5, 6, 5, 4, 7, 5, 6, 5, 4, 5] * 3,
}

# Hitung konsumsi kWh
df_real = pd.DataFrame(data_real)
df_real["Konsumsi AC (kWh)"] = df_real["Durasi AC (jam)"] * daya_ac_kw
df_real["Konsumsi Lampu (kWh)"] = df_real["Durasi Lampu (jam)"] * daya_lampu_kw
df_real["Total Konsumsi Listrik (kWh)"] = df_real["Konsumsi AC (kWh)"] + df_real["Konsumsi Lampu (kWh)"]

# Simpan ke CSV
df_real.to_csv("konsumsi_listrik_30hari_realis.csv", index=False)

print("Dataset berhasil dibuat.")
