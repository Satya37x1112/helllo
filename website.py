import streamlit as st

st.title("welcome to my website")
name=st.text_input("enter your name")
address=st.text_area("enter your address")
course=st.text_input("enter your course")
year=st.selectbox("select your year :",(1,2,3,4,5))
button=st.button("done")