from opensearchpy import OpenSearch
import numpy as np

client = OpenSearch(hosts=[{"host": "your-opensearch-endpoint", "port": 443}],
                    use_ssl=True, verify_certs=True)

def store_in_opensearch(text, embedding):
    doc = {
        "text": text,
        "vector": embedding.tolist()
    }
    client.index(index="rag_embeddings", body=doc)
    print(f"Stored in OpenSearch: {text[:50]}...")
