import os
from typing import List

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from groq import Groq
from pydantic import BaseModel

load_dotenv()

app = FastAPI(title="AI Voice Agent")

os.makedirs("static", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY environment variable is missing.")

groq_client = Groq(api_key=api_key)


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: List[Message]


SYSTEM_PROMPT = (
    "You are an interactive, intelligent voice assistant. "
    "Provide clear, concise, and conversational responses suitable for text-to-speech synthesis. "
    "Avoid using markdown symbols like asterisks, bolding, bullet points, or code blocks that sound unnatural when spoken aloud."
)


@app.get("/")
async def serve_index():
    return FileResponse("static/index.html")


@app.post("/api/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        formatted_messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        for msg in request.messages:
            formatted_messages.append({"role": msg.role, "content": msg.content})

        completion = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=formatted_messages,
            temperature=0.7,
            max_tokens=250,
        )

        reply = completion.choices[0].message.content.strip()
        return {"response": reply}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
