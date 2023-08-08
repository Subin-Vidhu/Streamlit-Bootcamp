import pandas as pd
import numpy as np
import streamlit as st

chart_data = pd.DataFrame(
    np.random.randn(20,3,),
    columns = ['a','b','c'])


st.bar_chart(chart_data)
