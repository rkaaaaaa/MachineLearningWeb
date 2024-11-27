import pickle
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Load model prediksi harga mobil
model = pickle.load(open('Model_Prediksi_Harga_Mobil.sav', 'rb'))

# Set title of the page
st.title('Prediksi Harga Mobil')



# Dataset
st.header('Dataset Mobil')
st.write("Berikut adalah dataset yang digunakan untuk prediksi harga mobil.")
df1 = pd.read_csv('CarPrice.csv')
st.dataframe(df1)

# Visualisasi grafik Highway-mpg
st.header("Grafik Relasi Highway-mpg dan Harga Mobil")
st.write("Grafik ini menunjukkan hubungan antara 'Highway-mpg' dan harga mobil.")
chart_highwaympg = alt.Chart(df1).mark_line().encode(
    x='highwaympg',
    y='price'
).properties(
    width=600,
    height=400
)
st.altair_chart(chart_highwaympg, use_container_width=True)

# Visualisasi grafik Curbweight
st.header("Grafik Relasi Curbweight dan Harga Mobil")
st.write("Grafik ini menunjukkan hubungan antara 'Curbweight' dan harga mobil.")
chart_curweight = alt.Chart(df1).mark_line().encode(
    x='curbweight',
    y='price'
).properties(
    width=600,
    height=400
)
st.altair_chart(chart_curweight, use_container_width=True)

# Visualisasi grafik Horsepower
st.header("Grafik Relasi Horsepower dan Harga Mobil")
st.write("Grafik ini menunjukkan hubungan antara 'Horsepower' dan harga mobil.")
chart_horsepower = alt.Chart(df1).mark_line().encode(
    x='horsepower',
    y='price'
).properties(
    width=600,
    height=400
)
st.altair_chart(chart_horsepower, use_container_width=True)

# Form Input untuk prediksi
st.header('Masukkan Data untuk Prediksi Harga Mobil')
st.write("Masukkan nilai variabel independent berikut untuk melakukan prediksi harga mobil.")

# Input variabel independent
highwaympg = st.number_input('Highway-mpg (mpg)', min_value=0, step=1)
curbweight = st.number_input('Curbweight (kg)', min_value=0, step=1)
horsepower = st.number_input('Horsepower (hp)', min_value=0, step=1)

# Prediksi berdasarkan input
if st.button('Prediksi!'):
    # Prediksi harga mobil
    car_prediction = model.predict([[highwaympg, curbweight, horsepower]])
    
    # Format hasil prediksi
    harga_mobil_float = float(car_prediction[0])
    harga_mobil_formatted = "Rp {:,.0f}".format(harga_mobil_float)

    # Tampilkan hasil prediksi
    st.subheader("Hasil Prediksi")
    st.write(f"Prediksi Harga Mobil: {harga_mobil_formatted}")

    st.write("Terimakasih telah menggunakan aplikasi prediksi harga mobil!")
