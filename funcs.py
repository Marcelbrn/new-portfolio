# ===== Importação bibliotecas ===== #
import streamlit as st
from PIL import Image
import time

# ===== Definindo função para gerar estilo css personalizado da página ===== #
def load_css(v_path_css):
    with open(v_path_css) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        

# ===== Definindo função para gerar quadro de habilidades técnicas ===== #
def technical_skills(v_habilidades):
    st.markdown("### 🛠️ Habilidades Técnicas")

    cols = st.columns(4)
    for idx, (title, items) in enumerate(v_habilidades.items()):
        with cols[idx]:
            v_lista_habilidades = "".join(f"<li>{item}</li>" for item in items)

            st.markdown(f"""
                            <div class="skill-card">
                                <h5>{title}</h5>
                                <ul>{v_lista_habilidades}</ul>
                            </div><br>
                        """, unsafe_allow_html=True)


# ===== Definindo função para gerar quadro de projetos ===== #
def projects(v_projetos):
    st.markdown("### 👨🏻‍💻 Projetos")
    cols = st.columns(3, gap="large")
    for idx, projeto in enumerate(v_projetos):
        with cols[idx % 3]:

            st.markdown(
                f"""
                    <div class="project-card">
                        <img src="{projeto['img_projeto']}" class="project-image"/>
                        <h5>{projeto['nm_projeto']}</h5>
                        <p>{projeto['desc_projeto']}</p>
                        <p><b>Stack:</b> {projeto['tec_prohjeto']}</p>
                        <div class="project-links">
                            <a href="{projeto['link_projeto']}" target="_blank">🔗GitHub</a>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
         

# ===== Definindo função para gerar quadro de certificações ===== #
def certification(v_certificacoes):
    st.markdown("### 🏅 Certificações")
    cols = st.columns(4)
    for idx, cert in enumerate(v_certificacoes):
        with cols[idx % 4]:
            st.markdown(
                f"""
                    <div class="cert-card">
                        <a href="{cert['link_cert']}" target="_blank">
                            <img class="cert-image" src="{cert['img_cert']}">
                        </a>
                        <h5>{cert['tp_cert']}</h5>
                        <h6>{cert['nm_cert']}</h6>
                    </div>
                """, unsafe_allow_html=True)                     


# ===== Definindo função para gerar quadro de contato ===== #
def contact_form():
    v_img_carta  = "https://github.com/Marcelbrn/Portfolio/raw/e2cb95bec7bb3ee4f86bad18cc6a74cfed0ebc42/img/img_carta_gpt5.png"

    st.markdown("### 📬 Entre em Contato")

    st.markdown(
        """
            <div class="contact-description">
                Fique à vontade para enviar uma mensagem. Responderei o mais breve possível!
            </div>
        """, unsafe_allow_html=True)

    # Inicializa session_state
    for campo in ["nome_input", "email_input", "mensagem_input", "limpar_campos", "mensagem_enviada"]:
        if campo not in st.session_state:
            st.session_state[campo] = "" if campo != "limpar_campos" and campo != "mensagem_enviada" else False

    # Limpa os campos se flag estiver ativada
    if st.session_state.limpar_campos:
        st.session_state.nome_input = ""
        st.session_state.email_input = ""
        st.session_state.mensagem_input = ""
        st.session_state.limpar_campos = False

    col1, col2 = st.columns([2, 2])

    with col1:
        with st.form(key="formulario_contato"):
            nome = st.text_input("", placeholder="Nome", key="nome_input")
            email = st.text_input("", placeholder="Email", key="email_input")
            mensagem = st.text_area("", placeholder="Mensagem", key="mensagem_input")
            botao = st.form_submit_button("Enviar")

            if botao:
                if not nome or not email or not mensagem:
                    st.warning("⚠️ Por favor, preencha todos os campos antes de enviar.")
                    time.sleep(3)
                    st.session_state.mensagem_enviada = False
                else:
                    # Simula envio de e-mail (ou processa backend)
                    st.session_state.limpar_campos = True
                    st.session_state.mensagem_enviada = True

                    # Mostra toast e reseta após 3s
                    if st.session_state.mensagem_enviada:
                        st.success("✅ Sua mensagem foi enviada com sucesso!")
                        time.sleep(3)
                        st.session_state.mensagem_enviada = False

    with col2:
        st.markdown(
            f"""
                <div class="contact-container">
                    <img src="{v_img_carta}" class="contact-image" alt="Contact illustration">
                </div>
            """, unsafe_allow_html=True)
