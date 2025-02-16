import pytest # type: ignore
from src.chatbot import generate_response
from model.model_loader import load_model
from src.utils import log_error, log_debug

@pytest.fixture(scope="module")
def chatbot_model():
    """Fixture to load the chatbot model once per test session"""
    log_debug("Loading chatbot model for tests...")
    return load_model()

@pytest.mark.parametrize("user_input", [
    "Hello, i'm feeling devestated today!",
    "Hello, i'm feeling sad today!",
    "Hello, i'm feeling down today!",
    "Hello, i'm feeling angry today!",
])
def test_generate_response(chatbot_model, user_input):
    """Test chatbot response generation for multiple inputs"""
    model, tokenizer = chatbot_model
    try:
        response = generate_response(user_input, model, tokenizer, max_tokens=512, temperature=0.7, top_p=0.95)

        assert isinstance(response, str)
        assert len(response) > 0
        log_debug(f"Test Passed: Chatbot responded correctly to input '{user_input}'")
    except Exception as e:
        log_error(f"Test Failed: Chatbot response error - {str(e)}")
        assert False, f"Chatbot failed to generate response: {str(e)}"
