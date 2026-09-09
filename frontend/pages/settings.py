import streamlit as st

from components.sidebar import render_sidebar
from components.header import render_header
from utils.helpers import render_html


def settings():

    render_sidebar()
    render_header(crumbs=["Dashboard", "Settings"])

    render_html("""
<div class="nq-page-header">
    <h1>Settings</h1>
    <p>Manage your account and application preferences.</p>
</div>
""")

    # ---- Profile ----
    render_html("""
<div class="settings-card">
    <div class="settings-card-header">
        <div class="settings-avatar">V</div>
        <div>
            <div class="settings-card-title">Profile</div>
            <div class="settings-card-subtitle">Your personal and account information</div>
        </div>
    </div>
</div>
""")

    render_html("<div class='query-form-card'>")

    name_col, role_col = st.columns(2)
    with name_col:
        render_html("<div class='field-label'>Full Name</div>")
        st.text_input(
            "Full Name",
            value=st.session_state.get("settings_name", "Vijayashree"),
            key="settings_name",
            label_visibility="collapsed"
        )
    with role_col:
        render_html("<div class='field-label'>Role</div>")
        st.text_input(
            "Role",
            value=st.session_state.get("settings_role", "Senior Technician"),
            key="settings_role",
            label_visibility="collapsed"
        )

    render_html("<div class='form-gap'></div>")
    render_html("<div class='field-label'>Email</div>")
    st.text_input(
        "Email",
        value=st.session_state.get("settings_email", "vijayashree@maintai.com"),
        key="settings_email",
        label_visibility="collapsed"
    )

    render_html("<div class='form-gap'></div>")

    if st.button("Save Profile", key="settings_save_profile", type="primary"):
        st.toast("Profile saved.")

    render_html("</div>")  # close query-form-card

    render_html("<div class='section-gap'></div>")

    # ---- Notification Preferences ----
    render_html("""
<div class="section-header">
    <div>
        <h2>Notification Preferences</h2>
        <p>Choose what you want to be notified about</p>
    </div>
</div>
""")

    render_html("<div class='query-form-card'>")

    notif_options = [
        ("notif_email", "Email Notifications", "Get a summary of query activity by email"),
        ("notif_push", "Push Notifications", "Real-time alerts in your browser"),
        ("notif_safety", "Safety Alerts", "Critical safety notices for your assigned equipment"),
        ("notif_weekly", "Weekly Summary", "A digest of resolved and pending queries every week"),
    ]

    for key, title, desc in notif_options:
        toggle_col, text_col = st.columns([0.15, 4])
        with toggle_col:
            st.toggle(title, value=st.session_state.get(key, True), key=key, label_visibility="collapsed")
        with text_col:
            render_html(f"""
<div class="settings-toggle-label">
    <div class="settings-toggle-title">{title}</div>
    <div class="settings-toggle-desc">{desc}</div>
</div>
""")

    render_html("</div>")

    render_html("<div class='section-gap'></div>")

    # ---- Application Preferences ----
    render_html("""
<div class="section-header">
    <div>
        <h2>Application Preferences</h2>
        <p>Defaults used across MaintAI</p>
    </div>
</div>
""")

    render_html("<div class='query-form-card'>")

    pref_col1, pref_col2 = st.columns(2)

    with pref_col1:
        render_html("<div class='field-label'>Default Query Priority</div>")
        st.selectbox(
            "Default Priority",
            ["Low", "Medium", "High", "Critical"],
            index=["Low", "Medium", "High", "Critical"].index(
                st.session_state.get("settings_default_priority", "Medium")
            ),
            key="settings_default_priority",
            label_visibility="collapsed"
        )

    with pref_col2:
        render_html("<div class='field-label'>Language</div>")
        st.selectbox(
            "Language",
            ["English"],
            key="settings_language",
            label_visibility="collapsed",
            disabled=True
        )

    render_html("<div class='form-gap'></div>")
    render_html("<div class='field-label'>Theme</div>")

    theme_choice = st.radio(
        "Theme",
        ["Light", "Dark"],
        index=1 if st.session_state.get("dark_mode_enabled", False) else 0,
        horizontal=True,
        key="settings_theme",
        label_visibility="collapsed"
    )

    new_dark_mode = (theme_choice == "Dark")
    if new_dark_mode != st.session_state.get("dark_mode_enabled", False):
        st.session_state["dark_mode_enabled"] = new_dark_mode
        st.rerun()

    render_html("<div class='form-gap'></div>")

    if st.button("Save Preferences", key="settings_save_prefs", type="primary"):
        st.toast("Preferences saved.")

    render_html("</div>")  # close query-form-card

    render_html("<div class='section-gap'></div>")

    # ---- Session data / danger zone ----
    render_html("""
<div class="section-header">
    <div>
        <h2>Session Data</h2>
        <p>Data stored locally for this session only</p>
    </div>
</div>
""")

    render_html("""
<div class="settings-danger-card">
    <div class="settings-danger-title">⚠ Clear Session Data</div>
    <div class="settings-danger-message">
        This clears your query history and feedback log from this browser
        session. This cannot be undone, and does not affect any data
        already saved on the server.
    </div>
</div>
""")

    danger_col, _ = st.columns([1, 3])
    with danger_col:
        if st.button("Clear Session Data", key="settings_clear_session"):
            for key in ["query_history", "feedback_list", "last_result"]:
                st.session_state.pop(key, None)
            st.toast("Session data cleared.")
            st.rerun()