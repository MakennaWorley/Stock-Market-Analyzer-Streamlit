import streamlit as st
import plotly.graph_objects as go
from utils.tools import fetch_stock_data
import pandas as pd
import io
import zipfile

st.set_page_config(layout="wide")
st.title("📈 Stock Market Analyzer")

popular_tickers = ["AAPL", "MSFT", "GOOGL", "TSLA", "AMZN", "META", "NFLX", "NVDA"]
selected_tickers = st.multiselect("Select stock tickers", popular_tickers, default=["AAPL"])

col1, col2 = st.columns(2)
with col1:
    start = st.date_input("Start Date", value=pd.to_datetime("2023-01-01"))
with col2:
    end = st.date_input("End Date", value=pd.to_datetime("today"))

ma_1 = st.number_input("Short MA (days)", min_value=1, max_value=100, value=20)
ma_2 = st.number_input("Long MA (days)", min_value=5, max_value=200, value=50)

if "results" not in st.session_state:
    st.session_state["results"] = {}

if st.button("Analyze"):
    if not selected_tickers:
        st.warning("Please select at least one ticker.")
    else:
        st.session_state["results"].clear()
        for ticker in selected_tickers:
            try:
                df = fetch_stock_data(ticker, str(start), str(end), ma_1, ma_2)
                st.session_state["results"][ticker] = df

            except Exception as e:
                st.error(f"⚠️ Error loading data for {ticker}: {e}")

if st.session_state["results"]:
    for ticker, df in st.session_state["results"].items():
        with st.expander(f"📊 {ticker} Analysis", expanded=True):
            # Price + MA plot
            st.markdown(f"### 📈 Price & Moving Averages — {ticker}")
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=df.index, y=df['Price'], name=f"{ticker} Price"))
            fig.add_trace(go.Scatter(x=df.index, y=df[f'MA_{ma_1}'], name=f"{ma_1}-Day MA"))
            fig.add_trace(go.Scatter(x=df.index, y=df[f'MA_{ma_2}'], name=f"{ma_2}-Day MA"))
            st.plotly_chart(fig, use_container_width=True)

            # Return histogram
            st.markdown(f"### 📉 Daily Return Histogram — {ticker}")
            st.bar_chart(df['Return'].dropna())

            # Full data
            st.markdown(f"### 📄 Full Data — {ticker}")
            st.dataframe(df)  # Show everything now!

            # Per-ticker CSV download
            csv = df.to_csv(index=True).encode('utf-8')
            st.download_button(
                label=f"⬇️ Download {ticker} CSV",
                data=csv,
                file_name=f"{ticker}_stock_data.csv",
                mime='text/csv'
            )

    # Download All for multiple tickers
    if len(st.session_state["results"]) > 1:
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "w") as zip_file:
            for ticker, df in st.session_state["results"].items():
                csv_bytes = df.to_csv(index=True).encode('utf-8')
                zip_file.writestr(f"{ticker}_stock_data.csv", csv_bytes)

        zip_buffer.seek(0)
        st.download_button(
            label="⬇️ Download All Selected as ZIP",
            data=zip_buffer,
            file_name="stock_data_bundle.zip",
            mime="application/zip"
        )

