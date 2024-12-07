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
