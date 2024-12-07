import streamlit as st
import pandas as pd
from streamlit_login_form import st_login_form

# Buat judul halaman
st.title("Toko Baju Anak")

# Buat sidebar untuk katalog produk
st.sidebar.header("Katalog Produk")
kategori = st.sidebar.selectbox("Kategori", ("Semua", "Laki-laki", "Perempuan"))
ukuran = st.sidebar.selectbox("Ukuran", ("Semua", "S", "M", "L"))
harga_min = st.sidebar.number_input("Harga Minimum", min_value=0, max_value=1000000)
harga_max = st.sidebar.number_input("Harga Maksimum", min_value=0, max_value=1000000)

# Muat data
data = pd.read_csv("data_baju_anak.csv")

# Filter data sesuai dengan pilihan pengguna
if kategori != "Semua":
    data = data[data["kategori"] == kategori]
if ukuran != "Semua":
    data = data[data["ukuran"] == ukuran]
if harga_min > 0:
    data = data[data["harga"] >= harga_min]
if harga_max > 0:
    data = data[data["harga"] <= harga_max]

# Buat sistem login
username = st.session_state.get("username", None)
if not username:
    username, password = st_login_form(submit_button_text="Login")
    if username and password:
        # Validasi kredensial login
        # ...

        # Simpan username ke sesi
        st.session_state.username = username

# Tampilkan produk
for i, row in data.iterrows():
    # Tampilkan gambar produk
    st.image(row["gambar_produk"], widt
