import random

from aiogram import types
from aiogram.utils import executor

from app.recipes import Button
from data import breakfast, lunch, dinner
from app import keyboard
# from app.handlers import AnswerHandler
from app.core import dp, bot


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(f'<b>Привет, {message.from_user.first_name}!</b>\n'
                         f'Стоишь в супермаркете и не знаешь что взять?\n'
                         f'Я могу предложить тебе рецепт, а ты уже купишь для него продукты.\n'
                         f'Жми <b>Быстрый рецепт</b>!',
                         reply_markup=keyboard.start_kb)


@dp.message_handler(commands=['help'])
async def cmd_help(message: types.Message):
    await message.answer('Я могу подсказать тебе что приготовить.\n'
                         '<b>Быстрый рецепт</b> - рандомный рецепт\n'
                         '<b>Больше опций</b> - выбрать время приёма пищи',
                         reply_markup=keyboard.start_kb)


@dp.callback_query_handler()
async def callback_answer(call):
    handler = Button(call)
    ans = str(handler.get_recipe(call.data))
    await bot.send_message(call.from_user.id, f'https://www.russianfood.com/recipes/recipe.php?rid={ans}')
    await call.answer()


@dp.message_handler(content_types=['text'])
async def get_option(message: types.Message):
    if message.text == 'Больше опций':
        await message.answer('На выбор 3 основных времени приёма пищи: ',
                             reply_markup=keyboard.options_kb)
    elif message.text == 'Быстрый рецепт':
        all_recipes = breakfast.list + lunch.list + dinner.list
        fast_id = str(all_recipes[random.randint(0, len(all_recipes))])
        await message.answer(f'https://www.russianfood.com/recipes/recipe.php?rid={fast_id}')
    else:
        await bot.send_message(message.from_user.id,
                               'Сорян, не умею по человечьи. Только <b>команды</b>\n'
                               'Если возникли проблемы, воспользуйся командой /help',
                               reply_markup=keyboard.start_kb)


if __name__ == '__main__':
    executor.start_polling(dp)
