import telebot
from settings import *
from API import BlockcypherAPI

bot = telebot.TeleBot(API_TOKEN)
event = BlockcypherAPI()
