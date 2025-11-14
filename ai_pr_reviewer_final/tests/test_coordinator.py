from src.agent.coordinator import review_pr_text

def test_review_stub():
    res = review_pr_text({'diff': 'def a():\n    pass'})
    assert isinstance(res, dict)
