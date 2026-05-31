# ── scanner/signals.py ─────────────────────
import pandas as pd
from config import *

def check_entry_signal(df: pd.DataFrame, symbol: str) -> dict:
    latest = df.iloc[-1]
    result = {
        "symbol": symbol,
        "cmp": round(float(latest["Close"]), 2),
        "sma200": round(float(latest["SMA200"]), 2),
        "dist200_pct": round(float(latest["Dist200"]), 2),
        "rsi": round(float(latest["RSI14"]), 1),
        "vol_ratio": round(float(latest["VolRatio"]), 2),
        "signal": False, "reasons": []
    }
    if not (latest["Close"] > latest["SMA50"] > latest["SMA100"] > latest["SMA200"]):
        result["reasons"].append("FAIL: DMA stack not bullish")
        return result
    if not (DMA_ABOVE_PCT_MIN <= latest["Dist200"] <= DMA_ABOVE_PCT_MAX):
        result["reasons"].append(f"FAIL: Dist200={result['dist200_pct']}%")
        return result
    if not (latest["EMA9"] > latest["EMA21"] > latest["EMA50"]):
        result["reasons"].append("FAIL: EMA stack broken")
        return result
    if not (RSI_MIN <= latest["RSI14"] <= RSI_MAX):
        result["reasons"].append(f"FAIL: RSI={result['rsi']}")
        return result
    result["signal"] = True
    result["stop_loss"] = round(float(latest["SMA200"]) * STOP_LOSS_BUFFER, 2)
    result["target"]    = round(float(latest["Close"]) * (1 + TARGET_PCT), 2)
    result["risk_reward"] = round(
        (result["target"] - result["cmp"]) /
        max(result["cmp"] - result["stop_loss"], 0.01), 2)
    result["reasons"].append("ALL FILTERS PASSED")
    return result
