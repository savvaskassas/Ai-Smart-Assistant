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

## System Usage Guide 

### Main Features

**1. Chatbot Interface**
- Natural conversation with AI assistant
- Calendar queries about schedule and appointments
- Task management and workflow organization

**2. Calendar Management**
- Load and display Google Calendar events
- First-time OAuth authentication required
- View upcoming events for next 30 days

**3. Email-to-Calendar Integration**
- Scan emails for event-related keywords
- Automatic date and time extraction using NLP
- One-click import to Google Calendar

**4. Day Planning**
- AI-generated daily schedule recommendations
- Free time block detection
- Productivity score calculation
- Deep work session suggestions

**5. Productivity Analytics**
- Interactive charts and statistics
- Event categorization (meetings, focus time, breaks, deadlines)
- Peak productivity hours analysis
- Time allocation insights

**6. Advanced Features**
- Named Entity Recognition (NER) for extracting persons, organizations, locations, dates
- Multilingual support (English and Greek)
- Theme customization (Dark/Light mode)
- Real-time error handling and authentication

### Best Practices

**For Optimal Performance:**
- Load calendar events at the start of each session
- Run email scan during off-peak hours
- Review day plan in the morning
- Check productivity insights weekly

**For Better AI Responses:**
- Use specific questions instead of vague queries
- Provide context when asking for recommendations
- Use natural language - the chatbot understands conversational queries

---

## References
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
