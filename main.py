import os
from pathlib import Path
from typing import List

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from groq import Groq
from pydantic import BaseModel

load_dotenv()

app = FastAPI(title="AI Voice Agent")

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
STATIC_DIR.mkdir(exist_ok=True)

app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

api_key = os.getenv("GROQ_API_KEY")
groq_client = Groq(api_key=api_key) if api_key else None


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
    index_path = STATIC_DIR / "index.html"
    if not index_path.exists():
        raise HTTPException(status_code=404, detail="static/index.html not found")
    return FileResponse(index_path)


@app.post("/api/chat")
async def chat_endpoint(request: ChatRequest):
    if not groq_client:
        raise HTTPException(
            status_code=500,
            detail="GROQ_API_KEY environment variable is missing on Vercel settings.",
        )

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
