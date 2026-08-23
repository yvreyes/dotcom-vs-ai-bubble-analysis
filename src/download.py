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

# Alright I think im mostly done with validate_date 
# ``
# def validate_date(df):
    
#     print("Date Validation: \n")
    
#     for index, find_date in enumerate(df["Price"]):
#         if find_date == "Date":
#             print(f"Date Marker: Found")

#             start_index = index + 1
#             date_values = df["Price"][start_index:]
#             converted_dates = pd.to_datetime(date_values, errors="coerce")
#             invalid_dates = converted_dates.isnull().sum()
#             valid_dates = len(date_values) - invalid_dates

#             print(f"Valid Dates: {valid_dates}")
#             print(f"Invalid Dates: {invalid_dates}")

#             chronological = converted_dates.is_monotonic_increasing
#             if chronological == True:
#                 print("Chronological Order: Valid")
#             else:
#                 print("Chronological Order: Invalid")
# ``
# I want to know what else should be worked on validate.py and going back to missing values, maybe taht explains why it returns something like this 
# ``
# Missing Values:
# Price: 0
# Close: 1
# High: 1
# Low: 1
# Open: 1
# Volume: 1
# ``
# Maybe because it should be "Date" instead of Price but I get it that we'll work on it on clean.py