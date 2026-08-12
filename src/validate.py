import pandas as pd
from config import RAW_DATA_PATH

def main():
    missing_values()

def missing_values():
    for csv_file in RAW_DATA_PATH.glob("*.csv"):
        df = pd.read_csv(csv_file)

        for col in df.columns:
            columns = f"{col}: {df[col].isnull().sum()}"
            print(columns)
main()