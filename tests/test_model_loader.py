import pytest # type: ignore
from model_loader import load_model
from src.utils import log_error, log_debug

def test_load_model():
    """Test model loading"""
    try:
        model, tokenizer = load_model()

        assert model is not None
        assert tokenizer is not None
        log_debug("Test Passed: Model loaded successfully.")
    except Exception as e:
        log_error(f"Test Failed: Model loading error - {str(e)}")
        assert False, f"Model failed to load: {str(e)}"
