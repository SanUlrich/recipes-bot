from app import keyboard
from app.core import bot
from app.recipes import BreakfastAnswer, LunchAnswer, DinnerAnswer


# class AnswerHandler:
#     answers = {
#         'breakfast': BreakfastAnswer,
#         'lunch': LunchAnswer,
#         'dinner': DinnerAnswer
#     }
#
#     def __init__(self, call):
#         self.call = call
#         self.answer_type = call.data
#
#     async def get_answer(self):
#         try:
#             recipe = self.answers[self.answer_type]
#         except KeyError:
#             await bot.send_message(self.call.from_user.id, 'Это я еще не обрабатываю')
#         else:
#             recipe_data = recipe().get_id()
#             await bot.send_message(self.call.from_user.id,
#                                    f'https://www.russianfood.com/recipes/recipe.php?rid={recipe_data}',
#                                    reply_markup=keyboard.lss_kb)
