# 🤖 Gemini Dual-Pass Chatbot

A Python-powered chatbot that uses the Google GenAI SDK to automatically enhance, re-engineer, and optimize every user message using a fast model before generating a high-quality final response with a reasoning model.

## 🚀 Features
- **Dual-Pass Prompt Architecture:** Automatically improves casual or vague user inputs on the fly using `gemini-2.5-flash`.
- **High-Fidelity Execution:** Leverages `gemini-2.5-pro` to answer the enhanced instructions.
- **GitHub-Safe Security:** No hardcoded API keys. It prompts you securely in the terminal so you never leak secrets.
- **Infinite Loop:** Keeps the conversation going right inside your console.

## 🛠️ Setup Instructions

### 1. Install Dependencies
Make sure you have the official Google GenAI SDK installed:
```bash
pip install google-genai
```

### 2. Run the Chatbot
Simply execute the script:
```bash
python main.py
```

If the script doesn't detect a `GEMINI_API_KEY` in your environment variables, it will securely ask you to paste it in right before the chat starts!

### 3. Exit the Chat
Type `quit` or `exit` anytime to end the chat.
