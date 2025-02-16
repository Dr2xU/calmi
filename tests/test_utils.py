import pytest # type: ignore
import os
import json
from src.utils import log_chat, log_error, log_debug

def test_log_chat():
    """Test chat logging"""
    try:
        user_input = "Hello!"
        bot_response = "Hi, how can I assist you?"

        log_chat(user_input, bot_response)

        assert os.path.exists("logs/chatbot.json")

        with open("logs/chatbot.json", "r", encoding="utf-8") as log_file:
            lines = log_file.readlines()
            last_entry = json.loads(lines[-1]) if lines else {}
            assert last_entry.get("user") == user_input
            assert last_entry.get("bot") == bot_response

        log_debug("Test Passed: Chat log entry recorded successfully.")
    except Exception as e:
        log_error(f"Test Failed: Chat logging error - {str(e)}")
        assert False, f"Chat log failed: {str(e)}"

def test_log_error():
    """Test error logging"""
    try:
        error_message = "Test error logging"
        log_error(error_message)

        assert os.path.exists("logs/error.json")

        with open("logs/error.json", "r", encoding="utf-8") as log_file:
            lines = log_file.readlines()
            last_entry = json.loads(lines[-1]) if lines else {}
            assert last_entry.get("message") == error_message

        log_debug("Test Passed: Error log entry recorded successfully.")
    except Exception as e:
        log_error(f"Test Failed: Error logging error - {str(e)}")
        assert False, f"Error log failed: {str(e)}"
