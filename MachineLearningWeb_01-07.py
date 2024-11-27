#233307097 - Bintang Raka Putra

#1. Mengimpor library streamlit

import streamlit as st

st.write('Halo Dunia')

#2. Membuat aksi dari button.
st.write('2. Membuat aksi dari button.')
st.header('st.button')

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')
    
#Susunlah kode untuk hasil form di bawah ini
st.write('3. Susunlah kode untuk hasil form di bawah ini')
st.title("this is the app title")
st.markdown("""
this is the markdown
---
### this is the header
#### this is the subheader
this is the caption
""")

#Susunlah kode untuk hasil form di bawah ini.
st.write('4. Susunlah kode untuk hasil form di bawah ini.')
# Checkbox
if st.checkbox("yes"):
    st.write("Checkbox is checked!")

# Button
if st.button("Click"):
    st.write("Button clicked!")

# Radio buttons
gender = st.radio("Pick your gender", ("Male", "Female"))
st.write(f"Selected gender: {gender}")

# Dropdown
dropdown_gender = st.selectbox("Pick your gender", ("Male", "Female"))
st.write(f"Dropdown gender: {dropdown_gender}")

planet = st.selectbox("Choose a planet", ("Choose an option", "Mercury", "Venus", "Earth", "Mars"))
st.write(f"Selected planet: {planet}")

# Slider for marks
mark = st.slider("Pick a mark", min_value=0, max_value=100, value=50, step=1)
st.write("Your mark:", mark)

# Slider for numbers
number = st.slider("Pick a number", min_value=0, max_value=50, value=9, step=1)
st.write("Your number:", number)


#Susunlah kode untuk hasil form di bawah ini.
st.write('5. Susunlah kode untuk hasil form di bawah ini.')
# Number input
number = st.number_input("Pick a number", min_value=1, max_value=100, value=1, step=1)
st.write(f"You picked: {number}")

# Email input
email = st.text_input("Email address")
st.write(f"Email entered: {email}")

# Date input
travel_date = st.date_input("Travelling date")
st.write(f"Travelling date: {travel_date}")

# Time input
school_time = st.time_input("School time", value=None)
st.write(f"School time: {school_time}")

# Multiline text input
description = st.text_area("Description")
st.write(f"Description: {description}")

# File uploader
uploaded_file = st.file_uploader("Upload a photo", type=["jpg", "jpeg", "png"])
if uploaded_file:
    st.image(uploaded_file, caption="Uploaded photo", use_column_width=True)

# Color picker
favorite_color = st.color_picker("Choose your favourite color", value="#800080")
st.write(f"Favourite color: {favorite_color}")


#Memuat sebuah Dataframe yang berisi data numerik, dan membuat visualisasi data numerik random ke dalam sebuah plot chart.
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.write('6. Memuat sebuah Dataframe yang berisi data numerik, dan membuat visualisasi data numerik random ke dalam sebuah plot chart.')
st.header('st.write')
st.write('Hello, *World!* :sunglasses:')

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write(df)

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c']
)
c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
)
st.write(c)

st.write('7. Buatlah line chart sesuai dengan kode berikut ini. Lalu tambahkan bar chart dan area chart.')

df3= pd.DataFrame(
    np.random.randn(10, 2),
    columns=['x', 'y'])
st.line_chart(df3)

