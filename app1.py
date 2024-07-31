import pandas as pd
import plotly.express as px
import streamlit as st
from pathlib import Path

df_carro = pd.read_csv(Path("data/vehicles.csv")) # lendo dados
criar_botao = st.button('Modelos: histograma') # criar um botão
criar_caixa_mod_pre = st.checkbox('Modelos vs Preços Médios') # criar caixa de seleção
criar_caixa_pre_hod = st.checkbox('Criar um histograma') # criar caixa de seleção

if criar_botao: # se o botão for clicado
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(df_carro, x="model") # criar um histograma
    st.title('Quantidade de Modelos de carros anunciados')
    fig.show()
    st.plotly_chart(fig, use_container_width=True) # exibir um gráfico Plotly interativo

if criar_caixa_mod_pre: # se a caixa for clicado
    df_mod_pri = df_carro.groupby('model')['price'].median().reset_index()
    fig = px.bar(df_mod_pri, x='model', y='price') # criar um histograma
    st.title('Modelos vs Preços Médios') # criando titulo para nosso dashboard
    fig.show()
    st.plotly_chart(fig, use_container_width=True) # exibir um gráfico Plotly interativo

if criar_caixa_pre_hod:
    fig = px.scatter(df_carro, x='price', y='odometer')
    st.title('Preços vs hodômetro') # criando titulo para nosso dashboard
    fig.show()
    st.plotly_chart(fig, use_container_width=True) # exibir um gráfico Plotly interativo