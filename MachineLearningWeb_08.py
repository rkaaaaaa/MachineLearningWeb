import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#8. Buatlah sebuah web untuk menampilkan image, dataset (csv), dan grafik sesuai menu selectbox yang dipilih pada left sidebar seperti pada gambar dibawah ini. Sumber image dan dataset yang digunakan bebas.
st.write('8. Buatlah sebuah web untuk menampilkan image, dataset (csv), dan grafik sesuai menu selectbox yang dipilih pada left sidebar seperti pada gambar dibawah ini. Sumber image dan dataset yang digunakan bebas.')

# Sidebar
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🚗 Data Mobil</h1>", unsafe_allow_html=True)
    st.markdown("---")  # Garis pemisah
    st.markdown(
        """
        **Navigasi Halaman**  
        Gunakan menu di bawah untuk menjelajahi:
        - 🔍 **Beranda**: Lihat pengenalan aplikasi.
        - 📊 **Dataset**: Jelajahi data penjualan mobil.
        - 📈 **Grafik**: Lihat distribusi harga mobil.
        """
    )
    # Dropdown menu
    page = st.selectbox("Pilih Halaman", ["Beranda", "Dataset", "Grafik"])


# Halaman Beranda
if page == "Beranda":
    st.title("Selamat Datang di Aplikasi Visualisasi Data Penjualan Mobil 🚗")
    st.write(
        """
        Aplikasi ini dirancang untuk membantu Anda menjelajahi data penjualan mobil
        dengan mudah. Anda dapat melihat gambar, mempelajari dataset, dan 
        memvisualisasikan data dalam bentuk grafik yang menarik.
        """
    )
    st.image("Jual_Mobil.jpeg", caption="Beli Mobil Impian Anda", use_container_width=True)

# Halaman Dataset
elif page == "Dataset":
    st.title("📊 Dataset Penjualan Mobil")
    st.write(
        """
        Berikut adalah data penjualan mobil. Anda dapat menjelajahi detail harga,
        model, dan spesifikasi lainnya.
        """
    )
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
        st.write(
            """
            Grafik berikut menunjukkan distribusi harga mobil yang ada di dataset.
            Grafik ini memberikan gambaran tentang persebaran harga mobil di pasar.
            """
        )
        # Membuat histogram distribusi harga
        fig, ax = plt.subplots()
        ax.hist(df['price'], bins=30, color='skyblue', edgecolor='black', alpha=0.8)
        ax.set_title("Distribusi Harga Mobil", fontsize=14)
        ax.set_xlabel("Harga (USD)", fontsize=12)
        ax.set_ylabel("Frekuensi", fontsize=12)
        st.pyplot(fig)
    except FileNotFoundError:
        st.error("File dataset tidak ditemukan. Pastikan file `CarPrice.csv` ada di direktori yang benar.")