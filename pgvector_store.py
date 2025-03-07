import psycopg2
import numpy as np

PG_CONFIG = {
    "dbname": "ragdb",
    "user": "admin",
    "password": "password",
    "host": "your-rds-endpoint"
}

def store_in_pgvector(text, embedding):
    conn = psycopg2.connect(**PG_CONFIG)
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS embeddings (
            id SERIAL PRIMARY KEY,
            text TEXT,
            vector VECTOR(768)
        )
    """)
    
    cursor.execute("INSERT INTO embeddings (text, vector) VALUES (%s, %s)", (text, embedding.tolist()))
    conn.commit()
    conn.close()
    print(f"Stored in PostgreSQL: {text[:50]}...")
