import pandas as pd
from config import RAW_DATA_PATH

def main():
    for csv_file in RAW_DATA_PATH.glob("*.csv"):
        df = pd.read_csv(csv_file) 

        print("=============================")
        print(f"File: {csv_file.name}")
        print("=============================\n")


        print(df.columns)
        print(df.head())
        # print(f"Rows: {len(df)}")
        # print(f"Columns: {len(df.columns)}\n")

        # missing_values(df)
        # duplicate_values(df)

def missing_values(df):
    print("Missing Values:")
    for col in df.columns:
        print(f"{col}: {df[col].isnull().sum()}")    

def duplicate_values(df):
    duplicates = df.duplicated().sum()
    print(f"Duplicate rows: {duplicates}\n")
    
main()
