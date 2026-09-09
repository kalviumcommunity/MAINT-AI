import streamlit as st
from pathlib import Path

from pages.dashboard import dashboard
from pages.new_query import new_query
from pages.results import results
from pages.history import history
from pages.sources import sources
from pages.document_viewer import document_viewer
from pages.documents import documents
from pages.feedback import feedback
from pages.settings import settings


st.set_page_config(
    page_title="MaintAI",
    page_icon="⚙",
    layout="wide",
    initial_sidebar_state="expanded"
)

css_path = Path(__file__).parent / "styles" / "main.css"
with open(css_path, "r", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Dark mode: re-declares the same CSS variables with dark values.
# Since this <style> block is injected AFTER main.css, the browser's
# cascade rules make these values win for every element that uses
# var(--page-bg), var(--card-bg), etc. — no per-page changes needed.
if st.session_state.get("dark_mode_enabled", False):
    st.markdown("""
    <style>
    :root {
        --page-bg: #10151f;
        --card-bg: #1b2230;
        --card-border: #2b3446;
        --divider: #2b3446;
        --text-heading: #eef1f6;
        --text-muted: #8a95a8;
        --text-body: #d7dde6;
        --form-card-start: #1b2230;
        --form-card-end: #1b2230;
    }
    </style>
    """, unsafe_allow_html=True)


if "page" not in st.session_state:
    st.session_state["page"] = "dashboard"

page = st.session_state["page"]

if page == "new_query":
    new_query()
elif page == "results":
    results()
elif page == "history":
    history()
elif page == "sources":
    sources()
elif page == "document_viewer":
    document_viewer()
elif page == "documents":
    documents()
elif page == "feedback":
    feedback()
elif page == "settings":
    settings()
else:
    dashboard()