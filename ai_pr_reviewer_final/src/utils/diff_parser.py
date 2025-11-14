import re
def parse_unified_diff(diff_text: str):
    files=[]; cur=None; hunk=None
    for line in diff_text.splitlines():
        if line.startswith('+++ b/'):
            path=line[6:]
            cur={'path':path,'hunks':[]}
            files.append(cur)
        elif line.startswith('@@'):
            hunk={'header':line,'added':[],'removed':[]}
            cur['hunks'].append(hunk)
        elif hunk is not None:
            if line.startswith('+') and not line.startswith('+++'):
                hunk['added'].append(line[1:])
            elif line.startswith('-') and not line.startswith('---'):
                hunk['removed'].append(line[1:])
    return files
