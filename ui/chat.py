import streamlit as st

from core.rag import RAGPipeline


@st.cache_resource
def load_rag():

    return RAGPipeline()


rag = load_rag()


def render_chat():

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

    prompt = st.chat_input(
        "Ask anything..."
    )

    if not prompt:
        return

    st.session_state.messages.append(

        {

            "role": "user",

            "content": prompt

        }

    )

    with st.chat_message("user"):

        st.markdown(prompt)

    with st.chat_message("assistant"):

        try:
            with st.spinner("Thinking..."):

                answer = rag.ask(prompt)

        except Exception:

            answer = (
                "⚠️ Gemini is currently busy.\n\n"
                "Please wait a few seconds and try again."
            )

        st.markdown(answer)

    st.session_state.messages.append(

        {

            "role": "assistant",

            "content": answer

        }

    )