# 🎯 AI Smart Assistant for Personal Organization

An intelligent personal digital assistant that leverages Artificial Intelligence (AI), Machine Learning (ML), and Natural Language Processing (NLP) to enhance daily organization and productivity workflows.

## 🔍 Overview

The AI Smart Assistant analyzes data from calendars, emails, and notes to provide smart daily plans, identify productive habits, and communicate naturally with users through an intuitive chatbot interface.

## 🧠 Core Features

### 1. Data Analysis & Organization
- Comprehensive analysis of calendars, emails, and notes
- Automatic detection of scheduled commitments, deadlines, and important contacts
- Intelligent event extraction from emails with automatic Google Calendar integration

### 2. Personalized Recommendations
- Dynamic daily plan generation based on user priorities
- Smart reminders, notifications, and optimal break time suggestions

### 3. Natural Language Interface
- Conversational AI chatbot for seamless user interaction
- Example: "What's my schedule for today?"

### 4. Productivity Analytics
- Time tracking across different activities
- Data-driven insights on peak productivity hours and patterns

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

## 🚧 Roadmap & Future Enhancements

- [ ] **Push Notifications** - Real-time alerts and reminders
- [ ] **Dark/Light Theme Toggle** - Enhanced user experience
- [ ] **Multi-user Support** - JWT authentication and user management
- [ ] **IoT Integration** - Smart home device connectivity
- [ ] **Offline Functionality** - Local data processing capabilities
- [ ] **Mobile Application** - React Native implementation
- [ ] **Advanced Analytics** - Machine learning-powered insights
- [ ] **Voice Commands** - Speech recognition integration

## 🤝 Contributing

We welcome contributions from the community! Please follow these guidelines:

### Development Process
1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add comprehensive AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request with detailed description

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