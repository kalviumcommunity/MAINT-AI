import streamlit as st
from pages.dashboard import dashboard

st.set_page_config(
    page_title="MaintAI",
    page_icon="⚙️",
    layout="wide"
)

dashboard()