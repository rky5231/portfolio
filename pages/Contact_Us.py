import streamlit as st

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address", key="email")
    message = st.text_area("Your Message", key="message")
    button = st.form_submit_button("Submit")