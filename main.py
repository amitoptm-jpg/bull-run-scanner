# ── main.py ────────────────────────────────
import pandas as pd
import os
from scanner.screener import run_screener

SYMBOLS = [
    "LT","ASIANPAINT","YESBANK","DRREDDY","MANKIND",
    "NYKAA","DIVISLAB","GRSE","INDUSINDBK","FORTIS",
    "PHOENIXLTD","ANTHEM","MEESHO","BHARTIARTL","INFY",
    "HDFCBANK","FEDERALBNK","RELIANCE","MCX","NETWEB",
    "NATIONALUM","COALINDIA","BAJFINANCE","HYUNDAI",
]

if __name__ == "__main__":
    print(f"Scanning {len(SYMBOLS)} stocks...\n")
    results = run_screener(SYMBOLS)
    print("\n=== ENTRY SIGNALS TODAY ===")
    if results.empty:
        print("No signals today.")
    else:
        cols = ["symbol","cmp","sma200","dist200_pct",
                "rsi","vol_ratio","stop_loss","target","risk_reward"]
        print(results[cols].to_string(index=False))
    os.makedirs("output", exist_ok=True)
    results.to_csv("output/signals_today.csv", index=False)
    print("\nSaved → output/signals_today.csv")
