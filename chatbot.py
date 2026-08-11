import json
import os

from dotenv import load_dotenv
from google import genai


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


# Load application-style financial data
with open("data/users_financial_data.json", "r") as file:
    financial_data = json.load(file)


def get_user_data(user_id):

    for user in financial_data["users"]:

        if user["user_id"] == user_id:
            return user

    return None


def create_financial_context(user):

    return f"""
User:
{user["name"]}

Currency:
{user["currency"]}

Monthly Income:
PKR {user["summary"]["monthly_income"]}

Monthly Expenses:
PKR {user["summary"]["monthly_expenses"]}

Receivables:
PKR {user["summary"]["receivables"]}

Payables:
PKR {user["summary"]["payables"]}

Customers:
{user["customers"]}

Expenses:
{user["expenses"]}
"""


def ask_ai(user_id, question):

    user = get_user_data(user_id)

    if user is None:
        raise ValueError("User ID not found.")

    context = create_financial_context(user)

    prompt = f"""
You are an AI Financial Assistant for HisabDo.

Answer the user's question using ONLY the provided
financial information.

Do not invent financial numbers.

If the requested information is unavailable,
clearly tell the user that the information is not available.

Keep the answer short, clear and useful.

Financial Information:
{context}

User Question:
{question}
"""

    response = client.models.generate_content(
       model="gemini-flash-latest",
        contents=prompt
    )

    return response.text