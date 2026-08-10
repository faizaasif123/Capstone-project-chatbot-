
---

# `architecture.md`

```markdown
# Day 10 – AI Financial Assistant Architecture

## 1. Overview

The HisabDo AI Financial Assistant is a Generative AI-based chatbot that allows users to ask questions about their financial information using natural language.

The current implementation is a Proof of Concept using sample financial data stored in JSON.

---

## 2. System Architecture

```text
                    ┌──────────────┐
                    │     USER     │
                    └──────┬───────┘
                           │
                           │ Natural Language Question
                           ▼
                ┌──────────────────────┐
                │  HisabDo Application │
                │  Web / Mobile App    │
                └──────────┬───────────┘
                           │
                           │ HTTP POST
                           ▼
                ┌──────────────────────┐
                │       FastAPI        │
                │      /chat API       │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │   Question +         │
                │ Financial Context    │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │    Gemini API        │
                │   Generative AI      │
                └──────────┬───────────┘
                           │
                           │ AI Response
                           ▼
                ┌──────────────────────┐
                │      FastAPI         │
                │    JSON Response     │
                └──────────┬───────────┘
                           │
                           ▼
                    ┌──────────────┐
                    │     USER     │
                    └──────────────┘
