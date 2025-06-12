from pathlib import Path
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

EXCEL_FILE = "pythonlog.xlsx"
SHEET_NAME = "Página1"

@st.cache_data(show_spinner=False)
def carregar_planilha(file, sheet):
    df = pd.read_excel(file, sheet_name=sheet)
    df.dropna(how="all", inplace=True)
    df["DATA"] = pd.to_datetime(df["DATA"], errors="coerce")

    colunas_numericas = [
        "QTD PEDIDOS", "QTD.COLABORADORES", "PESO TOTAL",
        "OCORRÊNCIAS", "AVARIAS",
        "QTD VUC", "QTD DUCATO", "QTD HR", "QTD FIORINO", "QTD MONTANA", "QTD SAVEIRO",
        "RECEBIMENTOS", "EXPEDIÇÃO", "ORGANIZAÇÃO INTERNA", "EMBALAMENTO"
    ]
    df[colunas_numericas] = df[colunas_numericas].apply(pd.to_numeric, errors="coerce")
    return df

@st.cache_data(show_spinner=False)
def calcular_kpis(df):
    total_pedidos = df["QTD PEDIDOS"].sum()
    soma_colaboradores = df["QTD.COLABORADORES"].sum()
    media_colab = df["QTD.COLABORADORES"].mean()
    total_peso = df["PESO TOTAL"].sum()
    total_ocor = df["OCORRÊNCIAS"].sum()
    total_avar = df["AVARIAS"].sum()

    prod_colab = total_pedidos / soma_colaboradores if soma_colaboradores > 0 else None

    return {
        "Total de Pedidos": total_pedidos,
        "Média de Colaboradores": media_colab,
        "Total de Peso (kg)": total_peso,
        "Total de Ocorrências": total_ocor,
        "Total de Avarias": total_avar,
        "Produtividade por Colaborador": prod_colab,
    }

@st.cache_data(show_spinner=False)
def totais_custom(df):
    veic_cols = [
        "QTD VUC", "QTD DUCATO", "QTD HR", "QTD FIORINO", "QTD MONTANA", "QTD SAVEIRO"
    ]
    set_cols = [
        "RECEBIMENTOS", "EXPEDIÇÃO", "ORGANIZAÇÃO INTERNA", "EMBALAMENTO"
    ]
    return df[veic_cols].sum(), df[set_cols].sum()

# ------------------- INTERFACE UI -------------------
st.set_page_config(page_title="Relatório Operacional – Tanaka", layout="wide")
st.title("📊 Relatório Operacional – Tanaka")

with st.sidebar:
    st.header("🔧 Configurações")
    uploaded_file = st.file_uploader("Selecione a planilha (.xlsx)", type=["xlsx"])
    sheet_input = st.text_input("Nome da aba", value=SHEET_NAME)

if uploaded_file is not None:
    df = carregar_planilha(uploaded_file, sheet_input)
else:
    default_path = Path(EXCEL_FILE)
    if not default_path.exists():
        st.error(f"Arquivo {EXCEL_FILE} não encontrado em {default_path.parent}.")
        st.stop()
    df = carregar_planilha(default_path, sheet_input)

# -------------------- KPIs ---------------------
kp = calcular_kpis(df)
cols = st.columns(len(kp))
for col, (nome, valor) in zip(cols, kp.items()):
    if valor is None:
        col.metric(nome, "N/A")
    else:
        if isinstance(valor, float):
            valor_fmt = f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        else:
            valor_fmt = f"{valor:,}".replace(",", ".")
        col.metric(nome, valor_fmt)

st.divider()

# -------------------- GRÁFICOS ---------------------
sns.set(style="whitegrid")
soma_veic, total_set = totais_custom(df)

# Total por Setor
st.subheader("📦 Total por Setor")
fig1, ax1 = plt.subplots(figsize=(8, 4))
bars1 = ax1.bar(total_set.index, total_set.values, color="#1f77b4")
ax1.set_ylabel("Unidades")
ax1.set_xlabel("Setor")
ax1.bar_label(bars1, fmt="%.0f", padding=3)
plt.xticks(rotation=15)
st.pyplot(fig1)

# Veículos
st.subheader("🚚 Uso de Veículos")
fig2, ax2 = plt.subplots(figsize=(8, 4))
bars2 = ax2.bar(soma_veic.index, soma_veic.values, color="#3c4bda")
ax2.set_ylabel("Qtd. Veículos")
ax2.set_xlabel("Tipo de Veículo")
ax2.bar_label(bars2, fmt="%.0f", padding=3)
plt.xticks(rotation=15)
st.pyplot(fig2)

# Pedidos por Dia
st.subheader("📈 Pedidos por Dia")
fig3, ax3 = plt.subplots(figsize=(10, 4))
linha = df.sort_values("DATA").set_index("DATA")["QTD PEDIDOS"]
ax3.plot(linha.index, linha.values, marker="o")
ax3.set_ylabel("Pedidos")
ax3.set_xlabel("Data")
plt.xticks(rotation=15)
st.pyplot(fig3)

with st.expander("🔍 Ver DataFrame Original"):
    st.dataframe(df)

st.success("Relatório carregado! Caso não veja dados, verifique colunas e valores da planilha.")
