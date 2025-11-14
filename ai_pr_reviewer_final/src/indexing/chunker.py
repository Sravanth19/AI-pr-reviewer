import ast
def chunk_code(source_code: str, file_path: str):
    try:
        tree = ast.parse(source_code)
    except Exception:
        return [{'file': file_path, 'code': source_code}]
    chunks = []
    for node in tree.body:
        if hasattr(node, 'lineno'):
            start = node.lineno-1
            end = getattr(node, 'end_lineno', start+1)
            code = '\n'.join(source_code.splitlines()[start:end])
            chunks.append({'file': file_path, 'code': code})
    if not chunks:
        chunks.append({'file': file_path, 'code': source_code})
    return chunks
