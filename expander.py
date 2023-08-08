import streamlit as st

st.bar_chart({"data":[1,5,2,6,2,1]})

with st.expander("Expand me"):
    st.write("Some text written inside expander")
    st.write("Hello Hello Hello")
