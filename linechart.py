import pandas as pd
import numpy as np
import streamlit as st

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns = ['A','B','C'])

st.line_chart(chart_data)
