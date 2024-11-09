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


left_co, cent_co, right_co = st.columns([1, 10, 1])



with cent_co:
    # Inserir a imagem logo abaixo do separador
    st.image("assets/lgbt-banner-11-2024.png", width=830)


# centered
st.markdown(
    """<h3><a style='display: block; text-align: center;' href="https://forms.gle/ySKFH2KJaZnXaHnA8">4º JOGOS LGBTQIAPN+ - INSCRIÇÃO 2024</a></h3>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """<h4>Nos dias 23, 24, 30 de novembro e 01 de dezembro acontecerá no Centro Olímpico de Treinamento e Pesquisa (Voleibol, Handebol e Futsal) e no CERET (Rugby) a 4ª edição dos Jogos LGBTQIAPN+.</h4>
    """,
    unsafe_allow_html=True,
)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown(
    """<h5><a style='display: block; text-align: center;' href="https://forms.gle/ySKFH2KJaZnXaHnA8">INSCREVA-SE AQUI</a></h5>
    """,
    unsafe_allow_html=True,
)


