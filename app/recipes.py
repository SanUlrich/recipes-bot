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
