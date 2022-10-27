import streamlit as st
import pandas as pd

st.title('Mannual Annotation Tool')
st.write('by Yulei')

df = pd.read_csv('data2compare.csv')

container_1 = st.container()
container_2 = st.container()
import time
for i in range(200):
    container_1.write('Raw reviews:')
    container_1.write(df.raw_reviews[i])
    container_2.write('Processed reviews')
    container_2.write(df.processed_reviews[i])
    time.sleep(2)
