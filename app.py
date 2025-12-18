import streamlit as st
import matplotlib.pyplot as plt

st.title("My First Streamlit App")
st.title("Simple Chart Example")

st.write("Hello 👋 Welcome to my web app")

name = st.text_input("Enter your name")

if st.button("Click Me"):
    st.write("Button clicked!")

if name:
    st.write("Hello", name)

data = [10, 20, 30, 40]
plt.plot(data)
st.pyplot(plt)

