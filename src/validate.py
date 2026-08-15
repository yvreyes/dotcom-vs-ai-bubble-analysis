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
            valid_dates = len(df[[find_date][start_index:]])
            invalid_dates = enumerate(valid_dates) 
            print(f"Valid Dates: {valid_dates}")
            print(f"Invalid Dates: {invalid_dates}")

    #date order chronological
        

def missing_values(df):
    print("Missing Values:")
    for col in df.columns:
        print(f"{col}: {df[col].isnull().sum()}")    

def duplicate_values(df):
    duplicates = df.duplicated().sum()
    print(f"Duplicate rows: {duplicates}\n")
    
main()
