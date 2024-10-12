import streamlit as st

st.set_page_config(page_title="Contato", layout="wide")

# Título da página
st.title("História do Jiu-Jitsu")
st.write('---')

col1, col2, col3 = st.columns([3,3,3])
with col2:
    # Inserir a imagem logo abaixo do separador
    st.image("assets/favpng_black-belt-judo-dan-brazilian-jiu-jitsu.png", width=300)

st.write('---')

colT0, colT1, colT2, colT3 = st.columns([1, 5, 2, 1])
with colT1:
    st.write('Segundo alguns historiadores o Jiu-Jitsu ou “arte suave”, '
             'nasceu na Índia e era praticado por monges budistas. '
             'Preocupados com a auto defesa, os monges desenvolveram uma técnica '
             'baseada nos princípios do equilíbrio, do sistema de articulação do corpo '
             'e das alavancas, evitando o uso da força e de armas.')

    st.write('Com a expansão do budismo o Jiu-Jitsu percorreu o Sudeste asiático, '
             'a China e, finalmente, chegou ao Japão, onde se desenvolveu e popularizou-se.')

    st.write('A partir do final do século XIX, alguns mestres de Jiu-Jitsu migraram do Japão '
             'para outros Continentes, vivendo do ensino da arte marcial e das lutas que realizavam.')
with colT2:
    # Inserir a imagem logo abaixo do separador
    st.image("assets/jiu-jitsu-simbolo.webp", width=250)

st.write("")
colT0_2, colT1_2, colT2_2, colT3_2 = st.columns([1, 2, 5, 1])
with colT1_2:
    # Inserir a imagem logo abaixo do separador
    st.image("assets/Maeda_Mituyo.jpg", caption="Mitsuyo Maeda", width=200)

with colT2_2:
    st.write('Mitsuyo Maeda, conhecido como Conde Koma, foi um deles. Depois de viajar com sua trupe '
             'lutando em vários países da Europa e das Américas, chegou ao Brasil em 1915 e se '
             'fixou em Belém do Pará, no ano seguinte, onde conheceu Gastão Gracie. Pai de oito filhos, '
             'cinco homens e três mulheres, Gastão tornou-se um entusiasta do Jiu-Jitsu e levou o mais velho, '
             'Carlos, para aprender a luta com o japonês. Franzino por natureza, aos 15 anos, '
             'Carlos Gracie encontrou no Jiu-Jitsu um meio de realização pessoal. Aos 19, se transferiu para '
             'o Rio de Janeiro com a família e adotou a profissão de lutador e professor dessa arte marcial.')

    st.write('Viajou para Belo Horizonte e depois para São Paulo, ministrando aulas e vencendo adversários '
             'bem mais fortes fisicamente. Em 1925, voltou ao Rio de Janeiro e abriu a primeira Academia '
             'Gracie de Jiu-Jitsu.')

st.write("")
colT0_3, colT1_3, colT2_3, colT3_3 = st.columns([1, 5, 2, 1])
with colT1_3:
    st.write('Convidou seus irmãos Oswaldo e Gastão para assessorá-lo e assumiu a criação dos meninos menores, '
             'George com 14 anos, e Hélio com 12.')

    st.write('Desde então, Carlos passou a transmitir seus conhecimentos aos irmãos, adequando e aperfeiçoando a'
             ' técnica à compleição física franzina característica de sua família. Também lhes transmitiu sua '
             'filosofia de vida e conceitos de alimentação natural, sendo um pioneiro na criação de uma dieta '
             'especial para atletas, a Dieta Gracie, transformando o Jiu-Jitsu em sinônimo de saúde.')

with colT2_3:
    # Inserir a imagem logo abaixo do separador
    st.image("assets/gastao-gracie.jpg", caption="Gastão Gracie", width=270)


st.write("")
colC1, colC2, colC3 = st.columns([1, 7, 1])
with colC2:
    st.write("Convidou seus irmãos Oswaldo e Gastão para assessorá-lo e assumiu a criação dos meninos menores, George com 14 anos, e Hélio com 12.")
    st.write("Desde então, Carlos passou a transmitir seus conhecimentos aos irmãos, adequando e aperfeiçoando a técnica à compleição física franzina característica de sua família. Também lhes transmitiu sua filosofia de vida e conceitos de alimentação natural, sendo um pioneiro na criação de uma dieta especial para atletas, a Dieta Gracie, transformando o Jiu-Jitsu em sinônimo de saúde.")
    st.write("De posse de uma eficiente técnica de defesa pessoal, Carlos Gracie viu no Jiu-Jitsu um meio para se tornar um homem mais tolerante, respeitoso e autoconfiante. Imbuído de provar a superioridade do Jiu-Jitsu e formar uma tradição familiar, Carlos Gracie lançou desafios aos grandes lutadores da época e passou a gerenciar a carreira dos irmãos.")
    st.write("Enfrentando adversários 20, 30 quilos mais pesados, os Gracie logo adquiriram fama e notoriedade nacional. Atraídos pelo novo mercado que se abriu em torno do Jiu-Jitsu, muitos japoneses vieram para o Rio de Janeiro, porém, nenhum deles formou uma escola tão sólida quanto a da Academia Gracie, pois o Jiu-Jitsu que praticavam privilegiava as quedas e o dos Gracie, o aprimoramento da luta no chão e os golpes de finalização.")
    st.write("Ao modificar as regras internacionais do Jiu-Jitsu japonês nas lutas que ele e os irmãos realizavam, Carlos Gracie iniciou o primeiro caso de mudança de nacionalidade de uma luta, ou esporte, na história esportiva mundial.")
    st.write("Anos depois, a arte marcial japonesa passou a ser denominada de Jiu-Jitsu brasileiro, sendo exportada para o mundo todo, inclusive para o Japão.")

st.write("")
colT0_4, colT1_4, colT2_4, colT3_4 = st.columns([1, 2, 5, 1])
with colT1_4:
    # Inserir a imagem logo abaixo do separador
    st.image("assets/historia-jj.jpg", width=220)

with colT2_4:
    st.write('O Jiu-Jitsu é a arte marcial mais antiga, perfeita, completa e eficiente de Defesa Pessoal. Sua origem apesar de contraditória é atribuída a China depois Índia, Japão e Brasil, onde se desenvolveu, aprimorou e tornou-se o centro mundial desta preciosa arte.')
    st.write("O Jiu-Jitsu desportivo é a parte competitiva, onde os atletas exibirão suas habilidades técnicas, físicas e psicológicas com o objetivo de alcançar a vitória sobre seus adversários.")

st.write("")
colC1_0, colC2_1, colC3_2 = st.columns([1, 7, 1])
with colC2_1:
    st.write("Os golpes válidos são aqueles que procuram neutralizar, imobilizar, estrangular, pressionar, torcer articulações, como também lançar seu adversário ao solo através de quedas enquanto os golpes não válidos, considerados desleais, como morder, puxar cabelo, enfiar os dedos nos olhos, atingir os órgãos genitais, torcer dedos ou qualquer outro processo tendente a traumatizar com o uso das mãos, cotovelos, cabeça, joelhos e pés.")
    st.write("As competições são o marco do esporte e é o momento mais importante para os atletas, técnicos – (professores) e para todos aqueles que estão envolvidos direta ou indiretamente, não cabendo por tanto, a vitória a qualquer custo, ao contrário, o fair play deve ser o principal norteador. O comportamento ético é o que dará ao esporte credibilidade e segurança, fatores indispensáveis ao nosso esporte, pois, por isso só, já conquistamos o espaço na sociedade, em seus aspectos de eficiência e de eficácia, tornando-o o esporte espetáculo.")
    st.write("Assim sendo, para se almejar a participar do maior espetáculo do mundo, que é as Olimpíadas, devemos estar imbuídos deste objetivo, tornando o Jiu-Jitsu desportivo a nossa meta.")
    st.write("O regulamento é a carta magna do esporte, nesta consta os direitos e deveres, de todos aqueles envolvidos, como atletas, técnicos (professores), dirigentes, e até mesmo o público assistente. Pois teremos a responsabilidade de cumprir e fazer cumprir este regulamento, pois, só assim, poderemos conquistar os nossos objetivos.")

