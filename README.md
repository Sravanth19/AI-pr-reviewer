# 🤖 AI-PR-Reviewer v1.0

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-brightgreen)

> "Human speed. Machine accuracy."

AI-PR-Reviewer is an autonomous humanoid reviewer unit, engineered to scan, analyze, and interpret code with machine precision and cognitive reasoning.

It operates as a multi-agent LLM system, built to support engineering teams by reducing review time, detecting hidden issues, and elevating code quality to production-grade levels.

## 🧠 System Purpose

Modern development moves fast — codebases grow, PRs expand, and human reviewers overlook patterns due to fatigue or context overload. This system is designed to step in exactly where humans slow down.

My core directive:
* Understand code changes
* Detect issues across logic, security, and performance
* Retrieve related files using embeddings
* Produce clean, readable, structured feedback
* Help you ship safer, better code — faster

---

## 🦾 Core Capabilities

### 🔍 1. Autonomous Code Analysis
I break down your pull request and evaluate:
* Logic correctness
* Architectural consistency
* Clean code practices
* Anti-patterns and code smells
* Missing edge cases
* Error-prone areas

### 🛡️ 2. Security Intelligence Module
My scanner identifies:
* Unsafe inputs
* Possible injections
* Weak crypto usage
* Secrets left in code
* Permission flaws

### ⚡ 3. Performance Optimization Engine
I flag:
* High-complexity loops
* Unnecessary computations
* Non-optimal patterns
* Expensive operations

### 🧭 4. Agent-Driven Reasoning
My thought pipeline includes:
* **Planner Agent** – maps review steps
* **Retriever Agent** – fetches related files via FAISS vector search
* **Reviewer Agent** – performs deep reasoning
* **Formatter Agent** – assembles final structured output

### 💬 5. Clear, Human-Friendly Output
I transform internal reasoning into:
* Issue list
* Suggestions
* Severity classification
* Summary
* Final verdict (approve / minor changes / major changes)

All formatted professionally for engineers.

---

## 🏗️ System Architecture

```bash
ai-pr-reviewer/
│
├── app/
│   ├── api/             # Entry API routes
│   ├── reviewers/       # LLM-based review agents
│   ├── services/        # PR processing logic
│   ├── vector_store/    # FAISS embeddings store
│   ├── models/          # Pydantic schemas
│   └── utils/           # Helpers
│
├── ui/                  # Streamlit frontend
├── tests/               # Automated test suite
└── docs/                # Full documentation
```

---

## ⚙️ Execution Protocols

### Backend Activation
```bash
cd backend
pip install -r requirements.txt
uvicorn app.api.main:app --reload
```
**Accessible at:** `http://localhost:8000`

### Frontend Activation
```bash
cd frontend
npm install
npm run dev
```
**UI Dashboard at:** `http://localhost:5173`

### 🐳 Docker Autonomous Boot Mode
```bash
docker-compose build
docker-compose up
```
Your system runs as two independent humanoid modules:
* `api_unit` → Code analysis
* `ui_unit` → Interface control

---

## 🔁 Sample Interaction

**User Input:** A pull request diff + changed files.

**My Response (`application/json`):**
```json
{
  "summary": "This PR modifies the authentication layer...",
  "issues": [
    {
      "type": "security",
      "severity": "high",
      "message": "JWT verification missing audience check."
    }
  ],
  "suggestions": ["Add claim validation for aud, iss, exp."],
  "verdict": "needs_major_changes"
}
```

---

## 🚀 Why This Project Matters

This project demonstrates expertise in:
* LLM expertise
* RAG & retrieval systems
* Multi-agent reasoning
* API development
* Frontend engineering
* AI workflow orchestration
* Clean coding & architecture

It is exactly aligned with roles like:
* ✔ Applied AI Engineer
* ✔ AI Agent Systems
* ✔ LLM Infrastructure
* ✔ AI-powered Developer Tools
* ✔ Engineering Productivity

---

## 🤝 Contribution Protocol

1.  **Fork** the repository.
2.  Create your feature branch (`git checkout -b feature/AmazingFeature`).
3.  **Commit** your changes (`git commit -m 'Add some AmazingFeature'`).
4.  **Push** to the branch (`git push origin feature/AmazingFeature`).
5.  Open a **Pull Request** for human + AI review.

---

## 🧬 System Identity

**AI-PR-Reviewer v1.0**
* Designed for new-generation engineering teams.
* Optimized for accuracy, speed, and collaboration.
* Built by **Sravanth** — engineered for the future.
