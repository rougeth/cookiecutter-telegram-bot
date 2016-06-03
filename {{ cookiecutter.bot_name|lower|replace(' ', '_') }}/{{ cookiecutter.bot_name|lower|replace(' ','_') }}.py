#!/usr/bin/env python3

import os

from telebot import TeleBot

from utils import TokenNotDefined


TOKEN = os.environ.get('TOKEN')
if not TOKEN:
    raise TokenNotDefined('TOKEN must be defined')

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome to {{ cookiecutter.bot_name | title }} Bot')


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


if __name__ == '__main__':
    bot.polling()
