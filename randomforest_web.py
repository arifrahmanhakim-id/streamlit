import pickle
import streamlit as st

# Membaca file model Random Forest
with open('randomforet_pickle', 'rb') as r:
    classifier1 = pickle.load(r)

# Menu navigasi
menu = ['Halaman Utama', 'Tentang Kami', 'Kontak']
choice = st.sidebar.selectbox('Navigasi', menu)


# Fungsi prediksi
def prediction1(
    sepal_length1,
    sepal_width1,
    petal_length1,
    petal_width1
):
    prediction = classifier1.predict([[
        sepal_length1,
        sepal_width1,
        petal_length1,
        petal_width1
    ]])

    return prediction


# Halaman Utama
if choice == 'Halaman Utama':

    st.title('Aplikasi Web Machine Learning')
    st.subheader('Prediksi Bunga Iris')

    # Input user
    sepal_length1 = st.text_input("Sepal Length", "")
    sepal_width1 = st.text_input("Sepal Width", "")
    petal_length1 = st.text_input("Petal Length", "")
    petal_width1 = st.text_input("Petal Width", "")

    result = ""

    # Tombol prediksi
    if st.button("Predict"):

        result = prediction1(
            float(sepal_length1),
            float(sepal_width1),
            float(petal_length1),
            float(petal_width1)
        )

        # Konversi hasil prediksi
        if result[0] == 1:
            result = 'Bunga Iris Setosa'

        elif result[0] == 2:
            result = 'Bunga Iris Versicolor'

        elif result[0] == 3:
            result = 'Bunga Iris Virginica'

        # Menampilkan hasil
        st.success(f'Hasil Prediksinya adalah {result}')

        # st.write("Hasil Prediksinya adalah:", result)


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
        'Kalian bisa menghubungi kami di '
        'arifrahmanarh@telkomuniversity.ac.id'
    )