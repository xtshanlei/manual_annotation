import streamlit as st
import pandas as pd

st.title('Mannual Annotation Tool')
st.write('by Yulei')

df = pd.read_csv('data2compare.csv')

container_1 = st.container()
container_2 = st.container()
placeholder = st.empty()

import time

for i in range(200):
    with placeholder.container():
        st.write(df.raw_reviews[i])
        st.write(df.processed_reviews[i])
        answer = st.radio('Is the computer doing a good job?',('Yes','No'),key = i)
        st.write(answer)
