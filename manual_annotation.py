import streamlit as st
import pandas as pd

st.title('Mannual Annotation Tool')
st.write('by Yulei')

df = pd.read_csv('data2compare.csv')


for i in range(200):
    st.write(df.raw_reviews[i])
    answer = st.radio('asdf',('Y','N'),key =i)
    st.write(answer)
