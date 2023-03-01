import os
import telebot
import time

from pyrogram import Client, filters
from pyrogram.types import Message



bot_token = os.getenv('TG_BOT_TOKEN')
bot = telebot.TeleBot(bot_token)

api_hash = os.getenv('API_HASH')
api_id = os.getenv('API_ID')

client = Client(name="whoismyav", api_hash=api_hash, api_id=api_id)

@bot.message_handler(commands=['start'])
def start(message):
    mes = f'Привет, {message.from_user.first_name} {message.from_user.last_name}'
    bot.send_message(message.chat.id, mes)

@client.on_message(filters.command("summarize", prefixes='/'))
def type(client_object, message: Message):
    for data in client_object.get_chat_history(-884174798):
        print(data.text)

client.run()
