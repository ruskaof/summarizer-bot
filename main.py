import telebot

bot = telebot.TeleBot('6215154364:AAEhtscNNRwlOcKlQgZCZADgxYBz9l67k-M')


@bot.message_handler(commands=['start'])
def start(message):
    mes = f'Привет, {message.from_user.first_name} {message.from_user.last_name}'
    bot.send_message(message.chat.id, mes)


bot.polling(none_stop=True)
