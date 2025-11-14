from fastapi import FastAPI, Request, Header, HTTPException
from fastapi.responses import JSONResponse
from src.agent.coordinator import review_pr_text
import os

app = FastAPI(title="AI PR Reviewer API")

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/review")
async def review_endpoint(request: Request):
    body = await request.json()
    diff = body.get("diff") or body.get("code") or body.get("files")
    if not diff:
        raise HTTPException(status_code=400, detail="No diff/code/files provided in request body")
    result = review_pr_text(body)
    return JSONResponse(content=result)

# Simple GitHub webhook endpoint (for GitHub App simulation)
@app.post("/webhook/github")
async def github_webhook(request: Request, x_hub_signature: str = Header(None)):
    payload = await request.json()
    # For simplicity, just accept payload and trigger a review if diff present
    diff = payload.get("diff") or payload.get("patch")
    if not diff:
        return {"status": "ignored", "message": "no diff in payload"}
    result = review_pr_text({"diff": diff})
    return JSONResponse(content={"status": "reviewed", "result": result})
