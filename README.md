# Day 10 – HisabDo AI Financial Assistant

## 📌 Project Overview

This project is a Proof of Concept (POC) for an AI Financial Assistant for HisabDo.

The chatbot allows users to ask financial questions in natural language and receive answers based on the provided financial data.

## 🎯 Objective

The objective is to demonstrate how Generative AI can be integrated into HisabDo to help users access their financial information through a conversational interface.

## 🤖 AI Feature

### AI Financial Assistant / Chatbot

The chatbot can answer questions such as:

- How much did I spend this month?
- Who owes me the most?
- How much does Ahmed owe me?
- What are my total receivables?
- What are my total payables?
- How much did I spend on transport?

## 🔄 Workflow

User Question
↓
FastAPI API
↓
Financial Data
↓
Gemini AI Model
↓
AI Generated Response
↓
User

# Day 11 – HisabDo AI Financial Assistant

## 📌 Project Overview

This project is an improved Proof of Concept (POC) of the HisabDo AI Financial Assistant developed for the Day 11 Capstone Project.

The chatbot allows users to ask questions about their financial information using natural language.

The Day 11 version improves the Day 10 prototype by:

- Using realistic application-style financial data
- Supporting multiple users
- Accepting user ID with each request
- Validating input
- Handling invalid users
- Handling incomplete requests
- Using Gemini API for AI responses
- Providing realistic financial use cases

---

# 🎯 Objective

The objective is to demonstrate how an AI chatbot can be integrated into HisabDo to help users interact with their financial data using natural language.

Example:

User:

> Who owes me the most?

AI:

> Ali Traders owes you PKR 45,000, which is the highest outstanding balance.

---

# 🤖 Selected AI Feature

## AI Financial Assistant / Chatbot

The selected feature is an AI-powered financial chatbot.

Users can ask questions about:

- Expenses
- Income
- Receivables
- Payables
- Customer balances
- Expense categories

The AI generates a response based on the user's financial data.

---

# 📥 Required Input Data Structure

The application sends two main fields to the API:

```json
{
    "user_id": "USR001",
    "question": "Who owes me the most?"
}

## 📥 Sample Input

```json
{
  "question": "How much did I spend this month?"
}
