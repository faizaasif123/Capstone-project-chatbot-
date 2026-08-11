
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


---


```markdown
# Day 11 – AI Financial Assistant Architecture

## 1. Overview

The HisabDo AI Financial Assistant is a Generative AI chatbot that allows users to ask questions about their financial data using natural language.

The Day 11 version improves the Day 10 prototype by introducing:

- Application-style input
- Multiple users
- User-specific financial data
- Input validation
- Invalid input handling
- Gemini AI integration
- Structured API responses

---

# 2. Main Architecture

```text
┌───────────────┐
│     USER      │
└───────┬───────┘
        │
        │ Question
        ▼
┌──────────────────────┐
│ HisabDo Web/Mobile   │
│ Application          │
└──────────┬───────────┘
           │
           │ HTTP Request
           ▼
┌──────────────────────┐
│ FastAPI Backend      │
│ POST /chat           │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Input Validation     │
│ Pydantic             │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ User Data Retrieval  │
│ JSON Dataset         │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Financial Context    │
│ + User Question      │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Google Gemini API    │
│ Generative AI        │
└──────────┬───────────┘
           │
           │ AI Response
           ▼
┌──────────────────────┐
│ FastAPI JSON         │
│ Response             │
└──────────┬───────────┘
           │
           ▼
┌───────────────┐
│     USER      │
└───────────────┘
