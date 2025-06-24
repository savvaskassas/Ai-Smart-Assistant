from fastapi import FastAPI, Request
from pydantic import BaseModel
from app.nlp.nlp_engine import get_chat_response
from app.nlp.ner import extract_entities

app = FastAPI(
    title="AI-powered Smart Assistant Backend",
    description="API for a personal AI assistant focused on organization and productivity"
)

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI-powered Smart Assistant API!"}

@app.post("/chat/")
async def chat_endpoint(request: ChatRequest):
    response = get_chat_response(request.message)
    return {"response": response}

@app.post("/extract-entities/")
async def extract_entities_endpoint(request: Request):
    data = await request.json()
    text = data.get("text")
    entities = extract_entities(text)
    return {"entities": entities}