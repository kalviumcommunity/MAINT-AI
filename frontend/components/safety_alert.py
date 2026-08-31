from utils.helpers import render_html


def render_safety_alert():
    render_html("""
<div class="safety-alert">
    <div class="safety-title">⚠ Important Safety Alert</div>
    <div class="safety-message">
        Lockout/Tagout is required before maintenance work in Zone B today.
    </div>
    <div class="safety-action">Review Safety Procedure →</div>
</div>
""")