import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Downloads", layout="wide")

# Título da página
st.title("Página de Downloads")

# Conteúdo da página de downloads
st.write("Em construção")

# Botão para voltar à página principal
if st.button("Voltar para a Página Principal"):
    switch_page("app")