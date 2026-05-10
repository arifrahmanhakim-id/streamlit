import pickle
import streamlit as st

# Membaca file model Naive Bayes
with open('naivebayes_pickle', 'rb') as r:
    hasil = pickle.load(r)

# Menu navigasi
menu = ['Halaman Utama', 'Tentang Kami', 'Kontak']
choice = st.sidebar.selectbox('Navigasi', menu)


# Fungsi prediksi
def prediction1(
    age,
    sex,
    cp,
    trestbps,
    chol,
    fbs,
    restecg,
    thalach,
    exang,
    oldpeak,
    slope,
    ca,
    thal
):

    prediction = hasil.predict([[
        age,
        sex,
        cp,
        trestbps,
        chol,
        fbs,
        restecg,
        thalach,
        exang,
        oldpeak,
        slope,
        ca,
        thal
    ]])

    return prediction


# Halaman Utama
if choice == 'Halaman Utama':

    st.title('Aplikasi Web Machine Learning')
    st.subheader('Algoritma Naive Bayes')

    col1, col2 = st.columns(2)

    # Kolom kiri
    with col1:

        age = st.number_input(
            "Age",
            min_value=0,
            max_value=100,
            step=1
        )

        sex = st.number_input(
            "Sex",
            min_value=0,
            max_value=1,
            step=1
        )

        cp = st.number_input(
            "CP",
            min_value=0,
            max_value=4,
            step=1
        )

        trestbps = st.number_input(
            "Trestbps",
            min_value=0,
            max_value=300,
            step=1
        )

        chol = st.number_input(
            "Chol",
            min_value=0,
            max_value=600,
            step=1
        )

        fbs = st.number_input(
            "FBS",
            min_value=0,
            max_value=1,
            step=1
        )

    # Kolom kanan
    with col2:

        restecg = st.number_input(
            "Restecg",
            min_value=0,
            max_value=2,
            step=1
        )

        thalach = st.number_input(
            "Thalach",
            min_value=0,
            max_value=300,
            step=1
        )

        exang = st.number_input(
            "Exang",
            min_value=0,
            max_value=1,
            step=1
        )

        oldpeak = st.number_input(
            "Oldpeak",
            min_value=0.0,
            max_value=10.0,
            step=0.1
        )

        slope = st.number_input(
            "Slope",
            min_value=0,
            max_value=3,
            step=1
        )

        ca = st.number_input(
            "CA",
            min_value=0,
            max_value=4,
            step=1
        )

        thal = st.number_input(
            "Thal",
            min_value=0,
            max_value=3,
            step=1
        )

    result = ""

    # Tombol prediksi
    if st.button("Predict"):

        result = prediction1(
            age,
            sex,
            cp,
            trestbps,
            chol,
            fbs,
            restecg,
            thalach,
            exang,
            oldpeak,
            slope,
            ca,
            thal
        )

        # Konversi hasil prediksi
        if result[0] == 0:
            result = 'Tidak Punya Penyakit Jantung'

        elif result[0] == 1:
            result = 'Punya Penyakit Jantung'

        # Menampilkan hasil
        st.success(f'Hasil Prediksinya adalah: {result}')

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