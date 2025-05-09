# ===== Importação bibliotecas ===== #
import streamlit as st

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