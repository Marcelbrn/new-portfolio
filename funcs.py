# ===== Importação bibliotecas ===== #
import streamlit as st

# ===== Definindo função para gerar estilo css personalizado da página ===== #
def load_css(v_path_css):
    with open(v_path_css) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)