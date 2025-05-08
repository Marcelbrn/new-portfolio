
# ===== Importação bibliotecas ===== #
import streamlit as st
from PIL import Image
from funcs import load_css

# ===== Configurando variáveis com os caminhos imagens ===== #
v_img_perfil         = "https://github.com/Marcelbrn/marcel-portfolio/raw/6721ec536e4cdd14fa4748889c45cfd9ef3a00c0/img/img_marcel.png"
v_img_linkedin       = "https://github.com/Marcelbrn/Portfolio/raw/686a9cca66a2d1c4e1ece9edcfa641d0dd328a4e/img/img_icon_linkedin.png"
v_img_github         = "https://github.com/Marcelbrn/Portfolio/raw/686a9cca66a2d1c4e1ece9edcfa641d0dd328a4e/img/img_icon_github.png"
v_img_plano_de_fundo = Image.open("img/img_plano_de_fundo.png")
v_img_txt_sobre      = Image.open("img/img_dados_cgpt.png")
v_link_linkedin      = "https://www.linkedin.com/in/marcel-bruno/"
v_link_github        = "https://github.com/Marcelbrn/"


# ===== Configurando informações de habilidades, projetos e certificações  ===== #
habilidades_tecnicas = {
    "Dev & Linguagens": ["SAS", "SQL", "Python, PySpark, Shell Script", "DBT"],
    "BD & Armazenamento": ["SQL Server, Oracle, Teradata", "MongoDB, Cassandra", "Data Warehouse", "Data Lake"],
    "DevOps & Ferramentas": ["Airflow", "Docker, Kubernetes","Terraform, CI/CD", "Streamlit, Power BI"],
    "Cloud & Processamento": ["AWS, Azure, GCP", "Databricks", "Snowflake", "BigQuery"],
}

# ===== Configurações da página como: layout da página, nome e icone na aba do navegador ===== #
st.set_page_config(page_title = "Marcel Bruno - Portfólio", page_icon = "📑", layout = "wide")

# ===== Carregando o estilo css personalizado da página ===== #
load_css("css/estilo.css")

# ===== Adiciona imagem de plano de fundo ===== #
st.image(v_img_plano_de_fundo, use_container_width=True, output_format="PNG", clamp=True)

# ===== Adiciona ícone do linkein ===== #
st.markdown(
    "<div class='icon-container linkedin-icon'>"
        "<div class='icon-circle'>"
            f"<a href='{v_link_linkedin}' target='_blank'>"
                f"<img src='{v_img_linkedin}' class='icon-image'>"
            "</a>"
        "</div>"
    "</div>", unsafe_allow_html=True
)

# ===== Adiciona foto de perfil ===== #
st.markdown(
    "<div class='profile-circle'>"
            f"<img src='{v_img_perfil}' class='profile-image'>"
    "</div>", unsafe_allow_html=True
)

# ===== Adiciona ícone do github ===== #
st.markdown(
    "<div class='icon-container github-icon'>"
        "<div class='icon-circle'>"
            f"<a href='{v_link_github}' target='_blank'>"
                f"<img src='{v_img_github}' class='icon-image'>"
            "</a>"
        "</div>"
    "</div>", unsafe_allow_html=True
)

# ===== Adiciona ícone do github ===== #
st.markdown("""
    <div style='text-align: center;'>
        <h2>Marcel Bruno</h2> 
    </div> """, unsafe_allow_html=True
)

# ===== Configurando o container ===== #
with st.container(border=0):
    col1, col2 = st.columns([4,1])

    # Adicionando texto 'sobre'
    with col1:
        st.markdown("""### 👋🏻 Olá, seja bem-vindo(a)""", unsafe_allow_html=True)
        st.markdown(
            """
                <div style="padding-right: 1rem; padding-left: 1rem;">
                    Sou Marcel Bruno, profissional apaixonado por Engenharia de Dados, com aproximadamente 8 anos de experiência no desenvolvimento de pipelines de dados, especializado em programação SAS. Atualmente, estou ampliando meus conhecimentos em engenharia de dados, explorando novas linguagens, ferramentas e tecnologias em nuvem para fortalecer ainda mais minha atuação no universo de dados. Além da carreira, sou pai do Heitor e também dos meus pets Thor, Pandora e Tico, gosto de estudar sobre plantas medicinais e cultivo uma vida espiritualizada, buscando equilíbrio e aprendizado contínuo em todas as áreas da vida.
                </div>
            """, unsafe_allow_html=True)

    with col2:
        #st.image(v_img_txt_sobre, width=200)
        st.image(v_img_txt_sobre, width=255)
