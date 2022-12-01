from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

# Кнопки основной клавиатуры
fast_recipe_button = KeyboardButton('Быстрый рецепт')
settings = KeyboardButton('Больше опций')

start_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
start_kb.add(settings, fast_recipe_button)

# Инлайновые кнопки
breakfast = InlineKeyboardButton('Завтрак', callback_data='breakfast')
lunch = InlineKeyboardButton('Обед', callback_data='lunch')
dinner = InlineKeyboardButton('Ужин', callback_data='dinner')

options_kb = InlineKeyboardMarkup()
options_kb.add(breakfast).add(lunch).add(dinner)

like = InlineKeyboardButton('❤', callback_data='like')
share = InlineKeyboardButton('📢', callback_data='share')
store = InlineKeyboardButton('⭐', callback_data='store')

lss_kb = InlineKeyboardMarkup()
lss_kb.add(store, share, like)