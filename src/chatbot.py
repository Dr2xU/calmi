from model_loader import load_model
from src.utils import log_error, log_debug
from config import PROMPT

try:
    pipe = load_model()
    log_debug("TinyLlama pipeline initialized in chatbot.py")
except RuntimeError as e:
    log_error(str(e))
    pipe = None

def generate_response(user_input, history, system_message, max_tokens=50, temperature=0.6, top_k=30, top_p=0.85):
    """Generates a chatbot response using TinyLlama while ensuring quality and speed."""
    try:
        if pipe is None:
            raise RuntimeError("TinyLlama pipeline not initialized!")

        # ✅ Structure the chat format correctly
        messages = [{"role": "system", "content": system_message}] + history + [{"role": "user", "content": user_input}]

        # ✅ Format the chat message
        prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

        # ✅ Generate response with optimized parameters
        outputs = pipe(
            prompt,
            max_new_tokens=max_tokens,
            do_sample=True,  # Faster and more stable responses
            temperature=temperature,
            top_k=top_k,
            top_p=top_p,
            pad_token_id=pipe.tokenizer.eos_token_id,  # Prevents excessive generation
        )

        # ✅ Extract ONLY the assistant's response
        response = outputs[0]["generated_text"]

        # ✅ Ensure model doesn't mirror user input
        if "<|assistant|>" in response:
            response = response.split("<|assistant|>")[-1].strip()  # Keep only model output

        return response
    except Exception as e:
        log_error(f"Error generating response: {str(e)}")
        return "I'm sorry, but I encountered an error."
