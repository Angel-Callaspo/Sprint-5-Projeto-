import pandas as pd
import plotly.express as px
import streamlit as st
from pathlib import Path

df_carro = pd.read_csv(Path("data/vehicles.csv")) # lendo dados

df = px.df_carro
st.write(st.df['molde'])

