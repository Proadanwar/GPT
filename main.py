import telebot
import requests
from keep_alive import keep_alive

# Start the keep alive mechanism
keep_alive()

API_TOKEN = '6828113424:AAGwv1yoDTo38Fv8ustatbTOjIGx2JOJ9DU'
URL = "https://dev-gpts.pantheonsite.io/wp-admin/js/apis/WormGPT.php"

# Initialize the bot
bot = telebot.TeleBot(API_TOKEN)

# Handler for the /start and /help commands
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to WormGPT.")

# Handler for all messages
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    data = {
        "text": message.text,
        "api_key": "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",
        "temperature": 0.9
    }
    # Send a POST request to the model URL
    response = requests.post(URL, json=data).json()
    text = response["choices"][0]["message"]["content"]
    # Reply to the user with the model response
    bot.reply_to(message, text, parse_mode='markdown')

# Start the bot
bot.polling()
