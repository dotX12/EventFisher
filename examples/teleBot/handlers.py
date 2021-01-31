from misc import *


@event.on('new_transaction')
def new_transaction():
    bot.send_message(ADMIN_ID, f'New Transaction! TX Hash: {event.tx["tx_hash"]}')


@event.on('new_btc_medium_fee')
def btc_new_price():
    bot.send_message(ADMIN_ID, f'BTC NEW MEDIUM FEE: {event.medium_fee}')


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "Hi there, I am EchoBot.")


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)