import pandas as pd
import plotly.express as px
import streamlit as st
from pathlib import Path

df_carro = pd.read_csv(Path("data/vehicles.csv")) # lendo dados

fig = px.histogram(df_carro, x= 'odometer')
st.plotly_chart(fig)