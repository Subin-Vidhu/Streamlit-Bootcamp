import streamlit as st
import pandas as pd
import numpy as np

st.write("This is a Table Demo")

df = pd.DataFrame(

    np.random.randn(10,5),
    columns = ('col %d' % i for i in range(5)))

st.dataframe(df)
