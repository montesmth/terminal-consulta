import streamlit as st
import pandas as pd

st.set_page_config(page_title="Consulta de Ligações", layout="wide")
st.title("🔍 Terminal de Consulta")

# ── Carrega seus arquivos ──────────────────────────────────────────
@st.cache_data
def carregar_dados():
    tabela1 = pd.read_excel("base_de_cadastro_norte.xlsb", engine="pyxlsb")
    return {"Dados da matrícula": tabela1}

tabelas = carregar_dados()

# ── Campo de busca ─────────────────────────────────────────────────
num = st.text_input("Digite a Matrícula:")

if num:
    encontrou = False

    for nome, df in tabelas.items():
        if "Matrícula" in df.columns:
            resultado = df[df["Matrícula"].astype(str) == str(num)]

            if not resultado.empty:
                st.subheader(f"📋 {nome}")

                for _, linha in resultado.iterrows():
                    for coluna, valor in linha.items():
                        st.write(f"**{coluna}:** {valor}")
                    st.divider()

                encontrou = True

    if not encontrou:
        st.warning("Nenhum registro encontrado para essa Matrícula.")
        
        
        
# python -m streamlit run app.py
