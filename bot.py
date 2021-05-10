import logging
import requests
import locale

import telegram

locale.setlocale(locale.LC_ALL, 'en_AG')


from telegram.ext import Updater, CommandHandler

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hey this is your bot!')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Currently I am in Alpha stage, help me also!')

def piracy(update, context):
    update.message.reply_text('Ahhan, FBI wants to know your location!')

def price(update, context):
    r = requests.get(url="https://api.pancakeswap.info/api/v2/tokens/0xe1DB3d1eE5CfE5C6333BE96e6421f9Bd5b85c987")

    response = r.json()

    name = response['data']['name']
    price = float(response['data']['price']) * 1e6
    market_cap = round(650 * 1e6 * price)
    locale_market_cap = locale.format_string("%d", market_cap, grouping=True)

    update.message.reply_text(text=f"  🚀   {name}   🚀\n\n💰  1M tokens: <b>${round(price, 8)}</b> \n💴  Market cap: <b>${locale_market_cap}</b>", parse_mode=telegram.ParseMode.HTML)
    # update.message.reply_text(f"🚀 {name} 🚀\n\n💰  1M tokens: ${round(price, 8)} \n💴  Market cap: ${locale_market_cap}")


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1838016774:AAEkm57AJJY8Iz1D_9P_z_8ifzb8qj8v1PU", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("piracy", piracy))
    dp.add_handler(CommandHandler("price", price))
    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
