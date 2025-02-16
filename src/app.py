import torch
import gradio as gr
from model.Janus.janus.models import VLChatProcessor, MultiModalityCausalLM
from model.Janus.janus.utils.io import load_pil_images
from src.chatbot import generate_response
from src.utils import log_chat, log_error, log_debug
from config import MODEL_NAME, PROMPT
# Load Model (CPU/GPU)

def respond(message, history, max_tokens, temperature, top_p):
    """Handles chatbot responses while considering chat history and system instructions."""
    try:
        response = generate_response(
            user_input=message,
            history=history,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p
        )
        log_chat(message, response)
        history.append({"role": "user", "content": message})
        history.append({"role": "assistant", "content": response})
        return response, history
    except Exception as e:
        log_error(f"Chatbot error: {str(e)}")
        return "Sorry, I encountered an error. Please try again.", history

# Define Gradio UI
demo = gr.ChatInterface(
    respond,
    additional_inputs=[
        gr.Textbox(value=PROMPT, label="System message"),
        gr.Slider(minimum=1, maximum=512, value=80, step=1, label="Max new tokens"),
        gr.Slider(minimum=0.1, maximum=4.0, value=0.7, step=0.1, label="Temperature"),
        gr.Slider(minimum=0.1, maximum=1.0, value=0.95, step=0.05, label="Top-p (nucleus sampling)"),
    ],
    type="messages",  # ✅ OpenAI-style chat format
)

if __name__ == "__main__":
    demo.launch()