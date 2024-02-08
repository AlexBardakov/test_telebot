from config import TOKEN, trigger_items
from datetime import datetime

from random import choice

import telebot
from telebot import types

bot = telebot.TeleBot(TOKEN)
time_of_refresh = '25-12-2023'


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
def start(message):
    if message.chat.id == 386637507:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Отметка об обновлении каталога")
        # btn2 = types.KeyboardButton("Наличие и цены")
        # btn3 = types.KeyboardButton("Когда будет в наличии...")
        # btn4 = types.KeyboardButton("Наши контакты")
        # btn5 = types.KeyboardButton("Доступные предзаказы")
        # btn6 = types.KeyboardButton("Сотрудничество")
        # btn7 = types.KeyboardButton("График работы")
        # btn8 = types.KeyboardButton("Связь с руководителем")
        # markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        # bot.send_message(message.chat.id,
        #                  text='Добрый день, администратор, чем я могу помочь?', reply_markup=markup)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Доставка")
        btn2 = types.KeyboardButton("Наличие и цены")
        btn3 = types.KeyboardButton("Когда будет в наличии...")
        btn4 = types.KeyboardButton("Наши контакты")
        btn5 = types.KeyboardButton("Доступные предзаказы")
        btn6 = types.KeyboardButton("Сотрудничество")
        btn7 = types.KeyboardButton("График работы")
        btn8 = types.KeyboardButton("Связь с руководителем")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id,
                         text="Добрый день, {0.first_name}! Я бот сыроварни Four Kings. Я нужен для того, чтобы Вы могли "
                              "быстро получать нужную Вам информацию, не дожидаясь ответа от персонала сыроварни. Я могу "
                              "подсказать Вам, как найти наши контакты, дам информацию о доставке и многое другое. Вы "
                              "можете выбрать свой вопрос через кнопки команд. Если нужной команды среди кнопок не окажется"
                              ", нажмите на соответствующую клавишу и я переведу Вас в диалог с "
                              "сыроварами.".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    global time_of_refresh
    if message.text == 'Доставка':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Доставка по Томску")
        btn2 = types.KeyboardButton("Доставка в другие регионы")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text='Выберите вариант доставки:', reply_markup=markup)
    elif message.text == 'Наличие и цены':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Вернуться в главное меню')
        markup.add(back)
        bot.send_message(message.chat.id, text='С актуальным наличием и ценами Вы можете ознакомиться по ссылке '
                                               'fourkings.ru. Последнее обновление информации на сайте '
                                               'было {}'.format(time_of_refresh), reply_markup=markup)
    elif message.text == 'Отметка об обновлении каталога':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Вернуться в главное меню')
        markup.add(back)
        time_of_refresh = str(datetime.now().strftime("%d/%m/%Y"))
        bot.send_message(message.chat.id, text='Информация о последнем обновлении каталога '
                                               'обновлена'.format(time_of_refresh), reply_markup=markup)
    # elif (message.text == "Как меня зовут?"):
    #     bot.send_message(message.chat.id, "У меня нет имени..")
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
