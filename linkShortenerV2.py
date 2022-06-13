import logging
import re
import requests
import telebot
import urllib
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


API_KEY_url = '25eab58e3f5cc717d5529391d5fd3458e200c'

#First Attempts
"""'url = urllib.parse.quote("https://twitter.com/furkan_alkaya_")'
name = ''
r = requests.get('http://cutt.ly/api/api.php?key={}&short={}&name={}'.format(API_KEY_url, url, name))
json = r.json()
link = json['url']['shortLink']
"""

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.


def start(update, context):
    update.message.reply_text('Welcome to URL shortener, please enter your URL ')

def shorten(update, context):

    url = update.message.text
    if (re.findall("https:", url)):
        'url = urllib.parse.quote("https://twitter.com/furkan_alkaya_")'
        name = ''
        r = requests.get('http://cutt.ly/api/api.php?key={}&short={}&name={}'.format(API_KEY_url, url, name))
        json = r.json()
        link = json['url']['shortLink']
        update.message.reply_text("Here's your shortened link " + link)

    else:
        update.message.reply_text("Please Enter a Valid URL or command")
        update.message.reply_text("Type '/help' to see available commands")

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text("Here's the list of commands: \n  /help -- Help \n /start -- Starts the bot \n")

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Start the bot."""
    API_KEY_telegram = "5565330019:AAEGRW5MZ4TDo-TbTKoWgA-cPsWReYPr9Mw"
    updater = Updater(API_KEY_telegram, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - recieve links from user
    dp.add_handler(MessageHandler(Filters.text, shorten))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()