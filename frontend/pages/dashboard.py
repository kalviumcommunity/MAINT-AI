import streamlit as st

from components.sidebar import render_sidebar
from components.header import render_header
from components.cards import render_metric_card
from components.safety_alert import render_safety_alert
from utils.helpers import render_html


def dashboard():

    render_sidebar()
    render_header()

    render_html("""
<div class="hero-section">
    <div class="hero-content">
        <div class="eyebrow">TECHNICIAN DASHBOARD</div>
        <h1>Good morning, Vijayashree</h1>
        <p>Monitor maintenance activity, troubleshoot equipment,
        and access your technical knowledge base.</p>
    </div>
</div>
""")

    action_col1, action_col2 = st.columns([5, 1])
    with action_col2:
        if st.button("＋ Start New Query", key="dashboard_new_query", use_container_width=True):
            st.session_state["page"] = "new_query"
            st.rerun()

    render_html("<div class='small-gap'></div>")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        render_metric_card("TOTAL QUERIES", "128", "All troubleshooting sessions", "▦")
    with c2:
        render_metric_card("RESOLVED QUERIES", "112", "87.5% resolution rate", "✓")
    with c3:
        render_metric_card("KNOWLEDGE BASE", "486", "Approved technical documents", "▤")
    with c4:
        render_metric_card("AVERAGE FEEDBACK", "4.6 / 5", "Based on technician feedback", "★")

    render_html("<div class='section-gap'></div>")

    left, right = st.columns([2.05, 1], gap="large")

    with left:

        render_html("""
<div class="section-header">
    <div>
        <h2>Recent Queries</h2>
        <p>Your latest troubleshooting activity</p>
    </div>
    <div class="query-count">3 recent</div>
</div>
""")

        queries = [
            ("Why is the motor overheating?", "M-204", "Resolved", "resolved", "✓"),
            ("How to replace bearing in M-204?", "M-204", "In Progress", "progress", "↻"),
            ("What does error code E17 mean on PLC-402?", "PLC-402", "Escalated", "escalated", "!")
        ]

        for query, equipment, status, status_class, icon in queries:
            render_html(f"""
<div class="query-card">
    <div class="query-left">
        <div class="query-icon {status_class}">{icon}</div>
        <div class="query-information">
            <div class="query-title">{query}</div>
            <div class="query-meta">Equipment ID · {equipment}</div>
        </div>
    </div>
    <div class="query-right">
        <div class="equipment-badge">{equipment}</div>
        <div class="status-badge {status_class}">
            <span class="status-dot-small"></span>
            {status}
        </div>
    </div>
</div>
""")

        render_html("<div class='button-space'></div>")

        if st.button("View All Queries  →", key="dashboard_view_history"):
            st.session_state["page"] = "history"
            st.rerun()

    with right:

        render_safety_alert()
        render_html("<div class='card-gap'></div>")

        render_html("""
<div class="equipment-section">
    <div class="equipment-section-header">
        <h2>Recently Viewed</h2>
        <p>Equipment you recently accessed</p>
    </div>
    <div class="equipment-item">
        <div class="equipment-icon">⚙</div>
        <div class="equipment-information">
            <strong>Main Conveyor Motor</strong>
            <span>M-204 · Conveyor System</span>
        </div>
        <div class="equipment-arrow">›</div>
    </div>
    <div class="equipment-item">
        <div class="equipment-icon">▣</div>
        <div class="equipment-information">
            <strong>Control Logic Unit</strong>
            <span>PLC-402 · Control System</span>
        </div>
        <div class="equipment-arrow">›</div>
    </div>
</div>
""")

    render_html("""
<div class="dashboard-footer">
    <strong>MaintAI</strong>
    <span>•</span>
    AI-powered maintenance assistance
    <span>•</span>
    Technician Workspace
</div>
""")