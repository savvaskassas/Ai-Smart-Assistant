from fastapi import FastAPI, Request
from pydantic import BaseModel
from app.nlp.nlp_engine import get_chat_response
from app.nlp.ner import extract_entities
from fastapi.middleware.cors import CORSMiddleware
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os

app = FastAPI(
    title="AI-powered Smart Assistant Backend",
    description="API for a personal AI assistant focused on organization and productivity"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
CREDENTIALS_FILE = os.path.join(os.path.dirname(__file__), 'client_secret_633312370488-b6gjg118flkj05a0c8ni44p611hs53q5.apps.googleusercontent.com.json')
TOKEN_FILE = os.path.join(os.path.dirname(__file__), 'token.json')

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

@app.get("/calendar/events")
def get_calendar_events():
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())
    service = build('calendar', 'v3', credentials=creds)
    events_result = service.events().list(
        calendarId='primary', maxResults=10, singleEvents=True,
        orderBy='startTime', timeMin=None).execute()
    events = events_result.get('items', [])
    return {"events": events}