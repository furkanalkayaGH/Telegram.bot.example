
import telebot

API_KEY = '5565330019:AAEGRW5MZ4TDo-TbTKoWgA-cPsWReYPr9Mw'
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['Greet'])
def greet(message):
    bot.reply_to(message, 'Hello :)')

@bot.message_handler(commands=['hello'])
def hello(message):
    bot.send_message(message.chat.id, 'HELLO!!!!!')


bot.polling()

