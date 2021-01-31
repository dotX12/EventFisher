import asyncio
from API.blockcypher import *
from scheduler.scheduler import Scheduler
import concurrent.futures
import telebot
from examples.teleBot import non_blocking

API_TOKEN = '1085642934:AAG9eNsHj2dsZlVup9bFhYLQJ7F_G8DuMjo'
ADMIN_ID = '227020931'

bot = telebot.TeleBot(API_TOKEN)
event = BlockcypherAPI()


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


loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.ensure_future(event.create_session()))
scheduler = Scheduler([event], loop)
executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)
loop.run_until_complete(non_blocking(loop, executor, bot.polling, scheduler.run_forever))
