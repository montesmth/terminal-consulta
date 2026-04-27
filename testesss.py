import streamlit as st
from supabase import create_client

st.set_page_config(page_title="Pesquisa de Matrículas", layout="wide")
st.title("🔍 Terminal de Consulta")

@st.cache_resource
def conectar():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)

supabase = conectar()

num = st.text_input("Digite a Matrícula:")

if num:
    try:
        response = supabase.table("base_cadastral_norte") \
            .select("*") \
            .eq("Matricula", int(num)) \
            .execute()

        if response.data:
            st.subheader("📋 Dados da Matrícula")
            for linha in response.data:
                for coluna, valor in linha.items():
                    st.write(f"**{coluna}:** {valor}")
                st.divider()
        else:
            st.warning("Nenhum registro encontrado para essa Matrícula.")
    except ValueError:
        st.error("Digite apenas números na matrícula.")
