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

## 🛠️ Technology Stack

### Backend Architecture
- **Python** - FastAPI framework for high-performance APIs
- **AI/ML** - Hugging Face Transformers, spaCy NLP, scikit-learn, PyTorch
- **Cloud APIs** - Google Calendar API, Gmail API with OAuth2 authentication
- **Data Processing** - Advanced date/time extraction and entity recognition

### Frontend Stack
- **React** - Modern JavaScript framework with Vite build tool
- **Material-UI** - Professional component library with responsive design
- **Material Icons** - Comprehensive icon system
- **RESTful API Integration** - Seamless backend communication

### AI/ML Pipeline
- **Named Entity Recognition (NER)** - Intelligent text analysis
- **Text Generation** - Natural language processing and classification
- **Multi-language Support** - English and Greek language processing
- **Date Extraction** - Advanced temporal information extraction using spaCy, regex, and dateparser

## � Prerequisites

- **Python** 3.8 or higher
- **Node.js** 16.0 or higher
- **Google Cloud Console** account with API access
- **Git** for version control

## 🚀 Installation

### 1. Repository Setup
```bash
git clone https://github.com/your-username/ai-smart-assistant.git
cd ai-smart-assistant
```

### 2. Backend Configuration
```bash
cd backend
python -m venv venv

# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Google Cloud API Setup
1. Navigate to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the following APIs:
   - Google Calendar API
   - Gmail API
4. Create OAuth2 credentials (Desktop application type)
5. Download the JSON credentials file
6. Place the file in the `backend/app/` directory

### 4. Frontend Dependencies
```bash
cd frontend
npm install
```

## 🏃‍♂️ Running the Application

### Start Backend Server
```bash
cd backend
uvicorn app.main:app --reload --port 8080
```
Server will be available at `http://localhost:8080`

### Start Frontend Development Server
```bash
cd frontend
npm run dev
```
Application will be available at `http://localhost:5173`

## 📋 API Documentation

### Natural Language Processing
- `POST /chat/` - Interactive chatbot conversation endpoint
- `POST /extract-entities/` - Extract named entities from text input

### Google Calendar Integration
- `GET /calendar/events` - Retrieve calendar events for next 30 days
- `GET /emails/important-and-add` - Analyze emails and auto-create calendar events

### Productivity Analytics
- `GET /day-plan` - Generate personalized daily schedule
- `GET /productivity-insights` - Comprehensive productivity metrics and analytics

### API Response Format
All endpoints return JSON responses with consistent error handling and status codes.

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

## 🔧 Advanced Configuration

### Environment Variables
Create a `.env` file in the backend directory:
```bash
GOOGLE_CLIENT_ID=your_client_id
GOOGLE_CLIENT_SECRET=your_client_secret
CALENDAR_SCOPE=https://www.googleapis.com/auth/calendar
GMAIL_SCOPE=https://www.googleapis.com/auth/gmail.readonly
```

### Customization Options
- **Keywords**: Modify email filtering keywords in `backend/app/main.py`
- **UI Theme**: Customize Material-UI theme in `frontend/src/`
- **Language Support**: Extend multi-language support in NLP modules

## ✨ Recently Implemented Features

### Version 2.0.0 - January 2026

- ✅ **Dark/Light Theme Toggle** - Complete theme switching system with Material-UI integration
  - React Context API for theme management
  - Adaptive colors for all components including charts
  - Toggle button with smooth transitions
  
- ✅ **Advanced Analytics Dashboard** - Interactive data visualization with Recharts
  - Bar charts for hourly activity distribution
  - Pie charts for time allocation analysis
  - Summary cards with key productivity metrics
  - Responsive design for all screen sizes
  
- ✅ **Smart Scheduling Engine** - Intelligent daily planning algorithm
  - Free time block detection and optimization
  - Deep work session recommendations
  - Productivity score calculation
  - Automated task scheduling suggestions
  
- ✅ **Email-to-Calendar Integration** - Automatic event creation from emails
  - Smart email scanning with keyword filtering
  - NLP-powered date extraction (multilingual)
  - One-click event import to Google Calendar
  - Real-time feedback and debug information
  
- ✅ **Context-Aware Chatbot** - Enhanced AI assistant with intelligent responses
  - Keyword-based query understanding
  - Calendar and productivity-specific answers
  - Multilingual support (English/Greek)
  - Feature discovery and help system
  
- ✅ **Comprehensive Productivity Analyzer** - ML-powered insights
  - Event categorization (meetings, focus time, breaks, deadlines)
  - Statistical analysis with mean/median calculations
  - Peak productivity hours detection
  - AI-generated recommendations
  - Weekly trend analysis
  
- ✅ **Environment Variables Support** - Secure configuration management
  - `.env.example` template for easy setup
  - Flexible deployment options
  - Security best practices documentation

## 🚧 Roadmap & Future Enhancements

- [ ] **Push Notifications** - Real-time alerts and reminders
- [ ] **Multi-user Support** - JWT authentication and user management
- [ ] **IoT Integration** - Smart home device connectivity
- [ ] **Offline Functionality** - Local data processing capabilities
- [ ] **Mobile Application** - React Native implementation
- [ ] **Voice Commands** - Speech recognition integration

### Code Standards
- Follow PEP 8 for Python code
- Use ESLint configuration for JavaScript/React
- Include comprehensive tests for new features
- Update documentation for API changes

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for complete details.

## � Development Team

- **[@savvaskassas](https://github.com/savvaskassas)** - Lead Developer & Project Architect

## 🙏 Acknowledgments

- **Hugging Face** - Pre-trained transformer models and NLP infrastructure
- **Google** - Calendar and Gmail API services
- **Material-UI Team** - Comprehensive React component library
- **React & FastAPI Communities** - Framework development and support
- **spaCy** - Advanced natural language processing capabilities

## 📞 Support & Contact

For questions, feature requests, or technical support:
- **Issues**: Open a GitHub issue with detailed information
- **Discussions**: Use GitHub Discussions for community questions
- **Documentation**: Refer to inline code documentation and API specs

---

**Built with ❤️ for enhanced personal organization and productivity**