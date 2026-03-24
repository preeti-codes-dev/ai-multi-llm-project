# Multi-LLM API Integration Project

This project demonstrates integration of multiple AI APIs.

## APIs Used
- Groq
- Cohere
- Hugging Face
- Ollama (Local LLM)
- Gemini
- OpenAI

## Features
- Accepts user input
- Generates AI response
- Handles errors gracefully

## How to Run

Install dependencies:
pip install -r requirements.txt

Run any file:
python groq_example.py
python cohere_example.py
python huggingface_example.py
python ollama_example.py

## Screenshots

### Groq Output
![Groq Output](screenshots/groq_output.png)

### Cohere Output
![Cohere Output](screenshots/cohere_output.png)

### HuggingFace Output
![HuggingFace Output](screenshots/huggingface_output.png)

### Ollama Output
![Ollama Output](screenshots/ollama_output.png)

### Gemini Output (Quota Error)
![Gemini Output](screenshots/gemini_output.png)

### OpenAI Output (Quota Error)
![OpenAI Output](screenshots/openai_output.png)

## Note
Gemini and OpenAI may show quota errors depending on API limits.