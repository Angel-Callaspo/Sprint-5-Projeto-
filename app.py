import pandas as pd
import plotly.express as px
import streamlit as st
from pathlib import Path

df_carro = pd.read_csv(Path("data/vehicles.csv")) # lendo dados

#criar_botao = st.button('Filtrar por nodelos') # criar um botão
#if criar_botao: # se botão for clicado
 
col1 = st.text_input('inserir modelo')
botao_executar = st.button('Filtra')
st.write('Banco de dados de Anuncios de Carros')
st.dataframe(df_carro)
if botao_executar:
    filtro = df_carro[df_carro['model']==col1]
    if len(filtro) == 0:
        st.write(f"O modelo '{col1}', Não está registrado")
    else:
        st.write(f'Relatorio para o modelo: {col1}')
        st.dataframe(filtro)
