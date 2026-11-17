import streamlit as st
import pandas as pd
import plotly.express as px


caminho_ou_arquivo = pd.read_excel("dados-educacao.xlsx")
df = pd.read_excel("dados-educacao.xlsx")
st.set_page_config(
    page_title="DADOS-EDUCAÇÃO",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)


@st.cache_data
def carregar_e_limpar_dados(caminho_ou_arquivo):
    if isinstance(caminho_ou_arquivo, str):
        bruto = pd.read_excel(caminho_ou_arquivo, sheet_name='genero', header=2)
    else:
        bruto = pd.read_excel(caminho_ou_arquivo, sheet_name='genero', header=2)


    df = df.rename(columns={
        "genero": "gn",
        "idade": "ida",
        "escolaridade": "eclo"
    })


    df["ida"] = pd.to_numeric(df["ida"], errors="coerce")


    df = bruto.dropna(pd.DataFrame(caminho_ou_arquivo))

    return df

df = pd.DataFrame(caminho_ou_arquivo)
    

df_filtrado = df[
    (df["genero"].isin(["masculino", "feminino"])) 
].copy()

df_tabela = df_filtrado[["genero"]]
