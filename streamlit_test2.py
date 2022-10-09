import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader("Archivo CSV")
if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file, sep=";")
    st.write(dataframe)
