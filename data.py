import streamlit as st
import yfinance as yf
type = "BTC-USD"
data = yf.Ticker(type)
filter = data.history(period="1y")
st.write("# Bitcoin Data")
st.line_chart(filter.Close)
type = "ETH-USD"
data = yf.Ticker(type)
filter = data.history(period="1y")
st.write("# ETH Data")
st.line_chart(filter.Close)
type = "ADA-USD"
data = yf.Ticker(type)
filter = data.history(period="1y")
st.write("# Cardano Data")
st.line_chart(filter.Close)
type = "MATIC-USD"
data = yf.Ticker(type)
filter = data.history(period="1y")
st.write("# Polygon Data")
st.line_chart(filter.Close)
type = "BNB-USD"
data = yf.Ticker(type)
filter = data.history(period="1y")
st.write("# Binance Data")
st.line_chart(filter.Close)
type = "MANA-USD"
data = yf.Ticker(type)
filter = data.history(period="1y")
st.write("# Decentraland Data")
st.line_chart(filter.Close)