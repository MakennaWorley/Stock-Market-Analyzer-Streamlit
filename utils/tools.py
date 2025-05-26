import io

import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
from urllib.parse import urlparse

def fetch_stock_data(ticker: str, start: str, end: str, ma1=20, ma2=50, use_numpy=False):
    df = yf.download(ticker, start=start, end=end)

    if df.empty:
        raise ValueError(f"No data for {ticker}")

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    price_col = 'Adj Close' if 'Adj Close' in df.columns else 'Close' if 'Close' in df.columns else None
    if not price_col:
        raise KeyError("No usable price column found.")

    df['Price'] = df[price_col]
    df['Return'] = df['Price'].pct_change()

    if use_numpy:
        df[f'MA_{ma1}'] = np.append([np.nan] * (ma1 - 1), np.convolve(df['Price'], np.ones(ma1) / ma1, mode='valid'))
        df[f'MA_{ma2}'] = np.append([np.nan] * (ma2 - 1), np.convolve(df['Price'], np.ones(ma2) / ma2, mode='valid'))
    else:
        df[f'MA_{ma1}'] = df['Price'].rolling(window=ma1).mean()
        df[f'MA_{ma2}'] = df['Price'].rolling(window=ma2).mean()

    return df

def save_histogram_as_png(series, ticker):
    fig, ax = plt.subplots()
    sns.histplot(series.dropna(), bins=30, kde=True, ax=ax)
    ax.set_title(f"{ticker} Return Distribution")
    ax.set_xlabel("Daily Return")
    ax.set_ylabel("Frequency")

    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)
    return buf

def get_headline_sentiments(headlines):
    result = []
    for text, url, time_str in headlines:
        domain = urlparse(url).netloc.replace("www.", "")
        score = TextBlob(text).sentiment.polarity
        result.append((text, domain, score, url, time_str))
    return result
