# ===== Importação bibliotecas ===== #
import streamlit as st
from PIL import Image

# ===== Definindo função para gerar estilo css personalizado da página ===== #
def load_css(v_path_css):
    with open(v_path_css, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        

# ===== Definindo função para gerar quadro de habilidades técnicas ===== #
def technical_skills(v_habilidades):
    st.markdown("### 🛠️ Habilidades Técnicas")

    cols = st.columns(4, gap="small")
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
                    </div><br>
                """, unsafe_allow_html=True)
         

# ===== Definindo função para gerar quadro de certificações ===== #
def certification(v_certificacoes):
    st.markdown("### 🏅 Certificações")
    cols = st.columns(4, gap="small")
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
                    </div><br>
                """, unsafe_allow_html=True)                     


# ===== Definindo função para gerar quadro de contato ===== #
def contact_form():

    # Texto
    st.markdown("### 📬 Entre em Contato")
    st.markdown(
        """
            <div class="contact-description">Fique à vontade para enviar uma mensagem. Responderei o mais breve possível!</div>
        """, unsafe_allow_html=True
    )

    col1, col2 = st.columns([2, 2])
    
    # Formulário
    with col1:
        st.markdown(
            """
            <div class="form-card">
                <form action="https://formsubmit.co/marcelbrn@gmail.com" method="POST">
                    <input type="hidden" name="_next" value="https://marcelbruno.streamlit.app/?success=true">
                    <input type="hidden" name="_captcha" value="false">
                    <input type="hidden" name="_template" value="table">
                    <input class="form-input" type="text" name="name" placeholder="Nome" required>
                    <input class="form-input" type="email" name="email" placeholder="Email" required>
                    <textarea class="form-textarea" name="message" placeholder="Mensagem" rows="4" required></textarea>
                    <button type="submit" class="form-button">Enviar</button>
                </form>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Confirmação de envio do email
        query_params = st.query_params

        if "success" in query_params:
            st.success("✅ Sua mensagem foi enviada com sucesso!")

    # Imagem
    v_carta = "https://github.com/Marcelbrn/Portfolio/raw/4ceace1b3b5cf082ca52dba6ed49351f14cb33f1/img/img_carta_gpt5.png"

    with col2:
        st.markdown(
            f"""
                <div class="contact-container">
                    <img src="{v_carta}" class="contact-image" alt="Contact illustration">
                </div>
            """, unsafe_allow_html=True)
