def simple_hardcoded_check(code: str):
    """
    Very simple heuristic security checks:
    - Look for 'password' or 'secret' string matches in code
    - Look for use of eval()
    Returns list of issues.
    """
    issues = []
    lowered = code.lower()
    if "password" in lowered or "secret" in lowered:
        issues.append("Potential hardcoded credential string found.")
    if "eval(" in code:
        issues.append("Use of eval() detected — ensure safe usage.")
    if "subprocess" in code and "shell=True" in code:
        issues.append("subprocess(shell=True) may be unsafe.")
    return issues
