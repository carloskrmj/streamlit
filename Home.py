import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# Configurações da página
st.set_page_config(page_title="Projeto Social T3", layout="wide")

# Estilo customizado para centralizar o título e aproximá-lo do topo
st.markdown(
    """
    <style>
    .title {
        text-align: center;
        margin-top: -50px;
    }
    .menu {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    .menu button {
        margin: 0 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título centralizado
st.markdown('<h1 class="title">Bem-vindo à Associação Desportiva T3</h1>', unsafe_allow_html=True)
st.write('---')

col1, col2, col3 = st.columns([2,3,3])
with col2:
    # Inserir a imagem logo abaixo do separador
    st.image("assets/favpng_black-belt-judo-dan-brazilian-jiu-jitsu.png", caption="BJJ", width=400)

st.markdown('</div>', unsafe_allow_html=True)

# Conteúdo da página principal
st.write("Em construção")