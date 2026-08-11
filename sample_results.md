# Day 11 – Sample Inputs and Outputs

## AI Financial Assistant POC

The following examples demonstrate how the **HisabDo AI Financial Assistant** processes application-style financial questions and generates responses using the sample financial dataset.

---

# Day 10 – Basic POC Results

## Test 1 – Monthly Expenses

### Input

```json
{
  "question": "How much did I spend this month?"
}
```

### Output

```json
{
  "question": "How much did I spend this month?",
  "answer": "Your total monthly expenses are PKR 45,000."
}
```

---

## Test 2 – Highest Outstanding Customer

### Input

```json
{
  "question": "Who owes me the most?"
}
```

### Output

```json
{
  "question": "Who owes me the most?",
  "answer": "Ahmed owes you PKR 35,000, which is the highest outstanding balance."
}
```

---

# Day 11 – Application-Style Results

Day 11 improves the chatbot by adding:

* User identification
* Realistic financial data
* Input validation
* Invalid user handling
* Incomplete input handling
* Multiple users

---

## Test 3 – Monthly Expense Summary

### Input

```json
{
  "user_id": "USR001",
  "question": "How much did I spend this month?"
}
```

### Output

```json
{
  "user_id": "USR001",
  "question": "How much did I spend this month?",
  "answer": "Your total monthly expenses are PKR 62,000."
}
```

---

## Test 4 – Highest Outstanding Customer

### Input

```json
{
  "user_id": "USR001",
  "question": "Who owes me the most?"
}
```

### Output

```json
{
  "user_id": "USR001",
  "question": "Who owes me the most?",
  "answer": "Ali Traders owes you PKR 45,000, which is the highest outstanding balance."
}
```

---

## Test 5 – Expense Category Analysis

### Input

```json
{
  "user_id": "USR001",
  "question": "How much did I spend on food?"
}
```

### Output

```json
{
  "user_id": "USR001",
  "question": "How much did I spend on food?",
  "answer": "You spent PKR 18,000 on food."
}
```

---

## Test 6 – Receivable Summary

### Input

```json
{
  "user_id": "USR001",
  "question": "What are my total receivables?"
}
```

### Output

```json
{
  "user_id": "USR001",
  "question": "What are my total receivables?",
  "answer": "Your total receivables are PKR 85,000."
}
```

---

## Test 7 – Payable Summary

### Input

```json
{
  "user_id": "USR001",
  "question": "What are my total payables?"
}
```

### Output

```json
{
  "user_id": "USR001",
  "question": "What are my total payables?",
  "answer": "Your total payables are PKR 30,000."
}
```

---

# Invalid Input Testing

## Test 8 – Invalid User ID

### Input

```json
{
  "user_id": "USR999",
  "question": "How much did I spend?"
}
```

### Output

```json
{
  "detail": "User ID not found."
}
```

### Result

The system correctly rejects the request because the user does not exist in the dataset.

---

## Test 9 – Missing Question

### Input

```json
{
  "user_id": "USR001"
}
```

### Result

The API rejects the request because the `question` field is required.

---

## Test 10 – Empty Question

### Input

```json
{
  "user_id": "USR001",
  "question": ""
}
```

### Result

The API rejects the request because the question does not meet the minimum length requirement.




