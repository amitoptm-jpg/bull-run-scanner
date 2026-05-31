# ── scanner/fetcher.py ─────────────────────
import yfinance as yf
import pandas as pd

def fetch_ohlcv(symbol: str, period: str = "1y") -> pd.DataFrame:
    ticker = f"{symbol}.NS"
    df = yf.download(ticker, period=period,
                     auto_adjust=True, progress=False)
    df.dropna(inplace=True)
    return df
