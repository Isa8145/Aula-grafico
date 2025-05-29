import pandas as pd
import streamlit as st

df = pd.read_csv('dados_temperatura.csv')

st.write("📊 Dados de Temperatura por Mês")
st.dataframe(df)

st.bar_chart(data=df, x='mes', y='temperatura')

