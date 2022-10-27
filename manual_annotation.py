import streamlit as st
import pandas as pd

st.title('Mannual Annotation Tool')
st.write('by Yulei')

df = pd.read_csv('data2compare.csv')
import time
placeholder = st.empty()
container1 = st.container()
container2 = st.container()
for i in range(200):
    with placeholder.container():
        container1.write(df.raw_reviews[i])
        container2.write(df.processed_reviews[i])
    placeholder.empty()
