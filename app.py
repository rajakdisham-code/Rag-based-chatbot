import streamlit as st

from ui.styles import load_css
from ui.sidebar import render_sidebar
from ui.home import render_home
from ui.chat import render_chat

st.set_page_config(
    page_title="PDF RAG Chatbot",
    page_icon="🤖",
    layout="wide",
)

load_css()

if "messages" not in st.session_state:

    st.session_state.messages = []

render_sidebar()

render_home()

render_chat()