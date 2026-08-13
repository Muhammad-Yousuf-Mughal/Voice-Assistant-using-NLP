import os
from pathlib import Path
from typing import List

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from groq import Groq
from pydantic import BaseModel

load_dotenv()

app = FastAPI(title="Aurora AI Voice Agent")

BASE_DIR = Path(__file__).resolve().parent

api_key = os.getenv("GROQ_API_KEY")
groq_client = Groq(api_key=api_key) if api_key else None


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: List[Message]


SYSTEM_PROMPT = (
    "You are Aurora, an ultra-fast, intelligent voice assistant. "
    "Provide very concise, natural, and friendly conversational responses (1 to 3 short sentences max) "
    "suitable for text-to-speech synthesis. Avoid markdown formatting, asterisks, bullet points, "
    "or code blocks as they sound unnatural when spoken."
)


@app.get("/", response_class=HTMLResponse)
async def serve_index():
    index_path = BASE_DIR / "index.html"
    if index_path.exists():
        return HTMLResponse(content=index_path.read_text(encoding="utf-8"))
    return HTMLResponse(content="<h1>index.html not found in root directory</h1>", status_code=404)


@app.post("/api/chat")
async def chat_endpoint(request: ChatRequest):
    if not groq_client:
        raise HTTPException(
            status_code=500,
            detail="GROQ_API_KEY is missing. Add it in Vercel Project Settings -> Environment Variables.",
        )

    try:
        formatted_messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        for msg in request.messages:
            formatted_messages.append({"role": msg.role, "content": msg.content})

        # Switched to llama-3.1-8b-instant for hyper-fast response latency
        completion = groq_client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=formatted_messages,
            temperature=0.6,
            max_tokens=150,
        )

        reply = completion.choices[0].message.content.strip()
        return {"response": reply}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
