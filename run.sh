#!/bin/bash

# Stop execution if any command fails
set -e

echo "🔥 Activating Virtual Environment..."
# source venv/bin/activate  # For Mac/Linux
source venv/Scripts/activate

echo "📥 Installing Dependencies..."
pip install -r requirements.txt

echo "📦 Loging/Checking/Downloading Model..."
huggingface-cli login  # Ensure HF authentication
llama model download --source huggingface --model-id deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B

# echo "📊 Checking/Downloading Dataset..."
# mkdir -p data
# if [ ! -f "data/conversations.json" ]; then
#     echo "⬇️  Downloading dataset..."
#     wget -O data/conversations.json "https://your-dataset-url.com/conversations.json"
# fi

echo "🚀 Starting Chatbot..."
python src/app.py
