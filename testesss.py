import streamlit as st
from supabase import create_client
import os

st.set_page_config(page_title="Pesquisa de Matrículas", layout="wide")

st.title("🔍 Debug de Conexão")

@st.cache_resource
def conectar():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key), url

supabase, url = conectar()

st.write(f"URL sendo usada: `{url}`")

# Listar todas as tabelas visíveis
try:
    response = supabase.table("base_cadastral_norte") \
        .select("*") \
        .limit(1) \
        .execute()
    st.write("Conexão OK!")
    st.write(response.data)
except Exception as e:
    st.error(f"Erro detalhado: {e}")
