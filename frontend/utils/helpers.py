import textwrap
import streamlit as st


def render_html(html: str):
    """Render raw HTML safely in Streamlit, avoiding markdown's
    4-space-indent-as-code-block trap."""
    st.markdown(textwrap.dedent(html), unsafe_allow_html=True)