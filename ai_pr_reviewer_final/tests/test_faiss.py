from src.indexing.build_index import build_index
from src.retrieval.faiss_store import search

def test_build_and_search(tmp_path):
    # Use sample repo in data/sample_repo
    build_index(code_root="data/sample_repo")
    results = search("login user", k=2)
    assert isinstance(results, list)
    assert len(results) >= 1
