import streamlit as st
st.title("registration page")
name=st.text_input("Full name")
email=st.text_input("Email")
mobile=st.text_input("Mobile Number")
course=st.selectbox("Select course",
                    ["pyhton","java","AI"])
if st.button("Registration"):
    if name and email and mobile:
        st.success("Registration done!")
        
    else:
        st.warning("please fill all the details")