# ── scanner/indicators.py ──────────────────
import pandas as pd
from ta.momentum import RSIIndicator

def compute_all(df: pd.DataFrame) -> pd.DataFrame:
    close = df["Close"]
    df["SMA50"]   = close.rolling(50).mean()
    df["SMA100"]  = close.rolling(100).mean()
    df["SMA200"]  = close.rolling(200).mean()
    df["EMA9"]    = close.ewm(span=9,  adjust=False).mean()
    df["EMA21"]   = close.ewm(span=21, adjust=False).mean()
    df["EMA50"]   = close.ewm(span=50, adjust=False).mean()
    rsi = RSIIndicator(close=close, window=14)
    df["RSI14"]   = rsi.rsi()
    df["Vol20Avg"]= df["Volume"].rolling(20).mean()
    df["VolRatio"]= df["Volume"] / df["Vol20Avg"]
    df["Dist200"] = ((close - df["SMA200"]) / df["SMA200"]) * 100
    return df
