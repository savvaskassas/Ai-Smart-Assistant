from transformers import pipeline

# Initialize the NLP pipeline (e.g., conversational model)
nlp = pipeline("text-generation", model="facebook/blenderbot-400M-distill")

def get_chat_response(user_message: str) -> str:
    if not user_message:
        return "Please provide a message."
    response = nlp(user_message)
    return response[0]['generated_text'] if response else "Sorry, I didn't understand. Could you repeat?"