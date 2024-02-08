import telebot
import requests
from keep_alive import keep_alive

# Start the keep alive mechanism
keep_alive()

# Your Telegram bot token and model URL
API_TOKEN = '6828113424:AAGwv1yoDTo38Fv8ustatbTOjIGx2JOJ9DU'
URL = "https://dev-gpts.pantheonsite.io/wp-admin/js/apis/WormGPT.php"

# Initialize the bot
bot = telebot.TeleBot(API_TOKEN)

# Handler for the /start and /help commands
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to WormGPT. Send me your request and I'll respond.")

# Handler for all messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    data = {
        "text": message.text,
        "api_key": "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",
        "temperature": 0.9
    }
    response = requests.post(URL, json=data).json()
    text = response["choices"][0]["message"]["content"]
    bot.reply_to(message, text, parse_mode='markdown')

# Start the bot
bot.polling()
