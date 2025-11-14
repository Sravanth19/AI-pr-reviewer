import ast
from typing import List

def find_function_calls(code: str) -> List[str]:
    """Return list of function names called in code string."""
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return []
    calls = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            func = node.func
            if isinstance(func, ast.Name):
                calls.add(func.id)
            elif isinstance(func, ast.Attribute):
                calls.add(func.attr)
    return list(calls)
