import streamlit as st

option = st.selectbox(
    'How would you like to be contacted?',
    ('Email','Home phone','mobile phone'))

st.write('You selected:',option)
