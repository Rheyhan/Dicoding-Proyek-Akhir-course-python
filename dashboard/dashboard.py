import streamlit as st
import time
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


st.set_page_config(page_title='Final Project',  layout='wide')

#this is the header
t1,  = st.columns(1) 

t1.title("Courses Materials application on the *Bike Sharing Dataset")


## Data
    
# Contact Form

with st.expander("Contact me"):
    with st.form(key='contact', clear_on_submit=True):
        
        email = st.text_input('Contact Email')
        st.text_area("Query","Write here if yo wanna contact me")
        
        submit_button = st.form_submit_button(label='Send Information')  