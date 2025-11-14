from src.pr.diff_parser import parse_unified_diff

SAMPLE_DIFF = """
diff --git a/data/sample_repo/auth.py b/data/sample_repo/auth.py
index 000000..111111 100644
--- a/data/sample_repo/auth.py
+++ b/data/sample_repo/auth.py
@@ -1,3 +1,4 @@
 def login(user):
-    if not user:
-        return False
+    if not user:
+        return False
+    print("login called")
"""
def test_parse_diff():
    parsed = parse_unified_diff(SAMPLE_DIFF)
    assert isinstance(parsed, list)
    assert parsed[0]["path"].endswith("data/sample_repo/auth.py")
    assert any("login called" in "".join(h["added"]) for h in parsed[0]["hunks"])
