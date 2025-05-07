# ===== Importação bibliotecas ===== #
import streamlit as st
from PIL import Image
from funcs import load_css

# ===== Configurando variáveis com os caminhos imagens ===== #
v_img_perfil         = "https://github.com/Marcelbrn/marcel-portfolio/raw/6721ec536e4cdd14fa4748889c45cfd9ef3a00c0/img/img_marcel.png"
v_img_linkedin       = "https://github.com/Marcelbrn/Portfolio/raw/686a9cca66a2d1c4e1ece9edcfa641d0dd328a4e/img/img_icon_linkedin.png"
v_img_github         = "https://github.com/Marcelbrn/Portfolio/raw/686a9cca66a2d1c4e1ece9edcfa641d0dd328a4e/img/img_icon_github.png"
v_img_plano_de_fundo = Image.open("img/img_plano_de_fundo.png")
v_img_txt_sobre      = Image.open("img/img_dados.png")
v_link_linkedin      = "https://www.linkedin.com/in/marcel-bruno/"
v_link_github        = "https://github.com/Marcelbrn/"

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