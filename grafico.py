import pandas as pd
import streamlit as st

df = pd.read_csv('tempo_uso_apps.csv')

st.title("📱 Tempo médio gasto por dia em aplicativos")
st.caption("Dados fictícios, mas provavelmente bem reais pra nossa vida 😅")

st.caption("Tempo médio diário gasto em aplicativos (em horas)")

st.dataframe(df)

st.bar_chart(df.set_index('dia'))
