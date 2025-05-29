import pandas as pd
import streamlit as st

try: 
  tot_registros = df.count() ['total']
except: 
  df = pd.read_csv('https://www.kaggle.com/datasets/umerhaddii/f1-japanese-grand-prix-2025#')

st.bar_chart(df, x='month', y='total')
