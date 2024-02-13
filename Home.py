import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Ranjit Kumar Yadav")
    content = """Hi, I am Ranjit! I am a Python programmer and a 
    Full Stack Developer currently working at Cognizant. I graduated in 2022 
    with a Bachelor of Technology in Computer Science. Additionally, I hold 
    a three-year diploma in Computer Science Engineering. My expertise lies 
    in developing web applications using Python and related technologies. At 
    Cognizant, I contribute to various software projects, leveraging my 
    skills in both front-end and back-end development. """

    st.info(content)

content2 = """Below you can find some of the apps I have built in Python. 
Fell free to contact me! """
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:4].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[4:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


