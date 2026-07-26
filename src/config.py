from pathlib import Path

# Project Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_PATH = DATA_DIR / "raw"
PROCESSED_DATA_PATH = DATA_DIR / "processed"

# Market Periods

MARKET_PERIODS = {
    "dotcom": {
        "start": "1995-01-01",
        "end": "2002-12-31",
        "tickers": {
            "Cisco": "CSCO",
            "Intel": "INTC",
            "Microsoft": "MSFT",
            "Oracle": "ORCL",
            "Yahoo": "YHOO",
            "Amazon": "AMZN",
        }
    },
    "ai": {
        "start": "2022-01-01",
        "end": "2026-04-30",
        "tickers": {
            "Nvidia": "NVDA",
            "Microsoft": "MSFT",
            "Alphabet": "GOOGL",
            "Amazon": "AMZN",
            "Meta": "META",
            "Palantir": "PLTR"
        }
    }
}