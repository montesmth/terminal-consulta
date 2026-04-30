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


def exibir_resultados(dados):
    if dados:
        st.subheader("📋 Dados encontrados")
        for linha in dados:
            for coluna, valor in linha.items():
                st.write(f"**{coluna}:** {valor}")
            st.divider()
    else:
        st.warning("Nenhum registro encontrado.")

aba_matricula, aba_medidor = st.tabs(["📄 Busca por Matrícula", "💧 Busca por Nº do HD"])

with aba_matricula:
    st.markdown("### Pesquisar por Matrícula")
    num_matricula = st.text_input("Digite a Matrícula:", key="input_matricula")

    if num_matricula:
        try:
            response = (
                supabase.table("base_rio_norte_v3")
                .select("*")
                .eq("Matricula", int(num_matricula))
                .execute()
            )
            exibir_resultados(response.data)
        except ValueError:
            st.error("Digite apenas números na matrícula.")
        except Exception as e:
            st.error(f"Erro detalhado: {e}")

with aba_medidor:
    st.markdown("### Pesquisar por Número do Medidor")
    num_medidor = st.text_input("Digite o Número do Medidor:", key="input_medidor")

    if num_medidor:
        try:
            response = (
                supabase.table("base_rio_norte_v3")
                .select("*")
                .eq("HD", num_medidor)   
                .execute()
            )
            exibir_resultados(response.data)
        except Exception as e:
            st.error(f"Erro detalhado: {e}")
