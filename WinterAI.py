import os
import json
from dotenv import load_dotenv
import google.generativeai as genai
import telebot

# Load environment variables
env_path = '.env/apikey.env'
load_dotenv(dotenv_path=env_path)

# Get API keys from environment
TELEGRAM_API_KEY = os.getenv('TELEGRAM_API_KEY')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Initialize Telegram bot
bot = telebot.TeleBot(TELEGRAM_API_KEY)

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Safety settings
safety_settings = [
    {'category': 'HARM_CATEGORY_HARASSMENT', 'threshold': 'BLOCK_MEDIUM_AND_ABOVE'},
    {'category': 'HARM_CATEGORY_HATE_SPEECH', 'threshold': 'BLOCK_MEDIUM_AND_ABOVE'},
    {'category': 'HARM_CATEGORY_SEXUALLY_EXPLICIT', 'threshold': 'BLOCK_MEDIUM_AND_ABOVE'},
    {'category': 'HARM_CATEGORY_DANGEROUS_CONTENT', 'threshold': 'BLOCK_MEDIUM_AND_ABOVE'}
]

# Initialize Gemini model
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    generation_config=genai.types.GenerationConfig(
        temperature=0.7,
        top_p=0.9,
        top_k=50,
        max_output_tokens=500
    ),
    safety_settings=safety_settings
)

# Load dataset
data_path = 'data/data_forIntegration.json'
with open(data_path, "r", encoding="utf-8") as f:
    dataset = json.load(f)

# Display first 3 entries
for i in dataset[:3]:
    print(f"Q: {i['user']}\nA: {i['bot']}\n")

# Create knowledge base from dataset
knowledge_base = "\n".join([f"Q: {d['user']}\nA: {d['bot']}" for d in dataset])

# Function to handle user messages
@bot.message_handler(func=lambda m: True)
def reply_user(message):
    user_question = message.text
    prompt = f"""
You're an AI Chatbot named WinterAI. Answer and assist based on these data:

{knowledge_base}

Question: "{user_question}"
Answer:
"""
    try:
        response = model.generate_content(prompt)
        bot_response = response.text.strip()

        if not bot_response:
            bot_response = "Sorry, I couldn't generate a response. Please try again."

    except Exception as e:
        bot_response = f"An error occurred: {e}. Please try again later."

    # Reply to user with bot's response
    bot.reply_to(message, bot_response)

# Run the bot
bot.infinity_polling()
