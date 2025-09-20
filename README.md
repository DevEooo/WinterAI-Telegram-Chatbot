# ❄️ WinterAI – Telegram Chatbot

WinterAI is a personal AI chatbot powered by Gemini LLM for Telegram, designed to be a calm and intelligent companion that representing reserved personality.

## ⚠️ Limitations
While WinterAI provides a smooth chatting experience, there are some current limitations:
- **Static Prompting** – Personality and responses rely on predefined system prompts (not fully adaptive).  
- **No Long-Term Memory** – Conversations reset after sessions (unless manually integrated with a database).  
- **API Dependency** – Requires a valid LLM API key and stable internet connection to function.  
- **Limited Privacy** – Data is processed through third-party LLM APIs (depending on your provider).  
- **Single-Personality Mode** – Currently limited to one persona (calm, intelligent, emotionally reserved).  


## Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd <your-repo-directory>
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   - Copy the example environment file: `cp .env.example .env`
   - Edit `.env` and add your actual API keys:
     - `TELEGRAM_API_KEY`: Get from [@BotFather](https://t.me/botfather) on Telegram
     - `GEMINI_API_KEY`: Get from [Google AI Studio](https://aistudio.google.com/)

4. **Run the bot**
   ```bash
   python WinterAI.py
   ```

## Security Notes

- Never commit your `.env` file to version control
- The `.env` file is automatically ignored by `.gitignore`
- Use the provided `.env.example` as a template for setting up your environment

## Features

- AI-powered responses using Google Gemini
- Knowledge base integration
- Safety settings for content filtering
- Persistent conversation handling
