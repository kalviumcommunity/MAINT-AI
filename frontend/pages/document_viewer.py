import streamlit as st

from components.sidebar import render_sidebar
from components.header import render_header
from utils.helpers import render_html


def document_viewer():

    render_sidebar()

    doc_title = st.session_state.get("current_document", "Motor Maintenance Manual v4.2")
    return_to = st.session_state.get("doc_viewer_return_to", "sources")
    back_label = "← Back to Sources" if return_to == "sources" else "← Back to Documents"

    render_header(crumbs=["Dashboard", "New Query", "Sources", "Document"] if return_to == "sources" else ["Dashboard", "Documents", "Document"])

    top_col, _ = st.columns([1, 5])
    with top_col:
        if st.button(back_label, key="doc_back"):
            st.session_state["page"] = return_to
            st.rerun()

    render_html(f"""
<div class="doc-viewer-header">
    <div class="doc-viewer-icon">📘</div>
    <div>
        <div class="doc-viewer-title">{doc_title}</div>
        <div class="doc-viewer-meta">Asset ID: MTR-992-A &nbsp;•&nbsp; Last updated: Oct 12, 2023</div>
    </div>
</div>
""")

    render_html("<div class='card-gap'></div>")

    rail_col, main_col = st.columns([1, 3.2], gap="medium")

    with rail_col:
        render_html("""
<div class="doc-thumb-rail">
    <div class="doc-thumb-rail-title">Pages <span class="doc-thumb-count">142 total</span></div>
""")
        for i in range(1, 6):
            active = "active" if i == 1 else ""
            render_html(f"""
<div class="doc-thumbnail {active}">
    <div class="doc-thumbnail-lines">
        <div></div><div></div><div></div>
    </div>
    <div class="doc-thumbnail-number">{i}</div>
</div>
""")
        render_html("</div>")

    with main_col:
        render_html("""
<div class="doc-viewer-main">
    <div class="doc-viewer-placeholder-icon">📄</div>
    <div class="doc-viewer-placeholder-title">Document Preview</div>
    <div class="doc-viewer-placeholder-text">
        Full PDF rendering will appear here once connected to the
        document storage backend. This page currently shows the
        structural layout only.
    </div>
</div>
""")