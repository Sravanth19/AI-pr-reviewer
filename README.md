project:
  name: "AI PR Reviewer"
  description: |
    # AI PR Reviewer
    AI-powered pull request reviewer that analyzes code, detects issues,
    retrieves related files using embeddings, and produces structured
    intelligent review comments.

sections:

  overview:
    problem_statement: |
      ## 🚨 Problem Statement
      Reviewing pull requests is slow, inconsistent, and requires deep context
      across the codebase. Developers often miss bugs, performance issues,
      or logical errors due to time pressure or large diffs.

    solution: |
      ## ✅ Solution
      **AI PR Reviewer** automates code analysis using LLMs + vector search.
      It provides summaries, issue detection, security checks, suggestions,
      and intelligent insights.

    audience:
      - "AI/ML Students"
      - "Backend Developers"
      - "Full-Stack Developers"
      - "Companies building developer tools"

  features:
    - "**🔍 LLM-based PR Analysis** — summary, issues, suggestions"
    - "**🧠 Multi-Agent Review System** — planner, retriever, reviewer, formatter"
    - "**📁 FAISS Vector Search** for related code retrieval"
    - "**⚡ FastAPI Backend** with clean REST API"
    - "**🎨 Streamlit Frontend UI**"
    - "**🐳 Docker Support**"
    - "**🧪 Unit Tests Included**"

  architecture:
    diagram: |
      ## 🏗️ Project Architecture

      ai-pr-reviewer/
      ├── app/
      │   ├── api/
      │   ├── services/
      │   ├── reviewers/
      │   ├── utils/
      │   ├── models/
      │   └── vector_store/
      ├── ui/
      ├── tests/
      ├── docker-compose.yml
      ├── Dockerfile
      └── README.md

    components:
      backend: "FastAPI"
      frontend: "Streamlit"
      vector_db: "FAISS"
      embeddings: "Sentence Transformers / OpenAI"
      orchestrator: "Multi-Agent LLM Pipeline"

  workflow:
    step_1_user_uploads_pr: |
      ### 1️⃣ User Uploads PR
      A PR diff + changed files are sent to backend.

    step_2_embedding_retrieval: |
      ### 2️⃣ Retrieve Context Files
      FAISS vector store finds related code segments.

    step_3_agentic_review: |
      ### 3️⃣ Multi-Agent LLM Processing
      - Planner Agent  
      - Retriever Agent  
      - Reviewer Agent  
      - Formatter Agent  

    step_4_output_rendered: |
      ### 4️⃣ Streamlit UI Shows Results
      - Summary  
      - Issues  
      - Suggestions  
      - Final verdict  

  api_documentation:
    base_url: "http://localhost:8000"
    endpoints:
      - path: "/review"
        method: "POST"
        description: "Analyze PR diff and files."
        request_body:
          diff: "Unified diff text"
          files:
            - path: "string"
              content: "string"
        response:
          summary: "LLM-generated overview"
          issues: "Detected bugs, smells, risks"
          suggestions: "Fixes and improvements"
          verdict: "approve | minor_changes | major_changes"

  agent_architecture:
    planner_agent: |
      ## 🧭 Planner Agent
      Determines what needs deeper analysis.

    retriever_agent: |
      ## 📚 Retriever Agent
      Searches vector DB for related files.

    reviewer_agent: |
      ## 🧪 Reviewer Agent
      Performs code-level reasoning on:
      - correctness
      - security
      - performance
      - best practices

    formatter_agent: |
      ## 📝 Formatter Agent
      Outputs clean JSON results.

  review_logic:
    checks:
      bugs:
        - "Undefined variables"
        - "Incorrect logic"
        - "Missing edge cases"
      security:
        - "SQL injection risks"
        - "Hardcoded secrets"
        - "Unsafe user input"
      performance:
        - "Nested loops"
        - "Unnecessary computations"
      architecture:
        - "SOLID violations"
        - "Poor abstractions"
      final_verdict:
        - "Approve"
        - "Needs Minor Fixes"
        - "Needs Major Fixes"

  setup:
    prerequisites:
      - "Python 3.10+"
      - "pip"
      - "Docker (optional)"
    manual_installation:
      - "pip install -r requirements.txt"
    run_backend:
      - "uvicorn app.api.main:app --reload"
    run_ui:
      - "streamlit run ui/Home.py"

  docker:
    build:
      - "docker-compose build"
    run:
      - "docker-compose up"
    services:
      api: "Runs on http://localhost:8000"
      ui: "Runs on http://localhost:8501"

  testing:
    run_tests:
      - "pytest -q"
    test_coverage:
      - "API tests"
      - "Agent workflow tests"
      - "FAISS retrieval tests"
      - "Prompt tests"

  folder_explanation:
    app/api: "API route handlers"
    app/services: "Core logic"
    app/reviewers: "LLM agents"
    app/utils: "Helpers"
    app/models: "Pydantic schemas"
    app/vector_store: "FAISS storage"
    ui: "Frontend UI"
    tests: "All unit tests"

  deployment:
    methods:
      - "Render"
      - "Railway"
      - "AWS EC2"
      - "Fly.io"
    ui_hosting:
      - "Streamlit Cloud"

  future_scope:
    - "GitHub App integration"
    - "Auto code-fix patch generation"
    - "Semantic diff viewer"
    - "Slack notifications"
    - "Multi-agent LangGraph"

  contribution_guide:
    steps:
      - "Fork the repo"
      - "Create feature branch"
      - "Commit changes"
      - "Push and open PR"
    code_style:
      - "Use black formatter"
      - "Good commit messages"
      - "Add tests for new code"
