from utils.helpers import render_html


def render_header(page_title="Dashboard"):
    render_html(f"""
<div class="top-header">
    <div class="breadcrumb">
        <span>MaintAI</span>
        <span class="breadcrumb-arrow">›</span>
        <strong>{page_title}</strong>
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