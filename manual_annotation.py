import streamlit as st
import pandas as pd

st.title('Manual Annotation Tool')
st.write('by Yulei')

df = pd.read_csv('data2compare.csv')
i=0
while i <=200:
    st.write(df.raw_reviews[i])
    st.write(df.processed_reviews[i])
    if st.button('YES',key='yes'+str(i)):
        answer = 1
    elif st.button('NO',key ='no'+str(i)):
        answer = 0

    if st.button('YES') or st.button('NO'):
        if st.button('Next',key ='next'+str(i)):
            i +=1
