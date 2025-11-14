from typing import Dict, Any
from src.agent.planner import plan_review
from src.agent.retriever import retrieve_context
from src.agent.reviewer import generate_review
from src.agent.formatter import format_review

def review_pr_text(payload: Dict[str, Any]) -> Dict[str, Any]:
    # payload can contain 'diff' or 'code' or 'files' list
    text = payload.get('diff') or payload.get('code') or ''
    plan = plan_review(text)
    context = retrieve_context(text, top_k=5)
    raw = generate_review(text, context, plan)
    result = format_review(raw, context, plan)
    return result
