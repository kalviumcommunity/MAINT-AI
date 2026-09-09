import streamlit as st

from components.sidebar import render_sidebar
from components.header import render_header
from utils.helpers import render_html


SAMPLE_DOCUMENTS = [
    {
        "icon": "📘",
        "title": "Motor Maintenance Manual Sec 4.2",
        "category": "Mechanical",
        "equipment_tag": "M-204",
        "version": "v2.4.1",
        "updated": "Oct 2023",
        "approval_status": "Approved",
        "approval_icon": "✓",
        "accent": "green",
    },
    {
        "icon": "⚡",
        "title": "Troubleshooting Guide Ch 3",
        "category": "Electrical",
        "equipment_tag": "M-204",
        "version": "v1.1.0",
        "updated": "Jan 2024",
        "approval_status": "Approved",
        "approval_icon": "✓",
        "accent": "green",
    },
    {
        "icon": "🕐",
        "title": "Preventive Maintenance SOP",
        "category": "General",
        "equipment_tag": None,
        "version": "v5.0.2",
        "updated": "Mar 2022",
        "approval_status": "Review Pending",
        "approval_icon": "⏳",
        "accent": "amber",
    },
    {
        "icon": "⚠",
        "title": "Safety Procedures Manual",
        "category": "Safety",
        "equipment_tag": None,
        "version": "v12.0",
        "updated": "Jan 2024",
        "approval_status": "Mandatory",
        "approval_icon": "⚠",
        "accent": "red",
    },
    {
        "icon": "🔧",
        "title": "Hydraulic Pump Service Manual",
        "category": "Hydraulic / Pneumatic",
        "equipment_tag": "P-118",
        "version": "v3.2.0",
        "updated": "Jun 2023",
        "approval_status": "Approved",
        "approval_icon": "✓",
        "accent": "green",
    },
    {
        "icon": "💻",
        "title": "PLC-402 Control Logic Reference",
        "category": "Software / PLC",
        "equipment_tag": "PLC-402",
        "version": "v2.0.1",
        "updated": "Feb 2024",
        "approval_status": "Approved",
        "approval_icon": "✓",
        "accent": "green",
    },
    {
        "icon": "📋",
        "title": "Routine Inspection Checklist",
        "category": "General",
        "equipment_tag": None,
        "version": "v1.4.0",
        "updated": "Sep 2023",
        "approval_status": "Approved",
        "approval_icon": "✓",
        "accent": "green",
    },
    {
        "icon": "🌬",
        "title": "Air Compressor Maintenance Guide",
        "category": "Mechanical",
        "equipment_tag": "C-330",
        "version": "v1.0.0",
        "updated": "Nov 2022",
        "approval_status": "Review Pending",
        "approval_icon": "⏳",
        "accent": "amber",
    },
]


def documents():

    render_sidebar()
    render_header(crumbs=["Dashboard", "Documents"])

    render_html("""
<div class="nq-page-header">
    <h1>Knowledge Base Documents</h1>
    <p>Browse and search approved maintenance documentation.</p>
</div>
""")

    # ---- Filters ----
    render_html("<div class='history-filters-card'>")

    f_search, f_category, f_status = st.columns([2, 1, 1])

    with f_search:
        search_term = st.text_input(
            "Search",
            placeholder="🔍 Search documents...",
            key="doc_search",
            label_visibility="collapsed"
        )

    categories = ["All Categories"] + sorted({d["category"] for d in SAMPLE_DOCUMENTS})
    with f_category:
        category_filter = st.selectbox(
            "Category",
            categories,
            key="doc_category",
            label_visibility="collapsed"
        )

    statuses = ["All Statuses", "Approved", "Review Pending", "Mandatory"]
    with f_status:
        status_filter = st.selectbox(
            "Status",
            statuses,
            key="doc_status",
            label_visibility="collapsed"
        )

    render_html("</div>")
    render_html("<div class='card-gap'></div>")

    # ---- Apply filters ----
    filtered = SAMPLE_DOCUMENTS

    if search_term.strip():
        term = search_term.strip().lower()
        filtered = [
            d for d in filtered
            if term in d["title"].lower()
            or term in d["category"].lower()
            or (d["equipment_tag"] and term in d["equipment_tag"].lower())
        ]

    if category_filter != "All Categories":
        filtered = [d for d in filtered if d["category"] == category_filter]

    if status_filter != "All Statuses":
        filtered = [d for d in filtered if d["approval_status"] == status_filter]

    render_html(f"""
<div class="history-count">{len(filtered)} of {len(SAMPLE_DOCUMENTS)} documents shown</div>
""")

    render_html("<div class='small-gap'></div>")

    if not filtered:
        render_html("""
<div class="history-empty-state">
    <div class="history-empty-icon">🔍</div>
    <div class="history-empty-title">No matching documents</div>
    <div class="history-empty-message">
        Try adjusting your search or filters.
    </div>
</div>
""")
        return

    # ---- Document grid ----
    col1, col2 = st.columns(2, gap="medium")
    columns = [col1, col2]

    for i, doc in enumerate(filtered):
        with columns[i % 2]:

            tag_html = ""
            if doc.get("equipment_tag"):
                tag_html = f'<span class="source-equipment-tag">Equipment {doc["equipment_tag"]}</span>'
            else:
                tag_html = f'<span class="plain-tag">{doc["category"]}</span>'

            approval_class = f"approval-{doc['accent']}"

            render_html(f"""
<div class="source-card source-card-{doc['accent']}">
    <div class="source-card-top">
        <span class="source-relevance relevance-{doc['accent']}">{doc['icon']} {doc['category'].upper()}</span>
        <span class="source-menu">⋮</span>
    </div>
    <div class="source-title">{doc['title']}</div>
    <div class="source-tag-row">{tag_html}</div>
    <div class="source-meta-row">
        <div class="source-meta-col">
            <div class="source-meta-label">Version</div>
            <div class="source-meta-value">{doc['version']} ({doc['updated']})</div>
        </div>
        <div class="source-meta-col">
            <div class="source-meta-label">Approval Status</div>
            <div class="source-meta-value {approval_class}">{doc['approval_icon']} {doc['approval_status']}</div>
        </div>
    </div>
</div>
""")

            if st.button("👁 View Document", key=f"doc_view_{i}", use_container_width=True):
                st.session_state["current_document"] = doc["title"]
                st.session_state["doc_viewer_return_to"] = "documents"
                st.session_state["page"] = "document_viewer"
                st.rerun()

            render_html("<div class='card-gap'></div>")