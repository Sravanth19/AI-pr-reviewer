import os

def read_text_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_text_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
