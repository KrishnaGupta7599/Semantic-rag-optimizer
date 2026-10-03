# 01 — Project Setup

## What are we building?

We are building a Semantic RAG Optimizer.

The system will eventually:

- Answer questions using RAG
- Cache similar questions using semantic similarity
- Route questions to different LLMs based on complexity
- Track cost and latency

## Project Structure

```text
Semantic-Rag/
├── app/
│   └── main.py
├── docs/
├── venv/
├── .gitignore
└── requirements.txt

## FastAPI Server

We use Uvicorn to run our FastAPI application.

```bash
uvicorn app.main:app --reload

API Endpoints
GET /

Checks whether the API is running.

POST /ask

Accepts a question and currently returns the same question.