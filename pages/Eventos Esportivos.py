import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_carousel import carousel

st.set_page_config(page_title="Eventos Esportivos", layout="wide")

# Título da página
st.title("Confira nossos eventos")


amistoso_volei = [
    dict(
        title="",
        text="",
        img="assets/Amistoso de vôlei Clube  Guapira São Paulo/2e8ca80a-71af-4c2d-8c8f-309de9bc1713.jpg",

    ),
    dict(
        title="",
        text="",
        img="assets/Amistoso de vôlei Clube  Guapira São Paulo/94f856cc-6ba5-4418-8c2b-284b5f5f4cc6.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/Amistoso de vôlei Clube  Guapira São Paulo/a2be1bf6-a9a7-4656-89e9-64c929471d6a.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/Amistoso de vôlei Clube  Guapira São Paulo/def74b2c-07dc-4e81-b31d-2fac4f56d6e5.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/Amistoso de vôlei Clube  Guapira São Paulo/e23cdcf6-d50c-432c-83bf-b1f225581849.jpg",

    ),
]

st.write('Amistoso de vôlei Clube  Guapira São Paulo - 15/11/2023')
carousel(items=amistoso_volei, wrap=True)


copa_liga_zn = [
    dict(
        title="",
        text="",
        img="assets/Copa Liga Zona Norte/4fc3300c-2588-4441-bea8-2776bd750445.jpg",
    ),
    dict(
            title="",
            text="",
            img="assets/Copa Liga Zona Norte/5c11b985-69d2-44c6-bd55-de68ccdb7402.jpg",
        ),
    dict(
            title="",
            text="",
            img="assets/Copa Liga Zona Norte/62e96818-e219-47e6-9cee-5a2cf01c4708.jpg",
        ),
    dict(
            title="",
            text="",
            img="assets/Copa Liga Zona Norte/854d4c83-d156-4f94-a38b-3eb5627d88f3.jpg",
        ),
    dict(
            title="",
            text="",
            img="assets/Copa Liga Zona Norte/78376c15-8bc6-4723-aea5-02e692d1872f.jpg",
        ),
    dict(
            title="",
            text="",
            img="assets/Copa Liga Zona Norte/b59439c9-55bd-41cc-9d41-88df215c9f13.jpg",
        ),
    dict(
            title="",
            text="",
            img="assets/Copa Liga Zona Norte/e720833c-a165-4c05-abd9-6cb8517139e0.jpg",
        ),

]

st.write('Copa Liga Zona Norte - 03-02-2024 - Ginásio CDC Curtiball - Público 1200 pessoas')
carousel(items=copa_liga_zn, wrap=True)


copa_martins = [
    dict(
        title="",
        text="",
        img="assets/Copa Martins Neto 2023/18b5a86f-f971-4556-8df6-176c5310416b.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/Copa Martins Neto 2023/33c4043a-11e7-4f29-9207-ea8b2e545745.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/Copa Martins Neto 2023/75ae3bf0-faed-4d09-acff-945952380a29.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/Copa Martins Neto 2023/84e6e631-d0ad-4e78-b8b0-b8de2da371f4.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/Copa Martins Neto 2023/704c562e-8ba0-4712-9c6c-19d19093fed2.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/Copa Martins Neto 2023/b8d55585-b184-45b1-8654-318aa04fbf4f.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/Copa Martins Neto 2023/c0b750dc-f8fe-4f7b-ac56-4c5182aeb58b.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/Copa Martins Neto 2023/d9380c69-51b8-4af4-9755-8432bcff0a5b.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/Copa Martins Neto 2023/dc2b6a30-dc89-43be-994b-3506d8c13293.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/Copa Martins Neto 2023/e0f66f4b-ab71-43dd-9346-41ff388488eb.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/Copa Martins Neto 2023/ec6e8827-c97c-46b0-9dd1-5f6597202c2b.jpg",
    ),


]

st.write('Copa Martins Neto 2023 - 10/12/2023 - Maior campeonato de várzea de São Paulo - Público 1500 pessoas')
carousel(items=copa_martins, wrap=True)

