import streamlit as st
import pandas as pd

st.title('Manual Annotation Tool')
st.write('by Yulei')

df = pd.read_csv('data2compare.csv')
import time
placeholder = st.empty()
container1 = placeholder.container()
container2 = placeholder.container()
for i in range(200):
    container1.write(df.raw_reviews[i])
    container2.write(df.processed_reviews[i])
    time.sleep(2)
