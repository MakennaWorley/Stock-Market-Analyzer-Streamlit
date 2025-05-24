# 📈 Stock Market Analyzer

An interactive Streamlit dashboard that lets you analyze historical stock price trends, compute moving averages, visualize daily returns, and optionally correlate movements with headlines.

Built with:
- Python (Pandas)
- Plotly & Streamlit
- yfinance API

## 🚀 Features

- Select one or more popular stock tickers
- Analyze adjustable moving averages (e.g., 20-day, 50-day)
- Visualize:
  - Historical price charts
  - Moving average overlays
  - Daily % return trends
  - Raw data

![screenshot](/assets/dashboard.png)

## 🧰 Tech Stack

| Area          | Tools                |
|---------------|----------------------|
| Data Fetching | `yfinance`, `pandas` |
| Visualization | `plotly`             |
| Dashboard     | `streamlit`          |
| Deployment    | Streamlit Cloud      |

## 📦 Installation

1. **Clone the repo**

```bash
git clone https://github.com/YOUR_USERNAME/stock-analyzer.git
cd stock-analyzer

pip install -r requirements.txt

streamlit run app.py
