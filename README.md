# Calmi: Artificial Emotional Intelligence Mental Health Chatbot

## Overview

Calmi is an advanced **Artificial Emotional Intelligence (AEI)** chatbot designed to help users navigate their emotions and mental well-being. It engages in thoughtful, supportive conversations, ensuring users stay focused on their emotions. The chatbot integrates **speech recognition, sentiment analysis, and facial emotion recognition** to provide a holistic emotional support system.

## Features

- **Conversational AI with AEI**: Uses **DeepSeek-R1-Distill-Qwen-1.5B** for empathetic and context-aware responses.
- **Artificial Emotional Intelligence (AEI)**: Enhances interactions by analyzing tone, emotion, and intent.
- **Prompt Guarding**: Implements **meta-llama/Prompt-Guard-86M** to filter and moderate user prompts.
- **Speech-to-Text (STT)**: Uses **OpenAI Whisper** for real-time speech recognition.
- **Text-to-Speech (TTS)**: Uses **Coqui TTS** for chatbot voice responses.
- **Sentiment Analysis**: Detects user emotions via **GoEmotions dataset**.
- **Facial Emotion Recognition**: Integrates **AffectNet** for webcam-based emotion detection and response adaptation.

## Setup & Installation

### **1. Clone the Repository**

```bash
git clone https://huggingface.co/spaces/Dr-2xU/AEI-Mental-Health-Chatbot
cd AEI-Mental-Health-Chatbot
```

### **2. Create Virtual Environment & Install Dependencies**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### **3. Download & Load Fine-Tuned Model**

```bash
huggingface-cli login  # Ensure access to private models
llama model download --source huggingface --model-id deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B
```

### **4. Run the Chatbot**

```bash
python app.py  # Runs the chatbot locally
```

## Model Configuration

| Parameter | Value |
|-----------|-------|
| Max New Tokens | 512 |
| Temperature | 0.7 |
| Top-p (Nucleus Sampling) | 0.95 |

## Deployment on Hugging Face

Calmi is hosted on **Hugging Face Spaces** using **Gradio** for an interactive user interface.

### **Deploy in Hugging Face Space***

1. Go to **[Hugging Face Spaces](https://huggingface.co/spaces)**
2. Select `Create Space` → Choose **Gradio** as SDK
3. Upload project files & configure model
4. Set environment variables for Hugging Face API tokens
5. Click **Run Space**

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Added new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a Pull Request

## License

This project is licensed under the **Apache-2.0 License**.
