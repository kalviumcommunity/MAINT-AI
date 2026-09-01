import streamlit as st

from components.sidebar import render_sidebar
from components.header import render_header
from utils.helpers import render_html


def new_query():

    render_sidebar()
    render_header("New Query")

    render_html("""
<div class="hero-section">
    <div class="hero-content">
        <div class="eyebrow">TROUBLESHOOTING ASSISTANT</div>
        <h1>Start a New Query</h1>
        <p>Describe the issue you're facing and get instant
        AI-powered troubleshooting guidance.</p>
    </div>
</div>
""")

    render_html("<div class='small-gap'></div>")

    # Counter used to reset the text area by giving it a fresh
    # widget key — Streamlit does not allow directly overwriting
    # a widget's session_state value after it has been instantiated.
    if "nq_form_version" not in st.session_state:
        st.session_state["nq_form_version"] = 0

    text_key = f"nq_query_text_{st.session_state['nq_form_version']}"

    left, right = st.columns([2, 1], gap="large")

    with left:

        render_html("""
<div class="form-card">
    <div class="form-card-title">Query Details</div>
""")

        equipment_id = st.selectbox(
            "Equipment ID",
            [
                "M-204 · Main Conveyor Motor",
                "PLC-402 · Control Logic Unit",
                "P-118 · Hydraulic Pump",
                "C-330 · Air Compressor",
                "Other / Not listed"
            ],
            key="nq_equipment"
        )

        category = st.selectbox(
            "Issue Category",
            [
                "Mechanical",
                "Electrical",
                "Software / PLC",
                "Hydraulic / Pneumatic",
                "Safety",
                "Other"
            ],
            key="nq_category"
        )

        query_text = st.text_area(
            "Describe the issue",
            placeholder="e.g. The motor is overheating after 20 minutes of continuous operation and making a grinding noise...",
            height=160,
            key=text_key
        )

        priority = st.radio(
            "Priority",
            ["Low", "Medium", "High", "Critical"],
            index=1,
            horizontal=True,
            key="nq_priority"
        )

        render_html("<div class='form-gap'></div>")

        submit_col, clear_col = st.columns([1, 1])

        with submit_col:
            submitted = st.button(
                "Submit Query",
                key="nq_submit",
                use_container_width=True,
                type="primary"
            )

        with clear_col:
            if st.button("Clear Form", key="nq_clear", use_container_width=True):
                st.session_state["nq_form_version"] += 1
                st.rerun()

        render_html("</div>")

        if submitted:
            if not query_text.strip():
                render_html("""
<div class="form-warning">
    ⚠ Please describe the issue before submitting.
</div>
""")
            else:
                if "query_history" not in st.session_state:
                    st.session_state["query_history"] = []

                st.session_state["query_history"].insert(0, {
                    "equipment": equipment_id,
                    "category": category,
                    "text": query_text,
                    "priority": priority,
                })

                render_html("<div class='card-gap'></div>")

                render_html(f"""
<div class="result-card">
    <div class="result-card-header">
        <div class="result-icon">✓</div>
        <div>
            <div class="result-title">Query Submitted Successfully</div>
            <div class="result-subtitle">Our AI is analyzing your issue</div>
        </div>
    </div>
    <div class="result-body">
        <div class="result-row">
            <span class="result-label">Equipment</span>
            <span class="result-value">{equipment_id}</span>
        </div>
        <div class="result-row">
            <span class="result-label">Category</span>
            <span class="result-value">{category}</span>
        </div>
        <div class="result-row">
            <span class="result-label">Priority</span>
            <span class="result-value">{priority}</span>
        </div>
    </div>
</div>
""")

                render_html("""
<div class="ai-response-card">
    <div class="ai-response-title">🤖 Suggested Next Steps</div>
    <ul class="ai-response-list">
        <li>Check the equipment's maintenance log for similar past incidents.</li>
        <li>Verify recent operating conditions (load, temperature, duty cycle).</li>
        <li>Inspect for visible wear, loose connections, or abnormal noise/vibration.</li>
        <li>If unresolved, escalate to a senior technician with these details attached.</li>
    </ul>
    <div class="ai-response-note">
        This is a preliminary suggestion. Full AI-powered diagnostics will appear here
        once the knowledge base integration is connected.
    </div>
</div>
""")

    with right:

        render_html("""
<div class="tips-card">
    <div class="tips-title">💡 Tips for a Better Response</div>
    <ul class="tips-list">
        <li>Be specific about symptoms (sounds, smells, error codes).</li>
        <li>Mention when the issue started and how often it occurs.</li>
        <li>Include any troubleshooting steps you've already tried.</li>
        <li>Attach the correct equipment ID for accurate matching.</li>
    </ul>
</div>
""")

        render_html("<div class='card-gap'></div>")

        history = st.session_state.get("query_history", [])

        if history:
            items_html = ""
            for item in history[:5]:
                items_html += f"""
<div class="mini-history-item">
    <div class="mini-history-text">{item['text'][:60]}{'...' if len(item['text']) > 60 else ''}</div>
    <div class="mini-history-meta">{item['equipment'].split(' · ')[0]} · {item['priority']}</div>
</div>
"""
            render_html(f"""
<div class="tips-card">
    <div class="tips-title">🕘 This Session</div>
    {items_html}
</div>
""")