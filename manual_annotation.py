import streamlit as st
import pandas as pd

st.title('Mannual Annotation Tool')
st.write('by Yulei')

df = pd.read_csv('data2compare.csv')
st.write(df)
st.write(len(df))
for i in len(df):
    st.write(i)
    st.write(df.raw_reviews[i])
    break
