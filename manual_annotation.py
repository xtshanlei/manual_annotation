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
    with placeholder.container1:
        st.write(df.raw_reviews[i])
    with placeholder.container2:
        st.write(df.processed_reviews[i])
    time.sleep(5)
