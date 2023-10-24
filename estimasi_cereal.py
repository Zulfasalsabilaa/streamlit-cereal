import pickle
import streamlit as st

model = pickle.load(open('estimasi_cereal.sav', 'rb'))

st.title('Estimasi Kandungan Serat')

calories = st.number_input('Input Kandungan Kalori')
protein = st.number_input('Input Kandungan Protein')
fat = st.number_input('Input Kandungan Lemak')
sodium = st.number_input('Input Natrium')
sugars = st.number_input('Input Kandungan Sugars')
potass = st.number_input('Input Kandungan Potassium ')
vitamins = st.number_input('Input Vitamin ')

predict = ''

if st.button('Estimasi Kandungan Serat'):
    predict = model.predict(
        [[calories, protein, fat, sodium, sugars, potass, vitamins]]
    )
    st.write ('Estimasi Kandungan Serat Pada Cereal : ', predict)