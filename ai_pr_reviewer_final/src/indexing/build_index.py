import os, json, numpy as np, faiss
from src.indexing.chunker import chunk_code
from src.indexing.embedder import embed_texts

INDEX_FILE='faiss_index.bin'
META_FILE='index_metadata.json'

def build_index(code_root='data/sample_repo'):
    all_chunks=[]
    for root,dirs,files in os.walk(code_root):
        for f in files:
            if f.endswith('.py'):
                path=os.path.join(root,f)
                with open(path,'r',encoding='utf-8') as fh:
                    content=fh.read()
                chunks=chunk_code(content,path)
                all_chunks.extend(chunks)
    texts=[c['code'] for c in all_chunks]
    if not texts:
        print('no texts to index'); return
    emb = embed_texts(texts)
    emb = np.array(emb).astype('float32')
    dim = emb.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(emb)
    faiss.write_index(index, INDEX_FILE)
    with open(META_FILE,'w',encoding='utf-8') as f:
        json.dump(all_chunks,f,indent=2)
    print('index built', len(all_chunks))
if __name__=='__main__':
    build_index()
