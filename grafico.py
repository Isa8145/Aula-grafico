import pandas as pd
import streamlit as st

try: 
  tot_registros = df.count() ['total']
except: 
  df = pd.read_csv('constructor_results_2025.csv')

st.bar_chart(df, x='month', y='total')
