import pandas as pd
import streamlit as st

st.title("🏎️ Pontuação por Construtora - Temporada 2025")

df = pd.read_csv("constructor_results_2025.csv")

df_grouped = df.groupby('constructorId')['points'].sum().reset_index()

df_grouped = df_grouped.sort_values(by='points', ascending=False)

st.write("Ranking de Construtoras por Pontos:")
st.dataframe(df_grouped)

st.bar_chart(df_grouped.set_index('constructorId'))
