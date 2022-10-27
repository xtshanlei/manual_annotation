import streamlit as st
import pandas as pd

st.title('Mannual Annotation Tool')
st.write('by Yulei')

df = pd.read_csv('data2compare.csv')
import time
placeholder = st.empty()
for i in range(200):
    with placeholder.container():
        st.write(df.raw_reviews[i])
    with placeholder.container():
        st.write(df.processed_reviews[i])
    time.sleep(5)
