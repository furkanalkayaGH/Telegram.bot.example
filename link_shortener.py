import requests
import urllib
import telebot
import json

API_KEY_url = '25eab58e3f5cc717d5529391d5fd3458e200c'
API_KEY_telegrambot = '5565330019:AAEGRW5MZ4TDo-TbTKoWgA-cPsWReYPr9Mw'

bot = telebot.TeleBot(API_KEY_telegrambot)
url = urllib.parse.quote("https://twitter.com/furkan_alkaya_")
name = ''
r = requests.get('http://cutt.ly/api/api.php?key={}&short={}&name={}'.format(API_KEY_url, url, name))
json = r.json()
link = json['url']['shortLink']


@bot.message_handler(commands=['Greet'])
def greet(message):
    bot.reply_to(message, 'Welcome to url shortener')
    bot.send_message(message.chat.id, "Here's your shortened link :) " + link)
    print(link)



bot.polling()