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
        st.header('Is the processed reviews what we want?')
        answer = st.radio('Is the processed reviews what we want?',('YES','NO'))
        st.write(answer)
