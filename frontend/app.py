import streamlit as st
from pathlib import Path

from pages.dashboard import dashboard
from pages.new_query import new_query
from pages.results import results
from pages.history import history


st.set_page_config(
    page_title="MaintAI",
    page_icon="⚙",
    layout="wide",
    initial_sidebar_state="expanded"
)

css_path = Path(__file__).parent / "styles" / "main.css"
with open(css_path, "r", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


if "page" not in st.session_state:
    st.session_state["page"] = "dashboard"

page = st.session_state["page"]

if page == "new_query":
    new_query()
elif page == "results":
    results()
elif page == "history":
    history()
else:
    dashboard()