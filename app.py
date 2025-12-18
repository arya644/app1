import streamlit as st

st.title("My First Streamlit App")

st.write("Hello 👋 Welcome to my web app")

name = st.text_input("Enter your name")

if st.button("Click Me"):
    st.write("Button clicked!")

if name:
    st.write("Hello", name)
