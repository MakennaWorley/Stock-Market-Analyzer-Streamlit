import streamlit as st
import plotly.graph_objects as go
from utils.tools import fetch_stock_data
import pandas as pd

st.set_page_config(layout="wide")
st.title("📈 Stock Market Time Series Analyzer")

ticker = st.text_input("Enter Stock Ticker:", "AAPL")
col1, col2 = st.columns(2)
with col1:
    start = st.date_input("Start Date", value=pd.to_datetime("2020-01-01"))
with col2:
    end = st.date_input("End Date", value=pd.to_datetime("today"))

if st.button("Fetch Data"):
    df = fetch_stock_data(ticker, str(start), str(end))

    st.subheader("Adjusted Close Price with Moving Averages")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['Price'], name="Price"))
    fig.add_trace(go.Scatter(x=df.index, y=df['MA_20'], name="20-Day MA"))
    fig.add_trace(go.Scatter(x=df.index, y=df['MA_50'], name="50-Day MA"))
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Daily % Return")
    st.line_chart(df['Return'].dropna())

    st.subheader("Raw Data")
    st.dataframe(df.tail(10))
