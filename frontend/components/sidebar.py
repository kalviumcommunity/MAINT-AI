import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.title("⚙ MaintAI")

        st.caption("AI-POWERED MAINTENANCE")

        st.divider()

        st.caption("WORKSPACE")

        if st.button(
            "▦  Dashboard",
            key="nav_dashboard",
            use_container_width=True
        ):
            st.session_state["page"] = "dashboard"
            st.rerun()

        if st.button(
            "＋  New Query",
            key="nav_new_query",
            use_container_width=True
        ):
            st.session_state["page"] = "new_query"
            st.rerun()

        if st.button(
            "↻  History",
            key="nav_history",
            use_container_width=True
        ):
            st.session_state["page"] = "history"
            st.rerun()

        if st.button(
            "▤  Documents",
            key="nav_documents",
            use_container_width=True
        ):
            st.session_state["page"] = "documents"
            st.rerun()

        st.write("")

        st.caption("SYSTEM")

        if st.button(
            "◉  Feedback",
            key="nav_feedback",
            use_container_width=True
        ):
            st.session_state["page"] = "feedback"
            st.rerun()

        if st.button(
            "⚙  Settings",
            key="nav_settings",
            use_container_width=True
        ):
            st.session_state["page"] = "settings"
            st.rerun()

        st.divider()

        st.success("System Online")