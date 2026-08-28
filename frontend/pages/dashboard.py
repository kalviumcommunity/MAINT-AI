import streamlit as st

from components.sidebar import render_sidebar
from components.header import render_header
from components.cards import render_metric_card
from components.safety_alert import render_safety_alert


def dashboard():

    # Sidebar
    render_sidebar()

    # Header
    render_header()

    # Page title
    st.caption("TECHNICIAN DASHBOARD")

    title_col, button_col = st.columns([3, 1])

    with title_col:
        st.title("Good morning, Vijayashree")
        st.write(
            "Here's what's happening with your maintenance activity."
        )

    with button_col:
        if st.button(
            "＋ Start New Query",
            key="dashboard_new_query",
            use_container_width=True
        ):
            st.session_state["page"] = "new_query"
            st.rerun()

    st.write("")

    # Cards
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        render_metric_card(
            "TOTAL QUERIES",
            "128",
            "All troubleshooting sessions",
            "▦"
        )

    with c2:
        render_metric_card(
            "RESOLVED QUERIES",
            "112",
            "87.5% resolution rate",
            "✓"
        )

    with c3:
        render_metric_card(
            "KNOWLEDGE BASE",
            "486",
            "Approved documents",
            "▤"
        )

    with c4:
        render_metric_card(
            "AVERAGE FEEDBACK",
            "4.6 / 5",
            "Technician feedback",
            "★"
        )

    st.write("")

    # Main content
    left, right = st.columns([2.1, 1])

    # Recent queries
    with left:

        st.subheader("Recent Queries")
        st.caption("Your latest troubleshooting activity")

        queries = [
            ("Why is the motor overheating?", "M-204", "🟢 Resolved"),
            ("How to replace bearing in M-204?", "M-204", "🔵 In Progress"),
            (
                "What does error code E17 mean on PLC-402?",
                "PLC-402",
                "🔴 Escalated"
            ),
        ]

        for query, equipment, status in queries:

            with st.container(border=True):

                q1, q2, q3 = st.columns([3, 1, 1])

                with q1:
                    st.write(f"**{query}**")

                with q2:
                    st.caption(equipment)

                with q3:
                    st.write(status)

        if st.button(
            "View All Queries →",
            key="dashboard_view_history"
        ):
            st.session_state["page"] = "history"
            st.rerun()

    # Right side
    with right:

        render_safety_alert()

        st.write("")

        st.subheader("Recently Viewed Equipment")
        st.caption("Equipment you recently accessed")

        with st.container(border=True):

            st.write("⚙️ **Main Conveyor Motor**")
            st.caption("M-204")

            st.divider()

            st.write("▣ **Control Logic Unit**")
            st.caption("PLC-402")

    st.write("")

    st.caption("MaintAI • AI-powered maintenance assistance")