import streamlit as st


def render_metric_card(title, value, description, icon):

    with st.container(border=True):

        top_left, top_right = st.columns([4, 1])

        with top_left:
            st.caption(title)

        with top_right:
            st.write(icon)

        st.markdown(
            f"<div class='metric-value'>{value}</div>",
            unsafe_allow_html=True
        )

        st.caption(description)