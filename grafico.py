import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título
st.title("🚛 Pontuação por Construtora - Temporada 2025")

# Upload do arquivo
uploaded_file = st.file_uploader("Faça upload do arquivo CSV", type="csv")

if uploaded_file:
    try:
        # Carregar os dados
        df = pd.read_csv(uploaded_file)

        # Verifica colunas disponíveis
        st.write("📊 Colunas encontradas no arquivo:")
        st.write(df.columns)

        # Verifica se as colunas necessárias existem
        if 'constructorId' in df.columns and 'points' in df.columns:
            # Agrupar e somar pontos por construtora
            df_grouped = df.groupby('constructorId')['points'].sum().reset_index()

            # Ordenar para visualização
            df_grouped = df_grouped.sort_values(by='points', ascending=False)

            # Mostrar DataFrame
            st.subheader("🏆 Pontuação Total por Construtora")
            st.dataframe(df_grouped)

            # Plotar gráfico de barras
            fig, ax = plt.subplots()
            ax.bar(df_grouped['constructorId'], df_grouped['points'], color='skyblue')
            ax.set_xlabel("Construtora")
            ax.set_ylabel("Pontos")
            ax.set_title("Pontuação por Construtora - Temporada 2025")
            plt.xticks(rotation=45)

            st.pyplot(fig)
        else:
            st.error("❌ O arquivo precisa ter as colunas 'constructorId' e 'points'. Confira o cabeçalho.")
    except Exception as e:
        st.error(f"😵 Ocorreu um erro ao processar os dados: {e}")
else:
    st.info("👆 Faça upload de um arquivo CSV para começar.")
