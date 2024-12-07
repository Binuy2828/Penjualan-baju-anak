import streamlit as st
import pandas as pd
from streamlit_login_form import st_login_form

# Buat judul halaman
st.title("Toko Baju Bayi")

# Buat sidebar untuk filter
st.sidebar.header("Filter")
kategori = st.sidebar.selectbox("Kategori", ("Semua", "Laki-laki", "Perempuan"))
ukuran = st.sidebar.selectbox("Ukuran", ("Semua", "S", "M", "L"))
harga_min = st.sidebar.number_input("Harga Minimum", min_value=0, max_value=1000000)
harga_max = st.sidebar.number_input("Harga Maksimum", min_value=0, max_value=1000000)

# Muat data
data = pd.read_csv("data_baju_bayi.csv")

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
    st.image(row["gambar_produk"], width=200)

# Tampilkan informasi produk
    st.write(f"**{row['nama_produk']}**")
    st.write(f"Rp{row['harga']}")

    # Tambahkan tombol "Tambahkan ke Keranjang"
    if st.button(f"Tambahkan ke Keranjang ({row['nama_produk']})"):
        # Tambahkan produk ke keranjang
        # ...

        # Tampilkan pemberitahuan waktu nyata
        st.success(f"{row['nama_produk']} telah ditambahkan ke keranjang.")

# Tampilkan rekomendasi produk
if username:
    # Dapatkan riwayat pembelian pengguna
    # ...

    # Rekomendasikan produk berdasarkan riwayat pembelian
    # ...

    # Tampilkan rekomendasi
    st.header("Rekomendasi Produk")
    for produk in rekomendasi:
        # Tampilkan gambar produk
        st.image(produk["gambar_produk"], width=200)

        # Tampilkan informasi produk
        st.write(f"**{produk['nama_produk']}**")
        st.write(f"Rp{produk['harga']}")

        # Tambahkan tombol "Tambahkan ke Keranjang"
        if st.button(f"Tambahkan ke Keranjang ({produk['nama_produk']})"):
            # Tambahkan produk ke keranjang
            # ...

            # Tampilkan pemberitahuan waktu nyata
            st.success(f"{produk['nama_produk']} telah ditambahkan ke keranjang.")

# Tampilkan pelacakan pesanan
if username:
    # Dapatkan informasi pesanan pengguna
    # ...

    # Tampilkan informasi pesanan
    st.header("Pelacakan Pesanan")
    for pesanan in pesanan:
        # Tampilkan status pesanan
        st.write(f"Status: {pesanan['status']}")

        # Tampilkan tanggal pemesanan
        st.write(f"Tanggal Pemesanan: {pesanan['tanggal_pemesanan']}")

        # Tampilkan tanggal pengiriman
        st.write(f"Tanggal Pengiriman: {pesanan['tanggal_pengiriman']}")

        # Tampilkan tombol "Lihat Detail"
        if st.button(f"Lihat Detail ({pesanan['id']})"):
