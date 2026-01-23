# Environment Variables Setup Guide

## Overview
This guide explains how to configure environment variables for the AI Smart Assistant application.

## Setup Instructions

### 1. Create .env File
Copy the `.env.example` file to create your own `.env` file:

```bash
cd backend
cp .env.example .env
```

### 2. Configure Google Cloud Credentials

1. **Get your Google Cloud credentials:**
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select existing one
   - Enable Google Calendar API and Gmail API
   - Create OAuth 2.0 credentials (Desktop application)
   - Download the JSON credentials file

2. **Place the credentials file:**
   - Save the downloaded JSON file to `backend/app/` directory
   - Update the `CREDENTIALS_FILE` variable in `.env` with the filename

3. **Update .env with your values:**
   ```env
   GOOGLE_CLIENT_ID=your_actual_client_id
   GOOGLE_CLIENT_SECRET=your_actual_client_secret
   CREDENTIALS_FILE=your_credentials_filename.json
   ```

### 3. Environment Variables Reference

#### Google Cloud API Configuration
- `GOOGLE_CLIENT_ID`: Your Google OAuth client ID
- `GOOGLE_CLIENT_SECRET`: Your Google OAuth client secret
- `CREDENTIALS_FILE`: Filename of your Google credentials JSON file
- `TOKEN_FILE`: Filename where OAuth tokens will be stored (default: token.json)

#### Google API Scopes
- `CALENDAR_SCOPE`: Permissions for Google Calendar access
- `GMAIL_SCOPE`: Permissions for Gmail access

#### Server Configuration
- `BACKEND_HOST`: Host address for the backend server (default: 0.0.0.0)
- `BACKEND_PORT`: Port for the backend server (default: 8080)
- `FRONTEND_URL`: URL of the frontend application (default: http://localhost:5173)

#### AI/ML Configuration
- `NLP_MODEL`: Transformer model for chatbot responses
- `NER_MODEL`: Model for Named Entity Recognition

#### Email Configuration
- `EMAIL_KEYWORDS`: Comma-separated keywords for filtering important emails

### 4. Using the New Configuration

To use the environment variables version of the application:

**Option 1: Replace main.py (Recommended)**
```bash
cd backend/app
mv main.py main_old.py
mv main_with_env.py main.py
```

**Option 2: Use directly with uvicorn**
```bash
cd backend
uvicorn app.main_with_env:app --reload --port 8080
```

### 5. Verify Setup

After configuration, verify the setup:

```bash
# Start backend
cd backend
uvicorn app.main:app --reload --port 8080

# In another terminal, test the API
curl http://localhost:8080/
```

Expected response:
```json
{"message": "Welcome to the AI-powered Smart Assistant API!"}
```

## Security Best Practices

1. **Never commit .env file to version control**
   - The `.env` file is already in `.gitignore`
   - Always use `.env.example` for templates

2. **Keep credentials secure**
   - Don't share your `.env` file
   - Don't share your Google credentials JSON file
   - Regularly rotate OAuth tokens

3. **Use different credentials for development and production**

## Troubleshooting

### Issue: "CREDENTIALS_FILE not found"
- Verify the credentials file path in `.env`
- Ensure the file is in the `backend/app/` directory

### Issue: "Invalid OAuth credentials"
- Check that GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET match your JSON file
- Regenerate credentials in Google Cloud Console if needed

### Issue: "Permission denied" errors
- Verify the SCOPES in `.env` match your Google Cloud project settings
- Delete `token.json` and re-authenticate

## Additional Notes

- The application will automatically create `token.json` after first OAuth authentication
- Email keywords can be customized in `.env` to match your needs
- Frontend URL can be updated for production deployment
