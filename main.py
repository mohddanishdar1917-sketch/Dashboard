import streamlit as st
import pandas as pd
import numpy as np

#PAge configuration
st.set_page_config(page_title = "Dashboard",
                   page_icon = "fortuner1.png",
                   layout ="wide",
                   initial_sidebar_state = "expanded"
                   )
st.title("Student performance Dashboard")
st.write("This is the sample dashboard")

data = {
    "T1":[66,89,78,92],
    "T2":[91,68,68,82],
    "T3":[76,99,68,72],
}

df = pd.DataFrame(data, index = ["S1","S2","S3","S4"])

st.subheader("Marks Card")
st.dataframe(df)

st.subheader("Performance trend (Line Chart)")
st.line_chart(df.T)