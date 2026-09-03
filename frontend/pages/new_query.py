import streamlit as st
from datetime import datetime

from components.sidebar import render_sidebar
from components.header import render_header
from utils.helpers import render_html
from services.api import submit_query


EQUIPMENT_DATA = [
    {"code": "M-204", "name": "Industrial Motor Assembly", "category": "Mechanical",
     "status": "Running with Warning", "status_type": "warning"},
    {"code": "PLC-402", "name": "Control Logic Unit", "category": "Software / PLC",
     "status": "Online", "status_type": "ok"},
    {"code": "P-118", "name": "Hydraulic Pump", "category": "Hydraulic / Pneumatic",
     "status": "Offline", "status_type": "error"},
    {"code": "C-330", "name": "Air Compressor", "category": "Mechanical",
     "status": "Running", "status_type": "ok"},
]

SUGGESTED_QUERIES = [
    "Why is the motor overheating?",
    "What does error code E17 mean?",
    "Show recent maintenance logs",
]


def _asset_lookup(code):
    for item in EQUIPMENT_DATA:
        if item["code"] == code:
            return item
    return EQUIPMENT_DATA[0]


def new_query():

    render_sidebar()
    render_header(crumbs=["Dashboard", "New Query"])

    render_html("""
<div class="nq-page-header">
    <h1>Troubleshoot Issue</h1>
    <p>Provide details about the equipment and the problem to get AI-assisted diagnostics.</p>
</div>
""")

    if "nq_form_version" not in st.session_state:
        st.session_state["nq_form_version"] = 0

    desc_key = f"nq_description_{st.session_state['nq_form_version']}"

    render_html("<div class='query-form-card'>")

    render_html("<div class='field-label'>Target Asset</div>")

    asset_options = [f"{item['code']} — {item['name']}" for item in EQUIPMENT_DATA]
    selected_option = st.selectbox(
        "Target Asset",
        asset_options,
        key="nq_asset",
        label_visibility="collapsed"
    )
    selected_code = selected_option.split(" — ")[0]
    asset = _asset_lookup(selected_code)

    status_class = f"asset-status-{asset['status_type']}"

    render_html(f"""
<div class="asset-preview">
    <div class="asset-icon">⚙</div>
    <div class="asset-info">
        <div class="asset-name">{asset['name']}</div>
        <div class="asset-tags">
            <span class="asset-code-tag">{asset['code']}</span>
            <span class="asset-status-tag {status_class}">● {asset['status']}</span>
        </div>
    </div>
</div>
""")

    render_html("<div class='form-gap'></div>")
    render_html("<div class='field-label'>Describe the Problem <span class='required-mark'>*</span></div>")

    description = st.text_area(
        "Describe the Problem",
        placeholder="e.g. The motor is overheating after approximately 30 minutes of operation.",
        height=110,
        key=desc_key,
        label_visibility="collapsed"
    )

    render_html("<div class='form-gap'></div>")

    ec_col, sym_col = st.columns(2)

    with ec_col:
        render_html("<div class='field-label'>Error Code <span class='optional-mark'>(Optional)</span></div>")
        error_code = st.text_input(
            "Error Code",
            placeholder="E17",
            key="nq_error_code",
            label_visibility="collapsed"
        )

    with sym_col:
        render_html("<div class='field-label'>Symptoms <span class='optional-mark'>(Optional)</span></div>")
        symptoms = st.text_input(
            "Symptoms",
            placeholder="e.g. Unusual noise, vibration",
            key="nq_symptoms",
            label_visibility="collapsed"
        )

    render_html("<div class='form-gap'></div>")

    submitted = st.button(
        "✦  Ask MaintAI",
        key="nq_submit",
        use_container_width=True,
        type="primary"
    )

    render_html("</div>")  # close query-form-card

    render_html("<div class='card-gap'></div>")

    render_html("<div class='field-label'>Suggested Queries</div>")

    sug_cols = st.columns(len(SUGGESTED_QUERIES))
    for i, (col, suggestion) in enumerate(zip(sug_cols, SUGGESTED_QUERIES)):
        with col:
            if st.button(f"🔍 {suggestion}", key=f"nq_suggestion_{i}", use_container_width=True):
                st.session_state["nq_form_version"] += 1
                new_key = f"nq_description_{st.session_state['nq_form_version']}"
                st.session_state[new_key] = suggestion
                st.rerun()

    render_html("<div class='card-gap'></div>")

    render_html("""
<div class="safety-alert">
    <div class="safety-title">⚠ Safety Notice</div>
    <div class="safety-message">
        MaintAI provides recommendations based on approved maintenance documentation.
        Always follow applicable safety procedures and Lockout/Tagout (LOTO) protocols
        before interacting with physical hardware.
    </div>
</div>
""")

    if submitted:
        if not description.strip():
            render_html("""
<div class="form-warning">
    ⚠ Please describe the problem before submitting.
</div>
""")
        else:
            full_query_text = description.strip()
            if error_code.strip():
                full_query_text += f"\nError code: {error_code.strip()}"
            if symptoms.strip():
                full_query_text += f"\nSymptoms: {symptoms.strip()}"

            with st.spinner("Analyzing your issue with AI..."):
                result = submit_query(
                    equipment_id=f"{asset['code']} · {asset['name']}",
                    category=asset["category"],
                    query_text=full_query_text,
                    priority="Medium",
                )

            if not result["success"]:
                render_html(f"""
<div class="form-warning">
    ⚠ {result['error']}
</div>
""")
            else:
                data = result["data"]

                result_payload = {
                    "equipment_id": asset["code"],
                    "equipment_name": asset["name"],
                    "question": description,
                    "grounded": bool(data.get("sources")),
                    "safety_warning": data.get("safety_warning"),
                    "causes": data.get("causes", []),
                    "actions": [
                        {"text": step, "source": ""} for step in data.get("steps", [])
                    ],
                    "diagnosis": data.get("answer", ""),
                    "sources_used": len(data.get("sources", [])),
                }

                if "query_history" not in st.session_state:
                    st.session_state["query_history"] = []

                st.session_state["query_history"].insert(0, {
                    "equipment_code": asset["code"],
                    "equipment_name": asset["name"],
                    "category": asset["category"],
                    "text": description,
                    "priority": "Medium",
                    "status": "Resolved",
                    "timestamp": datetime.now().strftime("%b %d, %Y · %I:%M %p"),
                    "result": result_payload,
                })

                st.session_state["last_result"] = result_payload
                st.session_state["page"] = "results"
                st.rerun()