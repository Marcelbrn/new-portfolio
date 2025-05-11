
# ===== Importação bibliotecas ===== #
import streamlit as st
from PIL import Image
from funcs import load_css, technical_skills, projects, certification, contact_form

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

projetos = [
    {
        "nm_projeto": "Portfólio",
        "desc_projeto": "Projeto criado para apresentar minhas experiências, certificações e habilidades técnicas de forma interativa por meio de projetos com o objetivo de destacar meu perfil profissional de maneira clara, organizada e atrativa.",
        "link_projeto": "https://github.com/Marcelbrn/new-portfolio/tree/main",
        "img_projeto":  "https://github.com/Marcelbrn/Portfolio/raw/abb39375456090922cf800a4d819b812f56239be/img/img_portfolio_gpt2.png",
        "tec_prohjeto": "Python, Streamlit, CSS"
    },
    {
        "nm_projeto": "Portfólio",
        "desc_projeto": "Implementação de página web para apresentação de portfólio profissional, destacando projetos, habilidades e experiências.",
        "link_projeto": "https://github.com/Marcelbrn/new-portfolio/tree/main",
        "img_projeto":  "https://github.com/Marcelbrn/Portfolio/raw/322893482f15ac1d2237667e0a568d1abe5d9797/img/img_portfolio_gpt5.png",
        "tec_prohjeto": "Python, Streamlit, CSS"
    },
    {
        "nm_projeto": "Portfólio",
        "desc_projeto": "Implementação de página web para apresentação de portfólio profissional, destacando projetos, habilidades e experiências fjsdljlfasdd jlfasdjlk  jfsdjlkjfsadl jflsdjjfksdjhk bkjerwiurkjlksd jfsdlj.",
        "link_projeto": "https://github.com/Marcelbrn/new-portfolio/tree/main",
        "img_projeto":  "https://github.com/Marcelbrn/Portfolio/raw/abb39375456090922cf800a4d819b812f56239be/img/img_portfolio_gpt2.png",
        "tec_prohjeto": "Python, Streamlit, CSS"
    }
]

certificacoes = [
    {
        "img_cert": "https://github.com/Marcelbrn/portfolio/raw/7d7f1e5dbff9ed1d6370e929c5ae8e4440233a58/img/img_certificacao_microsoft.png",
        "tp_cert": "Microsoft Certified",
        "nm_cert": "Azure Fundamentals",
        "link_cert": ""
    },
    {
        "img_cert": "https://github.com/Marcelbrn/portfolio/raw/8d7506d39ae93358dd1ed90503e2bdb0cae09f3b/img/img_certificacao_sas.png",
        "tp_cert": "SAS Certified Professional",
        "nm_cert": "Advanced Programming Using SAS 9.4",
        "link_cert": "https://www.credly.com/badges/3e324c11-c28b-46aa-be33-0e780f9a4fcd/linked_in_profile"
    },
    {
        "img_cert": "https://github.com/Marcelbrn/portfolio/raw/8d7506d39ae93358dd1ed90503e2bdb0cae09f3b/img/img_certificacao_sas.png",
        "tp_cert": "SAS Certified Specialist",
        "nm_cert": "Base Programming Using SAS 9.4",
        "link_cert": "https://www.credly.com/badges/603b630f-203c-43a8-a568-6384de851889/linked_in"
    },
    {
        "img_cert": "https://github.com/Marcelbrn/portfolio/raw/8d7506d39ae93358dd1ed90503e2bdb0cae09f3b/img/img_certificacao_sas.png",
        "tp_cert": "SAS Certified",
        "nm_cert": "Base Programmer for SAS 9",
        "link_cert": "https://www.youracclaim.com/badges/b2d53d81-f4d4-4f24-af0a-322c2b673020/linked_in_profile"
    }
]

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
        st.image(v_img_txt_sobre, width=255)

    # Adicionando quadro de habilidades
    technical_skills(habilidades_tecnicas)

    # Adicionando quadro de projetos
    projects(projetos)

    # Adicionando quadro de certificações
    certification(certificacoes)

    # Contatos
    contact_form()

    # Rodapé
    st.markdown(
        """
            <hr style='margin-top: 2rem; margin-bottom: 1rem;'>
            <p style='text-align: center; font-size: 0.9rem; color: gray;'>
                © 2025 Marcel Bruno — Desenvolvido com Python & Streamlit
            </p>
        """, unsafe_allow_html=True)