import yfinance as yf
import streamlit as st
import datetime
import numpy as np
import pandas as pd

st.write("""
# Stock Price App
Shown are the stock **Open, Close , Low ,High price** and **volume** of **Google(GOOGL),  Microsoft(MSFT), Apple(APPL)**!

Between **Input date** to **Current date**
""")
start='2010-07-23'
start=st.sidebar.text_input('Start Date format YYYY-MM-DD')
end=datetime.datetime.today().strftime ('%Y-%m-%d')
#get data on this ticker
st.write('From given Start date', start ,'to current Date', end)
#define the ticker symbol
if st.sidebar.checkbox('Single Company'):
    option = st.sidebar.selectbox('Select Company', ('GOOGL','AAPL','MSFT'))
    st.write('Your selection: ', option)
    tickerSymbol = option
    tickerData = yf.Ticker(tickerSymbol)
else:
    options = st.sidebar.multiselect('Select Companies (atleast 2)', ('GOOGL','AAPL','MSFT'))
    st.write('You selected: ', options)
    tickerSymbol = options

    tickerData = yf.Tickers(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start=start, end=end)

if st.sidebar.checkbox('Show data'):
    st.write(tickerDf)


# Open	High	Low	Close	Volume
st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
## Opening Price
""")
st.line_chart(tickerDf.Open)

st.write("""
## High Price
""")
st.line_chart(tickerDf.High)

st.write("""
## Low Price
""")
st.line_chart(tickerDf.Low)

st.write("""
## Volume
""")
st.line_chart(tickerDf.Volume)
