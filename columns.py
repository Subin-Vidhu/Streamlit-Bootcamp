import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    st.header("This is column 1")
    st.title("Col 1")
    st.write("Some text inside column 1")


with col2:
    st.header("This is column 2")
    st.title("Col 2")
    st.write("Some text inside column 2")

with col3:
    st.header("This is column 3")
    st.title("Col 3")
    st.write("Some text inside column 3")
