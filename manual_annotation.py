import streamlit as st
import pandas as pd

st.title('Mannual Annotation Tool')
st.write('by Yulei')

df = pd.read_csv('data2compare.csv')

with st.empty():
    for i in range(200):
        st.write(df.raw_reviews[i])
        if st.button('YES'):
            answer = 1
        elif st.button('NO'):
            answer = 0
        st.write(answer)
