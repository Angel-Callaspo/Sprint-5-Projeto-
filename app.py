import pandas as pd
import plotly.express as px
import streamlit as st
from pathlib import Path

df_carro = pd.read_csv(Path("data/vehicles.csv")) # lendo dados
histog_botao = st.button('Criar histograma') # criar um botão

if histog_botao: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig = px.histogram(df_carro, x= 'odometer')

    # exibir um grafico Plotly interativo
    st.plotly_chart(fig) #use_container_width=True

