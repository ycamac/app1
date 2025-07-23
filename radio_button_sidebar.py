import streamlit as st
import pandas as pd
import numpy as np

st.sidebar.write("Type of Analysis")
selected_option=st.sidebar.radio("Select any option", options=("Line Graph","Bar Graph","Area Chart"))
 
data = pd.DataFrame(np.random.randn(50,2), columns=['Age','BMI'])
 
if selected_option=='Line Graph':
    st.line_chart(data)
elif selected_option=='Bar Graph':
    st.bar_chart(data)
else:
    st.area_chart(data)