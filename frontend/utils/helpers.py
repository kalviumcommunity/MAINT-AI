import streamlit as st


def render_html(html: str):
    """Render raw HTML safely in Streamlit.

    Strips leading whitespace from EVERY line individually (rather than
    textwrap.dedent's common-prefix approach). This matters because HTML
    fragments are often built in nested Python blocks (if/for) and then
    interpolated into another f-string — dedent alone can't fix that,
    since the "outer" string's flush-left lines make dedent think there's
    no common indentation to strip, leaving the nested lines indented
    by 4+ spaces, which Markdown then renders as a literal code block.

    Per-line stripping sidesteps this entirely: no line can ever end up
    indented enough to trigger that behavior, regardless of how deeply
    nested or how the string was assembled in Python.
    """
    cleaned = "\n".join(line.lstrip() for line in html.split("\n"))
    st.markdown(cleaned, unsafe_allow_html=True)