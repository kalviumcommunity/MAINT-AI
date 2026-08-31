import textwrap
import streamlit as st


def render_html(html: str):
    st.markdown(textwrap.dedent(html), unsafe_allow_html=True)