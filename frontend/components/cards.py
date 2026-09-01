from utils.helpers import render_html


def render_metric_card(title, value, description, icon):
    render_html(f"""
<div class="metric-card">
    <div class="metric-top">
        <div class="metric-title">{title}</div>
        <div class="metric-icon">{icon}</div>
    </div>
    <div class="metric-value">{value}</div>
    <div class="metric-description">{description}</div>
</div>
""")