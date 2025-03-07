import pandas as pd
import pyarrow.parquet as pq

def convert_jsonl_to_parquet(jsonl_file, parquet_file):
    df = pd.read_json(jsonl_file, lines=True)
    df.to_parquet(parquet_file, engine='pyarrow')
    print(f"Converted {jsonl_file} to {parquet_file}")

if __name__ == "__main__":
    convert_jsonl_to_parquet("../data/raw/data.jsonl", "../data/processed/data.parquet")
