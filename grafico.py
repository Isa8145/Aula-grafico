import pandas as pd
import streamlit as st

# Título e descrição
st.title("📱 Tempo médio diário em aplicativos")

df = pd.read_csv("tempo_uso_apps_horas.csv")

st.subheader("📋 Tabela de dados")
st.dataframe(df)

st.subheader("📈 Gráfico de uso por dia da semana")
st.line_chart(df.set_index("dia"))

st.markdown("> *Saia da tela e viva mais!!!* 😄")
