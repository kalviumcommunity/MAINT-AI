from utils.helpers import render_html


def render_header():
    render_html("""
<div class="top-header">
    <div class="breadcrumb">
        <span>MaintAI</span>
        <span class="breadcrumb-arrow">›</span>
        <strong>Dashboard</strong>
    </div>
    <div class="user-profile">
        <div class="notification-icon">🔔</div>
        <div class="avatar">V</div>
        <div class="user-details">
            <div class="user-name">Vijayashree</div>
            <div class="user-role">Senior Technician</div>
        </div>
    </div>
</div>
""")