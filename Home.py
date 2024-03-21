import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Ranjit Kumar Yadav")
    content = """Hi, I am Ranjit! a passionate Python programmer and 
    Full Stack Developer, dedicated to crafting innovative solutions. 
    I graduated in 2022 with a Bachelor of Technology in Computer Science. 
    Additionally, I hold a three-year diploma in Computer Science Engineering. 
    I specialize in creating dynamic web applications using Python and 
    related technologies. With a keen interest in data science, 
    I integrate PySpark into my projects for efficient big data 
    processing and analysis, ensuring our solutions are both scalable 
    and insightful. """

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


