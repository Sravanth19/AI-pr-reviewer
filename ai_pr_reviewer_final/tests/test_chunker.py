from src.indexing.chunker import chunk_code

def test_chunker_simple():
    code = "def a():\n    return 5\n\nclass C:\n    def m(self):\n        pass\n"
    chunks = chunk_code(code, "sample.py")
    assert len(chunks) >= 2
    assert any(c["type"] == "FunctionDef" for c in chunks) or any(c["type"] == "ClassDef" for c in chunks)
