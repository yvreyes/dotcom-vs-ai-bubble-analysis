import yfinance as yf
from config import MARKET_PERIODS, RAW_DATA_PATH 

# def main():

#     for period in MARKET_PERIODS:
#         print(period, MARKET_PERIODS['dotcome']["tickers"])

#     return(period)
# main;        



for period in MARKET_PERIODS:
    period_data = MARKET_PERIODS[period]

    stocks = period_data["tickers"]
    start_date = period_data["start"]
    end_date = period_data["end"]

    for company_name in stocks:
        ticker = stocks[company_name]
        # print(f"[{period}] {company_name} {ticker}")
        
        data = yf.download(
        tickers=ticker, 
        start=start_date, 
        end=end_date
        ).to_csv(RAW_DATA_PATH / f"{period}_{company_name}_data.csv")
