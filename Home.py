import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Ranjit Kumar Yadav")
    content = """Hi, I am Ranjit! A dedicated Full Stack Developer with a passion for creating innovative web solutions. I specialize in Java, Spring Boot, ReactJS, and AWS, bringing robust and dynamic applications to life. I hold a Bachelor's degree in Computer Science Engineering and have additional proficiency in Front-End UI Development and MySQL Query Concepts.

With a strong foundation in both back-end and front-end technologies, I excel in crafting seamless user experiences. My expertise extends to Python, where I leverage its versatility to solve complex problems. I am committed to delivering high-quality, scalable solutions that meet modern web standards. """

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


