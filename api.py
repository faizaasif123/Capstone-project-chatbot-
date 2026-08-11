from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from chatbot import ask_ai


app = FastAPI(
    title="HisabDo AI Financial Assistant",
    description="Day 11 Capstone POC",
    version="2.0"
)


class ChatRequest(BaseModel):

    user_id: str = Field(
        ...,
        min_length=3,
        max_length=20
    )

    question: str = Field(
        ...,
        min_length=3,
        max_length=500
    )


@app.get("/")
def home():

    return {
        "message": "HisabDo AI Financial Assistant",
        "status": "running"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    try:

        answer = ask_ai(
            request.user_id,
            request.question
        )

        return {
            "user_id": request.user_id,
            "question": request.question,
            "answer": answer
        }

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )

    except Exception:

        raise HTTPException(
            status_code=500,
            detail="Unable to process the request."
        )