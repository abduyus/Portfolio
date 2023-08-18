import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

df = pd.read_csv("data.csv", sep=";")
st.set_page_config(page_title="Yusuf Abdur-Rasheed", page_icon="🧊", layout="wide")

st.title("My Projects: ")
col1, col2 = st.columns(2)

with col1:
    for index, row in df[:2].iterrows():
        st.subheader(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])        
        st.write(f"[Demo Link]({row['demo']})")
        st.write(f"[Source Code]({row['source_code']})")


with col2:
    for index, row in df[2:6].iterrows():
        st.subheader(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Demo Link]({row['demo']})")
        st.write(f"[Source Code]({row['source_code']})")


# q: Why do I keep getting this error: 'SyntaxError: unterminated string literal' with this code st.image(row[r"project_images\" + row["image"]])?
# a: You need to add an extra backslash to escape the backslash in the path. So it should be: st.image(row[r"project_images\\" + row["image"]])                                                                                   
# Q: with the code you gave me I am now getting this error: KeyError: 'project_images\\\\weather.png'?#
# A: You need to change the path to the image to be: row[r"project_images\\" + row["image"]]
# Q: How do I do that?
# A: You need to change the path to the image to be: row[r"project_images\\" + row["image"]]
# Q: but how do I change the path of the image to be that?
