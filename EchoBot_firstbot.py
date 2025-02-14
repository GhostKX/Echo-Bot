import telebot
from dotenv import load_dotenv
import os

# Loading environment variables from the .env file
load_dotenv()
API_KEY = str(os.getenv('API_KEY'))
bot = telebot.TeleBot(API_KEY)


# Creating decorator to handle start of the bot
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id  # Unique ID of a user
    first_name = message.from_user.first_name  # First name of the user
    last_name = message.from_user.last_name  # Last name of the user
    username = message.from_user.username  # Username of the user
    if first_name and last_name:
        greeting = f'Hi,{first_name} {last_name}\n' \
                   f'\nWelcome to First Echo bot!'
    elif first_name is not None and last_name is None:
        greeting = f'Hi, {first_name}\n' \
                   f'\nWelcome to the My first Echo bot!'
    else:
        greeting = 'Hi, Welcome to the My first Echo bot!'

    bot.send_message(user_id, greeting)
    # bot.send_message(user_id, message)


# Creating decorator to handle any other text messages
@bot.message_handler(content_types=['text'])
def echo(message):
    user_id = message.from_user.id
    user_text = message.text  # The text that user has typed in and send it to the bot chat
    bot.send_message(user_id, user_text)  # Sending back the same type of the message to that user who sent it


# Start polling the bot to keep it running and listening for incoming messages
bot.infinity_polling()
