import json
def format_review(raw_text, context, plan):
    # Try to parse JSON from model output, otherwise return raw text in a structure
    try:
        parsed = json.loads(raw_text)
        return parsed
    except Exception:
        return {'summary': 'LLM output (raw)', 'llm_text': raw_text, 'context_count': len(context), 'plan': plan}
