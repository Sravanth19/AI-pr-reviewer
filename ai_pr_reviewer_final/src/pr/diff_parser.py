import re
from typing import List, Dict

def parse_unified_diff(diff_text: str) -> List[Dict]:
    """
    Very small parser for unified diff format.
    Returns list of changed hunks with metadata and new code lines.
    """
    files = []
    cur_file = None
    cur_hunk = None
    for line in diff_text.splitlines():
        if line.startswith("+++ ") or line.startswith("--- "):
            # skip original markers
            continue
        if line.startswith("diff ") or line.startswith("Index: "):
            if cur_file:
                files.append(cur_file)
            cur_file = {"path": None, "hunks": []}
            cur_hunk = None
            continue
        m = re.match(r"\+\+\+ b/(.+)", line)
        if m:
            if not cur_file:
                cur_file = {"path": m.group(1), "hunks": []}
            else:
                cur_file["path"] = m.group(1)
            continue
        if line.startswith("@@"):
            # new hunk header
            cur_hunk = {"header": line, "added": [], "removed": []}
            if cur_file is None:
                cur_file = {"path": None, "hunks": []}
            cur_file["hunks"].append(cur_hunk)
            continue
        if cur_hunk is None:
            continue
        if line.startswith("+") and not line.startswith("+++"):
            cur_hunk["added"].append(line[1:])
        elif line.startswith("-") and not line.startswith("---"):
            cur_hunk["removed"].append(line[1:])
        else:
            # context lines or others
            pass
    if cur_file:
        files.append(cur_file)
    return files
