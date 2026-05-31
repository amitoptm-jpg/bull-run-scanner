# ── scanner/screener.py ────────────────────
import pandas as pd
from scanner.fetcher import fetch_ohlcv
from scanner.indicators import compute_all
from scanner.signals import check_entry_signal

def run_screener(symbols: list) -> pd.DataFrame:
    signals = []
    for sym in symbols:
        try:
            df = fetch_ohlcv(sym)
            if len(df) < 220:
                continue
            df = compute_all(df)
            sig = check_entry_signal(df, sym)
            signals.append(sig)
            status = "SIGNAL" if sig["signal"] else sig["reasons"][0]
            print(f"{sym:15s}: {status}")
        except Exception as e:
            print(f"{sym:15s}: ERROR — {e}")
    results = pd.DataFrame(signals)
    if results.empty:
        return results
    return results[results["signal"]==True].sort_values(
        "risk_reward", ascending=False)
