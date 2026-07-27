import pandas as pd
from config import RAW_DATA_PATH

def main():
    validate_csv_files()

def validate_csv_files():
    for csv_file in RAW_DATA_PATH.glob("*.csv"):
        df = pd.read_csv(csv_file)
       
        print("===================================")
        print(f"File: {csv_file.name}\n")
        print(f"Rows: {len(df)}")
        print(f"Columns: {len(df.columns)}\n")   
        print("Missing Values:")
        print(f"Open: {df['Open'].isnull().sum()}")
        print(f"High: {df['High'].isnull().sum()}")
        print(f"Low: {df['Low'].isnull().sum()}")
        print(f"Close: {df['Close'].isnull().sum()}")
        print(f"Volume: {df['Volume'].isnull().sum()}")
        print("===================================") 

if __name__ == "__main__":
    main()