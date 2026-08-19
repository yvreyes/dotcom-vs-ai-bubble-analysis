import pandas as pd
from config import RAW_DATA_PATH

required_col = ["Date", "Open", "High", "Low", "Close", "Volume"]
def main():
    for csv_file in RAW_DATA_PATH.glob("*.csv"):
        df = pd.read_csv(csv_file) 

        print("=============================")
        print(f"File: {csv_file.name}")
        print("=============================\n")

        
        validate_date(df)
    
        # print(f"Rows: {len(df)}")
        # print(f"Columns: {len(df.columns)}\n")

        # missing_values(df)
        # duplicate_values(df)

def validate_columns(df):
    # Check if columns exist
    for col_name in required_col:
        if col_name in df.columns:
            print(f"{col_name} exists")
        else:
            print(f"{col_name} doesnt exists")               

def validate_date(df):
    
    print("Date Validation: \n")
    
    for index, find_date in enumerate(df["Price"]):
        if find_date == "Date":
            print(f"Date marker for at index {index}")
            start_index = index + 1

            print(f"Actual date data starts at index {start_index}")
            date_values = df["Price"][start_index:]
            converted_dates = pd.to_datetime(date_values, errors="coerce")
            invalid_dates = converted_dates.isnull().sum()
            valid_dates = len(date_values) - invalid_dates
            print(f"Valid Dates: {valid_dates}")
            print(f"Invalid Dates: {invalid_dates}")

    #Date order chronological
        

def missing_values(df):
    print("Missing Values:")
    for col in df.columns:
        print(f"{col}: {df[col].isnull().sum()}")    

def duplicate_values(df):
    duplicates = df.duplicated().sum()
    print(f"Duplicate rows: {duplicates}\n")
    
main()
