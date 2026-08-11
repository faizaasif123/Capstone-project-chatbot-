
---

# 3. `use_cases.md`

```markdown
# Day 11 – AI Financial Chatbot Use Cases

## Selected Feature

**AI Financial Assistant / Chatbot**

The chatbot allows HisabDo users to ask questions about their financial information in natural language.

---

# Use Case 1 – Monthly Expense Summary

## Problem

Users may need to manually check multiple expense records to determine their total monthly spending.

## AI Solution

The chatbot retrieves the user's expense information and provides the total amount through a natural-language response.

## Input

```json
{
    "user_id": "USR001",
    "question": "How much did I spend this month?"
}

Use Case 2 – Outstanding Customer Identification
Problem

A business owner may have multiple customers with outstanding balances and may not immediately know who owes the most.

AI Solution

The chatbot checks customer balances and identifies the customer with the highest outstanding amount.

Input
{
    "user_id": "USR001",
    "question": "Who owes me the most?"
}
Output
Ali Traders owes you PKR 45,000, which is the highest outstanding balance.
Value

This helps users quickly identify customers that require payment follow-up.

Use Case 3 – Expense Category Analysis
Problem

Users may want to know how much they spend on a specific category such as food, transport or utilities.

AI Solution

The chatbot retrieves the requested expense category and provides the corresponding amount.

Input
{
    "user_id": "USR001",
    "question": "How much did I spend on food?"
}
Output
You spent PKR 18,000 on food.
Value

This helps users understand their spending habits and identify areas where they may reduce expenses.
Additional Possible Use Cases
4. Receivable Summary

Question:

What are my total receivables?

The chatbot provides the total outstanding amount owed to the user.

5. Payable Summary

Question:

What are my total payables?

The chatbot provides the total amount the user needs to pay.

6. Financial Insights

Future version:

Where am I spending the most money?

The AI could analyze expense categories and provide a simple financial insight.
