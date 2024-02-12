import telebot

from bg import keep_alive
from codes import codes as c

bot = telebot.TeleBot('6593640929:AAE5zl8zxzL2xMooxKGuP2K29RW20q8XUpA')


@bot.message_handler()
def info(message):
    bot.reply_to(message, f'{c[message.text]}')


keep_alive()
bot.infinity_polling()
