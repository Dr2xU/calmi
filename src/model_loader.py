import torch
from transformers import pipeline
from config import MODEL_NAME
from utils import log_error, log_debug

try:
    # ✅ Load TinyLlama model with pipeline
    pipe = pipeline(
        "text-generation",
        model=MODEL_NAME,
        torch_dtype=torch.float32,
        device_map="auto",
    )
    log_debug("TinyLlama pipeline initialized successfully.")
except Exception as e:
    log_error(f"Failed to load TinyLlama pipeline: {str(e)}")
    pipe = None

# ✅ Function to return the pipeline
def load_model():
    if pipe is None:
        raise RuntimeError("TinyLlama pipeline not initialized!")
    return pipe
