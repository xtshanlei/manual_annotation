import streamlit as st
import pandas as pd

st.title('Mannual Annotation Tool')
st.write('by Yulei')

df = pd.read_csv('data2compare.csv')

placeholder = st.empty()
import time
for i in range(200):
    with placeholder.container():
        st.write(df.raw_reviews[i])
        st.write(df.processed_reviews[i])
        time.sleep(2)

# Clear all those elements:
placeholder.empty()
