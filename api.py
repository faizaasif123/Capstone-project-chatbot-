from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from chatbot import ask_ai


app = FastAPI(
    title="HisabDo AI Financial Assistant",
    description="Day 10 AI/ML Internship POC",
    version="1.0"
)


class ChatRequest(BaseModel):

    question: str = Field(
        ...,
        min_length=2,
        max_length=500
    )


@app.get("/")
def home():

    return {
        "message": "HisabDo AI Financial Assistant API",
        "status": "running"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    try:

        answer = ask_ai(
            request.question
        )

        return {
            "question": request.question,
            "answer": answer
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )