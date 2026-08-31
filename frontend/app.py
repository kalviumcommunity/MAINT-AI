import streamlit as st
from pathlib import Path

from pages.dashboard import dashboard


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

# For today, only the dashboard is wired up.
# Sidebar buttons for other pages will update session_state,
# but won't navigate anywhere yet until those pages are fixed.
dashboard()