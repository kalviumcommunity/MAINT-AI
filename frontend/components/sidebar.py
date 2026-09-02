import streamlit as st
from utils.helpers import render_html


def render_sidebar():

    with st.sidebar:

        render_html("""
<div class="sidebar-brand">
    <div class="brand-icon">⚙</div>
    <div>
        <div class="brand-name">MaintAI</div>
        <div class="brand-subtitle">ENTERPRISE AI</div>
    </div>
</div>
<div class="sidebar-divider"></div>
""")

        current_page = st.session_state.get("page", "dashboard")

        # The Results page is reached via New Query, so it should
        # keep "New Query" highlighted in the sidebar rather than
        # having no active item at all.
        highlight_page = "new_query" if current_page == "results" else current_page

        nav_items = [
            ("dashboard", "▦", "Dashboard"),
            ("new_query", "◈", "New Query"),
            ("history", "↻", "History"),
            ("documents", "▤", "Documents"),
        ]

        for page_key, icon, label in nav_items:
            is_active = "active-nav" if highlight_page == page_key else ""
            render_html(f'<div class="nav-wrapper {is_active}">')
            if st.button(f"{icon}  {label}", key=f"sidebar_{page_key}", use_container_width=True):
                st.session_state["page"] = page_key
                st.rerun()
            render_html("</div>")

        render_html("""
<div class="sidebar-section-title system-title">SYSTEM</div>
""")

        system_items = [
            ("feedback", "◉", "Feedback"),
            ("settings", "⚙", "Settings"),
        ]

        for page_key, icon, label in system_items:
            is_active = "active-nav" if highlight_page == page_key else ""
            render_html(f'<div class="nav-wrapper {is_active}">')
            if st.button(f"{icon}  {label}", key=f"sidebar_{page_key}", use_container_width=True):
                st.session_state["page"] = page_key
                st.rerun()
            render_html("</div>")

        render_html("""
<div class="sidebar-spacer"></div>
<div class="system-status">
    <span class="status-dot"></span>
    System Online
</div>
""")