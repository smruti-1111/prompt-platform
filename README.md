# Prompt Evaluation Platform (Local LLM)

A FastAPI-based platform to design, version, and evaluate prompts using a local LLM (Phi-3 via Ollama). It focuses on improving reliability of structured outputs for classification tasks.

## 🚀 Features

- Prompt versioning (`v1`, `v2`, etc.)
- Local LLM inference using Ollama (Phi-3)
- Structured JSON output validation (Pydantic)
- Robust JSON extraction for messy LLM responses
- Dataset-driven evaluation
- Metrics: accuracy, JSON success rate, latency
- Result logging for reproducibility

---

## 🧠 Architecture
API → Prompt → Dataset → Phi-3 → JSON Extraction → Validation → Evan->results
## ⚙️ Setup

### 1. Install Ollama & run model
```bash
ollama pull phi3
ollama run phi3

##Install dependencies
pip install fastapi uvicorn requests pydantic

##Run server
uvicorn app.main:app --reload --port 8001

##Run evaluation
curl "http://localhost:8001/evaluate/classification_v1"

Example output

{
  "accuracy": 0.83,
  "json_success_rate": 1.0,
  "avg_latency": 0.4
}

##project structure
app/
  main.py
  evaluator.py
  llm.py
  prompt_manager.py
  schemas.py
  utils.py

prompts/
data/
results/
