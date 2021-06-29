import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import requests
from dotenv import load_dotenv
import os
import plotly.io as pio



st.title('Stock price')
st.sidebar.title("Selector")
st.markdown('<style>body{background-color: lightblue;}</style>',unsafe_allow_html=True)


year_select = st.sidebar.selectbox('Select a year',(2021,2020,2019,2018,2017,2016,\
                                                      2015,2014,2013,2012,2011,2010,\
                                                      2009,2008,2007,2006,2005,2004,\
                                                      2003,2002,2001,2000,1999))
month_select = st.sidebar.selectbox('Selecet a month',(12,11,10,9,8,7,6,5,4,3,\
                                                       2,1))


def load_data ():
    load_dotenv()
    api_key = os.environ['PRIVATE_API_KEY']
    df = pd.read_csv("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=full&symbol=IBM&apikey=api_key&datatype=csv")
    return df

data= load_data()
data['year']= pd.DatetimeIndex(data['timestamp']).year
data['month']=pd.DatetimeIndex(data['timestamp']).month
data['day']=pd.DatetimeIndex(data['timestamp']).day

selected_year = data[data['year']==year_select]
selected = selected_year[selected_year['month']==month_select]
st.markdown("## ** Selected year and month**")

fig = px.line(selected, x="timestamp",y="close", title = 'Close Price')
st.plotly_chart(fig)
#fig.show()





