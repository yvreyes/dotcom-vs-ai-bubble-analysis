import pandas as pd
from config import RAW_DATA_PATH

required_col = ["Date", "Open", "High", "Low", "Close", "Volume"]
def main():
    for csv_file in RAW_DATA_PATH.glob("*.csv"):
        df = pd.read_csv(csv_file) 

        print("=============================")
        print(f"File: {csv_file.name}")
        print("=============================\n")
        print(f"Rows: {len(df)}")
        print(f"Columns: {len(df.columns)}\n")
        validate_date(df)
        missing_values(df)
        duplicate_values(df)

def validate_columns(df):
    # Check if columns exist
    for col_name in required_col:
        if col_name in df.columns:
            print(f"{col_name} exists")
        else:
            print(f"{col_name} doesnt exists")               

def validate_date(df):
    print("-----------------------------")
    print("Date Validation: ")
    print("-----------------------------")
    for index, find_date in enumerate(df["Price"]):
        if find_date == "Date":
            print(f"Date Marker: Found")

            start_index = index + 1
            date_values = df["Price"][start_index:]
            converted_dates = pd.to_datetime(date_values, errors="coerce")
            invalid_dates = converted_dates.isnull().sum()
            valid_dates = len(date_values) - invalid_dates

            print(f"Valid Dates: {valid_dates}")
            print(f"Invalid Dates: {invalid_dates}")

            chronological = converted_dates.is_monotonic_increasing
            if chronological == True:
                print("Chronological Order: Valid")
            else:
                print("Chronological Order: Invalid")
        

def missing_values(df):
    print("-----------------------------")
    print("Missing Values:")
    print("-----------------------------")
    for col in df.columns:
        print(f"{col}: {df[col].isnull().sum()}")    

def duplicate_values(df):
    duplicates = df.duplicated().sum()
    print("-----------------------------")
    print(f"Duplicate rows: {duplicates}")
    print("-----------------------------")    
main()
