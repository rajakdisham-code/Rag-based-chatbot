import streamlit as st


def load_css():

    st.markdown(
        """
<style>

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

.block-container{
padding-top:2rem;
padding-bottom:6rem;
max-width:1100px;
}

</style>
""",
        unsafe_allow_html=True,
    )