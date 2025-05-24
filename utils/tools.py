import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker: str, start: str, end: str):
    df = yf.download(ticker, start=start, end=end)

    if df.empty:
        raise ValueError("No data fetched. Check the ticker or date range.")

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    if 'Adj Close' in df.columns:
        price_col = 'Adj Close'
    elif 'Close' in df.columns:
        price_col = 'Close'
    else:
        raise KeyError("Neither 'Adj Close' nor 'Close' column found in data.")

    df['Return'] = df[price_col].pct_change()
    df['MA_20'] = df[price_col].rolling(window=20).mean()
    df['MA_50'] = df[price_col].rolling(window=50).mean()

    df.rename(columns={price_col: 'Price'}, inplace=True)

    print("Columns fetched:", df.columns.tolist())

    return df
