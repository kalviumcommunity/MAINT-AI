import streamlit as st

from components.sidebar import render_sidebar
from components.header import render_header
from utils.helpers import render_html


# Sample source metadata matching the Figma design. In the full
# integration, this would come from the backend's per-source
# citation data attached to the query response.
SAMPLE_SOURCES = [
    {
        "relevance": "high",
        "icon": "📘",
        "title": "Motor Maintenance Manual Sec 4.2",
        "equipment_tag": "Equipment M-204",
        "version": "v2.4.1 (Oct 2023)",
        "approval_status": "Approved",
        "approval_icon": "✓",
        "button_label": "👁 View Document",
        "accent": "green",
    },
    {
        "relevance": "high",
        "icon": "⚡",
        "title": "Troubleshooting Guide Ch 3",
        "equipment_tag": "Equipment M-204",
        "version": "v1.1.0 (Jan 2024)",
        "approval_status": "Approved",
        "approval_icon": "✓",
        "button_label": "👁 View Document",
        "accent": "green",
    },
    {
        "relevance": "medium",
        "icon": "🕐",
        "title": "Preventive Maintenance SOP",
        "plain_tag": "General Plant Procedures",
        "version": "v5.0.2 (Mar 2022)",
        "approval_status": "Review Pending",
        "approval_icon": "⏳",
        "button_label": "👁 View Document",
        "accent": "amber",
    },
    {
        "relevance": "critical",
        "icon": "⚠",
        "title": "Safety Procedures Manual",
        "plain_tag": "Lockout/Tagout (LOTO) Required",
        "version": "v12.0 (Jan 2024)",
        "approval_status": "Mandatory",
        "approval_icon": "⚠",
        "button_label": "⚠ Review Safety Docs",
        "accent": "red",
    },
]

RELEVANCE_LABELS = {
    "high": "HIGH RELEVANCE",
    "medium": "MEDIUM RELEVANCE",
    "critical": "CRITICAL RELEVANCE",
}


def sources():

    render_sidebar()
    render_header(crumbs=["Dashboard", "New Query", "Sources"])

    render_html("""
<div class="ai-insight-badge">✦ AI INSIGHT EVIDENCE</div>
""")

    render_html("""
<div class="nq-page-header">
    <h1>Sources Used for This Answer</h1>
    <p>Verify the recommendations against approved maintenance documentation.</p>
</div>
""")

    source_list = st.session_state.get("current_sources", SAMPLE_SOURCES)

    col1, col2 = st.columns(2, gap="medium")
    columns = [col1, col2]

    for i, source in enumerate(source_list):
        with columns[i % 2]:

            accent = source.get("accent", "green")
            relevance_label = RELEVANCE_LABELS.get(source.get("relevance", "high"), "RELEVANCE")

            tag_html = ""
            if source.get("equipment_tag"):
                tag_html = f'<span class="source-equipment-tag">{source["equipment_tag"]}</span><span class="source-tag-dot"></span>'
            elif source.get("plain_tag"):
                tag_color = "plain-tag-critical" if accent == "red" else "plain-tag"
                tag_html = f'<span class="{tag_color}">{source["plain_tag"]}</span>'

            approval_class = f"approval-{accent}"

            render_html(f"""
<div class="source-card source-card-{accent}">
    <div class="source-card-top">
        <span class="source-relevance relevance-{accent}">{source['icon']} {relevance_label}</span>
        <span class="source-menu">⋮</span>
    </div>
    <div class="source-title">{source['title']}</div>
    <div class="source-tag-row">{tag_html}</div>
    <div class="source-meta-row">
        <div class="source-meta-col">
            <div class="source-meta-label">Version</div>
            <div class="source-meta-value">{source['version']}</div>
        </div>
        <div class="source-meta-col">
            <div class="source-meta-label">Approval Status</div>
            <div class="source-meta-value {approval_class}">{source['approval_icon']} {source['approval_status']}</div>
        </div>
    </div>
</div>
""")

            btn_type = "primary" if accent == "red" else "secondary"
            if st.button(source["button_label"], key=f"src_btn_{i}", use_container_width=True):
                st.session_state["current_document"] = source["title"]
                st.session_state["doc_viewer_return_to"] = "sources"
                st.session_state["page"] = "document_viewer"
                st.rerun()

            render_html("<div class='card-gap'></div>")