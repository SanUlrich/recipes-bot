import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.environ.get('TOKEN')
bot = Bot(token=TOKEN, parse_mode='html')
dp = Dispatcher(bot)
