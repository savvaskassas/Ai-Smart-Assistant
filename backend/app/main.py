from fastapi import FastAPI, Request
from app.nlp.nlp_engine.py import get_chat_response

app = FastAPI(
    title="AI-powered Smart Assistant Backend",
    description="API για προσωπικό AI βοηθό οργάνωσης"
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI-powered Smart Assistant API!"}

@app.post("/chat/")
async def chat_endpoint(request: Request):
    data = await request.json()
    user_message = data.get("message")
    response = get_chat_response(user_message)
    return {"response": response}