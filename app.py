import pandas as pd
import plotly.express as px
import streamlit as st
from pathlib import Path

df_carro = pd.read_csv(Path("data/vehicles.csv")) # lendo dados
st.title('Dashboard Anuncios de Carros')
criar_caixa_mod_qua = st.checkbox('Modelos Anunciados') # criar uma caixa histograma
criar_caixa_mod_pre = st.checkbox('Modelos vs Preços Médios') # criar caixa de seleção
criar_caixa_pre_hod = st.checkbox('Preços vs hodômetro') # criar caixa de seleção
criar_bot_filtro = st.button('Filtra dados por modelos') # criar botão filtrar base dados

if criar_caixa_mod_qua: # se o botão for clicado
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(df_carro, x="model") # criar um histograma
    st.title('Quantidade de Modelos de carros anunciados')
    fig.show()
    #st.plotly_chart(fig, use_container_width=True) # exibir um gráfico Plotly interativo
      
if criar_caixa_mod_pre: # se a caixa for clicado
    df_mod_pri = df_carro.groupby('model')['price'].median().reset_index()
    fig = px.bar(df_mod_pri, x='model', y='price') # criar um histograma
    st.title('Modelos vs Preços Médios') # criando titulo para nosso dashboard
    fig.show()
    #st.plotly_chart(fig, use_container_width=True) # exibir um gráfico Plotly interativo
    
    criar_botao = st.button('Ver dados') # criar um botão
    if criar_botao: # se botão for clicado
        resumo = df_carro.loc[:,['model', 'price']]
        st.dataframe(resumo)

if criar_caixa_pre_hod:
    fig = px.scatter(df_carro, x='price', y='odometer')
    st.title('Preços vs hodômetro') # criando titulo para nosso dashboard
    fig.show()
    #st.plotly_chart(fig, use_container_width=True) # exibir um gráfico Plotly interativo

    criar_botao = st.button('Ver dados') # criar um botão
    if criar_botao: # se botão for clicado
        resumo = df_carro.loc[:,['odometer', 'price']]
        st.dataframe(resumo)

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
