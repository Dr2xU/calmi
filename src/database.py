import sqlite3
from src.config import DB_FILE
from src.utils import log_error, log_debug

def init_db():
    """Initializes the database to store user interactions."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS interactions (id INTEGER PRIMARY KEY, user_message TEXT, bot_response TEXT)''')
        conn.commit()
        conn.close()
        log_debug("Database initialized.")
    except Exception as e:
        log_error(f"Database initialization failed: {str(e)}")

def save_interaction(user_message, bot_response):
    """Stores user interactions into the database."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO interactions (user_message, bot_response) VALUES (?, ?)", (user_message, bot_response))
        conn.commit()
        conn.close()
    except Exception as e:
        log_error(f"Failed to save interaction: {str(e)}")
