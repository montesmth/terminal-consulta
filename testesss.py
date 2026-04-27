import streamlit as st
from supabase import create_client

st.set_page_config(page_title="Consulta de Matrículas", layout="wide")
st.title("🔍 Terminal de Consulta")

@st.cache_resource
def conectar():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)

supabase = conectar()

# ── DIAGNÓSTICO TEMPORÁRIO ─────────────────────────────────────────
st.subheader("🔧 Diagnóstico")

try:
    teste = supabase.table("Database_Cadastro").select("*").limit(3).execute()
    
    if teste.data:
        st.success("✅ Conexão OK!")
        st.write("**Primeiras 3 linhas:**")
        st.write(teste.data)
        st.write("**Colunas encontradas:**")
        st.write(list(teste.data[0].keys()))
    else:
        st.error("❌ Tabela vazia ou sem permissão de leitura")
except Exception as e:
    st.error(f"❌ Erro na conexão: {e}")
# ──────────────────────────────────────────────────────────────────

num = st.text_input("Digite a Matrícula:")
# ... resto do código
