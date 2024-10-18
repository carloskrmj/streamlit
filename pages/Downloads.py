import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Transparência e Downloads", layout="wide")

# Título da página
st.title("Transparência e Downloads")

st.header("NF's de parcerias publicas")

# Carregar o arquivo PDF
with open("assets/documentos/35503082229899331000197000000000000824065208566351.pdf", "rb") as pdf_file:
    danfe_12062024 = pdf_file.read()

with open("assets/documentos/35503082229899331000197000000000000924076481969951.pdf", "rb") as pdf_file:
    danfe_02072024 = pdf_file.read()

# Criação do botão de download para o PDF
st.download_button(
    label="Baixar PDF - danfe_12-06-2024",
    data=danfe_12062024,
    file_name="danfe_12-06-2024.pdf",
    mime="application/pdf"
)

# Criação do botão de download para o PDF
st.download_button(
    label="Baixar PDF - danfe_02-07-2024",
    data=danfe_02072024,
    file_name="danfe_02-07-2024.pdf",
    mime="application/pdf"
)
