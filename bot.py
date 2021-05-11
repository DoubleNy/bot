import logging
import requests
import math
import telegram

from telegram.ext import Updater, CommandHandler

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)



millnames = ['',' Thousand',' Million',' Billion',' Trillion']

def millify(n):
    n = float(n)
    millidx = max(0,min(len(millnames)-1,
                        int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))

    return '{:.0f}{}'.format(n / 10**(3 * millidx), millnames[millidx])

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hey this is your bot, Uncle Space Bot!\n'
                              'I am glad to serve you with most updated info.')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text(text='<b>/p</b> or <b>/price</b> shows the price for SAFESPACE from pancakeSwap & boggedFinance.\n'
                              '<b>/p_bogged</b> or <b>/price_bogged</b> shows the price for SAFESPACE from boggedFinance\n'
                              '<b>/p_pancake</b> or <b>/price_pancake</b> shows the price for SAFESPACE from pancakeSwap\n'
                              '<b>/help</b> helps you in finding the commands supported by the bot\n', parse_mode=telegram.ParseMode.HTML
                              )
def price(update, context):
    r = requests.get(url="https://api.pancakeswap.info/api/v2/tokens/0xe1DB3d1eE5CfE5C6333BE96e6421f9Bd5b85c987")

    response = r.json()

    name = response['data']['name']
    p_price = float(response['data']['price']) * 1e6
    p_mcapp = round(650 * 1e6 * p_price)
    p_market_cap = "{:,}".format(p_mcapp)

    b_price = p_price - (p_price / 100 * 28)
    b_mcapp = round(p_mcapp - (p_mcapp / 100 * 28))
    b_market_cap = "{:,}".format(b_mcapp)

    update.message.reply_text(text=f"         🚀   {name}   🚀\n\n"
                                   f"  ~~   <i>Pancakeswap[v2]</i>  ~~  \n"
                                   f"💰  1M tokens: <b>${round(p_price, 8)}</b> \n"
                                   f"💴  Market cap: <b>${p_market_cap}</b> <i>({millify(p_mcapp)})</i>\n\n"
                                   f"  ~~   <i>BoggedFinance</i>  ~~  \n"
                                   f"💰  1M tokens: <b>${round(b_price, 8)}</b> \n"
                                   f"💴  Market cap: <b>${b_market_cap}</b> <i>({millify(b_mcapp)})</i>\n"
                                   f"", parse_mode=telegram.ParseMode.HTML)


def priceB(update, context):
    r = requests.get(url="https://api.pancakeswap.info/api/v2/tokens/0xe1DB3d1eE5CfE5C6333BE96e6421f9Bd5b85c987")

    response = r.json()

    name = response['data']['name']
    p_price = float(response['data']['price']) * 1e6
    p_mcapp = round(650 * 1e6 * p_price)

    b_price = p_price - (p_price / 100 * 28)
    b_mcapp = round(p_mcapp - (p_mcapp / 100 * 28))
    b_market_cap = "{:,}".format(b_mcapp)

    update.message.reply_text(text=f"         🚀   {name}   🚀\n\n"
                                   f"  ~~   <i>BoggedFinance</i>  ~~  \n"
                                   f"💰  1M tokens: <b>${round(b_price, 8)}</b> \n"
                                   f"💴  Market cap: <b>${b_market_cap}</b> <i>({millify(b_mcapp)})</i>\n"
                                   f"", parse_mode=telegram.ParseMode.HTML)

def priceP(update, context):
    r = requests.get(url="https://api.pancakeswap.info/api/v2/tokens/0xe1DB3d1eE5CfE5C6333BE96e6421f9Bd5b85c987")

    response = r.json()

    name = response['data']['name']
    p_price = float(response['data']['price']) * 1e6
    p_mcapp = round(650 * 1e6 * p_price)
    p_market_cap = "{:,}".format(p_mcapp)

    update.message.reply_text(text=f"         🚀   {name}   🚀\n\n"
                                   f"  ~~   <i>Pancakeswap[v2]</i>  ~~  \n"
                                   f"💰  1M tokens: <b>${round(p_price, 8)}</b> \n"
                                   f"💴  Market cap: <b>${p_market_cap}</b> <i>({millify(p_mcapp)})</i>\n\n"
                                   f"", parse_mode=telegram.ParseMode.HTML)

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
    dp.add_handler(CommandHandler("price", price))
    dp.add_handler(CommandHandler("p", price))

    dp.add_handler(CommandHandler("price_bogged", priceB))
    dp.add_handler(CommandHandler("p_bogged", priceB))

    dp.add_handler(CommandHandler("price_pancake", priceP))
    dp.add_handler(CommandHandler("p_pancake", priceP))
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
