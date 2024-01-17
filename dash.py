import streamlit as st
import pandas as pd
import plotly.express as px


st.title(" Grafico Interativo Covid-19")
st.write('Nessa aplicação , o usuário tem a opção de escolher o estado e o tipo de informação para mostrar o gráfico.Utilize o Menu lateral para alterar a mostragem.')


df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')

df = df.rename(columns={'newDeaths': 'Novos óbitos', 'newCases': 'Novos Casos', 'deaths_per_100k_inhabitants': 'Óbitos por 100 mil habitantes', 'totalCases_per_100k_inhabitants': 'Casos por 100 mil habitantes'})

st.sidebar.write(
    'COVID - BRASIL')
estados = list(df['state'].unique())
state = st.sidebar.selectbox(
    'Selecione o Estado:  ', estados)


colunas = ['Novos óbitos','Novos Casos','Óbitos por 100 mil habitantes','Casos por 100 mil habitantes']
column = st.sidebar.selectbox(
    'Selecione o Tipo da  Informação : ', colunas)

df = df[df['state'] == state]

fig = px.line(df, x='date', y=column, title=column + '- ' + state)
fig.update_layout( xaxis_title='Data por Periodo', yaxis_title=column.upper(), title={'x': 0.5})

st.plotly_chart(fig)

st.caption('Os dados forma obtidos a partir do site : https://github.com/wcota/covid19br')



