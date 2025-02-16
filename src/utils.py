import logging
import os
import json
from datetime import datetime

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

def log_to_json(filename, log_data):
    """Logs data in JSON format."""
    file_path = os.path.join("logs", filename)
    with open(file_path, "a", encoding="utf-8") as log_file:
        log_file.write(json.dumps(log_data, ensure_ascii=False) + "\n")

# Setup error logging
error_logger = logging.getLogger("error_logger")
error_logger.setLevel(logging.ERROR)
error_handler = logging.FileHandler("logs/error.json")
error_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
error_logger.addHandler(error_handler)

def log_error(message):
    """Logs an error message to error.json in JSON format"""
    log_data = {"timestamp": datetime.now().isoformat(), "level": "ERROR", "message": message}
    log_to_json("error.json", log_data)
    error_logger.error(message)

# Setup chatbot interaction logging
chat_logger = logging.getLogger("chat_logger")
chat_logger.setLevel(logging.INFO)
chat_handler = logging.FileHandler("logs/chatbot.json")
chat_handler.setFormatter(logging.Formatter("%(asctime)s - USER: %(message)s"))
chat_logger.addHandler(chat_handler)

def log_chat(user_input, bot_response):
    """Logs user queries and chatbot responses to chatbot.json in JSON format"""
    log_data = {"timestamp": datetime.now().isoformat(), "user": user_input, "bot": bot_response}
    log_to_json("chatbot.json", log_data)
    chat_logger.info(f"User: {user_input} | Bot: {bot_response}")

# Setup debug logging
debug_logger = logging.getLogger("debug_logger")
debug_logger.setLevel(logging.DEBUG)
debug_handler = logging.FileHandler("logs/debug.json")
debug_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
debug_logger.addHandler(debug_handler)

def log_debug(message):
    """Logs debug messages to debug.json in JSON format"""
    log_data = {"timestamp": datetime.now().isoformat(), "level": "DEBUG", "message": message}
    log_to_json("debug.json", log_data)
    debug_logger.debug(message)
