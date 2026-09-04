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
        # validate_columns(df)
        # validate_date(df, start_index)
        # missing_values(df)
        # duplicate_values(df)
        # validate_data_type(df)
        find_data_start(df)

def validate_columns(df):
    # Check if columns exist
    for col_name in required_col:
        if col_name in df.columns:
            print(f"{col_name} exists")
        else:
            print(f"{col_name} doesnt exists")     

def find_data_start(df):
    for index, find_date in enumerate(df["Price"]):
        if find_date == "Date":
            start_index = index + 1
            # start_index + 1
            print(start_index)
        
def validate_date(df, start_index):
    print("-----------------------------")
    print("Date Validation: ")
    print("-----------------------------")
    date_found = False
   
    if start_index == "Date":
        date_found = True
        print(f"Date Marker: Found")
        
        converted_dates = pd.to_datetime(start_index.values, errors="coerce")
        invalid_dates = converted_dates.isnull().sum()
        valid_dates = len(start_index.values) - invalid_dates
        print(f"Valid Dates: {valid_dates}")
        print(f"Invalid Dates: {invalid_dates}")
        chronological = converted_dates.is_monotonic_increasing
        if chronological:
            print("Chronological Order: Valid")
        else:
            print("Chronological Order: Invalid")  
    if not date_found:
        print("Date Marker: Not Found") 
        
                  
# def validate_data_type(df, find_data_start):
#     ohlcv_columns = required_col[1:]
#     for num_col in df[ohlcv_columns]:
#         converted_val = pd.to_numeric(df[num_col], errors="coerce")
#         invalid_val = converted_val.isnull().sum()
#         print(f"{num_col}: Invalid values {invalid_val}")

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
