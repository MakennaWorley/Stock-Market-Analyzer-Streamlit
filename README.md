# 📈 Stock Market Analyzer

An interactive Streamlit dashboard that lets you analyze historical stock prices, visualize return distributions, and correlate sentiment from recent financial headlines.

Built with:
- Python (Pandas, NumPy)
- Plotly, Seaborn, Matplotlib
- yfinance API
- BeautifulSoup + Regex
- TextBlob for sentiment analysis

---

## 🚀 Features

- 🔍 Select one or more stock tickers
- 📅 Define custom date ranges
- 🧮 Choose moving average windows (20-day, 50-day, etc.)
- ✅ Toggle between Pandas and NumPy moving average calculation
- 📈 View:
  - Historical price chart with moving averages (Plotly)
  - Return distribution histogram (Seaborn + Matplotlib)
  - Full raw data table (Pandas)
- 📰 Scrape recent headlines from Yahoo Finance:
  - Includes source, publish time, and sentiment score
- 💾 Export:
  - CSV download per ticker
  - ZIP archive of all selected tickers
  - PNG of histogram chart

---

## 🖼 Images

![screenshot](/assets/ui.png)
![screenshot](/assets/example_data.png)

## 🧰 Tech Stack

| Area             | Tools Used                                     |
|------------------|------------------------------------------------|
| Data Fetching    | `yfinance`, `pandas`, `numpy`                  |
| Visualization    | `plotly`, `matplotlib`, `seaborn`              |
| NLP Sentiment    | `textblob`                                     |
| Web Scraping     | `beautifulsoup4`, `requests`, `re`             |
| Dashboard        | `streamlit`                                    |
| Deployment       | Streamlit Cloud or Docker                      |

---

## 📦 Installation

1. **Clone the repo**

```bash
git clone https://github.com/YOUR_USERNAME/stock-analyzer.git
cd stock-analyzer

pip install -r requirements.txt
python -m textblob.download_corpora

streamlit run app.py
