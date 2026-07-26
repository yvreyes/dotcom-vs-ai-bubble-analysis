import pandas as pd
from config import RAW_DATA_PATH

def main():
    pass

for csv_file in RAW_DATA_PATH.glob("*.csv"):
    df = pd.read_csv(csv_file)
    print(f"File: {csv_file.name}, Rows: {len(df)}, Columns: {len(df.columns)}")