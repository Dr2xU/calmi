import pytest # type: ignore
import sqlite3
from src.database import init_db, save_interaction
from src.config import DB_FILE
from src.utils import log_error, log_debug

@pytest.fixture(scope="module")
def setup_database():
    """Initialize the database once per session"""
    log_debug("Initializing test database...")
    init_db()

def test_database_connection(setup_database):
    """Test if the database initializes properly"""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='interactions';")
        table_exists = cursor.fetchone() is not None
        conn.close()

        assert table_exists
        log_debug("Test Passed: Database initialized successfully.")
    except Exception as e:
        log_error(f"Test Failed: Database initialization error - {str(e)}")
        assert False, f"Database initialization failed: {str(e)}"

def test_save_interaction(setup_database):
    """Test if user interactions are saved in the database"""
    try:
        user_input = "Hello!"
        bot_response = "Hi there!"

        save_interaction(user_input, bot_response)

        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT user_message, bot_response FROM interactions ORDER BY id DESC LIMIT 1;")
        last_entry = cursor.fetchone()
        conn.close()

        assert last_entry is not None
        assert last_entry[0] == user_input
        assert last_entry[1] == bot_response

        log_debug("Test Passed: Interaction saved in database successfully.")
    except Exception as e:
        log_error(f"Test Failed: Database save error - {str(e)}")
        assert False, f"Database save test failed: {str(e)}"
