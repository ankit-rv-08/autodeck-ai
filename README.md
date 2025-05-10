# autodeck-ai
Autodeck AI is a simple Python tool that converts long text documents into concise, bullet-point slides using OpenAI's GPT models. It automatically chunks input text, handles rate limits, and generates slide-style summaries — perfect for making presentations from articles, notes, or research papers.

# 🧠 Autodeck AI

Turn large documents into clean, bullet-point slides using GPT.

## 🚀 Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/autodeck-ai.git
   cd autodeck-ai
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Set your OpenAI key:

bash
Copy
Edit
export OPENAI_API_KEY=your-key-here  # Linux/macOS
set OPENAI_API_KEY=your-key-here     # Windows CMD
Place your input.txt file in the root folder.

Run it:

bash
Copy
Edit
python app.py
🛠 Features
Splits large documents into chunks

Summarizes each chunk as a presentation slide

Handles rate limits automatically

📦 Future Ideas
Upload PDF support

Web interface (Flask or Streamlit)

Use Mixtral/Groq for free inference

🧠 Built with
Python 🐍

OpenAI GPT-3.5 Turbo
