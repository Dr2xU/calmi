import torch
from model.Janus.janus.models import VLChatProcessor, MultiModalityCausalLM
from model.Janus.janus.utils.io import load_pil_images
from src.utils import log_error, log_debug
from model.model_loader import load_model
from config import MODEL_NAME, PROMPT

model, processor, tokenizer = load_model()

def generate_response(user_input, history, max_tokens=80, temperature=0.7, top_p=0.95, image=None):
    """Generates a response considering chat history, system instructions, and optional images."""
    try:
        if model is None:
            return "Model failed to load."

        # Create conversation format with system message
        conversation = [
            {"role": "<|System|>", "content": PROMPT},  # Inject system message
        ] + list(history) + [
            {"role": "<|User|>", "content": f"{user_input}"},
            {"role": "<|Assistant|>", "content": ""},
        ]

        # If there's an image, process it
        if image:
            conversation[-2]["content"] = f"<image_placeholder>\n{user_input}"
            conversation[-2]["images"] = [image]

        # Load images if available
        pil_images = load_pil_images(conversation) if image else None

        # Prepare input
        prepare_inputs = processor(conversations=conversation, images=pil_images, force_batchify=True).to(model.device)

        # Get input embeddings
        inputs_embeds = model.prepare_inputs_embeds(**prepare_inputs)

        # Generate response
        outputs = model.language_model.generate(
            inputs_embeds=inputs_embeds,
            attention_mask=prepare_inputs.attention_mask,
            pad_token_id=tokenizer.eos_token_id,
            bos_token_id=tokenizer.bos_token_id,
            eos_token_id=tokenizer.eos_token_id,
            max_new_tokens=max_tokens,
            do_sample=True,  # Enable sampling
            temperature=temperature,
            top_p=top_p,
            use_cache=True,
        )

        # Decode response
        answer = tokenizer.decode(outputs[0].cpu().tolist(), skip_special_tokens=True)
        return answer
    except Exception as e:
        log_error(f"Error generating response: {str(e)}")
        return "I'm sorry, but I encountered an error."