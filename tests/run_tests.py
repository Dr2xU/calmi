import pytest # type: ignore
from src.utils import log_debug

def run_tests():
    """Runs all test files in logical order"""
    log_debug("Starting all tests...")

    test_files = [
        "tests/test_utils.py",
        "tests/test_model_loader.py",
        "tests/test_chatbot.py",
        "tests/test_database.py",
        "tests/test_api.py",
    ]

    for test in test_files:
        log_debug(f"Running: {test}")
        pytest.main([test])

    log_debug("All tests completed.")

if __name__ == "__main__":
    run_tests()
