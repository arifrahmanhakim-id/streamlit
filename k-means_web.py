import pickle
import streamlit as st

# Membaca file model K-Means
with open('k-means_pickle', 'rb') as r:
    classifier1 = pickle.load(r)

# Menu navigasi
menu = ['Halaman Utama', 'Tentang Kami', 'Kontak']
choice = st.sidebar.selectbox('Navigasi', menu)


# Fungsi prediksi
def prediction1(longitude, latitude):

    prediction = classifier1.predict([[
        longitude,
        latitude
    ]])

    return prediction


# Halaman Utama
if choice == 'Halaman Utama':

    st.title('Aplikasi Web Machine Learning')
    st.subheader('Klaster Rumah')

    # Input user
    longitude = st.text_input("Longitude", "")
    latitude = st.text_input("Latitude", "")

    result = ""

    # Tombol prediksi
    if st.button("Predict"):

        result = prediction1(
            float(longitude),
            float(latitude)
        )

        # Konversi hasil cluster
        if result[0] == 0:
            result = 'Cukup Tinggi'

        elif result[0] == 1:
            result = 'Cukup Tinggi'

        elif result[0] == 2:
            result = 'Lebih Rendah'

        # Menampilkan hasil
        st.success(f'Masuk ke Klaster Rumah:  {result}')

        # st.write("Masuk ke Klaster Rumah:", result)


# Halaman Tentang Kami
elif choice == 'Tentang Kami':

    st.title('Tentang Kami')

    st.write(
        'Buku ini dibuat untuk belajar aplikasi Streamlit.'
    )

    st.write(
        'Kami sangat senang Anda belajar machine learning '
        'dengan Streamlit.'
    )


# Halaman Kontak
elif choice == 'Kontak':

    st.title('Kontak')

    st.write(
        'Bisa menghubungi kami di '
        'arifrahmanarh@telkomuniversity.ac.id'
    )