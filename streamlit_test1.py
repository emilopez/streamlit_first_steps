import streamlit as st
import plotly.graph_objects as go
import numpy as np

x = np.arange(0,1,0.01)
y = np.sin(2*np.pi*x*2)

fig = go.Figure()
fig.add_trace(go.Scattergl(x=x, y=y))

st.plotly_chart(fig, use_container_width=True)

