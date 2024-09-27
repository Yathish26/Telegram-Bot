import os

from dotenv import load_dotenv
load_dotenv()

import telebot

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")
    
    
@bot.message_handler(commands=['day'])
def send_day(message):
    from datetime import date
    today = date.today()
    bot.reply_to(message, f"Today is {today.strftime('%d.%m.%Y')}")
    
    
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Here are the commands you can use:\n/start\n/hello\n/help\n/day\n/register\n/quiz")
    

user_data = {}

@bot.message_handler(commands=['register'])
def register(message):
    user_data[message.chat.id] = {}
    bot.send_message(message.chat.id, "What's your name?")
    bot.register_next_step_handler(message, get_name)

def get_name(message):
    user_data[message.chat.id]['name'] = message.text
    bot.send_message(message.chat.id, "What's your email?")
    bot.register_next_step_handler(message, get_email)

def get_email(message):
    user_data[message.chat.id]['email'] = message.text
    bot.send_message(message.chat.id, f"Thank you for registering, {user_data[message.chat.id]['name']}")
    

    
quiz_data = {
    "What is the capital of France?": "Paris",
    "What is 2 + 2?": "4"
}

@bot.message_handler(commands=['quiz'])
def start_quiz(message):
    question = list(quiz_data.keys())[1]
    bot.send_message(message.chat.id, question)
    bot.register_next_step_handler(message, check_answer, question)

def check_answer(message, question):
    if message.text.lower() == quiz_data[question].lower():
        bot.send_message(message.chat.id, "Correct!")
    else:
        bot.send_message(message.chat.id, "Wrong! Try again.")


    

    
bot.infinity_polling()


