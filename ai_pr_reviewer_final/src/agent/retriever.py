import os, json, numpy as np
from src.retrieval.faiss_store import search

def retrieve_context(text: str, top_k: int = 5):
    # Use FAISS-based search for similar code chunks
    try:
        results = search(text, k=top_k)
        return results
    except Exception as e:
        return []
