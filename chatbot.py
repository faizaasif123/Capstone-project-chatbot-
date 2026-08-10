import json
import os

from dotenv import load_dotenv
from google import genai


# Load environment variables
load_dotenv()

# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)


# Load financial data
with open("data/financial_data.json", "r") as file:
    financial_data = json.load(file)


def create_financial_context():

    return f"""
Business Name:
{financial_data["business"]["name"]}

Currency:
{financial_data["business"]["currency"]}

Monthly Income:
PKR {financial_data["summary"]["monthly_income"]}

Monthly Expenses:
PKR {financial_data["summary"]["monthly_expenses"]}

Receivables:
PKR {financial_data["summary"]["receivables"]}

Payables:
PKR {financial_data["summary"]["payables"]}

Customers:
{financial_data["customers"]}

Expenses:
{financial_data["expenses"]}
"""


def ask_ai(question):

    context = create_financial_context()

    prompt = f"""
You are an AI Financial Assistant for HisabDo.

Answer the user's question using ONLY the financial
information provided below.

Do not invent financial numbers.

If the requested information is not available,
say that the information is not available.

Keep your answer short and easy to understand.

Financial Data:
{context}

User Question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    return response.text