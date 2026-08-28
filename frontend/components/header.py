import streamlit as st


def render_header():

    left, right = st.columns([4, 1])

    with left:
        st.caption("MaintAI  ›  Dashboard")

    with right:
        st.write("🔔 **Vijayashree**")
        st.caption("Senior Technician")

    st.divider()