import os
import telebot

bot_token = os.getenv('TG_BOT_TOKEN')
bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['start'])
def start(message):
    mes = f'Привет, {message.from_user.first_name} {message.from_user.last_name}'
    bot.send_message(message.chat.id, mes)

