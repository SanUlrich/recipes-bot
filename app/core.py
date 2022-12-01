from aiogram import Bot, Dispatcher

from app.config import TOKEN


bot = Bot(token=TOKEN, parse_mode='html')
dp = Dispatcher(bot)

