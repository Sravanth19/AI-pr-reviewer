def plan_review(text: str):
    # Simple planner: detect goals based on keywords
    goals = []
    if 'security' in text.lower() or 'password' in text.lower():
        goals.append('security')
    goals.append('logic')
    goals.append('style')
    return {'goals': goals, 'text': text}
