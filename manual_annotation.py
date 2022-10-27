import streamlit as st
import pandas as pd

st.title('Mannual Annotation Tool')
st.write('by Yulei')

df = pd.read_csv('data2compare.csv')

import time
with st.empty():
    for i in range(200):
        st.write(df.raw_reviews[i])
        st.write(df.processed_reviews[i])
        time.sleep(1)
    st.write('end')
