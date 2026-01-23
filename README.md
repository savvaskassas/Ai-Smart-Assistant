# AI Smart Assistant - README

## Contents

1. [Additional Assumptions and Deviations](#additional-assumptions-and-deviations)
2. [Technologies Used](#technologies-used)
3. [Description of Constructed Files](#description-of-constructed-files)
4. [Database Description](#database-description)
5. [System Execution Guide](#system-execution-guide)
6. [System Usage Guide (with examples)](#system-usage-guide-with-examples)
7. [References](#references)

---

## Additional Assumptions and Deviations

- The project is structured for both local testing and scalable deployment.
- OAuth2 setup is required for Google Calendar and Gmail integration.
- All AI/ML processing is performed server-side using Python.
- The system supports both English and Greek language processing.
- No user authentication/JWT by default (planned as enhancement).
- Development and production environments are separated for clear setup.
- Auto-scroll and tooltips implemented for enhanced UX.
- Responsive design supports both mobile and desktop interfaces.

---

## Technologies Used

- **Backend:** Python 3.8+, FastAPI, Hugging Face Transformers, spaCy, scikit-learn, dateparser
- **Frontend:** React + Vite, Material-UI (v7), Material Icons, @emotion/styled
- **APIs:** Google Calendar API, Gmail API (OAuth2)
- **AI/ML:** Named Entity Recognition (NER), text classification, date extraction
- **Other:** RESTful API, CORS middleware, regex patterns, multilingual support

---

## Description of Constructed Files

### Backend Structure

#### `/backend/app/main.py`
- Main FastAPI application entry point
- Defines all API endpoints and routes
- Handles CORS middleware configuration
- Manages Google Calendar and Gmail OAuth2 integration

#### `/backend/app/utils.py`
- Utility functions for Google API authentication
- OAuth2 credential management
- API service initialization helpers

#### `/backend/app/nlp/nlp_engine.py`
- Core NLP processing engine
- Text classification and generation
- Hugging Face transformer model integration
- Multilingual text processing

#### `/backend/app/nlp/ner.py`
- Named Entity Recognition implementation
- spaCy model integration for entity extraction
- Custom entity processing and filtering

#### `/backend/app/productivity/analyzer.py`
- Productivity metrics calculation
- Event categorization logic
- Statistical analysis of calendar data
- AI-powered recommendation generation

#### `/backend/app/scheduler/scheduler.py`
- Smart scheduling algorithm
- Free time detection
- Task optimization and allocation
- Daily plan generation

#### `/backend/requirements.txt`
- Python dependencies list
- Package versions for reproducibility

### Frontend Structure

#### `/frontend/src/App.jsx`
- Main React application component
- Layout and routing management
- Component orchestration

#### `/frontend/src/main.jsx`
- Application entry point
- React DOM rendering
- Global providers setup

#### `/frontend/src/ThemeContext.jsx`
- Theme management context
- Dark/Light mode toggle logic
- Material-UI theme configuration

#### `/frontend/src/components/Chatbot.jsx`
- Interactive chatbot UI component
- Message handling and display
- API integration for chat functionality

#### `/frontend/src/components/Calendar.jsx`
- Calendar events display component
- Event loading and rendering
- Integration with Google Calendar API

#### `/frontend/src/components/ProductivityChart.jsx`
- Data visualization component
- Recharts integration for analytics
- Interactive charts and graphs

#### `/frontend/package.json`
- Node.js dependencies
- Build scripts and configuration

#### `/frontend/vite.config.js`
- Vite build tool configuration
- Development server settings

### Configuration Files

#### `/backend/ENV_SETUP.md`
- Environment setup documentation
- Configuration instructions

#### `/.gitignore`
- Git ignore patterns
- Excludes sensitive files and dependencies

#### `/LICENSE`
- MIT License text
- Copyright and usage terms

---

## Database Description

This application currently uses **Google Calendar** and **Gmail** as external data sources rather than a traditional database. All persistent data is stored in the user's Google account.

### Data Storage Architecture

#### Google Calendar API
- **Primary Data Store**: Calendar events with metadata
- **Event Properties**: title, start time, end time, description, location, attendees
- **Access Method**: OAuth2 authenticated REST API
- **Data Scope**: Read and write access to user's calendar events

#### Gmail API
- **Data Source**: User's email messages
- **Access Type**: Read-only access
- **Filtering**: Keyword-based email scanning for event extraction
- **Data Processing**: NLP-based date and event information extraction

### In-Memory Processing

- **Session Data**: OAuth2 tokens stored locally during runtime
- **Cache**: Temporary storage of API responses for performance
- **Analytics**: Calculated metrics stored transiently for dashboard display

### Future Database Considerations

For enhanced functionality, a traditional database could be added to support:
- User profiles and authentication (JWT-based)
- Custom task management separate from calendar
- Historical analytics and trend tracking
- Offline data caching
- User preferences and settings

**Potential Database Solutions:**
- **SQLite** - For local development and simple deployments
- **PostgreSQL** - For production with advanced features
- **MongoDB** - For flexible schema and document storage

---

## System Execution Guide

### Prerequisites Check

Before running the system, ensure all prerequisites are installed:

```bash
# Check Python version
python --version  # Should be 3.8+

# Check Node.js version
node --version    # Should be 16.0+

# Check npm version
npm --version
```

### Step-by-Step Execution

#### Step 1: Clone and Navigate to Project
```bash
git clone https://github.com/your-username/ai-smart-assistant.git
cd ai-smart-assistant
```

#### Step 2: Backend Setup and Execution

**A. Create Virtual Environment**
```bash
cd backend
python -m venv venv
```

**B. Activate Virtual Environment**

*Windows:*
```bash
venv\Scripts\activate
```

*macOS/Linux:*
```bash
source venv/bin/activate
```

**C. Install Dependencies**
```bash
pip install -r requirements.txt
```

**D. Configure Google Cloud Credentials**
1. Download your OAuth2 credentials JSON file from Google Cloud Console
2. Place it in the `backend/app/` directory
3. Ensure the filename matches the one referenced in your code

**E. Start Backend Server**
```bash
uvicorn app.main:app --reload --port 8080
```

**Expected Output:**
```
INFO:     Uvicorn running on http://127.0.0.1:8080 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

#### Step 3: Frontend Setup and Execution

**A. Open New Terminal and Navigate to Frontend**
```bash
cd frontend
```

**B. Install Node Dependencies**
```bash
npm install
```

**C. Start Development Server**
```bash
npm run dev
```

**Expected Output:**
```
VITE v5.x.x  ready in xxx ms

➜  Local:   http://localhost:5173/
➜  Network: use --host to expose
```

#### Step 4: Access the Application

1. Open your web browser
2. Navigate to `http://localhost:5173`
3. The application should load with the chatbot interface

#### Step 5: First-Time OAuth Authentication

When you first use features requiring Google API access:

1. Click on "Show Calendar Events" or use email features
2. A browser window will open for Google OAuth consent
3. Sign in with your Google account
4. Grant the requested permissions
5. You'll be redirected back to the application
6. A `token.json` file will be created in `backend/app/` for future use

### Troubleshooting Common Issues

**Backend won't start:**
- Verify Python version: `python --version`
- Check if port 8080 is available: `netstat -an | findstr 8080` (Windows) or `lsof -i :8080` (macOS/Linux)
- Ensure all dependencies installed: `pip list`

**Frontend won't start:**
- Clear npm cache: `npm cache clean --force`
- Delete `node_modules` and reinstall: `rm -rf node_modules && npm install`
- Check Node.js version compatibility

**OAuth2 Errors:**
- Verify credentials file is in correct location
- Check Google Cloud Console for enabled APIs
- Ensure redirect URI matches in Google Cloud Console
- Delete `token.json` and re-authenticate

**Module Import Errors:**
- Activate virtual environment before running backend
- Reinstall problematic package: `pip install --force-reinstall package-name`

### Stopping the Application

**Backend:**
- Press `CTRL+C` in the terminal running uvicorn
- Deactivate virtual environment: `deactivate`

**Frontend:**
- Press `CTRL+C` in the terminal running Vite

---

## System Usage Guide (with examples)

### Getting Started

Once both backend and frontend servers are running, follow these usage examples:

### 1. Chatbot Interaction

#### Example 1: General Query
**User Input:**
```
Hello! What can you help me with?
```

**Expected Response:**
```
Hello! I'm your AI Smart Assistant. I can help you with:
- Managing your Google Calendar
- Analyzing your productivity
- Planning your day
- Extracting important information from emails
- Answering questions about your schedule
```

#### Example 2: Schedule Query
**User Input:**
```
What's on my schedule today?
```

**Action:** Click "Show Calendar Events" button first to load your calendar data.

**Expected Response:**
```
Based on your calendar, here are today's events:
- 9:00 AM: Team Meeting
- 2:00 PM: Project Review
- 4:30 PM: One-on-one with Manager
```

#### Example 3: Productivity Query
**User Input:**
```
How productive was I this week?
```

**Action:** The system will analyze your calendar events and provide insights.

**Expected Response:**
```
Your productivity analysis:
- Total events: 24
- Meetings: 12 (50%)
- Focus time: 8 (33%)
- Peak hours: 10 AM - 12 PM
- Recommendation: Try to schedule deep work during morning hours
```

### 2. Calendar Management

#### Loading Calendar Events

**Steps:**
1. Click the "Show Calendar Events" button in the interface
2. If first time, authenticate with Google account
3. View events displayed in the calendar component

**Example Output:**
```
Upcoming Events (Next 30 Days):

📅 January 24, 2026
  • 10:00 AM - 11:00 AM: Sprint Planning
  • 3:00 PM - 4:00 PM: Client Call

📅 January 25, 2026
  • 9:00 AM - 10:30 AM: Code Review Session
  • 2:00 PM - 3:00 PM: Department Meeting
```

#### Email-to-Calendar Integration

**Steps:**
1. Click "Scan Emails for Events" button
2. System analyzes recent emails for keywords: meeting, deadline, appointment, etc.
3. Review detected events
4. Click "Add to Calendar" to import

**Example Scenario:**

*Email Subject:* "Project Deadline - January 30"
*Email Body:* "Please submit the final report by January 30, 2026, 5:00 PM."

**System Detection:**
```json
{
  "event": "Project Deadline",
  "date": "2026-01-30",
  "time": "17:00",
  "source": "email",
  "confidence": "high"
}
```

**Result:** Event automatically added to Google Calendar with reminder

### 3. Day Planning

#### Generate Daily Plan

**Steps:**
1. Click "Generate Day Plan" button
2. System analyzes your calendar and free time
3. View AI-generated schedule recommendations

**Example Output:**
```
🌅 Your Optimized Day Plan for January 24, 2026

7:00 AM - 8:00 AM: Morning routine & breakfast
8:00 AM - 10:00 AM: 🎯 Deep Work Block (High focus task)
10:00 AM - 11:00 AM: Sprint Planning Meeting
11:00 AM - 12:00 PM: 🎯 Deep Work Block
12:00 PM - 1:00 PM: ☕ Lunch Break
1:00 PM - 3:00 PM: 🎯 Deep Work Block
3:00 PM - 4:00 PM: Client Call
4:00 PM - 5:00 PM: Email processing & admin tasks
5:00 PM - 6:00 PM: Exercise & personal time

💡 Productivity Score: 8.5/10
💡 Free time available: 4 hours
💡 Recommendation: Your morning is ideal for complex tasks!
```

### 4. Productivity Analytics

#### View Productivity Insights

**Steps:**
1. Click "Productivity Insights" button
2. System analyzes recent calendar history
3. View interactive charts and statistics

**Example Dashboard:**

**Summary Cards:**
```
📊 Total Events: 156 (last 30 days)
⏰ Average per Day: 5.2 events
🎯 Most Productive Hour: 10:00 AM
📈 Productivity Score: 7.8/10
```

**Time Allocation (Pie Chart):**
- Meetings: 45%
- Focus Time: 30%
- Breaks: 15%
- Deadlines: 10%

### 5. Advanced Features

#### Named Entity Recognition

**Example Input:**
```
I need to meet with John Smith from Microsoft next Tuesday at their Seattle office to discuss the Azure integration project.
```

**System Extraction:**
```json
{
  "persons": ["John Smith"],
  "organizations": ["Microsoft"],
  "locations": ["Seattle"],
  "dates": ["next Tuesday"],
  "projects": ["Azure integration"]
}
```

#### Multilingual Support

**Greek Example:**
**Input:** "Έχω συνάντηση την Παρασκευή στις 3 το απόγευμα"
**Translation:** "I have a meeting on Friday at 3 PM"

**System Detection:**
```json
{
  "event_type": "meeting",
  "day": "Friday",
  "time": "15:00",
  "language": "Greek"
}
```

### 6. Theme Customization

**Steps:**
1. Locate the theme toggle button (🌙/☀️) in the top navigation
2. Click to switch between Dark and Light modes
3. Theme preference is saved automatically

**Dark Mode Benefits:**
- Reduced eye strain in low-light environments
- Better contrast for charts and data visualization
- Battery saving on OLED screens

### 7. Error Handling Examples

#### Scenario: No Internet Connection

**User Action:** Try to load calendar events

**System Response:**
```
❌ Unable to connect to Google Calendar
🔄 Please check your internet connection and try again
```

#### Scenario: Invalid OAuth Token

**User Action:** Access calendar after token expiration

**System Response:**
```
🔐 Authentication expired
➡️ Redirecting to Google login...
```

### 8. Best Practices

**For Optimal Performance:**
- Load calendar events at the start of each session
- Run email scan during off-peak hours (fewer API calls)
- Review day plan in the morning
- Check productivity insights weekly
- Keep browser tab active for real-time updates

**For Better AI Responses:**
- Use specific questions: "What meetings do I have tomorrow?" instead of "Schedule?"
- Provide context: "Based on my calendar, when should I schedule a 2-hour deep work block?"
- Use natural language: The chatbot understands conversational queries

---

## 💡 Usage Guide

### Chatbot Interface
1. **Natural Conversation**: Type messages to interact with the AI assistant
2. **Calendar Queries**: Ask about your schedule, appointments, and events
3. **Task Management**: Get help organizing your daily workflow

### Smart Features
1. **Calendar Events**: Click the button to load and display your Google Calendar events
2. **Day Planning**: Generate AI-powered daily schedules based on your commitments
3. **Productivity Insights**: Access detailed analytics about your time usage patterns
4. **Email-to-Calendar**: Automatically detect important events in emails and add them to your calendar

### Supported Natural Language Queries
- "What's my schedule for today?"
- "Show me my upcoming meetings"
- "When is my next deadline?"
- "Analyze my productivity this week"

## 
5. **Google Calendar API**
   - URL: https://developers.google.com/calendar
   - Used for: Calendar event management, OAuth2 authentication

6. **Gmail API**
   - URL: https://developers.google.com/gmail/api
   - Used for: Email access, message parsing, event extraction

### AI/ML Libraries

7. **Hugging Face Transformers**
   - URL: https://huggingface.co/docs/transformers
   - Used for: Pre-trained NLP models, text generation, classification
   - Models Used: GPT-2, BERT variants

8. **spaCy**
   - URL: https://spacy.io/
   - Used for: Named Entity Recognition, linguistic analysis
   - Models: `en_core_web_sm`, `el_core_news_sm` (Greek)

9. **scikit-learn**
   - URL: https://scikit-learn.org/
   - Used for: Machine learning algorithms, data preprocessing

10. **dateparser**
    - URL: https://dateparser.readthedocs.io/
    - Used for: Natural language date extraction, multilingual date parsing

### Data Visualization

11. **Recharts**
    - URL: https://recharts.org/
    - Used for: React charts, productivity visualizations

### Python Packages

12. **Uvicorn**
    - URL: https://www.uvicorn.org/
    - Used for: ASGI server, FastAPI deployment

13. **Google API Python Client**
    - URL: https://github.com/googleapis/google-api-python-client
    - Used for: Google API authentication and communication

### Development Tools

14. **Git**
    - URL: https://git-scm.com/
    - Used for: Version control, collaboration

15. **npm**
    - URL: https://www.npmjs.com/
    - Used for: JavaScript package management

### Research Papers & Articles

16. **BERT: Pre-training of Deep Bidirectional Transformers**
    - Devlin et al., 2018
    - Used for: Understanding transformer architecture

17. **Attention Is All You Need**
    - Vaswani et al., 2017
    - Used for: Transformer model foundation

### Tutorials & Guides

18. **FastAPI Tutorial - OAuth2 with Password and Bearer**
    - URL: https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
    - Used for: Authentication patterns (future enhancement)

19. **React Context API Guide**
    - URL: https://react.dev/learn/passing-data-deeply-with-context
    - Used for: Theme management implementation

20. **Material-UI Theme Customization**
    - URL: https://mui.com/material-ui/customization/theming/
    - Used for: Dark/Light mode implementation

### Community Resources

21. **Stack Overflow**
    - URL: https://stackoverflow.com/
    - Used for: Troubleshooting, community solutions

22. **GitHub Discussions**
    - Various repositories for FastAPI, React, spaCy
    - Used for: Feature discussions, best practices

### Standards & Specifications

23. **OAuth 2.0 Specification**
    - URL: https://oauth.net/2/
    - Used for: Google API authentication

24. **RESTful API Design**
    - URL: https://restfulapi.net/
    - Used for: API architecture patterns

25. **JSON Schema**
    - URL: https://json-schema.org/
    - Used for: API request/response validation

### Additional Resources

26. **PEP 8 -- Style Guide for Python Code**
    - URL: https://peps.python.org/pep-0008/
    - Used for: Python code style standards

27. **ESLint Configuration**
    - URL: https://eslint.org/
    - Used for: JavaScript/React code quality

28. **CORS (Cross-Origin Resource Sharing)**
    - URL: https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
    - Used for: Handling cross-origin requests

---

**Built with ❤️ for enhanced personal organization and productivity**