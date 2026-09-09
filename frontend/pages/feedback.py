import streamlit as st
from datetime import datetime

from components.sidebar import render_sidebar
from components.header import render_header
from utils.helpers import render_html


FEEDBACK_TYPES = [
    "AI Response Quality",
    "General Feedback",
    "Bug Report",
    "Feature Request",
]

RATING_OPTIONS = ["😞 Poor", "😐 Fair", "🙂 Good", "😊 Great", "😍 Excellent"]


def feedback():

    render_sidebar()
    render_header(crumbs=["Dashboard", "Feedback"])

    render_html("""
<div class="nq-page-header">
    <h1>Feedback</h1>
    <p>Help us improve MaintAI by sharing your experience.</p>
</div>
""")

    if "fb_form_version" not in st.session_state:
        st.session_state["fb_form_version"] = 0

    msg_key = f"fb_message_{st.session_state['fb_form_version']}"

    render_html("<div class='query-form-card'>")

    render_html("<div class='field-label'>Feedback Type</div>")
    feedback_type = st.selectbox(
        "Feedback Type",
        FEEDBACK_TYPES,
        key="fb_type",
        label_visibility="collapsed"
    )

    render_html("<div class='form-gap'></div>")

    render_html("<div class='field-label'>Related Query <span class='optional-mark'>(Optional)</span></div>")
    history_list = st.session_state.get("query_history", [])
    query_options = ["Not related to a specific query"] + [
        item["text"][:60] + ("..." if len(item["text"]) > 60 else "") for item in history_list
    ]
    related_query = st.selectbox(
        "Related Query",
        query_options,
        key="fb_related_query",
        label_visibility="collapsed"
    )

    render_html("<div class='form-gap'></div>")

    render_html("<div class='field-label'>How would you rate it?</div>")
    rating = st.radio(
        "Rating",
        RATING_OPTIONS,
        index=3,
        horizontal=True,
        key="fb_rating",
        label_visibility="collapsed"
    )

    render_html("<div class='form-gap'></div>")

    render_html("<div class='field-label'>Tell us more <span class='required-mark'>*</span></div>")
    message = st.text_area(
        "Message",
        placeholder="What went well? What could be improved?",
        height=120,
        key=msg_key,
        label_visibility="collapsed"
    )

    render_html("<div class='form-gap'></div>")

    submitted = st.button(
        "Submit Feedback",
        key="fb_submit",
        use_container_width=True,
        type="primary"
    )

    render_html("</div>")  # close query-form-card

    if submitted:
        if not message.strip():
            render_html("""
<div class="form-warning">
    ⚠ Please share a few details before submitting.
</div>
""")
        else:
            if "feedback_list" not in st.session_state:
                st.session_state["feedback_list"] = []

            st.session_state["feedback_list"].insert(0, {
                "type": feedback_type,
                "related_query": related_query,
                "rating": rating,
                "message": message.strip(),
                "timestamp": datetime.now().strftime("%b %d, %Y · %I:%M %p"),
            })

            st.session_state["fb_form_version"] += 1
            st.toast("Thank you for your feedback!")
            st.rerun()

    render_html("<div class='section-gap'></div>")

    # ---- Past feedback log ----
    render_html("""
<div class="section-header">
    <div>
        <h2>Your Feedback History</h2>
        <p>Feedback you've submitted in this session</p>
    </div>
</div>
""")

    feedback_list = st.session_state.get("feedback_list", [])

    if not feedback_list:
        render_html("""
<div class="history-empty-state">
    <div class="history-empty-icon">💬</div>
    <div class="history-empty-title">No feedback submitted yet</div>
    <div class="history-empty-message">
        Your submitted feedback will appear here for reference.
    </div>
</div>
""")
        return

    for item in feedback_list:
        render_html(f"""
<div class="feedback-card">
    <div class="feedback-card-top">
        <span class="feedback-type-tag">{item['type']}</span>
        <span class="feedback-rating">{item['rating']}</span>
    </div>
    <div class="feedback-message">{item['message']}</div>
    <div class="feedback-meta">
        {item['related_query']} &nbsp;•&nbsp; {item['timestamp']}
    </div>
</div>
""")