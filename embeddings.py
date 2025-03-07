import ray
from sentence_transformers import SentenceTransformer

ray.init()

model = SentenceTransformer("all-mpnet-base-v2")

@ray.remote
def generate_embeddings(batch_text):
    return model.encode(batch_text)
