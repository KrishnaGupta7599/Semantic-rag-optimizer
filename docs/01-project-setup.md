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