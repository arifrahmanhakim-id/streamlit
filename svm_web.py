# Import library
import pickle
import streamlit as st

# Membaca file model
with open('svm_pickle', 'rb') as r:
    model = pickle.load(r)

# Menu navigasi
menu = ['Halaman Utama', 'Tentang Kami', 'Kontak']
choice = st.sidebar.selectbox('Navigasi', menu)


# Fungsi prediksi
def prediction1(
    x1, x2, x3, x4, x5, x6, x7, x8, x9, x10,
    x11, x12, x13, x14, x15, x16, x17, x18, x19, x20,
    x21, x22, x23, x24, x25, x26, x27, x28, x29, x30
):

    data = [[
        float(x1), float(x2), float(x3), float(x4), float(x5),
        float(x6), float(x7), float(x8), float(x9), float(x10),
        float(x11), float(x12), float(x13), float(x14), float(x15),
        float(x16), float(x17), float(x18), float(x19), float(x20),
        float(x21), float(x22), float(x23), float(x24), float(x25),
        float(x26), float(x27), float(x28), float(x29), float(x30)
    ]]

    prediction = model.predict(data)
    return prediction


# Halaman utama
if choice == 'Halaman Utama':

    st.title('Aplikasi Web Machine Learning')
    st.subheader('Prediksi Kanker Payudara')
    st.write('Menggunakan Algoritma Support Vector Machine (SVM)')

    col1, col2, col3 = st.columns(3)

    # Kolom 1
    with col1:
        x1 = st.text_input("Mean Radius", "")
        x2 = st.text_input("Mean Texture", "")
        x3 = st.text_input("Mean Perimeter", "")
        x4 = st.text_input("Mean Area", "")
        x5 = st.text_input("Mean Smoothness", "")
        x6 = st.text_input("Mean Compactness", "")
        x7 = st.text_input("Mean Concavity", "")
        x8 = st.text_input("Mean Concave Points", "")
        x9 = st.text_input("Mean Symmetry", "")
        x10 = st.text_input("Mean Fractal Dimension", "")

    # Kolom 2
    with col2:
        x11 = st.text_input("Radius Error", "")
        x12 = st.text_input("Texture Error", "")
        x13 = st.text_input("Perimeter Error", "")
        x14 = st.text_input("Area Error", "")
        x15 = st.text_input("Smoothness Error", "")
        x16 = st.text_input("Compactness Error", "")
        x17 = st.text_input("Concavity Error", "")
        x18 = st.text_input("Concave Points Error", "")
        x19 = st.text_input("Symmetry Error", "")
        x20 = st.text_input("Fractal Dimension Error", "")

    # Kolom 3
    with col3:
        x21 = st.text_input("Worst Radius", "")
        x22 = st.text_input("Worst Texture", "")
        x23 = st.text_input("Worst Perimeter", "")
        x24 = st.text_input("Worst Area", "")
        x25 = st.text_input("Worst Smoothness", "")
        x26 = st.text_input("Worst Compactness", "")
        x27 = st.text_input("Worst Concavity", "")
        x28 = st.text_input("Worst Concave Points", "")
        x29 = st.text_input("Worst Symmetry", "")
        x30 = st.text_input("Worst Fractal Dimension", "")

    # Tombol prediksi
    if st.button("Predict"):

        hasil = prediction1(
            x1, x2, x3, x4, x5, x6, x7, x8, x9, x10,
            x11, x12, x13, x14, x15, x16, x17, x18, x19, x20,
            x21, x22, x23, x24, x25, x26, x27, x28, x29, x30
        )

        st.success(f'Hasil Prediksi: {hasil[0]}')


# Halaman Tentang Kami
elif choice == 'Tentang Kami':

    st.title('Tentang Kami')
    st.write('Aplikasi ini dibuat untuk belajar machine learning menggunakan Streamlit.')
    st.write('Kami sangat senang Anda belajar machine learning dengan Streamlit.')


# Halaman Kontak
elif choice == 'Kontak':

    st.title('Kontak')
    st.write('Kalian bisa menghubungi kami di: arifrahmanarh@telkomuniversity.ac.id')