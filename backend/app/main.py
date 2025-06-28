from fastapi import FastAPI, Request
from pydantic import BaseModel
from app.nlp.nlp_engine import get_chat_response
from app.nlp.ner import extract_entities
from datetime import datetime, timedelta
from fastapi.middleware.cors import CORSMiddleware
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from base64 import urlsafe_b64decode
from email import message_from_bytes
from email.header import decode_header
from google.auth.transport.requests import Request as GoogleRequest
import os
import spacy
import dateparser
import re

app = FastAPI(
    title="AI-powered Smart Assistant Backend",
    description="API for a personal AI assistant focused on organization and productivity"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

SCOPES = [
    'https://www.googleapis.com/auth/calendar.readonly',
    'https://www.googleapis.com/auth/calendar.events',
    'https://www.googleapis.com/auth/gmail.readonly'
]
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
            creds.refresh(GoogleRequest())
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

@app.get("/emails/important")
def get_important_emails():
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(GoogleRequest())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())
    service = build('gmail', 'v1', credentials=creds)
    results = service.users().messages().list(userId='me', maxResults=20, q='is:important').execute()
    messages = results.get('messages', [])
    important_emails = []
    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id'], format='raw').execute()
        raw_msg = urlsafe_b64decode(msg_data['raw'].encode('ASCII'))
        email_msg = message_from_bytes(raw_msg)
        subject = email_msg['Subject']
        from_ = email_msg['From']
        payload = email_msg.get_payload(decode=True)
        body = payload.decode(errors='ignore') if payload else ''
        # Εδώ μπορείς να βάλεις NLP/NER extraction ημερομηνιών
        # και να φιλτράρεις τα σημαντικά emails
        important_emails.append({
            'subject': subject,
            'from': from_,
            'body': body
        })
    return {'important_emails': important_emails}

# Load spaCy English model
try:
    nlp_spacy = spacy.load("en_core_web_sm")
except:
    import os
    os.system("python -m spacy download en_core_web_sm")
    nlp_spacy = spacy.load("en_core_web_sm")

def extract_dates(text):
    # spaCy NER
    doc = nlp_spacy(text)
    dates = [ent.text for ent in doc.ents if ent.label_ == "DATE"]
    # Regex patterns
    regex_dates = re.findall(r"\b\d{1,2}/\d{1,2}/\d{2,4}\b|\b\d{4}-\d{2}-\d{2}\b|\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{1,2}, \d{4}\b", text)
    dates.extend(regex_dates)
    # Parse dates to standard format
    parsed = []
    for d in dates:
        dt = dateparser.parse(d, languages=["en", "el"])
        if dt:
            parsed.append(dt.strftime("%Y-%m-%d"))
    # Αν δεν βρέθηκε ημερομηνία, ψάξε για μέρες (ελληνικά/αγγλικά)
    if not parsed:
        days_map = {
            'σαββατο': 5, 'σάββατο': 5, 'saturday': 5,
            'κυριακη': 6, 'κυριακή': 6, 'sunday': 6,
            'δευτερα': 0, 'δευτέρα': 0, 'monday': 0,
            'τριτη': 1, 'τρίτη': 1, 'tuesday': 1,
            'τεταρτη': 2, 'τετάρτη': 2, 'wednesday': 2,
            'πεμπτη': 3, 'πέμπτη': 3, 'thursday': 3,
            'παρασκευη': 4, 'παρασκευή': 4, 'friday': 4
        }
        text_lower = text.lower()
        for day_word, day_num in days_map.items():
            if day_word in text_lower:
                today = datetime.now().date()
                days_ahead = (day_num - today.weekday() + 7) % 7
                if days_ahead == 0:
                    days_ahead = 7
                next_day = today + timedelta(days=days_ahead)
                parsed.append(next_day.strftime("%Y-%m-%d"))
                break
    return list(set(parsed))

@app.get("/emails/important-and-add")
def get_important_emails_and_add_events():
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(GoogleRequest())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())
    gmail_service = build('gmail', 'v1', credentials=creds)
    calendar_service = build('calendar', 'v3', credentials=creds)
    # Gmail query: important OR from specific sender
    query = 'is:important OR from:no-reply@aristarchus.ds.unipi.gr'
    results = gmail_service.users().messages().list(userId='me', maxResults=20, q=query).execute()
    messages = results.get('messages', [])
    added_events = []
    debug_info = []
    for msg in messages:
        msg_data = gmail_service.users().messages().get(userId='me', id=msg['id'], format='raw').execute()
        raw_msg = urlsafe_b64decode(msg_data['raw'].encode('ASCII'))
        email_msg = message_from_bytes(raw_msg)
        # Decode subject
        subject_raw = email_msg['Subject']
        if subject_raw:
            decoded_parts = decode_header(subject_raw)
            subject = ''.join([
                part.decode(enc or 'utf-8') if isinstance(part, bytes) else part
                for part, enc in decoded_parts
            ])
        else:
            subject = ''
        from_ = email_msg['From']
        payload = email_msg.get_payload(decode=True)
        body = payload.decode(errors='ignore') if payload else ''
        # Extract dates with spaCy, regex, dateparser
        found_dates = extract_dates(subject + ' ' + body)
        debug_info.append({'subject': subject, 'from': from_, 'body': body, 'found_dates': found_dates})
        for date_str in found_dates:
            event = {
                'summary': f"Important: {subject}",
                'description': body,
                'start': {'date': date_str},
                'end': {'date': date_str}
            }
            created_event = calendar_service.events().insert(calendarId='primary', body=event).execute()
            added_events.append({'email_subject': subject, 'event_id': created_event['id'], 'date': date_str})
    return {'added_events': added_events, 'debug_info': debug_info}

@app.get("/day-plan")
def get_day_plan():
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(GoogleRequest())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())
    service = build('calendar', 'v3', credentials=creds)
    now = datetime.utcnow().isoformat() + 'Z'
    end_of_day = (datetime.utcnow().replace(hour=23, minute=59, second=59)).isoformat() + 'Z'
    events_result = service.events().list(
        calendarId='primary', timeMin=now, timeMax=end_of_day, singleEvents=True,
        orderBy='startTime').execute()
    events = events_result.get('items', [])
    plan = []
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        summary = event.get('summary', 'No Title')
        plan.append(f"{start}: {summary}")
    if not plan:
        plan.append("No scheduled events for today. You may want to focus on personal tasks or take a break.")
    return {"day_plan": plan}