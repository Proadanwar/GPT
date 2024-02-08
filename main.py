import telebot
import requests
from keep_alive import keep_alive
keep_alive()
API_TOKEN = '6828113424:AAGwv1yoDTo38Fv8ustatbTOjIGx2JOJ9DU'
URL = "https://dev-gpts.pantheonsite.io/wp-admin/js/apis/WormGPT.php"

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, " welcome to WormGPT .")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    data = {
        "text": message.text,
        "api_key": "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",
        "temperature": 0.9
    }
    response = requests.post(URL, json=data).json()
    text = response["choices"][0]["message"]["content"]
    bot.reply_to(message, text, parse_mode='markdown')

bot.polling()
