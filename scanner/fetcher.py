# ── scanner/fetcher.py (FIXED) ─────────────
import yfinance as yf
import pandas as pd

def fetch_ohlcv(symbol: str, period: str = "1y") -> pd.DataFrame:
    ticker = f"{symbol}.NS"
    df = yf.download(ticker, period=period,
                     auto_adjust=True, progress=False)
    # Fix multi-level columns (causes HYUNDAI/BAJFINANCE error)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    df.dropna(inplace=True)
    return df
