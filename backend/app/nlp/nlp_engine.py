from transformers import pipeline
import re
from datetime import datetime

# Initialize the NLP pipeline (e.g., conversational model)
nlp = pipeline("text-generation", model="facebook/blenderbot-400M-distill")

def get_chat_response(user_message: str, calendar_context=None) -> str:
    """
    Generate intelligent chat responses with context awareness.
    
    Args:
        user_message: User's input message
        calendar_context: Optional calendar events for context
    
    Returns:
        Contextual response string
    """
    if not user_message:
        return "Please provide a message."
    
    user_message_lower = user_message.lower()
    
    # Calendar-related queries
    if any(keyword in user_message_lower for keyword in ['schedule', 'calendar', 'events', 'meetings', 'appointments', 
                                                          'ημερολόγιο', 'ραντεβού', 'συναντήσεις', 'πρόγραμμα']):
        return "I can help you with your calendar! Click the 'Calendar Events' button to load your schedule, or 'Day Plan' for a personalized daily plan. 📅"
    
    # Productivity queries
    if any(keyword in user_message_lower for keyword in ['productivity', 'insights', 'analytics', 'performance',
                                                          'παραγωγικότητα', 'απόδοση', 'στατιστικά']):
        return "Want to see your productivity insights? Click the 'Productivity Insights' button to analyze your time usage patterns and get detailed metrics! 📊"
    
    # Email-related queries
    if any(keyword in user_message_lower for keyword in ['email', 'mail', 'inbox', 'messages',
                                                          'email', 'μήνυμα', 'εισερχόμενα']):
        return "I can scan your important emails and automatically add events to your calendar! Just click the '📧 Email → Calendar' button. ✉️"
    
    # Time-related queries
    if any(keyword in user_message_lower for keyword in ['today', 'tomorrow', 'week', 'time', 'when',
                                                          'σήμερα', 'αύριο', 'εβδομάδα', 'πότε']):
        now = datetime.now()
        return f"Today is {now.strftime('%A, %B %d, %Y')}. Use 'Day Plan' to see your schedule for today! 🕐"
    
    # Help queries
    if any(keyword in user_message_lower for keyword in ['help', 'what can you do', 'features', 'capabilities',
                                                          'βοήθεια', 'τι μπορείς', 'δυνατότητες']):
        return """I'm your AI Smart Assistant! Here's what I can do:

📅 **Calendar Management** - View and manage your Google Calendar events
📧 **Email Integration** - Automatically add important email events to calendar
📊 **Productivity Analytics** - Track and analyze your time usage
🗓️ **Daily Planning** - Get optimized daily schedules
💬 **Natural Conversation** - Ask me anything about your schedule!

Use the buttons below to access these features!"""
    
    # Greeting
    if any(keyword in user_message_lower for keyword in ['hello', 'hi', 'hey', 'γεια', 'καλημέρα', 'καλησπέρα']):
        return "Hello! 👋 I'm your AI Smart Assistant. I can help you manage your calendar, analyze productivity, and organize your day. How can I assist you today?"
    
    # Thank you
    if any(keyword in user_message_lower for keyword in ['thank', 'thanks', 'ευχαριστώ']):
        return "You're welcome! Happy to help! 😊"
    
    # Default: Use the transformer model for general conversation
    try:
        response = nlp(user_message, max_length=100, num_return_sequences=1)
        return response[0]['generated_text'] if response else "I'm here to help with your calendar and productivity! Ask me about your schedule or use the buttons below."
    except Exception as e:
        return "I'm your AI assistant focused on calendar management and productivity. How can I help you today? Try asking about your schedule or clicking one of the buttons below!"