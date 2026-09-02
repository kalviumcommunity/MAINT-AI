import streamlit as st

from components.sidebar import render_sidebar
from components.header import render_header
from utils.helpers import render_html
from services.api import submit_query


# Fallback sample data so this page still looks complete even if
# no real result exists yet (e.g. visited directly during dev).
SAMPLE_RESULT = {
    "equipment_id": "M-204",
    "equipment_name": "Conveyor Drive Motor",
    "question": "Why is the motor on M-204 overheating?",
    "grounded": True,
    "safety_warning": "Disconnect power and follow lockout/tagout procedure before inspection.",
    "causes": [
        {
            "icon": "💧",
            "color": "red",
            "title": "Insufficient Lubrication",
            "description": "The bearing housing may lack adequate grease, causing increased friction and thermal build-up.",
        },
        {
            "icon": "🔺",
            "color": "red",
            "title": "Overloaded Motor",
            "description": "Conveyor belt tension may be too high or jamming is occurring downstream, exceeding rated load.",
        },
        {
            "icon": "💨",
            "color": "orange",
            "title": "Blocked Ventilation",
            "description": "Cooling fins or fan shroud may be obstructed by industrial debris or dust accumulation.",
        },
    ],
    "actions": [
        {
            "text": "Check lubrication level in both front and rear bearing housings. Regrease if necessary using Polyrex EM or equivalent.",
            "source": "Source [1]: M-200 Series Maintenance Manual, Sec 4.2",
        },
        {
            "text": "Verify motor load current using a clamp meter. Compare reading against the nameplate Full Load Amps (FLA).",
            "source": "Source [2]: Electrical Troubleshooting Guide v3",
        },
        {
            "text": "Inspect external cooling fins and clean with compressed air if obstructed.",
            "source": "Source [3]: Routine Inspection Checklist",
        },
    ],
    "sources_used": 4,
}


def _render_causes(causes):
    if not causes:
        return ""
    html = '<div class="causes-grid">'
    for cause in causes:
        color_class = f"cause-icon-{cause.get('color', 'red')}"
        html += f"""
<div class="cause-item">
    <div class="cause-icon {color_class}">{cause['icon']}</div>
    <div class="cause-body">
        <div class="cause-title">{cause['title']}</div>
        <div class="cause-description">{cause['description']}</div>
    </div>
</div>
"""
    html += "</div>"
    return html


def _render_actions(actions):
    html = ""
    for i, action in enumerate(actions, start=1):
        source_html = ""
        if action.get("source"):
            source_html = f'<div class="action-source">📄 {action["source"]}</div>'
        html += f"""
<div class="action-item">
    <div class="action-number">{i}</div>
    <div class="action-body">
        <div class="action-text">{action['text']}</div>
        {source_html}
    </div>
</div>
"""
    return html


def results():

    render_sidebar()
    render_header(crumbs=["Dashboard", "New Query", "Result"])

    data = st.session_state.get("last_result", SAMPLE_RESULT)

    grounded_badge = ""
    if data.get("grounded"):
        grounded_badge = """
        <div class="grounded-badge">
            🛡 Grounded in approved maintenance documentation
        </div>
        """

    render_html(f"""
<div class="result-header-card">
    <div class="result-header-top">
        <div class="result-tags">
            <span class="equipment-tag">● {data['equipment_id']}</span>
            <span class="equipment-tag-name">{data['equipment_name']}</span>
        </div>
        {grounded_badge}
    </div>
    <h2 class="result-question">{data['question']}</h2>
</div>
""")

    render_html("<div class='card-gap'></div>")

    if data.get("safety_warning"):
        render_html(f"""
<div class="critical-warning">
    <div class="critical-warning-icon">⚠</div>
    <div>
        <div class="critical-warning-title">Safety Critical Warning</div>
        <div class="critical-warning-message">{data['safety_warning']}</div>
    </div>
</div>
""")

    render_html("<div class='card-gap'></div>")

    causes_html = _render_causes(data.get("causes", []))
    actions_html = _render_actions(data.get("actions", []))

    causes_section = ""
    if causes_html:
        causes_section = f"""
    <div class="diagnostic-section-label">POSSIBLE CAUSES</div>
    {causes_html}
"""
    elif data.get("diagnosis"):
        causes_section = f"""
    <div class="diagnostic-section-label">DIAGNOSIS</div>
    <p style="color:#35476b; font-size:12.5px; line-height:1.7; margin: 0 0 6px;">
        {data['diagnosis']}
    </p>
"""

    render_html(f"""
<div class="diagnostic-card">
    <div class="diagnostic-header">
        📋 Diagnostic Analysis
    </div>
    <div class="diagnostic-divider"></div>
    {causes_section}
    <div class="diagnostic-section-label actions-label">RECOMMENDED ACTIONS</div>
    {actions_html}
</div>
""")

    render_html("<div class='small-gap'></div>")

    # ---- Footer action bar ----
    render_html(f"""
<div class="result-footer">
    <div class="result-footer-left">
        📚 {data.get('sources_used', len(data.get('actions', [])))} approved sources used
    </div>
</div>
""")

    fb1, fb2, fb3, fb4, fb5, fb6 = st.columns([1.3, 1.3, 1, 0.6, 0.6, 1.1])

    with fb1:
        view_sources = st.button("📄 View Sources", key="res_view_sources", use_container_width=True)
    with fb2:
        regenerate = st.button("↻ Regenerate", key="res_regenerate", use_container_width=True)
    with fb3:
        copy_clicked = st.button("⧉ Copy", key="res_copy", use_container_width=True)
    with fb4:
        thumbs_up = st.button("👍", key="res_thumbs_up", use_container_width=True)
    with fb5:
        thumbs_down = st.button("👎", key="res_thumbs_down", use_container_width=True)
    with fb6:
        escalate = st.button("Escalate", key="res_escalate", use_container_width=True, type="primary")

    if view_sources:
        with st.expander("Sources used in this diagnosis", expanded=True):
            for action in data.get("actions", []):
                st.markdown(f"- {action['source']}")

    if copy_clicked:
        full_text = data["question"] + "\n\n"
        full_text += "Possible causes:\n"
        for c in data.get("causes", []):
            full_text += f"- {c['title']}: {c['description']}\n"
        full_text += "\nRecommended actions:\n"
        for i, a in enumerate(data.get("actions", []), start=1):
            full_text += f"{i}. {a['text']} ({a['source']})\n"

        with st.expander("Copy full report", expanded=True):
            st.code(full_text, language=None)

    if regenerate:
        equipment_id = data.get("equipment_id", "")
        category = st.session_state.get("nq_category", "Mechanical")
        priority = st.session_state.get("nq_priority", "Medium")
        query_text = data.get("question", "")

        with st.spinner("Regenerating response..."):
            result = submit_query(equipment_id, category, query_text, priority)

        if result["success"]:
            resp = result["data"]
            st.session_state["last_result"] = {
                **data,
                "causes": data.get("causes", []),
                "question": query_text,
            }
            st.toast("Response regenerated.")
            st.rerun()
        else:
            st.toast(f"Failed to regenerate: {result['error']}")

    if thumbs_up:
        st.toast("Thanks for the feedback! 👍")

    if thumbs_down:
        st.toast("Thanks for the feedback — we'll use this to improve. 👎")

    if escalate:
        st.toast("Escalated to a senior technician.")