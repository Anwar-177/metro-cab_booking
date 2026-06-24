import streamlit as st
st.title("login page")
username=st.text_input("Username")
password=st.text_input("Password",type="password")
if st.button("Signin"):
    if username=="admin" and password=="1234":
        st.success("Login Done!")
        st.balloons()
    else:
        st.error("Invalid")
