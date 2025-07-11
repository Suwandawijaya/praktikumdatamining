import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Parameter daya
daya_ac_kw = 1.0        # 1000 watt = 1 kW
daya_lampu_kw = 0.15    # 150 watt = 0.15 kW

# Judul aplikasi
st.title("Prediksi Konsumsi Listrik Harian (Tanpa Suhu) + Grafik")

# Load dataset
df = pd.read_csv("konsumsi_listrik_30hari_tanpa_suhu.csv")

# Tampilkan tabel data
st.subheader("📊 Data Konsumsi Listrik 30 Hari")
st.dataframe(df)

st.markdown("---")

# Grafik histori konsumsi listrik
st.subheader("📈 Grafik Total Konsumsi Listrik 30 Hari")

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(df["Tanggal"], df["Total Konsumsi Listrik (kWh)"], marker='o', color='blue')
ax.set_xlabel("Tanggal")
ax.set_ylabel("Konsumsi Listrik (kWh)")
ax.set_title("Grafik Total Konsumsi Listrik Harian")
ax.grid(True)
plt.xticks(rotation=45)
st.pyplot(fig)

st.markdown("---")

# Form input slider
st.subheader("🔧 Prediksi Konsumsi Listrik Berdasarkan Input Manual")

durasi_ac = st.slider("Durasi AC (jam)", 0, 24, 8)
durasi_lampu = st.slider("Durasi Lampu (jam)", 0, 24, 10)
jumlah_lampu = st.slider("Jumlah Lampu", 1, 10, 5)

# Hitung konsumsi listrik
konsumsi_ac = daya_ac_kw * durasi_ac
konsumsi_lampu = daya_lampu_kw * durasi_lampu
total_konsumsi = konsumsi_ac + konsumsi_lampu

# Tampilkan hasil prediksi
st.subheader("🔋 Hasil Prediksi Konsumsi Listrik")
st.write(f"**Konsumsi AC:** {konsumsi_ac:.2f} kWh")
st.write(f"**Konsumsi Lampu:** {konsumsi_lampu:.2f} kWh")
st.write(f"**Total Konsumsi Listrik:** {total_konsumsi:.2f} kWh per hari")

st.markdown("---")

# Keterangan rumus
with st.expander("ℹ️ Rumus Perhitungan"):
    st.write(f"""
    **Konsumsi AC (kWh) = Durasi AC (jam) × {daya_ac_kw} kW**
    
    **Konsumsi Lampu (kWh) = Durasi Lampu (jam) × {daya_lampu_kw} kW**
    
    **Total Konsumsi Listrik = Konsumsi AC + Konsumsi Lampu**
    """)
