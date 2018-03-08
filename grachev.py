import telegram
import pprint

bot = telegram.Bot('520075736:AAHoRHoWW5KDIzTJ4mnMspzWEDCYu5UYN5s')
pprint.pprint([x.message.text for x in bot.get_updates(timeout=10)])

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
updater = Updater('520075736:AAHoRHoWW5KDIzTJ4mnMspzWEDCYu5UYN5s')
dp = updater.dispatcher


def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

def check(bot, update):
    print(update.message.text)


dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text, callback=check))

updater.start_polling()
