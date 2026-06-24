import streamlit as st
import random
st.title("Friendship Calculator")
n1=st.text_input("Your Name")
n2=st.text_input("friend's name")
if st.button("check %"):
    s=random.randint(1,100)
    st.success(f"Friendship score:{s} %")
    st.balloons()