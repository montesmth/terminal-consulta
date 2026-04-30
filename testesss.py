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

num = st.text_input("Digite a Matrícula:")

if num:
    try:
        response = supabase.table("base_rio_norte_v3") \
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
    except Exception as e:
        st.error(f"Erro detalhado: {e}")
