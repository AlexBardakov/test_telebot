import telebot

from config import TOKEN

bot = telebot.TeleBot(TOKEN)


bot.infinity_polling()