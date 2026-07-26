import yfinance as yf
from config import MARKET_PERIODS, RAW_DATA_PATH 

def main():
    for period in MARKET_PERIODS:
        period_data = MARKET_PERIODS[period]

        stocks = period_data["tickers"]
        start_date = period_data["start"]
        end_date = period_data["end"]

        for company_name in stocks:
            ticker = stocks[company_name]
            
            data = yf.download(
                tickers=ticker, 
                start=start_date, 
                end=end_date
            )

            data.to_csv(
                RAW_DATA_PATH / f"{period}_{company_name}_data.csv"
            )

if __name__ == "__main__":
    main()