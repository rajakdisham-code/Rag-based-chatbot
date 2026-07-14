import streamlit as st


def render_home():
    st.title("🤖 Chat with your PDFs")

    st.caption(
        "Ask questions from your uploaded PDF documents."
    )

    if len(st.session_state.messages) == 0:

        st.info(
            """
👋 Welcome!

Ask anything from your PDFs.

Example Questions:

• What is Object Oriented Programming?

• Explain inheritance.

• Summarize Chapter 2.

• What is counselling cutoff?
"""
        )