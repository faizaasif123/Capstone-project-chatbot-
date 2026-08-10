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

## 📥 Sample Input

```json
{
  "question": "How much did I spend this month?"
}
