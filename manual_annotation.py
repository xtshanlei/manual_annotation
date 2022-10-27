import streamlit as st
import pandas as pd

st.title('Mannual Annotation Tool')
st.write('by Yulei')

df = pd.read_csv('data2compare.csv')
st.write(df)

for i in len(df):
    st.write(record.raw_reviews[i])
    break
