import pickle
import streamlit as st

# Membaca file model
with open('decisiontree_pickle', 'rb') as r:
    hasil = pickle.load(r)

# Menu navigasi
menu = ['Halaman Utama', 'Tentang Kami', 'Kontak']
choice = st.sidebar.selectbox('Navigasi', menu)


# Fungsi prediksi
def prediction1(
    Pregnancies,
    Glucose,
    BloodPressure,
    SkinThickness,
    Insulin,
    BMI,
    DiabetesPedigreeFunction,
    Age
):
    prediction = hasil.predict([[
        Pregnancies,
        Glucose,
        BloodPressure,
        SkinThickness,
        Insulin,
        BMI,
        DiabetesPedigreeFunction,
        Age
    ]])

    return prediction


# Halaman utama
if choice == 'Halaman Utama':

    st.title('Aplikasi Web Machine Learning')
    st.subheader('Algoritma Decision Tree')

    col1, col2 = st.columns(2)

    with col1:
        Pregnancies = st.text_input("Pregnancies", "")
        Glucose = st.text_input("Glucose", "")
        BloodPressure = st.text_input("Blood Pressure", "")
        SkinThickness = st.text_input("Skin Thickness", "")

    with col2:
        Insulin = st.text_input("Insulin", "")
        BMI = st.text_input("BMI", "")
        DiabetesPedigreeFunction = st.text_input(
            "Diabetes Pedigree Function", ""
        )
        Age = st.text_input("Age", "")

    result = ""

    if st.button("Predict"):
        result = prediction1(
            float(Pregnancies),
            float(Glucose),
            float(BloodPressure),
            float(SkinThickness),
            float(Insulin),
            float(BMI),
            float(DiabetesPedigreeFunction),
            float(Age)
        )

        st.success(f'Hasil Prediksinya adalah {result}')

# Halaman tentang kami
elif choice == 'Tentang Kami':

    st.title('Tentang Kami')

    st.write(
        'Buku ini dibuat untuk belajar aplikasi Streamlit.'
    )

    st.write(
        'Kami sangat senang Anda belajar machine learning dengan Streamlit.'
    )

# Halaman kontak
elif choice == 'Kontak':

    st.title('Kontak')

    st.write(
        'Kalian bisa menghubungi kami di '
        'arifrahmanarh@telkomuniversity.ac.id'
    )