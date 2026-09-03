import streamlit as st

from components.sidebar import render_sidebar
from components.header import render_header
from utils.helpers import render_html


STATUS_CLASS_MAP = {
    "Resolved": "resolved",
    "In Progress": "progress",
    "Escalated": "escalated",
}

STATUS_ICON_MAP = {
    "Resolved": "✓",
    "In Progress": "↻",
    "Escalated": "!",
}


def history():

    render_sidebar()
    render_header(crumbs=["Dashboard", "History"])

    render_html("""
<div class="nq-page-header">
    <h1>Query History</h1>
    <p>Browse and search your past troubleshooting queries.</p>
</div>
""")

    all_history = st.session_state.get("query_history", [])

    # ---- Filters ----
    render_html("<div class='history-filters-card'>")

    f_search, f_category, f_status = st.columns([2, 1, 1])

    with f_search:
        search_term = st.text_input(
            "Search",
            placeholder="🔍 Search by keyword...",
            key="hist_search",
            label_visibility="collapsed"
        )

    categories = ["All Categories"] + sorted({item["category"] for item in all_history})
    with f_category:
        category_filter = st.selectbox(
            "Category",
            categories,
            key="hist_category",
            label_visibility="collapsed"
        )

    statuses = ["All Statuses", "Resolved", "In Progress", "Escalated"]
    with f_status:
        status_filter = st.selectbox(
            "Status",
            statuses,
            key="hist_status",
            label_visibility="collapsed"
        )

    render_html("</div>")
    render_html("<div class='card-gap'></div>")

    # ---- Apply filters ----
    filtered = all_history

    if search_term.strip():
        term = search_term.strip().lower()
        filtered = [
            item for item in filtered
            if term in item["text"].lower()
            or term in item["equipment_code"].lower()
            or term in item["equipment_name"].lower()
        ]

    if category_filter != "All Categories":
        filtered = [item for item in filtered if item["category"] == category_filter]

    if status_filter != "All Statuses":
        filtered = [item for item in filtered if item["status"] == status_filter]

    # ---- Result count ----
    render_html(f"""
<div class="history-count">{len(filtered)} of {len(all_history)} quer{'y' if len(all_history) == 1 else 'ies'} shown</div>
""")

    render_html("<div class='small-gap'></div>")

    # ---- Empty states ----
    if not all_history:
        render_html("""
<div class="history-empty-state">
    <div class="history-empty-icon">🕘</div>
    <div class="history-empty-title">No queries yet</div>
    <div class="history-empty-message">
        Once you submit a troubleshooting query, it will show up here for you to review anytime.
    </div>
</div>
""")
        if st.button("＋ Start a New Query", key="hist_start_new"):
            st.session_state["page"] = "new_query"
            st.rerun()
        return

    if not filtered:
        render_html("""
<div class="history-empty-state">
    <div class="history-empty-icon">🔍</div>
    <div class="history-empty-title">No matching queries</div>
    <div class="history-empty-message">
        Try adjusting your search or filters.
    </div>
</div>
""")
        return

    # ---- Query list ----
    for idx, item in enumerate(filtered):
        status_class = STATUS_CLASS_MAP.get(item["status"], "progress")
        status_icon = STATUS_ICON_MAP.get(item["status"], "•")

        render_html(f"""
<div class="query-card">
    <div class="query-left">
        <div class="query-icon {status_class}">{status_icon}</div>
        <div class="query-information">
            <div class="query-title">{item['text'][:90]}{'...' if len(item['text']) > 90 else ''}</div>
            <div class="query-meta">Equipment ID · {item['equipment_code']} &nbsp;•&nbsp; {item['timestamp']}</div>
        </div>
    </div>
    <div class="query-right">
        <div class="equipment-badge">{item['equipment_code']}</div>
        <div class="status-badge {status_class}">
            <span class="status-dot-small"></span>
            {item['status']}
        </div>
    </div>
</div>
""")

        if item.get("result"):
            if st.button("View Result →", key=f"hist_view_{idx}"):
                st.session_state["last_result"] = item["result"]
                st.session_state["page"] = "results"
                st.rerun()