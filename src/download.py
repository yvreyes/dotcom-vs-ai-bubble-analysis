import yfinance as yf
from config import MARKET_PERIODS, RAW_DATA_PATH 

# def main():

#     for period in MARKET_PERIODS:
#         print(period, MARKET_PERIODS['dotcome']["tickers"])

#     return(period)
# main;        



for period in MARKET_PERIODS:
    period_data = MARKET_PERIODS[period]
    stocks = period_data["tickers"].values()
    start_date = period_data["start"]
    end_date = period_data["end"]
    print(period, stocks)
    print(period, start_date, end_date)