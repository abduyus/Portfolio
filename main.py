import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
# title and about me section

st.title("Yusuf Abdur-Rasheed")

st.subheader("About Me")
st.info("Hi! I am Yusuf, A student studying at Solihull School passionate about" 
        "programming based in Solihull, UK. 📍")


st.markdown("[GitHub](https://www.github.com/abduyus)")

st.subheader("🧰 Tools and Languages: ")


components.html(
    """
    <img align="left" alt="Git" width="30px" style="padding-right:10px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" />

    <img align="left" alt="HTML" width="30px" style="padding-right:10px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-plain.svg" />
    <img align="left" alt="CSS" width="30px" style="padding-right:10px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-plain.svg" />

    <img align="left" alt="Python" width="30px" style="padding-right:10px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-plain.svg" />

    <img align="left" alt="GitHub" width="30px" style="padding-right:10px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" />

    """)



