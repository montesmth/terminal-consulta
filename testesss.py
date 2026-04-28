import streamlit as st
from supabase import create_client
import os

st.set_page_config(page_title="Pesquisa de Matrículas", layout="wide")

caminho_css = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".streamlit", "styles.css")
with open(caminho_css) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🔍 Terminal de Consulta")

@st.cache_resource
def conectar():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)

supabase = conectar()

# Teste direto - sem filtro nenhum
try:
    response = supabase.table("base_cadastral_norte") \
        .select("*") \
        .limit(1) \
        .execute()
    st.write("Conexão OK!")
    st.write(response.data)
except Exception as e:
    st.error(f"Erro detalhado: {e}")
