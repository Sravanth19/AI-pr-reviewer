from fastapi import FastAPI, Request, Header
from src.agent.reviewer import review_pr
import json

app = FastAPI()

# Simple webhook to accept PR diff payload (for learning/demo)
@app.post("/webhook/pr")
async def pr_webhook(request: Request, x_github_event: str = Header(None)):
    """
    Expects JSON payload with keys:
    - 'diff' (string): unified diff text
    - 'action' (optional): opened/synced, etc.
    """
    payload = await request.json()
    diff_text = payload.get("diff") or payload.get("patch") or payload.get("unified_diff") or ""
    if not diff_text:
        return {"error": "no diff found in payload"}

    result = review_pr(diff_text)
    return {"status": "reviewed", "result": result}
