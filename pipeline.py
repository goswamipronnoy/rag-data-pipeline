from convert import convert_jsonl_to_parquet
from embeddings import generate_embeddings
from opensearch_store import store_in_opensearch
from pgvector_store import store_in_pgvector
import ray
import pandas as pd

ray.init()

def process_dataset(parquet_file):
    df = pd.read_parquet(parquet_file)
    text_samples = df["text"].tolist()[:100]  # Sample size for testing
    
    embeddings = ray.get([generate_embeddings.remote(text) for text in text_samples])
    
    for text, embedding in zip(text_samples, embeddings):
        store_in_opensearch(text, embedding)
        store_in_pgvector(text, embedding)

if __name__ == "__main__":
    convert_jsonl_to_parquet("../data/raw/data.jsonl", "../data/processed/data.parquet")
    process_dataset("../data/processed/data.parquet")
