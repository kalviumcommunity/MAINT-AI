from utils.helpers import render_html


def render_header(page_title="Dashboard", crumbs=None):
    """Renders the top header bar.

    - Simple usage: render_header("Dashboard") -> "MaintAI › Dashboard"
    - Multi-level: render_header(crumbs=["Dashboard", "New Query", "Result"])
      -> "Dashboard › New Query › Result" with the last item bold/active
      and middle items styled as links.
    """

    if crumbs is None:
        crumbs = ["MaintAI", page_title]

    parts = []
    last_index = len(crumbs) - 1

    for i, label in enumerate(crumbs):
        if i == last_index:
            parts.append(f'<strong class="crumb-current">{label}</strong>')
        elif i == 0:
            parts.append(f'<span class="crumb-root">{label}</span>')
        else:
            parts.append(f'<span class="crumb-link">{label}</span>')

        if i != last_index:
            parts.append('<span class="breadcrumb-arrow">›</span>')

    breadcrumb_html = "".join(parts)

    render_html(f"""
<div class="top-header">
    <div class="breadcrumb">
        {breadcrumb_html}
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