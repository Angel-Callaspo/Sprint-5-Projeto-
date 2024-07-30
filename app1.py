import pandas as pd
import plotly.express as px
import streamlit as st
from pathlib import Path

df_carro = pd.read_csv(Path("data/vehicles.csv")) # lendo dados
hist_button = st.button('Criar histograma') # criar um botão

if hist_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    
    # criar um histograma
    fig = px.histogram(df_carro, x="odometer")

    # criando titulo para nosso dashboard
    st.title('Frequência de hodômetro dos carros')

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)