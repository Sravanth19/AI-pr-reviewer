import streamlit as st
from src.agent.reviewer import review_pr

st.set_page_config(page_title="AI PR Reviewer", layout="wide")

st.title("AI Pull Request Reviewer — Demo")
st.write("Paste a unified diff (git format-patch / `git diff`) for quick review.")

diff = st.text_area("PR diff", height=300)

top_k = st.slider("semantic search top-k", 1, 10, 3)

if st.button("Review PR"):
    if not diff.strip():
        st.error("Please paste a diff first.")
    else:
        with st.spinner("Running review..."):
            res = review_pr(diff, top_k=top_k)
        st.subheader("Static Issues (heuristics)")
        st.json(res.get("static_issues", []))
        st.subheader("LLM Review Output")
        st.code(res.get("llm_review", "No LLM output (maybe API key missing)"))
