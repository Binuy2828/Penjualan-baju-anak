import streamlit as st
import pandas as pd

# Judul aplikasi
st.title("TOKO BAJU ANAK ANDALAN")
st.write("HALO SELAMAT DATANG DI TOKO BAJU ANDALAN! SELAMAT BERBELANJA.")

# Data awal untuk baju
data_baju = {
    "Nama": ["Kaos Anak Motif Bunga", "Kaos Anak Motif Dino", "Kaos Anak Motif Mobil"],
    "Harga": [50000, 70000, 80000],
    "Stok": [6, 17, 5]
}

# Mengubah data menjadi DataFrame
df_baju = pd.DataFrame(data_baju)

# Buat form login
form = st.form(key='login_form')
username = form.text_input('Username')
password = form.text_input('Password', type='password')
submit = form.form_submit_button('Login')

# Periksa apakah tombol login diklik
if submit:
    # Periksa apakah username dan password benar
    if username == 'admin' and password == 'password':
        st.success('Login berhasil!')

        # Tampilkan halaman toko baju setelah login berhasil
        # ...
    else:
        st.error('Username atau password salah!')


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

# Fungsi untuk menampilkan keranjang belanja
def tampilkan_keranjang(keranjang):
    st.markdown("## Keranjang Belanja")
    total_harga = 0
    if keranjang:
        for item in keranjang:
            st.write(f"{item['Jumlah']} x {item['Nama']} - Rp {item['Harga'] * item['Jumlah']}")
            total_harga += item['Harga'] * item['Jumlah']
        st.markdown("### Total Harga")
        st.write(f"Rp {total_harga:,}")
    else:
        st.write("Keranjang Anda masih kosong.")

# Fungsi utama
def main():
    keranjang = []
    if tampilkan_akun():
        tampilkan_baju()
        tambah_ke_keranjang(keranjang)
        tampilkan_keranjang(keranjang)

        # Tombol beli
        if st.button("Beli Sekarang"):
            st.success("Terima kasih atas pembelian Anda!")

if __name__ == "__main__":
    main()
