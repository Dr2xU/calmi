from src.chatbot import generate_response
from src.utils import log_debug

def chatbot_reply(message):
    """Returns chatbot response for a given user input."""
    log_debug(f"Processing input: {message}")
    return generate_response(message)
