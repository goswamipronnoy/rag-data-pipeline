# RAG Data Ingestion Pipeline

## Overview
This project implements a Retrieval Augmented Generation (RAG) data ingestion pipeline** using Ray, OpenSearch, and PostgreSQL with pgvector for large-scale ML workloads.

## Project Structure:

```
rag-data-ingestion-pipeline/
│-- data/
│   │-- raw/
│   │   ├── data.jsonl
│   │-- processed/
│   │   ├── data.parquet
│-- src/
│   │-- convert.py  # Converts JSONL to Parquet
│   │-- embeddings.py  # Handles embedding generation with Ray
│   │-- opensearch_store.py  # Stores embeddings in OpenSearch
│   │-- pgvector_store.py  # Stores embeddings in PostgreSQL
│   │-- pipeline.py  # Main script to run ingestion pipeline
│-- requirements.txt  # Python dependencies
│-- README.md
```

## Features
- Efficient embedding generation using distributed processing
- Storage in OpenSearch for ANN retrieval
- Storage in PostgreSQL with pgvector for k-NN searches

## Setup
### 1. Install dependencies
```
pip install -r requirements.txt
```
### 2. Convert Data
```
python src/convert.py
```
### 3. Run Ingestion Pipeline
```
python src/pipeline.py
```


