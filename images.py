from PIL import Image
import streamlit as st

image = Image.open('test.jpg')

st.image(image,caption="Nice Picture")
