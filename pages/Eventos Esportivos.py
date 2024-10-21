import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_carousel import carousel

st.set_page_config(page_title="Eventos Esportivos", layout="wide")

# Título da página
st.title("Confira nossos eventos")
st.write("---")


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

st.header('AMISTOSO DE VOLEI CLUBE GUAPIRA')
st.subheader('Realizado em 15 de Novembro de 2023')
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

st.write('---')
st.header('COPA LIGA ZONA NORTE')
st.subheader('Realizada no Ginásio CDC Curtiball em 03 de Fevereiro de 2024 com um público de 1200 pessoas')
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
st.write('---')

st.header('COPA 1º DE MAIO - DR CLAUDIO XARÁ')
st.subheader('Realizada em 1° de Maio de 2024')
st.write('Coordenação técnica e fornecimento de estrutura, material esportivo, alimentação, hidratação e premiação')
carousel(items=copa_martins, wrap=True)


jogos_lgbt = [
    dict(
        title="",
        text="",
        img="assets/jogos LGBT/1d0fbc6e-1202-480a-8ac2-1420ba9548e7.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/jogos LGBT/03f3d34d-7b7a-4dbf-9e44-2655233ee28c.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/jogos LGBT/5e4892d1-c329-4eee-a8f2-dab3c2000554.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/jogos LGBT/6ea81152-1c14-4a70-bbc9-c4169614193c.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/jogos LGBT/6f2557c9-dd8c-4cf0-899c-37b7bb1de0eb.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/jogos LGBT/9b1f6b8b-a3f2-4dd2-9a34-20313efe87d3.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/jogos LGBT/26c411d4-57e9-48b9-a19f-ba30a3261a20.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/jogos LGBT/36ce12ff-3112-4554-bc9b-08b79b779cdf.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/jogos LGBT/42e7e3bd-c829-4c4f-8c4f-a0fea0d92fea.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/jogos LGBT/50a85d35-ffbb-4930-8812-3b94d4bf72cd.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/jogos LGBT/50ba5c44-1332-48af-bc87-6e5ef200c089.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/jogos LGBT/71af6f8b-0013-416b-a56c-2b80dcc76b34.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/jogos LGBT/123ee455-9cec-4dfd-bc75-e65ac0bd902d.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/jogos LGBT/865c7540-b380-4789-89fb-043c4a92e9a6.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/jogos LGBT/884bdc7d-2705-4b86-b7cf-afeba912544a.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/jogos LGBT/13419a2e-e10e-4504-aa87-af50b5ceb4d9.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/jogos LGBT/872661e6-56cb-409a-b168-fc4f9a2b876b.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/jogos LGBT/947287e6-6204-4bb8-bbde-edae377e49df.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/jogos LGBT/a43f63a1-d136-4e7d-a46e-5671f1093612.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/jogos LGBT/bb14645b-0df7-40f7-8db9-141ad7f7b033.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/jogos LGBT/ca503709-cbb2-48fd-89ca-e931ccbc6b0b.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/jogos LGBT/d0f48ba1-9560-41ee-b608-a2ea9771dd37.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/jogos LGBT/d5f941d4-1ceb-4bce-9b3a-e4008636bbe4.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/jogos LGBT/f939ec58-c230-4a67-815a-1ae69d23e9f4.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/jogos LGBT/f17258f8-dfd5-4d88-9ed8-458758146423.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/jogos LGBT/f77910cf-0d71-4ee5-ae75-4964735fecdf.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/jogos LGBT/f3344748-b003-4dc4-ac70-b88d9186d937.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/jogos LGBT/fe1e1fd6-fc3d-4c4e-b2a8-635305b7099c.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/jogos LGBT/ff273552-c3ec-45a5-b0b4-198be6cb64e2.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/jogos LGBT/b9e98ca9-474a-4120-9db3-5304b37d7cd3.jpg",
    ),

]
st.write('---')

st.header('1ª EDIÇÃO DOS JOGOS LGBT')
st.subheader('Realizada em Novembro de 2021')
st.write('Coordenação do evento, distribuição de premiação, alimentação e hidratação de staff e atletas')
carousel(items=jogos_lgbt, wrap=True)


copa_atlas = [
    dict(
        title="",
        text="",
        img="assets/Copa Atlas/63233d9c-2549-4544-83a1-0b9f19602423.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/Copa Atlas/717888c2-0af0-41f8-94bb-0f01c236b9c5.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/Copa Atlas/a1d8df11-1c3c-4ee1-a066-33ca881d96fd.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/Copa Atlas/a772de83-8fc8-41fe-81b4-d52bca96cff1.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/Copa Atlas/be7d2600-9908-467d-a468-469c43502b74.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/Copa Atlas/c7ebb3ae-3409-4708-b1a7-57cc40f296f8.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/Copa Atlas/c111095e-1dd5-4848-870e-8fc5e1dd66b1.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/Copa Atlas/c3915408-78a5-4ec3-a5fb-9c99ec115781.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/Copa Atlas/cc8052b4-9d1e-499c-a0d7-f566ac8a33fd.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/Copa Atlas/d3ee52f8-e2c8-4839-a812-bdbd911ceac9.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/Copa Atlas/ea74fc8e-612f-47d4-ab52-6e53ef3eb0cf.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/Copa Atlas/f967f6d5-dba1-4bea-bc3c-7bd5c90a13b9.jpg",
    ),
]

st.write('---')

st.header('- 2023 - COPA ATLAS')
st.subheader('PROCESSO: 6019.2023/0002826-0')
st.write('Termo de Colaboração n°277/SEME/2023')
carousel(items=copa_atlas, wrap=True)


copa_atlas2 = [
    dict(
        title="",
        text="",
        img="assets/Copa Atlas 2/0c8d8e4a-e6f7-42d8-8368-42eeb3a05f3e.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/Copa Atlas 2/1db8b9a9-5f0d-461c-b9ad-0f9672db2375.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/Copa Atlas 2/5a9735de-0790-4057-9040-f17336fe3c80.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/Copa Atlas 2/7a620f9e-6738-4fea-a026-ad7d7e7faa9b.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/Copa Atlas 2/7ce56b7f-57f1-4856-885d-aace6146544b.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/Copa Atlas 2/7d6cc025-f1c3-4c98-a05a-93384565fc9d.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/Copa Atlas 2/8aee0646-d431-4b2b-a140-17f702659105.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/Copa Atlas 2/37bdc44e-af5e-4db8-aef4-2d11c8fa97f1.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/Copa Atlas 2/73d8742f-f9e4-4c0f-961e-dfecde5ab2d2.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/Copa Atlas 2/87a3fa1c-6f5b-4651-bd16-622d2a1a52a2.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/Copa Atlas 2/405b38dd-973b-430e-b9d5-d761686aa26b.jpg",
    ),
    dict(
        title="",
        text="",
        img="assets/Copa Atlas 2/912ac829-48ea-4c99-830d-13c399375a89.jpg",
    ),
]

st.write('---')

st.header('- 2024 - COPA ATLAS 2ª EDIÇÃO')
st.subheader('PROCESSO: 6019.2024/0001349-4')
st.write('Termo de Fomento nº 118/SEME/2024')
carousel(items=copa_atlas2, wrap=True)
