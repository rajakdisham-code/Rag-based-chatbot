import streamlit as st

from core.config import GENERATION_MODEL
from core.config import EMBEDDING_MODEL


def render_sidebar():

    with st.sidebar:

        st.title("🤖 PDF Assistant")

        st.caption("Version 1")

        st.divider()

        st.write("### LLM")

        st.success(GENERATION_MODEL)

        st.write("### Embedding")

        st.success(EMBEDDING_MODEL)

        st.divider()

        if st.button(
            "🗑 Clear Chat",
            use_container_width=True
        ):

            st.session_state.messages = []

            st.rerun()