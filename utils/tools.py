import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker: str, start: str, end: str, ma1=20, ma2=50):
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
    df[f'MA_{ma1}'] = df['Price'].rolling(window=ma1).mean()
    df[f'MA_{ma2}'] = df['Price'].rolling(window=ma2).mean()

    return df
