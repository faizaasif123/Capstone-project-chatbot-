# Day 11 – AI Financial Chatbot Use Cases

## Selected Feature

**AI Financial Assistant / Chatbot**

The chatbot allows HisabDo users to ask questions about their financial information using natural language.

---

## Use Case 1 – Monthly Expense Summary

### Problem

Users may need to manually check multiple expense records to determine their total monthly spending.

### AI Solution

The chatbot retrieves the user's expense information and provides the total amount through a natural-language response.

### Input

```json
{
  "user_id": "USR001",
  "question": "How much did I spend this month?"
}
```

### Output

```text
Your total monthly expenses are PKR 62,000.
```

### Value

This provides users with quick access to their monthly spending without manually calculating expenses.

---

## Use Case 2 – Outstanding Customer Identification

### Problem

A business owner may have multiple customers with outstanding balances and may not immediately know who owes the most.

### AI Solution

The chatbot checks customer balances and identifies the customer with the highest outstanding amount.

### Input

```json
{
  "user_id": "USR001",
  "question": "Who owes me the most?"
}
```

### Output

```text
Ali Traders owes you PKR 45,000, which is the highest outstanding balance.
```

### Value

This helps users quickly identify customers who require payment follow-up.

---

## Use Case 3 – Expense Category Analysis

### Problem

Users may want to know how much they spend on a specific category such as food, transport, or utilities.

### AI Solution

The chatbot retrieves the requested expense category and provides the corresponding amount.

### Input

```json
{
  "user_id": "USR001",
  "question": "How much did I spend on food?"
}
```

### Output

```text
You spent PKR 18,000 on food.
```

### Value

This helps users understand their spending habits and identify areas where they may reduce expenses.

---

# Additional Possible Use Cases

## 4. Receivable Summary

### Example Question

```text
What are my total receivables?
```

### AI Function

The chatbot provides the total outstanding amount owed to the user.

### Example Output

```text
Your total receivables are PKR 85,000.
```

---

## 5. Payable Summary

### Example Question

```text
What are my total payables?
```

### AI Function

The chatbot provides the total amount the user needs to pay.

### Example Output

```text
Your total payables are PKR 30,000.
```

---

## 6. Financial Insights

### Example Question

```text
Where am I spending the most money?
```

### AI Function

The future version of the chatbot can analyze expense categories and provide simple financial insights.

### Example Output

```text
Your highest expense category is Food, with spending of PKR 18,000.
```

---

# Use Case Summary

| # | Use Case                | Example User Question            | Expected AI Output            |
| - | ----------------------- | -------------------------------- | ----------------------------- |
| 1 | Monthly Expense Summary | How much did I spend this month? | Total monthly expenses        |
| 2 | Customer Balance        | Who owes me the most?            | Customer with highest balance |
| 3 | Expense Category        | How much did I spend on food?    | Food expense amount           |
| 4 | Receivable Summary      | What are my total receivables?   | Total receivables             |
| 5 | Payable Summary         | What are my total payables?      | Total payables                |
| 6 | Financial Insights      | Where am I spending the most?    | Highest spending category     |

---

# Future Improvements

The AI Financial Chatbot can be extended to support:

* Budget recommendations
* Spending predictions
* Automated financial reports
* Payment reminders
* Financial alerts
* Voice-based queries
* Urdu and Roman Urdu queries
* Personalized financial insights
* Integration with the real HisabDo database

---

# Conclusion

The three primary use cases demonstrate how the AI chatbot can provide practical value to HisabDo users by allowing them to interact with their financial information using natural language.

The current POC uses sample financial data. In the production version, the chatbot can be connected to the authenticated user's real financial records through the HisabDo backend and database.
