import streamlit as st


def render_safety_alert():

    st.warning(
        "⚠ **Important Safety Alert**\n\n"
        "Lockout/Tagout is required before maintenance "
        "work in Zone B today."
    )