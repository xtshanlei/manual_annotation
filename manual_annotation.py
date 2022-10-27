import streamlit as st
import pandas as pd

st.title('Mannual Annotation Tool')
st.write('by Yulei')

df = pd.read_csv('data2compare.csv')

with st.empty():
    for i in range(200):
        st.header('Raw reviews')
        st.write(df.raw_reviews[i])
        st.header('Processed reviews')
        st.write(df.processed_reviews[i])

import time

with st.empty():
    for seconds in range(60):
        st.write(f"⏳ {seconds} seconds have passed")
        time.sleep(1)
    st.write("✔️ 1 minute over!")
