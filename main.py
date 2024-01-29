from config import TOKEN, trigger_items

from random import choice

import telebot
from telebot import types


bot = telebot.TeleBot(TOKEN)


@bot.callback_query_handler(func=lambda call: 'YesNo:' in call.data)
def save_age(call):
    bot.send_message(call.message.chat.id, call.data)


def get_age(message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        types.InlineKeyboardButton(text='Да', callback_data='YesNo:yes'))
    keyboard.add(
        types.InlineKeyboardButton(text='Нет', callback_data='YesNo:no'))
    bot.send_message(message.chat.id, 'Да или нет?', reply_markup=keyboard)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет!')
    get_age(message)


@bot.message_handler(commands=['help'])
def bot_help(message):
    bot.send_message(message.chat.id, 'Помоги(')


@bot.message_handler(commands=['id'])
def bot_id(message):
    bot.send_message(message.chat.id, message.chat.id)


@bot.message_handler(content_types=['text'])
def bot_auto_call(message):
    for key, caller in trigger_items:
        if any((word in message.text.lower()) for word in key):
            if isinstance(caller, tuple):
                bot.send_message(message.chat.id, text=choice(caller))
            else:
                bot.send_message(message.chat.id, text=caller)


bot.infinity_polling()
