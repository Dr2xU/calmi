import gradio as gr
from src.chatbot import generate_response
from src.utils import log_debug

# ✅ Define Gradio UI
demo = gr.ChatInterface(
    fn=generate_response,
    additional_inputs=[
        gr.Textbox(value="You are Calmi, an empathetic AI focused on mental well-being.", label="System Message"),
        gr.Slider(minimum=1, maximum=256, value=128, step=1, label="Max Tokens"),
        gr.Slider(minimum=0.1, maximum=2.0, value=0.7, step=0.1, label="Temperature"),
        gr.Slider(minimum=10, maximum=100, value=40, step=1, label="Top-k"),
        gr.Slider(minimum=0.1, maximum=1.0, value=0.9, step=0.05, label="Top-p"),
    ],
    type="messages",
)

if __name__ == "__main__":
    log_debug("Launching chatbot UI with TinyLlama pipeline.")
    demo.launch()
