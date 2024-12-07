import streamlit as st

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

# judul toko
st.title("halo wndwkdnwdwnd")

# Data awal untuk baju
data_baju = {
    "Nama": ["Kaos Anak Motif Bunga", "Kaos Anak Motif Dino", "Kaos Anak Motif Mobil"],
    "Harga": [50000, 70000, 80000],
    "Stok": [6, 17, 5]
}

# Mengubah data menjadi DataFrame
df_baju = pd.DataFrame(data_baju)
