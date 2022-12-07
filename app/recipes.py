from data import breakfast, lunch, dinner
import random


class Button:
    def __init__(self, callback_data):
        self.data = callback_data.data

    def get_recipe(self, data):
        s = {
            'breakfast': breakfast.list,
            'lunch': lunch.list,
            'dinner': dinner.list
        }
        try:
            recipe_id = str(s[data][random.randint(0, len(s[data]))])
        except AttributeError:
            print('nothing')
        else:
            return recipe_id


# class BreakfastAnswer:
#     @staticmethod
#     def get_id():
#         return str(breakfast.data[random.randint(0, len(breakfast.data))])
#
#
# class LunchAnswer:
#     @staticmethod
#     def get_id():
#         return str(lunch.data[random.randint(0, len(lunch.data))])
#
#
# class DinnerAnswer:
#     @staticmethod
#     def get_id():
#         return str(dinner.data[random.randint(0, len(dinner.data))])

