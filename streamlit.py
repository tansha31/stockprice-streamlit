import pandas as pd
import numpy as np
import streamlit as st
import yfinance as yf

st.write("""
# Stock Price Web-App
Shown are the stock prices of **Google** and **Apple!**
""")
st.sidebar.header('Here you can toggle the Period of Stocks')
start_year = st.sidebar.slider('Start Year',2000,2020,2010)
end_year = st.sidebar.slider('End Year',2000,2020,2020)

if end_year <= start_year:
    st.sidebar.header('End Year cannot be same or less than start year')
else:
    tickerData_Google = yf.Ticker('GOOGL')
    tickerData_Apple = yf.Ticker('AAPL')
    tickerDf_G = tickerData_Google.history(period="1d",start=str(start_year)+'-01-01',end=str(end_year)+'-06-2')
    tickerData_A = tickerData_Apple.history(period="1d",start=str(start_year)+'-01-01',end=str(end_year)+'-06-2')

    final_df = pd.concat([tickerDf_G['Close'],tickerData_A['Close']],axis=1)
    final_df.columns = ['Google','Apple']

    st.write("""
    *Closing Price*
    """)

    st.line_chart(final_df)
