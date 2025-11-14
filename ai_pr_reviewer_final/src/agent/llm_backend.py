import os, requests, json
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
GROQ_API_KEY = os.environ.get('GROQ_API_KEY')
GROQ_API_URL = os.environ.get('GROQ_API_URL')

def call_groq(prompt, max_tokens=512, temperature=0.0):
    if not (GROQ_API_KEY and GROQ_API_URL):
        raise RuntimeError('Groq not configured')
    headers = {'Authorization': f'Bearer {GROQ_API_KEY}', 'Content-Type': 'application/json'}
    payload = {'prompt': prompt, 'max_tokens': max_tokens, 'temperature': temperature}
    r = requests.post(GROQ_API_URL, headers=headers, json=payload, timeout=30)
    r.raise_for_status()
    data = r.json()
    # try common fields
    if 'choices' in data and data['choices']:
        return data['choices'][0].get('text') or data['choices'][0].get('output') or json.dumps(data['choices'][0])
    if 'output' in data:
        return data['output']
    return json.dumps(data)

def call_openai(prompt, max_tokens=512, temperature=0.0):
    if not OPENAI_API_KEY:
        raise RuntimeError('OpenAI not configured')
    import openai
    openai.api_key = OPENAI_API_KEY
    resp = openai.ChatCompletion.create(model='gpt-4o-mini', messages=[{'role':'user','content':prompt}], max_tokens=max_tokens, temperature=temperature)
    try:
        return resp.choices[0].message.get('content','')
    except Exception:
        return resp.choices[0].text

def generate_review_from_llm(prompt, max_tokens=512, temperature=0.0):
    # prefer Groq if configured
    if GROQ_API_KEY and GROQ_API_URL:
        try:
            return call_groq(prompt, max_tokens=max_tokens, temperature=temperature)
        except Exception as e:
            print('Groq call failed:', e)
    if OPENAI_API_KEY:
        try:
            return call_openai(prompt, max_tokens=max_tokens, temperature=temperature)
        except Exception as e:
            print('OpenAI call failed:', e)
    return '[LLM not configured]'
