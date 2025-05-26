import requests
from bs4 import BeautifulSoup
import re

def get_news_headlines(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}?p={ticker}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    pattern = re.compile(rf'\b{ticker}\b', re.IGNORECASE)

    headlines = []
    for item in soup.select("li.js-stream-content, div.js-stream-content"):
        a = item.find("a", href=True)
        span = item.find("span", string=re.compile(r'(ago|AM|PM|\d{4})'))  # tries to catch timestamp
        if a:
            text = a.get_text(strip=True)
            href = a["href"]
            full_url = f"https://finance.yahoo.com{href}" if href.startswith("/") else href
            if pattern.search(text) and len(text) > 15:
                time_text = span.get_text(strip=True) if span else "N/A"
                headlines.append((text, full_url, time_text))

    return headlines[:5]
