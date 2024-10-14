import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your Email address")
    massage = st.text_area("Your Message")
    message = f"""
Subject: new email from {user_email}
from: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    print(button)
    if button:
        send_email(massage)
        st.info("Your message was send Successfully")