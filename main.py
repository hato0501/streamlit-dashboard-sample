import streamlit as st
from streamlit_option_menu import option_menu


with open("static/style.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

with st.sidebar:
    selected = option_menu(
        "Main Menu",
        ["Home", "JEPXスポット価格"],
        icons=["house", "gear"],
        menu_icon="cast",
        default_index=1,
    )
    selected
