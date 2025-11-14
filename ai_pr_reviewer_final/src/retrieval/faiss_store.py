import faiss, json, numpy as np
from src.indexing.embedder import embed_texts
INDEX_FILE='faiss_index.bin'
META_FILE='index_metadata.json'

def load_index():
    idx = faiss.read_index(INDEX_FILE)
    meta = json.load(open(META_FILE,'r',encoding='utf-8'))
    return idx, meta

def search(query, k=5):
    try:
        idx, meta = load_index()
    except Exception as e:
        raise RuntimeError('Index not found: build the index first') from e
    q = embed_texts([query])
    q = np.array(q).astype('float32')
    D, I = idx.search(q, k)
    results=[]
    for i,score in zip(I[0], D[0]):
        m = meta[i].copy()
        m['score']=float(score)
        results.append(m)
    return results
