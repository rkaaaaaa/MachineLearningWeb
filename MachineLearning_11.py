import pickle
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt

# Load model prediksi harga mobil
model = pickle.load(open('Model_Prediksi_Harga_Mobil.sav', 'rb'))

# Sidebar
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🚗 Data Mobil</h1>", unsafe_allow_html=True)
    st.markdown("---")  # Garis pemisah
    st.markdown("""  
        **Navigasi Halaman**  
        Gunakan menu di bawah untuk menjelajahi:
        - 🔍 **Beranda**: Lihat pengenalan aplikasi.
        - 📊 **Dataset**: Jelajahi data penjualan mobil.
        - 📈 **Grafik**: Lihat distribusi harga mobil.
        - 🏎️ **Prediksi Harga Mobil**: Prediksi harga mobil berdasarkan input.
    """, unsafe_allow_html=True)
    page = st.selectbox("Pilih Halaman", ["Beranda", "Dataset", "Grafik", "Prediksi Harga Mobil"])

# Halaman Beranda
if page == "Beranda":
    st.title("Selamat Datang di Aplikasi Prediksi Harga Mobil 🚗")
    st.markdown("""
        **Aplikasi Prediksi Harga Mobil** ini memanfaatkan model machine learning untuk memberikan estimasi harga mobil berdasarkan variabel-variabel tertentu.
        Kami menyediakan prediksi harga mobil dengan memasukkan beberapa parameter teknis seperti **Highway-mpg**, **Curbweight**, dan **Horsepower**.

        **Fitur utama aplikasi**:
        - Prediksi harga mobil yang cepat dan akurat.
        - Visualisasi data yang interaktif.
        - Desain antarmuka yang ramah pengguna dan mudah dipahami.

        **Silakan gunakan menu di sidebar untuk memulai!**
    """, unsafe_allow_html=True)
    st.image("car_image.jpg", use_container_width=True)

# Halaman Dataset
elif page == "Dataset":
    st.title("📊 Dataset Penjualan Mobil")
    st.write("""
        Berikut adalah data penjualan mobil. Anda dapat menjelajahi detail harga, model, dan spesifikasi lainnya.
    """)
    uploaded_file = "CarPrice.csv"
    try:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df, use_container_width=True)
    except FileNotFoundError:
        st.error("File dataset tidak ditemukan. Pastikan file `CarPrice.csv` ada di direktori yang benar.")

# Halaman Grafik
elif page == "Grafik":
    st.title("📈 Visualisasi Grafik Penjualan Mobil")
    try:
        df = pd.read_csv("CarPrice.csv")
        st.write("""
            Grafik berikut menunjukkan distribusi harga mobil yang ada di dataset.
            Grafik ini memberikan gambaran tentang persebaran harga mobil di pasar.
        """)
        
        # Membuat histogram distribusi harga
        fig, ax = plt.subplots()
        ax.hist(df['price'], bins=30, color='skyblue', edgecolor='black', alpha=0.8)
        ax.set_title("Distribusi Harga Mobil", fontsize=14)
        ax.set_xlabel("Harga (USD)", fontsize=12)
        ax.set_ylabel("Frekuensi", fontsize=12)
        st.pyplot(fig)
    except FileNotFoundError:
        st.error("File dataset tidak ditemukan. Pastikan file `CarPrice.csv` ada di direktori yang benar.")

# Halaman Prediksi Harga Mobil
elif page == "Prediksi Harga Mobil":
    # Load model prediksi harga mobil
    model = pickle.load(open('Model_Prediksi_Harga_Mobil.sav', 'rb'))

    st.header('Masukkan Data untuk Prediksi Harga Mobil')
    st.write("""
        Masukkan nilai untuk variabel-variabel berikut untuk mendapatkan prediksi harga mobil Anda.
        Kami akan memberikan estimasi harga berdasarkan spesifikasi mobil yang Anda pilih.
    """)

    # Input variabel independent
    highwaympg = st.number_input('Highway-mpg (mpg)', min_value=0, step=1)
    curbweight = st.number_input('Curbweight (kg)', min_value=0, step=1)
    horsepower = st.number_input('Horsepower (hp)', min_value=0, step=1)

    # Prediksi berdasarkan input
    if st.button('Prediksi Harga Mobil!'):
        # Prediksi harga mobil
        car_prediction = model.predict([[highwaympg, curbweight, horsepower]])

        # Format hasil prediksi
        harga_mobil_float = float(car_prediction[0])
        harga_mobil_formatted = "Rp {:,.0f}".format(harga_mobil_float)

        # Tampilkan hasil prediksi
        st.subheader("Hasil Prediksi Harga Mobil")
        st.markdown(f"**Prediksi Harga Mobil**: {harga_mobil_formatted}", unsafe_allow_html=True)

        # Ucapan terima kasih
        st.write("Terimakasih telah menggunakan aplikasi prediksi harga mobil! Kami harap aplikasi ini dapat membantu Anda dalam memilih mobil terbaik sesuai anggaran Anda.")
        
        # Tambahkan tombol untuk reset atau kembali ke input
        st.button("Coba Lagi", on_click=lambda: [st.session_state.clear()])

# Footer
st.markdown("""
    <style>
    .footer {
        background-color: #00796b;
        color: white;
        text-align: center;
        padding: 10px;
        font-size: 14px;
    }
    </style>
    <div class="footer">
        © 2024 Aplikasi Prediksi Harga Mobil | Dikembangkan oleh Bintang Raka Putra
    </div>
""", unsafe_allow_html=True)
