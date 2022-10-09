import streamlit as st
import plotly.graph_objects as go
import numpy as np
import pandas as pd

uploaded_file = st.file_uploader("Archivo CSV")
if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file, sep=";", parse_dates=["Fecha"], decimal = ',', comment="#", dayfirst=True)
    fig = go.Figure()
    fig.add_trace(go.Scattergl(x=dataframe.Fecha, y=dataframe.RP70, mode="markers"))
    st.plotly_chart(fig, use_container_width=True)
    
    st.write(dataframe)
