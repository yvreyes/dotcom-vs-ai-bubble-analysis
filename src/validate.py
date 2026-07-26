import pandas as pd
from config import RAW_DATA_PATH

def main():
    pass

for csv_file in RAW_DATA_PATH.glob("*.csv"):
    df = pd.read_csv(csv_file)
    print("===================================")
    print(f"File: {csv_file.name}")
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")
    print("===================================")