import streamlit as st
from PIL import Image

# title and about me section

st.title("Yusuf Abdur-Rasheed")

st.subheader("About Me")
st.info("Hi! I am Yusuf, A student studying at Solihull School passionate about" 
        "programming based in Solihull, UK. 📍")


st.markdown("[GitHub](https://www.github.com/abduyus)")

st.subheader("Tech Stack: ")
st.markdown(
    """
    <style>
        .st-b7 {
            padding: 1px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

col1, col2, col3, col4, col5 = st.columns(5)

# Display an image in each column
col1.image("images/python.png")
col2.image("images/html.png")
col3.image("images/css.png")
col4.image("images/vscode.png")
col5.image("images/git.png")



st.subheader("Projects: ")

col6 = st.columns(1)

with col6:
    pass

