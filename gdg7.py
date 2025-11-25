import streamlit as st 

counter=0

button=st.button("inc value")
if button:
    counter+=1
    
    st.header(counter)
    