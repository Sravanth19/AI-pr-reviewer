from src.agent.llm_backend import generate_review_from_llm

def generate_review(text: str, context, plan):
    # Build prompt
    prompt = 'You are an expert code reviewer.\n'
    prompt += 'Goals: ' + ','.join(plan.get('goals',[])) + '\n'
    prompt += '\nDIFF/INPUT:\n' + text[:4000] + '\n'
    prompt += '\nCONTEXT:\n'
    for c in context[:5]:
        prompt += f"--- file: {c.get('file')} ---\n" + c.get('code','')[:2000] + '\n'
    # Call LLM backend
    resp = generate_review_from_llm(prompt, max_tokens=800, temperature=0.0)
    return resp
