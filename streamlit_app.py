import streamlit as st
import pandas as pd
st.title("TOKO BAJU ANAK ANDALAN")
st.write(
    "HALO SELAMAT DATANG DI TOKO BAJU ANDALAN ! SELAMAT BERBELANJA."
)

# Data awal untuk baju
data_baju = {
    "Nama": ["Kaos Anak Motif Bunga", "Kaos Anak Motif Dino", "Kaos Anak Motif Mobil",],
    "Harga": [50000, 70000, 80000],
    "Stok": [6, 17, 5]
}

# Mengubah data menjadi DataFrame
df_baju = pd.DataFrame(data_baju)

# Fungsi untuk menampilkan akun pengguna
def tampilkan_akun():
    st.sidebar.header("Akun Pengguna")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type='password')
    
    if st.sidebar.button("Login Akun"):
        if username == "kasir1" and password == "kasir123":
            st.sidebar.success("Selamat Login Anda Sukses!")
            return True
        else:
            st.sidebar.error("Username atau password anda salah.")
    return False

# Fungsi untuk menampilkan daftar baju
def tampilkan_baju():
    st.header("Daftar Baju Anak")
    st.write(df_baju)

# Fungsi untuk menambahkan baju ke keranjang
def tambah_ke_keranjang(keranjang):
    st.header("Tambah Item Ke Keranjang")
    nama_baju = st.selectbox("Pilih Baju", df_baju["Nama"])
    jumlah = st.number_input("Jumlah", min_value=1, max_value=10, value=1)

    if st.button("Tambah ke Keranjang"):
        baju = df_baju[df_baju["Nama"] == nama_baju]
        if baju["Stok"].values[0] >= jumlah:
            keranjang.append({"Nama": nama_baju, "Jumlah": jumlah, "Harga": baju["Harga"].values[0]})
            df_baju.loc[df_baju["Nama"] == nama_baju, "Stok"] -= jumlah
            st.success(f"{jumlah} {nama_baju} berhasil ditambahkan ke keranjang anda.")
        else:
            st.error("Yahh Stok nya habis nih.")

st.markdown("## Keranjang Belanja")
    if keranjang:
        for item in keranjang:
            st.write(f"{item['Jumlah']} x {item['Nama']} - Rp {item['Harga'] * item['Jumlah']}")
        st.markdown("### Total Harga")
        st.write(f"Rp {total_harga:,}")
    else:
        st.write("Keranjang Anda masih kosong.")

    # Tombol beli
    if st.button("Beli Sekarang"):
        st.success("Terima kasih atas pembelian Anda!")
else:
    st.write("Silakan login untuk melihat katalog dan melakukan pembelian.")
if __name__ == "__main__":
    main()
