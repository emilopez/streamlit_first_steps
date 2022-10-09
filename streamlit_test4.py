import streamlit as st
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import datetime

#mapbox_access_token = open(".mapbox_token").read()
mapbox_access_token = st.secrets["mapbox_token"]

st.set_page_config(
     page_title="Pronóstico Río Salado",
     page_icon="❤️",
     layout="wide",
     initial_sidebar_state="expanded",
)

c1, c2 = st.columns([2, 1])

with c1:
    start_date = st.date_input("Visualizar desde", datetime.date.today()-datetime.timedelta(days=7))
    
    uploaded_file = c1.file_uploader("Cargar un archivo csv", type=["csv"])
    if uploaded_file is not None:
        
        dataframe = pd.read_csv(uploaded_file, sep=";", parse_dates=["Fecha"], decimal = ',', comment="#", dayfirst=True)

        mask_date = dataframe['Fecha'] > pd.Timestamp(start_date)
        dataframe = dataframe.loc[mask_date]

        fig = go.Figure()
        fig.add_trace(go.Scattergl(x=dataframe.Fecha, y=dataframe.RP70, mode="markers"))
        st.plotly_chart(fig, use_container_width=True)
        st.write(dataframe)

        ## Columna 2
        with c2:
            estaciones_sah_df = pd.read_csv("datos/meta_estaciones_sah.csv", sep=";", decimal = ',')
            estaciones_sah = go.Scattermapbox(mode = "markers", lon = estaciones_sah_df["lng"], lat = estaciones_sah_df["lat"], marker = {'size': 10}, name = "",
                                              hovertemplate =   "<b>" + estaciones_sah_df["Nombre"] + "</b><br><br>" +
                                                                "Coord: %{lon},%{lat}<br>"+
                                                                "Río: " + estaciones_sah_df["Rio"] + "<br>" +
                                                                "Ruta: "+ estaciones_sah_df["Ruta"] +"<br>" +
                                                                "Descripción:" + estaciones_sah_df["Descripción"]
                                             )

            layout = go.Layout(
                title = "Estaciones SAH",
                title_x=0.5,
                title_y=0.95,
                width=400, height=630, 
                margin ={'l':0,'t':50,'b':0,'r':0},
                
                mapbox = {
                    'accesstoken':mapbox_access_token,
                    'center': {'lat': -30.3, 'lon': -61},
                    'style': "satellite-streets",
                    'zoom': 7})

            data = [estaciones_sah]
            figure = go.Figure(data=data, layout=layout)
            st.plotly_chart(figure, use_container_width=True)
