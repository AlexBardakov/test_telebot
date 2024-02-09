from config import TOKEN, trigger_items

from random import choice
from refresher import date_catalog_refresh

import telebot
from telebot import types

import text_data

bot = telebot.TeleBot(TOKEN)


@bot.callback_query_handler(func=lambda call: 'YesNo:' in call.data)
def save_age(call):
    bot.send_message(call.message.chat.id, call.data)


# def get_age(message):
#     keyboard = types.InlineKeyboardMarkup(row_width=1)
#     keyboard.add(
#         types.InlineKeyboardButton(text='Да', callback_data='YesNo:yes'))
#     keyboard.add(
#         types.InlineKeyboardButton(text='Нет', callback_data='YesNo:no'))
#     bot.send_message(message.chat.id, 'Да или нет?', reply_markup=keyboard)


@bot.message_handler(commands=['start'])
def start(message, call_text=text_data.start_user_text):
    if message.chat.id == 386637507:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('_Отметка об обновлении каталога_')
        btn2 = types.KeyboardButton("Наличие и цены")
        btn3 = types.KeyboardButton("Когда будет в наличии...")
        btn4 = types.KeyboardButton("Наши контакты")
        btn5 = types.KeyboardButton("Доступные предзаказы")
        btn6 = types.KeyboardButton("Сотрудничество")
        btn7 = types.KeyboardButton("График работы")
        btn8 = types.KeyboardButton("Связь с руководителем")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id,
                         text='Добрый день, администратор, чем я могу помочь?', reply_markup=markup)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Доставка')
        btn2 = types.KeyboardButton('Наличие и цены')
        btn3 = types.KeyboardButton('Когда будет в наличии...')
        btn4 = types.KeyboardButton('Наши контакты')
        btn5 = types.KeyboardButton('Доступные предзаказы')
        btn6 = types.KeyboardButton('Сотрудничество')
        btn7 = types.KeyboardButton('График работы')
        btn8 = types.KeyboardButton('Связь с руководителем')
        btn9 = types.KeyboardButton('Как нас найти')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
        bot.send_message(message.chat.id,
                         call_text.format(message.from_user),
                         reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == 'Вернуться в главное меню':
        start(message, text_data.text_of_user_menu)

    elif message.text == 'Доставка':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Доставка по Томску')
        btn2 = types.KeyboardButton('Доставка в другие регионы')
        back = types.KeyboardButton(text_data.back_to_menu_text)
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text='Выберите вариант доставки:',
                         reply_markup=markup)

    elif message.text == 'Наличие и цены':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton(text_data.back_to_menu_text)
        markup.add(back)
        bot.send_message(message.chat.id,
                         text=text_data.refresh_catalog(),
                         reply_markup=markup)

    elif message.text == 'Когда будет в наличии...':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Буррата и страчателла')
        btn2 = types.KeyboardButton('Сырные десерты')
        btn3 = types.KeyboardButton('Плавленый сыр')
        btn4 = types.KeyboardButton('Другие сыры')
        back = types.KeyboardButton(text_data.back_to_menu_text)
        markup.add(btn1, btn2, btn3, btn4, back)
        bot.send_message(message.chat.id, text='Что Вас интересует?',
                         reply_markup=markup)

    elif message.text == 'Наши контакты':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton(text_data.back_to_menu_text)
        markup.add(back)
        bot.send_message(message.chat.id,
                         text=text_data.text_call_info, reply_markup=markup)

    elif message.text == 'Как нас найти':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton(text_data.back_to_menu_text)
        markup.add(back)
        bot.send_message(message.chat.id,
                         text=text_data.text_address_info, reply_markup=markup)

    elif message.text == 'Доступные предзаказы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton(text_data.back_to_menu_text)
        markup.add(back)
        bot.send_message(message.chat.id,
                         text=text_data.preorder_info, reply_markup=markup)

    elif message.text == 'Доступные предзаказы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton(text_data.back_to_menu_text)
        markup.add(back)
        bot.send_message(message.chat.id,
                         text=text_data.preorder_info, reply_markup=markup)

    elif message.text == 'График работы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton(text_data.back_to_menu_text)
        markup.add(back)
        bot.send_message(message.chat.id,
                         text=text_data.text_worktime, reply_markup=markup)

    elif message.text == '_Отметка об обновлении каталога_':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton(text_data.back_to_menu_text)
        markup.add(back)
        date_catalog_refresh()
        bot.send_message(message.chat.id,
                         text='Информация о последнем изменении каталога '
                              'обновлена', reply_markup=markup)

    elif (message.text == 'Как меня зовут?'):
        bot.send_message(message.chat.id, 'У меня нет имени..')
    #
    # elif message.text == "Что я могу?":
    #     bot.send_message(message.chat.id, text="Поздороваться с читателями")
    #
    # elif (message.text == "Вернуться в главное меню"):
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #     button1 = types.KeyboardButton("👋 Поздороваться")
    #     button2 = types.KeyboardButton("❓ Задать вопрос")
    #     markup.add(button1, button2)
    #     bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    # else:
    #     bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")


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
